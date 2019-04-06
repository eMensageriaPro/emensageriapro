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


def validacoes_s2190_evtadmprelim(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtAdmPrelim = doc.eSocial.evtAdmPrelim

    if 'tpAmb' in dir(evtAdmPrelim.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmPrelim.ideEvento.tpAmb', evtAdmPrelim.ideEvento.tpAmb.cdata, 1, u'1;2')
    if 'procEmi' in dir(evtAdmPrelim.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmPrelim.ideEvento.procEmi', evtAdmPrelim.ideEvento.procEmi.cdata, 1, u'1;2;3;4;5')
    if 'verProc' in dir(evtAdmPrelim.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmPrelim.ideEvento.verProc', evtAdmPrelim.ideEvento.verProc.cdata, 1, u'')
    if 'tpInsc' in dir(evtAdmPrelim.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAdmPrelim.ideEmpregador.tpInsc', evtAdmPrelim.ideEmpregador.tpInsc.cdata, 1, u'1;2;3;4')
    if 'nrInsc' in dir(evtAdmPrelim.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAdmPrelim.ideEmpregador.nrInsc', evtAdmPrelim.ideEmpregador.nrInsc.cdata, 1, u'')
    if 'cpfTrab' in dir(evtAdmPrelim.infoRegPrelim): validacoes_lista = validar_campo(validacoes_lista,'evtAdmPrelim.infoRegPrelim.cpfTrab', evtAdmPrelim.infoRegPrelim.cpfTrab.cdata, 1, u'')
    if 'dtNascto' in dir(evtAdmPrelim.infoRegPrelim): validacoes_lista = validar_campo(validacoes_lista,'evtAdmPrelim.infoRegPrelim.dtNascto', evtAdmPrelim.infoRegPrelim.dtNascto.cdata, 1, u'')
    if 'dtAdm' in dir(evtAdmPrelim.infoRegPrelim): validacoes_lista = validar_campo(validacoes_lista,'evtAdmPrelim.infoRegPrelim.dtAdm', evtAdmPrelim.infoRegPrelim.dtAdm.cdata, 1, u'')
    return validacoes_lista