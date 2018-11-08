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
from emensageriapro.padrao import ler_arquivo


def validacoes_s2220_evtmonit(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtMonit = doc.eSocial.evtMonit

    if 'indRetif' in dir(evtMonit.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideEvento.indRetif', evtMonit.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtMonit.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideEvento.nrRecibo', evtMonit.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtMonit.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideEvento.tpAmb', evtMonit.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtMonit.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideEvento.procEmi', evtMonit.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtMonit.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideEvento.verProc', evtMonit.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtMonit.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideEmpregador.tpInsc', evtMonit.ideEmpregador.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtMonit.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideEmpregador.nrInsc', evtMonit.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtMonit.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideVinculo.cpfTrab', evtMonit.ideVinculo.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtMonit.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideVinculo.nisTrab', evtMonit.ideVinculo.nisTrab.cdata, 0, '')
    if 'matricula' in dir(evtMonit.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideVinculo.matricula', evtMonit.ideVinculo.matricula.cdata, 0, '')
    if 'codCateg' in dir(evtMonit.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideVinculo.codCateg', evtMonit.ideVinculo.codCateg.cdata, 0, '')
    if 'tpExameOcup' in dir(evtMonit.exMedOcup): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.exMedOcup.tpExameOcup', evtMonit.exMedOcup.tpExameOcup.cdata, 1, '0;1;2;3;4;9')
    if 'dtAso' in dir(evtMonit.exMedOcup.aso): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.exMedOcup.aso.dtAso', evtMonit.exMedOcup.aso.dtAso.cdata, 1, '')
    if 'tpAso' in dir(evtMonit.exMedOcup.aso): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.exMedOcup.aso.tpAso', evtMonit.exMedOcup.aso.tpAso.cdata, 1, '0;1;2;3;4;8')
    if 'resAso' in dir(evtMonit.exMedOcup.aso): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.exMedOcup.aso.resAso', evtMonit.exMedOcup.aso.resAso.cdata, 1, '1;2')
    if 'cpfMed' in dir(evtMonit.exMedOcup.aso.medico): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.exMedOcup.aso.medico.cpfMed', evtMonit.exMedOcup.aso.medico.cpfMed.cdata, 0, '')
    if 'nisMed' in dir(evtMonit.exMedOcup.aso.medico): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.exMedOcup.aso.medico.nisMed', evtMonit.exMedOcup.aso.medico.nisMed.cdata, 0, '')
    if 'nmMed' in dir(evtMonit.exMedOcup.aso.medico): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.exMedOcup.aso.medico.nmMed', evtMonit.exMedOcup.aso.medico.nmMed.cdata, 1, '')
    if 'nrCRM' in dir(evtMonit.exMedOcup.aso.medico): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.exMedOcup.aso.medico.nrCRM', evtMonit.exMedOcup.aso.medico.nrCRM.cdata, 1, '')
    if 'ufCRM' in dir(evtMonit.exMedOcup.aso.medico): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.exMedOcup.aso.medico.ufCRM', evtMonit.exMedOcup.aso.medico.ufCRM.cdata, 1, '')
    if 'nisResp' in dir(evtMonit.exMedOcup.respMonit): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.exMedOcup.respMonit.nisResp', evtMonit.exMedOcup.respMonit.nisResp.cdata, 1, '')
    if 'nrConsClasse' in dir(evtMonit.exMedOcup.respMonit): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.exMedOcup.respMonit.nrConsClasse', evtMonit.exMedOcup.respMonit.nrConsClasse.cdata, 1, '')
    if 'ufConsClasse' in dir(evtMonit.exMedOcup.respMonit): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.exMedOcup.respMonit.ufConsClasse', evtMonit.exMedOcup.respMonit.ufConsClasse.cdata, 0, '')
    if 'cpfResp' in dir(evtMonit.exMedOcup.respMonit): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.exMedOcup.respMonit.cpfResp', evtMonit.exMedOcup.respMonit.cpfResp.cdata, 0, '')
    if 'nmResp' in dir(evtMonit.exMedOcup.respMonit): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.exMedOcup.respMonit.nmResp', evtMonit.exMedOcup.respMonit.nmResp.cdata, 1, '')
    if 'nrCRM' in dir(evtMonit.exMedOcup.respMonit): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.exMedOcup.respMonit.nrCRM', evtMonit.exMedOcup.respMonit.nrCRM.cdata, 1, '')
    if 'ufCRM' in dir(evtMonit.exMedOcup.respMonit): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.exMedOcup.respMonit.ufCRM', evtMonit.exMedOcup.respMonit.ufCRM.cdata, 1, '')
    if 'exame' in dir(evtMonit.exMedOcup.aso):
        for exame in evtMonit.exMedOcup.aso.exame:
       
            if 'dtExm' in dir(exame): validacoes_lista = validar_campo(validacoes_lista,'exame.dtExm', exame.dtExm.cdata, 1, '')
            if 'procRealizado' in dir(exame): validacoes_lista = validar_campo(validacoes_lista,'exame.procRealizado', exame.procRealizado.cdata, 1, '')
            if 'obsProc' in dir(exame): validacoes_lista = validar_campo(validacoes_lista,'exame.obsProc', exame.obsProc.cdata, 0, '')
            if 'interprExm' in dir(exame): validacoes_lista = validar_campo(validacoes_lista,'exame.interprExm', exame.interprExm.cdata, 1, '1;2;3')
            if 'ordExame' in dir(exame): validacoes_lista = validar_campo(validacoes_lista,'exame.ordExame', exame.ordExame.cdata, 1, '1;2')
            if 'dtIniMonit' in dir(exame): validacoes_lista = validar_campo(validacoes_lista,'exame.dtIniMonit', exame.dtIniMonit.cdata, 1, '')
            if 'dtFimMonit' in dir(exame): validacoes_lista = validar_campo(validacoes_lista,'exame.dtFimMonit', exame.dtFimMonit.cdata, 0, '')
            if 'indResult' in dir(exame): validacoes_lista = validar_campo(validacoes_lista,'exame.indResult', exame.indResult.cdata, 0, '1;2;3;4')

    return validacoes_lista