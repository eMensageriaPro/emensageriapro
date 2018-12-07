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


def read_s2416_evtcdbenalt_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2416_evtcdbenalt_obj(doc, status, validar)
    return dados

def read_s2416_evtcdbenalt(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2416_evtcdbenalt_obj(doc, status, validar)
    return dados



def read_s2416_evtcdbenalt_obj(doc, status, validar=False):
    s2416_evtcdbenalt_dados = {}
    s2416_evtcdbenalt_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2416_evtcdbenalt_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2416_evtcdbenalt_dados['identidade'] = doc.eSocial.evtCdBenAlt['Id']
    s2416_evtcdbenalt_dados['processamento_codigo_resposta'] = 1
    evtCdBenAlt = doc.eSocial.evtCdBenAlt

    if 'indRetif' in dir(evtCdBenAlt.ideEvento): s2416_evtcdbenalt_dados['indretif'] = evtCdBenAlt.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtCdBenAlt.ideEvento): s2416_evtcdbenalt_dados['nrrecibo'] = evtCdBenAlt.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtCdBenAlt.ideEvento): s2416_evtcdbenalt_dados['tpamb'] = evtCdBenAlt.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtCdBenAlt.ideEvento): s2416_evtcdbenalt_dados['procemi'] = evtCdBenAlt.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtCdBenAlt.ideEvento): s2416_evtcdbenalt_dados['verproc'] = evtCdBenAlt.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtCdBenAlt.ideEmpregador): s2416_evtcdbenalt_dados['tpinsc'] = evtCdBenAlt.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtCdBenAlt.ideEmpregador): s2416_evtcdbenalt_dados['nrinsc'] = evtCdBenAlt.ideEmpregador.nrInsc.cdata
    if 'cpfBenef' in dir(evtCdBenAlt.ideBeneficio): s2416_evtcdbenalt_dados['cpfbenef'] = evtCdBenAlt.ideBeneficio.cpfBenef.cdata
    if 'nrBeneficio' in dir(evtCdBenAlt.ideBeneficio): s2416_evtcdbenalt_dados['nrbeneficio'] = evtCdBenAlt.ideBeneficio.nrBeneficio.cdata
    if 'dtAltBeneficio' in dir(evtCdBenAlt.infoBenAlteracao): s2416_evtcdbenalt_dados['dtaltbeneficio'] = evtCdBenAlt.infoBenAlteracao.dtAltBeneficio.cdata
    if 'tpBeneficio' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio): s2416_evtcdbenalt_dados['tpbeneficio'] = evtCdBenAlt.infoBenAlteracao.dadosBeneficio.tpBeneficio.cdata
    if 'tpPlanRP' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio): s2416_evtcdbenalt_dados['tpplanrp'] = evtCdBenAlt.infoBenAlteracao.dadosBeneficio.tpPlanRP.cdata
    if 'dsc' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio): s2416_evtcdbenalt_dados['dsc'] = evtCdBenAlt.infoBenAlteracao.dadosBeneficio.dsc.cdata
    if 'indDecJud' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio): s2416_evtcdbenalt_dados['inddecjud'] = evtCdBenAlt.infoBenAlteracao.dadosBeneficio.indDecJud.cdata
    if 'indHomologTC' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio): s2416_evtcdbenalt_dados['indhomologtc'] = evtCdBenAlt.infoBenAlteracao.dadosBeneficio.indHomologTC.cdata
    if 'indSuspensao' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio): s2416_evtcdbenalt_dados['indsuspensao'] = evtCdBenAlt.infoBenAlteracao.dadosBeneficio.indSuspensao.cdata
    if 'inclusao' in dir(evtCdBenAlt.infoBenAlteracao): s2416_evtcdbenalt_dados['operacao'] = 1
    elif 'alteracao' in dir(evtCdBenAlt.infoBenAlteracao): s2416_evtcdbenalt_dados['operacao'] = 2
    elif 'exclusao' in dir(evtCdBenAlt.infoBenAlteracao): s2416_evtcdbenalt_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2416_evtcdbenalt', s2416_evtcdbenalt_dados)
    resp = executar_sql(insert, True)
    s2416_evtcdbenalt_id = resp[0][0]
    dados = s2416_evtcdbenalt_dados
    dados['evento'] = 's2416'
    dados['id'] = s2416_evtcdbenalt_id
    dados['identidade_evento'] = doc.eSocial.evtCdBenAlt['Id']
    dados['status'] = 1

    if 'infoPenMorte' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio):
        for infoPenMorte in evtCdBenAlt.infoBenAlteracao.dadosBeneficio.infoPenMorte:
            s2416_infopenmorte_dados = {}
            s2416_infopenmorte_dados['s2416_evtcdbenalt_id'] = s2416_evtcdbenalt_id
       
            if 'tpPenMorte' in dir(infoPenMorte): s2416_infopenmorte_dados['tppenmorte'] = infoPenMorte.tpPenMorte.cdata
            insert = create_insert('s2416_infopenmorte', s2416_infopenmorte_dados)
            resp = executar_sql(insert, True)
            s2416_infopenmorte_id = resp[0][0]
            #print s2416_infopenmorte_id

    if 'homologTC' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio):
        for homologTC in evtCdBenAlt.infoBenAlteracao.dadosBeneficio.homologTC:
            s2416_homologtc_dados = {}
            s2416_homologtc_dados['s2416_evtcdbenalt_id'] = s2416_evtcdbenalt_id
       
            if 'nrAtoLegal' in dir(homologTC): s2416_homologtc_dados['nratolegal'] = homologTC.nrAtoLegal.cdata
            insert = create_insert('s2416_homologtc', s2416_homologtc_dados)
            resp = executar_sql(insert, True)
            s2416_homologtc_id = resp[0][0]
            #print s2416_homologtc_id

    if 'suspensao' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio):
        for suspensao in evtCdBenAlt.infoBenAlteracao.dadosBeneficio.suspensao:
            s2416_suspensao_dados = {}
            s2416_suspensao_dados['s2416_evtcdbenalt_id'] = s2416_evtcdbenalt_id
       
            if 'mtvSuspensao' in dir(suspensao): s2416_suspensao_dados['mtvsuspensao'] = suspensao.mtvSuspensao.cdata
            if 'dscSuspensao' in dir(suspensao): s2416_suspensao_dados['dscsuspensao'] = suspensao.dscSuspensao.cdata
            insert = create_insert('s2416_suspensao', s2416_suspensao_dados)
            resp = executar_sql(insert, True)
            s2416_suspensao_id = resp[0][0]
            #print s2416_suspensao_id

    from emensageriapro.esocial.views.s2416_evtcdbenalt_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2416_evtcdbenalt_id, 'default')
    return dados