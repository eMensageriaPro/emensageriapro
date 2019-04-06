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


def validacoes_s5001_evtbasestrab(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtBasesTrab = doc.eSocial.evtBasesTrab

    if 'nrRecArqBase' in dir(evtBasesTrab.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtBasesTrab.ideEvento.nrRecArqBase', evtBasesTrab.ideEvento.nrRecArqBase.cdata, 1, u'')
    if 'indApuracao' in dir(evtBasesTrab.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtBasesTrab.ideEvento.indApuracao', evtBasesTrab.ideEvento.indApuracao.cdata, 1, u'1;2')
    if 'perApur' in dir(evtBasesTrab.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtBasesTrab.ideEvento.perApur', evtBasesTrab.ideEvento.perApur.cdata, 1, u'')
    if 'tpInsc' in dir(evtBasesTrab.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtBasesTrab.ideEmpregador.tpInsc', evtBasesTrab.ideEmpregador.tpInsc.cdata, 1, u'1;2;3;4')
    if 'nrInsc' in dir(evtBasesTrab.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtBasesTrab.ideEmpregador.nrInsc', evtBasesTrab.ideEmpregador.nrInsc.cdata, 1, u'')
    if 'cpfTrab' in dir(evtBasesTrab.ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtBasesTrab.ideTrabalhador.cpfTrab', evtBasesTrab.ideTrabalhador.cpfTrab.cdata, 1, u'')
    if 'procJudTrab' in dir(evtBasesTrab.ideTrabalhador):
        for procJudTrab in evtBasesTrab.ideTrabalhador.procJudTrab:

            if 'nrProcJud' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.nrProcJud', procJudTrab.nrProcJud.cdata, 1, u'')
            if 'codSusp' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.codSusp', procJudTrab.codSusp.cdata, 1, u'')

    if 'infoCpCalc' in dir(evtBasesTrab):
        for infoCpCalc in evtBasesTrab.infoCpCalc:

            if 'tpCR' in dir(infoCpCalc): validacoes_lista = validar_campo(validacoes_lista,'infoCpCalc.tpCR', infoCpCalc.tpCR.cdata, 1, u'108201;108202;108203;108204;108221;108222;108223;108224;109901;109902')
            if 'vrCpSeg' in dir(infoCpCalc): validacoes_lista = validar_campo(validacoes_lista,'infoCpCalc.vrCpSeg', infoCpCalc.vrCpSeg.cdata, 1, u'')
            if 'vrDescSeg' in dir(infoCpCalc): validacoes_lista = validar_campo(validacoes_lista,'infoCpCalc.vrDescSeg', infoCpCalc.vrDescSeg.cdata, 1, u'')

    if 'ideEstabLot' in dir(evtBasesTrab.infoCp):
        for ideEstabLot in evtBasesTrab.infoCp.ideEstabLot:

            if 'tpInsc' in dir(ideEstabLot): validacoes_lista = validar_campo(validacoes_lista,'ideEstabLot.tpInsc', ideEstabLot.tpInsc.cdata, 1, u'1;2;3;4')
            if 'nrInsc' in dir(ideEstabLot): validacoes_lista = validar_campo(validacoes_lista,'ideEstabLot.nrInsc', ideEstabLot.nrInsc.cdata, 1, u'')
            if 'codLotacao' in dir(ideEstabLot): validacoes_lista = validar_campo(validacoes_lista,'ideEstabLot.codLotacao', ideEstabLot.codLotacao.cdata, 1, u'')

            if 'infoCategIncid' in dir(ideEstabLot):
                for infoCategIncid in ideEstabLot.infoCategIncid:

                    if 'matricula' in dir(infoCategIncid): validacoes_lista = validar_campo(validacoes_lista,'infoCategIncid.matricula', infoCategIncid.matricula.cdata, 0, u'')
                    if 'codCateg' in dir(infoCategIncid): validacoes_lista = validar_campo(validacoes_lista,'infoCategIncid.codCateg', infoCategIncid.codCateg.cdata, 1, u'101;102;103;104;105;106;111;201;202;301;302;303;305;306;307;308;309;401;410;701;711;712;721;722;723;731;734;738;741;751;761;771;781;901;902;903;904;905')
                    if 'indSimples' in dir(infoCategIncid): validacoes_lista = validar_campo(validacoes_lista,'infoCategIncid.indSimples', infoCategIncid.indSimples.cdata, 0, u'1;2;3')

    return validacoes_lista