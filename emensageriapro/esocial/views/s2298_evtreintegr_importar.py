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


def read_s2298_evtreintegr_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2298_evtreintegr_obj(doc, status, validar)
    return dados

def read_s2298_evtreintegr(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2298_evtreintegr_obj(doc, status, validar)
    return dados



def read_s2298_evtreintegr_obj(doc, status, validar=False):
    s2298_evtreintegr_dados = {}
    s2298_evtreintegr_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2298_evtreintegr_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2298_evtreintegr_dados['identidade'] = doc.eSocial.evtReintegr['Id']
    s2298_evtreintegr_dados['processamento_codigo_resposta'] = 1
    evtReintegr = doc.eSocial.evtReintegr

    if 'indRetif' in dir(evtReintegr.ideEvento): s2298_evtreintegr_dados['indretif'] = evtReintegr.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtReintegr.ideEvento): s2298_evtreintegr_dados['nrrecibo'] = evtReintegr.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtReintegr.ideEvento): s2298_evtreintegr_dados['tpamb'] = evtReintegr.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtReintegr.ideEvento): s2298_evtreintegr_dados['procemi'] = evtReintegr.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtReintegr.ideEvento): s2298_evtreintegr_dados['verproc'] = evtReintegr.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtReintegr.ideEmpregador): s2298_evtreintegr_dados['tpinsc'] = evtReintegr.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtReintegr.ideEmpregador): s2298_evtreintegr_dados['nrinsc'] = evtReintegr.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtReintegr.ideVinculo): s2298_evtreintegr_dados['cpftrab'] = evtReintegr.ideVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtReintegr.ideVinculo): s2298_evtreintegr_dados['nistrab'] = evtReintegr.ideVinculo.nisTrab.cdata
    if 'matricula' in dir(evtReintegr.ideVinculo): s2298_evtreintegr_dados['matricula'] = evtReintegr.ideVinculo.matricula.cdata
    if 'tpReint' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['tpreint'] = evtReintegr.infoReintegr.tpReint.cdata
    if 'nrProcJud' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['nrprocjud'] = evtReintegr.infoReintegr.nrProcJud.cdata
    if 'nrLeiAnistia' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['nrleianistia'] = evtReintegr.infoReintegr.nrLeiAnistia.cdata
    if 'dtEfetRetorno' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['dtefetretorno'] = evtReintegr.infoReintegr.dtEfetRetorno.cdata
    if 'dtEfeito' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['dtefeito'] = evtReintegr.infoReintegr.dtEfeito.cdata
    if 'indPagtoJuizo' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['indpagtojuizo'] = evtReintegr.infoReintegr.indPagtoJuizo.cdata
    if 'inclusao' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['operacao'] = 1
    elif 'alteracao' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['operacao'] = 2
    elif 'exclusao' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2298_evtreintegr', s2298_evtreintegr_dados)
    resp = executar_sql(insert, True)
    s2298_evtreintegr_id = resp[0][0]
    dados = s2298_evtreintegr_dados
    dados['evento'] = 's2298'
    dados['id'] = s2298_evtreintegr_id
    dados['identidade_evento'] = doc.eSocial.evtReintegr['Id']
    dados['status'] = 1

    from emensageriapro.esocial.views.s2298_evtreintegr_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2298_evtreintegr_id, 'default')
    return dados