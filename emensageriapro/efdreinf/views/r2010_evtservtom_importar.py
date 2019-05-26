#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r2010.models import *



def read_r2010_evtservtom_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2010_evtservtom_obj(doc, status, validar)
    return dados



def read_r2010_evtservtom(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2010_evtservtom_obj(doc, status, validar)
    return dados



def read_r2010_evtservtom_obj(doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r2010_evtservtom_dados = {}
    r2010_evtservtom_dados['status'] = status
    r2010_evtservtom_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2010_evtservtom_dados['identidade'] = doc.Reinf.evtServTom['id']
    evtServTom = doc.Reinf.evtServTom
    
    try:
        r2010_evtservtom_dados['indretif'] = evtServTom.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['nrrecibo'] = evtServTom.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['perapur'] = evtServTom.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['tpamb'] = evtServTom.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['procemi'] = evtServTom.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['verproc'] = evtServTom.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['tpinsc'] = evtServTom.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['nrinsc'] = evtServTom.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['tpinscestab'] = evtServTom.infoServTom.ideEstabObra.tpInscEstab.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['nrinscestab'] = evtServTom.infoServTom.ideEstabObra.nrInscEstab.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['indobra'] = evtServTom.infoServTom.ideEstabObra.indObra.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['cnpjprestador'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.cnpjPrestador.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['vlrtotalbruto'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalBruto.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['vlrtotalbaseret'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalBaseRet.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['vlrtotalretprinc'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalRetPrinc.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['vlrtotalretadic'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalRetAdic.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['vlrtotalnretprinc'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalNRetPrinc.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['vlrtotalnretadic'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalNRetAdic.cdata
    except AttributeError: 
        pass
    
    try:
        r2010_evtservtom_dados['indcprb'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.indCPRB.cdata
    except AttributeError: 
        pass
        
    r2010_evtservtom = r2010evtServTom.objects.create(**r2010_evtservtom_dados)
    
    if 'nfs' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ):
    
        for nfs in evtServTom.infoServTom.ideEstabObra.idePrestServ.nfs:
    
            r2010_nfs_dados = {}
            r2010_nfs_dados['r2010_evtservtom_id'] = r2010_evtservtom.id
            
            try:
                r2010_nfs_dados['serie'] = nfs.serie.cdata
            except AttributeError: 
                pass
            
            try:
                r2010_nfs_dados['numdocto'] = nfs.numDocto.cdata
            except AttributeError: 
                pass
            
            try:
                r2010_nfs_dados['dtemissaonf'] = nfs.dtEmissaoNF.cdata
            except AttributeError: 
                pass
            
            try:
                r2010_nfs_dados['vlrbruto'] = nfs.vlrBruto.cdata
            except AttributeError: 
                pass
            
            try:
                r2010_nfs_dados['obs'] = nfs.obs.cdata
            except AttributeError: 
                pass
    
            r2010_nfs = r2010nfs.objects.create(**r2010_nfs_dados)
            
            if 'infoTpServ' in dir(nfs):
            
                for infoTpServ in nfs.infoTpServ:
            
                    r2010_infotpserv_dados = {}
                    r2010_infotpserv_dados['r2010_nfs_id'] = r2010_nfs.id
                    
                    try:
                        r2010_infotpserv_dados['tpservico'] = infoTpServ.tpServico.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2010_infotpserv_dados['vlrbaseret'] = infoTpServ.vlrBaseRet.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2010_infotpserv_dados['vlrretencao'] = infoTpServ.vlrRetencao.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2010_infotpserv_dados['vlrretsub'] = infoTpServ.vlrRetSub.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2010_infotpserv_dados['vlrnretprinc'] = infoTpServ.vlrNRetPrinc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2010_infotpserv_dados['vlrservicos15'] = infoTpServ.vlrServicos15.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2010_infotpserv_dados['vlrservicos20'] = infoTpServ.vlrServicos20.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2010_infotpserv_dados['vlrservicos25'] = infoTpServ.vlrServicos25.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2010_infotpserv_dados['vlradicional'] = infoTpServ.vlrAdicional.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2010_infotpserv_dados['vlrnretadic'] = infoTpServ.vlrNRetAdic.cdata
                    except AttributeError: 
                        pass
            
                    r2010_infotpserv = r2010infoTpServ.objects.create(**r2010_infotpserv_dados)
    
    if 'infoProcRetPr' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ):
    
        for infoProcRetPr in evtServTom.infoServTom.ideEstabObra.idePrestServ.infoProcRetPr:
    
            r2010_infoprocretpr_dados = {}
            r2010_infoprocretpr_dados['r2010_evtservtom_id'] = r2010_evtservtom.id
            
            try:
                r2010_infoprocretpr_dados['tpprocretprinc'] = infoProcRetPr.tpProcRetPrinc.cdata
            except AttributeError: 
                pass
            
            try:
                r2010_infoprocretpr_dados['nrprocretprinc'] = infoProcRetPr.nrProcRetPrinc.cdata
            except AttributeError: 
                pass
            
            try:
                r2010_infoprocretpr_dados['codsuspprinc'] = infoProcRetPr.codSuspPrinc.cdata
            except AttributeError: 
                pass
            
            try:
                r2010_infoprocretpr_dados['valorprinc'] = infoProcRetPr.valorPrinc.cdata
            except AttributeError: 
                pass
    
            r2010_infoprocretpr = r2010infoProcRetPr.objects.create(**r2010_infoprocretpr_dados)
    
    if 'infoProcRetAd' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ):
    
        for infoProcRetAd in evtServTom.infoServTom.ideEstabObra.idePrestServ.infoProcRetAd:
    
            r2010_infoprocretad_dados = {}
            r2010_infoprocretad_dados['r2010_evtservtom_id'] = r2010_evtservtom.id
            
            try:
                r2010_infoprocretad_dados['tpprocretadic'] = infoProcRetAd.tpProcRetAdic.cdata
            except AttributeError: 
                pass
            
            try:
                r2010_infoprocretad_dados['nrprocretadic'] = infoProcRetAd.nrProcRetAdic.cdata
            except AttributeError: 
                pass
            
            try:
                r2010_infoprocretad_dados['codsuspadic'] = infoProcRetAd.codSuspAdic.cdata
            except AttributeError: 
                pass
            
            try:
                r2010_infoprocretad_dados['valoradic'] = infoProcRetAd.valorAdic.cdata
            except AttributeError: 
                pass
    
            r2010_infoprocretad = r2010infoProcRetAd.objects.create(**r2010_infoprocretad_dados)    
    r2010_evtservtom_dados['evento'] = 'r2010'
    r2010_evtservtom_dados['id'] = r2010_evtservtom.id
    r2010_evtservtom_dados['identidade_evento'] = doc.Reinf.evtServTom['id']
    r2010_evtservtom_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r2010_evtservtom_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(r2010_evtservtom.id)
    return r2010_evtservtom_dados