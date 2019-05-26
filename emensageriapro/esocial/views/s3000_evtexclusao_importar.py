#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s3000.models import *



def read_s3000_evtexclusao_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s3000_evtexclusao_obj(doc, status, validar)
    return dados



def read_s3000_evtexclusao(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s3000_evtexclusao_obj(doc, status, validar)
    return dados



def read_s3000_evtexclusao_obj(doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s3000_evtexclusao_dados = {}
    s3000_evtexclusao_dados['status'] = status
    s3000_evtexclusao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s3000_evtexclusao_dados['identidade'] = doc.eSocial.evtExclusao['Id']
    evtExclusao = doc.eSocial.evtExclusao
    
    try:
        s3000_evtexclusao_dados['tpamb'] = evtExclusao.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s3000_evtexclusao_dados['procemi'] = evtExclusao.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s3000_evtexclusao_dados['verproc'] = evtExclusao.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s3000_evtexclusao_dados['tpinsc'] = evtExclusao.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s3000_evtexclusao_dados['nrinsc'] = evtExclusao.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s3000_evtexclusao_dados['tpevento'] = evtExclusao.infoExclusao.tpEvento.cdata
    except AttributeError: 
        pass
    
    try:
        s3000_evtexclusao_dados['nrrecevt'] = evtExclusao.infoExclusao.nrRecEvt.cdata
    except AttributeError: 
        pass
        
    s3000_evtexclusao = s3000evtExclusao.objects.create(**s3000_evtexclusao_dados)
    
    if 'ideTrabalhador' in dir(evtExclusao.infoExclusao):
    
        for ideTrabalhador in evtExclusao.infoExclusao.ideTrabalhador:
    
            s3000_idetrabalhador_dados = {}
            s3000_idetrabalhador_dados['s3000_evtexclusao_id'] = s3000_evtexclusao.id
            
            try:
                s3000_idetrabalhador_dados['cpftrab'] = ideTrabalhador.cpfTrab.cdata
            except AttributeError: 
                pass
            
            try:
                s3000_idetrabalhador_dados['nistrab'] = ideTrabalhador.nisTrab.cdata
            except AttributeError: 
                pass
    
            s3000_idetrabalhador = s3000ideTrabalhador.objects.create(**s3000_idetrabalhador_dados)
    
    if 'ideFolhaPagto' in dir(evtExclusao.infoExclusao):
    
        for ideFolhaPagto in evtExclusao.infoExclusao.ideFolhaPagto:
    
            s3000_idefolhapagto_dados = {}
            s3000_idefolhapagto_dados['s3000_evtexclusao_id'] = s3000_evtexclusao.id
            
            try:
                s3000_idefolhapagto_dados['indapuracao'] = ideFolhaPagto.indApuracao.cdata
            except AttributeError: 
                pass
            
            try:
                s3000_idefolhapagto_dados['perapur'] = ideFolhaPagto.perApur.cdata
            except AttributeError: 
                pass
    
            s3000_idefolhapagto = s3000ideFolhaPagto.objects.create(**s3000_idefolhapagto_dados)    
    s3000_evtexclusao_dados['evento'] = 's3000'
    s3000_evtexclusao_dados['id'] = s3000_evtexclusao.id
    s3000_evtexclusao_dados['identidade_evento'] = doc.eSocial.evtExclusao['Id']
    s3000_evtexclusao_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s3000_evtexclusao_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(s3000_evtexclusao.id)
    return s3000_evtexclusao_dados