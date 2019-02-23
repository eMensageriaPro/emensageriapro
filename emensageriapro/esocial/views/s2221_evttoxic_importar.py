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



def read_s2221_evttoxic_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2221_evttoxic_obj(doc, status, validar)
    return dados

def read_s2221_evttoxic(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2221_evttoxic_obj(doc, status, validar)
    return dados



def read_s2221_evttoxic_obj(doc, status, validar=False):
    s2221_evttoxic_dados = {}
    s2221_evttoxic_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2221_evttoxic_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2221_evttoxic_dados['identidade'] = doc.eSocial.evtToxic['Id']
    s2221_evttoxic_dados['processamento_codigo_resposta'] = 1
    evtToxic = doc.eSocial.evtToxic

    if 'indRetif' in dir(evtToxic.ideEvento): s2221_evttoxic_dados['indretif'] = evtToxic.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtToxic.ideEvento): s2221_evttoxic_dados['nrrecibo'] = evtToxic.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtToxic.ideEvento): s2221_evttoxic_dados['tpamb'] = evtToxic.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtToxic.ideEvento): s2221_evttoxic_dados['procemi'] = evtToxic.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtToxic.ideEvento): s2221_evttoxic_dados['verproc'] = evtToxic.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtToxic.ideEmpregador): s2221_evttoxic_dados['tpinsc'] = evtToxic.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtToxic.ideEmpregador): s2221_evttoxic_dados['nrinsc'] = evtToxic.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtToxic.ideVinculo): s2221_evttoxic_dados['cpftrab'] = evtToxic.ideVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtToxic.ideVinculo): s2221_evttoxic_dados['nistrab'] = evtToxic.ideVinculo.nisTrab.cdata
    if 'matricula' in dir(evtToxic.ideVinculo): s2221_evttoxic_dados['matricula'] = evtToxic.ideVinculo.matricula.cdata
    if 'codCateg' in dir(evtToxic.ideVinculo): s2221_evttoxic_dados['codcateg'] = evtToxic.ideVinculo.codCateg.cdata
    if 'dtExame' in dir(evtToxic.toxicologico): s2221_evttoxic_dados['dtexame'] = evtToxic.toxicologico.dtExame.cdata
    if 'cnpjLab' in dir(evtToxic.toxicologico): s2221_evttoxic_dados['cnpjlab'] = evtToxic.toxicologico.cnpjLab.cdata
    if 'codSeqExame' in dir(evtToxic.toxicologico): s2221_evttoxic_dados['codseqexame'] = evtToxic.toxicologico.codSeqExame.cdata
    if 'nmMed' in dir(evtToxic.toxicologico): s2221_evttoxic_dados['nmmed'] = evtToxic.toxicologico.nmMed.cdata
    if 'nrCRM' in dir(evtToxic.toxicologico): s2221_evttoxic_dados['nrcrm'] = evtToxic.toxicologico.nrCRM.cdata
    if 'ufCRM' in dir(evtToxic.toxicologico): s2221_evttoxic_dados['ufcrm'] = evtToxic.toxicologico.ufCRM.cdata
    if 'indRecusa' in dir(evtToxic.toxicologico): s2221_evttoxic_dados['indrecusa'] = evtToxic.toxicologico.indRecusa.cdata
    if 'inclusao' in dir(evtToxic.toxicologico): s2221_evttoxic_dados['operacao'] = 1
    elif 'alteracao' in dir(evtToxic.toxicologico): s2221_evttoxic_dados['operacao'] = 2
    elif 'exclusao' in dir(evtToxic.toxicologico): s2221_evttoxic_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2221_evttoxic', s2221_evttoxic_dados)
    resp = executar_sql(insert, True)
    s2221_evttoxic_id = resp[0][0]
    dados = s2221_evttoxic_dados
    dados['evento'] = 's2221'
    dados['id'] = s2221_evttoxic_id
    dados['identidade_evento'] = doc.eSocial.evtToxic['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    from emensageriapro.esocial.views.s2221_evttoxic_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2221_evttoxic_id, 'default')
    return dados