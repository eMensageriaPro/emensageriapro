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


def validacoes_r4010_evtretpf(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtRetPF = doc.Reinf.evtRetPF
    #variaveis
    
    if 'ideEvento' in dir(evtRetPF.ideEvento):
        for ideEvento in evtRetPF.ideEvento:
            
            if 'indRetif' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.indRetif', 
                                                  ideEvento.indRetif.cdata, 
                                                  1, u'1, 2')
            
            if 'nrRecibo' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.nrRecibo', 
                                                  ideEvento.nrRecibo.cdata, 
                                                  0, u'None')
            
            if 'perApur' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.perApur', 
                                                  ideEvento.perApur.cdata, 
                                                  1, u'None')
            
            if 'tpAmb' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.tpAmb', 
                                                  ideEvento.tpAmb.cdata, 
                                                  1, u'1, 2')
            
            if 'procEmi' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.procEmi', 
                                                  ideEvento.procEmi.cdata, 
                                                  1, u'1, 2')
            
            if 'verProc' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.verProc', 
                                                  ideEvento.verProc.cdata, 
                                                  1, u'None')
    
    if 'ideContri' in dir(evtRetPF.ideContri):
        for ideContri in evtRetPF.ideContri:
            
            if 'tpInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.tpInsc', 
                                                  ideContri.tpInsc.cdata, 
                                                  1, u'1, 2')
            
            if 'nrInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.nrInsc', 
                                                  ideContri.nrInsc.cdata, 
                                                  1, u'None')
    
    if 'ideEstab' in dir(evtRetPF.ideEstab):
        for ideEstab in evtRetPF.ideEstab:
            
            if 'tpInscEstab' in dir(ideEstab):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEstab.tpInscEstab', 
                                                  ideEstab.tpInscEstab.cdata, 
                                                  1, u'1, 2, 3')
            
            if 'nrInscEstab' in dir(ideEstab):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEstab.nrInscEstab', 
                                                  ideEstab.nrInscEstab.cdata, 
                                                  1, u'None')
            
            if 'ideBenef' in dir(ideEstab.ideBenef):
                for ideBenef in ideEstab.ideBenef:
                    
                    if 'cpfBenef' in dir(ideBenef):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideBenef.cpfBenef', 
                                                          ideBenef.cpfBenef.cdata, 
                                                          0, u'None')
                    
                    if 'nmBenef' in dir(ideBenef):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideBenef.nmBenef', 
                                                          ideBenef.nmBenef.cdata, 
                                                          0, u'None')
                    
                    if 'idePgto' in dir(ideBenef.idePgto):
                        for idePgto in ideBenef.idePgto:
                            
                            if 'natRend' in dir(idePgto):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePgto.natRend', 
                                                                  idePgto.natRend.cdata, 
                                                                  1, u'000000001, 000000002, 000000003, 000000004, 000000005, 000000006, 000000007, 000000008, 000000009, 000000010, 000000011, 000000012, 000000013, 000000014, 000000015, 000000016, 000000017, 000000018, 000000019, 000000020, 000000021, 000000022, 000000023, 000000024, 000000025, 000000026, 000000027, 000000028, 000000029, 000000030, 000000031, 000000032, 000000033, 000000034, 000000035, 000000036, 000000037, 000000038, 000000039, 000000040, 000000041, 000000042, 000000043, 000000044, 000000045, 000000046, 000000047, 000000048, 000000049, 000000050, 000000051, 000000052, 000000053, 000000054, 000000055, 000000056, 000000057, 000000058, 000000059, 000000060, 000000061, 000000062, 000000063, 000000064, 000000065, 000000066, 000000067, 000000068, 000000069, 000000070, 000000071, 000000072, 000000073, 000000074, 000000075, 000000076, 000000077, 000000078, 000000079, 000000080, 000000081, 000000082, 000000083, 000000084, 000000085, 000000086, 000000087, 000000088, 000000089, 000000090, 000000091, 000000092, 000000093, 000000094, 000000095, 000000096, 000000097, 000000098, 000000099, 000000100, 000000101, 000000102, 000000103, 000000104, 000000105, 000000106, 000000107, 000000108, 000000109, 000000110, 000000111, 000000112, 000000113, 000000114, 000000115, 000000116, 000000117, 000000118, 000000119, 000000120, 000000121, 000000122, 000000123, 000000124, 000000125, 000000126, 000000127, 000000128, 000000129, 000000130, 000000131, 000000132, 000000133, 000000134, 000000135, 200000001, 200000002, 200000003, 200000004, 200000005, 200000006, 200000007, 200000008, 200000009, 200000010, 200000011, 200000012, 200000013, 200000014, 200000015, 200000016, 200000017, 200000018, 200000019, 200000020, 200000021, 200000022, 200000023, 200000024, 200000025, 200000026, 200000027, 200000028, 200000029, 200000030, 200000031, 200000032, 200000033, 200000034, 200000035, 200000036, 200000037, 200000038')
                            
                            if 'paisResid' in dir(idePgto):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePgto.paisResid', 
                                                                  idePgto.paisResid.cdata, 
                                                                  1, u'008, 009, 013, 015, 017, 020, 023, 025, 031, 037, 040, 041, 042, 043, 047, 053, 059, 063, 064, 065, 069, 072, 073, 077, 080, 081, 083, 085, 087, 088, 090, 093, 097, 098, 099, 100, 101, 102, 105, 106, 108, 111, 115, 119, 127, 131, 137, 141, 145, 149, 150, 151, 152, 153, 154, 158, 160, 161, 163, 165, 169, 173, 177, 183, 187, 190, 193, 195, 196, 198, 199, 200, 229, 232, 235, 237, 239, 240, 243, 244, 245, 246, 247, 249, 251, 253, 255, 259, 263, 267, 271, 275, 281, 285, 289, 291, 292, 293, 297, 301, 305, 309, 313, 317, 321, 325, 329, 331, 334, 337, 341, 343, 345, 351, 355, 357, 358, 359, 361, 365, 367, 369, 372, 375, 379, 383, 386, 388, 391, 393, 395, 396, 399, 403, 411, 420, 423, 426, 427, 431, 434, 438, 440, 442, 445, 447, 449, 450, 452, 455, 458, 461, 464, 467, 472, 474, 476, 477, 485, 488, 489, 490, 493, 494, 495, 497, 498, 499, 501, 505, 507, 508, 511, 517, 521, 525, 528, 531, 535, 538, 542, 545, 548, 551, 556, 563, 566, 569, 573, 575, 576, 578, 580, 583, 586, 589, 593, 599, 603, 607, 611, 623, 625, 628, 640, 647, 660, 665, 670, 675, 676, 677, 678, 685, 687, 690, 691, 693, 695, 697, 698, 699, 700, 705, 710, 715, 720, 728, 731, 735, 737, 738, 741, 744, 748, 750, 754, 755, 756, 759, 760, 764, 767, 770, 772, 776, 780, 781, 782, 783, 785, 788, 790, 791, 795, 800, 805, 810, 815, 820, 823, 824, 827, 828, 831, 833, 840, 845, 847, 848, 850, 855, 858, 863, 866, 870, 873, 875, 888, 890, 895')
                            
                            if 'observ' in dir(idePgto):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePgto.observ', 
                                                                  idePgto.observ.cdata, 
                                                                  0, u'None')
                            
                            if 'infoPgto' in dir(idePgto.infoPgto):
                                for infoPgto in idePgto.infoPgto:
                                    
                                    if 'dtFG' in dir(infoPgto):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgto.dtFG', 
                                                                          infoPgto.dtFG.cdata, 
                                                                          1, u'None')
                                    
                                    if 'indDecTerc' in dir(infoPgto):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgto.indDecTerc', 
                                                                          infoPgto.indDecTerc.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'vlrRendBruto' in dir(infoPgto):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgto.vlrRendBruto', 
                                                                          infoPgto.vlrRendBruto.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vlrRendTrib' in dir(infoPgto):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgto.vlrRendTrib', 
                                                                          infoPgto.vlrRendTrib.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vlrIR' in dir(infoPgto):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgto.vlrIR', 
                                                                          infoPgto.vlrIR.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vlrRendSusp' in dir(infoPgto):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgto.vlrRendSusp', 
                                                                          infoPgto.vlrRendSusp.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vlrNIR' in dir(infoPgto):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgto.vlrNIR', 
                                                                          infoPgto.vlrNIR.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vlrDeposito' in dir(infoPgto):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgto.vlrDeposito', 
                                                                          infoPgto.vlrDeposito.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vlrCompAnoCalend' in dir(infoPgto):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgto.vlrCompAnoCalend', 
                                                                          infoPgto.vlrCompAnoCalend.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vlrCompAnoAnt' in dir(infoPgto):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgto.vlrCompAnoAnt', 
                                                                          infoPgto.vlrCompAnoAnt.cdata, 
                                                                          0, u'None')
                                    
                                    if 'FCI' in dir(infoPgto.FCI):
                                        for FCI in infoPgto.FCI:
                                            
                                            if 'nrInscFCI' in dir(FCI):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'FCI.nrInscFCI', 
                                                                                  FCI.nrInscFCI.cdata, 
                                                                                  1, u'None')
                                    
                                    if 'SCP' in dir(infoPgto.SCP):
                                        for SCP in infoPgto.SCP:
                                            
                                            if 'nrInscSCP' in dir(SCP):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'SCP.nrInscSCP', 
                                                                                  SCP.nrInscSCP.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'percSCP' in dir(SCP):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'SCP.percSCP', 
                                                                                  SCP.percSCP.cdata, 
                                                                                  1, u'None')
                                    
                                    if 'detDed' in dir(infoPgto.detDed):
                                        for detDed in infoPgto.detDed:
                                            
                                            if 'indTpDeducao' in dir(detDed):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'detDed.indTpDeducao', 
                                                                                  detDed.indTpDeducao.cdata, 
                                                                                  1, u'1, 2, 3, 4, 5, 6, 7')
                                            
                                            if 'vlrDeducao' in dir(detDed):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'detDed.vlrDeducao', 
                                                                                  detDed.vlrDeducao.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vlrDedSusp' in dir(detDed):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'detDed.vlrDedSusp', 
                                                                                  detDed.vlrDedSusp.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'nrInscPrevComp' in dir(detDed):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'detDed.nrInscPrevComp', 
                                                                                  detDed.nrInscPrevComp.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'benefPen' in dir(detDed.benefPen):
                                                for benefPen in detDed.benefPen:
                                                    
                                                    if 'cpf' in dir(benefPen):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'benefPen.cpf', 
                                                                                          benefPen.cpf.cdata, 
                                                                                          0, u'None')
                                                    
                                                    if 'dtNascto' in dir(benefPen):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'benefPen.dtNascto', 
                                                                                          benefPen.dtNascto.cdata, 
                                                                                          0, u'None')
                                                    
                                                    if 'nome' in dir(benefPen):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'benefPen.nome', 
                                                                                          benefPen.nome.cdata, 
                                                                                          1, u'None')
                                                    
                                                    if 'relDep' in dir(benefPen):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'benefPen.relDep', 
                                                                                          benefPen.relDep.cdata, 
                                                                                          1, u'1, 2, 3, 4, 5, 6, 7, 99')
                                                    
                                                    if 'descrDep' in dir(benefPen):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'benefPen.descrDep', 
                                                                                          benefPen.descrDep.cdata, 
                                                                                          0, u'None')
                                    
                                    if 'rendIsento' in dir(infoPgto.rendIsento):
                                        for rendIsento in infoPgto.rendIsento:
                                            
                                            if 'tpIsencao' in dir(rendIsento):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'rendIsento.tpIsencao', 
                                                                                  rendIsento.tpIsencao.cdata, 
                                                                                  1, u'1, 2, 3, 4, 5, 6, 7, 8, 99')
                                            
                                            if 'vlrIsento' in dir(rendIsento):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'rendIsento.vlrIsento', 
                                                                                  rendIsento.vlrIsento.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'descRendimento' in dir(rendIsento):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'rendIsento.descRendimento', 
                                                                                  rendIsento.descRendimento.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'dtLaudo' in dir(rendIsento):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'rendIsento.dtLaudo', 
                                                                                  rendIsento.dtLaudo.cdata, 
                                                                                  0, u'None')
                                    
                                    if 'infoProcRet' in dir(infoPgto.infoProcRet):
                                        for infoProcRet in infoPgto.infoProcRet:
                                            
                                            if 'tpProcRet' in dir(infoProcRet):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcRet.tpProcRet', 
                                                                                  infoProcRet.tpProcRet.cdata, 
                                                                                  1, u'1, 2')
                                            
                                            if 'nrProcRet' in dir(infoProcRet):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcRet.nrProcRet', 
                                                                                  infoProcRet.nrProcRet.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'codSusp' in dir(infoProcRet):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcRet.codSusp', 
                                                                                  infoProcRet.codSusp.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'vlrNRetido' in dir(infoProcRet):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcRet.vlrNRetido', 
                                                                                  infoProcRet.vlrNRetido.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'vlrDep' in dir(infoProcRet):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcRet.vlrDep', 
                                                                                  infoProcRet.vlrDep.cdata, 
                                                                                  0, u'None')
                                    
                                    if 'infoRRA' in dir(infoPgto.infoRRA):
                                        for infoRRA in infoPgto.infoRRA:
                                            
                                            if 'tpProcRRA' in dir(infoRRA):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoRRA.tpProcRRA', 
                                                                                  infoRRA.tpProcRRA.cdata, 
                                                                                  1, u'1, 2')
                                            
                                            if 'nrProcRRA' in dir(infoRRA):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoRRA.nrProcRRA', 
                                                                                  infoRRA.nrProcRRA.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'indOrigRec' in dir(infoRRA):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoRRA.indOrigRec', 
                                                                                  infoRRA.indOrigRec.cdata, 
                                                                                  1, u'1, 2')
                                            
                                            if 'descRRA' in dir(infoRRA):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoRRA.descRRA', 
                                                                                  infoRRA.descRRA.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'qtdMesesRRA' in dir(infoRRA):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoRRA.qtdMesesRRA', 
                                                                                  infoRRA.qtdMesesRRA.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'despProcJud' in dir(infoRRA.despProcJud):
                                                for despProcJud in infoRRA.despProcJud:
                                                    
                                                    if 'vlrDespCustas' in dir(despProcJud):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'despProcJud.vlrDespCustas', 
                                                                                          despProcJud.vlrDespCustas.cdata, 
                                                                                          1, u'None')
                                                    
                                                    if 'vlrDespAdvogados' in dir(despProcJud):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'despProcJud.vlrDespAdvogados', 
                                                                                          despProcJud.vlrDespAdvogados.cdata, 
                                                                                          1, u'None')
                                                    
                                                    if 'ideAdv' in dir(despProcJud.ideAdv):
                                                        for ideAdv in despProcJud.ideAdv:
                                                            
                                                            if 'tpInscAdv' in dir(ideAdv):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'ideAdv.tpInscAdv', 
                                                                                                  ideAdv.tpInscAdv.cdata, 
                                                                                                  1, u'1, 2')
                                                            
                                                            if 'nrInscAdv' in dir(ideAdv):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'ideAdv.nrInscAdv', 
                                                                                                  ideAdv.nrInscAdv.cdata, 
                                                                                                  1, u'None')
                                                            
                                                            if 'vlrAdv' in dir(ideAdv):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'ideAdv.vlrAdv', 
                                                                                                  ideAdv.vlrAdv.cdata, 
                                                                                                  1, u'None')
                                            
                                            if 'origemRec' in dir(infoRRA.origemRec):
                                                for origemRec in infoRRA.origemRec:
                                                    
                                                    if 'cnpjOrigRecurso' in dir(origemRec):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'origemRec.cnpjOrigRecurso', 
                                                                                          origemRec.cnpjOrigRecurso.cdata, 
                                                                                          1, u'None')
                                    
                                    if 'infoProcJud' in dir(infoPgto.infoProcJud):
                                        for infoProcJud in infoPgto.infoProcJud:
                                            
                                            if 'nrProc' in dir(infoProcJud):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcJud.nrProc', 
                                                                                  infoProcJud.nrProc.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'indOrigRec' in dir(infoProcJud):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcJud.indOrigRec', 
                                                                                  infoProcJud.indOrigRec.cdata, 
                                                                                  1, u'1, 2')
                                            
                                            if 'desc' in dir(infoProcJud):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcJud.desc', 
                                                                                  infoProcJud.desc.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'despProcJud' in dir(infoProcJud.despProcJud):
                                                for despProcJud in infoProcJud.despProcJud:
                                                    
                                                    if 'vlrDespCustas' in dir(despProcJud):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'despProcJud.vlrDespCustas', 
                                                                                          despProcJud.vlrDespCustas.cdata, 
                                                                                          1, u'None')
                                                    
                                                    if 'vlrDespAdvogados' in dir(despProcJud):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'despProcJud.vlrDespAdvogados', 
                                                                                          despProcJud.vlrDespAdvogados.cdata, 
                                                                                          1, u'None')
                                                    
                                                    if 'ideAdv' in dir(despProcJud.ideAdv):
                                                        for ideAdv in despProcJud.ideAdv:
                                                            
                                                            if 'tpInscAdv' in dir(ideAdv):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'ideAdv.tpInscAdv', 
                                                                                                  ideAdv.tpInscAdv.cdata, 
                                                                                                  1, u'1, 2')
                                                            
                                                            if 'nrInscAdv' in dir(ideAdv):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'ideAdv.nrInscAdv', 
                                                                                                  ideAdv.nrInscAdv.cdata, 
                                                                                                  1, u'None')
                                                            
                                                            if 'vlrAdv' in dir(ideAdv):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'ideAdv.vlrAdv', 
                                                                                                  ideAdv.vlrAdv.cdata, 
                                                                                                  1, u'None')
                                            
                                            if 'origemRec' in dir(infoProcJud.origemRec):
                                                for origemRec in infoProcJud.origemRec:
                                                    
                                                    if 'cnpjOrigRecurso' in dir(origemRec):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'origemRec.cnpjOrigRecurso', 
                                                                                          origemRec.cnpjOrigRecurso.cdata, 
                                                                                          1, u'None')
                            
                            if 'infoPgtoExt' in dir(idePgto.infoPgtoExt):
                                for infoPgtoExt in idePgto.infoPgtoExt:
                                    
                                    if 'endExt' in dir(infoPgtoExt.endExt):
                                        for endExt in infoPgtoExt.endExt:
                                            
                                            if 'dscLograd' in dir(endExt):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'endExt.dscLograd', 
                                                                                  endExt.dscLograd.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'nrLograd' in dir(endExt):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'endExt.nrLograd', 
                                                                                  endExt.nrLograd.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'complem' in dir(endExt):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'endExt.complem', 
                                                                                  endExt.complem.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'bairro' in dir(endExt):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'endExt.bairro', 
                                                                                  endExt.bairro.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'cidade' in dir(endExt):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'endExt.cidade', 
                                                                                  endExt.cidade.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'estado' in dir(endExt):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'endExt.estado', 
                                                                                  endExt.estado.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'codPostal' in dir(endExt):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'endExt.codPostal', 
                                                                                  endExt.codPostal.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'telef' in dir(endExt):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'endExt.telef', 
                                                                                  endExt.telef.cdata, 
                                                                                  0, u'None')
                                    
                                    if 'infoFiscal' in dir(infoPgtoExt.infoFiscal):
                                        for infoFiscal in infoPgtoExt.infoFiscal:
                                            
                                            if 'indNIF' in dir(infoFiscal):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoFiscal.indNIF', 
                                                                                  infoFiscal.indNIF.cdata, 
                                                                                  1, u'1, 2, 3')
                                            
                                            if 'nifBenef' in dir(infoFiscal):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoFiscal.nifBenef', 
                                                                                  infoFiscal.nifBenef.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'frmTribut' in dir(infoFiscal):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoFiscal.frmTribut', 
                                                                                  infoFiscal.frmTribut.cdata, 
                                                                                  1, u'10, 11, 12, 13, 30, 40, 41, 42, 43, 44, 50')
                    
                    if 'ideOpSaude' in dir(ideBenef.ideOpSaude):
                        for ideOpSaude in ideBenef.ideOpSaude:
                            
                            if 'nrInsc' in dir(ideOpSaude):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideOpSaude.nrInsc', 
                                                                  ideOpSaude.nrInsc.cdata, 
                                                                  1, u'None')
                            
                            if 'regANS' in dir(ideOpSaude):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideOpSaude.regANS', 
                                                                  ideOpSaude.regANS.cdata, 
                                                                  0, u'None')
                            
                            if 'vlrSaude' in dir(ideOpSaude):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideOpSaude.vlrSaude', 
                                                                  ideOpSaude.vlrSaude.cdata, 
                                                                  1, u'None')
                            
                            if 'infoReemb' in dir(ideOpSaude.infoReemb):
                                for infoReemb in ideOpSaude.infoReemb:
                                    
                                    if 'tpInsc' in dir(infoReemb):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoReemb.tpInsc', 
                                                                          infoReemb.tpInsc.cdata, 
                                                                          1, u'1, 2')
                                    
                                    if 'nrInsc' in dir(infoReemb):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoReemb.nrInsc', 
                                                                          infoReemb.nrInsc.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vlrReemb' in dir(infoReemb):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoReemb.vlrReemb', 
                                                                          infoReemb.vlrReemb.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vlrReembAnt' in dir(infoReemb):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoReemb.vlrReembAnt', 
                                                                          infoReemb.vlrReembAnt.cdata, 
                                                                          0, u'None')
                            
                            if 'infoDependPl' in dir(ideOpSaude.infoDependPl):
                                for infoDependPl in ideOpSaude.infoDependPl:
                                    
                                    if 'cpf' in dir(infoDependPl):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoDependPl.cpf', 
                                                                          infoDependPl.cpf.cdata, 
                                                                          0, u'None')
                                    
                                    if 'dtNascto' in dir(infoDependPl):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoDependPl.dtNascto', 
                                                                          infoDependPl.dtNascto.cdata, 
                                                                          0, u'None')
                                    
                                    if 'nome' in dir(infoDependPl):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoDependPl.nome', 
                                                                          infoDependPl.nome.cdata, 
                                                                          1, u'None')
                                    
                                    if 'relDep' in dir(infoDependPl):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoDependPl.relDep', 
                                                                          infoDependPl.relDep.cdata, 
                                                                          1, u'1, 2, 3, 4, 5, 6, 7, 99')
                                    
                                    if 'vlrSaude' in dir(infoDependPl):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoDependPl.vlrSaude', 
                                                                          infoDependPl.vlrSaude.cdata, 
                                                                          1, u'None')
                                    
                                    if 'infoReembDep' in dir(infoDependPl.infoReembDep):
                                        for infoReembDep in infoDependPl.infoReembDep:
                                            
                                            if 'tpInsc' in dir(infoReembDep):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoReembDep.tpInsc', 
                                                                                  infoReembDep.tpInsc.cdata, 
                                                                                  1, u'1, 2')
                                            
                                            if 'nrInsc' in dir(infoReembDep):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoReembDep.nrInsc', 
                                                                                  infoReembDep.nrInsc.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vlrReemb' in dir(infoReembDep):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoReembDep.vlrReemb', 
                                                                                  infoReembDep.vlrReemb.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vlrReembAnt' in dir(infoReembDep):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoReembDep.vlrReembAnt', 
                                                                                  infoReembDep.vlrReembAnt.cdata, 
                                                                                  0, u'None')
    return validacoes_lista