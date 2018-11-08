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


def read_s1295_evttotconting_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s1295_evttotconting_obj(doc, status, validar)
    return dados

def read_s1295_evttotconting(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s1295_evttotconting_obj(doc, status, validar)
    return dados



def read_s1295_evttotconting_obj(doc, status, validar=False):
    s1295_evttotconting_dados = {}
    s1295_evttotconting_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1295_evttotconting_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1295_evttotconting_dados['identidade'] = doc.eSocial.evtTotConting['Id']
    s1295_evttotconting_dados['processamento_codigo_resposta'] = 1
    evtTotConting = doc.eSocial.evtTotConting

    if 'indApuracao' in dir(evtTotConting.ideEvento): s1295_evttotconting_dados['indapuracao'] = evtTotConting.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtTotConting.ideEvento): s1295_evttotconting_dados['perapur'] = evtTotConting.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtTotConting.ideEvento): s1295_evttotconting_dados['tpamb'] = evtTotConting.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTotConting.ideEvento): s1295_evttotconting_dados['procemi'] = evtTotConting.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTotConting.ideEvento): s1295_evttotconting_dados['verproc'] = evtTotConting.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTotConting.ideEmpregador): s1295_evttotconting_dados['tpinsc'] = evtTotConting.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTotConting.ideEmpregador): s1295_evttotconting_dados['nrinsc'] = evtTotConting.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtTotConting.ideRespInf): s1295_evttotconting_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTotConting.ideRespInf): s1295_evttotconting_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTotConting.ideRespInf): s1295_evttotconting_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1295_evttotconting', s1295_evttotconting_dados)
    resp = executar_sql(insert, True)
    s1295_evttotconting_id = resp[0][0]
    dados = s1295_evttotconting_dados
    dados['evento'] = 's1295'
    dados['id'] = s1295_evttotconting_id
    dados['identidade_evento'] = doc.eSocial.evtTotConting['Id']
    dados['status'] = 1

    if 'ideRespInf' in dir(evtTotConting):
        for ideRespInf in evtTotConting.ideRespInf:
            s1295_iderespinf_dados = {}
            s1295_iderespinf_dados['s1295_evttotconting_id'] = s1295_evttotconting_id
       
            if 'nmResp' in dir(ideRespInf): s1295_iderespinf_dados['nmresp'] = ideRespInf.nmResp.cdata
            if 'cpfResp' in dir(ideRespInf): s1295_iderespinf_dados['cpfresp'] = ideRespInf.cpfResp.cdata
            if 'telefone' in dir(ideRespInf): s1295_iderespinf_dados['telefone'] = ideRespInf.telefone.cdata
            if 'email' in dir(ideRespInf): s1295_iderespinf_dados['email'] = ideRespInf.email.cdata
            insert = create_insert('s1295_iderespinf', s1295_iderespinf_dados)
            resp = executar_sql(insert, True)
            s1295_iderespinf_id = resp[0][0]
            #print s1295_iderespinf_id

    from emensageriapro.esocial.views.s1295_evttotconting_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1295_evttotconting_id, 'default')
    return dados