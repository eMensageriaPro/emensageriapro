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


def validacoes_r2030_evtassocdesprec(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtAssocDespRec = doc.Reinf.evtAssocDespRec
    #variaveis
    
    if 'ideEvento' in dir(evtAssocDespRec.ideEvento):
        for ideEvento in evtAssocDespRec.ideEvento:
            
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
    
    if 'ideContri' in dir(evtAssocDespRec.ideContri):
        for ideContri in evtAssocDespRec.ideContri:
            
            if 'tpInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.tpInsc', 
                                                  ideContri.tpInsc.cdata, 
                                                  1, u'1, 2, 3, 4, 5')
            
            if 'nrInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.nrInsc', 
                                                  ideContri.nrInsc.cdata, 
                                                  1, u'None')
            
            if 'ideEstab' in dir(ideContri.ideEstab):
                for ideEstab in ideContri.ideEstab:
                    
                    if 'tpInscEstab' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.tpInscEstab', 
                                                          ideEstab.tpInscEstab.cdata, 
                                                          1, u'None')
                    
                    if 'nrInscEstab' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.nrInscEstab', 
                                                          ideEstab.nrInscEstab.cdata, 
                                                          1, u'None')
                    
                    if 'recursosRec' in dir(ideEstab.recursosRec):
                        for recursosRec in ideEstab.recursosRec:
                            
                            if 'cnpjOrigRecurso' in dir(recursosRec):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'recursosRec.cnpjOrigRecurso', 
                                                                  recursosRec.cnpjOrigRecurso.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrTotalRec' in dir(recursosRec):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'recursosRec.vlrTotalRec', 
                                                                  recursosRec.vlrTotalRec.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrTotalRet' in dir(recursosRec):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'recursosRec.vlrTotalRet', 
                                                                  recursosRec.vlrTotalRet.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrTotalNRet' in dir(recursosRec):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'recursosRec.vlrTotalNRet', 
                                                                  recursosRec.vlrTotalNRet.cdata, 
                                                                  0, u'None')
                            
                            if 'infoRecurso' in dir(recursosRec.infoRecurso):
                                for infoRecurso in recursosRec.infoRecurso:
                                    
                                    if 'tpRepasse' in dir(infoRecurso):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoRecurso.tpRepasse', 
                                                                          infoRecurso.tpRepasse.cdata, 
                                                                          1, u'1, 2, 3, 4, 5')
                                    
                                    if 'descRecurso' in dir(infoRecurso):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoRecurso.descRecurso', 
                                                                          infoRecurso.descRecurso.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vlrBruto' in dir(infoRecurso):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoRecurso.vlrBruto', 
                                                                          infoRecurso.vlrBruto.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vlrRetApur' in dir(infoRecurso):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoRecurso.vlrRetApur', 
                                                                          infoRecurso.vlrRetApur.cdata, 
                                                                          1, u'None')
                            
                            if 'infoProc' in dir(recursosRec.infoProc):
                                for infoProc in recursosRec.infoProc:
                                    
                                    if 'tpProc' in dir(infoProc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProc.tpProc', 
                                                                          infoProc.tpProc.cdata, 
                                                                          1, u'1, 2')
                                    
                                    if 'nrProc' in dir(infoProc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProc.nrProc', 
                                                                          infoProc.nrProc.cdata, 
                                                                          1, u'None')
                                    
                                    if 'codSusp' in dir(infoProc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProc.codSusp', 
                                                                          infoProc.codSusp.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vlrNRet' in dir(infoProc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProc.vlrNRet', 
                                                                          infoProc.vlrNRet.cdata, 
                                                                          1, u'None')
    return validacoes_lista