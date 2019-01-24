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


def read_s2241_evtinsapo_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2241_evtinsapo_obj(doc, status, validar)
    return dados

def read_s2241_evtinsapo(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2241_evtinsapo_obj(doc, status, validar)
    return dados



def read_s2241_evtinsapo_obj(doc, status, validar=False):
    s2241_evtinsapo_dados = {}
    s2241_evtinsapo_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2241_evtinsapo_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
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

    if 'iniInsalPeric' in dir(evtInsApo.insalPeric):
        for iniInsalPeric in evtInsApo.insalPeric.iniInsalPeric:
            s2241_iniinsalperic_dados = {}
            s2241_iniinsalperic_dados['s2241_evtinsapo_id'] = s2241_evtinsapo_id

            if 'dtIniCondicao' in dir(iniInsalPeric): s2241_iniinsalperic_dados['dtinicondicao'] = iniInsalPeric.dtIniCondicao.cdata
            insert = create_insert('s2241_iniinsalperic', s2241_iniinsalperic_dados)
            resp = executar_sql(insert, True)
            s2241_iniinsalperic_id = resp[0][0]
            #print s2241_iniinsalperic_id

            if 'infoAmb' in dir(iniInsalPeric):
                for infoAmb in iniInsalPeric.infoAmb:
                    s2241_iniinsalperic_infoamb_dados = {}
                    s2241_iniinsalperic_infoamb_dados['s2241_iniinsalperic_id'] = s2241_iniinsalperic_id

                    if 'codAmb' in dir(infoAmb): s2241_iniinsalperic_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
                    insert = create_insert('s2241_iniinsalperic_infoamb', s2241_iniinsalperic_infoamb_dados)
                    resp = executar_sql(insert, True)
                    s2241_iniinsalperic_infoamb_id = resp[0][0]
                    #print s2241_iniinsalperic_infoamb_id

    if 'altInsalPeric' in dir(evtInsApo.insalPeric):
        for altInsalPeric in evtInsApo.insalPeric.altInsalPeric:
            s2241_altinsalperic_dados = {}
            s2241_altinsalperic_dados['s2241_evtinsapo_id'] = s2241_evtinsapo_id

            if 'dtAltCondicao' in dir(altInsalPeric): s2241_altinsalperic_dados['dtaltcondicao'] = altInsalPeric.dtAltCondicao.cdata
            insert = create_insert('s2241_altinsalperic', s2241_altinsalperic_dados)
            resp = executar_sql(insert, True)
            s2241_altinsalperic_id = resp[0][0]
            #print s2241_altinsalperic_id

            if 'infoamb' in dir(altInsalPeric):
                for infoamb in altInsalPeric.infoamb:
                    s2241_altinsalperic_infoamb_dados = {}
                    s2241_altinsalperic_infoamb_dados['s2241_altinsalperic_id'] = s2241_altinsalperic_id

                    if 'codAmb' in dir(infoamb): s2241_altinsalperic_infoamb_dados['codamb'] = infoamb.codAmb.cdata
                    insert = create_insert('s2241_altinsalperic_infoamb', s2241_altinsalperic_infoamb_dados)
                    resp = executar_sql(insert, True)
                    s2241_altinsalperic_infoamb_id = resp[0][0]
                    #print s2241_altinsalperic_infoamb_id

    if 'fimInsalPeric' in dir(evtInsApo.insalPeric):
        for fimInsalPeric in evtInsApo.insalPeric.fimInsalPeric:
            s2241_fiminsalperic_dados = {}
            s2241_fiminsalperic_dados['s2241_evtinsapo_id'] = s2241_evtinsapo_id

            if 'dtFimCondicao' in dir(fimInsalPeric): s2241_fiminsalperic_dados['dtfimcondicao'] = fimInsalPeric.dtFimCondicao.cdata
            insert = create_insert('s2241_fiminsalperic', s2241_fiminsalperic_dados)
            resp = executar_sql(insert, True)
            s2241_fiminsalperic_id = resp[0][0]
            #print s2241_fiminsalperic_id

            if 'infoAmb' in dir(fimInsalPeric):
                for infoAmb in fimInsalPeric.infoAmb:
                    s2241_fiminsalperic_infoamb_dados = {}
                    s2241_fiminsalperic_infoamb_dados['s2241_fiminsalperic_id'] = s2241_fiminsalperic_id

                    if 'codAmb' in dir(infoAmb): s2241_fiminsalperic_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
                    insert = create_insert('s2241_fiminsalperic_infoamb', s2241_fiminsalperic_infoamb_dados)
                    resp = executar_sql(insert, True)
                    s2241_fiminsalperic_infoamb_id = resp[0][0]
                    #print s2241_fiminsalperic_infoamb_id

    if 'iniAposentEsp' in dir(evtInsApo.aposentEsp):
        for iniAposentEsp in evtInsApo.aposentEsp.iniAposentEsp:
            s2241_iniaposentesp_dados = {}
            s2241_iniaposentesp_dados['s2241_evtinsapo_id'] = s2241_evtinsapo_id

            if 'dtIniCondicao' in dir(iniAposentEsp): s2241_iniaposentesp_dados['dtinicondicao'] = iniAposentEsp.dtIniCondicao.cdata
            insert = create_insert('s2241_iniaposentesp', s2241_iniaposentesp_dados)
            resp = executar_sql(insert, True)
            s2241_iniaposentesp_id = resp[0][0]
            #print s2241_iniaposentesp_id

            if 'infoAmb' in dir(iniAposentEsp):
                for infoAmb in iniAposentEsp.infoAmb:
                    s2241_iniaposentesp_infoamb_dados = {}
                    s2241_iniaposentesp_infoamb_dados['s2241_iniaposentesp_id'] = s2241_iniaposentesp_id

                    if 'codAmb' in dir(infoAmb): s2241_iniaposentesp_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
                    insert = create_insert('s2241_iniaposentesp_infoamb', s2241_iniaposentesp_infoamb_dados)
                    resp = executar_sql(insert, True)
                    s2241_iniaposentesp_infoamb_id = resp[0][0]
                    #print s2241_iniaposentesp_infoamb_id

    if 'altAposentEsp' in dir(evtInsApo.aposentEsp):
        for altAposentEsp in evtInsApo.aposentEsp.altAposentEsp:
            s2241_altaposentesp_dados = {}
            s2241_altaposentesp_dados['s2241_evtinsapo_id'] = s2241_evtinsapo_id

            if 'dtAltCondicao' in dir(altAposentEsp): s2241_altaposentesp_dados['dtaltcondicao'] = altAposentEsp.dtAltCondicao.cdata
            insert = create_insert('s2241_altaposentesp', s2241_altaposentesp_dados)
            resp = executar_sql(insert, True)
            s2241_altaposentesp_id = resp[0][0]
            #print s2241_altaposentesp_id

            if 'infoamb' in dir(altAposentEsp):
                for infoamb in altAposentEsp.infoamb:
                    s2241_altaposentesp_infoamb_dados = {}
                    s2241_altaposentesp_infoamb_dados['s2241_altaposentesp_id'] = s2241_altaposentesp_id

                    if 'codAmb' in dir(infoamb): s2241_altaposentesp_infoamb_dados['codamb'] = infoamb.codAmb.cdata
                    insert = create_insert('s2241_altaposentesp_infoamb', s2241_altaposentesp_infoamb_dados)
                    resp = executar_sql(insert, True)
                    s2241_altaposentesp_infoamb_id = resp[0][0]
                    #print s2241_altaposentesp_infoamb_id

    if 'fimAposentEsp' in dir(evtInsApo.aposentEsp):
        for fimAposentEsp in evtInsApo.aposentEsp.fimAposentEsp:
            s2241_fimaposentesp_dados = {}
            s2241_fimaposentesp_dados['s2241_evtinsapo_id'] = s2241_evtinsapo_id

            if 'dtFimCondicao' in dir(fimAposentEsp): s2241_fimaposentesp_dados['dtfimcondicao'] = fimAposentEsp.dtFimCondicao.cdata
            insert = create_insert('s2241_fimaposentesp', s2241_fimaposentesp_dados)
            resp = executar_sql(insert, True)
            s2241_fimaposentesp_id = resp[0][0]
            #print s2241_fimaposentesp_id

            if 'infoAmb' in dir(fimAposentEsp):
                for infoAmb in fimAposentEsp.infoAmb:
                    s2241_fimaposentesp_infoamb_dados = {}
                    s2241_fimaposentesp_infoamb_dados['s2241_fimaposentesp_id'] = s2241_fimaposentesp_id

                    if 'codAmb' in dir(infoAmb): s2241_fimaposentesp_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
                    insert = create_insert('s2241_fimaposentesp_infoamb', s2241_fimaposentesp_infoamb_dados)
                    resp = executar_sql(insert, True)
                    s2241_fimaposentesp_infoamb_id = resp[0][0]
                    #print s2241_fimaposentesp_infoamb_id

    from emensageriapro.esocial.views.s2241_evtinsapo_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2241_evtinsapo_id, 'default')
    return dados