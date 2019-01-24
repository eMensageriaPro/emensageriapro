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


def validacoes_s5012_evtirrf(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtIrrf = doc.eSocial.evtIrrf

    if 'perApur' in dir(evtIrrf.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtIrrf.ideEvento.perApur', evtIrrf.ideEvento.perApur.cdata, 1, '')
    if 'tpInsc' in dir(evtIrrf.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtIrrf.ideEmpregador.tpInsc', evtIrrf.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtIrrf.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtIrrf.ideEmpregador.nrInsc', evtIrrf.ideEmpregador.nrInsc.cdata, 1, '')
    if 'nrRecArqBase' in dir(evtIrrf.infoIRRF): validacoes_lista = validar_campo(validacoes_lista,'evtIrrf.infoIRRF.nrRecArqBase', evtIrrf.infoIRRF.nrRecArqBase.cdata, 1, '')
    if 'indExistInfo' in dir(evtIrrf.infoIRRF): validacoes_lista = validar_campo(validacoes_lista,'evtIrrf.infoIRRF.indExistInfo', evtIrrf.infoIRRF.indExistInfo.cdata, 1, '1;2;3')
    if 'infoCRContrib' in dir(evtIrrf.infoIRRF):
        for infoCRContrib in evtIrrf.infoIRRF.infoCRContrib:

            if 'tpCR' in dir(infoCRContrib): validacoes_lista = validar_campo(validacoes_lista,'infoCRContrib.tpCR', infoCRContrib.tpCR.cdata, 1, '047301;056107;056108;056109;056110;056111;056112;056113;058806;061001;3533;356201')
            if 'vrCR' in dir(infoCRContrib): validacoes_lista = validar_campo(validacoes_lista,'infoCRContrib.vrCR', infoCRContrib.vrCR.cdata, 1, '')

    return validacoes_lista