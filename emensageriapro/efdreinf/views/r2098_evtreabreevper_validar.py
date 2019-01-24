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


def validacoes_r2098_evtreabreevper(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtReabreEvPer = doc.Reinf.evtReabreEvPer

    if 'perApur' in dir(evtReabreEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideEvento.perApur', evtReabreEvPer.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtReabreEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideEvento.tpAmb', evtReabreEvPer.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtReabreEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideEvento.procEmi', evtReabreEvPer.ideEvento.procEmi.cdata, 1, '1;2')
    if 'verProc' in dir(evtReabreEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideEvento.verProc', evtReabreEvPer.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtReabreEvPer.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideContri.tpInsc', evtReabreEvPer.ideContri.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtReabreEvPer.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideContri.nrInsc', evtReabreEvPer.ideContri.nrInsc.cdata, 1, '')
    return validacoes_lista