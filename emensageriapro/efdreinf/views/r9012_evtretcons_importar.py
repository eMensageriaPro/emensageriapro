#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r9012.models import *



def read_r9012_evtretcons_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r9012_evtretcons_obj(request, doc, status, validar)
    return dados



def read_r9012_evtretcons(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r9012_evtretcons_obj(request, doc, status, validar)

    r9012evtRetCons.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_r9012_evtretcons_obj(request, doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r9012_evtretcons_dados = {}
    r9012_evtretcons_dados['status'] = status
    r9012_evtretcons_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r9012_evtretcons_dados['identidade'] = doc.Reinf.evtRetCons['id']
    evtRetCons = doc.Reinf.evtRetCons
    
    try:
        r9012_evtretcons_dados['perapur'] = evtRetCons.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        r9012_evtretcons_dados['tpinsc'] = evtRetCons.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r9012_evtretcons_dados['nrinsc'] = evtRetCons.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r9012_evtretcons_dados['cdretorno'] = evtRetCons.ideRecRetorno.ideStatus.cdRetorno.cdata
    except AttributeError: 
        pass
    
    try:
        r9012_evtretcons_dados['descretorno'] = evtRetCons.ideRecRetorno.ideStatus.descRetorno.cdata
    except AttributeError: 
        pass
    
    try:
        r9012_evtretcons_dados['nrprotentr'] = evtRetCons.infoRecEv.nrProtEntr.cdata
    except AttributeError: 
        pass
    
    try:
        r9012_evtretcons_dados['dhprocess'] = evtRetCons.infoRecEv.dhProcess.cdata
    except AttributeError: 
        pass
    
    try:
        r9012_evtretcons_dados['tpev'] = evtRetCons.infoRecEv.tpEv.cdata
    except AttributeError: 
        pass
    
    try:
        r9012_evtretcons_dados['idev'] = evtRetCons.infoRecEv.idEv.cdata
    except AttributeError: 
        pass
    
    try:
        r9012_evtretcons_dados['hash'] = evtRetCons.infoRecEv.hash.cdata
    except AttributeError: 
        pass
        
    r9012_evtretcons = r9012evtRetCons.objects.create(**r9012_evtretcons_dados)
    
    if 'regOcorrs' in dir(evtRetCons.ideRecRetorno.ideStatus):
    
        for regOcorrs in evtRetCons.ideRecRetorno.ideStatus.regOcorrs:
    
            r9012_regocorrs_dados = {}
            r9012_regocorrs_dados['r9012_evtretcons_id'] = r9012_evtretcons.id
            
            try:
                r9012_regocorrs_dados['tpocorr'] = regOcorrs.tpOcorr.cdata
            except AttributeError: 
                pass
            
            try:
                r9012_regocorrs_dados['localerroaviso'] = regOcorrs.localErroAviso.cdata
            except AttributeError: 
                pass
            
            try:
                r9012_regocorrs_dados['codresp'] = regOcorrs.codResp.cdata
            except AttributeError: 
                pass
            
            try:
                r9012_regocorrs_dados['dscresp'] = regOcorrs.dscResp.cdata
            except AttributeError: 
                pass
    
            r9012_regocorrs = r9012regOcorrs.objects.create(**r9012_regocorrs_dados)
    
    if 'infoTotalContrib' in dir(evtRetCons):
    
        for infoTotalContrib in evtRetCons.infoTotalContrib:
    
            r9012_infototalcontrib_dados = {}
            r9012_infototalcontrib_dados['r9012_evtretcons_id'] = r9012_evtretcons.id
            
            try:
                r9012_infototalcontrib_dados['nrrecarqbase'] = infoTotalContrib.nrRecArqBase.cdata
            except AttributeError: 
                pass
            
            try:
                r9012_infototalcontrib_dados['indexistinfo'] = infoTotalContrib.indExistInfo.cdata
            except AttributeError: 
                pass
    
            r9012_infototalcontrib = r9012infoTotalContrib.objects.create(**r9012_infototalcontrib_dados)
            
            if 'totApurMen' in dir(infoTotalContrib):
            
                for totApurMen in infoTotalContrib.totApurMen:
            
                    r9012_totapurmen_dados = {}
                    r9012_totapurmen_dados['r9012_infototalcontrib_id'] = r9012_infototalcontrib.id
                    
                    try:
                        r9012_totapurmen_dados['crmen'] = totApurMen.CRMen.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurmen_dados['vlrbasecrmen'] = totApurMen.vlrBaseCRMen.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurmen_dados['vlrcrmen'] = totApurMen.vlrCRMen.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurmen_dados['vlrbasecrmensusp'] = totApurMen.vlrBaseCRMenSusp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurmen_dados['vlrcrmensusp'] = totApurMen.vlrCRMenSusp.cdata
                    except AttributeError: 
                        pass
            
                    r9012_totapurmen = r9012totApurMen.objects.create(**r9012_totapurmen_dados)
            
            if 'totApurQui' in dir(infoTotalContrib):
            
                for totApurQui in infoTotalContrib.totApurQui:
            
                    r9012_totapurqui_dados = {}
                    r9012_totapurqui_dados['r9012_infototalcontrib_id'] = r9012_infototalcontrib.id
                    
                    try:
                        r9012_totapurqui_dados['perapurqui'] = totApurQui.perApurQui.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurqui_dados['crqui'] = totApurQui.CRQui.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurqui_dados['vlrbasecrqui'] = totApurQui.vlrBaseCRQui.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurqui_dados['vlrcrqui'] = totApurQui.vlrCRQui.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurqui_dados['vlrbasecrquisusp'] = totApurQui.vlrBaseCRQuiSusp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurqui_dados['vlrcrquisusp'] = totApurQui.vlrCRQuiSusp.cdata
                    except AttributeError: 
                        pass
            
                    r9012_totapurqui = r9012totApurQui.objects.create(**r9012_totapurqui_dados)
            
            if 'totApurDec' in dir(infoTotalContrib):
            
                for totApurDec in infoTotalContrib.totApurDec:
            
                    r9012_totapurdec_dados = {}
                    r9012_totapurdec_dados['r9012_infototalcontrib_id'] = r9012_infototalcontrib.id
                    
                    try:
                        r9012_totapurdec_dados['perapurdec'] = totApurDec.perApurDec.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurdec_dados['crdec'] = totApurDec.CRDec.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurdec_dados['vlrbasecrdec'] = totApurDec.vlrBaseCRDec.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurdec_dados['vlrcrdec'] = totApurDec.vlrCRDec.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurdec_dados['vlrbasecrdecsusp'] = totApurDec.vlrBaseCRDecSusp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurdec_dados['vlrcrdecsusp'] = totApurDec.vlrCRDecSusp.cdata
                    except AttributeError: 
                        pass
            
                    r9012_totapurdec = r9012totApurDec.objects.create(**r9012_totapurdec_dados)
            
            if 'totApurSem' in dir(infoTotalContrib):
            
                for totApurSem in infoTotalContrib.totApurSem:
            
                    r9012_totapursem_dados = {}
                    r9012_totapursem_dados['r9012_infototalcontrib_id'] = r9012_infototalcontrib.id
                    
                    try:
                        r9012_totapursem_dados['perapursem'] = totApurSem.perApurSem.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapursem_dados['crsem'] = totApurSem.CRSem.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapursem_dados['vlrbasecrsem'] = totApurSem.vlrBaseCRSem.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapursem_dados['vlrcrsem'] = totApurSem.vlrCRSem.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapursem_dados['vlrbasecrsemsusp'] = totApurSem.vlrBaseCRSemSusp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapursem_dados['vlrcrsemsusp'] = totApurSem.vlrCRSemSusp.cdata
                    except AttributeError: 
                        pass
            
                    r9012_totapursem = r9012totApurSem.objects.create(**r9012_totapursem_dados)
            
            if 'totApurDia' in dir(infoTotalContrib):
            
                for totApurDia in infoTotalContrib.totApurDia:
            
                    r9012_totapurdia_dados = {}
                    r9012_totapurdia_dados['r9012_infototalcontrib_id'] = r9012_infototalcontrib.id
                    
                    try:
                        r9012_totapurdia_dados['perapurdia'] = totApurDia.perApurDia.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurdia_dados['crdia'] = totApurDia.CRDia.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurdia_dados['vlrbasecrdia'] = totApurDia.vlrBaseCRDia.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurdia_dados['vlrcrdia'] = totApurDia.vlrCRDia.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurdia_dados['vlrbasecrdiasusp'] = totApurDia.vlrBaseCRDiaSusp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r9012_totapurdia_dados['vlrcrdiasusp'] = totApurDia.vlrCRDiaSusp.cdata
                    except AttributeError: 
                        pass
            
                    r9012_totapurdia = r9012totApurDia.objects.create(**r9012_totapurdia_dados)    
    r9012_evtretcons_dados['evento'] = 'r9012'
    r9012_evtretcons_dados['id'] = r9012_evtretcons.id
    r9012_evtretcons_dados['identidade_evento'] = doc.Reinf.evtRetCons['id']
    r9012_evtretcons_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r9012_evtretcons_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, r9012_evtretcons.id)
    
    return r9012_evtretcons_dados