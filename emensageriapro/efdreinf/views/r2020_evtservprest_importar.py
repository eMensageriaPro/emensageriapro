#coding:utf-8
"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos <www.emensageria.com.br>
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
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO



def read_r2020_evtservprest_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r2020_evtservprest_obj(doc, status, validar)
    return dados

def read_r2020_evtservprest(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r2020_evtservprest_obj(doc, status, validar)
    return dados



def read_r2020_evtservprest_obj(doc, status, validar=False):
    r2020_evtservprest_dados = {}
    r2020_evtservprest_dados['status'] = status
    xmlns_lista = doc.Reinf['xmlns'].split('/')
    r2020_evtservprest_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2020_evtservprest_dados['identidade'] = doc.Reinf.evtServPrest['id']
    r2020_evtservprest_dados['processamento_codigo_resposta'] = 1
    evtServPrest = doc.Reinf.evtServPrest

    if 'indRetif' in dir(evtServPrest.ideEvento): r2020_evtservprest_dados['indretif'] = evtServPrest.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtServPrest.ideEvento): r2020_evtservprest_dados['nrrecibo'] = evtServPrest.ideEvento.nrRecibo.cdata
    if 'perApur' in dir(evtServPrest.ideEvento): r2020_evtservprest_dados['perapur'] = evtServPrest.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtServPrest.ideEvento): r2020_evtservprest_dados['tpamb'] = evtServPrest.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtServPrest.ideEvento): r2020_evtservprest_dados['procemi'] = evtServPrest.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtServPrest.ideEvento): r2020_evtservprest_dados['verproc'] = evtServPrest.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtServPrest.ideContri): r2020_evtservprest_dados['tpinsc'] = evtServPrest.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtServPrest.ideContri): r2020_evtservprest_dados['nrinsc'] = evtServPrest.ideContri.nrInsc.cdata
    if 'tpInscEstabPrest' in dir(evtServPrest.infoServPrest.ideEstabPrest): r2020_evtservprest_dados['tpinscestabprest'] = evtServPrest.infoServPrest.ideEstabPrest.tpInscEstabPrest.cdata
    if 'nrInscEstabPrest' in dir(evtServPrest.infoServPrest.ideEstabPrest): r2020_evtservprest_dados['nrinscestabprest'] = evtServPrest.infoServPrest.ideEstabPrest.nrInscEstabPrest.cdata
    if 'tpInscTomador' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): r2020_evtservprest_dados['tpinsctomador'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.tpInscTomador.cdata
    if 'nrInscTomador' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): r2020_evtservprest_dados['nrinsctomador'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.nrInscTomador.cdata
    if 'indObra' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): r2020_evtservprest_dados['indobra'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.indObra.cdata
    if 'vlrTotalBruto' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): r2020_evtservprest_dados['vlrtotalbruto'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalBruto.cdata
    if 'vlrTotalBaseRet' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): r2020_evtservprest_dados['vlrtotalbaseret'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalBaseRet.cdata
    if 'vlrTotalRetPrinc' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): r2020_evtservprest_dados['vlrtotalretprinc'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalRetPrinc.cdata
    if 'vlrTotalRetAdic' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): r2020_evtservprest_dados['vlrtotalretadic'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalRetAdic.cdata
    if 'vlrTotalNRetPrinc' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): r2020_evtservprest_dados['vlrtotalnretprinc'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalNRetPrinc.cdata
    if 'vlrTotalNRetAdic' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador): r2020_evtservprest_dados['vlrtotalnretadic'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalNRetAdic.cdata
    if 'inclusao' in dir(evtServPrest.infoServPrest): r2020_evtservprest_dados['operacao'] = 1
    elif 'alteracao' in dir(evtServPrest.infoServPrest): r2020_evtservprest_dados['operacao'] = 2
    elif 'exclusao' in dir(evtServPrest.infoServPrest): r2020_evtservprest_dados['operacao'] = 3
    #print dados
    insert = create_insert('r2020_evtservprest', r2020_evtservprest_dados)
    resp = executar_sql(insert, True)
    r2020_evtservprest_id = resp[0][0]
    dados = r2020_evtservprest_dados
    dados['evento'] = 'r2020'
    dados['id'] = r2020_evtservprest_id
    dados['identidade_evento'] = doc.Reinf.evtServPrest['id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'nfs' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador):
        for nfs in evtServPrest.infoServPrest.ideEstabPrest.ideTomador.nfs:
            r2020_nfs_dados = {}
            r2020_nfs_dados['r2020_evtservprest_id'] = r2020_evtservprest_id

            if 'serie' in dir(nfs): r2020_nfs_dados['serie'] = nfs.serie.cdata
            if 'numDocto' in dir(nfs): r2020_nfs_dados['numdocto'] = nfs.numDocto.cdata
            if 'dtEmissaoNF' in dir(nfs): r2020_nfs_dados['dtemissaonf'] = nfs.dtEmissaoNF.cdata
            if 'vlrBruto' in dir(nfs): r2020_nfs_dados['vlrbruto'] = nfs.vlrBruto.cdata
            if 'obs' in dir(nfs): r2020_nfs_dados['obs'] = nfs.obs.cdata
            insert = create_insert('r2020_nfs', r2020_nfs_dados)
            resp = executar_sql(insert, True)
            r2020_nfs_id = resp[0][0]
            #print r2020_nfs_id

            if 'infoTpServ' in dir(nfs):
                for infoTpServ in nfs.infoTpServ:
                    r2020_infotpserv_dados = {}
                    r2020_infotpserv_dados['r2020_nfs_id'] = r2020_nfs_id

                    if 'tpServico' in dir(infoTpServ): r2020_infotpserv_dados['tpservico'] = infoTpServ.tpServico.cdata
                    if 'vlrBaseRet' in dir(infoTpServ): r2020_infotpserv_dados['vlrbaseret'] = infoTpServ.vlrBaseRet.cdata
                    if 'vlrRetencao' in dir(infoTpServ): r2020_infotpserv_dados['vlrretencao'] = infoTpServ.vlrRetencao.cdata
                    if 'vlrRetSub' in dir(infoTpServ): r2020_infotpserv_dados['vlrretsub'] = infoTpServ.vlrRetSub.cdata
                    if 'vlrNRetPrinc' in dir(infoTpServ): r2020_infotpserv_dados['vlrnretprinc'] = infoTpServ.vlrNRetPrinc.cdata
                    if 'vlrServicos15' in dir(infoTpServ): r2020_infotpserv_dados['vlrservicos15'] = infoTpServ.vlrServicos15.cdata
                    if 'vlrServicos20' in dir(infoTpServ): r2020_infotpserv_dados['vlrservicos20'] = infoTpServ.vlrServicos20.cdata
                    if 'vlrServicos25' in dir(infoTpServ): r2020_infotpserv_dados['vlrservicos25'] = infoTpServ.vlrServicos25.cdata
                    if 'vlrAdicional' in dir(infoTpServ): r2020_infotpserv_dados['vlradicional'] = infoTpServ.vlrAdicional.cdata
                    if 'vlrNRetAdic' in dir(infoTpServ): r2020_infotpserv_dados['vlrnretadic'] = infoTpServ.vlrNRetAdic.cdata
                    insert = create_insert('r2020_infotpserv', r2020_infotpserv_dados)
                    resp = executar_sql(insert, True)
                    r2020_infotpserv_id = resp[0][0]
                    #print r2020_infotpserv_id

    if 'infoProcRetPr' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador):
        for infoProcRetPr in evtServPrest.infoServPrest.ideEstabPrest.ideTomador.infoProcRetPr:
            r2020_infoprocretpr_dados = {}
            r2020_infoprocretpr_dados['r2020_evtservprest_id'] = r2020_evtservprest_id

            if 'tpProcRetPrinc' in dir(infoProcRetPr): r2020_infoprocretpr_dados['tpprocretprinc'] = infoProcRetPr.tpProcRetPrinc.cdata
            if 'nrProcRetPrinc' in dir(infoProcRetPr): r2020_infoprocretpr_dados['nrprocretprinc'] = infoProcRetPr.nrProcRetPrinc.cdata
            if 'codSuspPrinc' in dir(infoProcRetPr): r2020_infoprocretpr_dados['codsuspprinc'] = infoProcRetPr.codSuspPrinc.cdata
            if 'valorPrinc' in dir(infoProcRetPr): r2020_infoprocretpr_dados['valorprinc'] = infoProcRetPr.valorPrinc.cdata
            insert = create_insert('r2020_infoprocretpr', r2020_infoprocretpr_dados)
            resp = executar_sql(insert, True)
            r2020_infoprocretpr_id = resp[0][0]
            #print r2020_infoprocretpr_id

    if 'infoProcRetAd' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador):
        for infoProcRetAd in evtServPrest.infoServPrest.ideEstabPrest.ideTomador.infoProcRetAd:
            r2020_infoprocretad_dados = {}
            r2020_infoprocretad_dados['r2020_evtservprest_id'] = r2020_evtservprest_id

            if 'tpProcRetAdic' in dir(infoProcRetAd): r2020_infoprocretad_dados['tpprocretadic'] = infoProcRetAd.tpProcRetAdic.cdata
            if 'nrProcRetAdic' in dir(infoProcRetAd): r2020_infoprocretad_dados['nrprocretadic'] = infoProcRetAd.nrProcRetAdic.cdata
            if 'codSuspAdic' in dir(infoProcRetAd): r2020_infoprocretad_dados['codsuspadic'] = infoProcRetAd.codSuspAdic.cdata
            if 'valorAdic' in dir(infoProcRetAd): r2020_infoprocretad_dados['valoradic'] = infoProcRetAd.valorAdic.cdata
            insert = create_insert('r2020_infoprocretad', r2020_infoprocretad_dados)
            resp = executar_sql(insert, True)
            r2020_infoprocretad_id = resp[0][0]
            #print r2020_infoprocretad_id

    from emensageriapro.efdreinf.views.r2020_evtservprest_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r2020_evtservprest_id, 'default')
    return dados