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


def validacoes_r2070_evtpgtosdivs(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtPgtosDivs = doc.Reinf.evtPgtosDivs
    #variaveis

    if 'ideEvento' in dir(evtPgtosDivs.ideEvento):
        for ideEvento in evtPgtosDivs.ideEvento:

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

    if 'ideContri' in dir(evtPgtosDivs.ideContri):
        for ideContri in evtPgtosDivs.ideContri:

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

    if 'ideBenef' in dir(evtPgtosDivs.ideBenef):
        for ideBenef in evtPgtosDivs.ideBenef:

            if 'codPgto' in dir(ideBenef):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideBenef.codPgto',
                                                  ideBenef.codPgto.cdata,
                                                  1, u'0916, 0924, 1708, 3208, 3223, 3426, 3533, 3540, 3556, 3579, 3277, 3280, 3746, 3770, 4085, 4397, 4407, 4409, 5204, 5217, 5232, 5273, 5557, 5565, 5706, 5944, 5952, 5960, 5979, 5987, 6147, 6175, 6190, 6228, 6230, 6243, 6256, 6800, 6813, 6904, 8045, 8053, 8468, 8673, 8739, 8767, 8850, 8863, 9060, 9385, 1889, 0422, 0473, 0481, 0490, 0610, 5192, 5286, 9412, 9427, 9453, 9478, 9466')

            if 'tpInscBenef' in dir(ideBenef):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideBenef.tpInscBenef',
                                                  ideBenef.tpInscBenef.cdata,
                                                  0, u'1, 2')

            if 'nrInscBenef' in dir(ideBenef):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideBenef.nrInscBenef',
                                                  ideBenef.nrInscBenef.cdata,
                                                  0, u'None')

            if 'nmRazaoBenef' in dir(ideBenef):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideBenef.nmRazaoBenef',
                                                  ideBenef.nmRazaoBenef.cdata,
                                                  1, u'None')

            if 'infoResidExt' in dir(ideBenef.infoResidExt):
                for infoResidExt in ideBenef.infoResidExt:

                    if 'infoEnder' in dir(infoResidExt.infoEnder):
                        for infoEnder in infoResidExt.infoEnder:
        
                            if 'paisResid' in dir(infoEnder):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEnder.paisResid',
                                                                  infoEnder.paisResid.cdata,
                                                                  1, u'008, 009, 013, 015, 017, 020, 023, 025, 031, 037, 040, 041, 042, 043, 047, 053, 059, 063, 064, 065, 069, 072, 073, 077, 080, 081, 083, 085, 087, 088, 090, 093, 097, 098, 099, 100, 101, 102, 105, 106, 108, 111, 115, 119, 127, 131, 137, 141, 145, 149, 150, 151, 152, 153, 154, 158, 160, 161, 163, 165, 169, 173, 177, 183, 187, 190, 193, 195, 196, 198, 199, 200, 229, 232, 235, 237, 239, 240, 243, 244, 245, 246, 247, 249, 251, 253, 255, 259, 263, 267, 271, 275, 281, 285, 289, 291, 292, 293, 297, 301, 305, 309, 313, 317, 321, 325, 329, 331, 334, 337, 341, 343, 345, 351, 355, 357, 358, 359, 361, 365, 367, 369, 372, 375, 379, 383, 386, 388, 391, 393, 395, 396, 399, 403, 411, 420, 423, 426, 427, 431, 434, 438, 440, 442, 445, 447, 449, 450, 452, 455, 458, 461, 464, 467, 472, 474, 476, 477, 485, 488, 489, 490, 493, 494, 495, 497, 498, 499, 501, 505, 507, 508, 511, 517, 521, 525, 528, 531, 535, 538, 542, 545, 548, 551, 556, 563, 566, 569, 573, 575, 576, 578, 580, 583, 586, 589, 593, 599, 603, 607, 611, 623, 625, 628, 640, 647, 660, 665, 670, 675, 676, 677, 678, 685, 687, 690, 691, 693, 695, 697, 698, 699, 700, 705, 710, 715, 720, 728, 731, 735, 737, 738, 741, 744, 748, 750, 754, 755, 756, 759, 760, 764, 767, 770, 772, 776, 780, 781, 782, 783, 785, 788, 790, 791, 795, 800, 805, 810, 815, 820, 823, 824, 827, 828, 831, 833, 840, 845, 847, 848, 850, 855, 858, 863, 866, 870, 873, 875, 888, 890, 895')
        
                            if 'dscLograd' in dir(infoEnder):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEnder.dscLograd',
                                                                  infoEnder.dscLograd.cdata,
                                                                  1, u'None')
        
                            if 'nrLograd' in dir(infoEnder):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEnder.nrLograd',
                                                                  infoEnder.nrLograd.cdata,
                                                                  0, u'None')
        
                            if 'complem' in dir(infoEnder):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEnder.complem',
                                                                  infoEnder.complem.cdata,
                                                                  0, u'None')
        
                            if 'bairro' in dir(infoEnder):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEnder.bairro',
                                                                  infoEnder.bairro.cdata,
                                                                  0, u'None')
        
                            if 'cidade' in dir(infoEnder):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEnder.cidade',
                                                                  infoEnder.cidade.cdata,
                                                                  0, u'None')
        
                            if 'codPostal' in dir(infoEnder):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEnder.codPostal',
                                                                  infoEnder.codPostal.cdata,
                                                                  0, u'None')

                    if 'infoFiscal' in dir(infoResidExt.infoFiscal):
                        for infoFiscal in infoResidExt.infoFiscal:
        
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
        
                            if 'relFontePagad' in dir(infoFiscal):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoFiscal.relFontePagad',
                                                                  infoFiscal.relFontePagad.cdata,
                                                                  0, u'500, 510, 520, 530, 540, 550, 560, 570, 900')

            if 'infoMolestia' in dir(ideBenef.infoMolestia):
                for infoMolestia in ideBenef.infoMolestia:

                    if 'dtLaudo' in dir(infoMolestia):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoMolestia.dtLaudo',
                                                          infoMolestia.dtLaudo.cdata,
                                                          1, u'None')

            if 'infoPgto' in dir(ideBenef.infoPgto):
                for infoPgto in ideBenef.infoPgto:

                    if 'ideEstab' in dir(infoPgto.ideEstab):
                        for ideEstab in infoPgto.ideEstab:
        
                            if 'tpInsc' in dir(ideEstab):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideEstab.tpInsc',
                                                                  ideEstab.tpInsc.cdata,
                                                                  1, u'1, 2, 4')
        
                            if 'nrInsc' in dir(ideEstab):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideEstab.nrInsc',
                                                                  ideEstab.nrInsc.cdata,
                                                                  1, u'None')
        
                            if 'pgtoResidBR' in dir(ideEstab.pgtoResidBR):
                                for pgtoResidBR in ideEstab.pgtoResidBR:
                
                                    if 'pgtoPF' in dir(pgtoResidBR.pgtoPF):
                                        for pgtoPF in pgtoResidBR.pgtoPF:
                        
                                            if 'dtPgto' in dir(pgtoPF):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'pgtoPF.dtPgto',
                                                                                  pgtoPF.dtPgto.cdata,
                                                                                  1, u'None')
                        
                                            if 'indSuspExig' in dir(pgtoPF):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'pgtoPF.indSuspExig',
                                                                                  pgtoPF.indSuspExig.cdata,
                                                                                  1, u'S, N')
                        
                                            if 'indDecTerceiro' in dir(pgtoPF):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'pgtoPF.indDecTerceiro',
                                                                                  pgtoPF.indDecTerceiro.cdata,
                                                                                  1, u'S, N')
                        
                                            if 'vlrRendTributavel' in dir(pgtoPF):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'pgtoPF.vlrRendTributavel',
                                                                                  pgtoPF.vlrRendTributavel.cdata,
                                                                                  1, u'None')
                        
                                            if 'vlrIRRF' in dir(pgtoPF):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'pgtoPF.vlrIRRF',
                                                                                  pgtoPF.vlrIRRF.cdata,
                                                                                  1, u'None')
                        
                                            if 'detDeducao' in dir(pgtoPF.detDeducao):
                                                for detDeducao in pgtoPF.detDeducao:
                                
                                                    if 'indTpDeducao' in dir(detDeducao):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'detDeducao.indTpDeducao',
                                                                                          detDeducao.indTpDeducao.cdata,
                                                                                          1, u'1, 2, 3, 4, 5, 6')
                                
                                                    if 'vlrDeducao' in dir(detDeducao):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'detDeducao.vlrDeducao',
                                                                                          detDeducao.vlrDeducao.cdata,
                                                                                          1, u'None')
                        
                                            if 'rendIsento' in dir(pgtoPF.rendIsento):
                                                for rendIsento in pgtoPF.rendIsento:
                                
                                                    if 'tpIsencao' in dir(rendIsento):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'rendIsento.tpIsencao',
                                                                                          rendIsento.tpIsencao.cdata,
                                                                                          1, u'1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11')
                                
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
                        
                                            if 'detCompet' in dir(pgtoPF.detCompet):
                                                for detCompet in pgtoPF.detCompet:
                                
                                                    if 'indPerReferencia' in dir(detCompet):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'detCompet.indPerReferencia',
                                                                                          detCompet.indPerReferencia.cdata,
                                                                                          1, u'1, 2')
                                
                                                    if 'perRefPagto' in dir(detCompet):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'detCompet.perRefPagto',
                                                                                          detCompet.perRefPagto.cdata,
                                                                                          1, u'None')
                                
                                                    if 'vlrRendTributavel' in dir(detCompet):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'detCompet.vlrRendTributavel',
                                                                                          detCompet.vlrRendTributavel.cdata,
                                                                                          1, u'None')
                        
                                            if 'compJud' in dir(pgtoPF.compJud):
                                                for compJud in pgtoPF.compJud:
                                
                                                    if 'vlrCompAnoCalend' in dir(compJud):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'compJud.vlrCompAnoCalend',
                                                                                          compJud.vlrCompAnoCalend.cdata,
                                                                                          0, u'None')
                                
                                                    if 'vlrCompAnoAnt' in dir(compJud):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'compJud.vlrCompAnoAnt',
                                                                                          compJud.vlrCompAnoAnt.cdata,
                                                                                          0, u'None')
                        
                                            if 'infoRRA' in dir(pgtoPF.infoRRA):
                                                for infoRRA in pgtoPF.infoRRA:
                                
                                                    if 'tpProcRRA' in dir(infoRRA):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'infoRRA.tpProcRRA',
                                                                                          infoRRA.tpProcRRA.cdata,
                                                                                          0, u'1, 2')
                                
                                                    if 'nrProcRRA' in dir(infoRRA):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'infoRRA.nrProcRRA',
                                                                                          infoRRA.nrProcRRA.cdata,
                                                                                          0, u'None')
                                
                                                    if 'codSusp' in dir(infoRRA):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'infoRRA.codSusp',
                                                                                          infoRRA.codSusp.cdata,
                                                                                          0, u'None')
                                
                                                    if 'natRRA' in dir(infoRRA):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'infoRRA.natRRA',
                                                                                          infoRRA.natRRA.cdata,
                                                                                          0, u'None')
                                
                                                    if 'qtdMesesRRA' in dir(infoRRA):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'infoRRA.qtdMesesRRA',
                                                                                          infoRRA.qtdMesesRRA.cdata,
                                                                                          0, u'None')
                                
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
                                        
                                                            if 'ideAdvogado' in dir(despProcJud.ideAdvogado):
                                                                for ideAdvogado in despProcJud.ideAdvogado:
                                                
                                                                    if 'tpInscAdvogado' in dir(ideAdvogado):
                                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                                          'ideAdvogado.tpInscAdvogado',
                                                                                                          ideAdvogado.tpInscAdvogado.cdata,
                                                                                                          1, u'1, 2')
                                                
                                                                    if 'nrInscAdvogado' in dir(ideAdvogado):
                                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                                          'ideAdvogado.nrInscAdvogado',
                                                                                                          ideAdvogado.nrInscAdvogado.cdata,
                                                                                                          1, u'None')
                                                
                                                                    if 'vlrAdvogado' in dir(ideAdvogado):
                                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                                          'ideAdvogado.vlrAdvogado',
                                                                                                          ideAdvogado.vlrAdvogado.cdata,
                                                                                                          1, u'None')
                        
                                            if 'infoProcJud' in dir(pgtoPF.infoProcJud):
                                                for infoProcJud in pgtoPF.infoProcJud:
                                
                                                    if 'nrProcJud' in dir(infoProcJud):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'infoProcJud.nrProcJud',
                                                                                          infoProcJud.nrProcJud.cdata,
                                                                                          1, u'None')
                                
                                                    if 'codSusp' in dir(infoProcJud):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'infoProcJud.codSusp',
                                                                                          infoProcJud.codSusp.cdata,
                                                                                          0, u'None')
                                
                                                    if 'indOrigemRecursos' in dir(infoProcJud):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'infoProcJud.indOrigemRecursos',
                                                                                          infoProcJud.indOrigemRecursos.cdata,
                                                                                          1, u'1, 2')
                                
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
                                        
                                                            if 'ideAdvogado' in dir(despProcJud.ideAdvogado):
                                                                for ideAdvogado in despProcJud.ideAdvogado:
                                                
                                                                    if 'tpInscAdvogado' in dir(ideAdvogado):
                                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                                          'ideAdvogado.tpInscAdvogado',
                                                                                                          ideAdvogado.tpInscAdvogado.cdata,
                                                                                                          1, u'1, 2')
                                                
                                                                    if 'nrInscAdvogado' in dir(ideAdvogado):
                                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                                          'ideAdvogado.nrInscAdvogado',
                                                                                                          ideAdvogado.nrInscAdvogado.cdata,
                                                                                                          1, u'None')
                                                
                                                                    if 'vlrAdvogado' in dir(ideAdvogado):
                                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                                          'ideAdvogado.vlrAdvogado',
                                                                                                          ideAdvogado.vlrAdvogado.cdata,
                                                                                                          1, u'None')
                                
                                                    if 'origemRecursos' in dir(infoProcJud.origemRecursos):
                                                        for origemRecursos in infoProcJud.origemRecursos:
                                        
                                                            if 'cnpjOrigemRecursos' in dir(origemRecursos):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'origemRecursos.cnpjOrigemRecursos',
                                                                                                  origemRecursos.cnpjOrigemRecursos.cdata,
                                                                                                  1, u'None')
                        
                                            if 'depJudicial' in dir(pgtoPF.depJudicial):
                                                for depJudicial in pgtoPF.depJudicial:
                                
                                                    if 'vlrDepJudicial' in dir(depJudicial):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'depJudicial.vlrDepJudicial',
                                                                                          depJudicial.vlrDepJudicial.cdata,
                                                                                          0, u'None')
                
                                    if 'pgtoPJ' in dir(pgtoResidBR.pgtoPJ):
                                        for pgtoPJ in pgtoResidBR.pgtoPJ:
                        
                                            if 'dtPagto' in dir(pgtoPJ):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'pgtoPJ.dtPagto',
                                                                                  pgtoPJ.dtPagto.cdata,
                                                                                  1, u'None')
                        
                                            if 'vlrRendTributavel' in dir(pgtoPJ):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'pgtoPJ.vlrRendTributavel',
                                                                                  pgtoPJ.vlrRendTributavel.cdata,
                                                                                  1, u'None')
                        
                                            if 'vlrRet' in dir(pgtoPJ):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'pgtoPJ.vlrRet',
                                                                                  pgtoPJ.vlrRet.cdata,
                                                                                  1, u'None')
                        
                                            if 'infoProcJud' in dir(pgtoPJ.infoProcJud):
                                                for infoProcJud in pgtoPJ.infoProcJud:
                                
                                                    if 'nrProcJud' in dir(infoProcJud):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'infoProcJud.nrProcJud',
                                                                                          infoProcJud.nrProcJud.cdata,
                                                                                          1, u'None')
                                
                                                    if 'codSusp' in dir(infoProcJud):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'infoProcJud.codSusp',
                                                                                          infoProcJud.codSusp.cdata,
                                                                                          0, u'None')
                                
                                                    if 'indOrigemRecursos' in dir(infoProcJud):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'infoProcJud.indOrigemRecursos',
                                                                                          infoProcJud.indOrigemRecursos.cdata,
                                                                                          1, u'1, 2')
                                
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
                                        
                                                            if 'ideAdvogado' in dir(despProcJud.ideAdvogado):
                                                                for ideAdvogado in despProcJud.ideAdvogado:
                                                
                                                                    if 'tpInscAdvogado' in dir(ideAdvogado):
                                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                                          'ideAdvogado.tpInscAdvogado',
                                                                                                          ideAdvogado.tpInscAdvogado.cdata,
                                                                                                          1, u'1, 2')
                                                
                                                                    if 'nrInscAdvogado' in dir(ideAdvogado):
                                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                                          'ideAdvogado.nrInscAdvogado',
                                                                                                          ideAdvogado.nrInscAdvogado.cdata,
                                                                                                          1, u'None')
                                                
                                                                    if 'vlrAdvogado' in dir(ideAdvogado):
                                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                                          'ideAdvogado.vlrAdvogado',
                                                                                                          ideAdvogado.vlrAdvogado.cdata,
                                                                                                          1, u'None')
                                
                                                    if 'origemRecursos' in dir(infoProcJud.origemRecursos):
                                                        for origemRecursos in infoProcJud.origemRecursos:
                                        
                                                            if 'cnpjOrigemRecursos' in dir(origemRecursos):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'origemRecursos.cnpjOrigemRecursos',
                                                                                                  origemRecursos.cnpjOrigemRecursos.cdata,
                                                                                                  1, u'None')
        
                            if 'pgtoResidExt' in dir(ideEstab.pgtoResidExt):
                                for pgtoResidExt in ideEstab.pgtoResidExt:
                
                                    if 'dtPagto' in dir(pgtoResidExt):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'pgtoResidExt.dtPagto',
                                                                          pgtoResidExt.dtPagto.cdata,
                                                                          1, u'None')
                
                                    if 'tpRendimento' in dir(pgtoResidExt):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'pgtoResidExt.tpRendimento',
                                                                          pgtoResidExt.tpRendimento.cdata,
                                                                          1, u'500, 510, 520, 530, 540, 550, 560, 570, 900')
                
                                    if 'formaTributacao' in dir(pgtoResidExt):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'pgtoResidExt.formaTributacao',
                                                                          pgtoResidExt.formaTributacao.cdata,
                                                                          1, u'10, 11, 12, 13, 30, 40, 41, 42, 43, 44, 50')
                
                                    if 'vlrPgto' in dir(pgtoResidExt):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'pgtoResidExt.vlrPgto',
                                                                          pgtoResidExt.vlrPgto.cdata,
                                                                          1, u'None')
                
                                    if 'vlrRet' in dir(pgtoResidExt):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'pgtoResidExt.vlrRet',
                                                                          pgtoResidExt.vlrRet.cdata,
                                                                          1, u'None')
    return validacoes_lista