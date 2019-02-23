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



def read_s2250_evtavprevio_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2250_evtavprevio_obj(doc, status, validar)
    return dados

def read_s2250_evtavprevio(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2250_evtavprevio_obj(doc, status, validar)
    return dados



def read_s2250_evtavprevio_obj(doc, status, validar=False):
    s2250_evtavprevio_dados = {}
    s2250_evtavprevio_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2250_evtavprevio_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2250_evtavprevio_dados['identidade'] = doc.eSocial.evtAvPrevio['Id']
    s2250_evtavprevio_dados['processamento_codigo_resposta'] = 1
    evtAvPrevio = doc.eSocial.evtAvPrevio

    if 'indRetif' in dir(evtAvPrevio.ideEvento): s2250_evtavprevio_dados['indretif'] = evtAvPrevio.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtAvPrevio.ideEvento): s2250_evtavprevio_dados['nrrecibo'] = evtAvPrevio.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtAvPrevio.ideEvento): s2250_evtavprevio_dados['tpamb'] = evtAvPrevio.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtAvPrevio.ideEvento): s2250_evtavprevio_dados['procemi'] = evtAvPrevio.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtAvPrevio.ideEvento): s2250_evtavprevio_dados['verproc'] = evtAvPrevio.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtAvPrevio.ideEmpregador): s2250_evtavprevio_dados['tpinsc'] = evtAvPrevio.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtAvPrevio.ideEmpregador): s2250_evtavprevio_dados['nrinsc'] = evtAvPrevio.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtAvPrevio.ideVinculo): s2250_evtavprevio_dados['cpftrab'] = evtAvPrevio.ideVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtAvPrevio.ideVinculo): s2250_evtavprevio_dados['nistrab'] = evtAvPrevio.ideVinculo.nisTrab.cdata
    if 'matricula' in dir(evtAvPrevio.ideVinculo): s2250_evtavprevio_dados['matricula'] = evtAvPrevio.ideVinculo.matricula.cdata
    if 'inclusao' in dir(evtAvPrevio.infoAvPrevio): s2250_evtavprevio_dados['operacao'] = 1
    elif 'alteracao' in dir(evtAvPrevio.infoAvPrevio): s2250_evtavprevio_dados['operacao'] = 2
    elif 'exclusao' in dir(evtAvPrevio.infoAvPrevio): s2250_evtavprevio_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2250_evtavprevio', s2250_evtavprevio_dados)
    resp = executar_sql(insert, True)
    s2250_evtavprevio_id = resp[0][0]
    dados = s2250_evtavprevio_dados
    dados['evento'] = 's2250'
    dados['id'] = s2250_evtavprevio_id
    dados['identidade_evento'] = doc.eSocial.evtAvPrevio['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'detAvPrevio' in dir(evtAvPrevio.infoAvPrevio):
        for detAvPrevio in evtAvPrevio.infoAvPrevio.detAvPrevio:
            s2250_detavprevio_dados = {}
            s2250_detavprevio_dados['s2250_evtavprevio_id'] = s2250_evtavprevio_id

            if 'dtAvPrv' in dir(detAvPrevio): s2250_detavprevio_dados['dtavprv'] = detAvPrevio.dtAvPrv.cdata
            if 'dtPrevDeslig' in dir(detAvPrevio): s2250_detavprevio_dados['dtprevdeslig'] = detAvPrevio.dtPrevDeslig.cdata
            if 'tpAvPrevio' in dir(detAvPrevio): s2250_detavprevio_dados['tpavprevio'] = detAvPrevio.tpAvPrevio.cdata
            if 'observacao' in dir(detAvPrevio): s2250_detavprevio_dados['observacao'] = detAvPrevio.observacao.cdata
            insert = create_insert('s2250_detavprevio', s2250_detavprevio_dados)
            resp = executar_sql(insert, True)
            s2250_detavprevio_id = resp[0][0]
            #print s2250_detavprevio_id

    if 'cancAvPrevio' in dir(evtAvPrevio.infoAvPrevio):
        for cancAvPrevio in evtAvPrevio.infoAvPrevio.cancAvPrevio:
            s2250_cancavprevio_dados = {}
            s2250_cancavprevio_dados['s2250_evtavprevio_id'] = s2250_evtavprevio_id

            if 'dtCancAvPrv' in dir(cancAvPrevio): s2250_cancavprevio_dados['dtcancavprv'] = cancAvPrevio.dtCancAvPrv.cdata
            if 'observacao' in dir(cancAvPrevio): s2250_cancavprevio_dados['observacao'] = cancAvPrevio.observacao.cdata
            if 'mtvCancAvPrevio' in dir(cancAvPrevio): s2250_cancavprevio_dados['mtvcancavprevio'] = cancAvPrevio.mtvCancAvPrevio.cdata
            insert = create_insert('s2250_cancavprevio', s2250_cancavprevio_dados)
            resp = executar_sql(insert, True)
            s2250_cancavprevio_id = resp[0][0]
            #print s2250_cancavprevio_id

    from emensageriapro.esocial.views.s2250_evtavprevio_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2250_evtavprevio_id, 'default')
    return dados