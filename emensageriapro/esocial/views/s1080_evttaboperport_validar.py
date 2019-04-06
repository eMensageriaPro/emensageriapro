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


def validacoes_s1080_evttaboperport(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabOperPort = doc.eSocial.evtTabOperPort

    if 'tpAmb' in dir(evtTabOperPort.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabOperPort.ideEvento.tpAmb', evtTabOperPort.ideEvento.tpAmb.cdata, 1, u'1;2')
    if 'procEmi' in dir(evtTabOperPort.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabOperPort.ideEvento.procEmi', evtTabOperPort.ideEvento.procEmi.cdata, 1, u'1;2;3;4;5')
    if 'verProc' in dir(evtTabOperPort.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabOperPort.ideEvento.verProc', evtTabOperPort.ideEvento.verProc.cdata, 1, u'')
    if 'tpInsc' in dir(evtTabOperPort.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabOperPort.ideEmpregador.tpInsc', evtTabOperPort.ideEmpregador.tpInsc.cdata, 1, u'1;2;3;4')
    if 'nrInsc' in dir(evtTabOperPort.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabOperPort.ideEmpregador.nrInsc', evtTabOperPort.ideEmpregador.nrInsc.cdata, 1, u'')
    if 'inclusao' in dir(evtTabOperPort.infoOperPortuario):
        for inclusao in evtTabOperPort.infoOperPortuario.inclusao:

            if 'cnpjOpPortuario' in dir(inclusao.ideOperPortuario): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideOperPortuario.cnpjOpPortuario', inclusao.ideOperPortuario.cnpjOpPortuario.cdata, 1, u'')
            if 'iniValid' in dir(inclusao.ideOperPortuario): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideOperPortuario.iniValid', inclusao.ideOperPortuario.iniValid.cdata, 1, u'')
            if 'fimValid' in dir(inclusao.ideOperPortuario): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideOperPortuario.fimValid', inclusao.ideOperPortuario.fimValid.cdata, 0, u'')
            if 'aliqRat' in dir(inclusao.dadosOperPortuario): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosOperPortuario.aliqRat', inclusao.dadosOperPortuario.aliqRat.cdata, 1, u'1;2;3')
            if 'fap' in dir(inclusao.dadosOperPortuario): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosOperPortuario.fap', inclusao.dadosOperPortuario.fap.cdata, 1, u'')
            if 'aliqRatAjust' in dir(inclusao.dadosOperPortuario): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosOperPortuario.aliqRatAjust', inclusao.dadosOperPortuario.aliqRatAjust.cdata, 1, u'')

    if 'alteracao' in dir(evtTabOperPort.infoOperPortuario):
        for alteracao in evtTabOperPort.infoOperPortuario.alteracao:

            if 'cnpjOpPortuario' in dir(alteracao.ideOperPortuario): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideOperPortuario.cnpjOpPortuario', alteracao.ideOperPortuario.cnpjOpPortuario.cdata, 1, u'')
            if 'iniValid' in dir(alteracao.ideOperPortuario): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideOperPortuario.iniValid', alteracao.ideOperPortuario.iniValid.cdata, 1, u'')
            if 'fimValid' in dir(alteracao.ideOperPortuario): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideOperPortuario.fimValid', alteracao.ideOperPortuario.fimValid.cdata, 0, u'')
            if 'aliqRat' in dir(alteracao.dadosOperPortuario): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosOperPortuario.aliqRat', alteracao.dadosOperPortuario.aliqRat.cdata, 1, u'1;2;3')
            if 'fap' in dir(alteracao.dadosOperPortuario): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosOperPortuario.fap', alteracao.dadosOperPortuario.fap.cdata, 1, u'')
            if 'aliqRatAjust' in dir(alteracao.dadosOperPortuario): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosOperPortuario.aliqRatAjust', alteracao.dadosOperPortuario.aliqRatAjust.cdata, 1, u'')

            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:

                    if 'iniValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.iniValid', novaValidade.iniValid.cdata, 1, u'')
                    if 'fimValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.fimValid', novaValidade.fimValid.cdata, 0, u'')

    if 'exclusao' in dir(evtTabOperPort.infoOperPortuario):
        for exclusao in evtTabOperPort.infoOperPortuario.exclusao:

            if 'cnpjOpPortuario' in dir(exclusao.ideOperPortuario): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideOperPortuario.cnpjOpPortuario', exclusao.ideOperPortuario.cnpjOpPortuario.cdata, 1, u'')
            if 'iniValid' in dir(exclusao.ideOperPortuario): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideOperPortuario.iniValid', exclusao.ideOperPortuario.iniValid.cdata, 1, u'')
            if 'fimValid' in dir(exclusao.ideOperPortuario): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideOperPortuario.fimValid', exclusao.ideOperPortuario.fimValid.cdata, 0, u'')

    return validacoes_lista