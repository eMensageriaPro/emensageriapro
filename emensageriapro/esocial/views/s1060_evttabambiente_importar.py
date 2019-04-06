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



def read_s1060_evttabambiente_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1060_evttabambiente_obj(doc, status, validar)
    return dados

def read_s1060_evttabambiente(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1060_evttabambiente_obj(doc, status, validar)
    return dados



def read_s1060_evttabambiente_obj(doc, status, validar=False):
    s1060_evttabambiente_dados = {}
    s1060_evttabambiente_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1060_evttabambiente_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1060_evttabambiente_dados['identidade'] = doc.eSocial.evtTabAmbiente['Id']
    evtTabAmbiente = doc.eSocial.evtTabAmbiente

    try: s1060_evttabambiente_dados['tpamb'] = evtTabAmbiente.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s1060_evttabambiente_dados['procemi'] = evtTabAmbiente.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s1060_evttabambiente_dados['verproc'] = evtTabAmbiente.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s1060_evttabambiente_dados['tpinsc'] = evtTabAmbiente.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s1060_evttabambiente_dados['nrinsc'] = evtTabAmbiente.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtTabAmbiente.infoAmbiente): s1060_evttabambiente_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabAmbiente.infoAmbiente): s1060_evttabambiente_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabAmbiente.infoAmbiente): s1060_evttabambiente_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1060_evttabambiente', s1060_evttabambiente_dados)
    resp = executar_sql(insert, True)
    s1060_evttabambiente_id = resp[0][0]
    dados = s1060_evttabambiente_dados
    dados['evento'] = 's1060'
    dados['id'] = s1060_evttabambiente_id
    dados['identidade_evento'] = doc.eSocial.evtTabAmbiente['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'inclusao' in dir(evtTabAmbiente.infoAmbiente) and evtTabAmbiente.infoAmbiente.inclusao.cdata != '':
        for inclusao in evtTabAmbiente.infoAmbiente.inclusao:
            s1060_inclusao_dados = {}
            s1060_inclusao_dados['s1060_evttabambiente_id'] = s1060_evttabambiente_id

            try: s1060_inclusao_dados['codamb'] = inclusao.ideAmbiente.codAmb.cdata
            except AttributeError: pass
            try: s1060_inclusao_dados['inivalid'] = inclusao.ideAmbiente.iniValid.cdata
            except AttributeError: pass
            try: s1060_inclusao_dados['fimvalid'] = inclusao.ideAmbiente.fimValid.cdata
            except AttributeError: pass
            try: s1060_inclusao_dados['nmamb'] = inclusao.dadosAmbiente.nmAmb.cdata
            except AttributeError: pass
            try: s1060_inclusao_dados['dscamb'] = inclusao.dadosAmbiente.dscAmb.cdata
            except AttributeError: pass
            try: s1060_inclusao_dados['localamb'] = inclusao.dadosAmbiente.localAmb.cdata
            except AttributeError: pass
            try: s1060_inclusao_dados['tpinsc'] = inclusao.dadosAmbiente.tpInsc.cdata
            except AttributeError: pass
            try: s1060_inclusao_dados['nrinsc'] = inclusao.dadosAmbiente.nrInsc.cdata
            except AttributeError: pass
            try: s1060_inclusao_dados['codlotacao'] = inclusao.dadosAmbiente.codLotacao.cdata
            except AttributeError: pass
            insert = create_insert('s1060_inclusao', s1060_inclusao_dados)
            resp = executar_sql(insert, True)
            s1060_inclusao_id = resp[0][0]
            #print s1060_inclusao_id

    if 'alteracao' in dir(evtTabAmbiente.infoAmbiente) and evtTabAmbiente.infoAmbiente.alteracao.cdata != '':
        for alteracao in evtTabAmbiente.infoAmbiente.alteracao:
            s1060_alteracao_dados = {}
            s1060_alteracao_dados['s1060_evttabambiente_id'] = s1060_evttabambiente_id

            try: s1060_alteracao_dados['codamb'] = alteracao.ideAmbiente.codAmb.cdata
            except AttributeError: pass
            try: s1060_alteracao_dados['inivalid'] = alteracao.ideAmbiente.iniValid.cdata
            except AttributeError: pass
            try: s1060_alteracao_dados['fimvalid'] = alteracao.ideAmbiente.fimValid.cdata
            except AttributeError: pass
            try: s1060_alteracao_dados['nmamb'] = alteracao.dadosAmbiente.nmAmb.cdata
            except AttributeError: pass
            try: s1060_alteracao_dados['dscamb'] = alteracao.dadosAmbiente.dscAmb.cdata
            except AttributeError: pass
            try: s1060_alteracao_dados['localamb'] = alteracao.dadosAmbiente.localAmb.cdata
            except AttributeError: pass
            try: s1060_alteracao_dados['tpinsc'] = alteracao.dadosAmbiente.tpInsc.cdata
            except AttributeError: pass
            try: s1060_alteracao_dados['nrinsc'] = alteracao.dadosAmbiente.nrInsc.cdata
            except AttributeError: pass
            try: s1060_alteracao_dados['codlotacao'] = alteracao.dadosAmbiente.codLotacao.cdata
            except AttributeError: pass
            insert = create_insert('s1060_alteracao', s1060_alteracao_dados)
            resp = executar_sql(insert, True)
            s1060_alteracao_id = resp[0][0]
            #print s1060_alteracao_id

            if 'novaValidade' in dir(alteracao) and alteracao.novaValidade.cdata != '':
                for novaValidade in alteracao.novaValidade:
                    s1060_alteracao_novavalidade_dados = {}
                    s1060_alteracao_novavalidade_dados['s1060_alteracao_id'] = s1060_alteracao_id

                    try: s1060_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError: pass
                    try: s1060_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError: pass
                    insert = create_insert('s1060_alteracao_novavalidade', s1060_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1060_alteracao_novavalidade_id = resp[0][0]
                    #print s1060_alteracao_novavalidade_id

    if 'exclusao' in dir(evtTabAmbiente.infoAmbiente) and evtTabAmbiente.infoAmbiente.exclusao.cdata != '':
        for exclusao in evtTabAmbiente.infoAmbiente.exclusao:
            s1060_exclusao_dados = {}
            s1060_exclusao_dados['s1060_evttabambiente_id'] = s1060_evttabambiente_id

            try: s1060_exclusao_dados['codamb'] = exclusao.ideAmbiente.codAmb.cdata
            except AttributeError: pass
            try: s1060_exclusao_dados['inivalid'] = exclusao.ideAmbiente.iniValid.cdata
            except AttributeError: pass
            try: s1060_exclusao_dados['fimvalid'] = exclusao.ideAmbiente.fimValid.cdata
            except AttributeError: pass
            insert = create_insert('s1060_exclusao', s1060_exclusao_dados)
            resp = executar_sql(insert, True)
            s1060_exclusao_id = resp[0][0]
            #print s1060_exclusao_id

    from emensageriapro.esocial.views.s1060_evttabambiente_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1060_evttabambiente_id, 'default')
    return dados