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


def validacoes_s5013_evtfgts(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtFGTS = doc.eSocial.evtFGTS

    if 'perApur' in dir(evtFGTS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtFGTS.ideEvento.perApur', evtFGTS.ideEvento.perApur.cdata, 1, '')
    if 'tpInsc' in dir(evtFGTS.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtFGTS.ideEmpregador.tpInsc', evtFGTS.ideEmpregador.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtFGTS.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtFGTS.ideEmpregador.nrInsc', evtFGTS.ideEmpregador.nrInsc.cdata, 1, '')
    if 'nrRecArqBase' in dir(evtFGTS.infoFGTS): validacoes_lista = validar_campo(validacoes_lista,'evtFGTS.infoFGTS.nrRecArqBase', evtFGTS.infoFGTS.nrRecArqBase.cdata, 1, '')
    if 'indExistInfo' in dir(evtFGTS.infoFGTS): validacoes_lista = validar_campo(validacoes_lista,'evtFGTS.infoFGTS.indExistInfo', evtFGTS.infoFGTS.indExistInfo.cdata, 1, '1;2;3')
    if 'basePerApur' in dir(evtFGTS.infoFGTS.infoBaseFGTS):
        for basePerApur in evtFGTS.infoFGTS.infoBaseFGTS.basePerApur:
       
            if 'tpValor' in dir(basePerApur): validacoes_lista = validar_campo(validacoes_lista,'basePerApur.tpValor', basePerApur.tpValor.cdata, 1, '')
            if 'baseFGTS' in dir(basePerApur): validacoes_lista = validar_campo(validacoes_lista,'basePerApur.baseFGTS', basePerApur.baseFGTS.cdata, 1, '')

    if 'infoBasePerAntE' in dir(evtFGTS.infoFGTS.infoBaseFGTS):
        for infoBasePerAntE in evtFGTS.infoFGTS.infoBaseFGTS.infoBasePerAntE:
       
            if 'perRef' in dir(infoBasePerAntE): validacoes_lista = validar_campo(validacoes_lista,'infoBasePerAntE.perRef', infoBasePerAntE.perRef.cdata, 1, '')

            if 'basePerAntE' in dir(infoBasePerAntE):
                for basePerAntE in infoBasePerAntE.basePerAntE:
               
                    if 'tpValorE' in dir(basePerAntE): validacoes_lista = validar_campo(validacoes_lista,'basePerAntE.tpValorE', basePerAntE.tpValorE.cdata, 1, '')
                    if 'baseFGTSE' in dir(basePerAntE): validacoes_lista = validar_campo(validacoes_lista,'basePerAntE.baseFGTSE', basePerAntE.baseFGTSE.cdata, 1, '')
   
    if 'dpsPerApur' in dir(evtFGTS.infoFGTS.infoDpsFGTS):
        for dpsPerApur in evtFGTS.infoFGTS.infoDpsFGTS.dpsPerApur:
       
            if 'tpDps' in dir(dpsPerApur): validacoes_lista = validar_campo(validacoes_lista,'dpsPerApur.tpDps', dpsPerApur.tpDps.cdata, 1, '')
            if 'vrFGTS' in dir(dpsPerApur): validacoes_lista = validar_campo(validacoes_lista,'dpsPerApur.vrFGTS', dpsPerApur.vrFGTS.cdata, 1, '')

    if 'infoDpsPerAntE' in dir(evtFGTS.infoFGTS.infoDpsFGTS):
        for infoDpsPerAntE in evtFGTS.infoFGTS.infoDpsFGTS.infoDpsPerAntE:
       
            if 'perRef' in dir(infoDpsPerAntE): validacoes_lista = validar_campo(validacoes_lista,'infoDpsPerAntE.perRef', infoDpsPerAntE.perRef.cdata, 1, '')

            if 'dpsPerAntE' in dir(infoDpsPerAntE):
                for dpsPerAntE in infoDpsPerAntE.dpsPerAntE:
               
                    if 'tpDpsE' in dir(dpsPerAntE): validacoes_lista = validar_campo(validacoes_lista,'dpsPerAntE.tpDpsE', dpsPerAntE.tpDpsE.cdata, 1, '')
                    if 'vrFGTSE' in dir(dpsPerAntE): validacoes_lista = validar_campo(validacoes_lista,'dpsPerAntE.vrFGTSE', dpsPerAntE.vrFGTSE.cdata, 1, '')
   
    return validacoes_lista