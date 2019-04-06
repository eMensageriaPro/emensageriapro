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


def validacoes_s2399_evttsvtermino(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTSVTermino = doc.eSocial.evtTSVTermino

    if 'indRetif' in dir(evtTSVTermino.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideEvento.indRetif', evtTSVTermino.ideEvento.indRetif.cdata, 1, u'1;2')
    if 'nrRecibo' in dir(evtTSVTermino.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideEvento.nrRecibo', evtTSVTermino.ideEvento.nrRecibo.cdata, 0, u'')
    if 'tpAmb' in dir(evtTSVTermino.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideEvento.tpAmb', evtTSVTermino.ideEvento.tpAmb.cdata, 1, u'1;2')
    if 'procEmi' in dir(evtTSVTermino.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideEvento.procEmi', evtTSVTermino.ideEvento.procEmi.cdata, 1, u'1;2;3;4;5')
    if 'verProc' in dir(evtTSVTermino.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideEvento.verProc', evtTSVTermino.ideEvento.verProc.cdata, 1, u'')
    if 'tpInsc' in dir(evtTSVTermino.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideEmpregador.tpInsc', evtTSVTermino.ideEmpregador.tpInsc.cdata, 1, u'1;2;3;4')
    if 'nrInsc' in dir(evtTSVTermino.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideEmpregador.nrInsc', evtTSVTermino.ideEmpregador.nrInsc.cdata, 1, u'')
    if 'cpfTrab' in dir(evtTSVTermino.ideTrabSemVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideTrabSemVinculo.cpfTrab', evtTSVTermino.ideTrabSemVinculo.cpfTrab.cdata, 1, u'')
    if 'nisTrab' in dir(evtTSVTermino.ideTrabSemVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideTrabSemVinculo.nisTrab', evtTSVTermino.ideTrabSemVinculo.nisTrab.cdata, 0, u'')
    if 'codCateg' in dir(evtTSVTermino.ideTrabSemVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideTrabSemVinculo.codCateg', evtTSVTermino.ideTrabSemVinculo.codCateg.cdata, 1, u'101;102;103;104;105;106;111;201;202;301;302;303;305;306;307;308;309;401;410;701;711;712;721;722;723;731;734;738;741;751;761;771;781;901;902;903;904;905')
    if 'dtTerm' in dir(evtTSVTermino.infoTSVTermino): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.infoTSVTermino.dtTerm', evtTSVTermino.infoTSVTermino.dtTerm.cdata, 1, u'')
    if 'mtvDesligTSV' in dir(evtTSVTermino.infoTSVTermino): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.infoTSVTermino.mtvDesligTSV', evtTSVTermino.infoTSVTermino.mtvDesligTSV.cdata, 0, u'01;02;03;04;05;06;99')
    if 'pensAlim' in dir(evtTSVTermino.infoTSVTermino): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.infoTSVTermino.pensAlim', evtTSVTermino.infoTSVTermino.pensAlim.cdata, 0, u'0;1;2;3')
    if 'percAliment' in dir(evtTSVTermino.infoTSVTermino): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.infoTSVTermino.percAliment', evtTSVTermino.infoTSVTermino.percAliment.cdata, 0, u'')
    if 'vrAlim' in dir(evtTSVTermino.infoTSVTermino): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.infoTSVTermino.vrAlim', evtTSVTermino.infoTSVTermino.vrAlim.cdata, 0, u'')
    if 'mudancaCPF' in dir(evtTSVTermino.infoTSVTermino):
        for mudancaCPF in evtTSVTermino.infoTSVTermino.mudancaCPF:

            if 'novoCPF' in dir(mudancaCPF): validacoes_lista = validar_campo(validacoes_lista,'mudancaCPF.novoCPF', mudancaCPF.novoCPF.cdata, 1, u'')

    if 'dmDev' in dir(evtTSVTermino.infoTSVTermino.verbasResc):
        for dmDev in evtTSVTermino.infoTSVTermino.verbasResc.dmDev:

            if 'ideDmDev' in dir(dmDev): validacoes_lista = validar_campo(validacoes_lista,'dmDev.ideDmDev', dmDev.ideDmDev.cdata, 1, u'')

            if 'ideEstabLot' in dir(dmDev):
                for ideEstabLot in dmDev.ideEstabLot:

                    if 'tpInsc' in dir(ideEstabLot): validacoes_lista = validar_campo(validacoes_lista,'ideEstabLot.tpInsc', ideEstabLot.tpInsc.cdata, 1, u'1;2;3;4')
                    if 'nrInsc' in dir(ideEstabLot): validacoes_lista = validar_campo(validacoes_lista,'ideEstabLot.nrInsc', ideEstabLot.nrInsc.cdata, 1, u'')
                    if 'codLotacao' in dir(ideEstabLot): validacoes_lista = validar_campo(validacoes_lista,'ideEstabLot.codLotacao', ideEstabLot.codLotacao.cdata, 1, u'')

    if 'procJudTrab' in dir(evtTSVTermino.infoTSVTermino.verbasResc):
        for procJudTrab in evtTSVTermino.infoTSVTermino.verbasResc.procJudTrab:

            if 'tpTrib' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.tpTrib', procJudTrab.tpTrib.cdata, 1, u'4;2;3;4')
            if 'nrProcJud' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.nrProcJud', procJudTrab.nrProcJud.cdata, 1, u'')
            if 'codSusp' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.codSusp', procJudTrab.codSusp.cdata, 0, u'')

    if 'infoMV' in dir(evtTSVTermino.infoTSVTermino.verbasResc):
        for infoMV in evtTSVTermino.infoTSVTermino.verbasResc.infoMV:

            if 'indMV' in dir(infoMV): validacoes_lista = validar_campo(validacoes_lista,'infoMV.indMV', infoMV.indMV.cdata, 1, u'1;2;3')

            if 'remunOutrEmpr' in dir(infoMV):
                for remunOutrEmpr in infoMV.remunOutrEmpr:

                    if 'tpInsc' in dir(remunOutrEmpr): validacoes_lista = validar_campo(validacoes_lista,'remunOutrEmpr.tpInsc', remunOutrEmpr.tpInsc.cdata, 1, u'1;2;3;4')
                    if 'nrInsc' in dir(remunOutrEmpr): validacoes_lista = validar_campo(validacoes_lista,'remunOutrEmpr.nrInsc', remunOutrEmpr.nrInsc.cdata, 1, u'')
                    if 'codCateg' in dir(remunOutrEmpr): validacoes_lista = validar_campo(validacoes_lista,'remunOutrEmpr.codCateg', remunOutrEmpr.codCateg.cdata, 1, u'101;102;103;104;105;106;111;201;202;301;302;303;305;306;307;308;309;401;410;701;711;712;721;722;723;731;734;738;741;751;761;771;781;901;902;903;904;905')
                    if 'vlrRemunOE' in dir(remunOutrEmpr): validacoes_lista = validar_campo(validacoes_lista,'remunOutrEmpr.vlrRemunOE', remunOutrEmpr.vlrRemunOE.cdata, 1, u'')

    if 'quarentena' in dir(evtTSVTermino.infoTSVTermino):
        for quarentena in evtTSVTermino.infoTSVTermino.quarentena:

            if 'dtFimQuar' in dir(quarentena): validacoes_lista = validar_campo(validacoes_lista,'quarentena.dtFimQuar', quarentena.dtFimQuar.cdata, 1, u'')

    return validacoes_lista