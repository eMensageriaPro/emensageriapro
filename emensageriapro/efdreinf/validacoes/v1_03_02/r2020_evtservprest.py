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


def validacoes_r2020_evtservprest(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtServPrest = doc.Reinf.evtServPrest
    
    if 'indRetif' in dir(evtServPrest.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.ideEvento.indRetif', evtServPrest.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtServPrest.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.ideEvento.nrRecibo', evtServPrest.ideEvento.nrRecibo.cdata, 0, '')
    if 'perApur' in dir(evtServPrest.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.ideEvento.perApur', evtServPrest.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtServPrest.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.ideEvento.tpAmb', evtServPrest.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtServPrest.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.ideEvento.procEmi', evtServPrest.ideEvento.procEmi.cdata, 1, '1;2')
    if 'verProc' in dir(evtServPrest.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.ideEvento.verProc', evtServPrest.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtServPrest.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.ideContri.tpInsc', evtServPrest.ideContri.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtServPrest.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.ideContri.nrInsc', evtServPrest.ideContri.nrInsc.cdata, 1, '')
    if 'tpInscEstabPrest' in dir(evtServPrest.infoServPrest.ideEstabPrest): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.infoServPrest.ideEstabPrest.tpInscEstabPrest', evtServPrest.infoServPrest.ideEstabPrest.tpInscEstabPrest.cdata, 1, '1')
    if 'nrInscEstabPrest' in dir(evtServPrest.infoServPrest.ideEstabPrest): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.infoServPrest.ideEstabPrest.nrInscEstabPrest', evtServPrest.infoServPrest.ideEstabPrest.nrInscEstabPrest.cdata, 1, '')
    if 'tpInscTomador' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.infoServPrest.ideEstabPrest.ideTomador.tpInscTomador', evtServPrest.infoServPrest.ideEstabPrest.ideTomador.tpInscTomador.cdata, 1, '1;4')
    if 'nrInscTomador' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.infoServPrest.ideEstabPrest.ideTomador.nrInscTomador', evtServPrest.infoServPrest.ideEstabPrest.ideTomador.nrInscTomador.cdata, 1, '')
    if 'indObra' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.infoServPrest.ideEstabPrest.ideTomador.indObra', evtServPrest.infoServPrest.ideEstabPrest.ideTomador.indObra.cdata, 1, '0;1;2')
    if 'vlrTotalBruto' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalBruto', evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalBruto.cdata, 1, '')
    if 'vlrTotalBaseRet' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalBaseRet', evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalBaseRet.cdata, 1, '')
    if 'vlrTotalRetPrinc' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalRetPrinc', evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalRetPrinc.cdata, 1, '')
    if 'vlrTotalRetAdic' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalRetAdic', evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalRetAdic.cdata, 0, '')
    if 'vlrTotalNRetPrinc' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalNRetPrinc', evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalNRetPrinc.cdata, 0, '')
    if 'vlrTotalNRetAdic' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): validacoes_lista = validar_campo(validacoes_lista,'evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalNRetAdic', evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalNRetAdic.cdata, 0, '')
    if 'nfs' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador):
        for nfs in evtServPrest.infoServPrest.ideEstabPrest.ideTomador.nfs:
            
            if 'serie' in dir(nfs): validacoes_lista = validar_campo(validacoes_lista,'nfs.serie', nfs.serie.cdata, 1, '')
            if 'numDocto' in dir(nfs): validacoes_lista = validar_campo(validacoes_lista,'nfs.numDocto', nfs.numDocto.cdata, 1, '')
            if 'dtEmissaoNF' in dir(nfs): validacoes_lista = validar_campo(validacoes_lista,'nfs.dtEmissaoNF', nfs.dtEmissaoNF.cdata, 1, '')
            if 'vlrBruto' in dir(nfs): validacoes_lista = validar_campo(validacoes_lista,'nfs.vlrBruto', nfs.vlrBruto.cdata, 1, '')
            if 'obs' in dir(nfs): validacoes_lista = validar_campo(validacoes_lista,'nfs.obs', nfs.obs.cdata, 0, '')


            if 'infoTpServ' in dir(nfs):
                for infoTpServ in nfs.infoTpServ:
                    
                    if 'tpServico' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.tpServico', infoTpServ.tpServico.cdata, 1, '')
                    if 'vlrBaseRet' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrBaseRet', infoTpServ.vlrBaseRet.cdata, 1, '')
                    if 'vlrRetencao' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrRetencao', infoTpServ.vlrRetencao.cdata, 1, '')
                    if 'vlrRetSub' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrRetSub', infoTpServ.vlrRetSub.cdata, 0, '')
                    if 'vlrNRetPrinc' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrNRetPrinc', infoTpServ.vlrNRetPrinc.cdata, 0, '')
                    if 'vlrServicos15' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrServicos15', infoTpServ.vlrServicos15.cdata, 0, '')
                    if 'vlrServicos20' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrServicos20', infoTpServ.vlrServicos20.cdata, 0, '')
                    if 'vlrServicos25' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrServicos25', infoTpServ.vlrServicos25.cdata, 0, '')
                    if 'vlrAdicional' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrAdicional', infoTpServ.vlrAdicional.cdata, 0, '')
                    if 'vlrNRetAdic' in dir(infoTpServ): validacoes_lista = validar_campo(validacoes_lista,'infoTpServ.vlrNRetAdic', infoTpServ.vlrNRetAdic.cdata, 0, '')
        
        
    if 'infoProcRetPr' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador):
        for infoProcRetPr in evtServPrest.infoServPrest.ideEstabPrest.ideTomador.infoProcRetPr:
            
            if 'tpProcRetPrinc' in dir(infoProcRetPr): validacoes_lista = validar_campo(validacoes_lista,'infoProcRetPr.tpProcRetPrinc', infoProcRetPr.tpProcRetPrinc.cdata, 1, '1;2')
            if 'nrProcRetPrinc' in dir(infoProcRetPr): validacoes_lista = validar_campo(validacoes_lista,'infoProcRetPr.nrProcRetPrinc', infoProcRetPr.nrProcRetPrinc.cdata, 1, '')
            if 'codSuspPrinc' in dir(infoProcRetPr): validacoes_lista = validar_campo(validacoes_lista,'infoProcRetPr.codSuspPrinc', infoProcRetPr.codSuspPrinc.cdata, 0, '')
            if 'valorPrinc' in dir(infoProcRetPr): validacoes_lista = validar_campo(validacoes_lista,'infoProcRetPr.valorPrinc', infoProcRetPr.valorPrinc.cdata, 1, '')


    if 'infoProcRetAd' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador):
        for infoProcRetAd in evtServPrest.infoServPrest.ideEstabPrest.ideTomador.infoProcRetAd:
            
            if 'tpProcRetAdic' in dir(infoProcRetAd): validacoes_lista = validar_campo(validacoes_lista,'infoProcRetAd.tpProcRetAdic', infoProcRetAd.tpProcRetAdic.cdata, 1, '1;2')
            if 'nrProcRetAdic' in dir(infoProcRetAd): validacoes_lista = validar_campo(validacoes_lista,'infoProcRetAd.nrProcRetAdic', infoProcRetAd.nrProcRetAdic.cdata, 1, '')
            if 'codSuspAdic' in dir(infoProcRetAd): validacoes_lista = validar_campo(validacoes_lista,'infoProcRetAd.codSuspAdic', infoProcRetAd.codSuspAdic.cdata, 0, '')
            if 'valorAdic' in dir(infoProcRetAd): validacoes_lista = validar_campo(validacoes_lista,'infoProcRetAd.valorAdic', infoProcRetAd.valorAdic.cdata, 1, '')


    return validacoes_lista