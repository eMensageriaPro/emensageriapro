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


def validacoes_s2245_evttreicap(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTreiCap = doc.eSocial.evtTreiCap

    if 'indRetif' in dir(evtTreiCap.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTreiCap.ideEvento.indRetif', evtTreiCap.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtTreiCap.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTreiCap.ideEvento.nrRecibo', evtTreiCap.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtTreiCap.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTreiCap.ideEvento.tpAmb', evtTreiCap.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtTreiCap.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTreiCap.ideEvento.procEmi', evtTreiCap.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtTreiCap.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTreiCap.ideEvento.verProc', evtTreiCap.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtTreiCap.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTreiCap.ideEmpregador.tpInsc', evtTreiCap.ideEmpregador.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtTreiCap.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTreiCap.ideEmpregador.nrInsc', evtTreiCap.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtTreiCap.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtTreiCap.ideVinculo.cpfTrab', evtTreiCap.ideVinculo.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtTreiCap.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtTreiCap.ideVinculo.nisTrab', evtTreiCap.ideVinculo.nisTrab.cdata, 0, '')
    if 'matricula' in dir(evtTreiCap.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtTreiCap.ideVinculo.matricula', evtTreiCap.ideVinculo.matricula.cdata, 0, '')
    if 'codCateg' in dir(evtTreiCap.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtTreiCap.ideVinculo.codCateg', evtTreiCap.ideVinculo.codCateg.cdata, 0, '')
    if 'codTreiCap' in dir(evtTreiCap.treiCap): validacoes_lista = validar_campo(validacoes_lista,'evtTreiCap.treiCap.codTreiCap', evtTreiCap.treiCap.codTreiCap.cdata, 1, '')
    if 'obsTreiCap' in dir(evtTreiCap.treiCap): validacoes_lista = validar_campo(validacoes_lista,'evtTreiCap.treiCap.obsTreiCap', evtTreiCap.treiCap.obsTreiCap.cdata, 0, '')
    if 'observacao' in dir(evtTreiCap.treiCap): validacoes_lista = validar_campo(validacoes_lista,'evtTreiCap.treiCap.observacao', evtTreiCap.treiCap.observacao.cdata, 0, '')
    if 'infoComplem' in dir(evtTreiCap.treiCap):
        for infoComplem in evtTreiCap.treiCap.infoComplem:

            if 'dtTreiCap' in dir(infoComplem): validacoes_lista = validar_campo(validacoes_lista,'infoComplem.dtTreiCap', infoComplem.dtTreiCap.cdata, 1, '')
            if 'durTreiCap' in dir(infoComplem): validacoes_lista = validar_campo(validacoes_lista,'infoComplem.durTreiCap', infoComplem.durTreiCap.cdata, 1, '')
            if 'modTreiCap' in dir(infoComplem): validacoes_lista = validar_campo(validacoes_lista,'infoComplem.modTreiCap', infoComplem.modTreiCap.cdata, 1, '1;2;3')
            if 'tpTreiCap' in dir(infoComplem): validacoes_lista = validar_campo(validacoes_lista,'infoComplem.tpTreiCap', infoComplem.tpTreiCap.cdata, 1, '1;2;3;4;5')

            if 'ideProfResp' in dir(infoComplem):
                for ideProfResp in infoComplem.ideProfResp:

                    if 'cpfProf' in dir(ideProfResp): validacoes_lista = validar_campo(validacoes_lista,'ideProfResp.cpfProf', ideProfResp.cpfProf.cdata, 0, '')
                    if 'nmProf' in dir(ideProfResp): validacoes_lista = validar_campo(validacoes_lista,'ideProfResp.nmProf', ideProfResp.nmProf.cdata, 1, '')
                    if 'tpProf' in dir(ideProfResp): validacoes_lista = validar_campo(validacoes_lista,'ideProfResp.tpProf', ideProfResp.tpProf.cdata, 1, '1;2')
                    if 'formProf' in dir(ideProfResp): validacoes_lista = validar_campo(validacoes_lista,'ideProfResp.formProf', ideProfResp.formProf.cdata, 1, '')
                    if 'codCBO' in dir(ideProfResp): validacoes_lista = validar_campo(validacoes_lista,'ideProfResp.codCBO', ideProfResp.codCBO.cdata, 1, '')
                    if 'nacProf' in dir(ideProfResp): validacoes_lista = validar_campo(validacoes_lista,'ideProfResp.nacProf', ideProfResp.nacProf.cdata, 1, '1;2')

    return validacoes_lista