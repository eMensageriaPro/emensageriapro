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


def validacoes_s2405_evtcdbenefalt(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtCdBenefAlt = doc.eSocial.evtCdBenefAlt
    #variaveis
    
    if 'ideEvento' in dir(evtCdBenefAlt.ideEvento):
        for ideEvento in evtCdBenefAlt.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtCdBenefAlt.ideEmpregador):
        for ideEmpregador in evtCdBenefAlt.ideEmpregador:
            
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
    
    if 'ideBenef' in dir(evtCdBenefAlt.ideBenef):
        for ideBenef in evtCdBenefAlt.ideBenef:
            
            if 'cpfBenef' in dir(ideBenef):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideBenef.cpfBenef', 
                                                  ideBenef.cpfBenef.cdata, 
                                                  1, u'None')
    
    if 'alteracao' in dir(evtCdBenefAlt.alteracao):
        for alteracao in evtCdBenefAlt.alteracao:
            
            if 'dtAlteracao' in dir(alteracao):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'alteracao.dtAlteracao', 
                                                  alteracao.dtAlteracao.cdata, 
                                                  1, u'None')
            
            if 'dadosBenef' in dir(alteracao.dadosBenef):
                for dadosBenef in alteracao.dadosBenef:
                    
                    if 'nisBenef' in dir(dadosBenef):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosBenef.nisBenef', 
                                                          dadosBenef.nisBenef.cdata, 
                                                          0, u'None')
                    
                    if 'nmBenefic' in dir(dadosBenef):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosBenef.nmBenefic', 
                                                          dadosBenef.nmBenefic.cdata, 
                                                          1, u'None')
                    
                    if 'sexo' in dir(dadosBenef):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosBenef.sexo', 
                                                          dadosBenef.sexo.cdata, 
                                                          1, u'M, F')
                    
                    if 'racaCor' in dir(dadosBenef):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosBenef.racaCor', 
                                                          dadosBenef.racaCor.cdata, 
                                                          1, u'1, 2, 3, 4, 5, 6')
                    
                    if 'estCiv' in dir(dadosBenef):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosBenef.estCiv', 
                                                          dadosBenef.estCiv.cdata, 
                                                          0, u'1, 2, 3, 4, 5')
                    
                    if 'incFisMen' in dir(dadosBenef):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosBenef.incFisMen', 
                                                          dadosBenef.incFisMen.cdata, 
                                                          1, u'S, N')
                    
                    if 'dtIncFisMen' in dir(dadosBenef):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosBenef.dtIncFisMen', 
                                                          dadosBenef.dtIncFisMen.cdata, 
                                                          0, u'None')
                    
                    if 'dadosNasc' in dir(dadosBenef.dadosNasc):
                        for dadosNasc in dadosBenef.dadosNasc:
                            
                            if 'paisNac' in dir(dadosNasc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosNasc.paisNac', 
                                                                  dadosNasc.paisNac.cdata, 
                                                                  1, u'008, 009, 013, 015, 017, 020, 023, 025, 031, 037, 040, 041, 042, 043, 047, 053, 059, 063, 064, 065, 069, 072, 073, 077, 080, 081, 083, 085, 087, 088, 090, 093, 097, 098, 099, 100, 101, 102, 105, 106, 108, 111, 115, 119, 127, 131, 137, 141, 145, 149, 150, 151, 152, 153, 154, 158, 160, 161, 163, 165, 169, 173, 177, 183, 187, 190, 193, 195, 196, 198, 199, 200, 229, 232, 235, 237, 239, 240, 243, 244, 245, 246, 247, 249, 251, 253, 255, 259, 263, 267, 271, 275, 281, 285, 289, 291, 292, 293, 297, 301, 305, 309, 313, 317, 321, 325, 329, 331, 334, 337, 341, 343, 345, 351, 355, 357, 358, 359, 361, 365, 367, 369, 372, 375, 379, 383, 386, 388, 391, 393, 395, 396, 399, 403, 411, 420, 423, 426, 427, 431, 434, 438, 440, 442, 445, 447, 449, 450, 452, 455, 458, 461, 464, 467, 472, 474, 476, 477, 485, 488, 489, 490, 493, 494, 495, 497, 498, 499, 501, 505, 507, 508, 511, 517, 521, 525, 528, 531, 535, 538, 542, 545, 548, 551, 556, 563, 566, 569, 573, 575, 576, 578, 580, 583, 586, 589, 593, 599, 603, 607, 611, 623, 625, 628, 640, 647, 660, 665, 670, 675, 676, 677, 678, 685, 687, 690, 691, 693, 695, 697, 698, 699, 700, 705, 710, 715, 720, 728, 731, 735, 737, 738, 741, 744, 748, 750, 754, 755, 756, 759, 760, 764, 767, 770, 772, 776, 780, 781, 782, 783, 785, 788, 790, 791, 795, 800, 805, 810, 815, 820, 823, 824, 827, 828, 831, 833, 840, 845, 847, 848, 850, 855, 858, 863, 866, 870, 873, 875, 888, 890, 895')
                            
                            if 'nmMae' in dir(dadosNasc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosNasc.nmMae', 
                                                                  dadosNasc.nmMae.cdata, 
                                                                  0, u'None')
                            
                            if 'nmPai' in dir(dadosNasc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosNasc.nmPai', 
                                                                  dadosNasc.nmPai.cdata, 
                                                                  0, u'None')
                    
                    if 'endereco' in dir(dadosBenef.endereco):
                        for endereco in dadosBenef.endereco:
                            
                            if 'brasil' in dir(endereco.brasil):
                                for brasil in endereco.brasil:
                                    
                                    if 'tpLograd' in dir(brasil):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'brasil.tpLograd', 
                                                                          brasil.tpLograd.cdata, 
                                                                          1, u'A, AC, ACA, ACL, AD, AE, AER, AL, AMD, AME, AN, ANT, ART, AT, ATL, A V, AV, AVC, AVM, AVV, BAL, BC, BCO, BEL, BL, BLO, BLS, BLV, BSQ, BVD, BX, C, CAL, CAM, CAN, CH, CHA, CIC, CIR, CJ, CJM, CMP, COL, COM, CON, COND, COR, CPO, CRG, CTN, DSC, DSV, DT, EB, EIM, ENS, ENT, EQ, ESC, ESD, ESE, ESI, ESL, ESM, ESP, ESS, EST, ESV, ETA, ETC, ETD, ETN, ETP, ETT, EVA, EVD, EX, FAV, FAZ, FER, FNT, FRA, FTE, GAL, GJA, HAB, IA, IND, IOA, JD, JDE, LD, LGA, LGO, LOT, LRG, LT, MER, MNA, MOD, MRG, MRO, MTE, NUC, NUR, O, OUT, PAR, PAS, PAT, PC, PCE, PDA, PDO, PNT, PR, PRL, PRM, PRQ, PRR, PSA, PSG, PSP, PSS, PTE, PTO, Q, QTA, QTS, R, R I, R L, R P, R V, RAM, RCR, REC, RER, RES, RET, RLA, RMP, ROA, ROD, ROT, RPE, RPR, RTN, RTT, SEG, SIT, SRV, ST, SUB, TCH, TER, TR, TRV, TUN, TV, TVP, TVV, UNI, V, V C, V L, VAC, VAL, VCO, VD, V-E, VER, VEV, VL, VLA, VLE, VLT, VPE, VRT, ZIG')
                                    
                                    if 'dscLograd' in dir(brasil):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'brasil.dscLograd', 
                                                                          brasil.dscLograd.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nrLograd' in dir(brasil):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'brasil.nrLograd', 
                                                                          brasil.nrLograd.cdata, 
                                                                          1, u'None')
                                    
                                    if 'complemento' in dir(brasil):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'brasil.complemento', 
                                                                          brasil.complemento.cdata, 
                                                                          0, u'None')
                                    
                                    if 'bairro' in dir(brasil):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'brasil.bairro', 
                                                                          brasil.bairro.cdata, 
                                                                          0, u'None')
                                    
                                    if 'cep' in dir(brasil):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'brasil.cep', 
                                                                          brasil.cep.cdata, 
                                                                          1, u'None')
                                    
                                    if 'codMunic' in dir(brasil):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'brasil.codMunic', 
                                                                          brasil.codMunic.cdata, 
                                                                          1, u'None')
                                    
                                    if 'uf' in dir(brasil):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'brasil.uf', 
                                                                          brasil.uf.cdata, 
                                                                          1, u'None')
                            
                            if 'exterior' in dir(endereco.exterior):
                                for exterior in endereco.exterior:
                                    
                                    if 'paisResid' in dir(exterior):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'exterior.paisResid', 
                                                                          exterior.paisResid.cdata, 
                                                                          1, u'008, 009, 013, 015, 017, 020, 023, 025, 031, 037, 040, 041, 042, 043, 047, 053, 059, 063, 064, 065, 069, 072, 073, 077, 080, 081, 083, 085, 087, 088, 090, 093, 097, 098, 099, 100, 101, 102, 105, 106, 108, 111, 115, 119, 127, 131, 137, 141, 145, 149, 150, 151, 152, 153, 154, 158, 160, 161, 163, 165, 169, 173, 177, 183, 187, 190, 193, 195, 196, 198, 199, 200, 229, 232, 235, 237, 239, 240, 243, 244, 245, 246, 247, 249, 251, 253, 255, 259, 263, 267, 271, 275, 281, 285, 289, 291, 292, 293, 297, 301, 305, 309, 313, 317, 321, 325, 329, 331, 334, 337, 341, 343, 345, 351, 355, 357, 358, 359, 361, 365, 367, 369, 372, 375, 379, 383, 386, 388, 391, 393, 395, 396, 399, 403, 411, 420, 423, 426, 427, 431, 434, 438, 440, 442, 445, 447, 449, 450, 452, 455, 458, 461, 464, 467, 472, 474, 476, 477, 485, 488, 489, 490, 493, 494, 495, 497, 498, 499, 501, 505, 507, 508, 511, 517, 521, 525, 528, 531, 535, 538, 542, 545, 548, 551, 556, 563, 566, 569, 573, 575, 576, 578, 580, 583, 586, 589, 593, 599, 603, 607, 611, 623, 625, 628, 640, 647, 660, 665, 670, 675, 676, 677, 678, 685, 687, 690, 691, 693, 695, 697, 698, 699, 700, 705, 710, 715, 720, 728, 731, 735, 737, 738, 741, 744, 748, 750, 754, 755, 756, 759, 760, 764, 767, 770, 772, 776, 780, 781, 782, 783, 785, 788, 790, 791, 795, 800, 805, 810, 815, 820, 823, 824, 827, 828, 831, 833, 840, 845, 847, 848, 850, 855, 858, 863, 866, 870, 873, 875, 888, 890, 895')
                                    
                                    if 'dscLograd' in dir(exterior):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'exterior.dscLograd', 
                                                                          exterior.dscLograd.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nrLograd' in dir(exterior):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'exterior.nrLograd', 
                                                                          exterior.nrLograd.cdata, 
                                                                          1, u'None')
                                    
                                    if 'complemento' in dir(exterior):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'exterior.complemento', 
                                                                          exterior.complemento.cdata, 
                                                                          0, u'None')
                                    
                                    if 'bairro' in dir(exterior):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'exterior.bairro', 
                                                                          exterior.bairro.cdata, 
                                                                          0, u'None')
                                    
                                    if 'nmCid' in dir(exterior):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'exterior.nmCid', 
                                                                          exterior.nmCid.cdata, 
                                                                          1, u'None')
                                    
                                    if 'codPostal' in dir(exterior):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'exterior.codPostal', 
                                                                          exterior.codPostal.cdata, 
                                                                          0, u'None')
                    
                    if 'dependente' in dir(dadosBenef.dependente):
                        for dependente in dadosBenef.dependente:
                            
                            if 'tpDep' in dir(dependente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dependente.tpDep', 
                                                                  dependente.tpDep.cdata, 
                                                                  1, u'01, 02, 03, 04, 06, 07, 09, 10, 11, 12, 99')
                            
                            if 'nmDep' in dir(dependente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dependente.nmDep', 
                                                                  dependente.nmDep.cdata, 
                                                                  1, u'None')
                            
                            if 'dtNascto' in dir(dependente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dependente.dtNascto', 
                                                                  dependente.dtNascto.cdata, 
                                                                  1, u'None')
                            
                            if 'cpfDep' in dir(dependente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dependente.cpfDep', 
                                                                  dependente.cpfDep.cdata, 
                                                                  0, u'None')
                            
                            if 'sexoDep' in dir(dependente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dependente.sexoDep', 
                                                                  dependente.sexoDep.cdata, 
                                                                  1, u'M, F')
                            
                            if 'depIRRF' in dir(dependente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dependente.depIRRF', 
                                                                  dependente.depIRRF.cdata, 
                                                                  1, u'S, N')
                            
                            if 'incFisMen' in dir(dependente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dependente.incFisMen', 
                                                                  dependente.incFisMen.cdata, 
                                                                  1, u'S, N')
                            
                            if 'depFinsPrev' in dir(dependente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dependente.depFinsPrev', 
                                                                  dependente.depFinsPrev.cdata, 
                                                                  1, u'S, N')
    return validacoes_lista