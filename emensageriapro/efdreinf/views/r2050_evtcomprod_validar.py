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


def validacoes_r2050_evtcomprod(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtComProd = doc.Reinf.evtComProd
    #variaveis

    if 'ideEvento' in dir(evtComProd.ideEvento):
        for ideEvento in evtComProd.ideEvento:

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

    if 'ideContri' in dir(evtComProd.ideContri):
        for ideContri in evtComProd.ideContri:

            if 'tpInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.tpInsc',
                                                  ideContri.tpInsc.cdata,
                                                  1, u'None')

            if 'nrInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.nrInsc',
                                                  ideContri.nrInsc.cdata,
                                                  1, u'None')

    if 'infoComProd' in dir(evtComProd.infoComProd):
        for infoComProd in evtComProd.infoComProd:

            if 'ideEstab' in dir(infoComProd.ideEstab):
                for ideEstab in infoComProd.ideEstab:

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

                    if 'vlrRecBrutaTotal' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.vlrRecBrutaTotal',
                                                          ideEstab.vlrRecBrutaTotal.cdata,
                                                          1, u'None')

                    if 'vlrCPApur' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.vlrCPApur',
                                                          ideEstab.vlrCPApur.cdata,
                                                          1, u'None')

                    if 'vlrRatApur' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.vlrRatApur',
                                                          ideEstab.vlrRatApur.cdata,
                                                          1, u'None')

                    if 'vlrSenarApur' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.vlrSenarApur',
                                                          ideEstab.vlrSenarApur.cdata,
                                                          1, u'None')

                    if 'vlrCPSuspTotal' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.vlrCPSuspTotal',
                                                          ideEstab.vlrCPSuspTotal.cdata,
                                                          0, u'None')

                    if 'vlrRatSuspTotal' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.vlrRatSuspTotal',
                                                          ideEstab.vlrRatSuspTotal.cdata,
                                                          0, u'None')

                    if 'vlrSenarSuspTotal' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.vlrSenarSuspTotal',
                                                          ideEstab.vlrSenarSuspTotal.cdata,
                                                          0, u'None')

                    if 'tipoCom' in dir(ideEstab.tipoCom):
                        for tipoCom in ideEstab.tipoCom:
        
                            if 'indCom' in dir(tipoCom):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'tipoCom.indCom',
                                                                  tipoCom.indCom.cdata,
                                                                  1, u'1, 7, 8, 9')
        
                            if 'vlrRecBruta' in dir(tipoCom):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'tipoCom.vlrRecBruta',
                                                                  tipoCom.vlrRecBruta.cdata,
                                                                  1, u'None')
        
                            if 'infoProc' in dir(tipoCom.infoProc):
                                for infoProc in tipoCom.infoProc:
                
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
                
                                    if 'vlrCPSusp' in dir(infoProc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProc.vlrCPSusp',
                                                                          infoProc.vlrCPSusp.cdata,
                                                                          0, u'None')
                
                                    if 'vlrRatSusp' in dir(infoProc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProc.vlrRatSusp',
                                                                          infoProc.vlrRatSusp.cdata,
                                                                          0, u'None')
                
                                    if 'vlrSenarSusp' in dir(infoProc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProc.vlrSenarSusp',
                                                                          infoProc.vlrSenarSusp.cdata,
                                                                          0, u'None')
    return validacoes_lista