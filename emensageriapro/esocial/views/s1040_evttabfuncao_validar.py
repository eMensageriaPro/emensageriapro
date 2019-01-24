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


def validacoes_s1040_evttabfuncao(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabFuncao = doc.eSocial.evtTabFuncao

    if 'tpAmb' in dir(evtTabFuncao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabFuncao.ideEvento.tpAmb', evtTabFuncao.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtTabFuncao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabFuncao.ideEvento.procEmi', evtTabFuncao.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtTabFuncao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabFuncao.ideEvento.verProc', evtTabFuncao.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtTabFuncao.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabFuncao.ideEmpregador.tpInsc', evtTabFuncao.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtTabFuncao.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabFuncao.ideEmpregador.nrInsc', evtTabFuncao.ideEmpregador.nrInsc.cdata, 1, '')
    if 'inclusao' in dir(evtTabFuncao.infoFuncao):
        for inclusao in evtTabFuncao.infoFuncao.inclusao:

            if 'codFuncao' in dir(inclusao.ideFuncao): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideFuncao.codFuncao', inclusao.ideFuncao.codFuncao.cdata, 1, '')
            if 'iniValid' in dir(inclusao.ideFuncao): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideFuncao.iniValid', inclusao.ideFuncao.iniValid.cdata, 1, '')
            if 'fimValid' in dir(inclusao.ideFuncao): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideFuncao.fimValid', inclusao.ideFuncao.fimValid.cdata, 0, '')
            if 'dscFuncao' in dir(inclusao.dadosFuncao): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosFuncao.dscFuncao', inclusao.dadosFuncao.dscFuncao.cdata, 1, '')
            if 'codCBO' in dir(inclusao.dadosFuncao): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosFuncao.codCBO', inclusao.dadosFuncao.codCBO.cdata, 1, '')

    if 'alteracao' in dir(evtTabFuncao.infoFuncao):
        for alteracao in evtTabFuncao.infoFuncao.alteracao:

            if 'codFuncao' in dir(alteracao.ideFuncao): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideFuncao.codFuncao', alteracao.ideFuncao.codFuncao.cdata, 1, '')
            if 'iniValid' in dir(alteracao.ideFuncao): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideFuncao.iniValid', alteracao.ideFuncao.iniValid.cdata, 1, '')
            if 'fimValid' in dir(alteracao.ideFuncao): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideFuncao.fimValid', alteracao.ideFuncao.fimValid.cdata, 0, '')
            if 'dscFuncao' in dir(alteracao.dadosFuncao): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosFuncao.dscFuncao', alteracao.dadosFuncao.dscFuncao.cdata, 1, '')
            if 'codCBO' in dir(alteracao.dadosFuncao): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosFuncao.codCBO', alteracao.dadosFuncao.codCBO.cdata, 1, '')

            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:

                    if 'iniValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.iniValid', novaValidade.iniValid.cdata, 1, '')
                    if 'fimValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.fimValid', novaValidade.fimValid.cdata, 0, '')

    if 'exclusao' in dir(evtTabFuncao.infoFuncao):
        for exclusao in evtTabFuncao.infoFuncao.exclusao:

            if 'codFuncao' in dir(exclusao.ideFuncao): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideFuncao.codFuncao', exclusao.ideFuncao.codFuncao.cdata, 1, '')
            if 'iniValid' in dir(exclusao.ideFuncao): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideFuncao.iniValid', exclusao.ideFuncao.iniValid.cdata, 1, '')
            if 'fimValid' in dir(exclusao.ideFuncao): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideFuncao.fimValid', exclusao.ideFuncao.fimValid.cdata, 0, '')

    return validacoes_lista