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


def validacoes_s1300_evtcontrsindpatr(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtContrSindPatr = doc.eSocial.evtContrSindPatr

    if 'indRetif' in dir(evtContrSindPatr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEvento.indRetif', evtContrSindPatr.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtContrSindPatr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEvento.nrRecibo', evtContrSindPatr.ideEvento.nrRecibo.cdata, 0, '')
    if 'indApuracao' in dir(evtContrSindPatr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEvento.indApuracao', evtContrSindPatr.ideEvento.indApuracao.cdata, 1, '1;2')
    if 'perApur' in dir(evtContrSindPatr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEvento.perApur', evtContrSindPatr.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtContrSindPatr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEvento.tpAmb', evtContrSindPatr.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtContrSindPatr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEvento.procEmi', evtContrSindPatr.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtContrSindPatr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEvento.verProc', evtContrSindPatr.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtContrSindPatr.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEmpregador.tpInsc', evtContrSindPatr.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtContrSindPatr.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEmpregador.nrInsc', evtContrSindPatr.ideEmpregador.nrInsc.cdata, 1, '')
    if 'contribSind' in dir(evtContrSindPatr):
        for contribSind in evtContrSindPatr.contribSind:
       
            if 'cnpjSindic' in dir(contribSind): validacoes_lista = validar_campo(validacoes_lista,'contribSind.cnpjSindic', contribSind.cnpjSindic.cdata, 1, '')
            if 'tpContribSind' in dir(contribSind): validacoes_lista = validar_campo(validacoes_lista,'contribSind.tpContribSind', contribSind.tpContribSind.cdata, 1, '1;2;3;4')
            if 'vlrContribSind' in dir(contribSind): validacoes_lista = validar_campo(validacoes_lista,'contribSind.vlrContribSind', contribSind.vlrContribSind.cdata, 1, '')

    return validacoes_lista