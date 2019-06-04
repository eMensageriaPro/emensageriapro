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


def validacoes_s1299_evtfechaevper(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtFechaEvPer = doc.eSocial.evtFechaEvPer
    #variaveis
    
    if 'ideEvento' in dir(evtFechaEvPer.ideEvento):
        for ideEvento in evtFechaEvPer.ideEvento:
            
            if 'indApuracao' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.indApuracao', 
                                                  ideEvento.indApuracao.cdata, 
                                                  1, u'1, 2')
            
            if 'perApur' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.perApur', 
                                                  ideEvento.perApur.cdata, 
                                                  1, u'None')
            
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
    
    if 'ideEmpregador' in dir(evtFechaEvPer.ideEmpregador):
        for ideEmpregador in evtFechaEvPer.ideEmpregador:
            
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
    
    if 'ideRespInf' in dir(evtFechaEvPer.ideRespInf):
        for ideRespInf in evtFechaEvPer.ideRespInf:
            
            if 'nmResp' in dir(ideRespInf):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideRespInf.nmResp', 
                                                  ideRespInf.nmResp.cdata, 
                                                  1, u'None')
            
            if 'cpfResp' in dir(ideRespInf):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideRespInf.cpfResp', 
                                                  ideRespInf.cpfResp.cdata, 
                                                  1, u'None')
            
            if 'telefone' in dir(ideRespInf):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideRespInf.telefone', 
                                                  ideRespInf.telefone.cdata, 
                                                  1, u'None')
            
            if 'email' in dir(ideRespInf):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideRespInf.email', 
                                                  ideRespInf.email.cdata, 
                                                  0, u'None')
    
    if 'infoFech' in dir(evtFechaEvPer.infoFech):
        for infoFech in evtFechaEvPer.infoFech:
            
            if 'evtRemun' in dir(infoFech):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoFech.evtRemun', 
                                                  infoFech.evtRemun.cdata, 
                                                  1, u'S, N')
            
            if 'evtPgtos' in dir(infoFech):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoFech.evtPgtos', 
                                                  infoFech.evtPgtos.cdata, 
                                                  1, u'S, N')
            
            if 'evtAqProd' in dir(infoFech):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoFech.evtAqProd', 
                                                  infoFech.evtAqProd.cdata, 
                                                  1, u'S, N')
            
            if 'evtComProd' in dir(infoFech):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoFech.evtComProd', 
                                                  infoFech.evtComProd.cdata, 
                                                  1, u'S, N')
            
            if 'evtContratAvNP' in dir(infoFech):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoFech.evtContratAvNP', 
                                                  infoFech.evtContratAvNP.cdata, 
                                                  1, u'S, N')
            
            if 'evtInfoComplPer' in dir(infoFech):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoFech.evtInfoComplPer', 
                                                  infoFech.evtInfoComplPer.cdata, 
                                                  1, u'S, N')
            
            if 'compSemMovto' in dir(infoFech):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoFech.compSemMovto', 
                                                  infoFech.compSemMovto.cdata, 
                                                  0, u'None')
    return validacoes_lista