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


def validacoes_s2299_evtdeslig(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtDeslig = doc.eSocial.evtDeslig

    if 'indRetif' in dir(evtDeslig.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.ideEvento.indRetif', evtDeslig.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtDeslig.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.ideEvento.nrRecibo', evtDeslig.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtDeslig.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.ideEvento.tpAmb', evtDeslig.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtDeslig.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.ideEvento.procEmi', evtDeslig.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtDeslig.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.ideEvento.verProc', evtDeslig.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtDeslig.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.ideEmpregador.tpInsc', evtDeslig.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtDeslig.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.ideEmpregador.nrInsc', evtDeslig.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtDeslig.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.ideVinculo.cpfTrab', evtDeslig.ideVinculo.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtDeslig.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.ideVinculo.nisTrab', evtDeslig.ideVinculo.nisTrab.cdata, 1, '')
    if 'matricula' in dir(evtDeslig.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.ideVinculo.matricula', evtDeslig.ideVinculo.matricula.cdata, 1, '')
    if 'mtvDeslig' in dir(evtDeslig.infoDeslig): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.infoDeslig.mtvDeslig', evtDeslig.infoDeslig.mtvDeslig.cdata, 1, '01;02;03;04;05;06;07;08;09;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34')
    if 'dtDeslig' in dir(evtDeslig.infoDeslig): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.infoDeslig.dtDeslig', evtDeslig.infoDeslig.dtDeslig.cdata, 1, '')
    if 'indPagtoAPI' in dir(evtDeslig.infoDeslig): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.infoDeslig.indPagtoAPI', evtDeslig.infoDeslig.indPagtoAPI.cdata, 1, 'S;N')
    if 'dtProjFimAPI' in dir(evtDeslig.infoDeslig): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.infoDeslig.dtProjFimAPI', evtDeslig.infoDeslig.dtProjFimAPI.cdata, 0, '')
    if 'pensAlim' in dir(evtDeslig.infoDeslig): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.infoDeslig.pensAlim', evtDeslig.infoDeslig.pensAlim.cdata, 1, '0;1;2;3')
    if 'percAliment' in dir(evtDeslig.infoDeslig): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.infoDeslig.percAliment', evtDeslig.infoDeslig.percAliment.cdata, 0, '')
    if 'vrAlim' in dir(evtDeslig.infoDeslig): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.infoDeslig.vrAlim', evtDeslig.infoDeslig.vrAlim.cdata, 0, '')
    if 'nrCertObito' in dir(evtDeslig.infoDeslig): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.infoDeslig.nrCertObito', evtDeslig.infoDeslig.nrCertObito.cdata, 0, '')
    if 'nrProcTrab' in dir(evtDeslig.infoDeslig): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.infoDeslig.nrProcTrab', evtDeslig.infoDeslig.nrProcTrab.cdata, 0, '')
    if 'indCumprParc' in dir(evtDeslig.infoDeslig): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.infoDeslig.indCumprParc', evtDeslig.infoDeslig.indCumprParc.cdata, 1, '0;1;2;3;4')
    if 'qtdDiasInterm' in dir(evtDeslig.infoDeslig): validacoes_lista = validar_campo(validacoes_lista,'evtDeslig.infoDeslig.qtdDiasInterm', evtDeslig.infoDeslig.qtdDiasInterm.cdata, 0, '')
    if 'observacoes' in dir(evtDeslig.infoDeslig):
        for observacoes in evtDeslig.infoDeslig.observacoes:
       
            if 'observacao' in dir(observacoes): validacoes_lista = validar_campo(validacoes_lista,'observacoes.observacao', observacoes.observacao.cdata, 1, '')

    if 'sucessaoVinc' in dir(evtDeslig.infoDeslig):
        for sucessaoVinc in evtDeslig.infoDeslig.sucessaoVinc:
       
            if 'tpInscSuc' in dir(sucessaoVinc): validacoes_lista = validar_campo(validacoes_lista,'sucessaoVinc.tpInscSuc', sucessaoVinc.tpInscSuc.cdata, 1, '1;2')
            if 'cnpjSucessora' in dir(sucessaoVinc): validacoes_lista = validar_campo(validacoes_lista,'sucessaoVinc.cnpjSucessora', sucessaoVinc.cnpjSucessora.cdata, 1, '')

    if 'transfTit' in dir(evtDeslig.infoDeslig):
        for transfTit in evtDeslig.infoDeslig.transfTit:
       
            if 'cpfSubstituto' in dir(transfTit): validacoes_lista = validar_campo(validacoes_lista,'transfTit.cpfSubstituto', transfTit.cpfSubstituto.cdata, 1, '')
            if 'dtNascto' in dir(transfTit): validacoes_lista = validar_campo(validacoes_lista,'transfTit.dtNascto', transfTit.dtNascto.cdata, 1, '')

    if 'mudancaCPF' in dir(evtDeslig.infoDeslig):
        for mudancaCPF in evtDeslig.infoDeslig.mudancaCPF:
       
            if 'novoCPF' in dir(mudancaCPF): validacoes_lista = validar_campo(validacoes_lista,'mudancaCPF.novoCPF', mudancaCPF.novoCPF.cdata, 1, '')

    if 'dmDev' in dir(evtDeslig.infoDeslig.verbasResc):
        for dmDev in evtDeslig.infoDeslig.verbasResc.dmDev:
       
            if 'ideDmDev' in dir(dmDev): validacoes_lista = validar_campo(validacoes_lista,'dmDev.ideDmDev', dmDev.ideDmDev.cdata, 1, '')

            if 'ideEstabLot' in dir(dmDev.infoPerApur):
                for ideEstabLot in dmDev.infoPerApur.ideEstabLot:
               
                    if 'tpInsc' in dir(ideEstabLot): validacoes_lista = validar_campo(validacoes_lista,'ideEstabLot.tpInsc', ideEstabLot.tpInsc.cdata, 1, '1;2;3;4')
                    if 'nrInsc' in dir(ideEstabLot): validacoes_lista = validar_campo(validacoes_lista,'ideEstabLot.nrInsc', ideEstabLot.nrInsc.cdata, 1, '')
                    if 'codLotacao' in dir(ideEstabLot): validacoes_lista = validar_campo(validacoes_lista,'ideEstabLot.codLotacao', ideEstabLot.codLotacao.cdata, 1, '')
   
            if 'ideADC' in dir(dmDev.infoPerAnt):
                for ideADC in dmDev.infoPerAnt.ideADC:
               
                    if 'dtAcConv' in dir(ideADC): validacoes_lista = validar_campo(validacoes_lista,'ideADC.dtAcConv', ideADC.dtAcConv.cdata, 1, '')
                    if 'tpAcConv' in dir(ideADC): validacoes_lista = validar_campo(validacoes_lista,'ideADC.tpAcConv', ideADC.tpAcConv.cdata, 1, 'A;B;C;D;E')
                    if 'compAcConv' in dir(ideADC): validacoes_lista = validar_campo(validacoes_lista,'ideADC.compAcConv', ideADC.compAcConv.cdata, 0, '')
                    if 'dtEfAcConv' in dir(ideADC): validacoes_lista = validar_campo(validacoes_lista,'ideADC.dtEfAcConv', ideADC.dtEfAcConv.cdata, 1, '')
                    if 'dsc' in dir(ideADC): validacoes_lista = validar_campo(validacoes_lista,'ideADC.dsc', ideADC.dsc.cdata, 1, '')
   
            if 'infoTrabInterm' in dir(dmDev):
                for infoTrabInterm in dmDev.infoTrabInterm:
               
                    if 'codConv' in dir(infoTrabInterm): validacoes_lista = validar_campo(validacoes_lista,'infoTrabInterm.codConv', infoTrabInterm.codConv.cdata, 1, '')
   
    if 'procJudTrab' in dir(evtDeslig.infoDeslig.verbasResc):
        for procJudTrab in evtDeslig.infoDeslig.verbasResc.procJudTrab:
       
            if 'tpTrib' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.tpTrib', procJudTrab.tpTrib.cdata, 1, '3;2;3;4')
            if 'nrProcJud' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.nrProcJud', procJudTrab.nrProcJud.cdata, 1, '')
            if 'codSusp' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.codSusp', procJudTrab.codSusp.cdata, 0, '')

    if 'infoMV' in dir(evtDeslig.infoDeslig.verbasResc):
        for infoMV in evtDeslig.infoDeslig.verbasResc.infoMV:
       
            if 'indMV' in dir(infoMV): validacoes_lista = validar_campo(validacoes_lista,'infoMV.indMV', infoMV.indMV.cdata, 1, '1;2;3')

            if 'remunOutrEmpr' in dir(infoMV):
                for remunOutrEmpr in infoMV.remunOutrEmpr:
               
                    if 'tpInsc' in dir(remunOutrEmpr): validacoes_lista = validar_campo(validacoes_lista,'remunOutrEmpr.tpInsc', remunOutrEmpr.tpInsc.cdata, 1, '1;2;3;4')
                    if 'nrInsc' in dir(remunOutrEmpr): validacoes_lista = validar_campo(validacoes_lista,'remunOutrEmpr.nrInsc', remunOutrEmpr.nrInsc.cdata, 1, '')
                    if 'codCateg' in dir(remunOutrEmpr): validacoes_lista = validar_campo(validacoes_lista,'remunOutrEmpr.codCateg', remunOutrEmpr.codCateg.cdata, 1, '101;102;103;104;105;106;111;201;202;301;302;303;305;306;307;308;309;401;410;701;711;712;721;722;723;731;734;738;741;751;761;771;781;901;902;903;904;905')
                    if 'vlrRemunOE' in dir(remunOutrEmpr): validacoes_lista = validar_campo(validacoes_lista,'remunOutrEmpr.vlrRemunOE', remunOutrEmpr.vlrRemunOE.cdata, 1, '')
   
    if 'procCS' in dir(evtDeslig.infoDeslig.verbasResc):
        for procCS in evtDeslig.infoDeslig.verbasResc.procCS:
       
            if 'nrProcJud' in dir(procCS): validacoes_lista = validar_campo(validacoes_lista,'procCS.nrProcJud', procCS.nrProcJud.cdata, 1, '')

    if 'quarentena' in dir(evtDeslig.infoDeslig):
        for quarentena in evtDeslig.infoDeslig.quarentena:
       
            if 'dtFimQuar' in dir(quarentena): validacoes_lista = validar_campo(validacoes_lista,'quarentena.dtFimQuar', quarentena.dtFimQuar.cdata, 1, '')

    if 'consigFGTS' in dir(evtDeslig.infoDeslig):
        for consigFGTS in evtDeslig.infoDeslig.consigFGTS:
       
            if 'insConsig' in dir(consigFGTS): validacoes_lista = validar_campo(validacoes_lista,'consigFGTS.insConsig', consigFGTS.insConsig.cdata, 1, '')
            if 'nrContr' in dir(consigFGTS): validacoes_lista = validar_campo(validacoes_lista,'consigFGTS.nrContr', consigFGTS.nrContr.cdata, 1, '')

    return validacoes_lista