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


def validacoes_s1050_evttabhortur(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabHorTur = doc.eSocial.evtTabHorTur
    #variaveis

    if 'ideEvento' in dir(evtTabHorTur.ideEvento):
        for ideEvento in evtTabHorTur.ideEvento:

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

    if 'ideEmpregador' in dir(evtTabHorTur.ideEmpregador):
        for ideEmpregador in evtTabHorTur.ideEmpregador:

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

    if 'infoHorContratual' in dir(evtTabHorTur.infoHorContratual):
        for infoHorContratual in evtTabHorTur.infoHorContratual:

            if 'inclusao' in dir(infoHorContratual.inclusao):
                for inclusao in infoHorContratual.inclusao:

                    if 'ideHorContratual' in dir(inclusao.ideHorContratual):
                        for ideHorContratual in inclusao.ideHorContratual:
        
                            if 'codHorContrat' in dir(ideHorContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideHorContratual.codHorContrat',
                                                                  ideHorContratual.codHorContrat.cdata,
                                                                  1, u'None')
        
                            if 'iniValid' in dir(ideHorContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideHorContratual.iniValid',
                                                                  ideHorContratual.iniValid.cdata,
                                                                  1, u'None')
        
                            if 'fimValid' in dir(ideHorContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideHorContratual.fimValid',
                                                                  ideHorContratual.fimValid.cdata,
                                                                  0, u'None')

                    if 'dadosHorContratual' in dir(inclusao.dadosHorContratual):
                        for dadosHorContratual in inclusao.dadosHorContratual:
        
                            if 'hrEntr' in dir(dadosHorContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosHorContratual.hrEntr',
                                                                  dadosHorContratual.hrEntr.cdata,
                                                                  1, u'None')
        
                            if 'hrSaida' in dir(dadosHorContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosHorContratual.hrSaida',
                                                                  dadosHorContratual.hrSaida.cdata,
                                                                  1, u'None')
        
                            if 'durJornada' in dir(dadosHorContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosHorContratual.durJornada',
                                                                  dadosHorContratual.durJornada.cdata,
                                                                  1, u'None')
        
                            if 'perHorFlexivel' in dir(dadosHorContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosHorContratual.perHorFlexivel',
                                                                  dadosHorContratual.perHorFlexivel.cdata,
                                                                  1, u'S, N')
        
                            if 'horarioIntervalo' in dir(dadosHorContratual.horarioIntervalo):
                                for horarioIntervalo in dadosHorContratual.horarioIntervalo:
                
                                    if 'tpInterv' in dir(horarioIntervalo):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'horarioIntervalo.tpInterv',
                                                                          horarioIntervalo.tpInterv.cdata,
                                                                          1, u'1, 2')
                
                                    if 'durInterv' in dir(horarioIntervalo):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'horarioIntervalo.durInterv',
                                                                          horarioIntervalo.durInterv.cdata,
                                                                          1, u'None')
                
                                    if 'iniInterv' in dir(horarioIntervalo):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'horarioIntervalo.iniInterv',
                                                                          horarioIntervalo.iniInterv.cdata,
                                                                          0, u'None')
                
                                    if 'termInterv' in dir(horarioIntervalo):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'horarioIntervalo.termInterv',
                                                                          horarioIntervalo.termInterv.cdata,
                                                                          0, u'None')

            if 'alteracao' in dir(infoHorContratual.alteracao):
                for alteracao in infoHorContratual.alteracao:

                    if 'ideHorContratual' in dir(alteracao.ideHorContratual):
                        for ideHorContratual in alteracao.ideHorContratual:
        
                            if 'codHorContrat' in dir(ideHorContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideHorContratual.codHorContrat',
                                                                  ideHorContratual.codHorContrat.cdata,
                                                                  1, u'None')
        
                            if 'iniValid' in dir(ideHorContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideHorContratual.iniValid',
                                                                  ideHorContratual.iniValid.cdata,
                                                                  1, u'None')
        
                            if 'fimValid' in dir(ideHorContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideHorContratual.fimValid',
                                                                  ideHorContratual.fimValid.cdata,
                                                                  0, u'None')

                    if 'dadosHorContratual' in dir(alteracao.dadosHorContratual):
                        for dadosHorContratual in alteracao.dadosHorContratual:
        
                            if 'hrEntr' in dir(dadosHorContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosHorContratual.hrEntr',
                                                                  dadosHorContratual.hrEntr.cdata,
                                                                  1, u'None')
        
                            if 'hrSaida' in dir(dadosHorContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosHorContratual.hrSaida',
                                                                  dadosHorContratual.hrSaida.cdata,
                                                                  1, u'None')
        
                            if 'durJornada' in dir(dadosHorContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosHorContratual.durJornada',
                                                                  dadosHorContratual.durJornada.cdata,
                                                                  1, u'None')
        
                            if 'perHorFlexivel' in dir(dadosHorContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosHorContratual.perHorFlexivel',
                                                                  dadosHorContratual.perHorFlexivel.cdata,
                                                                  1, u'S, N')
        
                            if 'horarioIntervalo' in dir(dadosHorContratual.horarioIntervalo):
                                for horarioIntervalo in dadosHorContratual.horarioIntervalo:
                
                                    if 'tpInterv' in dir(horarioIntervalo):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'horarioIntervalo.tpInterv',
                                                                          horarioIntervalo.tpInterv.cdata,
                                                                          1, u'1, 2')
                
                                    if 'durInterv' in dir(horarioIntervalo):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'horarioIntervalo.durInterv',
                                                                          horarioIntervalo.durInterv.cdata,
                                                                          1, u'None')
                
                                    if 'iniInterv' in dir(horarioIntervalo):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'horarioIntervalo.iniInterv',
                                                                          horarioIntervalo.iniInterv.cdata,
                                                                          0, u'None')
                
                                    if 'termInterv' in dir(horarioIntervalo):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'horarioIntervalo.termInterv',
                                                                          horarioIntervalo.termInterv.cdata,
                                                                          0, u'None')

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

            if 'exclusao' in dir(infoHorContratual.exclusao):
                for exclusao in infoHorContratual.exclusao:

                    if 'ideHorContratual' in dir(exclusao.ideHorContratual):
                        for ideHorContratual in exclusao.ideHorContratual:
        
                            if 'codHorContrat' in dir(ideHorContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideHorContratual.codHorContrat',
                                                                  ideHorContratual.codHorContrat.cdata,
                                                                  1, u'None')
        
                            if 'iniValid' in dir(ideHorContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideHorContratual.iniValid',
                                                                  ideHorContratual.iniValid.cdata,
                                                                  1, u'None')
        
                            if 'fimValid' in dir(ideHorContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideHorContratual.fimValid',
                                                                  ideHorContratual.fimValid.cdata,
                                                                  0, u'None')
    return validacoes_lista