#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s5012.models import *



def read_s5012_evtirrf_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s5012_evtirrf_obj(request, doc, status, validar)
    return dados



def read_s5012_evtirrf(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s5012_evtirrf_obj(request, doc, status, validar)

    s5012evtIrrf.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s5012_evtirrf_obj(request, doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s5012_evtirrf_dados = {}
    s5012_evtirrf_dados['status'] = status
    s5012_evtirrf_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5012_evtirrf_dados['identidade'] = doc.eSocial.evtIrrf['Id']
    evtIrrf = doc.eSocial.evtIrrf
    
    try:
        s5012_evtirrf_dados['perapur'] = evtIrrf.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        s5012_evtirrf_dados['tpinsc'] = evtIrrf.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s5012_evtirrf_dados['nrinsc'] = evtIrrf.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s5012_evtirrf_dados['nrrecarqbase'] = evtIrrf.infoIRRF.nrRecArqBase.cdata
    except AttributeError: 
        pass
    
    try:
        s5012_evtirrf_dados['indexistinfo'] = evtIrrf.infoIRRF.indExistInfo.cdata
    except AttributeError: 
        pass
        
    s5012_evtirrf = s5012evtIrrf.objects.create(**s5012_evtirrf_dados)
    
    if 'infoIRRF' in dir(evtIrrf) and 'infoCRContrib' in dir(evtIrrf.infoIRRF):
    
        for infoCRContrib in evtIrrf.infoIRRF.infoCRContrib:
    
            s5012_infocrcontrib_dados = {}
            s5012_infocrcontrib_dados['s5012_evtirrf_id'] = s5012_evtirrf.id
            
            try:
                s5012_infocrcontrib_dados['tpcr'] = infoCRContrib.tpCR.cdata
            except AttributeError: 
                pass
            
            try:
                s5012_infocrcontrib_dados['vrcr'] = infoCRContrib.vrCR.cdata
            except AttributeError: 
                pass
    
            s5012_infocrcontrib = s5012infoCRContrib.objects.create(**s5012_infocrcontrib_dados)    
    s5012_evtirrf_dados['evento'] = 's5012'
    s5012_evtirrf_dados['id'] = s5012_evtirrf.id
    s5012_evtirrf_dados['identidade_evento'] = doc.eSocial.evtIrrf['Id']
    s5012_evtirrf_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s5012_evtirrf_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, s5012_evtirrf.id)
    
    return s5012_evtirrf_dados