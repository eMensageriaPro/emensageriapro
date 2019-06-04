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


def validacoes_s1250_evtaqprod(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtAqProd = doc.eSocial.evtAqProd
    #variaveis
    
    if 'ideEvento' in dir(evtAqProd.ideEvento):
        for ideEvento in evtAqProd.ideEvento:
            
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
            
            if 'indApuracao' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.indApuracao', 
                                                  ideEvento.indApuracao.cdata, 
                                                  1, u'1')
            
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
    
    if 'ideEmpregador' in dir(evtAqProd.ideEmpregador):
        for ideEmpregador in evtAqProd.ideEmpregador:
            
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
    
    if 'infoAquisProd' in dir(evtAqProd.infoAquisProd):
        for infoAquisProd in evtAqProd.infoAquisProd:
            
            if 'ideEstabAdquir' in dir(infoAquisProd.ideEstabAdquir):
                for ideEstabAdquir in infoAquisProd.ideEstabAdquir:
                    
                    if 'tpInscAdq' in dir(ideEstabAdquir):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstabAdquir.tpInscAdq', 
                                                          ideEstabAdquir.tpInscAdq.cdata, 
                                                          1, u'1, 2, 3, 4, 5')
                    
                    if 'nrInscAdq' in dir(ideEstabAdquir):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstabAdquir.nrInscAdq', 
                                                          ideEstabAdquir.nrInscAdq.cdata, 
                                                          1, u'None')
                    
                    if 'tpAquis' in dir(ideEstabAdquir.tpAquis):
                        for tpAquis in ideEstabAdquir.tpAquis:
                            
                            if 'indAquis' in dir(tpAquis):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'tpAquis.indAquis', 
                                                                  tpAquis.indAquis.cdata, 
                                                                  1, u'1, 2, 3, 4, 5, 6')
                            
                            if 'vlrTotAquis' in dir(tpAquis):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'tpAquis.vlrTotAquis', 
                                                                  tpAquis.vlrTotAquis.cdata, 
                                                                  1, u'None')
                            
                            if 'ideProdutor' in dir(tpAquis.ideProdutor):
                                for ideProdutor in tpAquis.ideProdutor:
                                    
                                    if 'tpInscProd' in dir(ideProdutor):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProdutor.tpInscProd', 
                                                                          ideProdutor.tpInscProd.cdata, 
                                                                          1, u'1, 2')
                                    
                                    if 'nrInscProd' in dir(ideProdutor):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProdutor.nrInscProd', 
                                                                          ideProdutor.nrInscProd.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vlrBruto' in dir(ideProdutor):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProdutor.vlrBruto', 
                                                                          ideProdutor.vlrBruto.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vrCPDescPR' in dir(ideProdutor):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProdutor.vrCPDescPR', 
                                                                          ideProdutor.vrCPDescPR.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vrRatDescPR' in dir(ideProdutor):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProdutor.vrRatDescPR', 
                                                                          ideProdutor.vrRatDescPR.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vrSenarDesc' in dir(ideProdutor):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProdutor.vrSenarDesc', 
                                                                          ideProdutor.vrSenarDesc.cdata, 
                                                                          1, u'None')
                                    
                                    if 'indOpcCP' in dir(ideProdutor):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideProdutor.indOpcCP', 
                                                                          ideProdutor.indOpcCP.cdata, 
                                                                          1, u'1, 2')
                                    
                                    if 'nfs' in dir(ideProdutor.nfs):
                                        for nfs in ideProdutor.nfs:
                                            
                                            if 'serie' in dir(nfs):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'nfs.serie', 
                                                                                  nfs.serie.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'nrDocto' in dir(nfs):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'nfs.nrDocto', 
                                                                                  nfs.nrDocto.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'dtEmisNF' in dir(nfs):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'nfs.dtEmisNF', 
                                                                                  nfs.dtEmisNF.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vlrBruto' in dir(nfs):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'nfs.vlrBruto', 
                                                                                  nfs.vlrBruto.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrCPDescPR' in dir(nfs):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'nfs.vrCPDescPR', 
                                                                                  nfs.vrCPDescPR.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrRatDescPR' in dir(nfs):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'nfs.vrRatDescPR', 
                                                                                  nfs.vrRatDescPR.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrSenarDesc' in dir(nfs):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'nfs.vrSenarDesc', 
                                                                                  nfs.vrSenarDesc.cdata, 
                                                                                  1, u'None')
                                    
                                    if 'infoProcJud' in dir(ideProdutor.infoProcJud):
                                        for infoProcJud in ideProdutor.infoProcJud:
                                            
                                            if 'nrProcJud' in dir(infoProcJud):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcJud.nrProcJud', 
                                                                                  infoProcJud.nrProcJud.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'codSusp' in dir(infoProcJud):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcJud.codSusp', 
                                                                                  infoProcJud.codSusp.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrCPNRet' in dir(infoProcJud):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcJud.vrCPNRet', 
                                                                                  infoProcJud.vrCPNRet.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrRatNRet' in dir(infoProcJud):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcJud.vrRatNRet', 
                                                                                  infoProcJud.vrRatNRet.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vrSenarNRet' in dir(infoProcJud):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcJud.vrSenarNRet', 
                                                                                  infoProcJud.vrSenarNRet.cdata, 
                                                                                  1, u'None')
                            
                            if 'infoProcJ' in dir(tpAquis.infoProcJ):
                                for infoProcJ in tpAquis.infoProcJ:
                                    
                                    if 'nrProcJud' in dir(infoProcJ):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcJ.nrProcJud', 
                                                                          infoProcJ.nrProcJud.cdata, 
                                                                          1, u'None')
                                    
                                    if 'codSusp' in dir(infoProcJ):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcJ.codSusp', 
                                                                          infoProcJ.codSusp.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vrCPNRet' in dir(infoProcJ):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcJ.vrCPNRet', 
                                                                          infoProcJ.vrCPNRet.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vrRatNRet' in dir(infoProcJ):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcJ.vrRatNRet', 
                                                                          infoProcJ.vrRatNRet.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vrSenarNRet' in dir(infoProcJ):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcJ.vrSenarNRet', 
                                                                          infoProcJ.vrSenarNRet.cdata, 
                                                                          1, u'None')
    return validacoes_lista