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



def read_s5002_evtirrfbenef_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s5002_evtirrfbenef_obj(doc, status, validar)
    return dados

def read_s5002_evtirrfbenef(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s5002_evtirrfbenef_obj(doc, status, validar)
    return dados



def read_s5002_evtirrfbenef_obj(doc, status, validar=False):
    s5002_evtirrfbenef_dados = {}
    s5002_evtirrfbenef_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s5002_evtirrfbenef_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5002_evtirrfbenef_dados['identidade'] = doc.eSocial.evtIrrfBenef['Id']
    evtIrrfBenef = doc.eSocial.evtIrrfBenef

    try: s5002_evtirrfbenef_dados['nrrecarqbase'] = evtIrrfBenef.ideEvento.nrRecArqBase.cdata
    except AttributeError: pass
    try: s5002_evtirrfbenef_dados['perapur'] = evtIrrfBenef.ideEvento.perApur.cdata
    except AttributeError: pass
    try: s5002_evtirrfbenef_dados['tpinsc'] = evtIrrfBenef.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s5002_evtirrfbenef_dados['nrinsc'] = evtIrrfBenef.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s5002_evtirrfbenef_dados['cpftrab'] = evtIrrfBenef.ideTrabalhador.cpfTrab.cdata
    except AttributeError: pass
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
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'infoDep' in dir(evtIrrfBenef) and evtIrrfBenef.infoDep.cdata != '':
        for infoDep in evtIrrfBenef.infoDep:
            s5002_infodep_dados = {}
            s5002_infodep_dados['s5002_evtirrfbenef_id'] = s5002_evtirrfbenef_id

            try: s5002_infodep_dados['vrdeddep'] = infoDep.vrDedDep.cdata
            except AttributeError: pass
            insert = create_insert('s5002_infodep', s5002_infodep_dados)
            resp = executar_sql(insert, True)
            s5002_infodep_id = resp[0][0]
            #print s5002_infodep_id

    if 'infoIrrf' in dir(evtIrrfBenef) and evtIrrfBenef.infoIrrf.cdata != '':
        for infoIrrf in evtIrrfBenef.infoIrrf:
            s5002_infoirrf_dados = {}
            s5002_infoirrf_dados['s5002_evtirrfbenef_id'] = s5002_evtirrfbenef_id

            try: s5002_infoirrf_dados['codcateg'] = infoIrrf.codCateg.cdata
            except AttributeError: pass
            try: s5002_infoirrf_dados['indresbr'] = infoIrrf.indResBr.cdata
            except AttributeError: pass
            insert = create_insert('s5002_infoirrf', s5002_infoirrf_dados)
            resp = executar_sql(insert, True)
            s5002_infoirrf_id = resp[0][0]
            #print s5002_infoirrf_id

            if 'basesIrrf' in dir(infoIrrf) and infoIrrf.basesIrrf.cdata != '':
                for basesIrrf in infoIrrf.basesIrrf:
                    s5002_basesirrf_dados = {}
                    s5002_basesirrf_dados['s5002_infoirrf_id'] = s5002_infoirrf_id

                    try: s5002_basesirrf_dados['tpvalor'] = basesIrrf.tpValor.cdata
                    except AttributeError: pass
                    try: s5002_basesirrf_dados['valor'] = basesIrrf.valor.cdata
                    except AttributeError: pass
                    insert = create_insert('s5002_basesirrf', s5002_basesirrf_dados)
                    resp = executar_sql(insert, True)
                    s5002_basesirrf_id = resp[0][0]
                    #print s5002_basesirrf_id

            if 'irrf' in dir(infoIrrf) and infoIrrf.irrf.cdata != '':
                for irrf in infoIrrf.irrf:
                    s5002_irrf_dados = {}
                    s5002_irrf_dados['s5002_infoirrf_id'] = s5002_infoirrf_id

                    try: s5002_irrf_dados['tpcr'] = irrf.tpCR.cdata
                    except AttributeError: pass
                    try: s5002_irrf_dados['vrirrfdesc'] = irrf.vrIrrfDesc.cdata
                    except AttributeError: pass
                    insert = create_insert('s5002_irrf', s5002_irrf_dados)
                    resp = executar_sql(insert, True)
                    s5002_irrf_id = resp[0][0]
                    #print s5002_irrf_id

            if 'idePgtoExt' in dir(infoIrrf) and infoIrrf.idePgtoExt.cdata != '':
                for idePgtoExt in infoIrrf.idePgtoExt:
                    s5002_idepgtoext_dados = {}
                    s5002_idepgtoext_dados['s5002_infoirrf_id'] = s5002_infoirrf_id

                    try: s5002_idepgtoext_dados['codpais'] = idePgtoExt.idePais.codPais.cdata
                    except AttributeError: pass
                    try: s5002_idepgtoext_dados['indnif'] = idePgtoExt.idePais.indNIF.cdata
                    except AttributeError: pass
                    try: s5002_idepgtoext_dados['nifbenef'] = idePgtoExt.idePais.nifBenef.cdata
                    except AttributeError: pass
                    try: s5002_idepgtoext_dados['dsclograd'] = idePgtoExt.endExt.dscLograd.cdata
                    except AttributeError: pass
                    try: s5002_idepgtoext_dados['nrlograd'] = idePgtoExt.endExt.nrLograd.cdata
                    except AttributeError: pass
                    try: s5002_idepgtoext_dados['complem'] = idePgtoExt.endExt.complem.cdata
                    except AttributeError: pass
                    try: s5002_idepgtoext_dados['bairro'] = idePgtoExt.endExt.bairro.cdata
                    except AttributeError: pass
                    try: s5002_idepgtoext_dados['nmcid'] = idePgtoExt.endExt.nmCid.cdata
                    except AttributeError: pass
                    try: s5002_idepgtoext_dados['codpostal'] = idePgtoExt.endExt.codPostal.cdata
                    except AttributeError: pass
                    insert = create_insert('s5002_idepgtoext', s5002_idepgtoext_dados)
                    resp = executar_sql(insert, True)
                    s5002_idepgtoext_id = resp[0][0]
                    #print s5002_idepgtoext_id

    from emensageriapro.esocial.views.s5002_evtirrfbenef_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s5002_evtirrfbenef_id, 'default')
    return dados