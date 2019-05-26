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


def validacoes_s1060_evttabambiente(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabAmbiente = doc.eSocial.evtTabAmbiente
    #variaveis
    
    if 'ideEvento' in dir(evtTabAmbiente.ideEvento):
        for ideEvento in evtTabAmbiente.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtTabAmbiente.ideEmpregador):
        for ideEmpregador in evtTabAmbiente.ideEmpregador:
            
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
    
    if 'infoAmbiente' in dir(evtTabAmbiente.infoAmbiente):
        for infoAmbiente in evtTabAmbiente.infoAmbiente:
            
            if 'inclusao' in dir(infoAmbiente.inclusao):
                for inclusao in infoAmbiente.inclusao:
                    
                    if 'ideAmbiente' in dir(inclusao.ideAmbiente):
                        for ideAmbiente in inclusao.ideAmbiente:
                            
                            if 'codAmb' in dir(ideAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideAmbiente.codAmb', 
                                                                  ideAmbiente.codAmb.cdata, 
                                                                  1, u'None')
                            
                            if 'iniValid' in dir(ideAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideAmbiente.iniValid', 
                                                                  ideAmbiente.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideAmbiente.fimValid', 
                                                                  ideAmbiente.fimValid.cdata, 
                                                                  0, u'None')
                    
                    if 'dadosAmbiente' in dir(inclusao.dadosAmbiente):
                        for dadosAmbiente in inclusao.dadosAmbiente:
                            
                            if 'nmAmb' in dir(dadosAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosAmbiente.nmAmb', 
                                                                  dadosAmbiente.nmAmb.cdata, 
                                                                  1, u'None')
                            
                            if 'dscAmb' in dir(dadosAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosAmbiente.dscAmb', 
                                                                  dadosAmbiente.dscAmb.cdata, 
                                                                  1, u'None')
                            
                            if 'localAmb' in dir(dadosAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosAmbiente.localAmb', 
                                                                  dadosAmbiente.localAmb.cdata, 
                                                                  1, u'1, 2, 3')
                            
                            if 'tpInsc' in dir(dadosAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosAmbiente.tpInsc', 
                                                                  dadosAmbiente.tpInsc.cdata, 
                                                                  0, u'1, 2, 3, 4, 5')
                            
                            if 'nrInsc' in dir(dadosAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosAmbiente.nrInsc', 
                                                                  dadosAmbiente.nrInsc.cdata, 
                                                                  0, u'None')
                            
                            if 'codLotacao' in dir(dadosAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosAmbiente.codLotacao', 
                                                                  dadosAmbiente.codLotacao.cdata, 
                                                                  0, u'None')
            
            if 'alteracao' in dir(infoAmbiente.alteracao):
                for alteracao in infoAmbiente.alteracao:
                    
                    if 'ideAmbiente' in dir(alteracao.ideAmbiente):
                        for ideAmbiente in alteracao.ideAmbiente:
                            
                            if 'codAmb' in dir(ideAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideAmbiente.codAmb', 
                                                                  ideAmbiente.codAmb.cdata, 
                                                                  1, u'None')
                            
                            if 'iniValid' in dir(ideAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideAmbiente.iniValid', 
                                                                  ideAmbiente.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideAmbiente.fimValid', 
                                                                  ideAmbiente.fimValid.cdata, 
                                                                  0, u'None')
                    
                    if 'dadosAmbiente' in dir(alteracao.dadosAmbiente):
                        for dadosAmbiente in alteracao.dadosAmbiente:
                            
                            if 'nmAmb' in dir(dadosAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosAmbiente.nmAmb', 
                                                                  dadosAmbiente.nmAmb.cdata, 
                                                                  1, u'None')
                            
                            if 'dscAmb' in dir(dadosAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosAmbiente.dscAmb', 
                                                                  dadosAmbiente.dscAmb.cdata, 
                                                                  1, u'None')
                            
                            if 'localAmb' in dir(dadosAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosAmbiente.localAmb', 
                                                                  dadosAmbiente.localAmb.cdata, 
                                                                  1, u'1, 2, 3')
                            
                            if 'tpInsc' in dir(dadosAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosAmbiente.tpInsc', 
                                                                  dadosAmbiente.tpInsc.cdata, 
                                                                  0, u'1, 2, 3, 4, 5')
                            
                            if 'nrInsc' in dir(dadosAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosAmbiente.nrInsc', 
                                                                  dadosAmbiente.nrInsc.cdata, 
                                                                  0, u'None')
                            
                            if 'codLotacao' in dir(dadosAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosAmbiente.codLotacao', 
                                                                  dadosAmbiente.codLotacao.cdata, 
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
            
            if 'exclusao' in dir(infoAmbiente.exclusao):
                for exclusao in infoAmbiente.exclusao:
                    
                    if 'ideAmbiente' in dir(exclusao.ideAmbiente):
                        for ideAmbiente in exclusao.ideAmbiente:
                            
                            if 'codAmb' in dir(ideAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideAmbiente.codAmb', 
                                                                  ideAmbiente.codAmb.cdata, 
                                                                  1, u'None')
                            
                            if 'iniValid' in dir(ideAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideAmbiente.iniValid', 
                                                                  ideAmbiente.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideAmbiente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideAmbiente.fimValid', 
                                                                  ideAmbiente.fimValid.cdata, 
                                                                  0, u'None')
    return validacoes_lista