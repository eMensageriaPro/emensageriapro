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


def validacoes_s5001_evtbasestrab(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtBasesTrab = doc.eSocial.evtBasesTrab
    #variaveis

    if 'ideEvento' in dir(evtBasesTrab.ideEvento):
        for ideEvento in evtBasesTrab.ideEvento:

            if 'nrRecArqBase' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.nrRecArqBase',
                                                  ideEvento.nrRecArqBase.cdata,
                                                  1, u'None')

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

    if 'ideEmpregador' in dir(evtBasesTrab.ideEmpregador):
        for ideEmpregador in evtBasesTrab.ideEmpregador:

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

    if 'ideTrabalhador' in dir(evtBasesTrab.ideTrabalhador):
        for ideTrabalhador in evtBasesTrab.ideTrabalhador:

            if 'cpfTrab' in dir(ideTrabalhador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideTrabalhador.cpfTrab',
                                                  ideTrabalhador.cpfTrab.cdata,
                                                  1, u'None')

            if 'procJudTrab' in dir(ideTrabalhador.procJudTrab):
                for procJudTrab in ideTrabalhador.procJudTrab:

                    if 'nrProcJud' in dir(procJudTrab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'procJudTrab.nrProcJud',
                                                          procJudTrab.nrProcJud.cdata,
                                                          1, u'None')

                    if 'codSusp' in dir(procJudTrab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'procJudTrab.codSusp',
                                                          procJudTrab.codSusp.cdata,
                                                          1, u'None')

    if 'infoCpCalc' in dir(evtBasesTrab.infoCpCalc):
        for infoCpCalc in evtBasesTrab.infoCpCalc:

            if 'tpCR' in dir(infoCpCalc):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoCpCalc.tpCR',
                                                  infoCpCalc.tpCR.cdata,
                                                  1, u'1082-01, 1082-02, 1082-03, 1082-04, 1082-21, 1082-22, 1082-23, 1082-24, 1099-01, 1099-02')

            if 'vrCpSeg' in dir(infoCpCalc):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoCpCalc.vrCpSeg',
                                                  infoCpCalc.vrCpSeg.cdata,
                                                  1, u'None')

            if 'vrDescSeg' in dir(infoCpCalc):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoCpCalc.vrDescSeg',
                                                  infoCpCalc.vrDescSeg.cdata,
                                                  1, u'None')

    if 'infoCp' in dir(evtBasesTrab.infoCp):
        for infoCp in evtBasesTrab.infoCp:

            if 'ideEstabLot' in dir(infoCp.ideEstabLot):
                for ideEstabLot in infoCp.ideEstabLot:

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

                    if 'infoCategIncid' in dir(ideEstabLot.infoCategIncid):
                        for infoCategIncid in ideEstabLot.infoCategIncid:
        
                            if 'matricula' in dir(infoCategIncid):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCategIncid.matricula',
                                                                  infoCategIncid.matricula.cdata,
                                                                  0, u'None')
        
                            if 'codCateg' in dir(infoCategIncid):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCategIncid.codCateg',
                                                                  infoCategIncid.codCateg.cdata,
                                                                  1, u'101, 102, 103, 104, 105, 106, 107, 108, 111, 201, 202, 301, 302, 303, 305, 306, 307, 308, 309, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 751, 761, 771, 781, 901, 902, 903, 904, 905')
        
                            if 'indSimples' in dir(infoCategIncid):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCategIncid.indSimples',
                                                                  infoCategIncid.indSimples.cdata,
                                                                  0, u'1, 2, 3')
        
                            if 'infoBaseCS' in dir(infoCategIncid.infoBaseCS):
                                for infoBaseCS in infoCategIncid.infoBaseCS:
                
                                    if 'ind13' in dir(infoBaseCS):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoBaseCS.ind13',
                                                                          infoBaseCS.ind13.cdata,
                                                                          1, u'0, 1')
                
                                    if 'tpValor' in dir(infoBaseCS):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoBaseCS.tpValor',
                                                                          infoBaseCS.tpValor.cdata,
                                                                          1, u'11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 31, 32, 41, 42, 43, 44, 45, 46, 47, 48, 49, 81, 82, 83, 84, 85, 86, 87, 88, 91, 92, 93, 94, 95, 97, 98')
                
                                    if 'valor' in dir(infoBaseCS):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoBaseCS.valor',
                                                                          infoBaseCS.valor.cdata,
                                                                          1, u'None')
        
                            if 'calcTerc' in dir(infoCategIncid.calcTerc):
                                for calcTerc in infoCategIncid.calcTerc:
                
                                    if 'tpCR' in dir(calcTerc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'calcTerc.tpCR',
                                                                          calcTerc.tpCR.cdata,
                                                                          1, u'1218-02, 1221-02')
                
                                    if 'vrCsSegTerc' in dir(calcTerc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'calcTerc.vrCsSegTerc',
                                                                          calcTerc.vrCsSegTerc.cdata,
                                                                          1, u'None')
                
                                    if 'vrDescTerc' in dir(calcTerc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'calcTerc.vrDescTerc',
                                                                          calcTerc.vrDescTerc.cdata,
                                                                          1, u'None')
    return validacoes_lista