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


def validacoes_s1060_evttabambiente(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabAmbiente = doc.eSocial.evtTabAmbiente
    
    if 'tpAmb' in dir(evtTabAmbiente.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabAmbiente.ideEvento.tpAmb', evtTabAmbiente.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtTabAmbiente.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabAmbiente.ideEvento.procEmi', evtTabAmbiente.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtTabAmbiente.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabAmbiente.ideEvento.verProc', evtTabAmbiente.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtTabAmbiente.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabAmbiente.ideEmpregador.tpInsc', evtTabAmbiente.ideEmpregador.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtTabAmbiente.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabAmbiente.ideEmpregador.nrInsc', evtTabAmbiente.ideEmpregador.nrInsc.cdata, 1, '')
    if 'inclusao' in dir(evtTabAmbiente.infoAmbiente):
        for inclusao in evtTabAmbiente.infoAmbiente.inclusao:
            
            if 'codAmb' in dir(inclusao.ideAmbiente): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideAmbiente.codAmb', inclusao.ideAmbiente.codAmb.cdata, 1, '')
            if 'iniValid' in dir(inclusao.ideAmbiente): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideAmbiente.iniValid', inclusao.ideAmbiente.iniValid.cdata, 1, '')
            if 'fimValid' in dir(inclusao.ideAmbiente): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideAmbiente.fimValid', inclusao.ideAmbiente.fimValid.cdata, 0, '')
            if 'dscAmb' in dir(inclusao.dadosAmbiente): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosAmbiente.dscAmb', inclusao.dadosAmbiente.dscAmb.cdata, 1, '')
            if 'localAmb' in dir(inclusao.dadosAmbiente): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosAmbiente.localAmb', inclusao.dadosAmbiente.localAmb.cdata, 1, '1;2;3')
            if 'tpInsc' in dir(inclusao.dadosAmbiente): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosAmbiente.tpInsc', inclusao.dadosAmbiente.tpInsc.cdata, 0, '1;3;4')
            if 'nrInsc' in dir(inclusao.dadosAmbiente): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosAmbiente.nrInsc', inclusao.dadosAmbiente.nrInsc.cdata, 0, '')
            if 'codLotacao' in dir(inclusao.dadosAmbiente): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosAmbiente.codLotacao', inclusao.dadosAmbiente.codLotacao.cdata, 0, '')

    if 'alteracao' in dir(evtTabAmbiente.infoAmbiente):
        for alteracao in evtTabAmbiente.infoAmbiente.alteracao:
            
            if 'codAmb' in dir(alteracao.ideAmbiente): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideAmbiente.codAmb', alteracao.ideAmbiente.codAmb.cdata, 1, '')
            if 'iniValid' in dir(alteracao.ideAmbiente): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideAmbiente.iniValid', alteracao.ideAmbiente.iniValid.cdata, 1, '')
            if 'fimValid' in dir(alteracao.ideAmbiente): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideAmbiente.fimValid', alteracao.ideAmbiente.fimValid.cdata, 0, '')
            if 'dscAmb' in dir(alteracao.dadosAmbiente): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosAmbiente.dscAmb', alteracao.dadosAmbiente.dscAmb.cdata, 1, '')
            if 'localAmb' in dir(alteracao.dadosAmbiente): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosAmbiente.localAmb', alteracao.dadosAmbiente.localAmb.cdata, 1, '1;2;3')
            if 'tpInsc' in dir(alteracao.dadosAmbiente): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosAmbiente.tpInsc', alteracao.dadosAmbiente.tpInsc.cdata, 0, '1;3;4')
            if 'nrInsc' in dir(alteracao.dadosAmbiente): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosAmbiente.nrInsc', alteracao.dadosAmbiente.nrInsc.cdata, 0, '')
            if 'codLotacao' in dir(alteracao.dadosAmbiente): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosAmbiente.codLotacao', alteracao.dadosAmbiente.codLotacao.cdata, 0, '')

            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    
                    if 'iniValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.iniValid', novaValidade.iniValid.cdata, 1, '')
                    if 'fimValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.fimValid', novaValidade.fimValid.cdata, 0, '')
        
    if 'exclusao' in dir(evtTabAmbiente.infoAmbiente):
        for exclusao in evtTabAmbiente.infoAmbiente.exclusao:
            
            if 'codAmb' in dir(exclusao.ideAmbiente): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideAmbiente.codAmb', exclusao.ideAmbiente.codAmb.cdata, 1, '')
            if 'iniValid' in dir(exclusao.ideAmbiente): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideAmbiente.iniValid', exclusao.ideAmbiente.iniValid.cdata, 1, '')
            if 'fimValid' in dir(exclusao.ideAmbiente): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideAmbiente.fimValid', exclusao.ideAmbiente.fimValid.cdata, 0, '')

    return validacoes_lista