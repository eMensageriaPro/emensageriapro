#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2260.models import *



def read_s2260_evtconvinterm_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2260_evtconvinterm_obj(doc, status, validar)
    return dados



def read_s2260_evtconvinterm(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2260_evtconvinterm_obj(doc, status, validar)
    return dados



def read_s2260_evtconvinterm_obj(doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2260_evtconvinterm_dados = {}
    s2260_evtconvinterm_dados['status'] = status
    s2260_evtconvinterm_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2260_evtconvinterm_dados['identidade'] = doc.eSocial.evtConvInterm['Id']
    evtConvInterm = doc.eSocial.evtConvInterm
    
    try:
        s2260_evtconvinterm_dados['indretif'] = evtConvInterm.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        s2260_evtconvinterm_dados['nrrecibo'] = evtConvInterm.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        s2260_evtconvinterm_dados['tpamb'] = evtConvInterm.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s2260_evtconvinterm_dados['procemi'] = evtConvInterm.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s2260_evtconvinterm_dados['verproc'] = evtConvInterm.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s2260_evtconvinterm_dados['tpinsc'] = evtConvInterm.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2260_evtconvinterm_dados['nrinsc'] = evtConvInterm.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2260_evtconvinterm_dados['cpftrab'] = evtConvInterm.ideVinculo.cpfTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2260_evtconvinterm_dados['nistrab'] = evtConvInterm.ideVinculo.nisTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2260_evtconvinterm_dados['matricula'] = evtConvInterm.ideVinculo.matricula.cdata
    except AttributeError: 
        pass
    
    try:
        s2260_evtconvinterm_dados['codconv'] = evtConvInterm.infoConvInterm.codConv.cdata
    except AttributeError: 
        pass
    
    try:
        s2260_evtconvinterm_dados['dtinicio'] = evtConvInterm.infoConvInterm.dtInicio.cdata
    except AttributeError: 
        pass
    
    try:
        s2260_evtconvinterm_dados['dtfim'] = evtConvInterm.infoConvInterm.dtFim.cdata
    except AttributeError: 
        pass
    
    try:
        s2260_evtconvinterm_dados['dtprevpgto'] = evtConvInterm.infoConvInterm.dtPrevPgto.cdata
    except AttributeError: 
        pass
    
    try:
        s2260_evtconvinterm_dados['codhorcontrat'] = evtConvInterm.infoConvInterm.jornada.codHorContrat.cdata
    except AttributeError: 
        pass
    
    try:
        s2260_evtconvinterm_dados['dscjornada'] = evtConvInterm.infoConvInterm.jornada.dscJornada.cdata
    except AttributeError: 
        pass
    
    try:
        s2260_evtconvinterm_dados['indlocal'] = evtConvInterm.infoConvInterm.localTrab.indLocal.cdata
    except AttributeError: 
        pass
        
    s2260_evtconvinterm = s2260evtConvInterm.objects.create(**s2260_evtconvinterm_dados)
    
    if 'localTrabInterm' in dir(evtConvInterm.infoConvInterm.localTrab):
    
        for localTrabInterm in evtConvInterm.infoConvInterm.localTrab.localTrabInterm:
    
            s2260_localtrabinterm_dados = {}
            s2260_localtrabinterm_dados['s2260_evtconvinterm_id'] = s2260_evtconvinterm.id
            
            try:
                s2260_localtrabinterm_dados['tplograd'] = localTrabInterm.tpLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2260_localtrabinterm_dados['dsclograd'] = localTrabInterm.dscLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2260_localtrabinterm_dados['nrlograd'] = localTrabInterm.nrLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2260_localtrabinterm_dados['complem'] = localTrabInterm.complem.cdata
            except AttributeError: 
                pass
            
            try:
                s2260_localtrabinterm_dados['bairro'] = localTrabInterm.bairro.cdata
            except AttributeError: 
                pass
            
            try:
                s2260_localtrabinterm_dados['cep'] = localTrabInterm.cep.cdata
            except AttributeError: 
                pass
            
            try:
                s2260_localtrabinterm_dados['codmunic'] = localTrabInterm.codMunic.cdata
            except AttributeError: 
                pass
            
            try:
                s2260_localtrabinterm_dados['uf'] = localTrabInterm.uf.cdata
            except AttributeError: 
                pass
    
            s2260_localtrabinterm = s2260localTrabInterm.objects.create(**s2260_localtrabinterm_dados)    
    s2260_evtconvinterm_dados['evento'] = 's2260'
    s2260_evtconvinterm_dados['id'] = s2260_evtconvinterm.id
    s2260_evtconvinterm_dados['identidade_evento'] = doc.eSocial.evtConvInterm['Id']
    s2260_evtconvinterm_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s2260_evtconvinterm_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(s2260_evtconvinterm.id)
    return s2260_evtconvinterm_dados