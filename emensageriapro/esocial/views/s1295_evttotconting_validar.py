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


def validacoes_s1295_evttotconting(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTotConting = doc.eSocial.evtTotConting

    if 'indApuracao' in dir(evtTotConting.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTotConting.ideEvento.indApuracao', evtTotConting.ideEvento.indApuracao.cdata, 1, '1;2')
    if 'perApur' in dir(evtTotConting.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTotConting.ideEvento.perApur', evtTotConting.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtTotConting.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTotConting.ideEvento.tpAmb', evtTotConting.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtTotConting.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTotConting.ideEvento.procEmi', evtTotConting.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtTotConting.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTotConting.ideEvento.verProc', evtTotConting.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtTotConting.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTotConting.ideEmpregador.tpInsc', evtTotConting.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtTotConting.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTotConting.ideEmpregador.nrInsc', evtTotConting.ideEmpregador.nrInsc.cdata, 1, '')
    if 'ideRespInf' in dir(evtTotConting):
        for ideRespInf in evtTotConting.ideRespInf:

            if 'nmResp' in dir(ideRespInf): validacoes_lista = validar_campo(validacoes_lista,'ideRespInf.nmResp', ideRespInf.nmResp.cdata, 1, '')
            if 'cpfResp' in dir(ideRespInf): validacoes_lista = validar_campo(validacoes_lista,'ideRespInf.cpfResp', ideRespInf.cpfResp.cdata, 1, '')
            if 'telefone' in dir(ideRespInf): validacoes_lista = validar_campo(validacoes_lista,'ideRespInf.telefone', ideRespInf.telefone.cdata, 1, '')
            if 'email' in dir(ideRespInf): validacoes_lista = validar_campo(validacoes_lista,'ideRespInf.email', ideRespInf.email.cdata, 0, '')

    return validacoes_lista