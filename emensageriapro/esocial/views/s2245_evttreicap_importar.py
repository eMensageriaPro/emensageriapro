#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2245.models import *



def read_s2245_evttreicap_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2245_evttreicap_obj(doc, status, validar)
    return dados



def read_s2245_evttreicap(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2245_evttreicap_obj(doc, status, validar)
    return dados



def read_s2245_evttreicap_obj(doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2245_evttreicap_dados = {}
    s2245_evttreicap_dados['status'] = status
    s2245_evttreicap_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2245_evttreicap_dados['identidade'] = doc.eSocial.evtTreiCap['Id']
    evtTreiCap = doc.eSocial.evtTreiCap
    
    try:
        s2245_evttreicap_dados['indretif'] = evtTreiCap.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['nrrecibo'] = evtTreiCap.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['tpamb'] = evtTreiCap.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['procemi'] = evtTreiCap.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['verproc'] = evtTreiCap.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['tpinsc'] = evtTreiCap.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['nrinsc'] = evtTreiCap.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['cpftrab'] = evtTreiCap.ideVinculo.cpfTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['nistrab'] = evtTreiCap.ideVinculo.nisTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['matricula'] = evtTreiCap.ideVinculo.matricula.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['codcateg'] = evtTreiCap.ideVinculo.codCateg.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['codtreicap'] = evtTreiCap.treiCap.codTreiCap.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['obstreicap'] = evtTreiCap.treiCap.obsTreiCap.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['observacao'] = evtTreiCap.treiCap.observacao.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['dttreicap'] = evtTreiCap.treiCap.infoComplem.dtTreiCap.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['durtreicap'] = evtTreiCap.treiCap.infoComplem.durTreiCap.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['modtreicap'] = evtTreiCap.treiCap.infoComplem.modTreiCap.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['tptreicap'] = evtTreiCap.treiCap.infoComplem.tpTreiCap.cdata
    except AttributeError: 
        pass
    
    try:
        s2245_evttreicap_dados['indtreinant'] = evtTreiCap.treiCap.infoComplem.indTreinAnt.cdata
    except AttributeError: 
        pass
        
    s2245_evttreicap = s2245evtTreiCap.objects.create(**s2245_evttreicap_dados)
    
    if 'ideProfResp' in dir(evtTreiCap.treiCap.infoComplem):
    
        for ideProfResp in evtTreiCap.treiCap.infoComplem.ideProfResp:
    
            s2245_ideprofresp_dados = {}
            s2245_ideprofresp_dados['s2245_evttreicap_id'] = s2245_evttreicap.id
            
            try:
                s2245_ideprofresp_dados['cpfprof'] = ideProfResp.cpfProf.cdata
            except AttributeError: 
                pass
            
            try:
                s2245_ideprofresp_dados['nmprof'] = ideProfResp.nmProf.cdata
            except AttributeError: 
                pass
            
            try:
                s2245_ideprofresp_dados['tpprof'] = ideProfResp.tpProf.cdata
            except AttributeError: 
                pass
            
            try:
                s2245_ideprofresp_dados['formprof'] = ideProfResp.formProf.cdata
            except AttributeError: 
                pass
            
            try:
                s2245_ideprofresp_dados['codcbo'] = ideProfResp.codCBO.cdata
            except AttributeError: 
                pass
            
            try:
                s2245_ideprofresp_dados['nacprof'] = ideProfResp.nacProf.cdata
            except AttributeError: 
                pass
    
            s2245_ideprofresp = s2245ideProfResp.objects.create(**s2245_ideprofresp_dados)    
    s2245_evttreicap_dados['evento'] = 's2245'
    s2245_evttreicap_dados['id'] = s2245_evttreicap.id
    s2245_evttreicap_dados['identidade_evento'] = doc.eSocial.evtTreiCap['Id']
    s2245_evttreicap_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s2245_evttreicap_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(s2245_evttreicap.id)
    return s2245_evttreicap_dados