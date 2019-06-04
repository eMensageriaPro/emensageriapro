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


def validacoes_s1005_evttabestab(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabEstab = doc.eSocial.evtTabEstab
    #variaveis
    
    if 'ideEvento' in dir(evtTabEstab.ideEvento):
        for ideEvento in evtTabEstab.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtTabEstab.ideEmpregador):
        for ideEmpregador in evtTabEstab.ideEmpregador:
            
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
    
    if 'infoEstab' in dir(evtTabEstab.infoEstab):
        for infoEstab in evtTabEstab.infoEstab:
            
            if 'inclusao' in dir(infoEstab.inclusao):
                for inclusao in infoEstab.inclusao:
                    
                    if 'ideEstab' in dir(inclusao.ideEstab):
                        for ideEstab in inclusao.ideEstab:
                            
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
                            
                            if 'iniValid' in dir(ideEstab):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideEstab.iniValid', 
                                                                  ideEstab.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideEstab):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideEstab.fimValid', 
                                                                  ideEstab.fimValid.cdata, 
                                                                  0, u'None')
                    
                    if 'dadosEstab' in dir(inclusao.dadosEstab):
                        for dadosEstab in inclusao.dadosEstab:
                            
                            if 'cnaePrep' in dir(dadosEstab):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosEstab.cnaePrep', 
                                                                  dadosEstab.cnaePrep.cdata, 
                                                                  1, u'None')
                            
                            if 'aliqGilrat' in dir(dadosEstab.aliqGilrat):
                                for aliqGilrat in dadosEstab.aliqGilrat:
                                    
                                    if 'aliqRat' in dir(aliqGilrat):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'aliqGilrat.aliqRat', 
                                                                          aliqGilrat.aliqRat.cdata, 
                                                                          1, u'1, 2, 3')
                                    
                                    if 'fap' in dir(aliqGilrat):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'aliqGilrat.fap', 
                                                                          aliqGilrat.fap.cdata, 
                                                                          0, u'None')
                                    
                                    if 'aliqRatAjust' in dir(aliqGilrat):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'aliqGilrat.aliqRatAjust', 
                                                                          aliqGilrat.aliqRatAjust.cdata, 
                                                                          0, u'None')
                                    
                                    if 'procAdmJudRat' in dir(aliqGilrat.procAdmJudRat):
                                        for procAdmJudRat in aliqGilrat.procAdmJudRat:
                                            
                                            if 'tpProc' in dir(procAdmJudRat):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'procAdmJudRat.tpProc', 
                                                                                  procAdmJudRat.tpProc.cdata, 
                                                                                  1, u'1, 2')
                                            
                                            if 'nrProc' in dir(procAdmJudRat):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'procAdmJudRat.nrProc', 
                                                                                  procAdmJudRat.nrProc.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'codSusp' in dir(procAdmJudRat):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'procAdmJudRat.codSusp', 
                                                                                  procAdmJudRat.codSusp.cdata, 
                                                                                  1, u'None')
                                    
                                    if 'procAdmJudFap' in dir(aliqGilrat.procAdmJudFap):
                                        for procAdmJudFap in aliqGilrat.procAdmJudFap:
                                            
                                            if 'tpProc' in dir(procAdmJudFap):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'procAdmJudFap.tpProc', 
                                                                                  procAdmJudFap.tpProc.cdata, 
                                                                                  1, u'1, 2, 4')
                                            
                                            if 'nrProc' in dir(procAdmJudFap):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'procAdmJudFap.nrProc', 
                                                                                  procAdmJudFap.nrProc.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'codSusp' in dir(procAdmJudFap):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'procAdmJudFap.codSusp', 
                                                                                  procAdmJudFap.codSusp.cdata, 
                                                                                  1, u'None')
                            
                            if 'infoCaepf' in dir(dadosEstab.infoCaepf):
                                for infoCaepf in dadosEstab.infoCaepf:
                                    
                                    if 'tpCaepf' in dir(infoCaepf):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoCaepf.tpCaepf', 
                                                                          infoCaepf.tpCaepf.cdata, 
                                                                          1, u'1, 2, 3')
                            
                            if 'infoObra' in dir(dadosEstab.infoObra):
                                for infoObra in dadosEstab.infoObra:
                                    
                                    if 'indSubstPatrObra' in dir(infoObra):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoObra.indSubstPatrObra', 
                                                                          infoObra.indSubstPatrObra.cdata, 
                                                                          1, u'1, 2')
                            
                            if 'infoTrab' in dir(dadosEstab.infoTrab):
                                for infoTrab in dadosEstab.infoTrab:
                                    
                                    if 'regPt' in dir(infoTrab):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoTrab.regPt', 
                                                                          infoTrab.regPt.cdata, 
                                                                          1, u'0, 1, 2, 3, 4, 5, 6')
                                    
                                    if 'infoApr' in dir(infoTrab.infoApr):
                                        for infoApr in infoTrab.infoApr:
                                            
                                            if 'contApr' in dir(infoApr):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoApr.contApr', 
                                                                                  infoApr.contApr.cdata, 
                                                                                  1, u'0, 1, 2')
                                            
                                            if 'nrProcJud' in dir(infoApr):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoApr.nrProcJud', 
                                                                                  infoApr.nrProcJud.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'contEntEd' in dir(infoApr):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoApr.contEntEd', 
                                                                                  infoApr.contEntEd.cdata, 
                                                                                  0, u'S, N')
                                            
                                            if 'infoEntEduc' in dir(infoApr.infoEntEduc):
                                                for infoEntEduc in infoApr.infoEntEduc:
                                                    
                                                    if 'nrInsc' in dir(infoEntEduc):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'infoEntEduc.nrInsc', 
                                                                                          infoEntEduc.nrInsc.cdata, 
                                                                                          1, u'None')
                                    
                                    if 'infoPCD' in dir(infoTrab.infoPCD):
                                        for infoPCD in infoTrab.infoPCD:
                                            
                                            if 'contPCD' in dir(infoPCD):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoPCD.contPCD', 
                                                                                  infoPCD.contPCD.cdata, 
                                                                                  1, u'0, 1, 2, 9')
                                            
                                            if 'nrProcJud' in dir(infoPCD):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoPCD.nrProcJud', 
                                                                                  infoPCD.nrProcJud.cdata, 
                                                                                  0, u'None')
            
            if 'alteracao' in dir(infoEstab.alteracao):
                for alteracao in infoEstab.alteracao:
                    
                    if 'ideEstab' in dir(alteracao.ideEstab):
                        for ideEstab in alteracao.ideEstab:
                            
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
                            
                            if 'iniValid' in dir(ideEstab):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideEstab.iniValid', 
                                                                  ideEstab.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideEstab):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideEstab.fimValid', 
                                                                  ideEstab.fimValid.cdata, 
                                                                  0, u'None')
                    
                    if 'dadosEstab' in dir(alteracao.dadosEstab):
                        for dadosEstab in alteracao.dadosEstab:
                            
                            if 'cnaePrep' in dir(dadosEstab):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosEstab.cnaePrep', 
                                                                  dadosEstab.cnaePrep.cdata, 
                                                                  1, u'None')
                            
                            if 'aliqGilrat' in dir(dadosEstab.aliqGilrat):
                                for aliqGilrat in dadosEstab.aliqGilrat:
                                    
                                    if 'aliqRat' in dir(aliqGilrat):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'aliqGilrat.aliqRat', 
                                                                          aliqGilrat.aliqRat.cdata, 
                                                                          1, u'1, 2, 3')
                                    
                                    if 'fap' in dir(aliqGilrat):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'aliqGilrat.fap', 
                                                                          aliqGilrat.fap.cdata, 
                                                                          0, u'None')
                                    
                                    if 'aliqRatAjust' in dir(aliqGilrat):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'aliqGilrat.aliqRatAjust', 
                                                                          aliqGilrat.aliqRatAjust.cdata, 
                                                                          0, u'None')
                                    
                                    if 'procAdmJudRat' in dir(aliqGilrat.procAdmJudRat):
                                        for procAdmJudRat in aliqGilrat.procAdmJudRat:
                                            
                                            if 'tpProc' in dir(procAdmJudRat):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'procAdmJudRat.tpProc', 
                                                                                  procAdmJudRat.tpProc.cdata, 
                                                                                  1, u'1, 2')
                                            
                                            if 'nrProc' in dir(procAdmJudRat):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'procAdmJudRat.nrProc', 
                                                                                  procAdmJudRat.nrProc.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'codSusp' in dir(procAdmJudRat):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'procAdmJudRat.codSusp', 
                                                                                  procAdmJudRat.codSusp.cdata, 
                                                                                  1, u'None')
                                    
                                    if 'procAdmJudFap' in dir(aliqGilrat.procAdmJudFap):
                                        for procAdmJudFap in aliqGilrat.procAdmJudFap:
                                            
                                            if 'tpProc' in dir(procAdmJudFap):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'procAdmJudFap.tpProc', 
                                                                                  procAdmJudFap.tpProc.cdata, 
                                                                                  1, u'1, 2, 4')
                                            
                                            if 'nrProc' in dir(procAdmJudFap):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'procAdmJudFap.nrProc', 
                                                                                  procAdmJudFap.nrProc.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'codSusp' in dir(procAdmJudFap):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'procAdmJudFap.codSusp', 
                                                                                  procAdmJudFap.codSusp.cdata, 
                                                                                  1, u'None')
                            
                            if 'infoCaepf' in dir(dadosEstab.infoCaepf):
                                for infoCaepf in dadosEstab.infoCaepf:
                                    
                                    if 'tpCaepf' in dir(infoCaepf):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoCaepf.tpCaepf', 
                                                                          infoCaepf.tpCaepf.cdata, 
                                                                          1, u'1, 2, 3')
                            
                            if 'infoObra' in dir(dadosEstab.infoObra):
                                for infoObra in dadosEstab.infoObra:
                                    
                                    if 'indSubstPatrObra' in dir(infoObra):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoObra.indSubstPatrObra', 
                                                                          infoObra.indSubstPatrObra.cdata, 
                                                                          1, u'1, 2')
                            
                            if 'infoTrab' in dir(dadosEstab.infoTrab):
                                for infoTrab in dadosEstab.infoTrab:
                                    
                                    if 'regPt' in dir(infoTrab):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoTrab.regPt', 
                                                                          infoTrab.regPt.cdata, 
                                                                          1, u'0, 1, 2, 3, 4, 5, 6')
                                    
                                    if 'infoApr' in dir(infoTrab.infoApr):
                                        for infoApr in infoTrab.infoApr:
                                            
                                            if 'contApr' in dir(infoApr):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoApr.contApr', 
                                                                                  infoApr.contApr.cdata, 
                                                                                  1, u'0, 1, 2')
                                            
                                            if 'nrProcJud' in dir(infoApr):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoApr.nrProcJud', 
                                                                                  infoApr.nrProcJud.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'contEntEd' in dir(infoApr):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoApr.contEntEd', 
                                                                                  infoApr.contEntEd.cdata, 
                                                                                  0, u'S, N')
                                            
                                            if 'infoEntEduc' in dir(infoApr.infoEntEduc):
                                                for infoEntEduc in infoApr.infoEntEduc:
                                                    
                                                    if 'nrInsc' in dir(infoEntEduc):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'infoEntEduc.nrInsc', 
                                                                                          infoEntEduc.nrInsc.cdata, 
                                                                                          1, u'None')
                                    
                                    if 'infoPCD' in dir(infoTrab.infoPCD):
                                        for infoPCD in infoTrab.infoPCD:
                                            
                                            if 'contPCD' in dir(infoPCD):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoPCD.contPCD', 
                                                                                  infoPCD.contPCD.cdata, 
                                                                                  1, u'0, 1, 2, 9')
                                            
                                            if 'nrProcJud' in dir(infoPCD):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoPCD.nrProcJud', 
                                                                                  infoPCD.nrProcJud.cdata, 
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
            
            if 'exclusao' in dir(infoEstab.exclusao):
                for exclusao in infoEstab.exclusao:
                    
                    if 'ideEstab' in dir(exclusao.ideEstab):
                        for ideEstab in exclusao.ideEstab:
                            
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
                            
                            if 'iniValid' in dir(ideEstab):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideEstab.iniValid', 
                                                                  ideEstab.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideEstab):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideEstab.fimValid', 
                                                                  ideEstab.fimValid.cdata, 
                                                                  0, u'None')
    return validacoes_lista