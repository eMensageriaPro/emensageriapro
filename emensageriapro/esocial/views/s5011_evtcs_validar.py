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
    #variaveis
    
    if 'ideEvento' in dir(evtCS.ideEvento):
        for ideEvento in evtCS.ideEvento:
            
            if 'indApuracao' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.indApuracao', 
                                                  ideEvento.indApuracao.cdata, 
                                                  1, u'1, 2')
            
            if 'perApur' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.perApur', 
                                                  ideEvento.perApur.cdata, 
                                                  1, u'None')
    
    if 'ideEmpregador' in dir(evtCS.ideEmpregador):
        for ideEmpregador in evtCS.ideEmpregador:
            
            if 'tpInsc' in dir(ideEmpregador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEmpregador.tpInsc', 
                                                  ideEmpregador.tpInsc.cdata, 
                                                  1, u'1, 2, 3, 4, 5')
            
            if 'nrInsc' in dir(ideEmpregador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEmpregador.nrInsc', 
                                                  ideEmpregador.nrInsc.cdata, 
                                                  1, u'None')
    
    if 'infoCS' in dir(evtCS.infoCS):
        for infoCS in evtCS.infoCS:
            
            if 'nrRecArqBase' in dir(infoCS):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoCS.nrRecArqBase', 
                                                  infoCS.nrRecArqBase.cdata, 
                                                  1, u'None')
            
            if 'indExistInfo' in dir(infoCS):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoCS.indExistInfo', 
                                                  infoCS.indExistInfo.cdata, 
                                                  1, u'None')
            
            if 'infoCPSeg' in dir(infoCS.infoCPSeg):
                for infoCPSeg in infoCS.infoCPSeg:
                    
                    if 'vrDescCP' in dir(infoCPSeg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoCPSeg.vrDescCP', 
                                                          infoCPSeg.vrDescCP.cdata, 
                                                          1, u'None')
                    
                    if 'vrCpSeg' in dir(infoCPSeg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoCPSeg.vrCpSeg', 
                                                          infoCPSeg.vrCpSeg.cdata, 
                                                          1, u'None')
            
            if 'infoContrib' in dir(infoCS.infoContrib):
                for infoContrib in infoCS.infoContrib:
                    
                    if 'classTrib' in dir(infoContrib):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoContrib.classTrib', 
                                                          infoContrib.classTrib.cdata, 
                                                          1, u'01, 02, 03, 04, 06, 07, 08, 09, 10, 11, 13, 14, 21, 22, 60, 70, 80, 85, 99')
                    
                    if 'infoPJ' in dir(infoContrib.infoPJ):
                        for infoPJ in infoContrib.infoPJ:
                            
                            if 'indCoop' in dir(infoPJ):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoPJ.indCoop', 
                                                                  infoPJ.indCoop.cdata, 
                                                                  0, u'0, 1, 2, 3')
                            
                            if 'indConstr' in dir(infoPJ):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoPJ.indConstr', 
                                                                  infoPJ.indConstr.cdata, 
                                                                  1, u'0, 1')
                            
                            if 'indSubstPatr' in dir(infoPJ):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoPJ.indSubstPatr', 
                                                                  infoPJ.indSubstPatr.cdata, 
                                                                  0, u'1, 2')
                            
                            if 'percRedContrib' in dir(infoPJ):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoPJ.percRedContrib', 
                                                                  infoPJ.percRedContrib.cdata, 
                                                                  0, u'None')
                            
                            if 'infoAtConc' in dir(infoPJ.infoAtConc):
                                for infoAtConc in infoPJ.infoAtConc:
                                    
                                    if 'fatorMes' in dir(infoAtConc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoAtConc.fatorMes', 
                                                                          infoAtConc.fatorMes.cdata, 
                                                                          1, u'None')
                                    
                                    if 'fator13' in dir(infoAtConc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoAtConc.fator13', 
                                                                          infoAtConc.fator13.cdata, 
                                                                          1, u'None')
            
            if 'ideEstab' in dir(infoCS.ideEstab):
                for ideEstab in infoCS.ideEstab:
                    
                    if 'tpInsc' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.tpInsc', 
                                                          ideEstab.tpInsc.cdata, 
                                                          1, u'1, 2, 3, 4, 5')
                    
                    if 'nrInsc' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.nrInsc', 
                                                          ideEstab.nrInsc.cdata, 
                                                          1, u'None')
                    
                    if 'infoEstab' in dir(ideEstab.infoEstab):
                        for infoEstab in ideEstab.infoEstab:
                            
                            if 'cnaePrep' in dir(infoEstab):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstab.cnaePrep', 
                                                                  infoEstab.cnaePrep.cdata, 
                                                                  1, u'None')
                            
                            if 'aliqRat' in dir(infoEstab):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstab.aliqRat', 
                                                                  infoEstab.aliqRat.cdata, 
                                                                  1, u'1, 2, 3')
                            
                            if 'fap' in dir(infoEstab):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstab.fap', 
                                                                  infoEstab.fap.cdata, 
                                                                  1, u'None')
                            
                            if 'aliqRatAjust' in dir(infoEstab):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstab.aliqRatAjust', 
                                                                  infoEstab.aliqRatAjust.cdata, 
                                                                  1, u'None')
                            
                            if 'infoComplObra' in dir(infoEstab.infoComplObra):
                                for infoComplObra in infoEstab.infoComplObra:
                                    
                                    if 'indSubstPatrObra' in dir(infoComplObra):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoComplObra.indSubstPatrObra', 
                                                                          infoComplObra.indSubstPatrObra.cdata, 
                                                                          1, u'1, 2')
                    
                    if 'ideLotacao' in dir(ideEstab.ideLotacao):
                        for ideLotacao in ideEstab.ideLotacao:
                            
                            if 'codLotacao' in dir(ideLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideLotacao.codLotacao', 
                                                                  ideLotacao.codLotacao.cdata, 
                                                                  1, u'None')
                            
                            if 'fpas' in dir(ideLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideLotacao.fpas', 
                                                                  ideLotacao.fpas.cdata, 
                                                                  1, u'507, 515, 523, 531, 540, 558, 566, 574, 582, 590, 604, 612, 620, 639, 647, 655, 680, 736, 744, 779, 787, 795, 825, 833, 868, 876')
                            
                            if 'codTercs' in dir(ideLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideLotacao.codTercs', 
                                                                  ideLotacao.codTercs.cdata, 
                                                                  1, u'507, 515, 523, 531, 540, 558, 566, 574, 582, 590, 604, 612, 620, 639, 647, 655, 680, 736, 744, 779, 787, 795, 825, 833, 868, 876')
                            
                            if 'codTercsSusp' in dir(ideLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideLotacao.codTercsSusp', 
                                                                  ideLotacao.codTercsSusp.cdata, 
                                                                  0, u'507, 515, 523, 531, 540, 558, 566, 574, 582, 590, 604, 612, 620, 639, 647, 655, 680, 736, 744, 779, 787, 795, 825, 833, 868, 876')
                            
                            if 'infoTercSusp' in dir(ideLotacao.infoTercSusp):
                                for infoTercSusp in ideLotacao.infoTercSusp:
                                    
                                    if 'codTerc' in dir(infoTercSusp):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoTercSusp.codTerc', 
                                                                          infoTercSusp.codTerc.cdata, 
                                                                          1, u'507, 515, 523, 531, 540, 558, 566, 574, 582, 590, 604, 612, 620, 639, 647, 655, 680, 736, 744, 779, 787, 795, 825, 833, 868, 876')
                            
                            if 'infoEmprParcial' in dir(ideLotacao.infoEmprParcial):
                                for infoEmprParcial in ideLotacao.infoEmprParcial:
                                    
                                    if 'tpInscContrat' in dir(infoEmprParcial):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoEmprParcial.tpInscContrat', 
                                                                          infoEmprParcial.tpInscContrat.cdata, 
                                                                          1, u'1, 2')
                                    
                                    if 'nrInscContrat' in dir(infoEmprParcial):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoEmprParcial.nrInscContrat', 
                                                                          infoEmprParcial.nrInscContrat.cdata, 
                                                                          1, u'None')
                                    
                                    if 'tpInscProp' in dir(infoEmprParcial):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoEmprParcial.tpInscProp', 
                                                                          infoEmprParcial.tpInscProp.cdata, 
                                                                          1, u'1, 2')
                                    
                                    if 'nrInscProp' in dir(infoEmprParcial):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoEmprParcial.nrInscProp', 
                                                                          infoEmprParcial.nrInscProp.cdata, 
                                                                          1, u'None')
                                    
                                    if 'cnoObra' in dir(infoEmprParcial):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoEmprParcial.cnoObra', 
                                                                          infoEmprParcial.cnoObra.cdata, 
                                                                          1, u'None')
                            
                            if 'dadosOpPort' in dir(ideLotacao.dadosOpPort):
                                for dadosOpPort in ideLotacao.dadosOpPort:
                                    
                                    if 'cnpjOpPortuario' in dir(dadosOpPort):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosOpPort.cnpjOpPortuario', 
                                                                          dadosOpPort.cnpjOpPortuario.cdata, 
                                                                          1, u'None')
                                    
                                    if 'aliqRat' in dir(dadosOpPort):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosOpPort.aliqRat', 
                                                                          dadosOpPort.aliqRat.cdata, 
                                                                          1, u'1, 2, 3')
                                    
                                    if 'fap' in dir(dadosOpPort):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosOpPort.fap', 
                                                                          dadosOpPort.fap.cdata, 
                                                                          1, u'None')
                                    
                                    if 'aliqRatAjust' in dir(dadosOpPort):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosOpPort.aliqRatAjust', 
                                                                          dadosOpPort.aliqRatAjust.cdata, 
                                                                          1, u'None')
                            
                            if 'basesRemun' in dir(ideLotacao.basesRemun):
                                for basesRemun in ideLotacao.basesRemun:
                                    
                                    if 'indIncid' in dir(basesRemun):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'basesRemun.indIncid', 
                                                                          basesRemun.indIncid.cdata, 
                                                                          1, u'None')
                                    
                                    if 'codCateg' in dir(basesRemun):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'basesRemun.codCateg', 
                                                                          basesRemun.codCateg.cdata, 
                                                                          1, u'101, 102, 103, 104, 105, 106, 111, 201, 202, 301, 302, 303, 305, 306, 307, 308, 309, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 751, 761, 771, 781, 901, 902, 903, 904, 905')
                                    
                                    if 'basesCp' in dir(basesRemun.basesCp):
                                        for basesCp in basesRemun.basesCp:
                                            
                                            if 'vrBcCp00' in dir(basesCp):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'basesCp.vrBcCp00', 
                                                                                  basesCp.vrBcCp00.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrBcCp15' in dir(basesCp):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'basesCp.vrBcCp15', 
                                                                                  basesCp.vrBcCp15.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrBcCp20' in dir(basesCp):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'basesCp.vrBcCp20', 
                                                                                  basesCp.vrBcCp20.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrBcCp25' in dir(basesCp):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'basesCp.vrBcCp25', 
                                                                                  basesCp.vrBcCp25.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrSuspBcCp00' in dir(basesCp):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'basesCp.vrSuspBcCp00', 
                                                                                  basesCp.vrSuspBcCp00.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrSuspBcCp15' in dir(basesCp):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'basesCp.vrSuspBcCp15', 
                                                                                  basesCp.vrSuspBcCp15.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrSuspBcCp20' in dir(basesCp):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'basesCp.vrSuspBcCp20', 
                                                                                  basesCp.vrSuspBcCp20.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrSuspBcCp25' in dir(basesCp):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'basesCp.vrSuspBcCp25', 
                                                                                  basesCp.vrSuspBcCp25.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrDescSest' in dir(basesCp):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'basesCp.vrDescSest', 
                                                                                  basesCp.vrDescSest.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrCalcSest' in dir(basesCp):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'basesCp.vrCalcSest', 
                                                                                  basesCp.vrCalcSest.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrDescSenat' in dir(basesCp):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'basesCp.vrDescSenat', 
                                                                                  basesCp.vrDescSenat.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrCalcSenat' in dir(basesCp):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'basesCp.vrCalcSenat', 
                                                                                  basesCp.vrCalcSenat.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrSalFam' in dir(basesCp):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'basesCp.vrSalFam', 
                                                                                  basesCp.vrSalFam.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrSalMat' in dir(basesCp):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'basesCp.vrSalMat', 
                                                                                  basesCp.vrSalMat.cdata, 
                                                                                  1, u'None')
                            
                            if 'basesAvNPort' in dir(ideLotacao.basesAvNPort):
                                for basesAvNPort in ideLotacao.basesAvNPort:
                                    
                                    if 'vrBcCp00' in dir(basesAvNPort):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'basesAvNPort.vrBcCp00', 
                                                                          basesAvNPort.vrBcCp00.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vrBcCp15' in dir(basesAvNPort):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'basesAvNPort.vrBcCp15', 
                                                                          basesAvNPort.vrBcCp15.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vrBcCp20' in dir(basesAvNPort):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'basesAvNPort.vrBcCp20', 
                                                                          basesAvNPort.vrBcCp20.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vrBcCp25' in dir(basesAvNPort):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'basesAvNPort.vrBcCp25', 
                                                                          basesAvNPort.vrBcCp25.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vrBcCp13' in dir(basesAvNPort):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'basesAvNPort.vrBcCp13', 
                                                                          basesAvNPort.vrBcCp13.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vrBcFgts' in dir(basesAvNPort):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'basesAvNPort.vrBcFgts', 
                                                                          basesAvNPort.vrBcFgts.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vrDescCP' in dir(basesAvNPort):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'basesAvNPort.vrDescCP', 
                                                                          basesAvNPort.vrDescCP.cdata, 
                                                                          1, u'None')
                            
                            if 'infoSubstPatrOpPort' in dir(ideLotacao.infoSubstPatrOpPort):
                                for infoSubstPatrOpPort in ideLotacao.infoSubstPatrOpPort:
                                    
                                    if 'cnpjOpPortuario' in dir(infoSubstPatrOpPort):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoSubstPatrOpPort.cnpjOpPortuario', 
                                                                          infoSubstPatrOpPort.cnpjOpPortuario.cdata, 
                                                                          1, u'None')
                    
                    if 'basesAquis' in dir(ideEstab.basesAquis):
                        for basesAquis in ideEstab.basesAquis:
                            
                            if 'indAquis' in dir(basesAquis):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'basesAquis.indAquis', 
                                                                  basesAquis.indAquis.cdata, 
                                                                  1, u'1, 2, 3, 4, 5, 6')
                            
                            if 'vlrAquis' in dir(basesAquis):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'basesAquis.vlrAquis', 
                                                                  basesAquis.vlrAquis.cdata, 
                                                                  1, u'None')
                            
                            if 'vrCPDescPR' in dir(basesAquis):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'basesAquis.vrCPDescPR', 
                                                                  basesAquis.vrCPDescPR.cdata, 
                                                                  1, u'None')
                            
                            if 'vrCPNRet' in dir(basesAquis):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'basesAquis.vrCPNRet', 
                                                                  basesAquis.vrCPNRet.cdata, 
                                                                  1, u'None')
                            
                            if 'vrRatNRet' in dir(basesAquis):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'basesAquis.vrRatNRet', 
                                                                  basesAquis.vrRatNRet.cdata, 
                                                                  1, u'None')
                            
                            if 'vrSenarNRet' in dir(basesAquis):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'basesAquis.vrSenarNRet', 
                                                                  basesAquis.vrSenarNRet.cdata, 
                                                                  1, u'None')
                            
                            if 'vrCPCalcPR' in dir(basesAquis):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'basesAquis.vrCPCalcPR', 
                                                                  basesAquis.vrCPCalcPR.cdata, 
                                                                  1, u'None')
                            
                            if 'vrRatDescPR' in dir(basesAquis):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'basesAquis.vrRatDescPR', 
                                                                  basesAquis.vrRatDescPR.cdata, 
                                                                  1, u'None')
                            
                            if 'vrRatCalcPR' in dir(basesAquis):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'basesAquis.vrRatCalcPR', 
                                                                  basesAquis.vrRatCalcPR.cdata, 
                                                                  1, u'None')
                            
                            if 'vrSenarDesc' in dir(basesAquis):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'basesAquis.vrSenarDesc', 
                                                                  basesAquis.vrSenarDesc.cdata, 
                                                                  1, u'None')
                            
                            if 'vrSenarCalc' in dir(basesAquis):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'basesAquis.vrSenarCalc', 
                                                                  basesAquis.vrSenarCalc.cdata, 
                                                                  1, u'None')
                    
                    if 'basesComerc' in dir(ideEstab.basesComerc):
                        for basesComerc in ideEstab.basesComerc:
                            
                            if 'indComerc' in dir(basesComerc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'basesComerc.indComerc', 
                                                                  basesComerc.indComerc.cdata, 
                                                                  1, u'2, 3, 7, 8, 9')
                            
                            if 'vrBcComPR' in dir(basesComerc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'basesComerc.vrBcComPR', 
                                                                  basesComerc.vrBcComPR.cdata, 
                                                                  1, u'None')
                            
                            if 'vrCPSusp' in dir(basesComerc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'basesComerc.vrCPSusp', 
                                                                  basesComerc.vrCPSusp.cdata, 
                                                                  0, u'None')
                            
                            if 'vrRatSusp' in dir(basesComerc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'basesComerc.vrRatSusp', 
                                                                  basesComerc.vrRatSusp.cdata, 
                                                                  0, u'None')
                            
                            if 'vrSenarSusp' in dir(basesComerc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'basesComerc.vrSenarSusp', 
                                                                  basesComerc.vrSenarSusp.cdata, 
                                                                  0, u'None')
                    
                    if 'infoCREstab' in dir(ideEstab.infoCREstab):
                        for infoCREstab in ideEstab.infoCREstab:
                            
                            if 'tpCR' in dir(infoCREstab):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCREstab.tpCR', 
                                                                  infoCREstab.tpCR.cdata, 
                                                                  1, u'None')
                            
                            if 'vrCR' in dir(infoCREstab):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCREstab.vrCR', 
                                                                  infoCREstab.vrCR.cdata, 
                                                                  1, u'None')
                            
                            if 'vrSuspCR' in dir(infoCREstab):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCREstab.vrSuspCR', 
                                                                  infoCREstab.vrSuspCR.cdata, 
                                                                  0, u'None')
            
            if 'infoCRContrib' in dir(infoCS.infoCRContrib):
                for infoCRContrib in infoCS.infoCRContrib:
                    
                    if 'tpCR' in dir(infoCRContrib):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoCRContrib.tpCR', 
                                                          infoCRContrib.tpCR.cdata, 
                                                          1, u'None')
                    
                    if 'vrCR' in dir(infoCRContrib):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoCRContrib.vrCR', 
                                                          infoCRContrib.vrCR.cdata, 
                                                          1, u'None')
                    
                    if 'vrCRSusp' in dir(infoCRContrib):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoCRContrib.vrCRSusp', 
                                                          infoCRContrib.vrCRSusp.cdata, 
                                                          0, u'None')
    return validacoes_lista