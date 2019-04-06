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



def read_s1035_evttabcarreira_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1035_evttabcarreira_obj(doc, status, validar)
    return dados

def read_s1035_evttabcarreira(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1035_evttabcarreira_obj(doc, status, validar)
    return dados



def read_s1035_evttabcarreira_obj(doc, status, validar=False):
    s1035_evttabcarreira_dados = {}
    s1035_evttabcarreira_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1035_evttabcarreira_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1035_evttabcarreira_dados['identidade'] = doc.eSocial.evtTabCarreira['Id']
    evtTabCarreira = doc.eSocial.evtTabCarreira

    try: s1035_evttabcarreira_dados['tpamb'] = evtTabCarreira.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s1035_evttabcarreira_dados['procemi'] = evtTabCarreira.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s1035_evttabcarreira_dados['verproc'] = evtTabCarreira.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s1035_evttabcarreira_dados['tpinsc'] = evtTabCarreira.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s1035_evttabcarreira_dados['nrinsc'] = evtTabCarreira.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtTabCarreira.infoCarreira): s1035_evttabcarreira_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabCarreira.infoCarreira): s1035_evttabcarreira_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabCarreira.infoCarreira): s1035_evttabcarreira_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1035_evttabcarreira', s1035_evttabcarreira_dados)
    resp = executar_sql(insert, True)
    s1035_evttabcarreira_id = resp[0][0]
    dados = s1035_evttabcarreira_dados
    dados['evento'] = 's1035'
    dados['id'] = s1035_evttabcarreira_id
    dados['identidade_evento'] = doc.eSocial.evtTabCarreira['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'inclusao' in dir(evtTabCarreira.infoCarreira) and evtTabCarreira.infoCarreira.inclusao.cdata != '':
        for inclusao in evtTabCarreira.infoCarreira.inclusao:
            s1035_inclusao_dados = {}
            s1035_inclusao_dados['s1035_evttabcarreira_id'] = s1035_evttabcarreira_id

            try: s1035_inclusao_dados['codcarreira'] = inclusao.ideCarreira.codCarreira.cdata
            except AttributeError: pass
            try: s1035_inclusao_dados['inivalid'] = inclusao.ideCarreira.iniValid.cdata
            except AttributeError: pass
            try: s1035_inclusao_dados['fimvalid'] = inclusao.ideCarreira.fimValid.cdata
            except AttributeError: pass
            try: s1035_inclusao_dados['dsccarreira'] = inclusao.dadosCarreira.dscCarreira.cdata
            except AttributeError: pass
            try: s1035_inclusao_dados['leicarr'] = inclusao.dadosCarreira.leiCarr.cdata
            except AttributeError: pass
            try: s1035_inclusao_dados['dtleicarr'] = inclusao.dadosCarreira.dtLeiCarr.cdata
            except AttributeError: pass
            try: s1035_inclusao_dados['sitcarr'] = inclusao.dadosCarreira.sitCarr.cdata
            except AttributeError: pass
            insert = create_insert('s1035_inclusao', s1035_inclusao_dados)
            resp = executar_sql(insert, True)
            s1035_inclusao_id = resp[0][0]
            #print s1035_inclusao_id

    if 'alteracao' in dir(evtTabCarreira.infoCarreira) and evtTabCarreira.infoCarreira.alteracao.cdata != '':
        for alteracao in evtTabCarreira.infoCarreira.alteracao:
            s1035_alteracao_dados = {}
            s1035_alteracao_dados['s1035_evttabcarreira_id'] = s1035_evttabcarreira_id

            try: s1035_alteracao_dados['codcarreira'] = alteracao.ideCarreira.codCarreira.cdata
            except AttributeError: pass
            try: s1035_alteracao_dados['inivalid'] = alteracao.ideCarreira.iniValid.cdata
            except AttributeError: pass
            try: s1035_alteracao_dados['fimvalid'] = alteracao.ideCarreira.fimValid.cdata
            except AttributeError: pass
            try: s1035_alteracao_dados['dsccarreira'] = alteracao.dadosCarreira.dscCarreira.cdata
            except AttributeError: pass
            try: s1035_alteracao_dados['leicarr'] = alteracao.dadosCarreira.leiCarr.cdata
            except AttributeError: pass
            try: s1035_alteracao_dados['dtleicarr'] = alteracao.dadosCarreira.dtLeiCarr.cdata
            except AttributeError: pass
            try: s1035_alteracao_dados['sitcarr'] = alteracao.dadosCarreira.sitCarr.cdata
            except AttributeError: pass
            insert = create_insert('s1035_alteracao', s1035_alteracao_dados)
            resp = executar_sql(insert, True)
            s1035_alteracao_id = resp[0][0]
            #print s1035_alteracao_id

            if 'novaValidade' in dir(alteracao) and alteracao.novaValidade.cdata != '':
                for novaValidade in alteracao.novaValidade:
                    s1035_alteracao_novavalidade_dados = {}
                    s1035_alteracao_novavalidade_dados['s1035_alteracao_id'] = s1035_alteracao_id

                    try: s1035_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError: pass
                    try: s1035_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError: pass
                    insert = create_insert('s1035_alteracao_novavalidade', s1035_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1035_alteracao_novavalidade_id = resp[0][0]
                    #print s1035_alteracao_novavalidade_id

    if 'exclusao' in dir(evtTabCarreira.infoCarreira) and evtTabCarreira.infoCarreira.exclusao.cdata != '':
        for exclusao in evtTabCarreira.infoCarreira.exclusao:
            s1035_exclusao_dados = {}
            s1035_exclusao_dados['s1035_evttabcarreira_id'] = s1035_evttabcarreira_id

            try: s1035_exclusao_dados['codcarreira'] = exclusao.ideCarreira.codCarreira.cdata
            except AttributeError: pass
            try: s1035_exclusao_dados['inivalid'] = exclusao.ideCarreira.iniValid.cdata
            except AttributeError: pass
            try: s1035_exclusao_dados['fimvalid'] = exclusao.ideCarreira.fimValid.cdata
            except AttributeError: pass
            insert = create_insert('s1035_exclusao', s1035_exclusao_dados)
            resp = executar_sql(insert, True)
            s1035_exclusao_id = resp[0][0]
            #print s1035_exclusao_id

    from emensageriapro.esocial.views.s1035_evttabcarreira_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1035_evttabcarreira_id, 'default')
    return dados