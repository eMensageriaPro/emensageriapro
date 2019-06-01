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


def validacoes_s2245_evttreicap(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTreiCap = doc.eSocial.evtTreiCap
    #variaveis
    
    if 'ideEvento' in dir(evtTreiCap.ideEvento):
        for ideEvento in evtTreiCap.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtTreiCap.ideEmpregador):
        for ideEmpregador in evtTreiCap.ideEmpregador:
            
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
    
    if 'ideVinculo' in dir(evtTreiCap.ideVinculo):
        for ideVinculo in evtTreiCap.ideVinculo:
            
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
    
    if 'treiCap' in dir(evtTreiCap.treiCap):
        for treiCap in evtTreiCap.treiCap:
            
            if 'codTreiCap' in dir(treiCap):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'treiCap.codTreiCap', 
                                                  treiCap.codTreiCap.cdata, 
                                                  1, u'3203, 3204, 3205, 3206, 3207, 3208, 3209, 3210, 3211, 3212, 3213, 3214, 3215, 3299, 3401, 3402, 3403, 3404, 3405, 3406, 3407, 3408, 3409, 3410, 3411, 3412, 3413, 3414, 3415, 3416, 3501, 3502, 3503, 3504, 1006, 1207, 0101, 0501, 0502, 0601, 0701, 0901, 0902, 0903, 0904, 1001, 1002, 1003, 1004, 1005, 1101, 1102, 1103, 1104, 1201, 1202, 1203, 1204, 1205, 1206, 1301, 1302, 1303, 1304, 1305, 1501, 1502, 1503, 1701, 1702, 1703, 1704, 1705, 1706, 1801, 1802, 1803, 1804, 1805, 1806, 1807, 1808, 1809, 1810, 1811, 1812, 1813, 1814, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2201, 2202, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2301, 2302, 2303, 2501, 2601, 2901, 2902, 2903, 3001, 3002, 3003, 3004, 3005, 3101, 3102, 3103, 3104, 3105, 3106, 3107, 3108, 3109, 3201, 3202, 3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308, 3309, 3310, 3417, 3601, 3602, 3603, 3604, 3605, 0097, 0098, 0099')
            
            if 'obsTreiCap' in dir(treiCap):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'treiCap.obsTreiCap', 
                                                  treiCap.obsTreiCap.cdata, 
                                                  0, u'None')
            
            if 'observacao' in dir(treiCap):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'treiCap.observacao', 
                                                  treiCap.observacao.cdata, 
                                                  0, u'None')
            
            if 'infoComplem' in dir(treiCap.infoComplem):
                for infoComplem in treiCap.infoComplem:
                    
                    if 'dtTreiCap' in dir(infoComplem):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoComplem.dtTreiCap', 
                                                          infoComplem.dtTreiCap.cdata, 
                                                          1, u'None')
                    
                    if 'durTreiCap' in dir(infoComplem):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoComplem.durTreiCap', 
                                                          infoComplem.durTreiCap.cdata, 
                                                          0, u'None')
                    
                    if 'modTreiCap' in dir(infoComplem):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoComplem.modTreiCap', 
                                                          infoComplem.modTreiCap.cdata, 
                                                          0, u'1, 2, 3')
                    
                    if 'tpTreiCap' in dir(infoComplem):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoComplem.tpTreiCap', 
                                                          infoComplem.tpTreiCap.cdata, 
                                                          0, u'1, 2, 3, 4, 5')
                    
                    if 'indTreinAnt' in dir(infoComplem):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoComplem.indTreinAnt', 
                                                          infoComplem.indTreinAnt.cdata, 
                                                          1, u'S, N')
                    
                    if 'ideProfResp' in dir(infoComplem.ideProfResp):
                        for ideProfResp in infoComplem.ideProfResp:
                            
                            if 'cpfProf' in dir(ideProfResp):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProfResp.cpfProf', 
                                                                  ideProfResp.cpfProf.cdata, 
                                                                  0, u'None')
                            
                            if 'nmProf' in dir(ideProfResp):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProfResp.nmProf', 
                                                                  ideProfResp.nmProf.cdata, 
                                                                  1, u'None')
                            
                            if 'tpProf' in dir(ideProfResp):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProfResp.tpProf', 
                                                                  ideProfResp.tpProf.cdata, 
                                                                  1, u'1, 2')
                            
                            if 'formProf' in dir(ideProfResp):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProfResp.formProf', 
                                                                  ideProfResp.formProf.cdata, 
                                                                  1, u'None')
                            
                            if 'codCBO' in dir(ideProfResp):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProfResp.codCBO', 
                                                                  ideProfResp.codCBO.cdata, 
                                                                  1, u'None')
                            
                            if 'nacProf' in dir(ideProfResp):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProfResp.nacProf', 
                                                                  ideProfResp.nacProf.cdata, 
                                                                  1, u'1, 2')
    return validacoes_lista