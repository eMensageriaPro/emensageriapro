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


def read_s1270_evtcontratavnp(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    read_s1270_evtcontratavnp_obj(doc, status)



def read_s1270_evtcontratavnp_obj(doc):
    s1270_evtcontratavnp_dados = {}
    s1270_evtcontratavnp_dados['versao'] = 'v02_04_02'
    s1270_evtcontratavnp_dados['status'] = status
    s1270_evtcontratavnp_dados['identidade'] = doc.eSocial.evtContratAvNP['Id']
    s1270_evtcontratavnp_dados['processamento_codigo_resposta'] = 1
    evtContratAvNP = doc.eSocial.evtContratAvNP
    
    if 'indRetif' in dir(evtContratAvNP.ideEvento): s1270_evtcontratavnp_dados['indretif'] = evtContratAvNP.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtContratAvNP.ideEvento): s1270_evtcontratavnp_dados['nrrecibo'] = evtContratAvNP.ideEvento.nrRecibo.cdata
    if 'indApuracao' in dir(evtContratAvNP.ideEvento): s1270_evtcontratavnp_dados['indapuracao'] = evtContratAvNP.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtContratAvNP.ideEvento): s1270_evtcontratavnp_dados['perapur'] = evtContratAvNP.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtContratAvNP.ideEvento): s1270_evtcontratavnp_dados['tpamb'] = evtContratAvNP.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtContratAvNP.ideEvento): s1270_evtcontratavnp_dados['procemi'] = evtContratAvNP.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtContratAvNP.ideEvento): s1270_evtcontratavnp_dados['verproc'] = evtContratAvNP.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtContratAvNP.ideEmpregador): s1270_evtcontratavnp_dados['tpinsc'] = evtContratAvNP.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtContratAvNP.ideEmpregador): s1270_evtcontratavnp_dados['nrinsc'] = evtContratAvNP.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtContratAvNP.remunAvNP): s1270_evtcontratavnp_dados['operacao'] = 1
    elif 'alteracao' in dir(evtContratAvNP.remunAvNP): s1270_evtcontratavnp_dados['operacao'] = 2
    elif 'exclusao' in dir(evtContratAvNP.remunAvNP): s1270_evtcontratavnp_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1270_evtcontratavnp', s1270_evtcontratavnp_dados)
    resp = executar_sql(insert, True)
    s1270_evtcontratavnp_id = resp[0][0]
    dados = s1270_evtcontratavnp_dados
    dados['evento'] = 's1270'
    dados['id'] = s1270_evtcontratavnp_id
    dados['identidade_evento'] = doc.eSocial.evtContratAvNP['Id']
    dados['status'] = 1

    if 'remunAvNP' in dir(evtContratAvNP):
        for remunAvNP in evtContratAvNP.remunAvNP:
            s1270_remunavnp_dados = {}
            s1270_remunavnp_dados['s1270_evtcontratavnp_id'] = s1270_evtcontratavnp_id
            
            if 'tpInsc' in dir(remunAvNP): s1270_remunavnp_dados['tpinsc'] = remunAvNP.tpInsc.cdata
            if 'nrInsc' in dir(remunAvNP): s1270_remunavnp_dados['nrinsc'] = remunAvNP.nrInsc.cdata
            if 'codLotacao' in dir(remunAvNP): s1270_remunavnp_dados['codlotacao'] = remunAvNP.codLotacao.cdata
            if 'vrBcCp00' in dir(remunAvNP): s1270_remunavnp_dados['vrbccp00'] = remunAvNP.vrBcCp00.cdata
            if 'vrBcCp15' in dir(remunAvNP): s1270_remunavnp_dados['vrbccp15'] = remunAvNP.vrBcCp15.cdata
            if 'vrBcCp20' in dir(remunAvNP): s1270_remunavnp_dados['vrbccp20'] = remunAvNP.vrBcCp20.cdata
            if 'vrBcCp25' in dir(remunAvNP): s1270_remunavnp_dados['vrbccp25'] = remunAvNP.vrBcCp25.cdata
            if 'vrBcCp13' in dir(remunAvNP): s1270_remunavnp_dados['vrbccp13'] = remunAvNP.vrBcCp13.cdata
            if 'vrBcFgts' in dir(remunAvNP): s1270_remunavnp_dados['vrbcfgts'] = remunAvNP.vrBcFgts.cdata
            if 'vrDescCP' in dir(remunAvNP): s1270_remunavnp_dados['vrdesccp'] = remunAvNP.vrDescCP.cdata
            insert = create_insert('s1270_remunavnp', s1270_remunavnp_dados)
            resp = executar_sql(insert, True)
            s1270_remunavnp_id = resp[0][0]
            #print s1270_remunavnp_id

    from emensageriapro.esocial.views.s1270_evtcontratavnp_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1270_evtcontratavnp_id, 'default')
    return dados