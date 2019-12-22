# eMensageriaAI #
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


def validacoes_r2060_evtcprb(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtCPRB = doc.Reinf.evtCPRB
    #variaveis

    if 'ideEvento' in dir(evtCPRB.ideEvento):
        for ideEvento in evtCPRB.ideEvento:

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

    if 'ideContri' in dir(evtCPRB.ideContri):
        for ideContri in evtCPRB.ideContri:

            if 'tpInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.tpInsc',
                                                  ideContri.tpInsc.cdata,
                                                  1, u'1')

            if 'nrInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.nrInsc',
                                                  ideContri.nrInsc.cdata,
                                                  1, u'None')

    if 'infoCPRB' in dir(evtCPRB.infoCPRB):
        for infoCPRB in evtCPRB.infoCPRB:

            if 'ideEstab' in dir(infoCPRB.ideEstab):
                for ideEstab in infoCPRB.ideEstab:

                    if 'tpInscEstab' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.tpInscEstab',
                                                          ideEstab.tpInscEstab.cdata,
                                                          1, u'None')

                    if 'nrInscEstab' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.nrInscEstab',
                                                          ideEstab.nrInscEstab.cdata,
                                                          1, u'None')

                    if 'vlrRecBrutaTotal' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.vlrRecBrutaTotal',
                                                          ideEstab.vlrRecBrutaTotal.cdata,
                                                          1, u'None')

                    if 'vlrCPApurTotal' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.vlrCPApurTotal',
                                                          ideEstab.vlrCPApurTotal.cdata,
                                                          1, u'None')

                    if 'vlrCPRBSuspTotal' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.vlrCPRBSuspTotal',
                                                          ideEstab.vlrCPRBSuspTotal.cdata,
                                                          0, u'None')

                    if 'tipoCod' in dir(ideEstab.tipoCod):
                        for tipoCod in ideEstab.tipoCod:
        
                            if 'codAtivEcon' in dir(tipoCod):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'tipoCod.codAtivEcon',
                                                                  tipoCod.codAtivEcon.cdata,
                                                                  1, u'I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, II, II, II, II, II, II, II, II, II, II, II, II, II, II, II, II, II, II, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, IV, IV, IV, IV, IV, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, III, IV, IV, IV, IV, IV, IV')
        
                            if 'vlrRecBrutaAtiv' in dir(tipoCod):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'tipoCod.vlrRecBrutaAtiv',
                                                                  tipoCod.vlrRecBrutaAtiv.cdata,
                                                                  1, u'None')
        
                            if 'vlrExcRecBruta' in dir(tipoCod):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'tipoCod.vlrExcRecBruta',
                                                                  tipoCod.vlrExcRecBruta.cdata,
                                                                  1, u'None')
        
                            if 'vlrAdicRecBruta' in dir(tipoCod):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'tipoCod.vlrAdicRecBruta',
                                                                  tipoCod.vlrAdicRecBruta.cdata,
                                                                  1, u'None')
        
                            if 'vlrBcCPRB' in dir(tipoCod):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'tipoCod.vlrBcCPRB',
                                                                  tipoCod.vlrBcCPRB.cdata,
                                                                  1, u'None')
        
                            if 'vlrCPRBapur' in dir(tipoCod):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'tipoCod.vlrCPRBapur',
                                                                  tipoCod.vlrCPRBapur.cdata,
                                                                  0, u'None')
        
                            if 'tipoAjuste' in dir(tipoCod.tipoAjuste):
                                for tipoAjuste in tipoCod.tipoAjuste:
                
                                    if 'tpAjuste' in dir(tipoAjuste):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'tipoAjuste.tpAjuste',
                                                                          tipoAjuste.tpAjuste.cdata,
                                                                          1, u'0, 1')
                
                                    if 'codAjuste' in dir(tipoAjuste):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'tipoAjuste.codAjuste',
                                                                          tipoAjuste.codAjuste.cdata,
                                                                          1, u'1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11')
                
                                    if 'vlrAjuste' in dir(tipoAjuste):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'tipoAjuste.vlrAjuste',
                                                                          tipoAjuste.vlrAjuste.cdata,
                                                                          1, u'None')
                
                                    if 'descAjuste' in dir(tipoAjuste):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'tipoAjuste.descAjuste',
                                                                          tipoAjuste.descAjuste.cdata,
                                                                          1, u'None')
                
                                    if 'dtAjuste' in dir(tipoAjuste):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'tipoAjuste.dtAjuste',
                                                                          tipoAjuste.dtAjuste.cdata,
                                                                          1, u'None')
        
                            if 'infoProc' in dir(tipoCod.infoProc):
                                for infoProc in tipoCod.infoProc:
                
                                    if 'tpProc' in dir(infoProc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProc.tpProc',
                                                                          infoProc.tpProc.cdata,
                                                                          1, u'1, 2')
                
                                    if 'nrProc' in dir(infoProc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProc.nrProc',
                                                                          infoProc.nrProc.cdata,
                                                                          1, u'None')
                
                                    if 'codSusp' in dir(infoProc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProc.codSusp',
                                                                          infoProc.codSusp.cdata,
                                                                          0, u'None')
                
                                    if 'vlrCPRBSusp' in dir(infoProc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProc.vlrCPRBSusp',
                                                                          infoProc.vlrCPRBSusp.cdata,
                                                                          1, u'None')
    return validacoes_lista