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

    if 'indRetif' in dir(evtCPRB.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCPRB.ideEvento.indRetif', evtCPRB.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtCPRB.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCPRB.ideEvento.nrRecibo', evtCPRB.ideEvento.nrRecibo.cdata, 0, '')
    if 'perApur' in dir(evtCPRB.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCPRB.ideEvento.perApur', evtCPRB.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtCPRB.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCPRB.ideEvento.tpAmb', evtCPRB.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtCPRB.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCPRB.ideEvento.procEmi', evtCPRB.ideEvento.procEmi.cdata, 1, '1;2')
    if 'verProc' in dir(evtCPRB.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCPRB.ideEvento.verProc', evtCPRB.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtCPRB.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtCPRB.ideContri.tpInsc', evtCPRB.ideContri.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtCPRB.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtCPRB.ideContri.nrInsc', evtCPRB.ideContri.nrInsc.cdata, 1, '')
    if 'tpInscEstab' in dir(evtCPRB.infoCPRB.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtCPRB.infoCPRB.ideEstab.tpInscEstab', evtCPRB.infoCPRB.ideEstab.tpInscEstab.cdata, 1, '1;4')
    if 'nrInscEstab' in dir(evtCPRB.infoCPRB.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtCPRB.infoCPRB.ideEstab.nrInscEstab', evtCPRB.infoCPRB.ideEstab.nrInscEstab.cdata, 1, '')
    if 'vlrRecBrutaTotal' in dir(evtCPRB.infoCPRB.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtCPRB.infoCPRB.ideEstab.vlrRecBrutaTotal', evtCPRB.infoCPRB.ideEstab.vlrRecBrutaTotal.cdata, 1, '')
    if 'vlrCPApurTotal' in dir(evtCPRB.infoCPRB.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtCPRB.infoCPRB.ideEstab.vlrCPApurTotal', evtCPRB.infoCPRB.ideEstab.vlrCPApurTotal.cdata, 1, '')
    if 'vlrCPRBSuspTotal' in dir(evtCPRB.infoCPRB.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtCPRB.infoCPRB.ideEstab.vlrCPRBSuspTotal', evtCPRB.infoCPRB.ideEstab.vlrCPRBSuspTotal.cdata, 0, '')
    if 'tipoCod' in dir(evtCPRB.infoCPRB.ideEstab):
        for tipoCod in evtCPRB.infoCPRB.ideEstab.tipoCod:

            if 'codAtivEcon' in dir(tipoCod): validacoes_lista = validar_campo(validacoes_lista,'tipoCod.codAtivEcon', tipoCod.codAtivEcon.cdata, 1, '')
            if 'vlrRecBrutaAtiv' in dir(tipoCod): validacoes_lista = validar_campo(validacoes_lista,'tipoCod.vlrRecBrutaAtiv', tipoCod.vlrRecBrutaAtiv.cdata, 1, '')
            if 'vlrExcRecBruta' in dir(tipoCod): validacoes_lista = validar_campo(validacoes_lista,'tipoCod.vlrExcRecBruta', tipoCod.vlrExcRecBruta.cdata, 1, '')
            if 'vlrAdicRecBruta' in dir(tipoCod): validacoes_lista = validar_campo(validacoes_lista,'tipoCod.vlrAdicRecBruta', tipoCod.vlrAdicRecBruta.cdata, 1, '')
            if 'vlrBcCPRB' in dir(tipoCod): validacoes_lista = validar_campo(validacoes_lista,'tipoCod.vlrBcCPRB', tipoCod.vlrBcCPRB.cdata, 1, '')
            if 'vlrCPRBapur' in dir(tipoCod): validacoes_lista = validar_campo(validacoes_lista,'tipoCod.vlrCPRBapur', tipoCod.vlrCPRBapur.cdata, 0, '')

            if 'tipoAjuste' in dir(tipoCod):
                for tipoAjuste in tipoCod.tipoAjuste:

                    if 'tpAjuste' in dir(tipoAjuste): validacoes_lista = validar_campo(validacoes_lista,'tipoAjuste.tpAjuste', tipoAjuste.tpAjuste.cdata, 1, '0;1')
                    if 'codAjuste' in dir(tipoAjuste): validacoes_lista = validar_campo(validacoes_lista,'tipoAjuste.codAjuste', tipoAjuste.codAjuste.cdata, 1, '1;2;3;4;5;6;7;8;9;10;11')
                    if 'vlrAjuste' in dir(tipoAjuste): validacoes_lista = validar_campo(validacoes_lista,'tipoAjuste.vlrAjuste', tipoAjuste.vlrAjuste.cdata, 1, '')
                    if 'descAjuste' in dir(tipoAjuste): validacoes_lista = validar_campo(validacoes_lista,'tipoAjuste.descAjuste', tipoAjuste.descAjuste.cdata, 1, '')
                    if 'dtAjuste' in dir(tipoAjuste): validacoes_lista = validar_campo(validacoes_lista,'tipoAjuste.dtAjuste', tipoAjuste.dtAjuste.cdata, 1, '')

            if 'infoProc' in dir(tipoCod):
                for infoProc in tipoCod.infoProc:

                    if 'tpProc' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.tpProc', infoProc.tpProc.cdata, 1, '1;2')
                    if 'nrProc' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.nrProc', infoProc.nrProc.cdata, 1, '')
                    if 'codSusp' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.codSusp', infoProc.codSusp.cdata, 0, '')
                    if 'vlrCPRBSusp' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.vlrCPRBSusp', infoProc.vlrCPRBSusp.cdata, 1, '')

    return validacoes_lista