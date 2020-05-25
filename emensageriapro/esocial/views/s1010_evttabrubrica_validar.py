# eMensageriaAI #
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


def validacoes_s1010_evttabrubrica(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabRubrica = doc.eSocial.evtTabRubrica
    #variaveis

    if 'ideEvento' in dir(evtTabRubrica.ideEvento):
        for ideEvento in evtTabRubrica.ideEvento:

            if 'tpAmb' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.tpAmb',
                                                  ideEvento.tpAmb.cdata,
                                                  1, u'1, 2')

            if 'procEmi' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.procEmi',
                                                  ideEvento.procEmi.cdata,
                                                  1, u'1, 2, 3, 4, 5')

            if 'verProc' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.verProc',
                                                  ideEvento.verProc.cdata,
                                                  1, u'None')

    if 'ideEmpregador' in dir(evtTabRubrica.ideEmpregador):
        for ideEmpregador in evtTabRubrica.ideEmpregador:

            if 'tpInsc' in dir(ideEmpregador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEmpregador.tpInsc',
                                                  ideEmpregador.tpInsc.cdata,
                                                  1, u'1, 2, 3, 4, 5, 6')

            if 'nrInsc' in dir(ideEmpregador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEmpregador.nrInsc',
                                                  ideEmpregador.nrInsc.cdata,
                                                  1, u'None')

    if 'infoRubrica' in dir(evtTabRubrica.infoRubrica):
        for infoRubrica in evtTabRubrica.infoRubrica:

            if 'inclusao' in dir(infoRubrica.inclusao):
                for inclusao in infoRubrica.inclusao:

                    if 'ideRubrica' in dir(inclusao.ideRubrica):
                        for ideRubrica in inclusao.ideRubrica:
        
                            if 'codRubr' in dir(ideRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideRubrica.codRubr',
                                                                  ideRubrica.codRubr.cdata,
                                                                  1, u'None')
        
                            if 'ideTabRubr' in dir(ideRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideRubrica.ideTabRubr',
                                                                  ideRubrica.ideTabRubr.cdata,
                                                                  1, u'None')
        
                            if 'iniValid' in dir(ideRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideRubrica.iniValid',
                                                                  ideRubrica.iniValid.cdata,
                                                                  1, u'None')
        
                            if 'fimValid' in dir(ideRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideRubrica.fimValid',
                                                                  ideRubrica.fimValid.cdata,
                                                                  0, u'None')

                    if 'dadosRubrica' in dir(inclusao.dadosRubrica):
                        for dadosRubrica in inclusao.dadosRubrica:
        
                            if 'dscRubr' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.dscRubr',
                                                                  dadosRubrica.dscRubr.cdata,
                                                                  1, u'None')
        
                            if 'natRubr' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.natRubr',
                                                                  dadosRubrica.natRubr.cdata,
                                                                  1, u'1000, 1002, 1003, 1004, 1005, 1006, 1007, 1009, 1010, 1011, 1020, 1021, 1022, 1023, 1024, 1040, 1041, 1050, 1080, 1099, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1225, 1230, 1299, 1300, 1350, 1351, 1352, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1409, 1410, 1601, 1602, 1603, 1604, 1619, 1620, 1621, 1623, 1629, 1650, 1651, 1652, 1801, 1802, 1805, 1810, 2501, 2502, 2510, 2801, 2901, 2902, 2920, 2930, 2999, 3501, 3505, 3506, 3508, 3509, 3520, 3525, 4010, 4050, 4051, 5001, 5005, 5501, 5504, 5510, 6000, 6001, 6002, 6003, 6004, 6006, 6007, 6101, 6102, 6103, 6104, 6105, 6106, 6107, 6119, 6129, 6901, 6904, 7001, 7002, 7003, 7004, 7005, 9200, 9201, 9203, 9205, 9209, 9210, 9213, 9214, 9216, 9217, 9218, 9219, 9220, 9221, 9222, 9223, 9224, 9225, 9226, 9230, 9231, 9232, 9233, 9250, 9254, 9255, 9258, 9260, 9270, 9290, 9299, 9901, 9902, 9903, 9904, 9905, 9906, 9908, 9910, 9911, 9930, 9931, 9932, 9933, 9938, 9939, 9950, 9951, 9989')
        
                            if 'tpRubr' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.tpRubr',
                                                                  dadosRubrica.tpRubr.cdata,
                                                                  1, u'1, 2, 3, 4')
        
                            if 'codIncCP' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.codIncCP',
                                                                  dadosRubrica.codIncCP.cdata,
                                                                  1, u'00, 01, 11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 34, 35, 51, 61, 91, 92, 93, 94, 95, 96, 97, 98')
        
                            if 'codIncIRRF' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.codIncIRRF',
                                                                  dadosRubrica.codIncIRRF.cdata,
                                                                  1, u'00, 01, 09, 11, 12, 13, 14, 15, 31, 32, 33, 34, 35, 41, 42, 43, 44, 46, 47, 51, 52, 53, 54, 55, 61, 62, 63, 64, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 81, 82, 83, 91, 92, 93, 94, 95')
        
                            if 'codIncFGTS' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.codIncFGTS',
                                                                  dadosRubrica.codIncFGTS.cdata,
                                                                  1, u'00, 11, 12, 21, 91')
        
                            if 'codIncSIND' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.codIncSIND',
                                                                  dadosRubrica.codIncSIND.cdata,
                                                                  1, u'00, 11, 31, 91')
        
                            if 'codIncCPRP' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.codIncCPRP',
                                                                  dadosRubrica.codIncCPRP.cdata,
                                                                  0, u'00, 01, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 31, 32, 33, 34, 35, 36, 41, 42, 51, 52, 91, 92, 93, 94, 95, 96')
        
                            if 'tetoRemun' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.tetoRemun',
                                                                  dadosRubrica.tetoRemun.cdata,
                                                                  0, u'S, N')
        
                            if 'observacao' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.observacao',
                                                                  dadosRubrica.observacao.cdata,
                                                                  0, u'None')
        
                            if 'ideProcessoCP' in dir(dadosRubrica.ideProcessoCP):
                                for ideProcessoCP in dadosRubrica.ideProcessoCP:
                
                                    if 'tpProc' in dir(ideProcessoCP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoCP.tpProc',
                                                                          ideProcessoCP.tpProc.cdata,
                                                                          1, u'1, 2')
                
                                    if 'nrProc' in dir(ideProcessoCP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoCP.nrProc',
                                                                          ideProcessoCP.nrProc.cdata,
                                                                          1, u'None')
                
                                    if 'extDecisao' in dir(ideProcessoCP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoCP.extDecisao',
                                                                          ideProcessoCP.extDecisao.cdata,
                                                                          1, u'1, 2')
                
                                    if 'codSusp' in dir(ideProcessoCP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoCP.codSusp',
                                                                          ideProcessoCP.codSusp.cdata,
                                                                          1, u'None')
        
                            if 'ideProcessoIRRF' in dir(dadosRubrica.ideProcessoIRRF):
                                for ideProcessoIRRF in dadosRubrica.ideProcessoIRRF:
                
                                    if 'nrProc' in dir(ideProcessoIRRF):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoIRRF.nrProc',
                                                                          ideProcessoIRRF.nrProc.cdata,
                                                                          1, u'None')
                
                                    if 'codSusp' in dir(ideProcessoIRRF):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoIRRF.codSusp',
                                                                          ideProcessoIRRF.codSusp.cdata,
                                                                          1, u'None')
        
                            if 'ideProcessoFGTS' in dir(dadosRubrica.ideProcessoFGTS):
                                for ideProcessoFGTS in dadosRubrica.ideProcessoFGTS:
                
                                    if 'nrProc' in dir(ideProcessoFGTS):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoFGTS.nrProc',
                                                                          ideProcessoFGTS.nrProc.cdata,
                                                                          1, u'None')
        
                            if 'ideProcessoSIND' in dir(dadosRubrica.ideProcessoSIND):
                                for ideProcessoSIND in dadosRubrica.ideProcessoSIND:
                
                                    if 'nrProc' in dir(ideProcessoSIND):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoSIND.nrProc',
                                                                          ideProcessoSIND.nrProc.cdata,
                                                                          1, u'None')
        
                            if 'ideProcessoCPRP' in dir(dadosRubrica.ideProcessoCPRP):
                                for ideProcessoCPRP in dadosRubrica.ideProcessoCPRP:
                
                                    if 'tpProc' in dir(ideProcessoCPRP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoCPRP.tpProc',
                                                                          ideProcessoCPRP.tpProc.cdata,
                                                                          1, u'1, 2')
                
                                    if 'nrProc' in dir(ideProcessoCPRP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoCPRP.nrProc',
                                                                          ideProcessoCPRP.nrProc.cdata,
                                                                          1, u'None')
                
                                    if 'extDecisao' in dir(ideProcessoCPRP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoCPRP.extDecisao',
                                                                          ideProcessoCPRP.extDecisao.cdata,
                                                                          1, u'1, 2, 3')

            if 'alteracao' in dir(infoRubrica.alteracao):
                for alteracao in infoRubrica.alteracao:

                    if 'ideRubrica' in dir(alteracao.ideRubrica):
                        for ideRubrica in alteracao.ideRubrica:
        
                            if 'codRubr' in dir(ideRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideRubrica.codRubr',
                                                                  ideRubrica.codRubr.cdata,
                                                                  1, u'None')
        
                            if 'ideTabRubr' in dir(ideRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideRubrica.ideTabRubr',
                                                                  ideRubrica.ideTabRubr.cdata,
                                                                  1, u'None')
        
                            if 'iniValid' in dir(ideRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideRubrica.iniValid',
                                                                  ideRubrica.iniValid.cdata,
                                                                  1, u'None')
        
                            if 'fimValid' in dir(ideRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideRubrica.fimValid',
                                                                  ideRubrica.fimValid.cdata,
                                                                  0, u'None')

                    if 'dadosRubrica' in dir(alteracao.dadosRubrica):
                        for dadosRubrica in alteracao.dadosRubrica:
        
                            if 'dscRubr' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.dscRubr',
                                                                  dadosRubrica.dscRubr.cdata,
                                                                  1, u'None')
        
                            if 'natRubr' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.natRubr',
                                                                  dadosRubrica.natRubr.cdata,
                                                                  1, u'1000, 1002, 1003, 1004, 1005, 1006, 1007, 1009, 1010, 1011, 1020, 1021, 1022, 1023, 1024, 1040, 1041, 1050, 1080, 1099, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1225, 1230, 1299, 1300, 1350, 1351, 1352, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1409, 1410, 1601, 1602, 1603, 1604, 1619, 1620, 1621, 1623, 1629, 1650, 1651, 1652, 1801, 1802, 1805, 1810, 2501, 2502, 2510, 2801, 2901, 2902, 2920, 2930, 2999, 3501, 3505, 3506, 3508, 3509, 3520, 3525, 4010, 4050, 4051, 5001, 5005, 5501, 5504, 5510, 6000, 6001, 6002, 6003, 6004, 6006, 6007, 6101, 6102, 6103, 6104, 6105, 6106, 6107, 6119, 6129, 6901, 6904, 7001, 7002, 7003, 7004, 7005, 9200, 9201, 9203, 9205, 9209, 9210, 9213, 9214, 9216, 9217, 9218, 9219, 9220, 9221, 9222, 9223, 9224, 9225, 9226, 9230, 9231, 9232, 9233, 9250, 9254, 9255, 9258, 9260, 9270, 9290, 9299, 9901, 9902, 9903, 9904, 9905, 9906, 9908, 9910, 9911, 9930, 9931, 9932, 9933, 9938, 9939, 9950, 9951, 9989')
        
                            if 'tpRubr' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.tpRubr',
                                                                  dadosRubrica.tpRubr.cdata,
                                                                  1, u'1, 2, 3, 4')
        
                            if 'codIncCP' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.codIncCP',
                                                                  dadosRubrica.codIncCP.cdata,
                                                                  1, u'00, 01, 11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 34, 35, 51, 61, 91, 92, 93, 94, 95, 96, 97, 98')
        
                            if 'codIncIRRF' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.codIncIRRF',
                                                                  dadosRubrica.codIncIRRF.cdata,
                                                                  1, u'00, 01, 09, 11, 12, 13, 14, 15, 31, 32, 33, 34, 35, 41, 42, 43, 44, 46, 47, 51, 52, 53, 54, 55, 61, 62, 63, 64, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 81, 82, 83, 91, 92, 93, 94, 95')
        
                            if 'codIncFGTS' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.codIncFGTS',
                                                                  dadosRubrica.codIncFGTS.cdata,
                                                                  1, u'00, 11, 12, 21, 91')
        
                            if 'codIncSIND' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.codIncSIND',
                                                                  dadosRubrica.codIncSIND.cdata,
                                                                  1, u'00, 11, 31, 91')
        
                            if 'codIncCPRP' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.codIncCPRP',
                                                                  dadosRubrica.codIncCPRP.cdata,
                                                                  0, u'00, 01, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 31, 32, 33, 34, 35, 36, 41, 42, 51, 52, 91, 92, 93, 94, 95, 96')
        
                            if 'tetoRemun' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.tetoRemun',
                                                                  dadosRubrica.tetoRemun.cdata,
                                                                  0, u'S, N')
        
                            if 'observacao' in dir(dadosRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosRubrica.observacao',
                                                                  dadosRubrica.observacao.cdata,
                                                                  0, u'None')
        
                            if 'ideProcessoCP' in dir(dadosRubrica.ideProcessoCP):
                                for ideProcessoCP in dadosRubrica.ideProcessoCP:
                
                                    if 'tpProc' in dir(ideProcessoCP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoCP.tpProc',
                                                                          ideProcessoCP.tpProc.cdata,
                                                                          1, u'1, 2')
                
                                    if 'nrProc' in dir(ideProcessoCP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoCP.nrProc',
                                                                          ideProcessoCP.nrProc.cdata,
                                                                          1, u'None')
                
                                    if 'extDecisao' in dir(ideProcessoCP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoCP.extDecisao',
                                                                          ideProcessoCP.extDecisao.cdata,
                                                                          1, u'1, 2')
                
                                    if 'codSusp' in dir(ideProcessoCP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoCP.codSusp',
                                                                          ideProcessoCP.codSusp.cdata,
                                                                          1, u'None')
        
                            if 'ideProcessoIRRF' in dir(dadosRubrica.ideProcessoIRRF):
                                for ideProcessoIRRF in dadosRubrica.ideProcessoIRRF:
                
                                    if 'nrProc' in dir(ideProcessoIRRF):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoIRRF.nrProc',
                                                                          ideProcessoIRRF.nrProc.cdata,
                                                                          1, u'None')
                
                                    if 'codSusp' in dir(ideProcessoIRRF):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoIRRF.codSusp',
                                                                          ideProcessoIRRF.codSusp.cdata,
                                                                          1, u'None')
        
                            if 'ideProcessoFGTS' in dir(dadosRubrica.ideProcessoFGTS):
                                for ideProcessoFGTS in dadosRubrica.ideProcessoFGTS:
                
                                    if 'nrProc' in dir(ideProcessoFGTS):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoFGTS.nrProc',
                                                                          ideProcessoFGTS.nrProc.cdata,
                                                                          1, u'None')
        
                            if 'ideProcessoSIND' in dir(dadosRubrica.ideProcessoSIND):
                                for ideProcessoSIND in dadosRubrica.ideProcessoSIND:
                
                                    if 'nrProc' in dir(ideProcessoSIND):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoSIND.nrProc',
                                                                          ideProcessoSIND.nrProc.cdata,
                                                                          1, u'None')
        
                            if 'ideProcessoCPRP' in dir(dadosRubrica.ideProcessoCPRP):
                                for ideProcessoCPRP in dadosRubrica.ideProcessoCPRP:
                
                                    if 'tpProc' in dir(ideProcessoCPRP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoCPRP.tpProc',
                                                                          ideProcessoCPRP.tpProc.cdata,
                                                                          1, u'1, 2')
                
                                    if 'nrProc' in dir(ideProcessoCPRP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoCPRP.nrProc',
                                                                          ideProcessoCPRP.nrProc.cdata,
                                                                          1, u'None')
                
                                    if 'extDecisao' in dir(ideProcessoCPRP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProcessoCPRP.extDecisao',
                                                                          ideProcessoCPRP.extDecisao.cdata,
                                                                          1, u'1, 2, 3')

                    if 'novaValidade' in dir(alteracao.novaValidade):
                        for novaValidade in alteracao.novaValidade:
        
                            if 'iniValid' in dir(novaValidade):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'novaValidade.iniValid',
                                                                  novaValidade.iniValid.cdata,
                                                                  1, u'None')
        
                            if 'fimValid' in dir(novaValidade):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'novaValidade.fimValid',
                                                                  novaValidade.fimValid.cdata,
                                                                  0, u'None')

            if 'exclusao' in dir(infoRubrica.exclusao):
                for exclusao in infoRubrica.exclusao:

                    if 'ideRubrica' in dir(exclusao.ideRubrica):
                        for ideRubrica in exclusao.ideRubrica:
        
                            if 'codRubr' in dir(ideRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideRubrica.codRubr',
                                                                  ideRubrica.codRubr.cdata,
                                                                  1, u'None')
        
                            if 'ideTabRubr' in dir(ideRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideRubrica.ideTabRubr',
                                                                  ideRubrica.ideTabRubr.cdata,
                                                                  1, u'None')
        
                            if 'iniValid' in dir(ideRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideRubrica.iniValid',
                                                                  ideRubrica.iniValid.cdata,
                                                                  1, u'None')
        
                            if 'fimValid' in dir(ideRubrica):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideRubrica.fimValid',
                                                                  ideRubrica.fimValid.cdata,
                                                                  0, u'None')
    return validacoes_lista