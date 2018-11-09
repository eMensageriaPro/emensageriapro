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


def validacoes_s3000_evtexclusao(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtExclusao = doc.eSocial.evtExclusao

    if 'tpAmb' in dir(evtExclusao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.ideEvento.tpAmb', evtExclusao.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtExclusao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.ideEvento.procEmi', evtExclusao.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtExclusao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.ideEvento.verProc', evtExclusao.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtExclusao.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.ideEmpregador.tpInsc', evtExclusao.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtExclusao.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.ideEmpregador.nrInsc', evtExclusao.ideEmpregador.nrInsc.cdata, 1, '')
    if 'tpEvento' in dir(evtExclusao.infoExclusao): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.infoExclusao.tpEvento', evtExclusao.infoExclusao.tpEvento.cdata, 1, 'S-1000;S-1005;S-1010;S-1020;S-1030;S-1035;S-1040;S-1050;S-1060;S-1070;S-1080;S-1200;S-1202;S-1207;S-1210;S-1250;S-1260;S-1270;S-1280;S-1295;S-1298;S-1299;S-1300;S-2190;S-2200;S-2205;S-2206;S-2210;S-2220;S-2230;S-2240;S-2241;S-2250;S-2260;S-2298;S-2299;S-2300;S-2306;S-2399;S-2400;S-3000;S-5001;S-5002;S-5011;S-5012')
    if 'nrRecEvt' in dir(evtExclusao.infoExclusao): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.infoExclusao.nrRecEvt', evtExclusao.infoExclusao.nrRecEvt.cdata, 1, '')
    if 'ideTrabalhador' in dir(evtExclusao.infoExclusao):
        for ideTrabalhador in evtExclusao.infoExclusao.ideTrabalhador:
       
            if 'cpfTrab' in dir(ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'ideTrabalhador.cpfTrab', ideTrabalhador.cpfTrab.cdata, 1, '')
            if 'nisTrab' in dir(ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'ideTrabalhador.nisTrab', ideTrabalhador.nisTrab.cdata, 0, '')

    if 'ideFolhaPagto' in dir(evtExclusao.infoExclusao):
        for ideFolhaPagto in evtExclusao.infoExclusao.ideFolhaPagto:
       
            if 'indApuracao' in dir(ideFolhaPagto): validacoes_lista = validar_campo(validacoes_lista,'ideFolhaPagto.indApuracao', ideFolhaPagto.indApuracao.cdata, 1, '1;2')
            if 'perApur' in dir(ideFolhaPagto): validacoes_lista = validar_campo(validacoes_lista,'ideFolhaPagto.perApur', ideFolhaPagto.perApur.cdata, 1, '')

    return validacoes_lista