#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r9000.models import *



def read_r9000_evtexclusao_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r9000_evtexclusao_obj(request, doc, status, validar)
    return dados



def read_r9000_evtexclusao(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r9000_evtexclusao_obj(request, doc, status, validar)

    r9000evtExclusao.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_r9000_evtexclusao_obj(request, doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r9000_evtexclusao_dados = {}
    r9000_evtexclusao_dados['status'] = status
    r9000_evtexclusao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r9000_evtexclusao_dados['identidade'] = doc.Reinf.evtExclusao['id']
    evtExclusao = doc.Reinf.evtExclusao
    
    try:
        r9000_evtexclusao_dados['tpamb'] = evtExclusao.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        r9000_evtexclusao_dados['procemi'] = evtExclusao.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        r9000_evtexclusao_dados['verproc'] = evtExclusao.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        r9000_evtexclusao_dados['tpinsc'] = evtExclusao.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r9000_evtexclusao_dados['nrinsc'] = evtExclusao.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r9000_evtexclusao_dados['tpevento'] = evtExclusao.infoExclusao.tpEvento.cdata
    except AttributeError: 
        pass
    
    try:
        r9000_evtexclusao_dados['nrrecevt'] = evtExclusao.infoExclusao.nrRecEvt.cdata
    except AttributeError: 
        pass
    
    try:
        r9000_evtexclusao_dados['perapur'] = evtExclusao.infoExclusao.perApur.cdata
    except AttributeError: 
        pass
        
    r9000_evtexclusao = r9000evtExclusao.objects.create(**r9000_evtexclusao_dados)    
    r9000_evtexclusao_dados['evento'] = 'r9000'
    r9000_evtexclusao_dados['id'] = r9000_evtexclusao.id
    r9000_evtexclusao_dados['identidade_evento'] = doc.Reinf.evtExclusao['id']
    r9000_evtexclusao_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r9000_evtexclusao_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, r9000_evtexclusao.id)
    
    return r9000_evtexclusao_dados