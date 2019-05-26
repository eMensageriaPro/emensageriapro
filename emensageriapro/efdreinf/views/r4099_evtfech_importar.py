#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r4099.models import *



def read_r4099_evtfech_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r4099_evtfech_obj(doc, status, validar)
    return dados



def read_r4099_evtfech(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r4099_evtfech_obj(doc, status, validar)
    return dados



def read_r4099_evtfech_obj(doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r4099_evtfech_dados = {}
    r4099_evtfech_dados['status'] = status
    r4099_evtfech_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r4099_evtfech_dados['identidade'] = doc.Reinf.evtFech['id']
    evtFech = doc.Reinf.evtFech
    
    try:
        r4099_evtfech_dados['perapur'] = evtFech.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        r4099_evtfech_dados['tpamb'] = evtFech.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        r4099_evtfech_dados['procemi'] = evtFech.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        r4099_evtfech_dados['verproc'] = evtFech.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        r4099_evtfech_dados['tpinsc'] = evtFech.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r4099_evtfech_dados['nrinsc'] = evtFech.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r4099_evtfech_dados['evtretpf'] = evtFech.infoFech.evtRetPF.cdata
    except AttributeError: 
        pass
    
    try:
        r4099_evtfech_dados['evtretpj'] = evtFech.infoFech.evtRetPJ.cdata
    except AttributeError: 
        pass
    
    try:
        r4099_evtfech_dados['evtpgtosnid'] = evtFech.infoFech.evtPgtosNId.cdata
    except AttributeError: 
        pass
        
    r4099_evtfech = r4099evtFech.objects.create(**r4099_evtfech_dados)
    
    if 'ideRespInf' in dir(evtFech):
    
        for ideRespInf in evtFech.ideRespInf:
    
            r4099_iderespinf_dados = {}
            r4099_iderespinf_dados['r4099_evtfech_id'] = r4099_evtfech.id
            
            try:
                r4099_iderespinf_dados['nmresp'] = ideRespInf.nmResp.cdata
            except AttributeError: 
                pass
            
            try:
                r4099_iderespinf_dados['cpfresp'] = ideRespInf.cpfResp.cdata
            except AttributeError: 
                pass
            
            try:
                r4099_iderespinf_dados['telefone'] = ideRespInf.telefone.cdata
            except AttributeError: 
                pass
            
            try:
                r4099_iderespinf_dados['email'] = ideRespInf.email.cdata
            except AttributeError: 
                pass
    
            r4099_iderespinf = r4099ideRespInf.objects.create(**r4099_iderespinf_dados)    
    r4099_evtfech_dados['evento'] = 'r4099'
    r4099_evtfech_dados['id'] = r4099_evtfech.id
    r4099_evtfech_dados['identidade_evento'] = doc.Reinf.evtFech['id']
    r4099_evtfech_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r4099_evtfech_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(r4099_evtfech.id)
    return r4099_evtfech_dados