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


def validacoes_s2220_evtmonit(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtMonit = doc.eSocial.evtMonit
    #variaveis
    
    if 'ideEvento' in dir(evtMonit.ideEvento):
        for ideEvento in evtMonit.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtMonit.ideEmpregador):
        for ideEmpregador in evtMonit.ideEmpregador:
            
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
    
    if 'ideVinculo' in dir(evtMonit.ideVinculo):
        for ideVinculo in evtMonit.ideVinculo:
            
            if 'cpfTrab' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.cpfTrab', 
                                                  ideVinculo.cpfTrab.cdata, 
                                                  1, u'None')
            
            if 'nisTrab' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.nisTrab', 
                                                  ideVinculo.nisTrab.cdata, 
                                                  0, u'None')
            
            if 'matricula' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.matricula', 
                                                  ideVinculo.matricula.cdata, 
                                                  0, u'None')
            
            if 'codCateg' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.codCateg', 
                                                  ideVinculo.codCateg.cdata, 
                                                  0, u'None')
    
    if 'exMedOcup' in dir(evtMonit.exMedOcup):
        for exMedOcup in evtMonit.exMedOcup:
            
            if 'tpExameOcup' in dir(exMedOcup):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'exMedOcup.tpExameOcup', 
                                                  exMedOcup.tpExameOcup.cdata, 
                                                  1, u'0, 1, 2, 3, 4, 9')
            
            if 'aso' in dir(exMedOcup.aso):
                for aso in exMedOcup.aso:
                    
                    if 'dtAso' in dir(aso):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'aso.dtAso', 
                                                          aso.dtAso.cdata, 
                                                          1, u'None')
                    
                    if 'tpAso' in dir(aso):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'aso.tpAso', 
                                                          aso.tpAso.cdata, 
                                                          1, u'0, 1, 2, 3, 4, 8')
                    
                    if 'resAso' in dir(aso):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'aso.resAso', 
                                                          aso.resAso.cdata, 
                                                          1, u'1, 2')
                    
                    if 'exame' in dir(aso.exame):
                        for exame in aso.exame:
                            
                            if 'dtExm' in dir(exame):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'exame.dtExm', 
                                                                  exame.dtExm.cdata, 
                                                                  1, u'None')
                            
                            if 'procRealizado' in dir(exame):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'exame.procRealizado', 
                                                                  exame.procRealizado.cdata, 
                                                                  1, u'None')
                            
                            if 'obsProc' in dir(exame):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'exame.obsProc', 
                                                                  exame.obsProc.cdata, 
                                                                  0, u'None')
                            
                            if 'interprExm' in dir(exame):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'exame.interprExm', 
                                                                  exame.interprExm.cdata, 
                                                                  1, u'1, 2, 3')
                            
                            if 'ordExame' in dir(exame):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'exame.ordExame', 
                                                                  exame.ordExame.cdata, 
                                                                  1, u'1, 2')
                            
                            if 'dtIniMonit' in dir(exame):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'exame.dtIniMonit', 
                                                                  exame.dtIniMonit.cdata, 
                                                                  1, u'None')
                            
                            if 'dtFimMonit' in dir(exame):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'exame.dtFimMonit', 
                                                                  exame.dtFimMonit.cdata, 
                                                                  0, u'None')
                            
                            if 'indResult' in dir(exame):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'exame.indResult', 
                                                                  exame.indResult.cdata, 
                                                                  0, u'1, 2, 3, 4')
                    
                    if 'medico' in dir(aso.medico):
                        for medico in aso.medico:
                            
                            if 'cpfMed' in dir(medico):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'medico.cpfMed', 
                                                                  medico.cpfMed.cdata, 
                                                                  0, u'None')
                            
                            if 'nisMed' in dir(medico):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'medico.nisMed', 
                                                                  medico.nisMed.cdata, 
                                                                  0, u'None')
                            
                            if 'nmMed' in dir(medico):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'medico.nmMed', 
                                                                  medico.nmMed.cdata, 
                                                                  1, u'None')
                            
                            if 'nrCRM' in dir(medico):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'medico.nrCRM', 
                                                                  medico.nrCRM.cdata, 
                                                                  1, u'None')
                            
                            if 'ufCRM' in dir(medico):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'medico.ufCRM', 
                                                                  medico.ufCRM.cdata, 
                                                                  1, u'None')
            
            if 'respMonit' in dir(exMedOcup.respMonit):
                for respMonit in exMedOcup.respMonit:
                    
                    if 'nisResp' in dir(respMonit):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respMonit.nisResp', 
                                                          respMonit.nisResp.cdata, 
                                                          1, u'None')
                    
                    if 'nrConsClasse' in dir(respMonit):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respMonit.nrConsClasse', 
                                                          respMonit.nrConsClasse.cdata, 
                                                          1, u'None')
                    
                    if 'ufConsClasse' in dir(respMonit):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respMonit.ufConsClasse', 
                                                          respMonit.ufConsClasse.cdata, 
                                                          0, u'None')
                    
                    if 'cpfResp' in dir(respMonit):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respMonit.cpfResp', 
                                                          respMonit.cpfResp.cdata, 
                                                          0, u'None')
                    
                    if 'nmResp' in dir(respMonit):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respMonit.nmResp', 
                                                          respMonit.nmResp.cdata, 
                                                          1, u'None')
                    
                    if 'nrCRM' in dir(respMonit):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respMonit.nrCRM', 
                                                          respMonit.nrCRM.cdata, 
                                                          1, u'None')
                    
                    if 'ufCRM' in dir(respMonit):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respMonit.ufCRM', 
                                                          respMonit.ufCRM.cdata, 
                                                          1, u'None')
    return validacoes_lista