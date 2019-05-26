#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r2060.models import *



def read_r2060_evtcprb_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2060_evtcprb_obj(doc, status, validar)
    return dados



def read_r2060_evtcprb(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2060_evtcprb_obj(doc, status, validar)
    return dados



def read_r2060_evtcprb_obj(doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r2060_evtcprb_dados = {}
    r2060_evtcprb_dados['status'] = status
    r2060_evtcprb_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2060_evtcprb_dados['identidade'] = doc.Reinf.evtCPRB['id']
    evtCPRB = doc.Reinf.evtCPRB
    
    try:
        r2060_evtcprb_dados['indretif'] = evtCPRB.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        r2060_evtcprb_dados['nrrecibo'] = evtCPRB.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        r2060_evtcprb_dados['perapur'] = evtCPRB.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        r2060_evtcprb_dados['tpamb'] = evtCPRB.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        r2060_evtcprb_dados['procemi'] = evtCPRB.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        r2060_evtcprb_dados['verproc'] = evtCPRB.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        r2060_evtcprb_dados['tpinsc'] = evtCPRB.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r2060_evtcprb_dados['nrinsc'] = evtCPRB.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r2060_evtcprb_dados['tpinscestab'] = evtCPRB.infoCPRB.ideEstab.tpInscEstab.cdata
    except AttributeError: 
        pass
    
    try:
        r2060_evtcprb_dados['nrinscestab'] = evtCPRB.infoCPRB.ideEstab.nrInscEstab.cdata
    except AttributeError: 
        pass
    
    try:
        r2060_evtcprb_dados['vlrrecbrutatotal'] = evtCPRB.infoCPRB.ideEstab.vlrRecBrutaTotal.cdata
    except AttributeError: 
        pass
    
    try:
        r2060_evtcprb_dados['vlrcpapurtotal'] = evtCPRB.infoCPRB.ideEstab.vlrCPApurTotal.cdata
    except AttributeError: 
        pass
    
    try:
        r2060_evtcprb_dados['vlrcprbsusptotal'] = evtCPRB.infoCPRB.ideEstab.vlrCPRBSuspTotal.cdata
    except AttributeError: 
        pass
        
    r2060_evtcprb = r2060evtCPRB.objects.create(**r2060_evtcprb_dados)
    
    if 'tipoCod' in dir(evtCPRB.infoCPRB.ideEstab):
    
        for tipoCod in evtCPRB.infoCPRB.ideEstab.tipoCod:
    
            r2060_tipocod_dados = {}
            r2060_tipocod_dados['r2060_evtcprb_id'] = r2060_evtcprb.id
            
            try:
                r2060_tipocod_dados['codativecon'] = tipoCod.codAtivEcon.cdata
            except AttributeError: 
                pass
            
            try:
                r2060_tipocod_dados['vlrrecbrutaativ'] = tipoCod.vlrRecBrutaAtiv.cdata
            except AttributeError: 
                pass
            
            try:
                r2060_tipocod_dados['vlrexcrecbruta'] = tipoCod.vlrExcRecBruta.cdata
            except AttributeError: 
                pass
            
            try:
                r2060_tipocod_dados['vlradicrecbruta'] = tipoCod.vlrAdicRecBruta.cdata
            except AttributeError: 
                pass
            
            try:
                r2060_tipocod_dados['vlrbccprb'] = tipoCod.vlrBcCPRB.cdata
            except AttributeError: 
                pass
            
            try:
                r2060_tipocod_dados['vlrcprbapur'] = tipoCod.vlrCPRBapur.cdata
            except AttributeError: 
                pass
            
            try:
                r2060_tipocod_dados['observ'] = tipoCod.observ.cdata
            except AttributeError: 
                pass
    
            r2060_tipocod = r2060tipoCod.objects.create(**r2060_tipocod_dados)
            
            if 'tipoAjuste' in dir(tipoCod):
            
                for tipoAjuste in tipoCod.tipoAjuste:
            
                    r2060_tipoajuste_dados = {}
                    r2060_tipoajuste_dados['r2060_tipocod_id'] = r2060_tipocod.id
                    
                    try:
                        r2060_tipoajuste_dados['tpajuste'] = tipoAjuste.tpAjuste.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2060_tipoajuste_dados['codajuste'] = tipoAjuste.codAjuste.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2060_tipoajuste_dados['vlrajuste'] = tipoAjuste.vlrAjuste.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2060_tipoajuste_dados['descajuste'] = tipoAjuste.descAjuste.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2060_tipoajuste_dados['dtajuste'] = tipoAjuste.dtAjuste.cdata
                    except AttributeError: 
                        pass
            
                    r2060_tipoajuste = r2060tipoAjuste.objects.create(**r2060_tipoajuste_dados)
            
            if 'infoProc' in dir(tipoCod):
            
                for infoProc in tipoCod.infoProc:
            
                    r2060_infoproc_dados = {}
                    r2060_infoproc_dados['r2060_tipocod_id'] = r2060_tipocod.id
                    
                    try:
                        r2060_infoproc_dados['tpproc'] = infoProc.tpProc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2060_infoproc_dados['nrproc'] = infoProc.nrProc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2060_infoproc_dados['codsusp'] = infoProc.codSusp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2060_infoproc_dados['vlrcprbsusp'] = infoProc.vlrCPRBSusp.cdata
                    except AttributeError: 
                        pass
            
                    r2060_infoproc = r2060infoProc.objects.create(**r2060_infoproc_dados)    
    r2060_evtcprb_dados['evento'] = 'r2060'
    r2060_evtcprb_dados['id'] = r2060_evtcprb.id
    r2060_evtcprb_dados['identidade_evento'] = doc.Reinf.evtCPRB['id']
    r2060_evtcprb_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r2060_evtcprb_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(r2060_evtcprb.id)
    return r2060_evtcprb_dados