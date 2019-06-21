#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r2020.models import *



def read_r2020_evtservprest_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2020_evtservprest_obj(request, doc, status, validar)
    return dados



def read_r2020_evtservprest(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2020_evtservprest_obj(request, doc, status, validar)

    r2020evtServPrest.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_r2020_evtservprest_obj(request, doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r2020_evtservprest_dados = {}
    r2020_evtservprest_dados['status'] = status
    r2020_evtservprest_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2020_evtservprest_dados['identidade'] = doc.Reinf.evtServPrest['id']
    evtServPrest = doc.Reinf.evtServPrest
    
    try:
        r2020_evtservprest_dados['indretif'] = evtServPrest.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['nrrecibo'] = evtServPrest.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['perapur'] = evtServPrest.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['tpamb'] = evtServPrest.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['procemi'] = evtServPrest.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['verproc'] = evtServPrest.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['tpinsc'] = evtServPrest.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['nrinsc'] = evtServPrest.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['tpinscestabprest'] = evtServPrest.infoServPrest.ideEstabPrest.tpInscEstabPrest.cdata
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['nrinscestabprest'] = evtServPrest.infoServPrest.ideEstabPrest.nrInscEstabPrest.cdata
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['tpinsctomador'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.tpInscTomador.cdata
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['nrinsctomador'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.nrInscTomador.cdata
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['indobra'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.indObra.cdata
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['vlrtotalbruto'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalBruto.cdata.replace('.', '').replace(',', '.')
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['vlrtotalbaseret'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalBaseRet.cdata.replace('.', '').replace(',', '.')
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['vlrtotalretprinc'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalRetPrinc.cdata.replace('.', '').replace(',', '.')
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['vlrtotalretadic'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalRetAdic.cdata.replace('.', '').replace(',', '.')
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['vlrtotalnretprinc'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalNRetPrinc.cdata.replace('.', '').replace(',', '.')
    except AttributeError: 
        pass
    
    try:
        r2020_evtservprest_dados['vlrtotalnretadic'] = evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalNRetAdic.cdata.replace('.', '').replace(',', '.')
    except AttributeError: 
        pass
        
    r2020_evtservprest = r2020evtServPrest.objects.create(**r2020_evtservprest_dados)
    
    if 'infoServPrest' in dir(evtServPrest) and 'ideEstabPrest' in dir(evtServPrest.infoServPrest) and 'ideTomador' in dir(evtServPrest.infoServPrest.ideEstabPrest) and 'nfs' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador):
    
        for nfs in evtServPrest.infoServPrest.ideEstabPrest.ideTomador.nfs:
    
            r2020_nfs_dados = {}
            r2020_nfs_dados['r2020_evtservprest_id'] = r2020_evtservprest.id
            
            try:
                r2020_nfs_dados['serie'] = nfs.serie.cdata
            except AttributeError: 
                pass
            
            try:
                r2020_nfs_dados['numdocto'] = nfs.numDocto.cdata
            except AttributeError: 
                pass
            
            try:
                r2020_nfs_dados['dtemissaonf'] = nfs.dtEmissaoNF.cdata
            except AttributeError: 
                pass
            
            try:
                r2020_nfs_dados['vlrbruto'] = nfs.vlrBruto.cdata.replace('.', '').replace(',', '.')
            except AttributeError: 
                pass
            
            try:
                r2020_nfs_dados['obs'] = nfs.obs.cdata
            except AttributeError: 
                pass
    
            r2020_nfs = r2020nfs.objects.create(**r2020_nfs_dados)
            
            if 'infoTpServ' in dir(nfs):
            
                for infoTpServ in nfs.infoTpServ:
            
                    r2020_infotpserv_dados = {}
                    r2020_infotpserv_dados['r2020_nfs_id'] = r2020_nfs.id
                    
                    try:
                        r2020_infotpserv_dados['tpservico'] = infoTpServ.tpServico.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2020_infotpserv_dados['vlrbaseret'] = infoTpServ.vlrBaseRet.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r2020_infotpserv_dados['vlrretencao'] = infoTpServ.vlrRetencao.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r2020_infotpserv_dados['vlrretsub'] = infoTpServ.vlrRetSub.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r2020_infotpserv_dados['vlrnretprinc'] = infoTpServ.vlrNRetPrinc.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r2020_infotpserv_dados['vlrservicos15'] = infoTpServ.vlrServicos15.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r2020_infotpserv_dados['vlrservicos20'] = infoTpServ.vlrServicos20.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r2020_infotpserv_dados['vlrservicos25'] = infoTpServ.vlrServicos25.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r2020_infotpserv_dados['vlradicional'] = infoTpServ.vlrAdicional.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r2020_infotpserv_dados['vlrnretadic'] = infoTpServ.vlrNRetAdic.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
            
                    r2020_infotpserv = r2020infoTpServ.objects.create(**r2020_infotpserv_dados)
    
    if 'infoServPrest' in dir(evtServPrest) and 'ideEstabPrest' in dir(evtServPrest.infoServPrest) and 'ideTomador' in dir(evtServPrest.infoServPrest.ideEstabPrest) and 'infoProcRetPr' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador):
    
        for infoProcRetPr in evtServPrest.infoServPrest.ideEstabPrest.ideTomador.infoProcRetPr:
    
            r2020_infoprocretpr_dados = {}
            r2020_infoprocretpr_dados['r2020_evtservprest_id'] = r2020_evtservprest.id
            
            try:
                r2020_infoprocretpr_dados['tpprocretprinc'] = infoProcRetPr.tpProcRetPrinc.cdata
            except AttributeError: 
                pass
            
            try:
                r2020_infoprocretpr_dados['nrprocretprinc'] = infoProcRetPr.nrProcRetPrinc.cdata
            except AttributeError: 
                pass
            
            try:
                r2020_infoprocretpr_dados['codsuspprinc'] = infoProcRetPr.codSuspPrinc.cdata
            except AttributeError: 
                pass
            
            try:
                r2020_infoprocretpr_dados['valorprinc'] = infoProcRetPr.valorPrinc.cdata
            except AttributeError: 
                pass
    
            r2020_infoprocretpr = r2020infoProcRetPr.objects.create(**r2020_infoprocretpr_dados)
    
    if 'infoServPrest' in dir(evtServPrest) and 'ideEstabPrest' in dir(evtServPrest.infoServPrest) and 'ideTomador' in dir(evtServPrest.infoServPrest.ideEstabPrest) and 'infoProcRetAd' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador):
    
        for infoProcRetAd in evtServPrest.infoServPrest.ideEstabPrest.ideTomador.infoProcRetAd:
    
            r2020_infoprocretad_dados = {}
            r2020_infoprocretad_dados['r2020_evtservprest_id'] = r2020_evtservprest.id
            
            try:
                r2020_infoprocretad_dados['tpprocretadic'] = infoProcRetAd.tpProcRetAdic.cdata
            except AttributeError: 
                pass
            
            try:
                r2020_infoprocretad_dados['nrprocretadic'] = infoProcRetAd.nrProcRetAdic.cdata
            except AttributeError: 
                pass
            
            try:
                r2020_infoprocretad_dados['codsuspadic'] = infoProcRetAd.codSuspAdic.cdata
            except AttributeError: 
                pass
            
            try:
                r2020_infoprocretad_dados['valoradic'] = infoProcRetAd.valorAdic.cdata
            except AttributeError: 
                pass
    
            r2020_infoprocretad = r2020infoProcRetAd.objects.create(**r2020_infoprocretad_dados)    
    r2020_evtservprest_dados['evento'] = 'r2020'
    r2020_evtservprest_dados['id'] = r2020_evtservprest.id
    r2020_evtservprest_dados['identidade_evento'] = doc.Reinf.evtServPrest['id']
    r2020_evtservprest_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r2020_evtservprest_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, r2020_evtservprest.id)
    
    return r2020_evtservprest_dados