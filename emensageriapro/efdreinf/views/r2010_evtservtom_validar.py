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


def validacoes_r2010_evtservtom(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtServTom = doc.Reinf.evtServTom

    if 'indRetif' in dir(evtServTom.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.ideEvento.indRetif', evtServTom.ideEvento.indRetif.cdata, 1, u'1;2')
    if 'nrRecibo' in dir(evtServTom.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.ideEvento.nrRecibo', evtServTom.ideEvento.nrRecibo.cdata, 0, u'')
    if 'perApur' in dir(evtServTom.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.ideEvento.perApur', evtServTom.ideEvento.perApur.cdata, 1, u'')
    if 'tpAmb' in dir(evtServTom.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.ideEvento.tpAmb', evtServTom.ideEvento.tpAmb.cdata, 1, u'1;2')
    if 'procEmi' in dir(evtServTom.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.ideEvento.procEmi', evtServTom.ideEvento.procEmi.cdata, 1, u'1;2')
    if 'verProc' in dir(evtServTom.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.ideEvento.verProc', evtServTom.ideEvento.verProc.cdata, 1, u'')
    if 'tpInsc' in dir(evtServTom.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.ideContri.tpInsc', evtServTom.ideContri.tpInsc.cdata, 1, u'1;2')
    if 'nrInsc' in dir(evtServTom.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.ideContri.nrInsc', evtServTom.ideContri.nrInsc.cdata, 1, u'')
    if 'tpInscEstab' in dir(evtServTom.infoServTom.ideEstabObra): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.infoServTom.ideEstabObra.tpInscEstab', evtServTom.infoServTom.ideEstabObra.tpInscEstab.cdata, 1, u'1;4')
    if 'nrInscEstab' in dir(evtServTom.infoServTom.ideEstabObra): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.infoServTom.ideEstabObra.nrInscEstab', evtServTom.infoServTom.ideEstabObra.nrInscEstab.cdata, 1, u'')
    if 'indObra' in dir(evtServTom.infoServTom.ideEstabObra): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.infoServTom.ideEstabObra.indObra', evtServTom.infoServTom.ideEstabObra.indObra.cdata, 1, u'0;1;2')
    if 'cnpjPrestador' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.infoServTom.ideEstabObra.idePrestServ.cnpjPrestador', evtServTom.infoServTom.ideEstabObra.idePrestServ.cnpjPrestador.cdata, 1, u'')
    if 'vlrTotalBruto' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalBruto', evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalBruto.cdata, 1, u'')
    if 'vlrTotalBaseRet' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalBaseRet', evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalBaseRet.cdata, 1, u'')
    if 'vlrTotalRetPrinc' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalRetPrinc', evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalRetPrinc.cdata, 1, u'')
    if 'vlrTotalRetAdic' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalRetAdic', evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalRetAdic.cdata, 0, u'')
    if 'vlrTotalNRetPrinc' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalNRetPrinc', evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalNRetPrinc.cdata, 0, u'')
    if 'vlrTotalNRetAdic' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalNRetAdic', evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalNRetAdic.cdata, 0, u'')
    if 'indCPRB' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): validacoes_lista = validar_campo(validacoes_lista,'evtServTom.infoServTom.ideEstabObra.idePrestServ.indCPRB', evtServTom.infoServTom.ideEstabObra.idePrestServ.indCPRB.cdata, 1, u'0;1')
    if 'nfs' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ):
        for nfs in evtServTom.infoServTom.ideEstabObra.idePrestServ.nfs:

            if 'serie' in dir(nfs): validacoes_lista = validar_campo(validacoes_lista,'nfs.serie', nfs.serie.cdata, 1, u'')
            if 'numDocto' in dir(nfs): validacoes_lista = validar_campo(validacoes_lista,'nfs.numDocto', nfs.numDocto.cdata, 1, u'')
            if 'dtEmissaoNF' in dir(nfs): validacoes_lista = validar_campo(validacoes_lista,'nfs.dtEmissaoNF', nfs.dtEmissaoNF.cdata, 1, u'')
            if 'vlrBruto' in dir(nfs): validacoes_lista = validar_campo(validacoes_lista,'nfs.vlrBruto', nfs.vlrBruto.cdata, 1, u'')
            if 'obs' in dir(nfs): validacoes_lista = validar_campo(validacoes_lista,'nfs.obs', nfs.obs.cdata, 0, u'')

            if 'infoTpServ' in dir(nfs):
                for infoTpServ in nfs.infoTpServ:

                    if 'tpServico' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.tpServico', infoTpServ.tpServico.cdata, 1, u'')
                    if 'vlrBaseRet' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrBaseRet', infoTpServ.vlrBaseRet.cdata, 1, u'')
                    if 'vlrRetencao' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrRetencao', infoTpServ.vlrRetencao.cdata, 1, u'')
                    if 'vlrRetSub' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrRetSub', infoTpServ.vlrRetSub.cdata, 0, u'')
                    if 'vlrNRetPrinc' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrNRetPrinc', infoTpServ.vlrNRetPrinc.cdata, 0, u'')
                    if 'vlrServicos15' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrServicos15', infoTpServ.vlrServicos15.cdata, 0, u'')
                    if 'vlrServicos20' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrServicos20', infoTpServ.vlrServicos20.cdata, 0, u'')
                    if 'vlrServicos25' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrServicos25', infoTpServ.vlrServicos25.cdata, 0, u'')
                    if 'vlrAdicional' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrAdicional', infoTpServ.vlrAdicional.cdata, 0, u'')
                    if 'vlrNRetAdic' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrNRetAdic', infoTpServ.vlrNRetAdic.cdata, 0, u'')

    if 'infoProcRetPr' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ):
        for infoProcRetPr in evtServTom.infoServTom.ideEstabObra.idePrestServ.infoProcRetPr:

            if 'tpProcRetPrinc' in dir(infoProcRetPr): validacoes_lista = validar_campo(validacoes_lista,'infoProcRetPr.tpProcRetPrinc', infoProcRetPr.tpProcRetPrinc.cdata, 1, u'1;2')
            if 'nrProcRetPrinc' in dir(infoProcRetPr): validacoes_lista = validar_campo(validacoes_lista,'infoProcRetPr.nrProcRetPrinc', infoProcRetPr.nrProcRetPrinc.cdata, 1, u'')
            if 'codSuspPrinc' in dir(infoProcRetPr): validacoes_lista = validar_campo(validacoes_lista,'infoProcRetPr.codSuspPrinc', infoProcRetPr.codSuspPrinc.cdata, 0, u'')
            if 'valorPrinc' in dir(infoProcRetPr): validacoes_lista = validar_campo(validacoes_lista,'infoProcRetPr.valorPrinc', infoProcRetPr.valorPrinc.cdata, 1, u'')

    if 'infoProcRetAd' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ):
        for infoProcRetAd in evtServTom.infoServTom.ideEstabObra.idePrestServ.infoProcRetAd:

            if 'tpProcRetAdic' in dir(infoProcRetAd): validacoes_lista = validar_campo(validacoes_lista,'infoProcRetAd.tpProcRetAdic', infoProcRetAd.tpProcRetAdic.cdata, 1, u'1;2')
            if 'nrProcRetAdic' in dir(infoProcRetAd): validacoes_lista = validar_campo(validacoes_lista,'infoProcRetAd.nrProcRetAdic', infoProcRetAd.nrProcRetAdic.cdata, 1, u'')
            if 'codSuspAdic' in dir(infoProcRetAd): validacoes_lista = validar_campo(validacoes_lista,'infoProcRetAd.codSuspAdic', infoProcRetAd.codSuspAdic.cdata, 0, u'')
            if 'valorAdic' in dir(infoProcRetAd): validacoes_lista = validar_campo(validacoes_lista,'infoProcRetAd.valorAdic', infoProcRetAd.valorAdic.cdata, 1, u'')

    return validacoes_lista