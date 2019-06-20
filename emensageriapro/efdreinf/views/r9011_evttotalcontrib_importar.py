#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r9011.models import *



def read_r9011_evttotalcontrib_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r9011_evttotalcontrib_obj(request, doc, status, validar)
    return dados



def read_r9011_evttotalcontrib(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r9011_evttotalcontrib_obj(request, doc, status, validar)

    r9011evtTotalContrib.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_r9011_evttotalcontrib_obj(request, doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r9011_evttotalcontrib_dados = {}
    r9011_evttotalcontrib_dados['status'] = status
    r9011_evttotalcontrib_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r9011_evttotalcontrib_dados['identidade'] = doc.Reinf.evtTotalContrib['id']
    evtTotalContrib = doc.Reinf.evtTotalContrib
    
    try:
        r9011_evttotalcontrib_dados['perapur'] = evtTotalContrib.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        r9011_evttotalcontrib_dados['tpinsc'] = evtTotalContrib.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r9011_evttotalcontrib_dados['nrinsc'] = evtTotalContrib.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r9011_evttotalcontrib_dados['cdretorno'] = evtTotalContrib.ideRecRetorno.ideStatus.cdRetorno.cdata
    except AttributeError: 
        pass
    
    try:
        r9011_evttotalcontrib_dados['descretorno'] = evtTotalContrib.ideRecRetorno.ideStatus.descRetorno.cdata
    except AttributeError: 
        pass
    
    try:
        r9011_evttotalcontrib_dados['nrprotentr'] = evtTotalContrib.infoRecEv.nrProtEntr.cdata
    except AttributeError: 
        pass
    
    try:
        r9011_evttotalcontrib_dados['dhprocess'] = evtTotalContrib.infoRecEv.dhProcess.cdata
    except AttributeError: 
        pass
    
    try:
        r9011_evttotalcontrib_dados['tpev'] = evtTotalContrib.infoRecEv.tpEv.cdata
    except AttributeError: 
        pass
    
    try:
        r9011_evttotalcontrib_dados['idev'] = evtTotalContrib.infoRecEv.idEv.cdata
    except AttributeError: 
        pass
    
    try:
        r9011_evttotalcontrib_dados['hash'] = evtTotalContrib.infoRecEv.hash.cdata
    except AttributeError: 
        pass
        
    r9011_evttotalcontrib = r9011evtTotalContrib.objects.create(**r9011_evttotalcontrib_dados)
    
    if 'regOcorrs' in dir(evtTotalContrib.ideRecRetorno.ideStatus):
    
        for regOcorrs in evtTotalContrib.ideRecRetorno.ideStatus.regOcorrs:
    
            r9011_regocorrs_dados = {}
            r9011_regocorrs_dados['r9011_evttotalcontrib_id'] = r9011_evttotalcontrib.id
            
            try:
                r9011_regocorrs_dados['tpocorr'] = regOcorrs.tpOcorr.cdata
            except AttributeError: 
                pass
            
            try:
                r9011_regocorrs_dados['localerroaviso'] = regOcorrs.localErroAviso.cdata
            except AttributeError: 
                pass
            
            try:
                r9011_regocorrs_dados['codresp'] = regOcorrs.codResp.cdata
            except AttributeError: 
                pass
            
            try:
                r9011_regocorrs_dados['dscresp'] = regOcorrs.dscResp.cdata
            except AttributeError: 
                pass
    
            r9011_regocorrs = r9011regOcorrs.objects.create(**r9011_regocorrs_dados)
    
    if 'infoTotalContrib' in dir(evtTotalContrib):
    
        for infoTotalContrib in evtTotalContrib.infoTotalContrib:
    
            r9011_infototalcontrib_dados = {}
            r9011_infototalcontrib_dados['r9011_evttotalcontrib_id'] = r9011_evttotalcontrib.id
            
            try:
                r9011_infototalcontrib_dados['nrrecarqbase'] = infoTotalContrib.nrRecArqBase.cdata
            except AttributeError: 
                pass
            
            try:
                r9011_infototalcontrib_dados['indexistinfo'] = infoTotalContrib.indExistInfo.cdata
            except AttributeError: 
                pass
    
            r9011_infototalcontrib = r9011infoTotalContrib.objects.create(**r9011_infototalcontrib_dados)
            
            if 'RTom' in dir(infoTotalContrib):
            
                for RTom in infoTotalContrib.RTom:
            
                    r9011_rtom_dados = {}
                    r9011_rtom_dados['r9011_infototalcontrib_id'] = r9011_infototalcontrib.id
                    
                    try:
                        r9011_rtom_dados['cnpjprestador'] = RTom.cnpjPrestador.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9011_rtom_dados['cno'] = RTom.cno.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9011_rtom_dados['vlrtotalbaseret'] = RTom.vlrTotalBaseRet.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
            
                    r9011_rtom = r9011RTom.objects.create(**r9011_rtom_dados)
                    
                    if 'infoCRTom' in dir(RTom):
                    
                        for infoCRTom in RTom.infoCRTom:
                    
                            r9011_infocrtom_dados = {}
                            r9011_infocrtom_dados['r9011_rtom_id'] = r9011_rtom.id
                            
                            try:
                                r9011_infocrtom_dados['crtom'] = infoCRTom.CRTom.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r9011_infocrtom_dados['vlrcrtom'] = infoCRTom.vlrCRTom.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r9011_infocrtom_dados['vlrcrtomsusp'] = infoCRTom.vlrCRTomSusp.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                    
                            r9011_infocrtom = r9011infoCRTom.objects.create(**r9011_infocrtom_dados)
            
            if 'RPrest' in dir(infoTotalContrib):
            
                for RPrest in infoTotalContrib.RPrest:
            
                    r9011_rprest_dados = {}
                    r9011_rprest_dados['r9011_infototalcontrib_id'] = r9011_infototalcontrib.id
                    
                    try:
                        r9011_rprest_dados['tpinsctomador'] = RPrest.tpInscTomador.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9011_rprest_dados['nrinsctomador'] = RPrest.nrInscTomador.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9011_rprest_dados['vlrtotalbaseret'] = RPrest.vlrTotalBaseRet.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r9011_rprest_dados['vlrtotalretprinc'] = RPrest.vlrTotalRetPrinc.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r9011_rprest_dados['vlrtotalretadic'] = RPrest.vlrTotalRetAdic.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r9011_rprest_dados['vlrtotalnretprinc'] = RPrest.vlrTotalNRetPrinc.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r9011_rprest_dados['vlrtotalnretadic'] = RPrest.vlrTotalNRetAdic.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
            
                    r9011_rprest = r9011RPrest.objects.create(**r9011_rprest_dados)
            
            if 'RRecRepAD' in dir(infoTotalContrib):
            
                for RRecRepAD in infoTotalContrib.RRecRepAD:
            
                    r9011_rrecrepad_dados = {}
                    r9011_rrecrepad_dados['r9011_infototalcontrib_id'] = r9011_infototalcontrib.id
                    
                    try:
                        r9011_rrecrepad_dados['crrecrepad'] = RRecRepAD.CRRecRepAD.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9011_rrecrepad_dados['vlrcrrecrepad'] = RRecRepAD.vlrCRRecRepAD.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r9011_rrecrepad_dados['vlrcrrecrepadsusp'] = RRecRepAD.vlrCRRecRepADSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
            
                    r9011_rrecrepad = r9011RRecRepAD.objects.create(**r9011_rrecrepad_dados)
            
            if 'RComl' in dir(infoTotalContrib):
            
                for RComl in infoTotalContrib.RComl:
            
                    r9011_rcoml_dados = {}
                    r9011_rcoml_dados['r9011_infototalcontrib_id'] = r9011_infototalcontrib.id
                    
                    try:
                        r9011_rcoml_dados['crcoml'] = RComl.CRComl.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9011_rcoml_dados['vlrcrcoml'] = RComl.vlrCRComl.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r9011_rcoml_dados['vlrcrcomlsusp'] = RComl.vlrCRComlSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
            
                    r9011_rcoml = r9011RComl.objects.create(**r9011_rcoml_dados)
            
            if 'RCPRB' in dir(infoTotalContrib):
            
                for RCPRB in infoTotalContrib.RCPRB:
            
                    r9011_rcprb_dados = {}
                    r9011_rcprb_dados['r9011_infototalcontrib_id'] = r9011_infototalcontrib.id
                    
                    try:
                        r9011_rcprb_dados['crcprb'] = RCPRB.CRCPRB.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9011_rcprb_dados['vlrcrcprb'] = RCPRB.vlrCRCPRB.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r9011_rcprb_dados['vlrcrcprbsusp'] = RCPRB.vlrCRCPRBSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
            
                    r9011_rcprb = r9011RCPRB.objects.create(**r9011_rcprb_dados)    
    r9011_evttotalcontrib_dados['evento'] = 'r9011'
    r9011_evttotalcontrib_dados['id'] = r9011_evttotalcontrib.id
    r9011_evttotalcontrib_dados['identidade_evento'] = doc.Reinf.evtTotalContrib['id']
    r9011_evttotalcontrib_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r9011_evttotalcontrib_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, r9011_evttotalcontrib.id)
    
    return r9011_evttotalcontrib_dados