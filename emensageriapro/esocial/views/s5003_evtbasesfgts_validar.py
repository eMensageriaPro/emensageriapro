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


def validacoes_s5003_evtbasesfgts(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtBasesFGTS = doc.eSocial.evtBasesFGTS
    #variaveis

    if 'ideEvento' in dir(evtBasesFGTS.ideEvento):
        for ideEvento in evtBasesFGTS.ideEvento:

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

    if 'ideEmpregador' in dir(evtBasesFGTS.ideEmpregador):
        for ideEmpregador in evtBasesFGTS.ideEmpregador:

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

    if 'ideTrabalhador' in dir(evtBasesFGTS.ideTrabalhador):
        for ideTrabalhador in evtBasesFGTS.ideTrabalhador:

            if 'cpfTrab' in dir(ideTrabalhador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideTrabalhador.cpfTrab',
                                                  ideTrabalhador.cpfTrab.cdata,
                                                  1, u'None')

            if 'nisTrab' in dir(ideTrabalhador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideTrabalhador.nisTrab',
                                                  ideTrabalhador.nisTrab.cdata,
                                                  0, u'None')

    if 'infoFGTS' in dir(evtBasesFGTS.infoFGTS):
        for infoFGTS in evtBasesFGTS.infoFGTS:

            if 'dtVenc' in dir(infoFGTS):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoFGTS.dtVenc',
                                                  infoFGTS.dtVenc.cdata,
                                                  0, u'None')

            if 'ideEstabLot' in dir(infoFGTS.ideEstabLot):
                for ideEstabLot in infoFGTS.ideEstabLot:

                    if 'tpInsc' in dir(ideEstabLot):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstabLot.tpInsc',
                                                          ideEstabLot.tpInsc.cdata,
                                                          1, u'1, 2, 3, 4, 5, 6')

                    if 'nrInsc' in dir(ideEstabLot):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstabLot.nrInsc',
                                                          ideEstabLot.nrInsc.cdata,
                                                          1, u'None')

                    if 'codLotacao' in dir(ideEstabLot):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstabLot.codLotacao',
                                                          ideEstabLot.codLotacao.cdata,
                                                          1, u'None')

                    if 'infoTrabFGTS' in dir(ideEstabLot.infoTrabFGTS):
                        for infoTrabFGTS in ideEstabLot.infoTrabFGTS:
        
                            if 'matricula' in dir(infoTrabFGTS):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabFGTS.matricula',
                                                                  infoTrabFGTS.matricula.cdata,
                                                                  0, u'None')
        
                            if 'codCateg' in dir(infoTrabFGTS):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabFGTS.codCateg',
                                                                  infoTrabFGTS.codCateg.cdata,
                                                                  1, u'101, 102, 103, 104, 105, 106, 107, 108, 111, 201, 202, 301, 302, 303, 305, 306, 307, 308, 309, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 751, 761, 771, 781, 901, 902, 903, 904, 905')
        
                            if 'dtAdm' in dir(infoTrabFGTS):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabFGTS.dtAdm',
                                                                  infoTrabFGTS.dtAdm.cdata,
                                                                  0, u'None')
        
                            if 'dtDeslig' in dir(infoTrabFGTS):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabFGTS.dtDeslig',
                                                                  infoTrabFGTS.dtDeslig.cdata,
                                                                  0, u'None')
        
                            if 'dtInicio' in dir(infoTrabFGTS):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabFGTS.dtInicio',
                                                                  infoTrabFGTS.dtInicio.cdata,
                                                                  0, u'None')
        
                            if 'mtvDeslig' in dir(infoTrabFGTS):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabFGTS.mtvDeslig',
                                                                  infoTrabFGTS.mtvDeslig.cdata,
                                                                  0, u'01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36')
        
                            if 'dtTerm' in dir(infoTrabFGTS):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabFGTS.dtTerm',
                                                                  infoTrabFGTS.dtTerm.cdata,
                                                                  0, u'None')
        
                            if 'mtvDesligTSV' in dir(infoTrabFGTS):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabFGTS.mtvDesligTSV',
                                                                  infoTrabFGTS.mtvDesligTSV.cdata,
                                                                  0, u'01, 02, 03, 04, 05, 06, 07, 99')
        
                            if 'infoBaseFGTS' in dir(infoTrabFGTS.infoBaseFGTS):
                                for infoBaseFGTS in infoTrabFGTS.infoBaseFGTS:
                
                                    if 'basePerApur' in dir(infoBaseFGTS.basePerApur):
                                        for basePerApur in infoBaseFGTS.basePerApur:
                        
                                            if 'tpValor' in dir(basePerApur):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'basePerApur.tpValor',
                                                                                  basePerApur.tpValor.cdata,
                                                                                  1, u'11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 91')
                        
                                            if 'remFGTS' in dir(basePerApur):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'basePerApur.remFGTS',
                                                                                  basePerApur.remFGTS.cdata,
                                                                                  1, u'None')
                
                                    if 'infoBasePerAntE' in dir(infoBaseFGTS.infoBasePerAntE):
                                        for infoBasePerAntE in infoBaseFGTS.infoBasePerAntE:
                        
                                            if 'perRef' in dir(infoBasePerAntE):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoBasePerAntE.perRef',
                                                                                  infoBasePerAntE.perRef.cdata,
                                                                                  1, u'None')
                        
                                            if 'basePerAntE' in dir(infoBasePerAntE.basePerAntE):
                                                for basePerAntE in infoBasePerAntE.basePerAntE:
                                
                                                    if 'tpValorE' in dir(basePerAntE):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'basePerAntE.tpValorE',
                                                                                          basePerAntE.tpValorE.cdata,
                                                                                          1, u'13, 14, 17, 18, 24, 25, 26, 30, 31, 32, 91')
                                
                                                    if 'remFGTSE' in dir(basePerAntE):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'basePerAntE.remFGTSE',
                                                                                          basePerAntE.remFGTSE.cdata,
                                                                                          1, u'None')

            if 'infoDpsFGTS' in dir(infoFGTS.infoDpsFGTS):
                for infoDpsFGTS in infoFGTS.infoDpsFGTS:

                    if 'infoTrabDps' in dir(infoDpsFGTS.infoTrabDps):
                        for infoTrabDps in infoDpsFGTS.infoTrabDps:
        
                            if 'matricula' in dir(infoTrabDps):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabDps.matricula',
                                                                  infoTrabDps.matricula.cdata,
                                                                  0, u'None')
        
                            if 'codCateg' in dir(infoTrabDps):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabDps.codCateg',
                                                                  infoTrabDps.codCateg.cdata,
                                                                  1, u'101, 102, 103, 104, 105, 106, 107, 108, 111, 201, 202, 301, 302, 303, 305, 306, 307, 308, 309, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 751, 761, 771, 781, 901, 902, 903, 904, 905')
        
                            if 'dpsPerApur' in dir(infoTrabDps.dpsPerApur):
                                for dpsPerApur in infoTrabDps.dpsPerApur:
                
                                    if 'tpDps' in dir(dpsPerApur):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dpsPerApur.tpDps',
                                                                          dpsPerApur.tpDps.cdata,
                                                                          1, u'51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82')
                
                                    if 'dpsFGTS' in dir(dpsPerApur):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dpsPerApur.dpsFGTS',
                                                                          dpsPerApur.dpsFGTS.cdata,
                                                                          1, u'None')
        
                            if 'infoDpsPerAntE' in dir(infoTrabDps.infoDpsPerAntE):
                                for infoDpsPerAntE in infoTrabDps.infoDpsPerAntE:
                
                                    if 'perRef' in dir(infoDpsPerAntE):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoDpsPerAntE.perRef',
                                                                          infoDpsPerAntE.perRef.cdata,
                                                                          1, u'None')
                
                                    if 'dpsPerAntE' in dir(infoDpsPerAntE.dpsPerAntE):
                                        for dpsPerAntE in infoDpsPerAntE.dpsPerAntE:
                        
                                            if 'tpDpsE' in dir(dpsPerAntE):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'dpsPerAntE.tpDpsE',
                                                                                  dpsPerAntE.tpDpsE.cdata,
                                                                                  1, u'53, 54, 57, 58, 64, 65, 66, 70, 71, 72, 75, 76, 80, 81, 82')
                        
                                            if 'dpsFGTSE' in dir(dpsPerAntE):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'dpsPerAntE.dpsFGTSE',
                                                                                  dpsPerAntE.dpsFGTSE.cdata,
                                                                                  1, u'None')
    return validacoes_lista