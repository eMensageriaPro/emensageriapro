#coding:utf-8
"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO



def read_s1080_evttaboperport_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1080_evttaboperport_obj(doc, status, validar)
    return dados

def read_s1080_evttaboperport(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1080_evttaboperport_obj(doc, status, validar)
    return dados



def read_s1080_evttaboperport_obj(doc, status, validar=False):
    s1080_evttaboperport_dados = {}
    s1080_evttaboperport_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1080_evttaboperport_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1080_evttaboperport_dados['identidade'] = doc.eSocial.evtTabOperPort['Id']
    evtTabOperPort = doc.eSocial.evtTabOperPort

    try: s1080_evttaboperport_dados['tpamb'] = evtTabOperPort.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s1080_evttaboperport_dados['procemi'] = evtTabOperPort.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s1080_evttaboperport_dados['verproc'] = evtTabOperPort.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s1080_evttaboperport_dados['tpinsc'] = evtTabOperPort.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s1080_evttaboperport_dados['nrinsc'] = evtTabOperPort.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtTabOperPort.infoOperPortuario): s1080_evttaboperport_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabOperPort.infoOperPortuario): s1080_evttaboperport_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabOperPort.infoOperPortuario): s1080_evttaboperport_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1080_evttaboperport', s1080_evttaboperport_dados)
    resp = executar_sql(insert, True)
    s1080_evttaboperport_id = resp[0][0]
    dados = s1080_evttaboperport_dados
    dados['evento'] = 's1080'
    dados['id'] = s1080_evttaboperport_id
    dados['identidade_evento'] = doc.eSocial.evtTabOperPort['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'inclusao' in dir(evtTabOperPort.infoOperPortuario) and evtTabOperPort.infoOperPortuario.inclusao.cdata != '':
        for inclusao in evtTabOperPort.infoOperPortuario.inclusao:
            s1080_inclusao_dados = {}
            s1080_inclusao_dados['s1080_evttaboperport_id'] = s1080_evttaboperport_id

            try: s1080_inclusao_dados['cnpjopportuario'] = inclusao.ideOperPortuario.cnpjOpPortuario.cdata
            except AttributeError: pass
            try: s1080_inclusao_dados['inivalid'] = inclusao.ideOperPortuario.iniValid.cdata
            except AttributeError: pass
            try: s1080_inclusao_dados['fimvalid'] = inclusao.ideOperPortuario.fimValid.cdata
            except AttributeError: pass
            try: s1080_inclusao_dados['aliqrat'] = inclusao.dadosOperPortuario.aliqRat.cdata
            except AttributeError: pass
            try: s1080_inclusao_dados['fap'] = inclusao.dadosOperPortuario.fap.cdata
            except AttributeError: pass
            try: s1080_inclusao_dados['aliqratajust'] = inclusao.dadosOperPortuario.aliqRatAjust.cdata
            except AttributeError: pass
            insert = create_insert('s1080_inclusao', s1080_inclusao_dados)
            resp = executar_sql(insert, True)
            s1080_inclusao_id = resp[0][0]
            #print s1080_inclusao_id

    if 'alteracao' in dir(evtTabOperPort.infoOperPortuario) and evtTabOperPort.infoOperPortuario.alteracao.cdata != '':
        for alteracao in evtTabOperPort.infoOperPortuario.alteracao:
            s1080_alteracao_dados = {}
            s1080_alteracao_dados['s1080_evttaboperport_id'] = s1080_evttaboperport_id

            try: s1080_alteracao_dados['cnpjopportuario'] = alteracao.ideOperPortuario.cnpjOpPortuario.cdata
            except AttributeError: pass
            try: s1080_alteracao_dados['inivalid'] = alteracao.ideOperPortuario.iniValid.cdata
            except AttributeError: pass
            try: s1080_alteracao_dados['fimvalid'] = alteracao.ideOperPortuario.fimValid.cdata
            except AttributeError: pass
            try: s1080_alteracao_dados['aliqrat'] = alteracao.dadosOperPortuario.aliqRat.cdata
            except AttributeError: pass
            try: s1080_alteracao_dados['fap'] = alteracao.dadosOperPortuario.fap.cdata
            except AttributeError: pass
            try: s1080_alteracao_dados['aliqratajust'] = alteracao.dadosOperPortuario.aliqRatAjust.cdata
            except AttributeError: pass
            insert = create_insert('s1080_alteracao', s1080_alteracao_dados)
            resp = executar_sql(insert, True)
            s1080_alteracao_id = resp[0][0]
            #print s1080_alteracao_id

            if 'novaValidade' in dir(alteracao) and alteracao.novaValidade.cdata != '':
                for novaValidade in alteracao.novaValidade:
                    s1080_alteracao_novavalidade_dados = {}
                    s1080_alteracao_novavalidade_dados['s1080_alteracao_id'] = s1080_alteracao_id

                    try: s1080_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError: pass
                    try: s1080_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError: pass
                    insert = create_insert('s1080_alteracao_novavalidade', s1080_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1080_alteracao_novavalidade_id = resp[0][0]
                    #print s1080_alteracao_novavalidade_id

    if 'exclusao' in dir(evtTabOperPort.infoOperPortuario) and evtTabOperPort.infoOperPortuario.exclusao.cdata != '':
        for exclusao in evtTabOperPort.infoOperPortuario.exclusao:
            s1080_exclusao_dados = {}
            s1080_exclusao_dados['s1080_evttaboperport_id'] = s1080_evttaboperport_id

            try: s1080_exclusao_dados['cnpjopportuario'] = exclusao.ideOperPortuario.cnpjOpPortuario.cdata
            except AttributeError: pass
            try: s1080_exclusao_dados['inivalid'] = exclusao.ideOperPortuario.iniValid.cdata
            except AttributeError: pass
            try: s1080_exclusao_dados['fimvalid'] = exclusao.ideOperPortuario.fimValid.cdata
            except AttributeError: pass
            insert = create_insert('s1080_exclusao', s1080_exclusao_dados)
            resp = executar_sql(insert, True)
            s1080_exclusao_id = resp[0][0]
            #print s1080_exclusao_id

    from emensageriapro.esocial.views.s1080_evttaboperport_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1080_evttaboperport_id, 'default')
    return dados