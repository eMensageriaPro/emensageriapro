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


def read_s5002_evtirrfbenef_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s5002_evtirrfbenef_obj(doc, status, validar)
    return dados

def read_s5002_evtirrfbenef(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s5002_evtirrfbenef_obj(doc, status, validar)
    return dados



def read_s5002_evtirrfbenef_obj(doc, status, validar=False):
    s5002_evtirrfbenef_dados = {}
    s5002_evtirrfbenef_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s5002_evtirrfbenef_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5002_evtirrfbenef_dados['identidade'] = doc.eSocial.evtIrrfBenef['Id']
    s5002_evtirrfbenef_dados['processamento_codigo_resposta'] = 1
    evtIrrfBenef = doc.eSocial.evtIrrfBenef

    if 'nrRecArqBase' in dir(evtIrrfBenef.ideEvento): s5002_evtirrfbenef_dados['nrrecarqbase'] = evtIrrfBenef.ideEvento.nrRecArqBase.cdata
    if 'perApur' in dir(evtIrrfBenef.ideEvento): s5002_evtirrfbenef_dados['perapur'] = evtIrrfBenef.ideEvento.perApur.cdata
    if 'tpInsc' in dir(evtIrrfBenef.ideEmpregador): s5002_evtirrfbenef_dados['tpinsc'] = evtIrrfBenef.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtIrrfBenef.ideEmpregador): s5002_evtirrfbenef_dados['nrinsc'] = evtIrrfBenef.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtIrrfBenef.ideTrabalhador): s5002_evtirrfbenef_dados['cpftrab'] = evtIrrfBenef.ideTrabalhador.cpfTrab.cdata
    if 'inclusao' in dir(evtIrrfBenef.infoIrrf): s5002_evtirrfbenef_dados['operacao'] = 1
    elif 'alteracao' in dir(evtIrrfBenef.infoIrrf): s5002_evtirrfbenef_dados['operacao'] = 2
    elif 'exclusao' in dir(evtIrrfBenef.infoIrrf): s5002_evtirrfbenef_dados['operacao'] = 3
    #print dados
    insert = create_insert('s5002_evtirrfbenef', s5002_evtirrfbenef_dados)
    resp = executar_sql(insert, True)
    s5002_evtirrfbenef_id = resp[0][0]
    dados = s5002_evtirrfbenef_dados
    dados['evento'] = 's5002'
    dados['id'] = s5002_evtirrfbenef_id
    dados['identidade_evento'] = doc.eSocial.evtIrrfBenef['Id']
    dados['status'] = 1

    if 'infoDep' in dir(evtIrrfBenef):
        for infoDep in evtIrrfBenef.infoDep:
            s5002_infodep_dados = {}
            s5002_infodep_dados['s5002_evtirrfbenef_id'] = s5002_evtirrfbenef_id

            if 'vrDedDep' in dir(infoDep): s5002_infodep_dados['vrdeddep'] = infoDep.vrDedDep.cdata
            insert = create_insert('s5002_infodep', s5002_infodep_dados)
            resp = executar_sql(insert, True)
            s5002_infodep_id = resp[0][0]
            #print s5002_infodep_id

    if 'infoIrrf' in dir(evtIrrfBenef):
        for infoIrrf in evtIrrfBenef.infoIrrf:
            s5002_infoirrf_dados = {}
            s5002_infoirrf_dados['s5002_evtirrfbenef_id'] = s5002_evtirrfbenef_id

            if 'codCateg' in dir(infoIrrf): s5002_infoirrf_dados['codcateg'] = infoIrrf.codCateg.cdata
            if 'indResBr' in dir(infoIrrf): s5002_infoirrf_dados['indresbr'] = infoIrrf.indResBr.cdata
            insert = create_insert('s5002_infoirrf', s5002_infoirrf_dados)
            resp = executar_sql(insert, True)
            s5002_infoirrf_id = resp[0][0]
            #print s5002_infoirrf_id

            if 'basesIrrf' in dir(infoIrrf):
                for basesIrrf in infoIrrf.basesIrrf:
                    s5002_basesirrf_dados = {}
                    s5002_basesirrf_dados['s5002_infoirrf_id'] = s5002_infoirrf_id

                    if 'tpValor' in dir(basesIrrf): s5002_basesirrf_dados['tpvalor'] = basesIrrf.tpValor.cdata
                    if 'valor' in dir(basesIrrf): s5002_basesirrf_dados['valor'] = basesIrrf.valor.cdata
                    insert = create_insert('s5002_basesirrf', s5002_basesirrf_dados)
                    resp = executar_sql(insert, True)
                    s5002_basesirrf_id = resp[0][0]
                    #print s5002_basesirrf_id

            if 'irrf' in dir(infoIrrf):
                for irrf in infoIrrf.irrf:
                    s5002_irrf_dados = {}
                    s5002_irrf_dados['s5002_infoirrf_id'] = s5002_infoirrf_id

                    if 'tpCR' in dir(irrf): s5002_irrf_dados['tpcr'] = irrf.tpCR.cdata
                    if 'vrIrrfDesc' in dir(irrf): s5002_irrf_dados['vrirrfdesc'] = irrf.vrIrrfDesc.cdata
                    insert = create_insert('s5002_irrf', s5002_irrf_dados)
                    resp = executar_sql(insert, True)
                    s5002_irrf_id = resp[0][0]
                    #print s5002_irrf_id

            if 'idePgtoExt' in dir(infoIrrf):
                for idePgtoExt in infoIrrf.idePgtoExt:
                    s5002_idepgtoext_dados = {}
                    s5002_idepgtoext_dados['s5002_infoirrf_id'] = s5002_infoirrf_id

                    if 'codPais' in dir(idePgtoExt): s5002_idepgtoext_dados['codpais'] = idePgtoExt.idePais.codPais.cdata
                    if 'indNIF' in dir(idePgtoExt): s5002_idepgtoext_dados['indnif'] = idePgtoExt.idePais.indNIF.cdata
                    if 'nifBenef' in dir(idePgtoExt): s5002_idepgtoext_dados['nifbenef'] = idePgtoExt.idePais.nifBenef.cdata
                    if 'dscLograd' in dir(idePgtoExt): s5002_idepgtoext_dados['dsclograd'] = idePgtoExt.endExt.dscLograd.cdata
                    if 'nrLograd' in dir(idePgtoExt): s5002_idepgtoext_dados['nrlograd'] = idePgtoExt.endExt.nrLograd.cdata
                    if 'complem' in dir(idePgtoExt): s5002_idepgtoext_dados['complem'] = idePgtoExt.endExt.complem.cdata
                    if 'bairro' in dir(idePgtoExt): s5002_idepgtoext_dados['bairro'] = idePgtoExt.endExt.bairro.cdata
                    if 'nmCid' in dir(idePgtoExt): s5002_idepgtoext_dados['nmcid'] = idePgtoExt.endExt.nmCid.cdata
                    if 'codPostal' in dir(idePgtoExt): s5002_idepgtoext_dados['codpostal'] = idePgtoExt.endExt.codPostal.cdata
                    insert = create_insert('s5002_idepgtoext', s5002_idepgtoext_dados)
                    resp = executar_sql(insert, True)
                    s5002_idepgtoext_id = resp[0][0]
                    #print s5002_idepgtoext_id

    from emensageriapro.esocial.views.s5002_evtirrfbenef_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s5002_evtirrfbenef_id, 'default')
    return dados