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


def validacoes_s2231_evtcessao(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtCessao = doc.eSocial.evtCessao
    
    if 'indRetif' in dir(evtCessao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCessao.ideEvento.indRetif', evtCessao.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtCessao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCessao.ideEvento.nrRecibo', evtCessao.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtCessao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCessao.ideEvento.tpAmb', evtCessao.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtCessao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCessao.ideEvento.procEmi', evtCessao.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtCessao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCessao.ideEvento.verProc', evtCessao.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtCessao.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCessao.ideEmpregador.tpInsc', evtCessao.ideEmpregador.tpInsc.cdata, 1, '')
    if 'nrInsc' in dir(evtCessao.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCessao.ideEmpregador.nrInsc', evtCessao.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtCessao.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtCessao.ideVinculo.cpfTrab', evtCessao.ideVinculo.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtCessao.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtCessao.ideVinculo.nisTrab', evtCessao.ideVinculo.nisTrab.cdata, 1, '')
    if 'matricula' in dir(evtCessao.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtCessao.ideVinculo.matricula', evtCessao.ideVinculo.matricula.cdata, 1, '')
    if 'iniCessao' in dir(evtCessao.infoCessao):
        for iniCessao in evtCessao.infoCessao.iniCessao:
            
            if 'dtIniCessao' in dir(iniCessao): validacoes_lista = validar_campo(validacoes_lista,'iniCessao.dtIniCessao', iniCessao.dtIniCessao.cdata, 1, '')
            if 'cnpjCess' in dir(iniCessao): validacoes_lista = validar_campo(validacoes_lista,'iniCessao.cnpjCess', iniCessao.cnpjCess.cdata, 1, '')
            if 'infOnus' in dir(iniCessao): validacoes_lista = validar_campo(validacoes_lista,'iniCessao.infOnus', iniCessao.infOnus.cdata, 1, '1;2;3;4')
            if 'indCessao' in dir(iniCessao): validacoes_lista = validar_campo(validacoes_lista,'iniCessao.indCessao', iniCessao.indCessao.cdata, 1, '1;2;3')
            if 'dscSituacao' in dir(iniCessao): validacoes_lista = validar_campo(validacoes_lista,'iniCessao.dscSituacao', iniCessao.dscSituacao.cdata, 0, '')

    if 'fimCessao' in dir(evtCessao.infoCessao):
        for fimCessao in evtCessao.infoCessao.fimCessao:
            
            if 'dtTermCessao' in dir(fimCessao): validacoes_lista = validar_campo(validacoes_lista,'fimCessao.dtTermCessao', fimCessao.dtTermCessao.cdata, 1, '')

    return validacoes_lista