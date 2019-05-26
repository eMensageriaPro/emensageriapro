#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1300.models import *



def read_s1300_evtcontrsindpatr_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1300_evtcontrsindpatr_obj(doc, status, validar)
    return dados



def read_s1300_evtcontrsindpatr(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1300_evtcontrsindpatr_obj(doc, status, validar)
    return dados



def read_s1300_evtcontrsindpatr_obj(doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1300_evtcontrsindpatr_dados = {}
    s1300_evtcontrsindpatr_dados['status'] = status
    s1300_evtcontrsindpatr_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1300_evtcontrsindpatr_dados['identidade'] = doc.eSocial.evtContrSindPatr['Id']
    evtContrSindPatr = doc.eSocial.evtContrSindPatr
    
    try:
        s1300_evtcontrsindpatr_dados['indretif'] = evtContrSindPatr.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        s1300_evtcontrsindpatr_dados['nrrecibo'] = evtContrSindPatr.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        s1300_evtcontrsindpatr_dados['indapuracao'] = evtContrSindPatr.ideEvento.indApuracao.cdata
    except AttributeError: 
        pass
    
    try:
        s1300_evtcontrsindpatr_dados['perapur'] = evtContrSindPatr.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        s1300_evtcontrsindpatr_dados['tpamb'] = evtContrSindPatr.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s1300_evtcontrsindpatr_dados['procemi'] = evtContrSindPatr.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s1300_evtcontrsindpatr_dados['verproc'] = evtContrSindPatr.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s1300_evtcontrsindpatr_dados['tpinsc'] = evtContrSindPatr.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s1300_evtcontrsindpatr_dados['nrinsc'] = evtContrSindPatr.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
        
    s1300_evtcontrsindpatr = s1300evtContrSindPatr.objects.create(**s1300_evtcontrsindpatr_dados)
    
    if 'contribSind' in dir(evtContrSindPatr):
    
        for contribSind in evtContrSindPatr.contribSind:
    
            s1300_contribsind_dados = {}
            s1300_contribsind_dados['s1300_evtcontrsindpatr_id'] = s1300_evtcontrsindpatr.id
            
            try:
                s1300_contribsind_dados['cnpjsindic'] = contribSind.cnpjSindic.cdata
            except AttributeError: 
                pass
            
            try:
                s1300_contribsind_dados['tpcontribsind'] = contribSind.tpContribSind.cdata
            except AttributeError: 
                pass
            
            try:
                s1300_contribsind_dados['vlrcontribsind'] = contribSind.vlrContribSind.cdata
            except AttributeError: 
                pass
    
            s1300_contribsind = s1300contribSind.objects.create(**s1300_contribsind_dados)    
    s1300_evtcontrsindpatr_dados['evento'] = 's1300'
    s1300_evtcontrsindpatr_dados['id'] = s1300_evtcontrsindpatr.id
    s1300_evtcontrsindpatr_dados['identidade_evento'] = doc.eSocial.evtContrSindPatr['Id']
    s1300_evtcontrsindpatr_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s1300_evtcontrsindpatr_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(s1300_evtcontrsindpatr.id)
    return s1300_evtcontrsindpatr_dados