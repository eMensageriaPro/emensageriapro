#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r4040.models import *



def read_r4040_evtbenefnid_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r4040_evtbenefnid_obj(request, doc, status, validar)
    return dados



def read_r4040_evtbenefnid(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r4040_evtbenefnid_obj(request, doc, status, validar)

    r4040evtBenefNId.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_r4040_evtbenefnid_obj(request, doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r4040_evtbenefnid_dados = {}
    r4040_evtbenefnid_dados['status'] = status
    r4040_evtbenefnid_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r4040_evtbenefnid_dados['identidade'] = doc.Reinf.evtBenefNId['id']
    evtBenefNId = doc.Reinf.evtBenefNId
    
    try:
        r4040_evtbenefnid_dados['indretif'] = evtBenefNId.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        r4040_evtbenefnid_dados['nrrecibo'] = evtBenefNId.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        r4040_evtbenefnid_dados['perapur'] = evtBenefNId.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        r4040_evtbenefnid_dados['tpamb'] = evtBenefNId.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        r4040_evtbenefnid_dados['procemi'] = evtBenefNId.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        r4040_evtbenefnid_dados['verproc'] = evtBenefNId.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        r4040_evtbenefnid_dados['tpinsc'] = evtBenefNId.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r4040_evtbenefnid_dados['nrinsc'] = evtBenefNId.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r4040_evtbenefnid_dados['tpinscestab'] = evtBenefNId.ideEstab.tpInscEstab.cdata
    except AttributeError: 
        pass
    
    try:
        r4040_evtbenefnid_dados['nrinscestab'] = evtBenefNId.ideEstab.nrInscEstab.cdata
    except AttributeError: 
        pass
        
    r4040_evtbenefnid = r4040evtBenefNId.objects.create(**r4040_evtbenefnid_dados)
    
    if 'ideEstab' in dir(evtBenefNId) and 'ideNat' in dir(evtBenefNId.ideEstab):
    
        for ideNat in evtBenefNId.ideEstab.ideNat:
    
            r4040_idenat_dados = {}
            r4040_idenat_dados['r4040_evtbenefnid_id'] = r4040_evtbenefnid.id
            
            try:
                r4040_idenat_dados['natrendim'] = ideNat.natRendim.cdata
            except AttributeError: 
                pass
    
            r4040_idenat = r4040ideNat.objects.create(**r4040_idenat_dados)
            
            if 'infoPgto' in dir(ideNat):
            
                for infoPgto in ideNat.infoPgto:
            
                    r4040_infopgto_dados = {}
                    r4040_infopgto_dados['r4040_idenat_id'] = r4040_idenat.id
                    
                    try:
                        r4040_infopgto_dados['dtfg'] = infoPgto.dtFG.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4040_infopgto_dados['vlrliq'] = infoPgto.vlrLiq.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r4040_infopgto_dados['vlrreaj'] = infoPgto.vlrReaj.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r4040_infopgto_dados['vlrir'] = infoPgto.vlrIR.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r4040_infopgto_dados['descr'] = infoPgto.descr.cdata
                    except AttributeError: 
                        pass
            
                    r4040_infopgto = r4040infoPgto.objects.create(**r4040_infopgto_dados)    
    r4040_evtbenefnid_dados['evento'] = 'r4040'
    r4040_evtbenefnid_dados['id'] = r4040_evtbenefnid.id
    r4040_evtbenefnid_dados['identidade_evento'] = doc.Reinf.evtBenefNId['id']
    r4040_evtbenefnid_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r4040_evtbenefnid_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, r4040_evtbenefnid.id)
    
    return r4040_evtbenefnid_dados