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


def validacoes_s2241_evtinsapo(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtInsApo = doc.eSocial.evtInsApo
    #variaveis
    
    if 'ideEvento' in dir(evtInsApo.ideEvento):
        for ideEvento in evtInsApo.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtInsApo.ideEmpregador):
        for ideEmpregador in evtInsApo.ideEmpregador:
            
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
    
    if 'ideVinculo' in dir(evtInsApo.ideVinculo):
        for ideVinculo in evtInsApo.ideVinculo:
            
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
    
    if 'insalPeric' in dir(evtInsApo.insalPeric):
        for insalPeric in evtInsApo.insalPeric:
            
            if 'iniInsalPeric' in dir(insalPeric.iniInsalPeric):
                for iniInsalPeric in insalPeric.iniInsalPeric:
                    
                    if 'dtIniCondicao' in dir(iniInsalPeric):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'iniInsalPeric.dtIniCondicao', 
                                                          iniInsalPeric.dtIniCondicao.cdata, 
                                                          1, u'None')
                    
                    if 'infoAmb' in dir(iniInsalPeric.infoAmb):
                        for infoAmb in iniInsalPeric.infoAmb:
                            
                            if 'codAmb' in dir(infoAmb):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoAmb.codAmb', 
                                                                  infoAmb.codAmb.cdata, 
                                                                  1, u'None')
                            
                            if 'fatRisco' in dir(infoAmb.fatRisco):
                                for fatRisco in infoAmb.fatRisco:
                                    
                                    if 'codFatRis' in dir(fatRisco):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'fatRisco.codFatRis', 
                                                                          fatRisco.codFatRis.cdata, 
                                                                          1, u'None')
            
            if 'altInsalPeric' in dir(insalPeric.altInsalPeric):
                for altInsalPeric in insalPeric.altInsalPeric:
                    
                    if 'dtAltCondicao' in dir(altInsalPeric):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'altInsalPeric.dtAltCondicao', 
                                                          altInsalPeric.dtAltCondicao.cdata, 
                                                          1, u'None')
                    
                    if 'infoamb' in dir(altInsalPeric.infoamb):
                        for infoamb in altInsalPeric.infoamb:
                            
                            if 'codAmb' in dir(infoamb):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoamb.codAmb', 
                                                                  infoamb.codAmb.cdata, 
                                                                  1, u'None')
                            
                            if 'fatRisco' in dir(infoamb.fatRisco):
                                for fatRisco in infoamb.fatRisco:
                                    
                                    if 'codFatRis' in dir(fatRisco):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'fatRisco.codFatRis', 
                                                                          fatRisco.codFatRis.cdata, 
                                                                          1, u'None')
            
            if 'fimInsalPeric' in dir(insalPeric.fimInsalPeric):
                for fimInsalPeric in insalPeric.fimInsalPeric:
                    
                    if 'dtFimCondicao' in dir(fimInsalPeric):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fimInsalPeric.dtFimCondicao', 
                                                          fimInsalPeric.dtFimCondicao.cdata, 
                                                          1, u'None')
                    
                    if 'infoAmb' in dir(fimInsalPeric.infoAmb):
                        for infoAmb in fimInsalPeric.infoAmb:
                            
                            if 'codAmb' in dir(infoAmb):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoAmb.codAmb', 
                                                                  infoAmb.codAmb.cdata, 
                                                                  1, u'None')
    
    if 'aposentEsp' in dir(evtInsApo.aposentEsp):
        for aposentEsp in evtInsApo.aposentEsp:
            
            if 'iniAposentEsp' in dir(aposentEsp.iniAposentEsp):
                for iniAposentEsp in aposentEsp.iniAposentEsp:
                    
                    if 'dtIniCondicao' in dir(iniAposentEsp):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'iniAposentEsp.dtIniCondicao', 
                                                          iniAposentEsp.dtIniCondicao.cdata, 
                                                          1, u'None')
                    
                    if 'infoAmb' in dir(iniAposentEsp.infoAmb):
                        for infoAmb in iniAposentEsp.infoAmb:
                            
                            if 'codAmb' in dir(infoAmb):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoAmb.codAmb', 
                                                                  infoAmb.codAmb.cdata, 
                                                                  1, u'None')
                            
                            if 'fatRisco' in dir(infoAmb.fatRisco):
                                for fatRisco in infoAmb.fatRisco:
                                    
                                    if 'codFatRis' in dir(fatRisco):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'fatRisco.codFatRis', 
                                                                          fatRisco.codFatRis.cdata, 
                                                                          1, u'None')
            
            if 'altAposentEsp' in dir(aposentEsp.altAposentEsp):
                for altAposentEsp in aposentEsp.altAposentEsp:
                    
                    if 'dtAltCondicao' in dir(altAposentEsp):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'altAposentEsp.dtAltCondicao', 
                                                          altAposentEsp.dtAltCondicao.cdata, 
                                                          1, u'None')
                    
                    if 'infoamb' in dir(altAposentEsp.infoamb):
                        for infoamb in altAposentEsp.infoamb:
                            
                            if 'codAmb' in dir(infoamb):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoamb.codAmb', 
                                                                  infoamb.codAmb.cdata, 
                                                                  1, u'None')
                            
                            if 'fatRisco' in dir(infoamb.fatRisco):
                                for fatRisco in infoamb.fatRisco:
                                    
                                    if 'codFatRis' in dir(fatRisco):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'fatRisco.codFatRis', 
                                                                          fatRisco.codFatRis.cdata, 
                                                                          1, u'None')
            
            if 'fimAposentEsp' in dir(aposentEsp.fimAposentEsp):
                for fimAposentEsp in aposentEsp.fimAposentEsp:
                    
                    if 'dtFimCondicao' in dir(fimAposentEsp):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fimAposentEsp.dtFimCondicao', 
                                                          fimAposentEsp.dtFimCondicao.cdata, 
                                                          1, u'None')
                    
                    if 'infoAmb' in dir(fimAposentEsp.infoAmb):
                        for infoAmb in fimAposentEsp.infoAmb:
                            
                            if 'codAmb' in dir(infoAmb):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoAmb.codAmb', 
                                                                  infoAmb.codAmb.cdata, 
                                                                  1, u'None')
    return validacoes_lista