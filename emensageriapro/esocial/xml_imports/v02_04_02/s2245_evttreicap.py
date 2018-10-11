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


def read_s2245_evttreicap(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    read_s2245_evttreicap_obj(doc, status)



def read_s2245_evttreicap_obj(doc):
    s2245_evttreicap_dados = {}
    s2245_evttreicap_dados['versao'] = 'v02_04_02'
    s2245_evttreicap_dados['status'] = status
    s2245_evttreicap_dados['identidade'] = doc.eSocial.evtTreiCap['Id']
    s2245_evttreicap_dados['processamento_codigo_resposta'] = 1
    evtTreiCap = doc.eSocial.evtTreiCap
    
    if 'indRetif' in dir(evtTreiCap.ideEvento): s2245_evttreicap_dados['indretif'] = evtTreiCap.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtTreiCap.ideEvento): s2245_evttreicap_dados['nrrecibo'] = evtTreiCap.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtTreiCap.ideEvento): s2245_evttreicap_dados['tpamb'] = evtTreiCap.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTreiCap.ideEvento): s2245_evttreicap_dados['procemi'] = evtTreiCap.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTreiCap.ideEvento): s2245_evttreicap_dados['verproc'] = evtTreiCap.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTreiCap.ideEmpregador): s2245_evttreicap_dados['tpinsc'] = evtTreiCap.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTreiCap.ideEmpregador): s2245_evttreicap_dados['nrinsc'] = evtTreiCap.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtTreiCap.ideVinculo): s2245_evttreicap_dados['cpftrab'] = evtTreiCap.ideVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtTreiCap.ideVinculo): s2245_evttreicap_dados['nistrab'] = evtTreiCap.ideVinculo.nisTrab.cdata
    if 'matricula' in dir(evtTreiCap.ideVinculo): s2245_evttreicap_dados['matricula'] = evtTreiCap.ideVinculo.matricula.cdata
    if 'codCateg' in dir(evtTreiCap.ideVinculo): s2245_evttreicap_dados['codcateg'] = evtTreiCap.ideVinculo.codCateg.cdata
    if 'codTreiCap' in dir(evtTreiCap.treiCap): s2245_evttreicap_dados['codtreicap'] = evtTreiCap.treiCap.codTreiCap.cdata
    if 'observacao' in dir(evtTreiCap.treiCap): s2245_evttreicap_dados['observacao'] = evtTreiCap.treiCap.observacao.cdata
    if 'inclusao' in dir(evtTreiCap.treiCap): s2245_evttreicap_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTreiCap.treiCap): s2245_evttreicap_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTreiCap.treiCap): s2245_evttreicap_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2245_evttreicap', s2245_evttreicap_dados)
    resp = executar_sql(insert, True)
    s2245_evttreicap_id = resp[0][0]
    dados = s2245_evttreicap_dados
    dados['evento'] = 's2245'
    dados['id'] = s2245_evttreicap_id
    dados['identidade_evento'] = doc.eSocial.evtTreiCap['Id']
    dados['status'] = 1

    if 'infoComplem' in dir(evtTreiCap.treiCap):
        for infoComplem in evtTreiCap.treiCap.infoComplem:
            s2245_infocomplem_dados = {}
            s2245_infocomplem_dados['s2245_evttreicap_id'] = s2245_evttreicap_id
            
            if 'dtTreiCap' in dir(infoComplem): s2245_infocomplem_dados['dttreicap'] = infoComplem.dtTreiCap.cdata
            if 'durTreiCap' in dir(infoComplem): s2245_infocomplem_dados['durtreicap'] = infoComplem.durTreiCap.cdata
            if 'modTreiCap' in dir(infoComplem): s2245_infocomplem_dados['modtreicap'] = infoComplem.modTreiCap.cdata
            if 'tpTreiCap' in dir(infoComplem): s2245_infocomplem_dados['tptreicap'] = infoComplem.tpTreiCap.cdata
            insert = create_insert('s2245_infocomplem', s2245_infocomplem_dados)
            resp = executar_sql(insert, True)
            s2245_infocomplem_id = resp[0][0]
            #print s2245_infocomplem_id

            if 'ideProfResp' in dir(infoComplem):
                for ideProfResp in infoComplem.ideProfResp:
                    s2245_ideprofresp_dados = {}
                    s2245_ideprofresp_dados['s2245_infocomplem_id'] = s2245_infocomplem_id
                    
                    if 'cpfProf' in dir(ideProfResp): s2245_ideprofresp_dados['cpfprof'] = ideProfResp.cpfProf.cdata
                    if 'nmProf' in dir(ideProfResp): s2245_ideprofresp_dados['nmprof'] = ideProfResp.nmProf.cdata
                    if 'tpProf' in dir(ideProfResp): s2245_ideprofresp_dados['tpprof'] = ideProfResp.tpProf.cdata
                    if 'formProf' in dir(ideProfResp): s2245_ideprofresp_dados['formprof'] = ideProfResp.formProf.cdata
                    if 'codCBO' in dir(ideProfResp): s2245_ideprofresp_dados['codcbo'] = ideProfResp.codCBO.cdata
                    insert = create_insert('s2245_ideprofresp', s2245_ideprofresp_dados)
                    resp = executar_sql(insert, True)
                    s2245_ideprofresp_id = resp[0][0]
                    #print s2245_ideprofresp_id
        
    from emensageriapro.esocial.views.s2245_evttreicap_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2245_evttreicap_id, 'default')
    return dados