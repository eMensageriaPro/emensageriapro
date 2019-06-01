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


def validacoes_s3000_evtexclusao(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtExclusao = doc.eSocial.evtExclusao
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
                                                  1, u'1, 2, 3, 4, 5')
            
            if 'verProc' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.verProc', 
                                                  ideEvento.verProc.cdata, 
                                                  1, u'None')
    
    if 'ideEmpregador' in dir(evtExclusao.ideEmpregador):
        for ideEmpregador in evtExclusao.ideEmpregador:
            
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
    
    if 'infoExclusao' in dir(evtExclusao.infoExclusao):
        for infoExclusao in evtExclusao.infoExclusao:
            
            if 'tpEvento' in dir(infoExclusao):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoExclusao.tpEvento', 
                                                  infoExclusao.tpEvento.cdata, 
                                                  1, u'S-1000, S-1005, S-1010, S-1020, S-1030, S-1035, S-1040, S-1050, S-1060, S-1070, S-1080, S-1200, S-1202, S-1207, S-1210, S-1250, S-1260, S-1270, S-1280, S-1295, S-1298, S-1299, S-1300, S-2190, S-2200, S-2205, S-2206, S-2210, S-2220, S-2221, S-2230, S-2240, S-2245, S-2250, S-2260, S-2298, S-2299, S-2300, S-2306, S-2399, S-2400, S-3000, S-5001, S-5002, S-5003, S-5011, S-5012, S-5013')
            
            if 'nrRecEvt' in dir(infoExclusao):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoExclusao.nrRecEvt', 
                                                  infoExclusao.nrRecEvt.cdata, 
                                                  1, u'None')
            
            if 'ideTrabalhador' in dir(infoExclusao.ideTrabalhador):
                for ideTrabalhador in infoExclusao.ideTrabalhador:
                    
                    if 'cpfTrab' in dir(ideTrabalhador):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideTrabalhador.cpfTrab', 
                                                          ideTrabalhador.cpfTrab.cdata, 
                                                          1, u'None')
                    
                    if 'nisTrab' in dir(ideTrabalhador):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideTrabalhador.nisTrab', 
                                                          ideTrabalhador.nisTrab.cdata, 
                                                          0, u'None')
            
            if 'ideFolhaPagto' in dir(infoExclusao.ideFolhaPagto):
                for ideFolhaPagto in infoExclusao.ideFolhaPagto:
                    
                    if 'indApuracao' in dir(ideFolhaPagto):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideFolhaPagto.indApuracao', 
                                                          ideFolhaPagto.indApuracao.cdata, 
                                                          1, u'1, 2')
                    
                    if 'perApur' in dir(ideFolhaPagto):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideFolhaPagto.perApur', 
                                                          ideFolhaPagto.perApur.cdata, 
                                                          1, u'None')
    return validacoes_lista