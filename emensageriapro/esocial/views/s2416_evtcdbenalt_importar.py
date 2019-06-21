#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2416.models import *



def read_s2416_evtcdbenalt_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2416_evtcdbenalt_obj(request, doc, status, validar)
    return dados



def read_s2416_evtcdbenalt(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2416_evtcdbenalt_obj(request, doc, status, validar)

    s2416evtCdBenAlt.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s2416_evtcdbenalt_obj(request, doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2416_evtcdbenalt_dados = {}
    s2416_evtcdbenalt_dados['status'] = status
    s2416_evtcdbenalt_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2416_evtcdbenalt_dados['identidade'] = doc.eSocial.evtCdBenAlt['Id']
    evtCdBenAlt = doc.eSocial.evtCdBenAlt
    
    try:
        s2416_evtcdbenalt_dados['indretif'] = evtCdBenAlt.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        s2416_evtcdbenalt_dados['nrrecibo'] = evtCdBenAlt.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        s2416_evtcdbenalt_dados['tpamb'] = evtCdBenAlt.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s2416_evtcdbenalt_dados['procemi'] = evtCdBenAlt.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s2416_evtcdbenalt_dados['verproc'] = evtCdBenAlt.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s2416_evtcdbenalt_dados['tpinsc'] = evtCdBenAlt.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2416_evtcdbenalt_dados['nrinsc'] = evtCdBenAlt.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2416_evtcdbenalt_dados['cpfbenef'] = evtCdBenAlt.ideBeneficio.cpfBenef.cdata
    except AttributeError: 
        pass
    
    try:
        s2416_evtcdbenalt_dados['nrbeneficio'] = evtCdBenAlt.ideBeneficio.nrBeneficio.cdata
    except AttributeError: 
        pass
    
    try:
        s2416_evtcdbenalt_dados['dtaltbeneficio'] = evtCdBenAlt.infoBenAlteracao.dtAltBeneficio.cdata
    except AttributeError: 
        pass
    
    try:
        s2416_evtcdbenalt_dados['tpbeneficio'] = evtCdBenAlt.infoBenAlteracao.dadosBeneficio.tpBeneficio.cdata
    except AttributeError: 
        pass
    
    try:
        s2416_evtcdbenalt_dados['tpplanrp'] = evtCdBenAlt.infoBenAlteracao.dadosBeneficio.tpPlanRP.cdata
    except AttributeError: 
        pass
    
    try:
        s2416_evtcdbenalt_dados['dsc'] = evtCdBenAlt.infoBenAlteracao.dadosBeneficio.dsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2416_evtcdbenalt_dados['inddecjud'] = evtCdBenAlt.infoBenAlteracao.dadosBeneficio.indDecJud.cdata
    except AttributeError: 
        pass
    
    try:
        s2416_evtcdbenalt_dados['indhomologtc'] = evtCdBenAlt.infoBenAlteracao.dadosBeneficio.indHomologTC.cdata
    except AttributeError: 
        pass
    
    try:
        s2416_evtcdbenalt_dados['indsuspensao'] = evtCdBenAlt.infoBenAlteracao.dadosBeneficio.indSuspensao.cdata
    except AttributeError: 
        pass
        
    s2416_evtcdbenalt = s2416evtCdBenAlt.objects.create(**s2416_evtcdbenalt_dados)
    
    if 'infoBenAlteracao' in dir(evtCdBenAlt) and 'dadosBeneficio' in dir(evtCdBenAlt.infoBenAlteracao) and 'infoPenMorte' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio):
    
        for infoPenMorte in evtCdBenAlt.infoBenAlteracao.dadosBeneficio.infoPenMorte:
    
            s2416_infopenmorte_dados = {}
            s2416_infopenmorte_dados['s2416_evtcdbenalt_id'] = s2416_evtcdbenalt.id
            
            try:
                s2416_infopenmorte_dados['tppenmorte'] = infoPenMorte.tpPenMorte.cdata
            except AttributeError: 
                pass
    
            s2416_infopenmorte = s2416infoPenMorte.objects.create(**s2416_infopenmorte_dados)
    
    if 'infoBenAlteracao' in dir(evtCdBenAlt) and 'dadosBeneficio' in dir(evtCdBenAlt.infoBenAlteracao) and 'homologTC' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio):
    
        for homologTC in evtCdBenAlt.infoBenAlteracao.dadosBeneficio.homologTC:
    
            s2416_homologtc_dados = {}
            s2416_homologtc_dados['s2416_evtcdbenalt_id'] = s2416_evtcdbenalt.id
            
            try:
                s2416_homologtc_dados['nratolegal'] = homologTC.nrAtoLegal.cdata
            except AttributeError: 
                pass
    
            s2416_homologtc = s2416homologTC.objects.create(**s2416_homologtc_dados)
    
    if 'infoBenAlteracao' in dir(evtCdBenAlt) and 'dadosBeneficio' in dir(evtCdBenAlt.infoBenAlteracao) and 'suspensao' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio):
    
        for suspensao in evtCdBenAlt.infoBenAlteracao.dadosBeneficio.suspensao:
    
            s2416_suspensao_dados = {}
            s2416_suspensao_dados['s2416_evtcdbenalt_id'] = s2416_evtcdbenalt.id
            
            try:
                s2416_suspensao_dados['mtvsuspensao'] = suspensao.mtvSuspensao.cdata
            except AttributeError: 
                pass
            
            try:
                s2416_suspensao_dados['dscsuspensao'] = suspensao.dscSuspensao.cdata
            except AttributeError: 
                pass
    
            s2416_suspensao = s2416suspensao.objects.create(**s2416_suspensao_dados)    
    s2416_evtcdbenalt_dados['evento'] = 's2416'
    s2416_evtcdbenalt_dados['id'] = s2416_evtcdbenalt.id
    s2416_evtcdbenalt_dados['identidade_evento'] = doc.eSocial.evtCdBenAlt['Id']
    s2416_evtcdbenalt_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s2416_evtcdbenalt_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, s2416_evtcdbenalt.id)
    
    return s2416_evtcdbenalt_dados