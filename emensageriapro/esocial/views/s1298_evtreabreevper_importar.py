#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1298.models import *



def read_s1298_evtreabreevper_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1298_evtreabreevper_obj(doc, status, validar)
    return dados



def read_s1298_evtreabreevper(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1298_evtreabreevper_obj(doc, status, validar)
    return dados



def read_s1298_evtreabreevper_obj(doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1298_evtreabreevper_dados = {}
    s1298_evtreabreevper_dados['status'] = status
    s1298_evtreabreevper_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1298_evtreabreevper_dados['identidade'] = doc.eSocial.evtReabreEvPer['Id']
    evtReabreEvPer = doc.eSocial.evtReabreEvPer
    
    try:
        s1298_evtreabreevper_dados['indapuracao'] = evtReabreEvPer.ideEvento.indApuracao.cdata
    except AttributeError: 
        pass
    
    try:
        s1298_evtreabreevper_dados['perapur'] = evtReabreEvPer.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        s1298_evtreabreevper_dados['tpamb'] = evtReabreEvPer.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s1298_evtreabreevper_dados['procemi'] = evtReabreEvPer.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s1298_evtreabreevper_dados['verproc'] = evtReabreEvPer.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s1298_evtreabreevper_dados['tpinsc'] = evtReabreEvPer.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s1298_evtreabreevper_dados['nrinsc'] = evtReabreEvPer.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
        
    s1298_evtreabreevper = s1298evtReabreEvPer.objects.create(**s1298_evtreabreevper_dados)    
    s1298_evtreabreevper_dados['evento'] = 's1298'
    s1298_evtreabreevper_dados['id'] = s1298_evtreabreevper.id
    s1298_evtreabreevper_dados['identidade_evento'] = doc.eSocial.evtReabreEvPer['Id']
    s1298_evtreabreevper_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s1298_evtreabreevper_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(s1298_evtreabreevper.id)
    return s1298_evtreabreevper_dados