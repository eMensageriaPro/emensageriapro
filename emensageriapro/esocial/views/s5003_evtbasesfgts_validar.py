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


def validacoes_s5003_evtbasesfgts(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtBasesFGTS = doc.eSocial.evtBasesFGTS

    if 'nrRecArqBase' in dir(evtBasesFGTS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtBasesFGTS.ideEvento.nrRecArqBase', evtBasesFGTS.ideEvento.nrRecArqBase.cdata, 1, '')
    if 'perApur' in dir(evtBasesFGTS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtBasesFGTS.ideEvento.perApur', evtBasesFGTS.ideEvento.perApur.cdata, 1, '')
    if 'tpInsc' in dir(evtBasesFGTS.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtBasesFGTS.ideEmpregador.tpInsc', evtBasesFGTS.ideEmpregador.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtBasesFGTS.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtBasesFGTS.ideEmpregador.nrInsc', evtBasesFGTS.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtBasesFGTS.ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtBasesFGTS.ideTrabalhador.cpfTrab', evtBasesFGTS.ideTrabalhador.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtBasesFGTS.ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtBasesFGTS.ideTrabalhador.nisTrab', evtBasesFGTS.ideTrabalhador.nisTrab.cdata, 0, '')
    if 'infoFGTS' in dir(evtBasesFGTS):
        for infoFGTS in evtBasesFGTS.infoFGTS:

            if 'dtVenc' in dir(infoFGTS): validacoes_lista = validar_campo(validacoes_lista,'infoFGTS.dtVenc', infoFGTS.dtVenc.cdata, 0, '')

            if 'ideEstabLot' in dir(infoFGTS):
                for ideEstabLot in infoFGTS.ideEstabLot:

                    if 'tpInsc' in dir(ideEstabLot): validacoes_lista = validar_campo(validacoes_lista,'ideEstabLot.tpInsc', ideEstabLot.tpInsc.cdata, 1, '')
                    if 'nrInsc' in dir(ideEstabLot): validacoes_lista = validar_campo(validacoes_lista,'ideEstabLot.nrInsc', ideEstabLot.nrInsc.cdata, 1, '')
                    if 'codLotacao' in dir(ideEstabLot): validacoes_lista = validar_campo(validacoes_lista,'ideEstabLot.codLotacao', ideEstabLot.codLotacao.cdata, 1, '')

            if 'infoTrabDps' in dir(infoFGTS.infoDpsFGTS):
                for infoTrabDps in infoFGTS.infoDpsFGTS.infoTrabDps:

                    if 'matricula' in dir(infoTrabDps): validacoes_lista = validar_campo(validacoes_lista,'infoTrabDps.matricula', infoTrabDps.matricula.cdata, 0, '')
                    if 'codCateg' in dir(infoTrabDps): validacoes_lista = validar_campo(validacoes_lista,'infoTrabDps.codCateg', infoTrabDps.codCateg.cdata, 1, '')

    return validacoes_lista