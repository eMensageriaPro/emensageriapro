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


def validacoes_s2230_evtafasttemp(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtAfastTemp = doc.eSocial.evtAfastTemp
    #variaveis
    
    if 'ideEvento' in dir(evtAfastTemp.ideEvento):
        for ideEvento in evtAfastTemp.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtAfastTemp.ideEmpregador):
        for ideEmpregador in evtAfastTemp.ideEmpregador:
            
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
    
    if 'ideVinculo' in dir(evtAfastTemp.ideVinculo):
        for ideVinculo in evtAfastTemp.ideVinculo:
            
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
                                                  0, u'None')
    
    if 'infoAfastamento' in dir(evtAfastTemp.infoAfastamento):
        for infoAfastamento in evtAfastTemp.infoAfastamento:
            
            if 'iniAfastamento' in dir(infoAfastamento.iniAfastamento):
                for iniAfastamento in infoAfastamento.iniAfastamento:
                    
                    if 'dtIniAfast' in dir(iniAfastamento):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'iniAfastamento.dtIniAfast', 
                                                          iniAfastamento.dtIniAfast.cdata, 
                                                          1, u'None')
                    
                    if 'codMotAfast' in dir(iniAfastamento):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'iniAfastamento.codMotAfast', 
                                                          iniAfastamento.codMotAfast.cdata, 
                                                          1, u'01, 03, 05, 06, 07, 08, 10, 11, 12, 13, 14, 15, 16, 17, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35')
                    
                    if 'infoMesmoMtv' in dir(iniAfastamento):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'iniAfastamento.infoMesmoMtv', 
                                                          iniAfastamento.infoMesmoMtv.cdata, 
                                                          0, u'S, N')
                    
                    if 'tpAcidTransito' in dir(iniAfastamento):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'iniAfastamento.tpAcidTransito', 
                                                          iniAfastamento.tpAcidTransito.cdata, 
                                                          0, u'1, 2, 3')
                    
                    if 'observacao' in dir(iniAfastamento):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'iniAfastamento.observacao', 
                                                          iniAfastamento.observacao.cdata, 
                                                          0, u'None')
                    
                    if 'infoAtestado' in dir(iniAfastamento.infoAtestado):
                        for infoAtestado in iniAfastamento.infoAtestado:
                            
                            if 'codCID' in dir(infoAtestado):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoAtestado.codCID', 
                                                                  infoAtestado.codCID.cdata, 
                                                                  0, u'None')
                            
                            if 'qtdDiasAfast' in dir(infoAtestado):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoAtestado.qtdDiasAfast', 
                                                                  infoAtestado.qtdDiasAfast.cdata, 
                                                                  1, u'None')
                            
                            if 'emitente' in dir(infoAtestado.emitente):
                                for emitente in infoAtestado.emitente:
                                    
                                    if 'nmEmit' in dir(emitente):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'emitente.nmEmit', 
                                                                          emitente.nmEmit.cdata, 
                                                                          1, u'None')
                                    
                                    if 'ideOC' in dir(emitente):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'emitente.ideOC', 
                                                                          emitente.ideOC.cdata, 
                                                                          1, u'1, 2, 3')
                                    
                                    if 'nrOc' in dir(emitente):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'emitente.nrOc', 
                                                                          emitente.nrOc.cdata, 
                                                                          1, u'None')
                                    
                                    if 'ufOC' in dir(emitente):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'emitente.ufOC', 
                                                                          emitente.ufOC.cdata, 
                                                                          0, u'None')
                    
                    if 'infoCessao' in dir(iniAfastamento.infoCessao):
                        for infoCessao in iniAfastamento.infoCessao:
                            
                            if 'cnpjCess' in dir(infoCessao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCessao.cnpjCess', 
                                                                  infoCessao.cnpjCess.cdata, 
                                                                  1, u'None')
                            
                            if 'infOnus' in dir(infoCessao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCessao.infOnus', 
                                                                  infoCessao.infOnus.cdata, 
                                                                  1, u'1, 2, 3')
                    
                    if 'infoMandSind' in dir(iniAfastamento.infoMandSind):
                        for infoMandSind in iniAfastamento.infoMandSind:
                            
                            if 'cnpjSind' in dir(infoMandSind):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoMandSind.cnpjSind', 
                                                                  infoMandSind.cnpjSind.cdata, 
                                                                  1, u'None')
                            
                            if 'infOnusRemun' in dir(infoMandSind):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoMandSind.infOnusRemun', 
                                                                  infoMandSind.infOnusRemun.cdata, 
                                                                  1, u'1, 2, 3')
            
            if 'infoRetif' in dir(infoAfastamento.infoRetif):
                for infoRetif in infoAfastamento.infoRetif:
                    
                    if 'origRetif' in dir(infoRetif):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoRetif.origRetif', 
                                                          infoRetif.origRetif.cdata, 
                                                          1, u'1, 2, 3')
                    
                    if 'tpProc' in dir(infoRetif):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoRetif.tpProc', 
                                                          infoRetif.tpProc.cdata, 
                                                          0, u'1, 2, 3')
                    
                    if 'nrProc' in dir(infoRetif):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoRetif.nrProc', 
                                                          infoRetif.nrProc.cdata, 
                                                          0, u'None')
            
            if 'fimAfastamento' in dir(infoAfastamento.fimAfastamento):
                for fimAfastamento in infoAfastamento.fimAfastamento:
                    
                    if 'dtTermAfast' in dir(fimAfastamento):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fimAfastamento.dtTermAfast', 
                                                          fimAfastamento.dtTermAfast.cdata, 
                                                          1, u'None')
    return validacoes_lista