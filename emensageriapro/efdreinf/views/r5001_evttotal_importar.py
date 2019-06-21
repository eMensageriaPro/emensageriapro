#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r5001.models import *



def read_r5001_evttotal_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r5001_evttotal_obj(request, doc, status, validar)
    return dados



def read_r5001_evttotal(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r5001_evttotal_obj(request, doc, status, validar)

    r5001evtTotal.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_r5001_evttotal_obj(request, doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r5001_evttotal_dados = {}
    r5001_evttotal_dados['status'] = status
    r5001_evttotal_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r5001_evttotal_dados['identidade'] = doc.Reinf.evtTotal['id']
    evtTotal = doc.Reinf.evtTotal
    
    try:
        r5001_evttotal_dados['perapur'] = evtTotal.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        r5001_evttotal_dados['tpinsc'] = evtTotal.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r5001_evttotal_dados['nrinsc'] = evtTotal.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r5001_evttotal_dados['cdretorno'] = evtTotal.ideRecRetorno.ideStatus.cdRetorno.cdata
    except AttributeError: 
        pass
    
    try:
        r5001_evttotal_dados['descretorno'] = evtTotal.ideRecRetorno.ideStatus.descRetorno.cdata
    except AttributeError: 
        pass
    
    try:
        r5001_evttotal_dados['nrprotentr'] = evtTotal.infoRecEv.nrProtEntr.cdata
    except AttributeError: 
        pass
    
    try:
        r5001_evttotal_dados['dhprocess'] = evtTotal.infoRecEv.dhProcess.cdata
    except AttributeError: 
        pass
    
    try:
        r5001_evttotal_dados['tpev'] = evtTotal.infoRecEv.tpEv.cdata
    except AttributeError: 
        pass
    
    try:
        r5001_evttotal_dados['idev'] = evtTotal.infoRecEv.idEv.cdata
    except AttributeError: 
        pass
    
    try:
        r5001_evttotal_dados['hash'] = evtTotal.infoRecEv.hash.cdata
    except AttributeError: 
        pass
        
    r5001_evttotal = r5001evtTotal.objects.create(**r5001_evttotal_dados)
    
    if 'ideRecRetorno' in dir(evtTotal) and 'ideStatus' in dir(evtTotal.ideRecRetorno) and 'regOcorrs' in dir(evtTotal.ideRecRetorno.ideStatus):
    
        for regOcorrs in evtTotal.ideRecRetorno.ideStatus.regOcorrs:
    
            r5001_regocorrs_dados = {}
            r5001_regocorrs_dados['r5001_evttotal_id'] = r5001_evttotal.id
            
            try:
                r5001_regocorrs_dados['tpocorr'] = regOcorrs.tpOcorr.cdata
            except AttributeError: 
                pass
            
            try:
                r5001_regocorrs_dados['localerroaviso'] = regOcorrs.localErroAviso.cdata
            except AttributeError: 
                pass
            
            try:
                r5001_regocorrs_dados['codresp'] = regOcorrs.codResp.cdata
            except AttributeError: 
                pass
            
            try:
                r5001_regocorrs_dados['dscresp'] = regOcorrs.dscResp.cdata
            except AttributeError: 
                pass
    
            r5001_regocorrs = r5001regOcorrs.objects.create(**r5001_regocorrs_dados)
    
    if 'infoTotal' in dir(evtTotal):
    
        for infoTotal in evtTotal.infoTotal:
    
            r5001_infototal_dados = {}
            r5001_infototal_dados['r5001_evttotal_id'] = r5001_evttotal.id
            
            try:
                r5001_infototal_dados['nrrecarqbase'] = infoTotal.nrRecArqBase.cdata
            except AttributeError: 
                pass
            
            try:
                r5001_infototal_dados['tpinsc'] = infoTotal.ideEstab.tpInsc.cdata
            except AttributeError: 
                pass
            
            try:
                r5001_infototal_dados['nrinsc'] = infoTotal.ideEstab.nrInsc.cdata
            except AttributeError: 
                pass
    
            r5001_infototal = r5001infoTotal.objects.create(**r5001_infototal_dados)
            
            if 'ideEstab' in dir(infoTotal) and 'RTom' in dir(infoTotal.ideEstab):
            
                for RTom in infoTotal.ideEstab.RTom:
            
                    r5001_rtom_dados = {}
                    r5001_rtom_dados['r5001_infototal_id'] = r5001_infototal.id
                    
                    try:
                        r5001_rtom_dados['cnpjprestador'] = RTom.cnpjPrestador.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rtom_dados['cno'] = RTom.cno.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rtom_dados['vlrtotalbaseret'] = RTom.vlrTotalBaseRet.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
            
                    r5001_rtom = r5001RTom.objects.create(**r5001_rtom_dados)
                    
                    if 'infoCRTom' in dir(RTom):
                    
                        for infoCRTom in RTom.infoCRTom:
                    
                            r5001_infocrtom_dados = {}
                            r5001_infocrtom_dados['r5001_rtom_id'] = r5001_rtom.id
                            
                            try:
                                r5001_infocrtom_dados['crtom'] = infoCRTom.CRTom.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r5001_infocrtom_dados['vlrcrtom'] = infoCRTom.vlrCRTom.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r5001_infocrtom_dados['vlrcrtomsusp'] = infoCRTom.vlrCRTomSusp.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                    
                            r5001_infocrtom = r5001infoCRTom.objects.create(**r5001_infocrtom_dados)
            
            if 'ideEstab' in dir(infoTotal) and 'RPrest' in dir(infoTotal.ideEstab):
            
                for RPrest in infoTotal.ideEstab.RPrest:
            
                    r5001_rprest_dados = {}
                    r5001_rprest_dados['r5001_infototal_id'] = r5001_infototal.id
                    
                    try:
                        r5001_rprest_dados['tpinsctomador'] = RPrest.tpInscTomador.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rprest_dados['nrinsctomador'] = RPrest.nrInscTomador.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rprest_dados['vlrtotalbaseret'] = RPrest.vlrTotalBaseRet.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rprest_dados['vlrtotalretprinc'] = RPrest.vlrTotalRetPrinc.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rprest_dados['vlrtotalretadic'] = RPrest.vlrTotalRetAdic.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rprest_dados['vlrtotalnretprinc'] = RPrest.vlrTotalNRetPrinc.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rprest_dados['vlrtotalnretadic'] = RPrest.vlrTotalNRetAdic.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
            
                    r5001_rprest = r5001RPrest.objects.create(**r5001_rprest_dados)
            
            if 'ideEstab' in dir(infoTotal) and 'RRecRepAD' in dir(infoTotal.ideEstab):
            
                for RRecRepAD in infoTotal.ideEstab.RRecRepAD:
            
                    r5001_rrecrepad_dados = {}
                    r5001_rrecrepad_dados['r5001_infototal_id'] = r5001_infototal.id
                    
                    try:
                        r5001_rrecrepad_dados['cnpjassocdesp'] = RRecRepAD.cnpjAssocDesp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rrecrepad_dados['vlrtotalrep'] = RRecRepAD.vlrTotalRep.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rrecrepad_dados['crrecrepad'] = RRecRepAD.CRRecRepAD.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rrecrepad_dados['vlrcrrecrepad'] = RRecRepAD.vlrCRRecRepAD.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rrecrepad_dados['vlrcrrecrepadsusp'] = RRecRepAD.vlrCRRecRepADSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
            
                    r5001_rrecrepad = r5001RRecRepAD.objects.create(**r5001_rrecrepad_dados)
            
            if 'ideEstab' in dir(infoTotal) and 'RComl' in dir(infoTotal.ideEstab):
            
                for RComl in infoTotal.ideEstab.RComl:
            
                    r5001_rcoml_dados = {}
                    r5001_rcoml_dados['r5001_infototal_id'] = r5001_infototal.id
                    
                    try:
                        r5001_rcoml_dados['crcoml'] = RComl.CRComl.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rcoml_dados['vlrcrcoml'] = RComl.vlrCRComl.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rcoml_dados['vlrcrcomlsusp'] = RComl.vlrCRComlSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
            
                    r5001_rcoml = r5001RComl.objects.create(**r5001_rcoml_dados)
            
            if 'ideEstab' in dir(infoTotal) and 'RCPRB' in dir(infoTotal.ideEstab):
            
                for RCPRB in infoTotal.ideEstab.RCPRB:
            
                    r5001_rcprb_dados = {}
                    r5001_rcprb_dados['r5001_infototal_id'] = r5001_infototal.id
                    
                    try:
                        r5001_rcprb_dados['crcprb'] = RCPRB.CRCPRB.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rcprb_dados['vlrcrcprb'] = RCPRB.vlrCRCPRB.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rcprb_dados['vlrcrcprbsusp'] = RCPRB.vlrCRCPRBSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
            
                    r5001_rcprb = r5001RCPRB.objects.create(**r5001_rcprb_dados)
            
            if 'ideEstab' in dir(infoTotal) and 'RRecEspetDesp' in dir(infoTotal.ideEstab):
            
                for RRecEspetDesp in infoTotal.ideEstab.RRecEspetDesp:
            
                    r5001_rrecespetdesp_dados = {}
                    r5001_rrecespetdesp_dados['r5001_infototal_id'] = r5001_infototal.id
                    
                    try:
                        r5001_rrecespetdesp_dados['crrecespetdesp'] = RRecEspetDesp.CRRecEspetDesp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rrecespetdesp_dados['vlrreceitatotal'] = RRecEspetDesp.vlrReceitaTotal.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rrecespetdesp_dados['vlrcrrecespetdesp'] = RRecEspetDesp.vlrCRRecEspetDesp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r5001_rrecespetdesp_dados['vlrcrrecespetdespsusp'] = RRecEspetDesp.vlrCRRecEspetDespSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
            
                    r5001_rrecespetdesp = r5001RRecEspetDesp.objects.create(**r5001_rrecespetdesp_dados)    
    r5001_evttotal_dados['evento'] = 'r5001'
    r5001_evttotal_dados['id'] = r5001_evttotal.id
    r5001_evttotal_dados['identidade_evento'] = doc.Reinf.evtTotal['id']
    r5001_evttotal_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r5001_evttotal_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, r5001_evttotal.id)
    
    return r5001_evttotal_dados