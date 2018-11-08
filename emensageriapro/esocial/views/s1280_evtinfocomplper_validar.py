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


def validacoes_s1280_evtinfocomplper(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtInfoComplPer = doc.eSocial.evtInfoComplPer

    if 'indRetif' in dir(evtInfoComplPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInfoComplPer.ideEvento.indRetif', evtInfoComplPer.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtInfoComplPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInfoComplPer.ideEvento.nrRecibo', evtInfoComplPer.ideEvento.nrRecibo.cdata, 0, '')
    if 'indApuracao' in dir(evtInfoComplPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInfoComplPer.ideEvento.indApuracao', evtInfoComplPer.ideEvento.indApuracao.cdata, 1, '1;2')
    if 'perApur' in dir(evtInfoComplPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInfoComplPer.ideEvento.perApur', evtInfoComplPer.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtInfoComplPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInfoComplPer.ideEvento.tpAmb', evtInfoComplPer.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtInfoComplPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInfoComplPer.ideEvento.procEmi', evtInfoComplPer.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtInfoComplPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInfoComplPer.ideEvento.verProc', evtInfoComplPer.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtInfoComplPer.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtInfoComplPer.ideEmpregador.tpInsc', evtInfoComplPer.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtInfoComplPer.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtInfoComplPer.ideEmpregador.nrInsc', evtInfoComplPer.ideEmpregador.nrInsc.cdata, 1, '')
    if 'infoSubstPatr' in dir(evtInfoComplPer):
        for infoSubstPatr in evtInfoComplPer.infoSubstPatr:
       
            if 'indSubstPatr' in dir(infoSubstPatr): validacoes_lista = validar_campo(validacoes_lista,'infoSubstPatr.indSubstPatr', infoSubstPatr.indSubstPatr.cdata, 1, '1;2')
            if 'percRedContrib' in dir(infoSubstPatr): validacoes_lista = validar_campo(validacoes_lista,'infoSubstPatr.percRedContrib', infoSubstPatr.percRedContrib.cdata, 1, '')

    if 'infoSubstPatrOpPort' in dir(evtInfoComplPer):
        for infoSubstPatrOpPort in evtInfoComplPer.infoSubstPatrOpPort:
       
            if 'cnpjOpPortuario' in dir(infoSubstPatrOpPort): validacoes_lista = validar_campo(validacoes_lista,'infoSubstPatrOpPort.cnpjOpPortuario', infoSubstPatrOpPort.cnpjOpPortuario.cdata, 1, '')

    if 'infoAtivConcom' in dir(evtInfoComplPer):
        for infoAtivConcom in evtInfoComplPer.infoAtivConcom:
       
            if 'fatorMes' in dir(infoAtivConcom): validacoes_lista = validar_campo(validacoes_lista,'infoAtivConcom.fatorMes', infoAtivConcom.fatorMes.cdata, 1, '')
            if 'fator13' in dir(infoAtivConcom): validacoes_lista = validar_campo(validacoes_lista,'infoAtivConcom.fator13', infoAtivConcom.fator13.cdata, 1, '')

    return validacoes_lista