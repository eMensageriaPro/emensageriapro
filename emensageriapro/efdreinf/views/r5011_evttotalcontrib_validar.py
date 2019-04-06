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


def validacoes_r5011_evttotalcontrib(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtTotalContrib = doc.Reinf.evtTotalContrib

    if 'perApur' in dir(evtTotalContrib.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTotalContrib.ideEvento.perApur', evtTotalContrib.ideEvento.perApur.cdata, 1, u'')
    if 'tpInsc' in dir(evtTotalContrib.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtTotalContrib.ideContri.tpInsc', evtTotalContrib.ideContri.tpInsc.cdata, 1, u'1;2')
    if 'nrInsc' in dir(evtTotalContrib.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtTotalContrib.ideContri.nrInsc', evtTotalContrib.ideContri.nrInsc.cdata, 1, u'')
    if 'cdRetorno' in dir(evtTotalContrib.ideRecRetorno.ideStatus): validacoes_lista = validar_campo(validacoes_lista,'evtTotalContrib.ideRecRetorno.ideStatus.cdRetorno', evtTotalContrib.ideRecRetorno.ideStatus.cdRetorno.cdata, 1, u'')
    if 'descRetorno' in dir(evtTotalContrib.ideRecRetorno.ideStatus): validacoes_lista = validar_campo(validacoes_lista,'evtTotalContrib.ideRecRetorno.ideStatus.descRetorno', evtTotalContrib.ideRecRetorno.ideStatus.descRetorno.cdata, 1, u'')
    if 'nrProtEntr' in dir(evtTotalContrib.infoRecEv): validacoes_lista = validar_campo(validacoes_lista,'evtTotalContrib.infoRecEv.nrProtEntr', evtTotalContrib.infoRecEv.nrProtEntr.cdata, 1, u'')
    if 'dhProcess' in dir(evtTotalContrib.infoRecEv): validacoes_lista = validar_campo(validacoes_lista,'evtTotalContrib.infoRecEv.dhProcess', evtTotalContrib.infoRecEv.dhProcess.cdata, 1, u'')
    if 'tpEv' in dir(evtTotalContrib.infoRecEv): validacoes_lista = validar_campo(validacoes_lista,'evtTotalContrib.infoRecEv.tpEv', evtTotalContrib.infoRecEv.tpEv.cdata, 1, u'')
    if 'idEv' in dir(evtTotalContrib.infoRecEv): validacoes_lista = validar_campo(validacoes_lista,'evtTotalContrib.infoRecEv.idEv', evtTotalContrib.infoRecEv.idEv.cdata, 1, u'')
    if 'hash' in dir(evtTotalContrib.infoRecEv): validacoes_lista = validar_campo(validacoes_lista,'evtTotalContrib.infoRecEv.hash', evtTotalContrib.infoRecEv.hash.cdata, 1, u'')
    if 'regOcorrs' in dir(evtTotalContrib.ideRecRetorno.ideStatus):
        for regOcorrs in evtTotalContrib.ideRecRetorno.ideStatus.regOcorrs:

            if 'tpOcorr' in dir(regOcorrs): validacoes_lista = validar_campo(validacoes_lista,'regOcorrs.tpOcorr', regOcorrs.tpOcorr.cdata, 1, u'1;2')
            if 'localErroAviso' in dir(regOcorrs): validacoes_lista = validar_campo(validacoes_lista,'regOcorrs.localErroAviso', regOcorrs.localErroAviso.cdata, 1, u'')
            if 'codResp' in dir(regOcorrs): validacoes_lista = validar_campo(validacoes_lista,'regOcorrs.codResp', regOcorrs.codResp.cdata, 1, u'')
            if 'dscResp' in dir(regOcorrs): validacoes_lista = validar_campo(validacoes_lista,'regOcorrs.dscResp', regOcorrs.dscResp.cdata, 1, u'')

    if 'infoTotalContrib' in dir(evtTotalContrib):
        for infoTotalContrib in evtTotalContrib.infoTotalContrib:

            if 'nrRecArqBase' in dir(infoTotalContrib): validacoes_lista = validar_campo(validacoes_lista,'infoTotalContrib.nrRecArqBase', infoTotalContrib.nrRecArqBase.cdata, 0, u'')
            if 'indExistInfo' in dir(infoTotalContrib): validacoes_lista = validar_campo(validacoes_lista,'infoTotalContrib.indExistInfo', infoTotalContrib.indExistInfo.cdata, 1, u'1;2;3')

            if 'RTom' in dir(infoTotalContrib):
                for RTom in infoTotalContrib.RTom:

                    if 'cnpjPrestador' in dir(RTom): validacoes_lista = validar_campo(validacoes_lista,'RTom.cnpjPrestador', RTom.cnpjPrestador.cdata, 1, u'')
                    if 'cno' in dir(RTom): validacoes_lista = validar_campo(validacoes_lista,'RTom.cno', RTom.cno.cdata, 0, u'')
                    if 'vlrTotalBaseRet' in dir(RTom): validacoes_lista = validar_campo(validacoes_lista,'RTom.vlrTotalBaseRet', RTom.vlrTotalBaseRet.cdata, 1, u'')

            if 'RPrest' in dir(infoTotalContrib):
                for RPrest in infoTotalContrib.RPrest:

                    if 'tpInscTomador' in dir(RPrest): validacoes_lista = validar_campo(validacoes_lista,'RPrest.tpInscTomador', RPrest.tpInscTomador.cdata, 1, u'1;4')
                    if 'nrInscTomador' in dir(RPrest): validacoes_lista = validar_campo(validacoes_lista,'RPrest.nrInscTomador', RPrest.nrInscTomador.cdata, 1, u'')
                    if 'vlrTotalBaseRet' in dir(RPrest): validacoes_lista = validar_campo(validacoes_lista,'RPrest.vlrTotalBaseRet', RPrest.vlrTotalBaseRet.cdata, 1, u'')
                    if 'vlrTotalRetPrinc' in dir(RPrest): validacoes_lista = validar_campo(validacoes_lista,'RPrest.vlrTotalRetPrinc', RPrest.vlrTotalRetPrinc.cdata, 1, u'')
                    if 'vlrTotalRetAdic' in dir(RPrest): validacoes_lista = validar_campo(validacoes_lista,'RPrest.vlrTotalRetAdic', RPrest.vlrTotalRetAdic.cdata, 0, u'')
                    if 'vlrTotalNRetPrinc' in dir(RPrest): validacoes_lista = validar_campo(validacoes_lista,'RPrest.vlrTotalNRetPrinc', RPrest.vlrTotalNRetPrinc.cdata, 0, u'')
                    if 'vlrTotalNRetAdic' in dir(RPrest): validacoes_lista = validar_campo(validacoes_lista,'RPrest.vlrTotalNRetAdic', RPrest.vlrTotalNRetAdic.cdata, 0, u'')

            if 'RRecRepAD' in dir(infoTotalContrib):
                for RRecRepAD in infoTotalContrib.RRecRepAD:

                    if 'cnpjAssocDesp' in dir(RRecRepAD): validacoes_lista = validar_campo(validacoes_lista,'RRecRepAD.cnpjAssocDesp', RRecRepAD.cnpjAssocDesp.cdata, 1, u'')
                    if 'vlrTotalRep' in dir(RRecRepAD): validacoes_lista = validar_campo(validacoes_lista,'RRecRepAD.vlrTotalRep', RRecRepAD.vlrTotalRep.cdata, 1, u'')
                    if 'CRRecRepAD' in dir(RRecRepAD): validacoes_lista = validar_campo(validacoes_lista,'RRecRepAD.CRRecRepAD', RRecRepAD.CRRecRepAD.cdata, 1, u'')
                    if 'vlrCRRecRepAD' in dir(RRecRepAD): validacoes_lista = validar_campo(validacoes_lista,'RRecRepAD.vlrCRRecRepAD', RRecRepAD.vlrCRRecRepAD.cdata, 1, u'')
                    if 'vlrCRRecRepADSusp' in dir(RRecRepAD): validacoes_lista = validar_campo(validacoes_lista,'RRecRepAD.vlrCRRecRepADSusp', RRecRepAD.vlrCRRecRepADSusp.cdata, 0, u'')

            if 'RComl' in dir(infoTotalContrib):
                for RComl in infoTotalContrib.RComl:

                    if 'CRComl' in dir(RComl): validacoes_lista = validar_campo(validacoes_lista,'RComl.CRComl', RComl.CRComl.cdata, 1, u'')
                    if 'vlrCRComl' in dir(RComl): validacoes_lista = validar_campo(validacoes_lista,'RComl.vlrCRComl', RComl.vlrCRComl.cdata, 1, u'')
                    if 'vlrCRComlSusp' in dir(RComl): validacoes_lista = validar_campo(validacoes_lista,'RComl.vlrCRComlSusp', RComl.vlrCRComlSusp.cdata, 0, u'')

            if 'RCPRB' in dir(infoTotalContrib):
                for RCPRB in infoTotalContrib.RCPRB:

                    if 'CRCPRB' in dir(RCPRB): validacoes_lista = validar_campo(validacoes_lista,'RCPRB.CRCPRB', RCPRB.CRCPRB.cdata, 1, u'')
                    if 'vlrCRCPRB' in dir(RCPRB): validacoes_lista = validar_campo(validacoes_lista,'RCPRB.vlrCRCPRB', RCPRB.vlrCRCPRB.cdata, 1, u'')
                    if 'vlrCRCPRBSusp' in dir(RCPRB): validacoes_lista = validar_campo(validacoes_lista,'RCPRB.vlrCRCPRBSusp', RCPRB.vlrCRCPRBSusp.cdata, 0, u'')

    return validacoes_lista