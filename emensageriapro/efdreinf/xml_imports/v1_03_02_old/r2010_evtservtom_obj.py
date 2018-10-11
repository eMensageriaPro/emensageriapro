#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_r2010_evtservtom_obj(doc):
    r2010_evtservtom_dados = {}
    r2010_evtservtom_dados['versao'] = 'v1_03_02'
    r2010_evtservtom_dados['status'] = 12
    r2010_evtservtom_dados['identidade'] = doc.Reinf.evtServTom['id']
    r2010_evtservtom_dados['processamento_codigo_resposta'] = 1
    evtServTom = doc.Reinf.evtServTom
    
    if 'indRetif' in dir(evtServTom.ideEvento): r2010_evtservtom_dados['indretif'] = evtServTom.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtServTom.ideEvento): r2010_evtservtom_dados['nrrecibo'] = evtServTom.ideEvento.nrRecibo.cdata
    if 'perApur' in dir(evtServTom.ideEvento): r2010_evtservtom_dados['perapur'] = evtServTom.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtServTom.ideEvento): r2010_evtservtom_dados['tpamb'] = evtServTom.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtServTom.ideEvento): r2010_evtservtom_dados['procemi'] = evtServTom.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtServTom.ideEvento): r2010_evtservtom_dados['verproc'] = evtServTom.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtServTom.ideContri): r2010_evtservtom_dados['tpinsc'] = evtServTom.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtServTom.ideContri): r2010_evtservtom_dados['nrinsc'] = evtServTom.ideContri.nrInsc.cdata
    if 'tpInscEstab' in dir(evtServTom.infoServTom.ideEstabObra): r2010_evtservtom_dados['tpinscestab'] = evtServTom.infoServTom.ideEstabObra.tpInscEstab.cdata
    if 'nrInscEstab' in dir(evtServTom.infoServTom.ideEstabObra): r2010_evtservtom_dados['nrinscestab'] = evtServTom.infoServTom.ideEstabObra.nrInscEstab.cdata
    if 'indObra' in dir(evtServTom.infoServTom.ideEstabObra): r2010_evtservtom_dados['indobra'] = evtServTom.infoServTom.ideEstabObra.indObra.cdata
    if 'cnpjPrestador' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): r2010_evtservtom_dados['cnpjprestador'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.cnpjPrestador.cdata
    if 'vlrTotalBruto' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): r2010_evtservtom_dados['vlrtotalbruto'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalBruto.cdata
    if 'vlrTotalBaseRet' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): r2010_evtservtom_dados['vlrtotalbaseret'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalBaseRet.cdata
    if 'vlrTotalRetPrinc' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): r2010_evtservtom_dados['vlrtotalretprinc'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalRetPrinc.cdata
    if 'vlrTotalRetAdic' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): r2010_evtservtom_dados['vlrtotalretadic'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalRetAdic.cdata
    if 'vlrTotalNRetPrinc' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): r2010_evtservtom_dados['vlrtotalnretprinc'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalNRetPrinc.cdata
    if 'vlrTotalNRetAdic' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): r2010_evtservtom_dados['vlrtotalnretadic'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalNRetAdic.cdata
    if 'indCPRB' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): r2010_evtservtom_dados['indcprb'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.indCPRB.cdata
    if 'inclusao' in dir(evtServTom.infoServTom): r2010_evtservtom_dados['operacao'] = 1
    elif 'alteracao' in dir(evtServTom.infoServTom): r2010_evtservtom_dados['operacao'] = 2
    elif 'exclusao' in dir(evtServTom.infoServTom): r2010_evtservtom_dados['operacao'] = 3
    #print dados
    insert = create_insert('r2010_evtservtom', r2010_evtservtom_dados)
    resp = executar_sql(insert, True)
    r2010_evtservtom_id = resp[0][0]
    dados = r2010_evtservtom_dados
    dados['evento'] = 'r2010'
    dados['id'] = r2010_evtservtom_id
    dados['identidade_evento'] = doc.Reinf.evtServTom['id']
    dados['status'] = 1


    if 'nfs' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ):
        for nfs in evtServTom.infoServTom.ideEstabObra.idePrestServ.nfs:
            r2010_nfs_dados = {}
            r2010_nfs_dados['r2010_evtservtom_id'] = r2010_evtservtom_id
            
            if 'serie' in dir(nfs): r2010_nfs_dados['serie'] = nfs.serie.cdata
            if 'numDocto' in dir(nfs): r2010_nfs_dados['numdocto'] = nfs.numDocto.cdata
            if 'dtEmissaoNF' in dir(nfs): r2010_nfs_dados['dtemissaonf'] = nfs.dtEmissaoNF.cdata
            if 'vlrBruto' in dir(nfs): r2010_nfs_dados['vlrbruto'] = nfs.vlrBruto.cdata
            if 'obs' in dir(nfs): r2010_nfs_dados['obs'] = nfs.obs.cdata
            insert = create_insert('r2010_nfs', r2010_nfs_dados)
            resp = executar_sql(insert, True)
            r2010_nfs_id = resp[0][0]
            #print r2010_nfs_id

            if 'infoTpServ' in dir(nfs):
                for infoTpServ in nfs.infoTpServ:
                    r2010_infotpserv_dados = {}
                    r2010_infotpserv_dados['r2010_nfs_id'] = r2010_nfs_id
                    
                    if 'tpServico' in dir(infoTpServ): r2010_infotpserv_dados['tpservico'] = infoTpServ.tpServico.cdata
                    if 'vlrBaseRet' in dir(infoTpServ): r2010_infotpserv_dados['vlrbaseret'] = infoTpServ.vlrBaseRet.cdata
                    if 'vlrRetencao' in dir(infoTpServ): r2010_infotpserv_dados['vlrretencao'] = infoTpServ.vlrRetencao.cdata
                    if 'vlrRetSub' in dir(infoTpServ): r2010_infotpserv_dados['vlrretsub'] = infoTpServ.vlrRetSub.cdata
                    if 'vlrNRetPrinc' in dir(infoTpServ): r2010_infotpserv_dados['vlrnretprinc'] = infoTpServ.vlrNRetPrinc.cdata
                    if 'vlrServicos15' in dir(infoTpServ): r2010_infotpserv_dados['vlrservicos15'] = infoTpServ.vlrServicos15.cdata
                    if 'vlrServicos20' in dir(infoTpServ): r2010_infotpserv_dados['vlrservicos20'] = infoTpServ.vlrServicos20.cdata
                    if 'vlrServicos25' in dir(infoTpServ): r2010_infotpserv_dados['vlrservicos25'] = infoTpServ.vlrServicos25.cdata
                    if 'vlrAdicional' in dir(infoTpServ): r2010_infotpserv_dados['vlradicional'] = infoTpServ.vlrAdicional.cdata
                    if 'vlrNRetAdic' in dir(infoTpServ): r2010_infotpserv_dados['vlrnretadic'] = infoTpServ.vlrNRetAdic.cdata
                    insert = create_insert('r2010_infotpserv', r2010_infotpserv_dados)
                    resp = executar_sql(insert, True)
                    r2010_infotpserv_id = resp[0][0]
                    #print r2010_infotpserv_id
        
    if 'infoProcRetPr' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ):
        for infoProcRetPr in evtServTom.infoServTom.ideEstabObra.idePrestServ.infoProcRetPr:
            r2010_infoprocretpr_dados = {}
            r2010_infoprocretpr_dados['r2010_evtservtom_id'] = r2010_evtservtom_id
            
            if 'tpProcRetPrinc' in dir(infoProcRetPr): r2010_infoprocretpr_dados['tpprocretprinc'] = infoProcRetPr.tpProcRetPrinc.cdata
            if 'nrProcRetPrinc' in dir(infoProcRetPr): r2010_infoprocretpr_dados['nrprocretprinc'] = infoProcRetPr.nrProcRetPrinc.cdata
            if 'codSuspPrinc' in dir(infoProcRetPr): r2010_infoprocretpr_dados['codsuspprinc'] = infoProcRetPr.codSuspPrinc.cdata
            if 'valorPrinc' in dir(infoProcRetPr): r2010_infoprocretpr_dados['valorprinc'] = infoProcRetPr.valorPrinc.cdata
            insert = create_insert('r2010_infoprocretpr', r2010_infoprocretpr_dados)
            resp = executar_sql(insert, True)
            r2010_infoprocretpr_id = resp[0][0]
            #print r2010_infoprocretpr_id

    if 'infoProcRetAd' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ):
        for infoProcRetAd in evtServTom.infoServTom.ideEstabObra.idePrestServ.infoProcRetAd:
            r2010_infoprocretad_dados = {}
            r2010_infoprocretad_dados['r2010_evtservtom_id'] = r2010_evtservtom_id
            
            if 'tpProcRetAdic' in dir(infoProcRetAd): r2010_infoprocretad_dados['tpprocretadic'] = infoProcRetAd.tpProcRetAdic.cdata
            if 'nrProcRetAdic' in dir(infoProcRetAd): r2010_infoprocretad_dados['nrprocretadic'] = infoProcRetAd.nrProcRetAdic.cdata
            if 'codSuspAdic' in dir(infoProcRetAd): r2010_infoprocretad_dados['codsuspadic'] = infoProcRetAd.codSuspAdic.cdata
            if 'valorAdic' in dir(infoProcRetAd): r2010_infoprocretad_dados['valoradic'] = infoProcRetAd.valorAdic.cdata
            insert = create_insert('r2010_infoprocretad', r2010_infoprocretad_dados)
            resp = executar_sql(insert, True)
            r2010_infoprocretad_id = resp[0][0]
            #print r2010_infoprocretad_id

    return dados