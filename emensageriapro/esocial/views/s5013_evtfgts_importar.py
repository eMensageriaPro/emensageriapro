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


def read_s5013_evtfgts_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s5013_evtfgts_obj(doc, status, validar)
    return dados

def read_s5013_evtfgts(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s5013_evtfgts_obj(doc, status, validar)
    return dados



def read_s5013_evtfgts_obj(doc, status, validar=False):
    s5013_evtfgts_dados = {}
    s5013_evtfgts_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s5013_evtfgts_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5013_evtfgts_dados['identidade'] = doc.eSocial.evtFGTS['Id']
    s5013_evtfgts_dados['processamento_codigo_resposta'] = 1
    evtFGTS = doc.eSocial.evtFGTS

    if 'perApur' in dir(evtFGTS.ideEvento): s5013_evtfgts_dados['perapur'] = evtFGTS.ideEvento.perApur.cdata
    if 'tpInsc' in dir(evtFGTS.ideEmpregador): s5013_evtfgts_dados['tpinsc'] = evtFGTS.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtFGTS.ideEmpregador): s5013_evtfgts_dados['nrinsc'] = evtFGTS.ideEmpregador.nrInsc.cdata
    if 'nrRecArqBase' in dir(evtFGTS.infoFGTS): s5013_evtfgts_dados['nrrecarqbase'] = evtFGTS.infoFGTS.nrRecArqBase.cdata
    if 'indExistInfo' in dir(evtFGTS.infoFGTS): s5013_evtfgts_dados['indexistinfo'] = evtFGTS.infoFGTS.indExistInfo.cdata
    if 'inclusao' in dir(evtFGTS.infoFGTS): s5013_evtfgts_dados['operacao'] = 1
    elif 'alteracao' in dir(evtFGTS.infoFGTS): s5013_evtfgts_dados['operacao'] = 2
    elif 'exclusao' in dir(evtFGTS.infoFGTS): s5013_evtfgts_dados['operacao'] = 3
    #print dados
    insert = create_insert('s5013_evtfgts', s5013_evtfgts_dados)
    resp = executar_sql(insert, True)
    s5013_evtfgts_id = resp[0][0]
    dados = s5013_evtfgts_dados
    dados['evento'] = 's5013'
    dados['id'] = s5013_evtfgts_id
    dados['identidade_evento'] = doc.eSocial.evtFGTS['Id']
    dados['status'] = 1

    if 'basePerApur' in dir(evtFGTS.infoFGTS.infoBaseFGTS):
        for basePerApur in evtFGTS.infoFGTS.infoBaseFGTS.basePerApur:
            s5013_baseperapur_dados = {}
            s5013_baseperapur_dados['s5013_evtfgts_id'] = s5013_evtfgts_id

            if 'tpValor' in dir(basePerApur): s5013_baseperapur_dados['tpvalor'] = basePerApur.tpValor.cdata
            if 'baseFGTS' in dir(basePerApur): s5013_baseperapur_dados['basefgts'] = basePerApur.baseFGTS.cdata
            insert = create_insert('s5013_baseperapur', s5013_baseperapur_dados)
            resp = executar_sql(insert, True)
            s5013_baseperapur_id = resp[0][0]
            #print s5013_baseperapur_id

    if 'infoBasePerAntE' in dir(evtFGTS.infoFGTS.infoBaseFGTS):
        for infoBasePerAntE in evtFGTS.infoFGTS.infoBaseFGTS.infoBasePerAntE:
            s5013_infobaseperante_dados = {}
            s5013_infobaseperante_dados['s5013_evtfgts_id'] = s5013_evtfgts_id

            if 'perRef' in dir(infoBasePerAntE): s5013_infobaseperante_dados['perref'] = infoBasePerAntE.perRef.cdata
            insert = create_insert('s5013_infobaseperante', s5013_infobaseperante_dados)
            resp = executar_sql(insert, True)
            s5013_infobaseperante_id = resp[0][0]
            #print s5013_infobaseperante_id

            if 'basePerAntE' in dir(infoBasePerAntE):
                for basePerAntE in infoBasePerAntE.basePerAntE:
                    s5013_baseperante_dados = {}
                    s5013_baseperante_dados['s5013_infobaseperante_id'] = s5013_infobaseperante_id

                    if 'tpValorE' in dir(basePerAntE): s5013_baseperante_dados['tpvalore'] = basePerAntE.tpValorE.cdata
                    if 'baseFGTSE' in dir(basePerAntE): s5013_baseperante_dados['basefgtse'] = basePerAntE.baseFGTSE.cdata
                    insert = create_insert('s5013_baseperante', s5013_baseperante_dados)
                    resp = executar_sql(insert, True)
                    s5013_baseperante_id = resp[0][0]
                    #print s5013_baseperante_id

    if 'dpsPerApur' in dir(evtFGTS.infoFGTS.infoDpsFGTS):
        for dpsPerApur in evtFGTS.infoFGTS.infoDpsFGTS.dpsPerApur:
            s5013_dpsperapur_dados = {}
            s5013_dpsperapur_dados['s5013_evtfgts_id'] = s5013_evtfgts_id

            if 'tpDps' in dir(dpsPerApur): s5013_dpsperapur_dados['tpdps'] = dpsPerApur.tpDps.cdata
            if 'vrFGTS' in dir(dpsPerApur): s5013_dpsperapur_dados['vrfgts'] = dpsPerApur.vrFGTS.cdata
            insert = create_insert('s5013_dpsperapur', s5013_dpsperapur_dados)
            resp = executar_sql(insert, True)
            s5013_dpsperapur_id = resp[0][0]
            #print s5013_dpsperapur_id

    if 'infoDpsPerAntE' in dir(evtFGTS.infoFGTS.infoDpsFGTS):
        for infoDpsPerAntE in evtFGTS.infoFGTS.infoDpsFGTS.infoDpsPerAntE:
            s5013_infodpsperante_dados = {}
            s5013_infodpsperante_dados['s5013_evtfgts_id'] = s5013_evtfgts_id

            if 'perRef' in dir(infoDpsPerAntE): s5013_infodpsperante_dados['perref'] = infoDpsPerAntE.perRef.cdata
            insert = create_insert('s5013_infodpsperante', s5013_infodpsperante_dados)
            resp = executar_sql(insert, True)
            s5013_infodpsperante_id = resp[0][0]
            #print s5013_infodpsperante_id

            if 'dpsPerAntE' in dir(infoDpsPerAntE):
                for dpsPerAntE in infoDpsPerAntE.dpsPerAntE:
                    s5013_dpsperante_dados = {}
                    s5013_dpsperante_dados['s5013_infodpsperante_id'] = s5013_infodpsperante_id

                    if 'tpDpsE' in dir(dpsPerAntE): s5013_dpsperante_dados['tpdpse'] = dpsPerAntE.tpDpsE.cdata
                    if 'vrFGTSE' in dir(dpsPerAntE): s5013_dpsperante_dados['vrfgtse'] = dpsPerAntE.vrFGTSE.cdata
                    insert = create_insert('s5013_dpsperante', s5013_dpsperante_dados)
                    resp = executar_sql(insert, True)
                    s5013_dpsperante_id = resp[0][0]
                    #print s5013_dpsperante_id

    from emensageriapro.esocial.views.s5013_evtfgts_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s5013_evtfgts_id, 'default')
    return dados