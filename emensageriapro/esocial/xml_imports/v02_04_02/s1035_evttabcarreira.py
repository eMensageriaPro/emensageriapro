#coding:utf-8
"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos<www.emensageria.com.br>
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


def read_s1035_evttabcarreira(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    read_s1035_evttabcarreira_obj(doc, status)



def read_s1035_evttabcarreira_obj(doc):
    s1035_evttabcarreira_dados = {}
    s1035_evttabcarreira_dados['versao'] = 'v02_04_02'
    s1035_evttabcarreira_dados['status'] = status
    s1035_evttabcarreira_dados['identidade'] = doc.eSocial.evtTabCarreira['Id']
    s1035_evttabcarreira_dados['processamento_codigo_resposta'] = 1
    evtTabCarreira = doc.eSocial.evtTabCarreira
    
    if 'tpAmb' in dir(evtTabCarreira.ideEvento): s1035_evttabcarreira_dados['tpamb'] = evtTabCarreira.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTabCarreira.ideEvento): s1035_evttabcarreira_dados['procemi'] = evtTabCarreira.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTabCarreira.ideEvento): s1035_evttabcarreira_dados['verproc'] = evtTabCarreira.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTabCarreira.ideEmpregador): s1035_evttabcarreira_dados['tpinsc'] = evtTabCarreira.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTabCarreira.ideEmpregador): s1035_evttabcarreira_dados['nrinsc'] = evtTabCarreira.ideEmpregador.nrInsc.cdata
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
    dados['status'] = 1

    if 'inclusao' in dir(evtTabCarreira.infoCarreira):
        for inclusao in evtTabCarreira.infoCarreira.inclusao:
            s1035_inclusao_dados = {}
            s1035_inclusao_dados['s1035_evttabcarreira_id'] = s1035_evttabcarreira_id
            
            if 'codCarreira' in dir(inclusao.ideCarreira): s1035_inclusao_dados['codcarreira'] = inclusao.ideCarreira.codCarreira.cdata
            if 'iniValid' in dir(inclusao.ideCarreira): s1035_inclusao_dados['inivalid'] = inclusao.ideCarreira.iniValid.cdata
            if 'fimValid' in dir(inclusao.ideCarreira): s1035_inclusao_dados['fimvalid'] = inclusao.ideCarreira.fimValid.cdata
            if 'dscCarreira' in dir(inclusao.dadosCarreira): s1035_inclusao_dados['dsccarreira'] = inclusao.dadosCarreira.dscCarreira.cdata
            if 'leiCarr' in dir(inclusao.dadosCarreira): s1035_inclusao_dados['leicarr'] = inclusao.dadosCarreira.leiCarr.cdata
            if 'dtLeiCarr' in dir(inclusao.dadosCarreira): s1035_inclusao_dados['dtleicarr'] = inclusao.dadosCarreira.dtLeiCarr.cdata
            if 'sitCarr' in dir(inclusao.dadosCarreira): s1035_inclusao_dados['sitcarr'] = inclusao.dadosCarreira.sitCarr.cdata
            insert = create_insert('s1035_inclusao', s1035_inclusao_dados)
            resp = executar_sql(insert, True)
            s1035_inclusao_id = resp[0][0]
            #print s1035_inclusao_id

    if 'alteracao' in dir(evtTabCarreira.infoCarreira):
        for alteracao in evtTabCarreira.infoCarreira.alteracao:
            s1035_alteracao_dados = {}
            s1035_alteracao_dados['s1035_evttabcarreira_id'] = s1035_evttabcarreira_id
            
            if 'codCarreira' in dir(alteracao.ideCarreira): s1035_alteracao_dados['codcarreira'] = alteracao.ideCarreira.codCarreira.cdata
            if 'iniValid' in dir(alteracao.ideCarreira): s1035_alteracao_dados['inivalid'] = alteracao.ideCarreira.iniValid.cdata
            if 'fimValid' in dir(alteracao.ideCarreira): s1035_alteracao_dados['fimvalid'] = alteracao.ideCarreira.fimValid.cdata
            if 'dscCarreira' in dir(alteracao.dadosCarreira): s1035_alteracao_dados['dsccarreira'] = alteracao.dadosCarreira.dscCarreira.cdata
            if 'leiCarr' in dir(alteracao.dadosCarreira): s1035_alteracao_dados['leicarr'] = alteracao.dadosCarreira.leiCarr.cdata
            if 'dtLeiCarr' in dir(alteracao.dadosCarreira): s1035_alteracao_dados['dtleicarr'] = alteracao.dadosCarreira.dtLeiCarr.cdata
            if 'sitCarr' in dir(alteracao.dadosCarreira): s1035_alteracao_dados['sitcarr'] = alteracao.dadosCarreira.sitCarr.cdata
            insert = create_insert('s1035_alteracao', s1035_alteracao_dados)
            resp = executar_sql(insert, True)
            s1035_alteracao_id = resp[0][0]
            #print s1035_alteracao_id

            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    s1035_alteracao_novavalidade_dados = {}
                    s1035_alteracao_novavalidade_dados['s1035_alteracao_id'] = s1035_alteracao_id
                    
                    if 'iniValid' in dir(novaValidade): s1035_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    if 'fimValid' in dir(novaValidade): s1035_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    insert = create_insert('s1035_alteracao_novavalidade', s1035_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1035_alteracao_novavalidade_id = resp[0][0]
                    #print s1035_alteracao_novavalidade_id
        
    if 'exclusao' in dir(evtTabCarreira.infoCarreira):
        for exclusao in evtTabCarreira.infoCarreira.exclusao:
            s1035_exclusao_dados = {}
            s1035_exclusao_dados['s1035_evttabcarreira_id'] = s1035_evttabcarreira_id
            
            if 'codCarreira' in dir(exclusao.ideCarreira): s1035_exclusao_dados['codcarreira'] = exclusao.ideCarreira.codCarreira.cdata
            if 'iniValid' in dir(exclusao.ideCarreira): s1035_exclusao_dados['inivalid'] = exclusao.ideCarreira.iniValid.cdata
            if 'fimValid' in dir(exclusao.ideCarreira): s1035_exclusao_dados['fimvalid'] = exclusao.ideCarreira.fimValid.cdata
            insert = create_insert('s1035_exclusao', s1035_exclusao_dados)
            resp = executar_sql(insert, True)
            s1035_exclusao_id = resp[0][0]
            #print s1035_exclusao_id

    from emensageriapro.esocial.views.s1035_evttabcarreira_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1035_evttabcarreira_id, 'default')
    return dados