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


def validacoes_s2221_evttoxic(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtToxic = doc.eSocial.evtToxic
    #variaveis
    
    if 'ideEvento' in dir(evtToxic.ideEvento):
        for ideEvento in evtToxic.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtToxic.ideEmpregador):
        for ideEmpregador in evtToxic.ideEmpregador:
            
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
    
    if 'ideVinculo' in dir(evtToxic.ideVinculo):
        for ideVinculo in evtToxic.ideVinculo:
            
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
                                                  0, u'101, 102, 103, 104, 105, 106, 111, 201, 202, 301, 302, 303, 305, 306, 307, 308, 309, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 751, 761, 771, 781, 901, 902, 903, 904, 905')
    
    if 'toxicologico' in dir(evtToxic.toxicologico):
        for toxicologico in evtToxic.toxicologico:
            
            if 'dtExame' in dir(toxicologico):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'toxicologico.dtExame', 
                                                  toxicologico.dtExame.cdata, 
                                                  1, u'None')
            
            if 'cnpjLab' in dir(toxicologico):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'toxicologico.cnpjLab', 
                                                  toxicologico.cnpjLab.cdata, 
                                                  0, u'None')
            
            if 'codSeqExame' in dir(toxicologico):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'toxicologico.codSeqExame', 
                                                  toxicologico.codSeqExame.cdata, 
                                                  0, u'None')
            
            if 'nmMed' in dir(toxicologico):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'toxicologico.nmMed', 
                                                  toxicologico.nmMed.cdata, 
                                                  0, u'None')
            
            if 'nrCRM' in dir(toxicologico):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'toxicologico.nrCRM', 
                                                  toxicologico.nrCRM.cdata, 
                                                  0, u'None')
            
            if 'ufCRM' in dir(toxicologico):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'toxicologico.ufCRM', 
                                                  toxicologico.ufCRM.cdata, 
                                                  0, u'None')
            
            if 'indRecusa' in dir(toxicologico):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'toxicologico.indRecusa', 
                                                  toxicologico.indRecusa.cdata, 
                                                  1, u'S, N')
    return validacoes_lista