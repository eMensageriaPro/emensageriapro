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

    if 'indRetif' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.indRetif', evtComProd.ideEvento.indRetif.cdata, 1, u'1;2')
    if 'nrRecibo' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.nrRecibo', evtComProd.ideEvento.nrRecibo.cdata, 0, u'')
    if 'perApur' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.perApur', evtComProd.ideEvento.perApur.cdata, 1, u'')
    if 'tpAmb' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.tpAmb', evtComProd.ideEvento.tpAmb.cdata, 1, u'1;2')
    if 'procEmi' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.procEmi', evtComProd.ideEvento.procEmi.cdata, 1, u'1;2')
    if 'verProc' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.verProc', evtComProd.ideEvento.verProc.cdata, 1, u'')
    if 'tpInsc' in dir(evtComProd.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideContri.tpInsc', evtComProd.ideContri.tpInsc.cdata, 1, u'1;2')
    if 'nrInsc' in dir(evtComProd.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideContri.nrInsc', evtComProd.ideContri.nrInsc.cdata, 1, u'')
    if 'tpInscEstab' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.tpInscEstab', evtComProd.infoComProd.ideEstab.tpInscEstab.cdata, 1, u'1')
    if 'nrInscEstab' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.nrInscEstab', evtComProd.infoComProd.ideEstab.nrInscEstab.cdata, 1, u'')
    if 'vlrRecBrutaTotal' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.vlrRecBrutaTotal', evtComProd.infoComProd.ideEstab.vlrRecBrutaTotal.cdata, 1, u'')
    if 'vlrCPApur' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.vlrCPApur', evtComProd.infoComProd.ideEstab.vlrCPApur.cdata, 1, u'')
    if 'vlrRatApur' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.vlrRatApur', evtComProd.infoComProd.ideEstab.vlrRatApur.cdata, 1, u'')
    if 'vlrSenarApur' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.vlrSenarApur', evtComProd.infoComProd.ideEstab.vlrSenarApur.cdata, 1, u'')
    if 'vlrCPSuspTotal' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.vlrCPSuspTotal', evtComProd.infoComProd.ideEstab.vlrCPSuspTotal.cdata, 0, u'')
    if 'vlrRatSuspTotal' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.vlrRatSuspTotal', evtComProd.infoComProd.ideEstab.vlrRatSuspTotal.cdata, 0, u'')
    if 'vlrSenarSuspTotal' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.vlrSenarSuspTotal', evtComProd.infoComProd.ideEstab.vlrSenarSuspTotal.cdata, 0, u'')
    if 'tipoCom' in dir(evtComProd.infoComProd.ideEstab):
        for tipoCom in evtComProd.infoComProd.ideEstab.tipoCom:

            if 'indCom' in dir(tipoCom): validacoes_lista = validar_campo(validacoes_lista,'tipoCom.indCom', tipoCom.indCom.cdata, 1, u'1;8;9')
            if 'vlrRecBruta' in dir(tipoCom): validacoes_lista = validar_campo(validacoes_lista,'tipoCom.vlrRecBruta', tipoCom.vlrRecBruta.cdata, 1, u'')

            if 'infoProc' in dir(tipoCom):
                for infoProc in tipoCom.infoProc:

                    if 'tpProc' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.tpProc', infoProc.tpProc.cdata, 1, u'1;2')
                    if 'nrProc' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.nrProc', infoProc.nrProc.cdata, 1, u'')
                    if 'codSusp' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.codSusp', infoProc.codSusp.cdata, 0, u'')
                    if 'vlrCPSusp' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.vlrCPSusp', infoProc.vlrCPSusp.cdata, 0, u'')
                    if 'vlrRatSusp' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.vlrRatSusp', infoProc.vlrRatSusp.cdata, 0, u'')
                    if 'vlrSenarSusp' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.vlrSenarSusp', infoProc.vlrSenarSusp.cdata, 0, u'')

    return validacoes_lista