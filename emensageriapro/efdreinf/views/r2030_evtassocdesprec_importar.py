#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r2030.models import *



def read_r2030_evtassocdesprec_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2030_evtassocdesprec_obj(request, doc, status, validar)
    return dados



def read_r2030_evtassocdesprec(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2030_evtassocdesprec_obj(request, doc, status, validar)

    r2030evtAssocDespRec.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_r2030_evtassocdesprec_obj(request, doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r2030_evtassocdesprec_dados = {}
    r2030_evtassocdesprec_dados['status'] = status
    r2030_evtassocdesprec_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2030_evtassocdesprec_dados['identidade'] = doc.Reinf.evtAssocDespRec['id']
    evtAssocDespRec = doc.Reinf.evtAssocDespRec
    
    try:
        r2030_evtassocdesprec_dados['indretif'] = evtAssocDespRec.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        r2030_evtassocdesprec_dados['nrrecibo'] = evtAssocDespRec.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        r2030_evtassocdesprec_dados['perapur'] = evtAssocDespRec.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        r2030_evtassocdesprec_dados['tpamb'] = evtAssocDespRec.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        r2030_evtassocdesprec_dados['procemi'] = evtAssocDespRec.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        r2030_evtassocdesprec_dados['verproc'] = evtAssocDespRec.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        r2030_evtassocdesprec_dados['tpinsc'] = evtAssocDespRec.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r2030_evtassocdesprec_dados['nrinsc'] = evtAssocDespRec.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r2030_evtassocdesprec_dados['tpinscestab'] = evtAssocDespRec.ideContri.ideEstab.tpInscEstab.cdata
    except AttributeError: 
        pass
    
    try:
        r2030_evtassocdesprec_dados['nrinscestab'] = evtAssocDespRec.ideContri.ideEstab.nrInscEstab.cdata
    except AttributeError: 
        pass
        
    r2030_evtassocdesprec = r2030evtAssocDespRec.objects.create(**r2030_evtassocdesprec_dados)
    
    if 'recursosRec' in dir(evtAssocDespRec.ideContri.ideEstab):
    
        for recursosRec in evtAssocDespRec.ideContri.ideEstab.recursosRec:
    
            r2030_recursosrec_dados = {}
            r2030_recursosrec_dados['r2030_evtassocdesprec_id'] = r2030_evtassocdesprec.id
            
            try:
                r2030_recursosrec_dados['cnpjorigrecurso'] = recursosRec.cnpjOrigRecurso.cdata
            except AttributeError: 
                pass
            
            try:
                r2030_recursosrec_dados['vlrtotalrec'] = recursosRec.vlrTotalRec.cdata.replace('.', '').replace(',', '.')
            except AttributeError: 
                pass
            
            try:
                r2030_recursosrec_dados['vlrtotalret'] = recursosRec.vlrTotalRet.cdata.replace('.', '').replace(',', '.')
            except AttributeError: 
                pass
            
            try:
                r2030_recursosrec_dados['vlrtotalnret'] = recursosRec.vlrTotalNRet.cdata.replace('.', '').replace(',', '.')
            except AttributeError: 
                pass
    
            r2030_recursosrec = r2030recursosRec.objects.create(**r2030_recursosrec_dados)
            
            if 'infoRecurso' in dir(recursosRec):
            
                for infoRecurso in recursosRec.infoRecurso:
            
                    r2030_inforecurso_dados = {}
                    r2030_inforecurso_dados['r2030_recursosrec_id'] = r2030_recursosrec.id
                    
                    try:
                        r2030_inforecurso_dados['tprepasse'] = infoRecurso.tpRepasse.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2030_inforecurso_dados['descrecurso'] = infoRecurso.descRecurso.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2030_inforecurso_dados['vlrbruto'] = infoRecurso.vlrBruto.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r2030_inforecurso_dados['vlrretapur'] = infoRecurso.vlrRetApur.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
            
                    r2030_inforecurso = r2030infoRecurso.objects.create(**r2030_inforecurso_dados)
            
            if 'infoProc' in dir(recursosRec):
            
                for infoProc in recursosRec.infoProc:
            
                    r2030_infoproc_dados = {}
                    r2030_infoproc_dados['r2030_recursosrec_id'] = r2030_recursosrec.id
                    
                    try:
                        r2030_infoproc_dados['tpproc'] = infoProc.tpProc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2030_infoproc_dados['nrproc'] = infoProc.nrProc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2030_infoproc_dados['codsusp'] = infoProc.codSusp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2030_infoproc_dados['vlrnret'] = infoProc.vlrNRet.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
            
                    r2030_infoproc = r2030infoProc.objects.create(**r2030_infoproc_dados)    
    r2030_evtassocdesprec_dados['evento'] = 'r2030'
    r2030_evtassocdesprec_dados['id'] = r2030_evtassocdesprec.id
    r2030_evtassocdesprec_dados['identidade_evento'] = doc.Reinf.evtAssocDespRec['id']
    r2030_evtassocdesprec_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r2030_evtassocdesprec_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, r2030_evtassocdesprec.id)
    
    return r2030_evtassocdesprec_dados