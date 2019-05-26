#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r2098.models import *



def read_r2098_evtreabreevper_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2098_evtreabreevper_obj(doc, status, validar)
    return dados



def read_r2098_evtreabreevper(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2098_evtreabreevper_obj(doc, status, validar)
    return dados



def read_r2098_evtreabreevper_obj(doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r2098_evtreabreevper_dados = {}
    r2098_evtreabreevper_dados['status'] = status
    r2098_evtreabreevper_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2098_evtreabreevper_dados['identidade'] = doc.Reinf.evtReabreEvPer['id']
    evtReabreEvPer = doc.Reinf.evtReabreEvPer
    
    try:
        r2098_evtreabreevper_dados['perapur'] = evtReabreEvPer.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        r2098_evtreabreevper_dados['tpamb'] = evtReabreEvPer.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        r2098_evtreabreevper_dados['procemi'] = evtReabreEvPer.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        r2098_evtreabreevper_dados['verproc'] = evtReabreEvPer.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        r2098_evtreabreevper_dados['tpinsc'] = evtReabreEvPer.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r2098_evtreabreevper_dados['nrinsc'] = evtReabreEvPer.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
        
    r2098_evtreabreevper = r2098evtReabreEvPer.objects.create(**r2098_evtreabreevper_dados)    
    r2098_evtreabreevper_dados['evento'] = 'r2098'
    r2098_evtreabreevper_dados['id'] = r2098_evtreabreevper.id
    r2098_evtreabreevper_dados['identidade_evento'] = doc.Reinf.evtReabreEvPer['id']
    r2098_evtreabreevper_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r2098_evtreabreevper_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(r2098_evtreabreevper.id)
    return r2098_evtreabreevper_dados