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


def validacoes_r9002_evtret(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtRet = doc.Reinf.evtRet
    #variaveis
    
    if 'ideEvento' in dir(evtRet.ideEvento):
        for ideEvento in evtRet.ideEvento:
            
            if 'perRef' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.perRef', 
                                                  ideEvento.perRef.cdata, 
                                                  1, u'None')
    
    if 'ideContri' in dir(evtRet.ideContri):
        for ideContri in evtRet.ideContri:
            
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
    
    if 'ideRecRetorno' in dir(evtRet.ideRecRetorno):
        for ideRecRetorno in evtRet.ideRecRetorno:
            
            if 'ideStatus' in dir(ideRecRetorno.ideStatus):
                for ideStatus in ideRecRetorno.ideStatus:
                    
                    if 'cdRetorno' in dir(ideStatus):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideStatus.cdRetorno', 
                                                          ideStatus.cdRetorno.cdata, 
                                                          1, u'0, 1, 2')
                    
                    if 'descRetorno' in dir(ideStatus):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideStatus.descRetorno', 
                                                          ideStatus.descRetorno.cdata, 
                                                          1, u'None')
                    
                    if 'regOcorrs' in dir(ideStatus.regOcorrs):
                        for regOcorrs in ideStatus.regOcorrs:
                            
                            if 'tpOcorr' in dir(regOcorrs):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'regOcorrs.tpOcorr', 
                                                                  regOcorrs.tpOcorr.cdata, 
                                                                  1, u'None')
                            
                            if 'localErroAviso' in dir(regOcorrs):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'regOcorrs.localErroAviso', 
                                                                  regOcorrs.localErroAviso.cdata, 
                                                                  1, u'None')
                            
                            if 'codResp' in dir(regOcorrs):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'regOcorrs.codResp', 
                                                                  regOcorrs.codResp.cdata, 
                                                                  1, u'None')
                            
                            if 'dscResp' in dir(regOcorrs):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'regOcorrs.dscResp', 
                                                                  regOcorrs.dscResp.cdata, 
                                                                  1, u'None')
    
    if 'infoRecEv' in dir(evtRet.infoRecEv):
        for infoRecEv in evtRet.infoRecEv:
            
            if 'nrProtEntr' in dir(infoRecEv):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoRecEv.nrProtEntr', 
                                                  infoRecEv.nrProtEntr.cdata, 
                                                  0, u'None')
            
            if 'dhProcess' in dir(infoRecEv):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoRecEv.dhProcess', 
                                                  infoRecEv.dhProcess.cdata, 
                                                  1, u'None')
            
            if 'tpEv' in dir(infoRecEv):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoRecEv.tpEv', 
                                                  infoRecEv.tpEv.cdata, 
                                                  1, u'None')
            
            if 'idEv' in dir(infoRecEv):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoRecEv.idEv', 
                                                  infoRecEv.idEv.cdata, 
                                                  1, u'None')
            
            if 'hash' in dir(infoRecEv):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoRecEv.hash', 
                                                  infoRecEv.hash.cdata, 
                                                  1, u'None')
    
    if 'infoTotal' in dir(evtRet.infoTotal):
        for infoTotal in evtRet.infoTotal:
            
            if 'nrRecArqBase' in dir(infoTotal):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoTotal.nrRecArqBase', 
                                                  infoTotal.nrRecArqBase.cdata, 
                                                  0, u'None')
            
            if 'ideEstab' in dir(infoTotal.ideEstab):
                for ideEstab in infoTotal.ideEstab:
                    
                    if 'tpInsc' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.tpInsc', 
                                                          ideEstab.tpInsc.cdata, 
                                                          1, u'1, 2')
                    
                    if 'nrInsc' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.nrInsc', 
                                                          ideEstab.nrInsc.cdata, 
                                                          1, u'None')
                    
                    if 'totApurMen' in dir(ideEstab.totApurMen):
                        for totApurMen in ideEstab.totApurMen:
                            
                            if 'CRMen' in dir(totApurMen):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurMen.CRMen', 
                                                                  totApurMen.CRMen.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrBaseCRMen' in dir(totApurMen):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurMen.vlrBaseCRMen', 
                                                                  totApurMen.vlrBaseCRMen.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrCRMen' in dir(totApurMen):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurMen.vlrCRMen', 
                                                                  totApurMen.vlrCRMen.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrBaseCRMenSusp' in dir(totApurMen):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurMen.vlrBaseCRMenSusp', 
                                                                  totApurMen.vlrBaseCRMenSusp.cdata, 
                                                                  0, u'None')
                            
                            if 'vlrCRMenSusp' in dir(totApurMen):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurMen.vlrCRMenSusp', 
                                                                  totApurMen.vlrCRMenSusp.cdata, 
                                                                  0, u'None')
                    
                    if 'totApurQui' in dir(ideEstab.totApurQui):
                        for totApurQui in ideEstab.totApurQui:
                            
                            if 'perApurQui' in dir(totApurQui):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurQui.perApurQui', 
                                                                  totApurQui.perApurQui.cdata, 
                                                                  1, u'1, 2')
                            
                            if 'CRQui' in dir(totApurQui):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurQui.CRQui', 
                                                                  totApurQui.CRQui.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrBaseCRQui' in dir(totApurQui):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurQui.vlrBaseCRQui', 
                                                                  totApurQui.vlrBaseCRQui.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrCRQui' in dir(totApurQui):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurQui.vlrCRQui', 
                                                                  totApurQui.vlrCRQui.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrBaseCRQuiSusp' in dir(totApurQui):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurQui.vlrBaseCRQuiSusp', 
                                                                  totApurQui.vlrBaseCRQuiSusp.cdata, 
                                                                  0, u'None')
                            
                            if 'vlrCRQuiSusp' in dir(totApurQui):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurQui.vlrCRQuiSusp', 
                                                                  totApurQui.vlrCRQuiSusp.cdata, 
                                                                  0, u'None')
                    
                    if 'totApurDec' in dir(ideEstab.totApurDec):
                        for totApurDec in ideEstab.totApurDec:
                            
                            if 'perApurDec' in dir(totApurDec):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurDec.perApurDec', 
                                                                  totApurDec.perApurDec.cdata, 
                                                                  1, u'1, 2, 3')
                            
                            if 'CRDec' in dir(totApurDec):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurDec.CRDec', 
                                                                  totApurDec.CRDec.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrBaseCRDec' in dir(totApurDec):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurDec.vlrBaseCRDec', 
                                                                  totApurDec.vlrBaseCRDec.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrCRDec' in dir(totApurDec):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurDec.vlrCRDec', 
                                                                  totApurDec.vlrCRDec.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrBaseCRDecSusp' in dir(totApurDec):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurDec.vlrBaseCRDecSusp', 
                                                                  totApurDec.vlrBaseCRDecSusp.cdata, 
                                                                  0, u'None')
                            
                            if 'vlrCRDecSusp' in dir(totApurDec):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurDec.vlrCRDecSusp', 
                                                                  totApurDec.vlrCRDecSusp.cdata, 
                                                                  0, u'None')
                    
                    if 'totApurSem' in dir(ideEstab.totApurSem):
                        for totApurSem in ideEstab.totApurSem:
                            
                            if 'perApurSem' in dir(totApurSem):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurSem.perApurSem', 
                                                                  totApurSem.perApurSem.cdata, 
                                                                  1, u'1, 2, 3, 4')
                            
                            if 'CRSem' in dir(totApurSem):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurSem.CRSem', 
                                                                  totApurSem.CRSem.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrBaseCRSem' in dir(totApurSem):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurSem.vlrBaseCRSem', 
                                                                  totApurSem.vlrBaseCRSem.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrCRSem' in dir(totApurSem):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurSem.vlrCRSem', 
                                                                  totApurSem.vlrCRSem.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrBaseCRSemSusp' in dir(totApurSem):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurSem.vlrBaseCRSemSusp', 
                                                                  totApurSem.vlrBaseCRSemSusp.cdata, 
                                                                  0, u'None')
                            
                            if 'vlrCRSemSusp' in dir(totApurSem):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurSem.vlrCRSemSusp', 
                                                                  totApurSem.vlrCRSemSusp.cdata, 
                                                                  0, u'None')
                    
                    if 'totApurDia' in dir(ideEstab.totApurDia):
                        for totApurDia in ideEstab.totApurDia:
                            
                            if 'perApurDia' in dir(totApurDia):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurDia.perApurDia', 
                                                                  totApurDia.perApurDia.cdata, 
                                                                  1, u'None')
                            
                            if 'CRDia' in dir(totApurDia):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurDia.CRDia', 
                                                                  totApurDia.CRDia.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrBaseCRDia' in dir(totApurDia):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurDia.vlrBaseCRDia', 
                                                                  totApurDia.vlrBaseCRDia.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrCRDia' in dir(totApurDia):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurDia.vlrCRDia', 
                                                                  totApurDia.vlrCRDia.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrBaseCRDiaSusp' in dir(totApurDia):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurDia.vlrBaseCRDiaSusp', 
                                                                  totApurDia.vlrBaseCRDiaSusp.cdata, 
                                                                  0, u'None')
                            
                            if 'vlrCRDiaSusp' in dir(totApurDia):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'totApurDia.vlrCRDiaSusp', 
                                                                  totApurDia.vlrCRDiaSusp.cdata, 
                                                                  0, u'None')
    return validacoes_lista