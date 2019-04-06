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



def read_s5013_evtfgts_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s5013_evtfgts_obj(doc, status, validar)
    return dados

def read_s5013_evtfgts(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s5013_evtfgts_obj(doc, status, validar)
    return dados



def read_s5013_evtfgts_obj(doc, status, validar=False):
    s5013_evtfgts_dados = {}
    s5013_evtfgts_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s5013_evtfgts_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5013_evtfgts_dados['identidade'] = doc.eSocial.evtFGTS['Id']
    evtFGTS = doc.eSocial.evtFGTS

    try: s5013_evtfgts_dados['perapur'] = evtFGTS.ideEvento.perApur.cdata
    except AttributeError: pass
    try: s5013_evtfgts_dados['tpinsc'] = evtFGTS.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s5013_evtfgts_dados['nrinsc'] = evtFGTS.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s5013_evtfgts_dados['nrrecarqbase'] = evtFGTS.infoFGTS.nrRecArqBase.cdata
    except AttributeError: pass
    try: s5013_evtfgts_dados['indexistinfo'] = evtFGTS.infoFGTS.indExistInfo.cdata
    except AttributeError: pass
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
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'basePerApur' in dir(evtFGTS.infoFGTS.infoBaseFGTS) and evtFGTS.infoFGTS.infoBaseFGTS.basePerApur.cdata != '':
        for basePerApur in evtFGTS.infoFGTS.infoBaseFGTS.basePerApur:
            s5013_baseperapur_dados = {}
            s5013_baseperapur_dados['s5013_evtfgts_id'] = s5013_evtfgts_id

            try: s5013_baseperapur_dados['tpvalor'] = basePerApur.tpValor.cdata
            except AttributeError: pass
            try: s5013_baseperapur_dados['basefgts'] = basePerApur.baseFGTS.cdata
            except AttributeError: pass
            insert = create_insert('s5013_baseperapur', s5013_baseperapur_dados)
            resp = executar_sql(insert, True)
            s5013_baseperapur_id = resp[0][0]
            #print s5013_baseperapur_id

    if 'infoBasePerAntE' in dir(evtFGTS.infoFGTS.infoBaseFGTS) and evtFGTS.infoFGTS.infoBaseFGTS.infoBasePerAntE.cdata != '':
        for infoBasePerAntE in evtFGTS.infoFGTS.infoBaseFGTS.infoBasePerAntE:
            s5013_infobaseperante_dados = {}
            s5013_infobaseperante_dados['s5013_evtfgts_id'] = s5013_evtfgts_id

            try: s5013_infobaseperante_dados['perref'] = infoBasePerAntE.perRef.cdata
            except AttributeError: pass
            insert = create_insert('s5013_infobaseperante', s5013_infobaseperante_dados)
            resp = executar_sql(insert, True)
            s5013_infobaseperante_id = resp[0][0]
            #print s5013_infobaseperante_id

            if 'basePerAntE' in dir(infoBasePerAntE) and infoBasePerAntE.basePerAntE.cdata != '':
                for basePerAntE in infoBasePerAntE.basePerAntE:
                    s5013_baseperante_dados = {}
                    s5013_baseperante_dados['s5013_infobaseperante_id'] = s5013_infobaseperante_id

                    try: s5013_baseperante_dados['tpvalore'] = basePerAntE.tpValorE.cdata
                    except AttributeError: pass
                    try: s5013_baseperante_dados['basefgtse'] = basePerAntE.baseFGTSE.cdata
                    except AttributeError: pass
                    insert = create_insert('s5013_baseperante', s5013_baseperante_dados)
                    resp = executar_sql(insert, True)
                    s5013_baseperante_id = resp[0][0]
                    #print s5013_baseperante_id

    if 'dpsPerApur' in dir(evtFGTS.infoFGTS.infoDpsFGTS) and evtFGTS.infoFGTS.infoDpsFGTS.dpsPerApur.cdata != '':
        for dpsPerApur in evtFGTS.infoFGTS.infoDpsFGTS.dpsPerApur:
            s5013_dpsperapur_dados = {}
            s5013_dpsperapur_dados['s5013_evtfgts_id'] = s5013_evtfgts_id

            try: s5013_dpsperapur_dados['tpdps'] = dpsPerApur.tpDps.cdata
            except AttributeError: pass
            try: s5013_dpsperapur_dados['vrfgts'] = dpsPerApur.vrFGTS.cdata
            except AttributeError: pass
            insert = create_insert('s5013_dpsperapur', s5013_dpsperapur_dados)
            resp = executar_sql(insert, True)
            s5013_dpsperapur_id = resp[0][0]
            #print s5013_dpsperapur_id

    if 'infoDpsPerAntE' in dir(evtFGTS.infoFGTS.infoDpsFGTS) and evtFGTS.infoFGTS.infoDpsFGTS.infoDpsPerAntE.cdata != '':
        for infoDpsPerAntE in evtFGTS.infoFGTS.infoDpsFGTS.infoDpsPerAntE:
            s5013_infodpsperante_dados = {}
            s5013_infodpsperante_dados['s5013_evtfgts_id'] = s5013_evtfgts_id

            try: s5013_infodpsperante_dados['perref'] = infoDpsPerAntE.perRef.cdata
            except AttributeError: pass
            insert = create_insert('s5013_infodpsperante', s5013_infodpsperante_dados)
            resp = executar_sql(insert, True)
            s5013_infodpsperante_id = resp[0][0]
            #print s5013_infodpsperante_id

            if 'dpsPerAntE' in dir(infoDpsPerAntE) and infoDpsPerAntE.dpsPerAntE.cdata != '':
                for dpsPerAntE in infoDpsPerAntE.dpsPerAntE:
                    s5013_dpsperante_dados = {}
                    s5013_dpsperante_dados['s5013_infodpsperante_id'] = s5013_infodpsperante_id

                    try: s5013_dpsperante_dados['tpdpse'] = dpsPerAntE.tpDpsE.cdata
                    except AttributeError: pass
                    try: s5013_dpsperante_dados['vrfgtse'] = dpsPerAntE.vrFGTSE.cdata
                    except AttributeError: pass
                    insert = create_insert('s5013_dpsperante', s5013_dpsperante_dados)
                    resp = executar_sql(insert, True)
                    s5013_dpsperante_id = resp[0][0]
                    #print s5013_dpsperante_id

    from emensageriapro.esocial.views.s5013_evtfgts_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s5013_evtfgts_id, 'default')
    return dados