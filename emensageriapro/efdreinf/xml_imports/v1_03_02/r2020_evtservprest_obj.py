#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_r2020_evtservprest_obj(doc):
    r2020_evtservprest_dados = {}
    r2020_evtservprest_dados['versao'] = 'v1_03_02'
    r2020_evtservprest_dados['status'] = 12
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
    dados['status'] = 1


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

    return dados