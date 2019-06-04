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


def validacoes_s5002_evtirrfbenef(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtIrrfBenef = doc.eSocial.evtIrrfBenef
    #variaveis
    
    if 'ideEvento' in dir(evtIrrfBenef.ideEvento):
        for ideEvento in evtIrrfBenef.ideEvento:
            
            if 'nrRecArqBase' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.nrRecArqBase', 
                                                  ideEvento.nrRecArqBase.cdata, 
                                                  1, u'None')
            
            if 'perApur' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.perApur', 
                                                  ideEvento.perApur.cdata, 
                                                  1, u'None')
    
    if 'ideEmpregador' in dir(evtIrrfBenef.ideEmpregador):
        for ideEmpregador in evtIrrfBenef.ideEmpregador:
            
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
    
    if 'ideTrabalhador' in dir(evtIrrfBenef.ideTrabalhador):
        for ideTrabalhador in evtIrrfBenef.ideTrabalhador:
            
            if 'cpfTrab' in dir(ideTrabalhador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideTrabalhador.cpfTrab', 
                                                  ideTrabalhador.cpfTrab.cdata, 
                                                  1, u'None')
    
    if 'infoDep' in dir(evtIrrfBenef.infoDep):
        for infoDep in evtIrrfBenef.infoDep:
            
            if 'vrDedDep' in dir(infoDep):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoDep.vrDedDep', 
                                                  infoDep.vrDedDep.cdata, 
                                                  1, u'None')
    
    if 'infoIrrf' in dir(evtIrrfBenef.infoIrrf):
        for infoIrrf in evtIrrfBenef.infoIrrf:
            
            if 'codCateg' in dir(infoIrrf):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoIrrf.codCateg', 
                                                  infoIrrf.codCateg.cdata, 
                                                  0, u'101, 102, 103, 104, 105, 106, 111, 201, 202, 301, 302, 303, 305, 306, 307, 308, 309, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 751, 761, 771, 781, 901, 902, 903, 904, 905')
            
            if 'indResBr' in dir(infoIrrf):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoIrrf.indResBr', 
                                                  infoIrrf.indResBr.cdata, 
                                                  1, u'S, N')
            
            if 'basesIrrf' in dir(infoIrrf.basesIrrf):
                for basesIrrf in infoIrrf.basesIrrf:
                    
                    if 'tpValor' in dir(basesIrrf):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'basesIrrf.tpValor', 
                                                          basesIrrf.tpValor.cdata, 
                                                          1, u'None')
                    
                    if 'valor' in dir(basesIrrf):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'basesIrrf.valor', 
                                                          basesIrrf.valor.cdata, 
                                                          1, u'None')
            
            if 'irrf' in dir(infoIrrf.irrf):
                for irrf in infoIrrf.irrf:
                    
                    if 'tpCR' in dir(irrf):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'irrf.tpCR', 
                                                          irrf.tpCR.cdata, 
                                                          1, u'None')
                    
                    if 'vrIrrfDesc' in dir(irrf):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'irrf.vrIrrfDesc', 
                                                          irrf.vrIrrfDesc.cdata, 
                                                          1, u'None')
            
            if 'idePgtoExt' in dir(infoIrrf.idePgtoExt):
                for idePgtoExt in infoIrrf.idePgtoExt:
                    
                    if 'idePais' in dir(idePgtoExt.idePais):
                        for idePais in idePgtoExt.idePais:
                            
                            if 'codPais' in dir(idePais):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePais.codPais', 
                                                                  idePais.codPais.cdata, 
                                                                  1, u'008, 009, 013, 015, 017, 020, 023, 025, 031, 037, 040, 041, 042, 043, 047, 053, 059, 063, 064, 065, 069, 072, 073, 077, 080, 081, 083, 085, 087, 088, 090, 093, 097, 098, 099, 100, 101, 102, 105, 106, 108, 111, 115, 119, 127, 131, 137, 141, 145, 149, 150, 151, 152, 153, 154, 158, 160, 161, 163, 165, 169, 173, 177, 183, 187, 190, 193, 195, 196, 198, 199, 200, 229, 232, 235, 237, 239, 240, 243, 244, 245, 246, 247, 249, 251, 253, 255, 259, 263, 267, 271, 275, 281, 285, 289, 291, 292, 293, 297, 301, 305, 309, 313, 317, 321, 325, 329, 331, 334, 337, 341, 343, 345, 351, 355, 357, 358, 359, 361, 365, 367, 369, 372, 375, 379, 383, 386, 388, 391, 393, 395, 396, 399, 403, 411, 420, 423, 426, 427, 431, 434, 438, 440, 442, 445, 447, 449, 450, 452, 455, 458, 461, 464, 467, 472, 474, 476, 477, 485, 488, 489, 490, 493, 494, 495, 497, 498, 499, 501, 505, 507, 508, 511, 517, 521, 525, 528, 531, 535, 538, 542, 545, 548, 551, 556, 563, 566, 569, 573, 575, 576, 578, 580, 583, 586, 589, 593, 599, 603, 607, 611, 623, 625, 628, 640, 647, 660, 665, 670, 675, 676, 677, 678, 685, 687, 690, 691, 693, 695, 697, 698, 699, 700, 705, 710, 715, 720, 728, 731, 735, 737, 738, 741, 744, 748, 750, 754, 755, 756, 759, 760, 764, 767, 770, 772, 776, 780, 781, 782, 783, 785, 788, 790, 791, 795, 800, 805, 810, 815, 820, 823, 824, 827, 828, 831, 833, 840, 845, 847, 848, 850, 855, 858, 863, 866, 870, 873, 875, 888, 890, 895')
                            
                            if 'indNIF' in dir(idePais):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePais.indNIF', 
                                                                  idePais.indNIF.cdata, 
                                                                  1, u'1, 2, 3')
                            
                            if 'nifBenef' in dir(idePais):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePais.nifBenef', 
                                                                  idePais.nifBenef.cdata, 
                                                                  0, u'None')
                    
                    if 'endExt' in dir(idePgtoExt.endExt):
                        for endExt in idePgtoExt.endExt:
                            
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
                            
                            if 'nmCid' in dir(endExt):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'endExt.nmCid', 
                                                                  endExt.nmCid.cdata, 
                                                                  1, u'None')
                            
                            if 'codPostal' in dir(endExt):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'endExt.codPostal', 
                                                                  endExt.codPostal.cdata, 
                                                                  0, u'None')
    return validacoes_lista