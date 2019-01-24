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


def validacoes_s2241_evtinsapo(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtInsApo = doc.eSocial.evtInsApo

    if 'indRetif' in dir(evtInsApo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInsApo.ideEvento.indRetif', evtInsApo.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtInsApo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInsApo.ideEvento.nrRecibo', evtInsApo.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtInsApo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInsApo.ideEvento.tpAmb', evtInsApo.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtInsApo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInsApo.ideEvento.procEmi', evtInsApo.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtInsApo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInsApo.ideEvento.verProc', evtInsApo.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtInsApo.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtInsApo.ideEmpregador.tpInsc', evtInsApo.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtInsApo.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtInsApo.ideEmpregador.nrInsc', evtInsApo.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtInsApo.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtInsApo.ideVinculo.cpfTrab', evtInsApo.ideVinculo.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtInsApo.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtInsApo.ideVinculo.nisTrab', evtInsApo.ideVinculo.nisTrab.cdata, 0, '')
    if 'matricula' in dir(evtInsApo.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtInsApo.ideVinculo.matricula', evtInsApo.ideVinculo.matricula.cdata, 0, '')
    if 'iniInsalPeric' in dir(evtInsApo.insalPeric):
        for iniInsalPeric in evtInsApo.insalPeric.iniInsalPeric:

            if 'dtIniCondicao' in dir(iniInsalPeric): validacoes_lista = validar_campo(validacoes_lista,'iniInsalPeric.dtIniCondicao', iniInsalPeric.dtIniCondicao.cdata, 1, '')

            if 'infoAmb' in dir(iniInsalPeric):
                for infoAmb in iniInsalPeric.infoAmb:

                    if 'codAmb' in dir(infoAmb): validacoes_lista = validar_campo(validacoes_lista,'infoAmb.codAmb', infoAmb.codAmb.cdata, 1, '')

    if 'altInsalPeric' in dir(evtInsApo.insalPeric):
        for altInsalPeric in evtInsApo.insalPeric.altInsalPeric:

            if 'dtAltCondicao' in dir(altInsalPeric): validacoes_lista = validar_campo(validacoes_lista,'altInsalPeric.dtAltCondicao', altInsalPeric.dtAltCondicao.cdata, 1, '')

            if 'infoamb' in dir(altInsalPeric):
                for infoamb in altInsalPeric.infoamb:

                    if 'codAmb' in dir(infoamb): validacoes_lista = validar_campo(validacoes_lista,'infoamb.codAmb', infoamb.codAmb.cdata, 1, '')

    if 'fimInsalPeric' in dir(evtInsApo.insalPeric):
        for fimInsalPeric in evtInsApo.insalPeric.fimInsalPeric:

            if 'dtFimCondicao' in dir(fimInsalPeric): validacoes_lista = validar_campo(validacoes_lista,'fimInsalPeric.dtFimCondicao', fimInsalPeric.dtFimCondicao.cdata, 1, '')

            if 'infoAmb' in dir(fimInsalPeric):
                for infoAmb in fimInsalPeric.infoAmb:

                    if 'codAmb' in dir(infoAmb): validacoes_lista = validar_campo(validacoes_lista,'infoAmb.codAmb', infoAmb.codAmb.cdata, 1, '')

    if 'iniAposentEsp' in dir(evtInsApo.aposentEsp):
        for iniAposentEsp in evtInsApo.aposentEsp.iniAposentEsp:

            if 'dtIniCondicao' in dir(iniAposentEsp): validacoes_lista = validar_campo(validacoes_lista,'iniAposentEsp.dtIniCondicao', iniAposentEsp.dtIniCondicao.cdata, 1, '')

            if 'infoAmb' in dir(iniAposentEsp):
                for infoAmb in iniAposentEsp.infoAmb:

                    if 'codAmb' in dir(infoAmb): validacoes_lista = validar_campo(validacoes_lista,'infoAmb.codAmb', infoAmb.codAmb.cdata, 1, '')

    if 'altAposentEsp' in dir(evtInsApo.aposentEsp):
        for altAposentEsp in evtInsApo.aposentEsp.altAposentEsp:

            if 'dtAltCondicao' in dir(altAposentEsp): validacoes_lista = validar_campo(validacoes_lista,'altAposentEsp.dtAltCondicao', altAposentEsp.dtAltCondicao.cdata, 1, '')

            if 'infoamb' in dir(altAposentEsp):
                for infoamb in altAposentEsp.infoamb:

                    if 'codAmb' in dir(infoamb): validacoes_lista = validar_campo(validacoes_lista,'infoamb.codAmb', infoamb.codAmb.cdata, 1, '')

    if 'fimAposentEsp' in dir(evtInsApo.aposentEsp):
        for fimAposentEsp in evtInsApo.aposentEsp.fimAposentEsp:

            if 'dtFimCondicao' in dir(fimAposentEsp): validacoes_lista = validar_campo(validacoes_lista,'fimAposentEsp.dtFimCondicao', fimAposentEsp.dtFimCondicao.cdata, 1, '')

            if 'infoAmb' in dir(fimAposentEsp):
                for infoAmb in fimAposentEsp.infoAmb:

                    if 'codAmb' in dir(infoAmb): validacoes_lista = validar_campo(validacoes_lista,'infoAmb.codAmb', infoAmb.codAmb.cdata, 1, '')

    return validacoes_lista