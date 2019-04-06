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


def validacoes_s2250_evtavprevio(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtAvPrevio = doc.eSocial.evtAvPrevio

    if 'indRetif' in dir(evtAvPrevio.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAvPrevio.ideEvento.indRetif', evtAvPrevio.ideEvento.indRetif.cdata, 1, u'1;2')
    if 'nrRecibo' in dir(evtAvPrevio.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAvPrevio.ideEvento.nrRecibo', evtAvPrevio.ideEvento.nrRecibo.cdata, 0, u'')
    if 'tpAmb' in dir(evtAvPrevio.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAvPrevio.ideEvento.tpAmb', evtAvPrevio.ideEvento.tpAmb.cdata, 1, u'1;2')
    if 'procEmi' in dir(evtAvPrevio.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAvPrevio.ideEvento.procEmi', evtAvPrevio.ideEvento.procEmi.cdata, 1, u'1;2;3;4;5')
    if 'verProc' in dir(evtAvPrevio.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAvPrevio.ideEvento.verProc', evtAvPrevio.ideEvento.verProc.cdata, 1, u'')
    if 'tpInsc' in dir(evtAvPrevio.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAvPrevio.ideEmpregador.tpInsc', evtAvPrevio.ideEmpregador.tpInsc.cdata, 1, u'1;2;3;4')
    if 'nrInsc' in dir(evtAvPrevio.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAvPrevio.ideEmpregador.nrInsc', evtAvPrevio.ideEmpregador.nrInsc.cdata, 1, u'')
    if 'cpfTrab' in dir(evtAvPrevio.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAvPrevio.ideVinculo.cpfTrab', evtAvPrevio.ideVinculo.cpfTrab.cdata, 1, u'')
    if 'nisTrab' in dir(evtAvPrevio.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAvPrevio.ideVinculo.nisTrab', evtAvPrevio.ideVinculo.nisTrab.cdata, 1, u'')
    if 'matricula' in dir(evtAvPrevio.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAvPrevio.ideVinculo.matricula', evtAvPrevio.ideVinculo.matricula.cdata, 1, u'')
    if 'detAvPrevio' in dir(evtAvPrevio.infoAvPrevio):
        for detAvPrevio in evtAvPrevio.infoAvPrevio.detAvPrevio:

            if 'dtAvPrv' in dir(detAvPrevio): validacoes_lista = validar_campo(validacoes_lista,'detAvPrevio.dtAvPrv', detAvPrevio.dtAvPrv.cdata, 1, u'')
            if 'dtPrevDeslig' in dir(detAvPrevio): validacoes_lista = validar_campo(validacoes_lista,'detAvPrevio.dtPrevDeslig', detAvPrevio.dtPrevDeslig.cdata, 1, u'')
            if 'tpAvPrevio' in dir(detAvPrevio): validacoes_lista = validar_campo(validacoes_lista,'detAvPrevio.tpAvPrevio', detAvPrevio.tpAvPrevio.cdata, 1, u'1;2;4;5')
            if 'observacao' in dir(detAvPrevio): validacoes_lista = validar_campo(validacoes_lista,'detAvPrevio.observacao', detAvPrevio.observacao.cdata, 0, u'')

    if 'cancAvPrevio' in dir(evtAvPrevio.infoAvPrevio):
        for cancAvPrevio in evtAvPrevio.infoAvPrevio.cancAvPrevio:

            if 'dtCancAvPrv' in dir(cancAvPrevio): validacoes_lista = validar_campo(validacoes_lista,'cancAvPrevio.dtCancAvPrv', cancAvPrevio.dtCancAvPrv.cdata, 1, u'')
            if 'observacao' in dir(cancAvPrevio): validacoes_lista = validar_campo(validacoes_lista,'cancAvPrevio.observacao', cancAvPrevio.observacao.cdata, 0, u'')
            if 'mtvCancAvPrevio' in dir(cancAvPrevio): validacoes_lista = validar_campo(validacoes_lista,'cancAvPrevio.mtvCancAvPrevio', cancAvPrevio.mtvCancAvPrevio.cdata, 1, u'1;2;3;9')

    return validacoes_lista