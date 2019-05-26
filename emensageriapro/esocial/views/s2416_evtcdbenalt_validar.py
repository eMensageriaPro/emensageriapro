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


def validacoes_s2416_evtcdbenalt(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtCdBenAlt = doc.eSocial.evtCdBenAlt
    #variaveis
    
    if 'ideEvento' in dir(evtCdBenAlt.ideEvento):
        for ideEvento in evtCdBenAlt.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtCdBenAlt.ideEmpregador):
        for ideEmpregador in evtCdBenAlt.ideEmpregador:
            
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
    
    if 'ideBeneficio' in dir(evtCdBenAlt.ideBeneficio):
        for ideBeneficio in evtCdBenAlt.ideBeneficio:
            
            if 'cpfBenef' in dir(ideBeneficio):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideBeneficio.cpfBenef', 
                                                  ideBeneficio.cpfBenef.cdata, 
                                                  1, u'None')
            
            if 'nrBeneficio' in dir(ideBeneficio):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideBeneficio.nrBeneficio', 
                                                  ideBeneficio.nrBeneficio.cdata, 
                                                  1, u'None')
    
    if 'infoBenAlteracao' in dir(evtCdBenAlt.infoBenAlteracao):
        for infoBenAlteracao in evtCdBenAlt.infoBenAlteracao:
            
            if 'dtAltBeneficio' in dir(infoBenAlteracao):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoBenAlteracao.dtAltBeneficio', 
                                                  infoBenAlteracao.dtAltBeneficio.cdata, 
                                                  1, u'None')
            
            if 'dadosBeneficio' in dir(infoBenAlteracao.dadosBeneficio):
                for dadosBeneficio in infoBenAlteracao.dadosBeneficio:
                    
                    if 'tpBeneficio' in dir(dadosBeneficio):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosBeneficio.tpBeneficio', 
                                                          dadosBeneficio.tpBeneficio.cdata, 
                                                          1, u'1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 91, 92, 93, 94, 95, 96, 97, 98, 99')
                    
                    if 'tpPlanRP' in dir(dadosBeneficio):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosBeneficio.tpPlanRP', 
                                                          dadosBeneficio.tpPlanRP.cdata, 
                                                          1, u'0, 1, 2, 3')
                    
                    if 'dsc' in dir(dadosBeneficio):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosBeneficio.dsc', 
                                                          dadosBeneficio.dsc.cdata, 
                                                          0, u'None')
                    
                    if 'indDecJud' in dir(dadosBeneficio):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosBeneficio.indDecJud', 
                                                          dadosBeneficio.indDecJud.cdata, 
                                                          1, u'S, N')
                    
                    if 'indHomologTC' in dir(dadosBeneficio):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosBeneficio.indHomologTC', 
                                                          dadosBeneficio.indHomologTC.cdata, 
                                                          1, u'S, N')
                    
                    if 'indSuspensao' in dir(dadosBeneficio):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosBeneficio.indSuspensao', 
                                                          dadosBeneficio.indSuspensao.cdata, 
                                                          1, u'S, N')
                    
                    if 'infoPenMorte' in dir(dadosBeneficio.infoPenMorte):
                        for infoPenMorte in dadosBeneficio.infoPenMorte:
                            
                            if 'tpPenMorte' in dir(infoPenMorte):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoPenMorte.tpPenMorte', 
                                                                  infoPenMorte.tpPenMorte.cdata, 
                                                                  1, u'1, 2')
                    
                    if 'homologTC' in dir(dadosBeneficio.homologTC):
                        for homologTC in dadosBeneficio.homologTC:
                            
                            if 'nrAtoLegal' in dir(homologTC):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'homologTC.nrAtoLegal', 
                                                                  homologTC.nrAtoLegal.cdata, 
                                                                  1, u'None')
                    
                    if 'suspensao' in dir(dadosBeneficio.suspensao):
                        for suspensao in dadosBeneficio.suspensao:
                            
                            if 'mtvSuspensao' in dir(suspensao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'suspensao.mtvSuspensao', 
                                                                  suspensao.mtvSuspensao.cdata, 
                                                                  1, u'01, 99')
                            
                            if 'dscSuspensao' in dir(suspensao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'suspensao.dscSuspensao', 
                                                                  suspensao.dscSuspensao.cdata, 
                                                                  0, u'None')
    return validacoes_lista