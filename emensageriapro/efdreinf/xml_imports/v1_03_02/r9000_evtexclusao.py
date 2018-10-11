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



def read_r9000_evtexclusao(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    read_r9000_evtexclusao_obj(doc, status)
    


def read_r9000_evtexclusao_obj(doc, status):
    r9000_evtexclusao_dados = {}
    r9000_evtexclusao_dados['versao'] = 'v1_03_02'
    r9000_evtexclusao_dados['status'] = status
    r9000_evtexclusao_dados['identidade'] = doc.Reinf.evtExclusao['id']
    r9000_evtexclusao_dados['processamento_codigo_resposta'] = 1
    evtExclusao = doc.Reinf.evtExclusao
    
    if 'tpAmb' in dir(evtExclusao.ideEvento): r9000_evtexclusao_dados['tpamb'] = evtExclusao.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtExclusao.ideEvento): r9000_evtexclusao_dados['procemi'] = evtExclusao.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtExclusao.ideEvento): r9000_evtexclusao_dados['verproc'] = evtExclusao.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtExclusao.ideContri): r9000_evtexclusao_dados['tpinsc'] = evtExclusao.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtExclusao.ideContri): r9000_evtexclusao_dados['nrinsc'] = evtExclusao.ideContri.nrInsc.cdata
    if 'tpEvento' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['tpevento'] = evtExclusao.infoExclusao.tpEvento.cdata
    if 'nrRecEvt' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['nrrecevt'] = evtExclusao.infoExclusao.nrRecEvt.cdata
    if 'perApur' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['perapur'] = evtExclusao.infoExclusao.perApur.cdata
    if 'inclusao' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['operacao'] = 1
    elif 'alteracao' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['operacao'] = 2
    elif 'exclusao' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['operacao'] = 3
    #print dados
    insert = create_insert('r9000_evtexclusao', r9000_evtexclusao_dados)
    resp = executar_sql(insert, True)
    r9000_evtexclusao_id = resp[0][0]
    dados = r9000_evtexclusao_dados
    dados['evento'] = 'r9000'
    dados['id'] = r9000_evtexclusao_id
    dados['identidade_evento'] = doc.Reinf.evtExclusao['id']
    dados['status'] = 1


    from emensageriapro.efdreinf.views.r9000_evtexclusao_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r9000_evtexclusao_id, 'default')
    return dados