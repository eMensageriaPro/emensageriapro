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


def validacoes_r9000_evtexclusao(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtExclusao = doc.Reinf.evtExclusao
    #variaveis
    
    if 'ideEvento' in dir(evtExclusao.ideEvento):
        for ideEvento in evtExclusao.ideEvento:
            
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
    
    if 'ideContri' in dir(evtExclusao.ideContri):
        for ideContri in evtExclusao.ideContri:
            
            if 'tpInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.tpInsc', 
                                                  ideContri.tpInsc.cdata, 
                                                  1, u'1, 2')
            
            if 'nrInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.nrInsc', 
                                                  ideContri.nrInsc.cdata, 
                                                  1, u'None')
    
    if 'infoExclusao' in dir(evtExclusao.infoExclusao):
        for infoExclusao in evtExclusao.infoExclusao:
            
            if 'tpEvento' in dir(infoExclusao):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoExclusao.tpEvento', 
                                                  infoExclusao.tpEvento.cdata, 
                                                  1, u'R-1000, R-1070, R-2010, R-2020, R-2030, R-2040, R-2050, R-2060, R-2098, R-2099, R-3010, R-4010, R-4020, R-4040, R-4098, R-4099, R-9000, R-9001, R-9002, R-9011, R-9012')
            
            if 'nrRecEvt' in dir(infoExclusao):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoExclusao.nrRecEvt', 
                                                  infoExclusao.nrRecEvt.cdata, 
                                                  1, u'None')
            
            if 'perApur' in dir(infoExclusao):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoExclusao.perApur', 
                                                  infoExclusao.perApur.cdata, 
                                                  1, u'None')
    return validacoes_lista