#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r4098.models import *



def read_r4098_evtreab_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r4098_evtreab_obj(request, doc, status, validar)
    return dados



def read_r4098_evtreab(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r4098_evtreab_obj(request, doc, status, validar)

    r4098evtReab.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_r4098_evtreab_obj(request, doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r4098_evtreab_dados = {}
    r4098_evtreab_dados['status'] = status
    r4098_evtreab_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r4098_evtreab_dados['identidade'] = doc.Reinf.evtReab['id']
    evtReab = doc.Reinf.evtReab
    
    try:
        r4098_evtreab_dados['perapur'] = evtReab.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        r4098_evtreab_dados['tpamb'] = evtReab.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        r4098_evtreab_dados['procemi'] = evtReab.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        r4098_evtreab_dados['verproc'] = evtReab.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        r4098_evtreab_dados['tpinsc'] = evtReab.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r4098_evtreab_dados['nrinsc'] = evtReab.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
        
    r4098_evtreab = r4098evtReab.objects.create(**r4098_evtreab_dados)    
    r4098_evtreab_dados['evento'] = 'r4098'
    r4098_evtreab_dados['id'] = r4098_evtreab.id
    r4098_evtreab_dados['identidade_evento'] = doc.Reinf.evtReab['id']
    r4098_evtreab_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r4098_evtreab_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, r4098_evtreab.id)
    
    return r4098_evtreab_dados