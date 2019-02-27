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



def read_s1300_evtcontrsindpatr_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1300_evtcontrsindpatr_obj(doc, status, validar)
    return dados

def read_s1300_evtcontrsindpatr(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1300_evtcontrsindpatr_obj(doc, status, validar)
    return dados



def read_s1300_evtcontrsindpatr_obj(doc, status, validar=False):
    s1300_evtcontrsindpatr_dados = {}
    s1300_evtcontrsindpatr_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1300_evtcontrsindpatr_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1300_evtcontrsindpatr_dados['identidade'] = doc.eSocial.evtContrSindPatr['Id']
    evtContrSindPatr = doc.eSocial.evtContrSindPatr

    if 'indRetif' in dir(evtContrSindPatr.ideEvento): s1300_evtcontrsindpatr_dados['indretif'] = evtContrSindPatr.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtContrSindPatr.ideEvento): s1300_evtcontrsindpatr_dados['nrrecibo'] = evtContrSindPatr.ideEvento.nrRecibo.cdata
    if 'indApuracao' in dir(evtContrSindPatr.ideEvento): s1300_evtcontrsindpatr_dados['indapuracao'] = evtContrSindPatr.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtContrSindPatr.ideEvento): s1300_evtcontrsindpatr_dados['perapur'] = evtContrSindPatr.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtContrSindPatr.ideEvento): s1300_evtcontrsindpatr_dados['tpamb'] = evtContrSindPatr.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtContrSindPatr.ideEvento): s1300_evtcontrsindpatr_dados['procemi'] = evtContrSindPatr.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtContrSindPatr.ideEvento): s1300_evtcontrsindpatr_dados['verproc'] = evtContrSindPatr.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtContrSindPatr.ideEmpregador): s1300_evtcontrsindpatr_dados['tpinsc'] = evtContrSindPatr.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtContrSindPatr.ideEmpregador): s1300_evtcontrsindpatr_dados['nrinsc'] = evtContrSindPatr.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtContrSindPatr.contribSind): s1300_evtcontrsindpatr_dados['operacao'] = 1
    elif 'alteracao' in dir(evtContrSindPatr.contribSind): s1300_evtcontrsindpatr_dados['operacao'] = 2
    elif 'exclusao' in dir(evtContrSindPatr.contribSind): s1300_evtcontrsindpatr_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1300_evtcontrsindpatr', s1300_evtcontrsindpatr_dados)
    resp = executar_sql(insert, True)
    s1300_evtcontrsindpatr_id = resp[0][0]
    dados = s1300_evtcontrsindpatr_dados
    dados['evento'] = 's1300'
    dados['id'] = s1300_evtcontrsindpatr_id
    dados['identidade_evento'] = doc.eSocial.evtContrSindPatr['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'contribSind' in dir(evtContrSindPatr):
        for contribSind in evtContrSindPatr.contribSind:
            s1300_contribsind_dados = {}
            s1300_contribsind_dados['s1300_evtcontrsindpatr_id'] = s1300_evtcontrsindpatr_id

            if 'cnpjSindic' in dir(contribSind): s1300_contribsind_dados['cnpjsindic'] = contribSind.cnpjSindic.cdata
            if 'tpContribSind' in dir(contribSind): s1300_contribsind_dados['tpcontribsind'] = contribSind.tpContribSind.cdata
            if 'vlrContribSind' in dir(contribSind): s1300_contribsind_dados['vlrcontribsind'] = contribSind.vlrContribSind.cdata
            insert = create_insert('s1300_contribsind', s1300_contribsind_dados)
            resp = executar_sql(insert, True)
            s1300_contribsind_id = resp[0][0]
            #print s1300_contribsind_id

    from emensageriapro.esocial.views.s1300_evtcontrsindpatr_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1300_evtcontrsindpatr_id, 'default')
    return dados