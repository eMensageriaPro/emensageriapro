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


def validacoes_s1035_evttabcarreira(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabCarreira = doc.eSocial.evtTabCarreira

    if 'tpAmb' in dir(evtTabCarreira.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabCarreira.ideEvento.tpAmb', evtTabCarreira.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtTabCarreira.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabCarreira.ideEvento.procEmi', evtTabCarreira.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtTabCarreira.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabCarreira.ideEvento.verProc', evtTabCarreira.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtTabCarreira.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabCarreira.ideEmpregador.tpInsc', evtTabCarreira.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtTabCarreira.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabCarreira.ideEmpregador.nrInsc', evtTabCarreira.ideEmpregador.nrInsc.cdata, 1, '')
    if 'inclusao' in dir(evtTabCarreira.infoCarreira):
        for inclusao in evtTabCarreira.infoCarreira.inclusao:

            if 'codCarreira' in dir(inclusao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideCarreira.codCarreira', inclusao.ideCarreira.codCarreira.cdata, 1, '')
            if 'iniValid' in dir(inclusao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideCarreira.iniValid', inclusao.ideCarreira.iniValid.cdata, 1, '')
            if 'fimValid' in dir(inclusao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideCarreira.fimValid', inclusao.ideCarreira.fimValid.cdata, 0, '')
            if 'dscCarreira' in dir(inclusao.dadosCarreira): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosCarreira.dscCarreira', inclusao.dadosCarreira.dscCarreira.cdata, 1, '')
            if 'leiCarr' in dir(inclusao.dadosCarreira): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosCarreira.leiCarr', inclusao.dadosCarreira.leiCarr.cdata, 0, '')
            if 'dtLeiCarr' in dir(inclusao.dadosCarreira): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosCarreira.dtLeiCarr', inclusao.dadosCarreira.dtLeiCarr.cdata, 1, '')
            if 'sitCarr' in dir(inclusao.dadosCarreira): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosCarreira.sitCarr', inclusao.dadosCarreira.sitCarr.cdata, 1, '1;2;3')

    if 'alteracao' in dir(evtTabCarreira.infoCarreira):
        for alteracao in evtTabCarreira.infoCarreira.alteracao:

            if 'codCarreira' in dir(alteracao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideCarreira.codCarreira', alteracao.ideCarreira.codCarreira.cdata, 1, '')
            if 'iniValid' in dir(alteracao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideCarreira.iniValid', alteracao.ideCarreira.iniValid.cdata, 1, '')
            if 'fimValid' in dir(alteracao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideCarreira.fimValid', alteracao.ideCarreira.fimValid.cdata, 0, '')
            if 'dscCarreira' in dir(alteracao.dadosCarreira): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosCarreira.dscCarreira', alteracao.dadosCarreira.dscCarreira.cdata, 1, '')
            if 'leiCarr' in dir(alteracao.dadosCarreira): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosCarreira.leiCarr', alteracao.dadosCarreira.leiCarr.cdata, 0, '')
            if 'dtLeiCarr' in dir(alteracao.dadosCarreira): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosCarreira.dtLeiCarr', alteracao.dadosCarreira.dtLeiCarr.cdata, 1, '')
            if 'sitCarr' in dir(alteracao.dadosCarreira): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosCarreira.sitCarr', alteracao.dadosCarreira.sitCarr.cdata, 1, '1;2;3')

            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:

                    if 'iniValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.iniValid', novaValidade.iniValid.cdata, 1, '')
                    if 'fimValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.fimValid', novaValidade.fimValid.cdata, 0, '')

    if 'exclusao' in dir(evtTabCarreira.infoCarreira):
        for exclusao in evtTabCarreira.infoCarreira.exclusao:

            if 'codCarreira' in dir(exclusao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideCarreira.codCarreira', exclusao.ideCarreira.codCarreira.cdata, 1, '')
            if 'iniValid' in dir(exclusao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideCarreira.iniValid', exclusao.ideCarreira.iniValid.cdata, 1, '')
            if 'fimValid' in dir(exclusao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideCarreira.fimValid', exclusao.ideCarreira.fimValid.cdata, 0, '')

    return validacoes_lista