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


def validacoes_s5011_evtcs(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtCS = doc.eSocial.evtCS

    if 'indApuracao' in dir(evtCS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCS.ideEvento.indApuracao', evtCS.ideEvento.indApuracao.cdata, 1, '1;2')
    if 'perApur' in dir(evtCS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCS.ideEvento.perApur', evtCS.ideEvento.perApur.cdata, 1, '')
    if 'tpInsc' in dir(evtCS.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCS.ideEmpregador.tpInsc', evtCS.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtCS.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCS.ideEmpregador.nrInsc', evtCS.ideEmpregador.nrInsc.cdata, 1, '')
    if 'nrRecArqBase' in dir(evtCS.infoCS): validacoes_lista = validar_campo(validacoes_lista,'evtCS.infoCS.nrRecArqBase', evtCS.infoCS.nrRecArqBase.cdata, 1, '')
    if 'indExistInfo' in dir(evtCS.infoCS): validacoes_lista = validar_campo(validacoes_lista,'evtCS.infoCS.indExistInfo', evtCS.infoCS.indExistInfo.cdata, 1, '1;2;3')
    if 'classTrib' in dir(evtCS.infoCS.infoContrib): validacoes_lista = validar_campo(validacoes_lista,'evtCS.infoCS.infoContrib.classTrib', evtCS.infoCS.infoContrib.classTrib.cdata, 1, '01;02;03;04;06;07;08;09;10;11;13;14;21;22;60;70;80;85;99')
    if 'infoCPSeg' in dir(evtCS.infoCS):
        for infoCPSeg in evtCS.infoCS.infoCPSeg:
       
            if 'vrDescCP' in dir(infoCPSeg): validacoes_lista = validar_campo(validacoes_lista,'infoCPSeg.vrDescCP', infoCPSeg.vrDescCP.cdata, 1, '')
            if 'vrCpSeg' in dir(infoCPSeg): validacoes_lista = validar_campo(validacoes_lista,'infoCPSeg.vrCpSeg', infoCPSeg.vrCpSeg.cdata, 1, '')

    if 'infoPJ' in dir(evtCS.infoCS.infoContrib):
        for infoPJ in evtCS.infoCS.infoContrib.infoPJ:
       
            if 'indCoop' in dir(infoPJ): validacoes_lista = validar_campo(validacoes_lista,'infoPJ.indCoop', infoPJ.indCoop.cdata, 0, '0;1;2;3')
            if 'indConstr' in dir(infoPJ): validacoes_lista = validar_campo(validacoes_lista,'infoPJ.indConstr', infoPJ.indConstr.cdata, 1, '0;1')
            if 'indSubstPatr' in dir(infoPJ): validacoes_lista = validar_campo(validacoes_lista,'infoPJ.indSubstPatr', infoPJ.indSubstPatr.cdata, 0, '1;2')
            if 'percRedContrib' in dir(infoPJ): validacoes_lista = validar_campo(validacoes_lista,'infoPJ.percRedContrib', infoPJ.percRedContrib.cdata, 0, '')

            if 'infoAtConc' in dir(infoPJ):
                for infoAtConc in infoPJ.infoAtConc:
               
                    if 'fatorMes' in dir(infoAtConc): validacoes_lista = validar_campo(validacoes_lista,'infoAtConc.fatorMes', infoAtConc.fatorMes.cdata, 1, '')
                    if 'fator13' in dir(infoAtConc): validacoes_lista = validar_campo(validacoes_lista,'infoAtConc.fator13', infoAtConc.fator13.cdata, 1, '')
   
    if 'ideEstab' in dir(evtCS.infoCS):
        for ideEstab in evtCS.infoCS.ideEstab:
       
            if 'tpInsc' in dir(ideEstab): validacoes_lista = validar_campo(validacoes_lista,'ideEstab.tpInsc', ideEstab.tpInsc.cdata, 1, '1;2;3;4')
            if 'nrInsc' in dir(ideEstab): validacoes_lista = validar_campo(validacoes_lista,'ideEstab.nrInsc', ideEstab.nrInsc.cdata, 1, '')

            if 'infoEstab' in dir(ideEstab):
                for infoEstab in ideEstab.infoEstab:
               
                    if 'cnaePrep' in dir(infoEstab): validacoes_lista = validar_campo(validacoes_lista,'infoEstab.cnaePrep', infoEstab.cnaePrep.cdata, 1, '')
                    if 'aliqRat' in dir(infoEstab): validacoes_lista = validar_campo(validacoes_lista,'infoEstab.aliqRat', infoEstab.aliqRat.cdata, 1, '1;2;3')
                    if 'fap' in dir(infoEstab): validacoes_lista = validar_campo(validacoes_lista,'infoEstab.fap', infoEstab.fap.cdata, 1, '')
                    if 'aliqRatAjust' in dir(infoEstab): validacoes_lista = validar_campo(validacoes_lista,'infoEstab.aliqRatAjust', infoEstab.aliqRatAjust.cdata, 1, '')
   
            if 'ideLotacao' in dir(ideEstab):
                for ideLotacao in ideEstab.ideLotacao:
               
                    if 'codLotacao' in dir(ideLotacao): validacoes_lista = validar_campo(validacoes_lista,'ideLotacao.codLotacao', ideLotacao.codLotacao.cdata, 1, '')
                    if 'fpas' in dir(ideLotacao): validacoes_lista = validar_campo(validacoes_lista,'ideLotacao.fpas', ideLotacao.fpas.cdata, 1, '')
                    if 'codTercs' in dir(ideLotacao): validacoes_lista = validar_campo(validacoes_lista,'ideLotacao.codTercs', ideLotacao.codTercs.cdata, 1, '')
                    if 'codTercsSusp' in dir(ideLotacao): validacoes_lista = validar_campo(validacoes_lista,'ideLotacao.codTercsSusp', ideLotacao.codTercsSusp.cdata, 0, '')
   
            if 'basesAquis' in dir(ideEstab):
                for basesAquis in ideEstab.basesAquis:
               
                    if 'indAquis' in dir(basesAquis): validacoes_lista = validar_campo(validacoes_lista,'basesAquis.indAquis', basesAquis.indAquis.cdata, 1, '1;2;3;4;5;6')
                    if 'vlrAquis' in dir(basesAquis): validacoes_lista = validar_campo(validacoes_lista,'basesAquis.vlrAquis', basesAquis.vlrAquis.cdata, 1, '')
                    if 'vrCPDescPR' in dir(basesAquis): validacoes_lista = validar_campo(validacoes_lista,'basesAquis.vrCPDescPR', basesAquis.vrCPDescPR.cdata, 1, '')
                    if 'vrCPNRet' in dir(basesAquis): validacoes_lista = validar_campo(validacoes_lista,'basesAquis.vrCPNRet', basesAquis.vrCPNRet.cdata, 1, '')
                    if 'vrRatNRet' in dir(basesAquis): validacoes_lista = validar_campo(validacoes_lista,'basesAquis.vrRatNRet', basesAquis.vrRatNRet.cdata, 1, '')
                    if 'vrSenarNRet' in dir(basesAquis): validacoes_lista = validar_campo(validacoes_lista,'basesAquis.vrSenarNRet', basesAquis.vrSenarNRet.cdata, 1, '')
                    if 'vrCPCalcPR' in dir(basesAquis): validacoes_lista = validar_campo(validacoes_lista,'basesAquis.vrCPCalcPR', basesAquis.vrCPCalcPR.cdata, 1, '')
                    if 'vrRatDescPR' in dir(basesAquis): validacoes_lista = validar_campo(validacoes_lista,'basesAquis.vrRatDescPR', basesAquis.vrRatDescPR.cdata, 1, '')
                    if 'vrRatCalcPR' in dir(basesAquis): validacoes_lista = validar_campo(validacoes_lista,'basesAquis.vrRatCalcPR', basesAquis.vrRatCalcPR.cdata, 1, '')
                    if 'vrSenarDesc' in dir(basesAquis): validacoes_lista = validar_campo(validacoes_lista,'basesAquis.vrSenarDesc', basesAquis.vrSenarDesc.cdata, 1, '')
                    if 'vrSenarCalc' in dir(basesAquis): validacoes_lista = validar_campo(validacoes_lista,'basesAquis.vrSenarCalc', basesAquis.vrSenarCalc.cdata, 1, '')
   
            if 'basesComerc' in dir(ideEstab):
                for basesComerc in ideEstab.basesComerc:
               
                    if 'indComerc' in dir(basesComerc): validacoes_lista = validar_campo(validacoes_lista,'basesComerc.indComerc', basesComerc.indComerc.cdata, 1, '2;3;7;8;9')
                    if 'vrBcComPR' in dir(basesComerc): validacoes_lista = validar_campo(validacoes_lista,'basesComerc.vrBcComPR', basesComerc.vrBcComPR.cdata, 1, '')
                    if 'vrCPSusp' in dir(basesComerc): validacoes_lista = validar_campo(validacoes_lista,'basesComerc.vrCPSusp', basesComerc.vrCPSusp.cdata, 0, '')
                    if 'vrRatSusp' in dir(basesComerc): validacoes_lista = validar_campo(validacoes_lista,'basesComerc.vrRatSusp', basesComerc.vrRatSusp.cdata, 0, '')
                    if 'vrSenarSusp' in dir(basesComerc): validacoes_lista = validar_campo(validacoes_lista,'basesComerc.vrSenarSusp', basesComerc.vrSenarSusp.cdata, 0, '')
   
            if 'infoCREstab' in dir(ideEstab):
                for infoCREstab in ideEstab.infoCREstab:
               
                    if 'tpCR' in dir(infoCREstab): validacoes_lista = validar_campo(validacoes_lista,'infoCREstab.tpCR', infoCREstab.tpCR.cdata, 1, '')
                    if 'vrCR' in dir(infoCREstab): validacoes_lista = validar_campo(validacoes_lista,'infoCREstab.vrCR', infoCREstab.vrCR.cdata, 1, '')
                    if 'vrSuspCR' in dir(infoCREstab): validacoes_lista = validar_campo(validacoes_lista,'infoCREstab.vrSuspCR', infoCREstab.vrSuspCR.cdata, 0, '')
   
    if 'infoCRContrib' in dir(evtCS.infoCS):
        for infoCRContrib in evtCS.infoCS.infoCRContrib:
       
            if 'tpCR' in dir(infoCRContrib): validacoes_lista = validar_campo(validacoes_lista,'infoCRContrib.tpCR', infoCRContrib.tpCR.cdata, 1, '')
            if 'vrCR' in dir(infoCRContrib): validacoes_lista = validar_campo(validacoes_lista,'infoCRContrib.vrCR', infoCRContrib.vrCR.cdata, 1, '')
            if 'vrCRSusp' in dir(infoCRContrib): validacoes_lista = validar_campo(validacoes_lista,'infoCRContrib.vrCRSusp', infoCRContrib.vrCRSusp.cdata, 0, '')

    return validacoes_lista