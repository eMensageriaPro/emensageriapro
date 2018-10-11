#coding:utf-8
"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos<www.emensageria.com.br>
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


def read_s2420_evtcdbenterm(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    read_s2420_evtcdbenterm_obj(doc, status)



def read_s2420_evtcdbenterm_obj(doc):
    s2420_evtcdbenterm_dados = {}
    s2420_evtcdbenterm_dados['versao'] = 'v02_04_02'
    s2420_evtcdbenterm_dados['status'] = status
    s2420_evtcdbenterm_dados['identidade'] = doc.eSocial.evtCdBenTerm['Id']
    s2420_evtcdbenterm_dados['processamento_codigo_resposta'] = 1
    evtCdBenTerm = doc.eSocial.evtCdBenTerm
    
    if 'indRetif' in dir(evtCdBenTerm.ideEvento): s2420_evtcdbenterm_dados['indretif'] = evtCdBenTerm.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtCdBenTerm.ideEvento): s2420_evtcdbenterm_dados['nrrecibo'] = evtCdBenTerm.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtCdBenTerm.ideEvento): s2420_evtcdbenterm_dados['tpamb'] = evtCdBenTerm.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtCdBenTerm.ideEvento): s2420_evtcdbenterm_dados['procemi'] = evtCdBenTerm.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtCdBenTerm.ideEvento): s2420_evtcdbenterm_dados['verproc'] = evtCdBenTerm.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtCdBenTerm.ideEmpregador): s2420_evtcdbenterm_dados['tpinsc'] = evtCdBenTerm.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtCdBenTerm.ideEmpregador): s2420_evtcdbenterm_dados['nrinsc'] = evtCdBenTerm.ideEmpregador.nrInsc.cdata
    if 'cpfBenef' in dir(evtCdBenTerm.ideBeneficio): s2420_evtcdbenterm_dados['cpfbenef'] = evtCdBenTerm.ideBeneficio.cpfBenef.cdata
    if 'nrBeneficio' in dir(evtCdBenTerm.ideBeneficio): s2420_evtcdbenterm_dados['nrbeneficio'] = evtCdBenTerm.ideBeneficio.nrBeneficio.cdata
    if 'dtTermBeneficio' in dir(evtCdBenTerm.infoBenTermino): s2420_evtcdbenterm_dados['dttermbeneficio'] = evtCdBenTerm.infoBenTermino.dtTermBeneficio.cdata
    if 'mtvTermino' in dir(evtCdBenTerm.infoBenTermino): s2420_evtcdbenterm_dados['mtvtermino'] = evtCdBenTerm.infoBenTermino.mtvTermino.cdata
    if 'inclusao' in dir(evtCdBenTerm.infoBenTermino): s2420_evtcdbenterm_dados['operacao'] = 1
    elif 'alteracao' in dir(evtCdBenTerm.infoBenTermino): s2420_evtcdbenterm_dados['operacao'] = 2
    elif 'exclusao' in dir(evtCdBenTerm.infoBenTermino): s2420_evtcdbenterm_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2420_evtcdbenterm', s2420_evtcdbenterm_dados)
    resp = executar_sql(insert, True)
    s2420_evtcdbenterm_id = resp[0][0]
    dados = s2420_evtcdbenterm_dados
    dados['evento'] = 's2420'
    dados['id'] = s2420_evtcdbenterm_id
    dados['identidade_evento'] = doc.eSocial.evtCdBenTerm['Id']
    dados['status'] = 1

    from emensageriapro.esocial.views.s2420_evtcdbenterm_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2420_evtcdbenterm_id, 'default')
    return dados