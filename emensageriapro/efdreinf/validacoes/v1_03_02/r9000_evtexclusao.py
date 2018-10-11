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


def validacoes_r9000_evtexclusao(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtExclusao = doc.Reinf.evtExclusao
    
    if 'tpAmb' in dir(evtExclusao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.ideEvento.tpAmb', evtExclusao.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtExclusao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.ideEvento.procEmi', evtExclusao.ideEvento.procEmi.cdata, 1, '1;2')
    if 'verProc' in dir(evtExclusao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.ideEvento.verProc', evtExclusao.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtExclusao.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.ideContri.tpInsc', evtExclusao.ideContri.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtExclusao.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.ideContri.nrInsc', evtExclusao.ideContri.nrInsc.cdata, 1, '')
    if 'tpEvento' in dir(evtExclusao.infoExclusao): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.infoExclusao.tpEvento', evtExclusao.infoExclusao.tpEvento.cdata, 1, '')
    if 'nrRecEvt' in dir(evtExclusao.infoExclusao): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.infoExclusao.nrRecEvt', evtExclusao.infoExclusao.nrRecEvt.cdata, 1, '')
    if 'perApur' in dir(evtExclusao.infoExclusao): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.infoExclusao.perApur', evtExclusao.infoExclusao.perApur.cdata, 1, '')
    return validacoes_lista