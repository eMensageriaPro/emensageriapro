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


def validacoes_s5012_evtirrf(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtIrrf = doc.eSocial.evtIrrf
    #variaveis
    
    if 'ideEvento' in dir(evtIrrf.ideEvento):
        for ideEvento in evtIrrf.ideEvento:
            
            if 'perApur' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.perApur', 
                                                  ideEvento.perApur.cdata, 
                                                  1, u'None')
    
    if 'ideEmpregador' in dir(evtIrrf.ideEmpregador):
        for ideEmpregador in evtIrrf.ideEmpregador:
            
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
    
    if 'infoIRRF' in dir(evtIrrf.infoIRRF):
        for infoIRRF in evtIrrf.infoIRRF:
            
            if 'nrRecArqBase' in dir(infoIRRF):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoIRRF.nrRecArqBase', 
                                                  infoIRRF.nrRecArqBase.cdata, 
                                                  1, u'None')
            
            if 'indExistInfo' in dir(infoIRRF):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoIRRF.indExistInfo', 
                                                  infoIRRF.indExistInfo.cdata, 
                                                  1, u'None')
            
            if 'infoCRContrib' in dir(infoIRRF.infoCRContrib):
                for infoCRContrib in infoIRRF.infoCRContrib:
                    
                    if 'tpCR' in dir(infoCRContrib):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoCRContrib.tpCR', 
                                                          infoCRContrib.tpCR.cdata, 
                                                          1, u'None')
                    
                    if 'vrCR' in dir(infoCRContrib):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoCRContrib.vrCR', 
                                                          infoCRContrib.vrCR.cdata, 
                                                          1, u'None')
    return validacoes_lista