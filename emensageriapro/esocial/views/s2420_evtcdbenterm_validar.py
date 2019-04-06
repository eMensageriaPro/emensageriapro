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


def validacoes_s2420_evtcdbenterm(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtCdBenTerm = doc.eSocial.evtCdBenTerm

    if 'indRetif' in dir(evtCdBenTerm.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenTerm.ideEvento.indRetif', evtCdBenTerm.ideEvento.indRetif.cdata, 1, u'1;2')
    if 'nrRecibo' in dir(evtCdBenTerm.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenTerm.ideEvento.nrRecibo', evtCdBenTerm.ideEvento.nrRecibo.cdata, 0, u'')
    if 'tpAmb' in dir(evtCdBenTerm.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenTerm.ideEvento.tpAmb', evtCdBenTerm.ideEvento.tpAmb.cdata, 1, u'1;2')
    if 'procEmi' in dir(evtCdBenTerm.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenTerm.ideEvento.procEmi', evtCdBenTerm.ideEvento.procEmi.cdata, 1, u'1;2;3;4;5')
    if 'verProc' in dir(evtCdBenTerm.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenTerm.ideEvento.verProc', evtCdBenTerm.ideEvento.verProc.cdata, 1, u'')
    if 'tpInsc' in dir(evtCdBenTerm.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenTerm.ideEmpregador.tpInsc', evtCdBenTerm.ideEmpregador.tpInsc.cdata, 1, u'1')
    if 'nrInsc' in dir(evtCdBenTerm.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenTerm.ideEmpregador.nrInsc', evtCdBenTerm.ideEmpregador.nrInsc.cdata, 1, u'')
    if 'cpfBenef' in dir(evtCdBenTerm.ideBeneficio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenTerm.ideBeneficio.cpfBenef', evtCdBenTerm.ideBeneficio.cpfBenef.cdata, 1, u'')
    if 'nrBeneficio' in dir(evtCdBenTerm.ideBeneficio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenTerm.ideBeneficio.nrBeneficio', evtCdBenTerm.ideBeneficio.nrBeneficio.cdata, 1, u'')
    if 'dtTermBeneficio' in dir(evtCdBenTerm.infoBenTermino): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenTerm.infoBenTermino.dtTermBeneficio', evtCdBenTerm.infoBenTermino.dtTermBeneficio.cdata, 1, u'')
    if 'mtvTermino' in dir(evtCdBenTerm.infoBenTermino): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenTerm.infoBenTermino.mtvTermino', evtCdBenTerm.infoBenTermino.mtvTermino.cdata, 1, u'')
    return validacoes_lista