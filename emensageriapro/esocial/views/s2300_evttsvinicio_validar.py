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


def validacoes_s2300_evttsvinicio(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTSVInicio = doc.eSocial.evtTSVInicio
    #variaveis
    
    if 'ideEvento' in dir(evtTSVInicio.ideEvento):
        for ideEvento in evtTSVInicio.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtTSVInicio.ideEmpregador):
        for ideEmpregador in evtTSVInicio.ideEmpregador:
            
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
    
    if 'trabalhador' in dir(evtTSVInicio.trabalhador):
        for trabalhador in evtTSVInicio.trabalhador:
            
            if 'cpfTrab' in dir(trabalhador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'trabalhador.cpfTrab', 
                                                  trabalhador.cpfTrab.cdata, 
                                                  1, u'None')
            
            if 'nisTrab' in dir(trabalhador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'trabalhador.nisTrab', 
                                                  trabalhador.nisTrab.cdata, 
                                                  0, u'None')
            
            if 'nmTrab' in dir(trabalhador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'trabalhador.nmTrab', 
                                                  trabalhador.nmTrab.cdata, 
                                                  1, u'None')
            
            if 'sexo' in dir(trabalhador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'trabalhador.sexo', 
                                                  trabalhador.sexo.cdata, 
                                                  1, u'M, F')
            
            if 'racaCor' in dir(trabalhador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'trabalhador.racaCor', 
                                                  trabalhador.racaCor.cdata, 
                                                  1, u'1, 2, 3, 4, 5, 6')
            
            if 'estCiv' in dir(trabalhador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'trabalhador.estCiv', 
                                                  trabalhador.estCiv.cdata, 
                                                  0, u'1, 2, 3, 4, 5')
            
            if 'grauInstr' in dir(trabalhador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'trabalhador.grauInstr', 
                                                  trabalhador.grauInstr.cdata, 
                                                  1, u'01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12')
            
            if 'nmSoc' in dir(trabalhador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'trabalhador.nmSoc', 
                                                  trabalhador.nmSoc.cdata, 
                                                  0, u'None')
            
            if 'nascimento' in dir(trabalhador.nascimento):
                for nascimento in trabalhador.nascimento:
                    
                    if 'dtNascto' in dir(nascimento):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'nascimento.dtNascto', 
                                                          nascimento.dtNascto.cdata, 
                                                          1, u'None')
                    
                    if 'codMunic' in dir(nascimento):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'nascimento.codMunic', 
                                                          nascimento.codMunic.cdata, 
                                                          0, u'None')
                    
                    if 'uf' in dir(nascimento):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'nascimento.uf', 
                                                          nascimento.uf.cdata, 
                                                          0, u'None')
                    
                    if 'paisNascto' in dir(nascimento):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'nascimento.paisNascto', 
                                                          nascimento.paisNascto.cdata, 
                                                          1, u'008, 009, 013, 015, 017, 020, 023, 025, 031, 037, 040, 041, 042, 043, 047, 053, 059, 063, 064, 065, 069, 072, 073, 077, 080, 081, 083, 085, 087, 088, 090, 093, 097, 098, 099, 100, 101, 102, 105, 106, 108, 111, 115, 119, 127, 131, 137, 141, 145, 149, 150, 151, 152, 153, 154, 158, 160, 161, 163, 165, 169, 173, 177, 183, 187, 190, 193, 195, 196, 198, 199, 200, 229, 232, 235, 237, 239, 240, 243, 244, 245, 246, 247, 249, 251, 253, 255, 259, 263, 267, 271, 275, 281, 285, 289, 291, 292, 293, 297, 301, 305, 309, 313, 317, 321, 325, 329, 331, 334, 337, 341, 343, 345, 351, 355, 357, 358, 359, 361, 365, 367, 369, 372, 375, 379, 383, 386, 388, 391, 393, 395, 396, 399, 403, 411, 420, 423, 426, 427, 431, 434, 438, 440, 442, 445, 447, 449, 450, 452, 455, 458, 461, 464, 467, 472, 474, 476, 477, 485, 488, 489, 490, 493, 494, 495, 497, 498, 499, 501, 505, 507, 508, 511, 517, 521, 525, 528, 531, 535, 538, 542, 545, 548, 551, 556, 563, 566, 569, 573, 575, 576, 578, 580, 583, 586, 589, 593, 599, 603, 607, 611, 623, 625, 628, 640, 647, 660, 665, 670, 675, 676, 677, 678, 685, 687, 690, 691, 693, 695, 697, 698, 699, 700, 705, 710, 715, 720, 728, 731, 735, 737, 738, 741, 744, 748, 750, 754, 755, 756, 759, 760, 764, 767, 770, 772, 776, 780, 781, 782, 783, 785, 788, 790, 791, 795, 800, 805, 810, 815, 820, 823, 824, 827, 828, 831, 833, 840, 845, 847, 848, 850, 855, 858, 863, 866, 870, 873, 875, 888, 890, 895')
                    
                    if 'paisNac' in dir(nascimento):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'nascimento.paisNac', 
                                                          nascimento.paisNac.cdata, 
                                                          1, u'008, 009, 013, 015, 017, 020, 023, 025, 031, 037, 040, 041, 042, 043, 047, 053, 059, 063, 064, 065, 069, 072, 073, 077, 080, 081, 083, 085, 087, 088, 090, 093, 097, 098, 099, 100, 101, 102, 105, 106, 108, 111, 115, 119, 127, 131, 137, 141, 145, 149, 150, 151, 152, 153, 154, 158, 160, 161, 163, 165, 169, 173, 177, 183, 187, 190, 193, 195, 196, 198, 199, 200, 229, 232, 235, 237, 239, 240, 243, 244, 245, 246, 247, 249, 251, 253, 255, 259, 263, 267, 271, 275, 281, 285, 289, 291, 292, 293, 297, 301, 305, 309, 313, 317, 321, 325, 329, 331, 334, 337, 341, 343, 345, 351, 355, 357, 358, 359, 361, 365, 367, 369, 372, 375, 379, 383, 386, 388, 391, 393, 395, 396, 399, 403, 411, 420, 423, 426, 427, 431, 434, 438, 440, 442, 445, 447, 449, 450, 452, 455, 458, 461, 464, 467, 472, 474, 476, 477, 485, 488, 489, 490, 493, 494, 495, 497, 498, 499, 501, 505, 507, 508, 511, 517, 521, 525, 528, 531, 535, 538, 542, 545, 548, 551, 556, 563, 566, 569, 573, 575, 576, 578, 580, 583, 586, 589, 593, 599, 603, 607, 611, 623, 625, 628, 640, 647, 660, 665, 670, 675, 676, 677, 678, 685, 687, 690, 691, 693, 695, 697, 698, 699, 700, 705, 710, 715, 720, 728, 731, 735, 737, 738, 741, 744, 748, 750, 754, 755, 756, 759, 760, 764, 767, 770, 772, 776, 780, 781, 782, 783, 785, 788, 790, 791, 795, 800, 805, 810, 815, 820, 823, 824, 827, 828, 831, 833, 840, 845, 847, 848, 850, 855, 858, 863, 866, 870, 873, 875, 888, 890, 895')
                    
                    if 'nmMae' in dir(nascimento):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'nascimento.nmMae', 
                                                          nascimento.nmMae.cdata, 
                                                          0, u'None')
                    
                    if 'nmPai' in dir(nascimento):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'nascimento.nmPai', 
                                                          nascimento.nmPai.cdata, 
                                                          0, u'None')
            
            if 'documentos' in dir(trabalhador.documentos):
                for documentos in trabalhador.documentos:
                    
                    if 'CTPS' in dir(documentos.CTPS):
                        for CTPS in documentos.CTPS:
                            
                            if 'nrCtps' in dir(CTPS):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'CTPS.nrCtps', 
                                                                  CTPS.nrCtps.cdata, 
                                                                  1, u'None')
                            
                            if 'serieCtps' in dir(CTPS):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'CTPS.serieCtps', 
                                                                  CTPS.serieCtps.cdata, 
                                                                  1, u'None')
                            
                            if 'ufCtps' in dir(CTPS):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'CTPS.ufCtps', 
                                                                  CTPS.ufCtps.cdata, 
                                                                  1, u'None')
                    
                    if 'RIC' in dir(documentos.RIC):
                        for RIC in documentos.RIC:
                            
                            if 'nrRic' in dir(RIC):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'RIC.nrRic', 
                                                                  RIC.nrRic.cdata, 
                                                                  1, u'None')
                            
                            if 'orgaoEmissor' in dir(RIC):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'RIC.orgaoEmissor', 
                                                                  RIC.orgaoEmissor.cdata, 
                                                                  1, u'None')
                            
                            if 'dtExped' in dir(RIC):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'RIC.dtExped', 
                                                                  RIC.dtExped.cdata, 
                                                                  0, u'None')
                    
                    if 'RG' in dir(documentos.RG):
                        for RG in documentos.RG:
                            
                            if 'nrRg' in dir(RG):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'RG.nrRg', 
                                                                  RG.nrRg.cdata, 
                                                                  1, u'None')
                            
                            if 'orgaoEmissor' in dir(RG):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'RG.orgaoEmissor', 
                                                                  RG.orgaoEmissor.cdata, 
                                                                  1, u'None')
                            
                            if 'dtExped' in dir(RG):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'RG.dtExped', 
                                                                  RG.dtExped.cdata, 
                                                                  0, u'None')
                    
                    if 'RNE' in dir(documentos.RNE):
                        for RNE in documentos.RNE:
                            
                            if 'nrRne' in dir(RNE):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'RNE.nrRne', 
                                                                  RNE.nrRne.cdata, 
                                                                  1, u'None')
                            
                            if 'orgaoEmissor' in dir(RNE):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'RNE.orgaoEmissor', 
                                                                  RNE.orgaoEmissor.cdata, 
                                                                  1, u'None')
                            
                            if 'dtExped' in dir(RNE):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'RNE.dtExped', 
                                                                  RNE.dtExped.cdata, 
                                                                  0, u'None')
                    
                    if 'OC' in dir(documentos.OC):
                        for OC in documentos.OC:
                            
                            if 'nrOc' in dir(OC):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'OC.nrOc', 
                                                                  OC.nrOc.cdata, 
                                                                  1, u'None')
                            
                            if 'orgaoEmissor' in dir(OC):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'OC.orgaoEmissor', 
                                                                  OC.orgaoEmissor.cdata, 
                                                                  1, u'None')
                            
                            if 'dtExped' in dir(OC):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'OC.dtExped', 
                                                                  OC.dtExped.cdata, 
                                                                  0, u'None')
                            
                            if 'dtValid' in dir(OC):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'OC.dtValid', 
                                                                  OC.dtValid.cdata, 
                                                                  0, u'None')
                    
                    if 'CNH' in dir(documentos.CNH):
                        for CNH in documentos.CNH:
                            
                            if 'nrRegCnh' in dir(CNH):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'CNH.nrRegCnh', 
                                                                  CNH.nrRegCnh.cdata, 
                                                                  1, u'None')
                            
                            if 'dtExped' in dir(CNH):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'CNH.dtExped', 
                                                                  CNH.dtExped.cdata, 
                                                                  0, u'None')
                            
                            if 'ufCnh' in dir(CNH):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'CNH.ufCnh', 
                                                                  CNH.ufCnh.cdata, 
                                                                  1, u'None')
                            
                            if 'dtValid' in dir(CNH):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'CNH.dtValid', 
                                                                  CNH.dtValid.cdata, 
                                                                  1, u'None')
                            
                            if 'dtPriHab' in dir(CNH):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'CNH.dtPriHab', 
                                                                  CNH.dtPriHab.cdata, 
                                                                  0, u'None')
                            
                            if 'categoriaCnh' in dir(CNH):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'CNH.categoriaCnh', 
                                                                  CNH.categoriaCnh.cdata, 
                                                                  1, u'A, B, C, D, E, AB, AC, AD, AE')
            
            if 'endereco' in dir(trabalhador.endereco):
                for endereco in trabalhador.endereco:
                    
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
            
            if 'trabEstrangeiro' in dir(trabalhador.trabEstrangeiro):
                for trabEstrangeiro in trabalhador.trabEstrangeiro:
                    
                    if 'dtChegada' in dir(trabEstrangeiro):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'trabEstrangeiro.dtChegada', 
                                                          trabEstrangeiro.dtChegada.cdata, 
                                                          0, u'None')
                    
                    if 'classTrabEstrang' in dir(trabEstrangeiro):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'trabEstrangeiro.classTrabEstrang', 
                                                          trabEstrangeiro.classTrabEstrang.cdata, 
                                                          1, u'1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12')
                    
                    if 'casadoBr' in dir(trabEstrangeiro):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'trabEstrangeiro.casadoBr', 
                                                          trabEstrangeiro.casadoBr.cdata, 
                                                          1, u'S, N')
                    
                    if 'filhosBr' in dir(trabEstrangeiro):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'trabEstrangeiro.filhosBr', 
                                                          trabEstrangeiro.filhosBr.cdata, 
                                                          1, u'S, N')
            
            if 'infoDeficiencia' in dir(trabalhador.infoDeficiencia):
                for infoDeficiencia in trabalhador.infoDeficiencia:
                    
                    if 'defFisica' in dir(infoDeficiencia):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoDeficiencia.defFisica', 
                                                          infoDeficiencia.defFisica.cdata, 
                                                          1, u'S, N')
                    
                    if 'defVisual' in dir(infoDeficiencia):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoDeficiencia.defVisual', 
                                                          infoDeficiencia.defVisual.cdata, 
                                                          1, u'S, N')
                    
                    if 'defAuditiva' in dir(infoDeficiencia):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoDeficiencia.defAuditiva', 
                                                          infoDeficiencia.defAuditiva.cdata, 
                                                          1, u'S, N')
                    
                    if 'defMental' in dir(infoDeficiencia):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoDeficiencia.defMental', 
                                                          infoDeficiencia.defMental.cdata, 
                                                          1, u'S, N')
                    
                    if 'defIntelectual' in dir(infoDeficiencia):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoDeficiencia.defIntelectual', 
                                                          infoDeficiencia.defIntelectual.cdata, 
                                                          1, u'S, N')
                    
                    if 'reabReadap' in dir(infoDeficiencia):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoDeficiencia.reabReadap', 
                                                          infoDeficiencia.reabReadap.cdata, 
                                                          1, u'S, N')
                    
                    if 'observacao' in dir(infoDeficiencia):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoDeficiencia.observacao', 
                                                          infoDeficiencia.observacao.cdata, 
                                                          0, u'None')
            
            if 'dependente' in dir(trabalhador.dependente):
                for dependente in trabalhador.dependente:
                    
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
                                                          0, u'M, F')
                    
                    if 'depIRRF' in dir(dependente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dependente.depIRRF', 
                                                          dependente.depIRRF.cdata, 
                                                          1, u'S, N')
                    
                    if 'depSF' in dir(dependente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dependente.depSF', 
                                                          dependente.depSF.cdata, 
                                                          1, u'S, N')
                    
                    if 'incTrab' in dir(dependente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dependente.incTrab', 
                                                          dependente.incTrab.cdata, 
                                                          1, u'S, N')
                    
                    if 'depFinsPrev' in dir(dependente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dependente.depFinsPrev', 
                                                          dependente.depFinsPrev.cdata, 
                                                          0, u'S, N')
            
            if 'contato' in dir(trabalhador.contato):
                for contato in trabalhador.contato:
                    
                    if 'fonePrinc' in dir(contato):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'contato.fonePrinc', 
                                                          contato.fonePrinc.cdata, 
                                                          0, u'None')
                    
                    if 'foneAlternat' in dir(contato):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'contato.foneAlternat', 
                                                          contato.foneAlternat.cdata, 
                                                          0, u'None')
                    
                    if 'emailPrinc' in dir(contato):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'contato.emailPrinc', 
                                                          contato.emailPrinc.cdata, 
                                                          0, u'None')
                    
                    if 'emailAlternat' in dir(contato):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'contato.emailAlternat', 
                                                          contato.emailAlternat.cdata, 
                                                          0, u'None')
    
    if 'infoTSVInicio' in dir(evtTSVInicio.infoTSVInicio):
        for infoTSVInicio in evtTSVInicio.infoTSVInicio:
            
            if 'cadIni' in dir(infoTSVInicio):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoTSVInicio.cadIni', 
                                                  infoTSVInicio.cadIni.cdata, 
                                                  1, u'S, N')
            
            if 'codCateg' in dir(infoTSVInicio):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoTSVInicio.codCateg', 
                                                  infoTSVInicio.codCateg.cdata, 
                                                  1, u'101, 102, 103, 104, 105, 106, 111, 201, 202, 301, 302, 303, 305, 306, 307, 308, 309, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 751, 761, 771, 781, 901, 902, 903, 904, 905')
            
            if 'dtInicio' in dir(infoTSVInicio):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoTSVInicio.dtInicio', 
                                                  infoTSVInicio.dtInicio.cdata, 
                                                  1, u'None')
            
            if 'natAtividade' in dir(infoTSVInicio):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoTSVInicio.natAtividade', 
                                                  infoTSVInicio.natAtividade.cdata, 
                                                  0, u'1, 2')
            
            if 'infoComplementares' in dir(infoTSVInicio.infoComplementares):
                for infoComplementares in infoTSVInicio.infoComplementares:
                    
                    if 'cargoFuncao' in dir(infoComplementares.cargoFuncao):
                        for cargoFuncao in infoComplementares.cargoFuncao:
                            
                            if 'codCargo' in dir(cargoFuncao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'cargoFuncao.codCargo', 
                                                                  cargoFuncao.codCargo.cdata, 
                                                                  1, u'None')
                            
                            if 'codFuncao' in dir(cargoFuncao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'cargoFuncao.codFuncao', 
                                                                  cargoFuncao.codFuncao.cdata, 
                                                                  0, u'None')
                    
                    if 'remuneracao' in dir(infoComplementares.remuneracao):
                        for remuneracao in infoComplementares.remuneracao:
                            
                            if 'vrSalFx' in dir(remuneracao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'remuneracao.vrSalFx', 
                                                                  remuneracao.vrSalFx.cdata, 
                                                                  1, u'None')
                            
                            if 'undSalFixo' in dir(remuneracao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'remuneracao.undSalFixo', 
                                                                  remuneracao.undSalFixo.cdata, 
                                                                  1, u'1, 2, 3, 4, 5, 6, 7')
                            
                            if 'dscSalVar' in dir(remuneracao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'remuneracao.dscSalVar', 
                                                                  remuneracao.dscSalVar.cdata, 
                                                                  0, u'None')
                    
                    if 'fgts' in dir(infoComplementares.fgts):
                        for fgts in infoComplementares.fgts:
                            
                            if 'opcFGTS' in dir(fgts):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'fgts.opcFGTS', 
                                                                  fgts.opcFGTS.cdata, 
                                                                  1, u'1, 2')
                            
                            if 'dtOpcFGTS' in dir(fgts):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'fgts.dtOpcFGTS', 
                                                                  fgts.dtOpcFGTS.cdata, 
                                                                  0, u'None')
                    
                    if 'infoDirigenteSindical' in dir(infoComplementares.infoDirigenteSindical):
                        for infoDirigenteSindical in infoComplementares.infoDirigenteSindical:
                            
                            if 'categOrig' in dir(infoDirigenteSindical):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoDirigenteSindical.categOrig', 
                                                                  infoDirigenteSindical.categOrig.cdata, 
                                                                  1, u'None')
                            
                            if 'cnpjOrigem' in dir(infoDirigenteSindical):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoDirigenteSindical.cnpjOrigem', 
                                                                  infoDirigenteSindical.cnpjOrigem.cdata, 
                                                                  0, u'None')
                            
                            if 'dtAdmOrig' in dir(infoDirigenteSindical):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoDirigenteSindical.dtAdmOrig', 
                                                                  infoDirigenteSindical.dtAdmOrig.cdata, 
                                                                  0, u'None')
                            
                            if 'matricOrig' in dir(infoDirigenteSindical):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoDirigenteSindical.matricOrig', 
                                                                  infoDirigenteSindical.matricOrig.cdata, 
                                                                  0, u'None')
                    
                    if 'infoTrabCedido' in dir(infoComplementares.infoTrabCedido):
                        for infoTrabCedido in infoComplementares.infoTrabCedido:
                            
                            if 'categOrig' in dir(infoTrabCedido):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabCedido.categOrig', 
                                                                  infoTrabCedido.categOrig.cdata, 
                                                                  1, u'None')
                            
                            if 'cnpjCednt' in dir(infoTrabCedido):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabCedido.cnpjCednt', 
                                                                  infoTrabCedido.cnpjCednt.cdata, 
                                                                  1, u'None')
                            
                            if 'matricCed' in dir(infoTrabCedido):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabCedido.matricCed', 
                                                                  infoTrabCedido.matricCed.cdata, 
                                                                  1, u'None')
                            
                            if 'dtAdmCed' in dir(infoTrabCedido):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabCedido.dtAdmCed', 
                                                                  infoTrabCedido.dtAdmCed.cdata, 
                                                                  1, u'None')
                            
                            if 'tpRegTrab' in dir(infoTrabCedido):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabCedido.tpRegTrab', 
                                                                  infoTrabCedido.tpRegTrab.cdata, 
                                                                  1, u'1, 2')
                            
                            if 'tpRegPrev' in dir(infoTrabCedido):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabCedido.tpRegPrev', 
                                                                  infoTrabCedido.tpRegPrev.cdata, 
                                                                  1, u'1, 2, 3')
                            
                            if 'infOnus' in dir(infoTrabCedido):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabCedido.infOnus', 
                                                                  infoTrabCedido.infOnus.cdata, 
                                                                  1, u'1, 2, 3')
                            
                            if 'indRemunCargo' in dir(infoTrabCedido):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabCedido.indRemunCargo', 
                                                                  infoTrabCedido.indRemunCargo.cdata, 
                                                                  0, u'None')
                    
                    if 'infoEstagiario' in dir(infoComplementares.infoEstagiario):
                        for infoEstagiario in infoComplementares.infoEstagiario:
                            
                            if 'natEstagio' in dir(infoEstagiario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstagiario.natEstagio', 
                                                                  infoEstagiario.natEstagio.cdata, 
                                                                  1, u'O, N')
                            
                            if 'nivEstagio' in dir(infoEstagiario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstagiario.nivEstagio', 
                                                                  infoEstagiario.nivEstagio.cdata, 
                                                                  1, u'1, 2, 3, 4, 8, 9')
                            
                            if 'areaAtuacao' in dir(infoEstagiario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstagiario.areaAtuacao', 
                                                                  infoEstagiario.areaAtuacao.cdata, 
                                                                  0, u'None')
                            
                            if 'nrApol' in dir(infoEstagiario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstagiario.nrApol', 
                                                                  infoEstagiario.nrApol.cdata, 
                                                                  0, u'None')
                            
                            if 'vlrBolsa' in dir(infoEstagiario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstagiario.vlrBolsa', 
                                                                  infoEstagiario.vlrBolsa.cdata, 
                                                                  0, u'None')
                            
                            if 'dtPrevTerm' in dir(infoEstagiario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstagiario.dtPrevTerm', 
                                                                  infoEstagiario.dtPrevTerm.cdata, 
                                                                  1, u'None')
                            
                            if 'instEnsino' in dir(infoEstagiario.instEnsino):
                                for instEnsino in infoEstagiario.instEnsino:
                                    
                                    if 'cnpjInstEnsino' in dir(instEnsino):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'instEnsino.cnpjInstEnsino', 
                                                                          instEnsino.cnpjInstEnsino.cdata, 
                                                                          0, u'None')
                                    
                                    if 'nmRazao' in dir(instEnsino):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'instEnsino.nmRazao', 
                                                                          instEnsino.nmRazao.cdata, 
                                                                          1, u'None')
                                    
                                    if 'dscLograd' in dir(instEnsino):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'instEnsino.dscLograd', 
                                                                          instEnsino.dscLograd.cdata, 
                                                                          0, u'None')
                                    
                                    if 'nrLograd' in dir(instEnsino):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'instEnsino.nrLograd', 
                                                                          instEnsino.nrLograd.cdata, 
                                                                          0, u'None')
                                    
                                    if 'bairro' in dir(instEnsino):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'instEnsino.bairro', 
                                                                          instEnsino.bairro.cdata, 
                                                                          0, u'None')
                                    
                                    if 'cep' in dir(instEnsino):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'instEnsino.cep', 
                                                                          instEnsino.cep.cdata, 
                                                                          0, u'None')
                                    
                                    if 'codMunic' in dir(instEnsino):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'instEnsino.codMunic', 
                                                                          instEnsino.codMunic.cdata, 
                                                                          0, u'None')
                                    
                                    if 'uf' in dir(instEnsino):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'instEnsino.uf', 
                                                                          instEnsino.uf.cdata, 
                                                                          0, u'None')
                            
                            if 'ageIntegracao' in dir(infoEstagiario.ageIntegracao):
                                for ageIntegracao in infoEstagiario.ageIntegracao:
                                    
                                    if 'cnpjAgntInteg' in dir(ageIntegracao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ageIntegracao.cnpjAgntInteg', 
                                                                          ageIntegracao.cnpjAgntInteg.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nmRazao' in dir(ageIntegracao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ageIntegracao.nmRazao', 
                                                                          ageIntegracao.nmRazao.cdata, 
                                                                          1, u'None')
                                    
                                    if 'dscLograd' in dir(ageIntegracao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ageIntegracao.dscLograd', 
                                                                          ageIntegracao.dscLograd.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nrLograd' in dir(ageIntegracao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ageIntegracao.nrLograd', 
                                                                          ageIntegracao.nrLograd.cdata, 
                                                                          1, u'None')
                                    
                                    if 'bairro' in dir(ageIntegracao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ageIntegracao.bairro', 
                                                                          ageIntegracao.bairro.cdata, 
                                                                          0, u'None')
                                    
                                    if 'cep' in dir(ageIntegracao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ageIntegracao.cep', 
                                                                          ageIntegracao.cep.cdata, 
                                                                          1, u'None')
                                    
                                    if 'codMunic' in dir(ageIntegracao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ageIntegracao.codMunic', 
                                                                          ageIntegracao.codMunic.cdata, 
                                                                          0, u'None')
                                    
                                    if 'uf' in dir(ageIntegracao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ageIntegracao.uf', 
                                                                          ageIntegracao.uf.cdata, 
                                                                          1, u'None')
                            
                            if 'supervisorEstagio' in dir(infoEstagiario.supervisorEstagio):
                                for supervisorEstagio in infoEstagiario.supervisorEstagio:
                                    
                                    if 'cpfSupervisor' in dir(supervisorEstagio):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'supervisorEstagio.cpfSupervisor', 
                                                                          supervisorEstagio.cpfSupervisor.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nmSuperv' in dir(supervisorEstagio):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'supervisorEstagio.nmSuperv', 
                                                                          supervisorEstagio.nmSuperv.cdata, 
                                                                          1, u'None')
            
            if 'mudancaCPF' in dir(infoTSVInicio.mudancaCPF):
                for mudancaCPF in infoTSVInicio.mudancaCPF:
                    
                    if 'cpfAnt' in dir(mudancaCPF):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'mudancaCPF.cpfAnt', 
                                                          mudancaCPF.cpfAnt.cdata, 
                                                          1, u'None')
                    
                    if 'dtAltCPF' in dir(mudancaCPF):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'mudancaCPF.dtAltCPF', 
                                                          mudancaCPF.dtAltCPF.cdata, 
                                                          1, u'None')
                    
                    if 'observacao' in dir(mudancaCPF):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'mudancaCPF.observacao', 
                                                          mudancaCPF.observacao.cdata, 
                                                          0, u'None')
            
            if 'afastamento' in dir(infoTSVInicio.afastamento):
                for afastamento in infoTSVInicio.afastamento:
                    
                    if 'dtIniAfast' in dir(afastamento):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'afastamento.dtIniAfast', 
                                                          afastamento.dtIniAfast.cdata, 
                                                          1, u'None')
                    
                    if 'codMotAfast' in dir(afastamento):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'afastamento.codMotAfast', 
                                                          afastamento.codMotAfast.cdata, 
                                                          1, u'01, 03, 05, 06, 07, 08, 10, 11, 12, 13, 14, 15, 16, 17, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35')
            
            if 'termino' in dir(infoTSVInicio.termino):
                for termino in infoTSVInicio.termino:
                    
                    if 'dtTerm' in dir(termino):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'termino.dtTerm', 
                                                          termino.dtTerm.cdata, 
                                                          1, u'None')
    return validacoes_lista