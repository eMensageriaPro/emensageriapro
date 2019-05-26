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


def validacoes_s1080_evttaboperport(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabOperPort = doc.eSocial.evtTabOperPort
    #variaveis
    
    if 'ideEvento' in dir(evtTabOperPort.ideEvento):
        for ideEvento in evtTabOperPort.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtTabOperPort.ideEmpregador):
        for ideEmpregador in evtTabOperPort.ideEmpregador:
            
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
    
    if 'infoOperPortuario' in dir(evtTabOperPort.infoOperPortuario):
        for infoOperPortuario in evtTabOperPort.infoOperPortuario:
            
            if 'inclusao' in dir(infoOperPortuario.inclusao):
                for inclusao in infoOperPortuario.inclusao:
                    
                    if 'ideOperPortuario' in dir(inclusao.ideOperPortuario):
                        for ideOperPortuario in inclusao.ideOperPortuario:
                            
                            if 'cnpjOpPortuario' in dir(ideOperPortuario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideOperPortuario.cnpjOpPortuario', 
                                                                  ideOperPortuario.cnpjOpPortuario.cdata, 
                                                                  1, u'None')
                            
                            if 'iniValid' in dir(ideOperPortuario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideOperPortuario.iniValid', 
                                                                  ideOperPortuario.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideOperPortuario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideOperPortuario.fimValid', 
                                                                  ideOperPortuario.fimValid.cdata, 
                                                                  0, u'None')
                    
                    if 'dadosOperPortuario' in dir(inclusao.dadosOperPortuario):
                        for dadosOperPortuario in inclusao.dadosOperPortuario:
                            
                            if 'aliqRat' in dir(dadosOperPortuario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosOperPortuario.aliqRat', 
                                                                  dadosOperPortuario.aliqRat.cdata, 
                                                                  1, u'1, 2, 3')
                            
                            if 'fap' in dir(dadosOperPortuario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosOperPortuario.fap', 
                                                                  dadosOperPortuario.fap.cdata, 
                                                                  1, u'None')
                            
                            if 'aliqRatAjust' in dir(dadosOperPortuario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosOperPortuario.aliqRatAjust', 
                                                                  dadosOperPortuario.aliqRatAjust.cdata, 
                                                                  1, u'None')
            
            if 'alteracao' in dir(infoOperPortuario.alteracao):
                for alteracao in infoOperPortuario.alteracao:
                    
                    if 'ideOperPortuario' in dir(alteracao.ideOperPortuario):
                        for ideOperPortuario in alteracao.ideOperPortuario:
                            
                            if 'cnpjOpPortuario' in dir(ideOperPortuario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideOperPortuario.cnpjOpPortuario', 
                                                                  ideOperPortuario.cnpjOpPortuario.cdata, 
                                                                  1, u'None')
                            
                            if 'iniValid' in dir(ideOperPortuario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideOperPortuario.iniValid', 
                                                                  ideOperPortuario.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideOperPortuario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideOperPortuario.fimValid', 
                                                                  ideOperPortuario.fimValid.cdata, 
                                                                  0, u'None')
                    
                    if 'dadosOperPortuario' in dir(alteracao.dadosOperPortuario):
                        for dadosOperPortuario in alteracao.dadosOperPortuario:
                            
                            if 'aliqRat' in dir(dadosOperPortuario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosOperPortuario.aliqRat', 
                                                                  dadosOperPortuario.aliqRat.cdata, 
                                                                  1, u'1, 2, 3')
                            
                            if 'fap' in dir(dadosOperPortuario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosOperPortuario.fap', 
                                                                  dadosOperPortuario.fap.cdata, 
                                                                  1, u'None')
                            
                            if 'aliqRatAjust' in dir(dadosOperPortuario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosOperPortuario.aliqRatAjust', 
                                                                  dadosOperPortuario.aliqRatAjust.cdata, 
                                                                  1, u'None')
                    
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
            
            if 'exclusao' in dir(infoOperPortuario.exclusao):
                for exclusao in infoOperPortuario.exclusao:
                    
                    if 'ideOperPortuario' in dir(exclusao.ideOperPortuario):
                        for ideOperPortuario in exclusao.ideOperPortuario:
                            
                            if 'cnpjOpPortuario' in dir(ideOperPortuario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideOperPortuario.cnpjOpPortuario', 
                                                                  ideOperPortuario.cnpjOpPortuario.cdata, 
                                                                  1, u'None')
                            
                            if 'iniValid' in dir(ideOperPortuario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideOperPortuario.iniValid', 
                                                                  ideOperPortuario.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideOperPortuario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideOperPortuario.fimValid', 
                                                                  ideOperPortuario.fimValid.cdata, 
                                                                  0, u'None')
    return validacoes_lista