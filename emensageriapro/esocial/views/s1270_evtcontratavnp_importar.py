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



def read_s1270_evtcontratavnp_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1270_evtcontratavnp_obj(doc, status, validar)
    return dados

def read_s1270_evtcontratavnp(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1270_evtcontratavnp_obj(doc, status, validar)
    return dados



def read_s1270_evtcontratavnp_obj(doc, status, validar=False):
    s1270_evtcontratavnp_dados = {}
    s1270_evtcontratavnp_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1270_evtcontratavnp_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1270_evtcontratavnp_dados['identidade'] = doc.eSocial.evtContratAvNP['Id']
    evtContratAvNP = doc.eSocial.evtContratAvNP

    try: s1270_evtcontratavnp_dados['indretif'] = evtContratAvNP.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s1270_evtcontratavnp_dados['nrrecibo'] = evtContratAvNP.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s1270_evtcontratavnp_dados['indapuracao'] = evtContratAvNP.ideEvento.indApuracao.cdata
    except AttributeError: pass
    try: s1270_evtcontratavnp_dados['perapur'] = evtContratAvNP.ideEvento.perApur.cdata
    except AttributeError: pass
    try: s1270_evtcontratavnp_dados['tpamb'] = evtContratAvNP.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s1270_evtcontratavnp_dados['procemi'] = evtContratAvNP.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s1270_evtcontratavnp_dados['verproc'] = evtContratAvNP.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s1270_evtcontratavnp_dados['tpinsc'] = evtContratAvNP.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s1270_evtcontratavnp_dados['nrinsc'] = evtContratAvNP.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
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
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'remunAvNP' in dir(evtContratAvNP) and evtContratAvNP.remunAvNP.cdata != '':
        for remunAvNP in evtContratAvNP.remunAvNP:
            s1270_remunavnp_dados = {}
            s1270_remunavnp_dados['s1270_evtcontratavnp_id'] = s1270_evtcontratavnp_id

            try: s1270_remunavnp_dados['tpinsc'] = remunAvNP.tpInsc.cdata
            except AttributeError: pass
            try: s1270_remunavnp_dados['nrinsc'] = remunAvNP.nrInsc.cdata
            except AttributeError: pass
            try: s1270_remunavnp_dados['codlotacao'] = remunAvNP.codLotacao.cdata
            except AttributeError: pass
            try: s1270_remunavnp_dados['vrbccp00'] = remunAvNP.vrBcCp00.cdata
            except AttributeError: pass
            try: s1270_remunavnp_dados['vrbccp15'] = remunAvNP.vrBcCp15.cdata
            except AttributeError: pass
            try: s1270_remunavnp_dados['vrbccp20'] = remunAvNP.vrBcCp20.cdata
            except AttributeError: pass
            try: s1270_remunavnp_dados['vrbccp25'] = remunAvNP.vrBcCp25.cdata
            except AttributeError: pass
            try: s1270_remunavnp_dados['vrbccp13'] = remunAvNP.vrBcCp13.cdata
            except AttributeError: pass
            try: s1270_remunavnp_dados['vrbcfgts'] = remunAvNP.vrBcFgts.cdata
            except AttributeError: pass
            try: s1270_remunavnp_dados['vrdesccp'] = remunAvNP.vrDescCP.cdata
            except AttributeError: pass
            insert = create_insert('s1270_remunavnp', s1270_remunavnp_dados)
            resp = executar_sql(insert, True)
            s1270_remunavnp_id = resp[0][0]
            #print s1270_remunavnp_id

    from emensageriapro.esocial.views.s1270_evtcontratavnp_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1270_evtcontratavnp_id, 'default')
    return dados