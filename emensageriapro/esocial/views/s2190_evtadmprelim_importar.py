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


def read_s2190_evtadmprelim_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2190_evtadmprelim_obj(doc, status, validar)
    return dados

def read_s2190_evtadmprelim(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2190_evtadmprelim_obj(doc, status, validar)
    return dados



def read_s2190_evtadmprelim_obj(doc, status, validar=False):
    s2190_evtadmprelim_dados = {}
    s2190_evtadmprelim_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2190_evtadmprelim_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2190_evtadmprelim_dados['identidade'] = doc.eSocial.evtAdmPrelim['Id']
    s2190_evtadmprelim_dados['processamento_codigo_resposta'] = 1
    evtAdmPrelim = doc.eSocial.evtAdmPrelim

    if 'tpAmb' in dir(evtAdmPrelim.ideEvento): s2190_evtadmprelim_dados['tpamb'] = evtAdmPrelim.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtAdmPrelim.ideEvento): s2190_evtadmprelim_dados['procemi'] = evtAdmPrelim.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtAdmPrelim.ideEvento): s2190_evtadmprelim_dados['verproc'] = evtAdmPrelim.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtAdmPrelim.ideEmpregador): s2190_evtadmprelim_dados['tpinsc'] = evtAdmPrelim.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtAdmPrelim.ideEmpregador): s2190_evtadmprelim_dados['nrinsc'] = evtAdmPrelim.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['cpftrab'] = evtAdmPrelim.infoRegPrelim.cpfTrab.cdata
    if 'dtNascto' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['dtnascto'] = evtAdmPrelim.infoRegPrelim.dtNascto.cdata
    if 'dtAdm' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['dtadm'] = evtAdmPrelim.infoRegPrelim.dtAdm.cdata
    if 'inclusao' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['operacao'] = 1
    elif 'alteracao' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['operacao'] = 2
    elif 'exclusao' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2190_evtadmprelim', s2190_evtadmprelim_dados)
    resp = executar_sql(insert, True)
    s2190_evtadmprelim_id = resp[0][0]
    dados = s2190_evtadmprelim_dados
    dados['evento'] = 's2190'
    dados['id'] = s2190_evtadmprelim_id
    dados['identidade_evento'] = doc.eSocial.evtAdmPrelim['Id']
    dados['status'] = 1

    from emensageriapro.esocial.views.s2190_evtadmprelim_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2190_evtadmprelim_id, 'default')
    return dados