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


def read_s2241_evtinsapo(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    read_s2241_evtinsapo_obj(doc, status)



def read_s2241_evtinsapo_obj(doc):
    s2241_evtinsapo_dados = {}
    s2241_evtinsapo_dados['versao'] = 'v02_04_02'
    s2241_evtinsapo_dados['status'] = status
    s2241_evtinsapo_dados['identidade'] = doc.eSocial.evtInsApo['Id']
    s2241_evtinsapo_dados['processamento_codigo_resposta'] = 1
    evtInsApo = doc.eSocial.evtInsApo
    
    if 'indRetif' in dir(evtInsApo.ideEvento): s2241_evtinsapo_dados['indretif'] = evtInsApo.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtInsApo.ideEvento): s2241_evtinsapo_dados['nrrecibo'] = evtInsApo.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtInsApo.ideEvento): s2241_evtinsapo_dados['tpamb'] = evtInsApo.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtInsApo.ideEvento): s2241_evtinsapo_dados['procemi'] = evtInsApo.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtInsApo.ideEvento): s2241_evtinsapo_dados['verproc'] = evtInsApo.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtInsApo.ideEmpregador): s2241_evtinsapo_dados['tpinsc'] = evtInsApo.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtInsApo.ideEmpregador): s2241_evtinsapo_dados['nrinsc'] = evtInsApo.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtInsApo.ideVinculo): s2241_evtinsapo_dados['cpftrab'] = evtInsApo.ideVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtInsApo.ideVinculo): s2241_evtinsapo_dados['nistrab'] = evtInsApo.ideVinculo.nisTrab.cdata
    if 'matricula' in dir(evtInsApo.ideVinculo): s2241_evtinsapo_dados['matricula'] = evtInsApo.ideVinculo.matricula.cdata
    if 'inclusao' in dir(evtInsApo.aposentEsp): s2241_evtinsapo_dados['operacao'] = 1
    elif 'alteracao' in dir(evtInsApo.aposentEsp): s2241_evtinsapo_dados['operacao'] = 2
    elif 'exclusao' in dir(evtInsApo.aposentEsp): s2241_evtinsapo_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2241_evtinsapo', s2241_evtinsapo_dados)
    resp = executar_sql(insert, True)
    s2241_evtinsapo_id = resp[0][0]
    dados = s2241_evtinsapo_dados
    dados['evento'] = 's2241'
    dados['id'] = s2241_evtinsapo_id
    dados['identidade_evento'] = doc.eSocial.evtInsApo['Id']
    dados['status'] = 1

    if 'insalPeric' in dir(evtInsApo):
        for insalPeric in evtInsApo.insalPeric:
            s2241_insalperic_dados = {}
            s2241_insalperic_dados['s2241_evtinsapo_id'] = s2241_evtinsapo_id
            
            insert = create_insert('s2241_insalperic', s2241_insalperic_dados)
            resp = executar_sql(insert, True)
            s2241_insalperic_id = resp[0][0]
            #print s2241_insalperic_id

            if 'iniInsalPeric' in dir(insalPeric):
                for iniInsalPeric in insalPeric.iniInsalPeric:
                    s2241_iniinsalperic_dados = {}
                    s2241_iniinsalperic_dados['s2241_insalperic_id'] = s2241_insalperic_id
                    
                    if 'dtIniCondicao' in dir(iniInsalPeric): s2241_iniinsalperic_dados['dtinicondicao'] = iniInsalPeric.dtIniCondicao.cdata
                    insert = create_insert('s2241_iniinsalperic', s2241_iniinsalperic_dados)
                    resp = executar_sql(insert, True)
                    s2241_iniinsalperic_id = resp[0][0]
                    #print s2241_iniinsalperic_id
        
            if 'altInsalPeric' in dir(insalPeric):
                for altInsalPeric in insalPeric.altInsalPeric:
                    s2241_altinsalperic_dados = {}
                    s2241_altinsalperic_dados['s2241_insalperic_id'] = s2241_insalperic_id
                    
                    if 'dtAltCondicao' in dir(altInsalPeric): s2241_altinsalperic_dados['dtaltcondicao'] = altInsalPeric.dtAltCondicao.cdata
                    insert = create_insert('s2241_altinsalperic', s2241_altinsalperic_dados)
                    resp = executar_sql(insert, True)
                    s2241_altinsalperic_id = resp[0][0]
                    #print s2241_altinsalperic_id
        
            if 'fimInsalPeric' in dir(insalPeric):
                for fimInsalPeric in insalPeric.fimInsalPeric:
                    s2241_fiminsalperic_dados = {}
                    s2241_fiminsalperic_dados['s2241_insalperic_id'] = s2241_insalperic_id
                    
                    if 'dtFimCondicao' in dir(fimInsalPeric): s2241_fiminsalperic_dados['dtfimcondicao'] = fimInsalPeric.dtFimCondicao.cdata
                    insert = create_insert('s2241_fiminsalperic', s2241_fiminsalperic_dados)
                    resp = executar_sql(insert, True)
                    s2241_fiminsalperic_id = resp[0][0]
                    #print s2241_fiminsalperic_id
        
    if 'aposentEsp' in dir(evtInsApo):
        for aposentEsp in evtInsApo.aposentEsp:
            s2241_aposentesp_dados = {}
            s2241_aposentesp_dados['s2241_evtinsapo_id'] = s2241_evtinsapo_id
            
            insert = create_insert('s2241_aposentesp', s2241_aposentesp_dados)
            resp = executar_sql(insert, True)
            s2241_aposentesp_id = resp[0][0]
            #print s2241_aposentesp_id

            if 'iniAposentEsp' in dir(aposentEsp):
                for iniAposentEsp in aposentEsp.iniAposentEsp:
                    s2241_iniaposentesp_dados = {}
                    s2241_iniaposentesp_dados['s2241_aposentesp_id'] = s2241_aposentesp_id
                    
                    if 'dtIniCondicao' in dir(iniAposentEsp): s2241_iniaposentesp_dados['dtinicondicao'] = iniAposentEsp.dtIniCondicao.cdata
                    insert = create_insert('s2241_iniaposentesp', s2241_iniaposentesp_dados)
                    resp = executar_sql(insert, True)
                    s2241_iniaposentesp_id = resp[0][0]
                    #print s2241_iniaposentesp_id
        
            if 'altAposentEsp' in dir(aposentEsp):
                for altAposentEsp in aposentEsp.altAposentEsp:
                    s2241_altaposentesp_dados = {}
                    s2241_altaposentesp_dados['s2241_aposentesp_id'] = s2241_aposentesp_id
                    
                    if 'dtAltCondicao' in dir(altAposentEsp): s2241_altaposentesp_dados['dtaltcondicao'] = altAposentEsp.dtAltCondicao.cdata
                    insert = create_insert('s2241_altaposentesp', s2241_altaposentesp_dados)
                    resp = executar_sql(insert, True)
                    s2241_altaposentesp_id = resp[0][0]
                    #print s2241_altaposentesp_id
        
            if 'fimAposentEsp' in dir(aposentEsp):
                for fimAposentEsp in aposentEsp.fimAposentEsp:
                    s2241_fimaposentesp_dados = {}
                    s2241_fimaposentesp_dados['s2241_aposentesp_id'] = s2241_aposentesp_id
                    
                    if 'dtFimCondicao' in dir(fimAposentEsp): s2241_fimaposentesp_dados['dtfimcondicao'] = fimAposentEsp.dtFimCondicao.cdata
                    insert = create_insert('s2241_fimaposentesp', s2241_fimaposentesp_dados)
                    resp = executar_sql(insert, True)
                    s2241_fimaposentesp_id = resp[0][0]
                    #print s2241_fimaposentesp_id
        
    from emensageriapro.esocial.views.s2241_evtinsapo_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2241_evtinsapo_id, 'default')
    return dados