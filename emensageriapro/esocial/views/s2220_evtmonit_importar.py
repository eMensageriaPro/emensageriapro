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



def read_s2220_evtmonit_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2220_evtmonit_obj(doc, status, validar)
    return dados

def read_s2220_evtmonit(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2220_evtmonit_obj(doc, status, validar)
    return dados



def read_s2220_evtmonit_obj(doc, status, validar=False):
    s2220_evtmonit_dados = {}
    s2220_evtmonit_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2220_evtmonit_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2220_evtmonit_dados['identidade'] = doc.eSocial.evtMonit['Id']
    evtMonit = doc.eSocial.evtMonit

    if 'indRetif' in dir(evtMonit.ideEvento): s2220_evtmonit_dados['indretif'] = evtMonit.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtMonit.ideEvento): s2220_evtmonit_dados['nrrecibo'] = evtMonit.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtMonit.ideEvento): s2220_evtmonit_dados['tpamb'] = evtMonit.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtMonit.ideEvento): s2220_evtmonit_dados['procemi'] = evtMonit.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtMonit.ideEvento): s2220_evtmonit_dados['verproc'] = evtMonit.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtMonit.ideEmpregador): s2220_evtmonit_dados['tpinsc'] = evtMonit.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtMonit.ideEmpregador): s2220_evtmonit_dados['nrinsc'] = evtMonit.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtMonit.ideVinculo): s2220_evtmonit_dados['cpftrab'] = evtMonit.ideVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtMonit.ideVinculo): s2220_evtmonit_dados['nistrab'] = evtMonit.ideVinculo.nisTrab.cdata
    if 'matricula' in dir(evtMonit.ideVinculo): s2220_evtmonit_dados['matricula'] = evtMonit.ideVinculo.matricula.cdata
    if 'codCateg' in dir(evtMonit.ideVinculo): s2220_evtmonit_dados['codcateg'] = evtMonit.ideVinculo.codCateg.cdata
    if 'tpExameOcup' in dir(evtMonit.exMedOcup): s2220_evtmonit_dados['tpexameocup'] = evtMonit.exMedOcup.tpExameOcup.cdata
    if 'dtAso' in dir(evtMonit.exMedOcup.aso): s2220_evtmonit_dados['dtaso'] = evtMonit.exMedOcup.aso.dtAso.cdata
    if 'tpAso' in dir(evtMonit.exMedOcup.aso): s2220_evtmonit_dados['tpaso'] = evtMonit.exMedOcup.aso.tpAso.cdata
    if 'resAso' in dir(evtMonit.exMedOcup.aso): s2220_evtmonit_dados['resaso'] = evtMonit.exMedOcup.aso.resAso.cdata
    if 'cpfMed' in dir(evtMonit.exMedOcup.aso.medico): s2220_evtmonit_dados['cpfmed'] = evtMonit.exMedOcup.aso.medico.cpfMed.cdata
    if 'nisMed' in dir(evtMonit.exMedOcup.aso.medico): s2220_evtmonit_dados['nismed'] = evtMonit.exMedOcup.aso.medico.nisMed.cdata
    if 'nmMed' in dir(evtMonit.exMedOcup.aso.medico): s2220_evtmonit_dados['nmmed'] = evtMonit.exMedOcup.aso.medico.nmMed.cdata
    if 'nrCRM' in dir(evtMonit.exMedOcup.aso.medico): s2220_evtmonit_dados['nrcrm'] = evtMonit.exMedOcup.aso.medico.nrCRM.cdata
    if 'ufCRM' in dir(evtMonit.exMedOcup.aso.medico): s2220_evtmonit_dados['ufcrm'] = evtMonit.exMedOcup.aso.medico.ufCRM.cdata
    if 'nisResp' in dir(evtMonit.exMedOcup.respMonit): s2220_evtmonit_dados['nisresp'] = evtMonit.exMedOcup.respMonit.nisResp.cdata
    if 'nrConsClasse' in dir(evtMonit.exMedOcup.respMonit): s2220_evtmonit_dados['nrconsclasse'] = evtMonit.exMedOcup.respMonit.nrConsClasse.cdata
    if 'ufConsClasse' in dir(evtMonit.exMedOcup.respMonit): s2220_evtmonit_dados['ufconsclasse'] = evtMonit.exMedOcup.respMonit.ufConsClasse.cdata
    if 'cpfResp' in dir(evtMonit.exMedOcup.respMonit): s2220_evtmonit_dados['cpfresp'] = evtMonit.exMedOcup.respMonit.cpfResp.cdata
    if 'nmResp' in dir(evtMonit.exMedOcup.respMonit): s2220_evtmonit_dados['nmresp'] = evtMonit.exMedOcup.respMonit.nmResp.cdata
    if 'nrCRM' in dir(evtMonit.exMedOcup.respMonit): s2220_evtmonit_dados['nrcrm'] = evtMonit.exMedOcup.respMonit.nrCRM.cdata
    if 'ufCRM' in dir(evtMonit.exMedOcup.respMonit): s2220_evtmonit_dados['ufcrm'] = evtMonit.exMedOcup.respMonit.ufCRM.cdata
    if 'inclusao' in dir(evtMonit.exMedOcup): s2220_evtmonit_dados['operacao'] = 1
    elif 'alteracao' in dir(evtMonit.exMedOcup): s2220_evtmonit_dados['operacao'] = 2
    elif 'exclusao' in dir(evtMonit.exMedOcup): s2220_evtmonit_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2220_evtmonit', s2220_evtmonit_dados)
    resp = executar_sql(insert, True)
    s2220_evtmonit_id = resp[0][0]
    dados = s2220_evtmonit_dados
    dados['evento'] = 's2220'
    dados['id'] = s2220_evtmonit_id
    dados['identidade_evento'] = doc.eSocial.evtMonit['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'exame' in dir(evtMonit.exMedOcup.aso):
        for exame in evtMonit.exMedOcup.aso.exame:
            s2220_exame_dados = {}
            s2220_exame_dados['s2220_evtmonit_id'] = s2220_evtmonit_id

            if 'dtExm' in dir(exame): s2220_exame_dados['dtexm'] = exame.dtExm.cdata
            if 'procRealizado' in dir(exame): s2220_exame_dados['procrealizado'] = exame.procRealizado.cdata
            if 'obsProc' in dir(exame): s2220_exame_dados['obsproc'] = exame.obsProc.cdata
            if 'interprExm' in dir(exame): s2220_exame_dados['interprexm'] = exame.interprExm.cdata
            if 'ordExame' in dir(exame): s2220_exame_dados['ordexame'] = exame.ordExame.cdata
            if 'dtIniMonit' in dir(exame): s2220_exame_dados['dtinimonit'] = exame.dtIniMonit.cdata
            if 'dtFimMonit' in dir(exame): s2220_exame_dados['dtfimmonit'] = exame.dtFimMonit.cdata
            if 'indResult' in dir(exame): s2220_exame_dados['indresult'] = exame.indResult.cdata
            insert = create_insert('s2220_exame', s2220_exame_dados)
            resp = executar_sql(insert, True)
            s2220_exame_id = resp[0][0]
            #print s2220_exame_id

    from emensageriapro.esocial.views.s2220_evtmonit_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2220_evtmonit_id, 'default')
    return dados