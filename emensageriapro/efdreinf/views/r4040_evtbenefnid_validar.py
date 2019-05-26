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


def validacoes_r4040_evtbenefnid(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtBenefNId = doc.Reinf.evtBenefNId
    #variaveis
    
    if 'ideEvento' in dir(evtBenefNId.ideEvento):
        for ideEvento in evtBenefNId.ideEvento:
            
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
                                                  1, u'1, 2')
            
            if 'verProc' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.verProc', 
                                                  ideEvento.verProc.cdata, 
                                                  1, u'None')
    
    if 'ideContri' in dir(evtBenefNId.ideContri):
        for ideContri in evtBenefNId.ideContri:
            
            if 'tpInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.tpInsc', 
                                                  ideContri.tpInsc.cdata, 
                                                  1, u'1, 2, 3, 4, 5')
            
            if 'nrInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.nrInsc', 
                                                  ideContri.nrInsc.cdata, 
                                                  1, u'None')
    
    if 'ideEstab' in dir(evtBenefNId.ideEstab):
        for ideEstab in evtBenefNId.ideEstab:
            
            if 'tpInscEstab' in dir(ideEstab):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEstab.tpInscEstab', 
                                                  ideEstab.tpInscEstab.cdata, 
                                                  1, u'1')
            
            if 'nrInscEstab' in dir(ideEstab):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEstab.nrInscEstab', 
                                                  ideEstab.nrInscEstab.cdata, 
                                                  1, u'None')
            
            if 'ideNat' in dir(ideEstab.ideNat):
                for ideNat in ideEstab.ideNat:
                    
                    if 'natRendim' in dir(ideNat):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideNat.natRendim', 
                                                          ideNat.natRendim.cdata, 
                                                          1, u'1, 9')
                    
                    if 'infoPgto' in dir(ideNat.infoPgto):
                        for infoPgto in ideNat.infoPgto:
                            
                            if 'dtFG' in dir(infoPgto):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoPgto.dtFG', 
                                                                  infoPgto.dtFG.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrLiq' in dir(infoPgto):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoPgto.vlrLiq', 
                                                                  infoPgto.vlrLiq.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrReaj' in dir(infoPgto):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoPgto.vlrReaj', 
                                                                  infoPgto.vlrReaj.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrIR' in dir(infoPgto):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoPgto.vlrIR', 
                                                                  infoPgto.vlrIR.cdata, 
                                                                  1, u'None')
                            
                            if 'descr' in dir(infoPgto):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoPgto.descr', 
                                                                  infoPgto.descr.cdata, 
                                                                  1, u'None')
    return validacoes_lista