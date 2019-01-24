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


def validacoes_r2040_evtassocdesprep(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtAssocDespRep = doc.Reinf.evtAssocDespRep

    if 'indRetif' in dir(evtAssocDespRep.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRep.ideEvento.indRetif', evtAssocDespRep.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtAssocDespRep.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRep.ideEvento.nrRecibo', evtAssocDespRep.ideEvento.nrRecibo.cdata, 0, '')
    if 'perApur' in dir(evtAssocDespRep.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRep.ideEvento.perApur', evtAssocDespRep.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtAssocDespRep.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRep.ideEvento.tpAmb', evtAssocDespRep.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtAssocDespRep.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRep.ideEvento.procEmi', evtAssocDespRep.ideEvento.procEmi.cdata, 1, '1;2')
    if 'verProc' in dir(evtAssocDespRep.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRep.ideEvento.verProc', evtAssocDespRep.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtAssocDespRep.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRep.ideContri.tpInsc', evtAssocDespRep.ideContri.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtAssocDespRep.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRep.ideContri.nrInsc', evtAssocDespRep.ideContri.nrInsc.cdata, 1, '')
    if 'tpInscEstab' in dir(evtAssocDespRep.ideContri.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRep.ideContri.ideEstab.tpInscEstab', evtAssocDespRep.ideContri.ideEstab.tpInscEstab.cdata, 1, '1')
    if 'nrInscEstab' in dir(evtAssocDespRep.ideContri.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRep.ideContri.ideEstab.nrInscEstab', evtAssocDespRep.ideContri.ideEstab.nrInscEstab.cdata, 1, '')
    if 'recursosRep' in dir(evtAssocDespRep.ideContri.ideEstab):
        for recursosRep in evtAssocDespRep.ideContri.ideEstab.recursosRep:

            if 'cnpjAssocDesp' in dir(recursosRep): validacoes_lista = validar_campo(validacoes_lista,'recursosRep.cnpjAssocDesp', recursosRep.cnpjAssocDesp.cdata, 1, '')
            if 'vlrTotalRep' in dir(recursosRep): validacoes_lista = validar_campo(validacoes_lista,'recursosRep.vlrTotalRep', recursosRep.vlrTotalRep.cdata, 1, '')
            if 'vlrTotalRet' in dir(recursosRep): validacoes_lista = validar_campo(validacoes_lista,'recursosRep.vlrTotalRet', recursosRep.vlrTotalRet.cdata, 1, '')
            if 'vlrTotalNRet' in dir(recursosRep): validacoes_lista = validar_campo(validacoes_lista,'recursosRep.vlrTotalNRet', recursosRep.vlrTotalNRet.cdata, 0, '')

            if 'infoRecurso' in dir(recursosRep):
                for infoRecurso in recursosRep.infoRecurso:

                    if 'tpRepasse' in dir(infoRecurso): validacoes_lista = validar_campo(validacoes_lista,'infoRecurso.tpRepasse', infoRecurso.tpRepasse.cdata, 1, '1;2;3;4;5')
                    if 'descRecurso' in dir(infoRecurso): validacoes_lista = validar_campo(validacoes_lista,'infoRecurso.descRecurso', infoRecurso.descRecurso.cdata, 1, '')
                    if 'vlrBruto' in dir(infoRecurso): validacoes_lista = validar_campo(validacoes_lista,'infoRecurso.vlrBruto', infoRecurso.vlrBruto.cdata, 1, '')
                    if 'vlrRetApur' in dir(infoRecurso): validacoes_lista = validar_campo(validacoes_lista,'infoRecurso.vlrRetApur', infoRecurso.vlrRetApur.cdata, 1, '')

            if 'infoProc' in dir(recursosRep):
                for infoProc in recursosRep.infoProc:

                    if 'tpProc' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.tpProc', infoProc.tpProc.cdata, 1, '1;2')
                    if 'nrProc' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.nrProc', infoProc.nrProc.cdata, 1, '')
                    if 'codSusp' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.codSusp', infoProc.codSusp.cdata, 0, '')
                    if 'vlrNRet' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.vlrNRet', infoProc.vlrNRet.cdata, 1, '')

    return validacoes_lista