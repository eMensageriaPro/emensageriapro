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


def validacoes_s2221_evttoxic(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtToxic = doc.eSocial.evtToxic

    if 'indRetif' in dir(evtToxic.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtToxic.ideEvento.indRetif', evtToxic.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtToxic.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtToxic.ideEvento.nrRecibo', evtToxic.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtToxic.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtToxic.ideEvento.tpAmb', evtToxic.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtToxic.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtToxic.ideEvento.procEmi', evtToxic.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtToxic.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtToxic.ideEvento.verProc', evtToxic.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtToxic.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtToxic.ideEmpregador.tpInsc', evtToxic.ideEmpregador.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtToxic.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtToxic.ideEmpregador.nrInsc', evtToxic.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtToxic.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtToxic.ideVinculo.cpfTrab', evtToxic.ideVinculo.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtToxic.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtToxic.ideVinculo.nisTrab', evtToxic.ideVinculo.nisTrab.cdata, 0, '')
    if 'matricula' in dir(evtToxic.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtToxic.ideVinculo.matricula', evtToxic.ideVinculo.matricula.cdata, 0, '')
    if 'codCateg' in dir(evtToxic.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtToxic.ideVinculo.codCateg', evtToxic.ideVinculo.codCateg.cdata, 0, '')
    if 'dtExame' in dir(evtToxic.toxicologico): validacoes_lista = validar_campo(validacoes_lista,'evtToxic.toxicologico.dtExame', evtToxic.toxicologico.dtExame.cdata, 1, '')
    if 'cnpjLab' in dir(evtToxic.toxicologico): validacoes_lista = validar_campo(validacoes_lista,'evtToxic.toxicologico.cnpjLab', evtToxic.toxicologico.cnpjLab.cdata, 1, '')
    if 'codSeqExame' in dir(evtToxic.toxicologico): validacoes_lista = validar_campo(validacoes_lista,'evtToxic.toxicologico.codSeqExame', evtToxic.toxicologico.codSeqExame.cdata, 1, '')
    if 'nmMed' in dir(evtToxic.toxicologico): validacoes_lista = validar_campo(validacoes_lista,'evtToxic.toxicologico.nmMed', evtToxic.toxicologico.nmMed.cdata, 1, '')
    if 'nrCRM' in dir(evtToxic.toxicologico): validacoes_lista = validar_campo(validacoes_lista,'evtToxic.toxicologico.nrCRM', evtToxic.toxicologico.nrCRM.cdata, 1, '')
    if 'ufCRM' in dir(evtToxic.toxicologico): validacoes_lista = validar_campo(validacoes_lista,'evtToxic.toxicologico.ufCRM', evtToxic.toxicologico.ufCRM.cdata, 1, '')
    return validacoes_lista