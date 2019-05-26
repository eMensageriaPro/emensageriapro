#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2420.models import *



def read_s2420_evtcdbenterm_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2420_evtcdbenterm_obj(doc, status, validar)
    return dados



def read_s2420_evtcdbenterm(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2420_evtcdbenterm_obj(doc, status, validar)
    return dados



def read_s2420_evtcdbenterm_obj(doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2420_evtcdbenterm_dados = {}
    s2420_evtcdbenterm_dados['status'] = status
    s2420_evtcdbenterm_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2420_evtcdbenterm_dados['identidade'] = doc.eSocial.evtCdBenTerm['Id']
    evtCdBenTerm = doc.eSocial.evtCdBenTerm
    
    try:
        s2420_evtcdbenterm_dados['indretif'] = evtCdBenTerm.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        s2420_evtcdbenterm_dados['nrrecibo'] = evtCdBenTerm.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        s2420_evtcdbenterm_dados['tpamb'] = evtCdBenTerm.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s2420_evtcdbenterm_dados['procemi'] = evtCdBenTerm.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s2420_evtcdbenterm_dados['verproc'] = evtCdBenTerm.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s2420_evtcdbenterm_dados['tpinsc'] = evtCdBenTerm.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2420_evtcdbenterm_dados['nrinsc'] = evtCdBenTerm.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2420_evtcdbenterm_dados['cpfbenef'] = evtCdBenTerm.ideBeneficio.cpfBenef.cdata
    except AttributeError: 
        pass
    
    try:
        s2420_evtcdbenterm_dados['nrbeneficio'] = evtCdBenTerm.ideBeneficio.nrBeneficio.cdata
    except AttributeError: 
        pass
    
    try:
        s2420_evtcdbenterm_dados['dttermbeneficio'] = evtCdBenTerm.infoBenTermino.dtTermBeneficio.cdata
    except AttributeError: 
        pass
    
    try:
        s2420_evtcdbenterm_dados['mtvtermino'] = evtCdBenTerm.infoBenTermino.mtvTermino.cdata
    except AttributeError: 
        pass
        
    s2420_evtcdbenterm = s2420evtCdBenTerm.objects.create(**s2420_evtcdbenterm_dados)    
    s2420_evtcdbenterm_dados['evento'] = 's2420'
    s2420_evtcdbenterm_dados['id'] = s2420_evtcdbenterm.id
    s2420_evtcdbenterm_dados['identidade_evento'] = doc.eSocial.evtCdBenTerm['Id']
    s2420_evtcdbenterm_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s2420_evtcdbenterm_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(s2420_evtcdbenterm.id)
    return s2420_evtcdbenterm_dados