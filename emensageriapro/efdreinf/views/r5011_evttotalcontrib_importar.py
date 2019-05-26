#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r5011.models import *



def read_r5011_evttotalcontrib_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r5011_evttotalcontrib_obj(doc, status, validar)
    return dados



def read_r5011_evttotalcontrib(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r5011_evttotalcontrib_obj(doc, status, validar)
    return dados



def read_r5011_evttotalcontrib_obj(doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r5011_evttotalcontrib_dados = {}
    r5011_evttotalcontrib_dados['status'] = status
    r5011_evttotalcontrib_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r5011_evttotalcontrib_dados['identidade'] = doc.Reinf.evtTotalContrib['id']
    evtTotalContrib = doc.Reinf.evtTotalContrib
    
    try:
        r5011_evttotalcontrib_dados['perapur'] = evtTotalContrib.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        r5011_evttotalcontrib_dados['tpinsc'] = evtTotalContrib.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r5011_evttotalcontrib_dados['nrinsc'] = evtTotalContrib.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r5011_evttotalcontrib_dados['cdretorno'] = evtTotalContrib.ideRecRetorno.ideStatus.cdRetorno.cdata
    except AttributeError: 
        pass
    
    try:
        r5011_evttotalcontrib_dados['descretorno'] = evtTotalContrib.ideRecRetorno.ideStatus.descRetorno.cdata
    except AttributeError: 
        pass
    
    try:
        r5011_evttotalcontrib_dados['nrprotentr'] = evtTotalContrib.infoRecEv.nrProtEntr.cdata
    except AttributeError: 
        pass
    
    try:
        r5011_evttotalcontrib_dados['dhprocess'] = evtTotalContrib.infoRecEv.dhProcess.cdata
    except AttributeError: 
        pass
    
    try:
        r5011_evttotalcontrib_dados['tpev'] = evtTotalContrib.infoRecEv.tpEv.cdata
    except AttributeError: 
        pass
    
    try:
        r5011_evttotalcontrib_dados['idev'] = evtTotalContrib.infoRecEv.idEv.cdata
    except AttributeError: 
        pass
    
    try:
        r5011_evttotalcontrib_dados['hash'] = evtTotalContrib.infoRecEv.hash.cdata
    except AttributeError: 
        pass
        
    r5011_evttotalcontrib = r5011evtTotalContrib.objects.create(**r5011_evttotalcontrib_dados)
    
    if 'regOcorrs' in dir(evtTotalContrib.ideRecRetorno.ideStatus):
    
        for regOcorrs in evtTotalContrib.ideRecRetorno.ideStatus.regOcorrs:
    
            r5011_regocorrs_dados = {}
            r5011_regocorrs_dados['r5011_evttotalcontrib_id'] = r5011_evttotalcontrib.id
            
            try:
                r5011_regocorrs_dados['tpocorr'] = regOcorrs.tpOcorr.cdata
            except AttributeError: 
                pass
            
            try:
                r5011_regocorrs_dados['localerroaviso'] = regOcorrs.localErroAviso.cdata
            except AttributeError: 
                pass
            
            try:
                r5011_regocorrs_dados['codresp'] = regOcorrs.codResp.cdata
            except AttributeError: 
                pass
            
            try:
                r5011_regocorrs_dados['dscresp'] = regOcorrs.dscResp.cdata
            except AttributeError: 
                pass
    
            r5011_regocorrs = r5011regOcorrs.objects.create(**r5011_regocorrs_dados)
    
    if 'infoTotalContrib' in dir(evtTotalContrib):
    
        for infoTotalContrib in evtTotalContrib.infoTotalContrib:
    
            r5011_infototalcontrib_dados = {}
            r5011_infototalcontrib_dados['r5011_evttotalcontrib_id'] = r5011_evttotalcontrib.id
            
            try:
                r5011_infototalcontrib_dados['nrrecarqbase'] = infoTotalContrib.nrRecArqBase.cdata
            except AttributeError: 
                pass
            
            try:
                r5011_infototalcontrib_dados['indexistinfo'] = infoTotalContrib.indExistInfo.cdata
            except AttributeError: 
                pass
    
            r5011_infototalcontrib = r5011infoTotalContrib.objects.create(**r5011_infototalcontrib_dados)
            
            if 'RTom' in dir(infoTotalContrib):
            
                for RTom in infoTotalContrib.RTom:
            
                    r5011_rtom_dados = {}
                    r5011_rtom_dados['r5011_infototalcontrib_id'] = r5011_infototalcontrib.id
                    
                    try:
                        r5011_rtom_dados['cnpjprestador'] = RTom.cnpjPrestador.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5011_rtom_dados['cno'] = RTom.cno.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5011_rtom_dados['vlrtotalbaseret'] = RTom.vlrTotalBaseRet.cdata
                    except AttributeError: 
                        pass
            
                    r5011_rtom = r5011RTom.objects.create(**r5011_rtom_dados)
                    
                    if 'infoCRTom' in dir(RTom):
                    
                        for infoCRTom in RTom.infoCRTom:
                    
                            r5011_infocrtom_dados = {}
                            r5011_infocrtom_dados['r5011_rtom_id'] = r5011_rtom.id
                            
                            try:
                                r5011_infocrtom_dados['crtom'] = infoCRTom.CRTom.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r5011_infocrtom_dados['vlrcrtom'] = infoCRTom.vlrCRTom.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r5011_infocrtom_dados['vlrcrtomsusp'] = infoCRTom.vlrCRTomSusp.cdata
                            except AttributeError: 
                                pass
                    
                            r5011_infocrtom = r5011infoCRTom.objects.create(**r5011_infocrtom_dados)
            
            if 'RPrest' in dir(infoTotalContrib):
            
                for RPrest in infoTotalContrib.RPrest:
            
                    r5011_rprest_dados = {}
                    r5011_rprest_dados['r5011_infototalcontrib_id'] = r5011_infototalcontrib.id
                    
                    try:
                        r5011_rprest_dados['tpinsctomador'] = RPrest.tpInscTomador.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5011_rprest_dados['nrinsctomador'] = RPrest.nrInscTomador.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5011_rprest_dados['vlrtotalbaseret'] = RPrest.vlrTotalBaseRet.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5011_rprest_dados['vlrtotalretprinc'] = RPrest.vlrTotalRetPrinc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5011_rprest_dados['vlrtotalretadic'] = RPrest.vlrTotalRetAdic.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5011_rprest_dados['vlrtotalnretprinc'] = RPrest.vlrTotalNRetPrinc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5011_rprest_dados['vlrtotalnretadic'] = RPrest.vlrTotalNRetAdic.cdata
                    except AttributeError: 
                        pass
            
                    r5011_rprest = r5011RPrest.objects.create(**r5011_rprest_dados)
            
            if 'RRecRepAD' in dir(infoTotalContrib):
            
                for RRecRepAD in infoTotalContrib.RRecRepAD:
            
                    r5011_rrecrepad_dados = {}
                    r5011_rrecrepad_dados['r5011_infototalcontrib_id'] = r5011_infototalcontrib.id
                    
                    try:
                        r5011_rrecrepad_dados['cnpjassocdesp'] = RRecRepAD.cnpjAssocDesp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5011_rrecrepad_dados['vlrtotalrep'] = RRecRepAD.vlrTotalRep.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5011_rrecrepad_dados['crrecrepad'] = RRecRepAD.CRRecRepAD.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5011_rrecrepad_dados['vlrcrrecrepad'] = RRecRepAD.vlrCRRecRepAD.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5011_rrecrepad_dados['vlrcrrecrepadsusp'] = RRecRepAD.vlrCRRecRepADSusp.cdata
                    except AttributeError: 
                        pass
            
                    r5011_rrecrepad = r5011RRecRepAD.objects.create(**r5011_rrecrepad_dados)
            
            if 'RComl' in dir(infoTotalContrib):
            
                for RComl in infoTotalContrib.RComl:
            
                    r5011_rcoml_dados = {}
                    r5011_rcoml_dados['r5011_infototalcontrib_id'] = r5011_infototalcontrib.id
                    
                    try:
                        r5011_rcoml_dados['crcoml'] = RComl.CRComl.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5011_rcoml_dados['vlrcrcoml'] = RComl.vlrCRComl.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5011_rcoml_dados['vlrcrcomlsusp'] = RComl.vlrCRComlSusp.cdata
                    except AttributeError: 
                        pass
            
                    r5011_rcoml = r5011RComl.objects.create(**r5011_rcoml_dados)
            
            if 'RCPRB' in dir(infoTotalContrib):
            
                for RCPRB in infoTotalContrib.RCPRB:
            
                    r5011_rcprb_dados = {}
                    r5011_rcprb_dados['r5011_infototalcontrib_id'] = r5011_infototalcontrib.id
                    
                    try:
                        r5011_rcprb_dados['crcprb'] = RCPRB.CRCPRB.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5011_rcprb_dados['vlrcrcprb'] = RCPRB.vlrCRCPRB.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5011_rcprb_dados['vlrcrcprbsusp'] = RCPRB.vlrCRCPRBSusp.cdata
                    except AttributeError: 
                        pass
            
                    r5011_rcprb = r5011RCPRB.objects.create(**r5011_rcprb_dados)    
    r5011_evttotalcontrib_dados['evento'] = 'r5011'
    r5011_evttotalcontrib_dados['id'] = r5011_evttotalcontrib.id
    r5011_evttotalcontrib_dados['identidade_evento'] = doc.Reinf.evtTotalContrib['id']
    r5011_evttotalcontrib_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r5011_evttotalcontrib_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(r5011_evttotalcontrib.id)
    return r5011_evttotalcontrib_dados