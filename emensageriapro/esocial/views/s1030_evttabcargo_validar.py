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


def validacoes_s1030_evttabcargo(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabCargo = doc.eSocial.evtTabCargo
    #variaveis
    
    if 'ideEvento' in dir(evtTabCargo.ideEvento):
        for ideEvento in evtTabCargo.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtTabCargo.ideEmpregador):
        for ideEmpregador in evtTabCargo.ideEmpregador:
            
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
    
    if 'infoCargo' in dir(evtTabCargo.infoCargo):
        for infoCargo in evtTabCargo.infoCargo:
            
            if 'inclusao' in dir(infoCargo.inclusao):
                for inclusao in infoCargo.inclusao:
                    
                    if 'ideCargo' in dir(inclusao.ideCargo):
                        for ideCargo in inclusao.ideCargo:
                            
                            if 'codCargo' in dir(ideCargo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCargo.codCargo', 
                                                                  ideCargo.codCargo.cdata, 
                                                                  1, u'None')
                            
                            if 'iniValid' in dir(ideCargo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCargo.iniValid', 
                                                                  ideCargo.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideCargo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCargo.fimValid', 
                                                                  ideCargo.fimValid.cdata, 
                                                                  0, u'None')
                    
                    if 'dadosCargo' in dir(inclusao.dadosCargo):
                        for dadosCargo in inclusao.dadosCargo:
                            
                            if 'nmCargo' in dir(dadosCargo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosCargo.nmCargo', 
                                                                  dadosCargo.nmCargo.cdata, 
                                                                  1, u'None')
                            
                            if 'codCBO' in dir(dadosCargo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosCargo.codCBO', 
                                                                  dadosCargo.codCBO.cdata, 
                                                                  1, u'None')
                            
                            if 'cargoPublico' in dir(dadosCargo.cargoPublico):
                                for cargoPublico in dadosCargo.cargoPublico:
                                    
                                    if 'acumCargo' in dir(cargoPublico):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'cargoPublico.acumCargo', 
                                                                          cargoPublico.acumCargo.cdata, 
                                                                          1, u'1, 2, 3, 4')
                                    
                                    if 'contagemEsp' in dir(cargoPublico):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'cargoPublico.contagemEsp', 
                                                                          cargoPublico.contagemEsp.cdata, 
                                                                          1, u'1, 2, 3, 4')
                                    
                                    if 'dedicExcl' in dir(cargoPublico):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'cargoPublico.dedicExcl', 
                                                                          cargoPublico.dedicExcl.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'codCarreira' in dir(cargoPublico):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'cargoPublico.codCarreira', 
                                                                          cargoPublico.codCarreira.cdata, 
                                                                          0, u'None')
                                    
                                    if 'leiCargo' in dir(cargoPublico.leiCargo):
                                        for leiCargo in cargoPublico.leiCargo:
                                            
                                            if 'nrLei' in dir(leiCargo):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'leiCargo.nrLei', 
                                                                                  leiCargo.nrLei.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'dtLei' in dir(leiCargo):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'leiCargo.dtLei', 
                                                                                  leiCargo.dtLei.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'sitCargo' in dir(leiCargo):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'leiCargo.sitCargo', 
                                                                                  leiCargo.sitCargo.cdata, 
                                                                                  1, u'1, 2, 3')
            
            if 'alteracao' in dir(infoCargo.alteracao):
                for alteracao in infoCargo.alteracao:
                    
                    if 'ideCargo' in dir(alteracao.ideCargo):
                        for ideCargo in alteracao.ideCargo:
                            
                            if 'codCargo' in dir(ideCargo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCargo.codCargo', 
                                                                  ideCargo.codCargo.cdata, 
                                                                  1, u'None')
                            
                            if 'iniValid' in dir(ideCargo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCargo.iniValid', 
                                                                  ideCargo.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideCargo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCargo.fimValid', 
                                                                  ideCargo.fimValid.cdata, 
                                                                  0, u'None')
                    
                    if 'dadosCargo' in dir(alteracao.dadosCargo):
                        for dadosCargo in alteracao.dadosCargo:
                            
                            if 'nmCargo' in dir(dadosCargo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosCargo.nmCargo', 
                                                                  dadosCargo.nmCargo.cdata, 
                                                                  1, u'None')
                            
                            if 'codCBO' in dir(dadosCargo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosCargo.codCBO', 
                                                                  dadosCargo.codCBO.cdata, 
                                                                  1, u'None')
                            
                            if 'cargoPublico' in dir(dadosCargo.cargoPublico):
                                for cargoPublico in dadosCargo.cargoPublico:
                                    
                                    if 'acumCargo' in dir(cargoPublico):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'cargoPublico.acumCargo', 
                                                                          cargoPublico.acumCargo.cdata, 
                                                                          1, u'1, 2, 3, 4')
                                    
                                    if 'contagemEsp' in dir(cargoPublico):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'cargoPublico.contagemEsp', 
                                                                          cargoPublico.contagemEsp.cdata, 
                                                                          1, u'1, 2, 3, 4')
                                    
                                    if 'dedicExcl' in dir(cargoPublico):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'cargoPublico.dedicExcl', 
                                                                          cargoPublico.dedicExcl.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'codCarreira' in dir(cargoPublico):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'cargoPublico.codCarreira', 
                                                                          cargoPublico.codCarreira.cdata, 
                                                                          0, u'None')
                                    
                                    if 'leiCargo' in dir(cargoPublico.leiCargo):
                                        for leiCargo in cargoPublico.leiCargo:
                                            
                                            if 'nrLei' in dir(leiCargo):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'leiCargo.nrLei', 
                                                                                  leiCargo.nrLei.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'dtLei' in dir(leiCargo):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'leiCargo.dtLei', 
                                                                                  leiCargo.dtLei.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'sitCargo' in dir(leiCargo):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'leiCargo.sitCargo', 
                                                                                  leiCargo.sitCargo.cdata, 
                                                                                  1, u'1, 2, 3')
                    
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
            
            if 'exclusao' in dir(infoCargo.exclusao):
                for exclusao in infoCargo.exclusao:
                    
                    if 'ideCargo' in dir(exclusao.ideCargo):
                        for ideCargo in exclusao.ideCargo:
                            
                            if 'codCargo' in dir(ideCargo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCargo.codCargo', 
                                                                  ideCargo.codCargo.cdata, 
                                                                  1, u'None')
                            
                            if 'iniValid' in dir(ideCargo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCargo.iniValid', 
                                                                  ideCargo.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideCargo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCargo.fimValid', 
                                                                  ideCargo.fimValid.cdata, 
                                                                  0, u'None')
    return validacoes_lista