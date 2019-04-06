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



def read_r9000_evtexclusao_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r9000_evtexclusao_obj(doc, status, validar)
    return dados

def read_r9000_evtexclusao(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r9000_evtexclusao_obj(doc, status, validar)
    return dados



def read_r9000_evtexclusao_obj(doc, status, validar=False):
    r9000_evtexclusao_dados = {}
    r9000_evtexclusao_dados['status'] = status
    xmlns_lista = doc.Reinf['xmlns'].split('/')
    r9000_evtexclusao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r9000_evtexclusao_dados['identidade'] = doc.Reinf.evtExclusao['id']
    evtExclusao = doc.Reinf.evtExclusao

    try: r9000_evtexclusao_dados['tpamb'] = evtExclusao.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: r9000_evtexclusao_dados['procemi'] = evtExclusao.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: r9000_evtexclusao_dados['verproc'] = evtExclusao.ideEvento.verProc.cdata
    except AttributeError: pass
    try: r9000_evtexclusao_dados['tpinsc'] = evtExclusao.ideContri.tpInsc.cdata
    except AttributeError: pass
    try: r9000_evtexclusao_dados['nrinsc'] = evtExclusao.ideContri.nrInsc.cdata
    except AttributeError: pass
    try: r9000_evtexclusao_dados['tpevento'] = evtExclusao.infoExclusao.tpEvento.cdata
    except AttributeError: pass
    try: r9000_evtexclusao_dados['nrrecevt'] = evtExclusao.infoExclusao.nrRecEvt.cdata
    except AttributeError: pass
    try: r9000_evtexclusao_dados['perapur'] = evtExclusao.infoExclusao.perApur.cdata
    except AttributeError: pass
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
    dados['status'] = STATUS_EVENTO_IMPORTADO

    from emensageriapro.efdreinf.views.r9000_evtexclusao_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r9000_evtexclusao_id, 'default')
    return dados