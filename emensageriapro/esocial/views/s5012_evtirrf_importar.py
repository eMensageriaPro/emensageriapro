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



def read_s5012_evtirrf_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s5012_evtirrf_obj(doc, status, validar)
    return dados

def read_s5012_evtirrf(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s5012_evtirrf_obj(doc, status, validar)
    return dados



def read_s5012_evtirrf_obj(doc, status, validar=False):
    s5012_evtirrf_dados = {}
    s5012_evtirrf_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s5012_evtirrf_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5012_evtirrf_dados['identidade'] = doc.eSocial.evtIrrf['Id']
    evtIrrf = doc.eSocial.evtIrrf

    try: s5012_evtirrf_dados['perapur'] = evtIrrf.ideEvento.perApur.cdata
    except AttributeError: pass
    try: s5012_evtirrf_dados['tpinsc'] = evtIrrf.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s5012_evtirrf_dados['nrinsc'] = evtIrrf.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s5012_evtirrf_dados['nrrecarqbase'] = evtIrrf.infoIRRF.nrRecArqBase.cdata
    except AttributeError: pass
    try: s5012_evtirrf_dados['indexistinfo'] = evtIrrf.infoIRRF.indExistInfo.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtIrrf.infoIRRF): s5012_evtirrf_dados['operacao'] = 1
    elif 'alteracao' in dir(evtIrrf.infoIRRF): s5012_evtirrf_dados['operacao'] = 2
    elif 'exclusao' in dir(evtIrrf.infoIRRF): s5012_evtirrf_dados['operacao'] = 3
    #print dados
    insert = create_insert('s5012_evtirrf', s5012_evtirrf_dados)
    resp = executar_sql(insert, True)
    s5012_evtirrf_id = resp[0][0]
    dados = s5012_evtirrf_dados
    dados['evento'] = 's5012'
    dados['id'] = s5012_evtirrf_id
    dados['identidade_evento'] = doc.eSocial.evtIrrf['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'infoCRContrib' in dir(evtIrrf.infoIRRF) and evtIrrf.infoIRRF.infoCRContrib.cdata != '':
        for infoCRContrib in evtIrrf.infoIRRF.infoCRContrib:
            s5012_infocrcontrib_dados = {}
            s5012_infocrcontrib_dados['s5012_evtirrf_id'] = s5012_evtirrf_id

            try: s5012_infocrcontrib_dados['tpcr'] = infoCRContrib.tpCR.cdata
            except AttributeError: pass
            try: s5012_infocrcontrib_dados['vrcr'] = infoCRContrib.vrCR.cdata
            except AttributeError: pass
            insert = create_insert('s5012_infocrcontrib', s5012_infocrcontrib_dados)
            resp = executar_sql(insert, True)
            s5012_infocrcontrib_id = resp[0][0]
            #print s5012_infocrcontrib_id

    from emensageriapro.esocial.views.s5012_evtirrf_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s5012_evtirrf_id, 'default')
    return dados