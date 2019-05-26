#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2220.models import *



def read_s2220_evtmonit_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2220_evtmonit_obj(doc, status, validar)
    return dados



def read_s2220_evtmonit(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2220_evtmonit_obj(doc, status, validar)
    return dados



def read_s2220_evtmonit_obj(doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2220_evtmonit_dados = {}
    s2220_evtmonit_dados['status'] = status
    s2220_evtmonit_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2220_evtmonit_dados['identidade'] = doc.eSocial.evtMonit['Id']
    evtMonit = doc.eSocial.evtMonit
    
    try:
        s2220_evtmonit_dados['indretif'] = evtMonit.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['nrrecibo'] = evtMonit.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['tpamb'] = evtMonit.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['procemi'] = evtMonit.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['verproc'] = evtMonit.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['tpinsc'] = evtMonit.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['nrinsc'] = evtMonit.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['cpftrab'] = evtMonit.ideVinculo.cpfTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['nistrab'] = evtMonit.ideVinculo.nisTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['matricula'] = evtMonit.ideVinculo.matricula.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['codcateg'] = evtMonit.ideVinculo.codCateg.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['tpexameocup'] = evtMonit.exMedOcup.tpExameOcup.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['dtaso'] = evtMonit.exMedOcup.aso.dtAso.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['tpaso'] = evtMonit.exMedOcup.aso.tpAso.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['resaso'] = evtMonit.exMedOcup.aso.resAso.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['cpfmed'] = evtMonit.exMedOcup.aso.medico.cpfMed.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['nismed'] = evtMonit.exMedOcup.aso.medico.nisMed.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['nmmed'] = evtMonit.exMedOcup.aso.medico.nmMed.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['nrcrm'] = evtMonit.exMedOcup.aso.medico.nrCRM.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['ufcrm'] = evtMonit.exMedOcup.aso.medico.ufCRM.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['nisresp'] = evtMonit.exMedOcup.respMonit.nisResp.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['nrconsclasse'] = evtMonit.exMedOcup.respMonit.nrConsClasse.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['ufconsclasse'] = evtMonit.exMedOcup.respMonit.ufConsClasse.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['cpfresp'] = evtMonit.exMedOcup.respMonit.cpfResp.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['nmresp'] = evtMonit.exMedOcup.respMonit.nmResp.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['nrcrm'] = evtMonit.exMedOcup.respMonit.nrCRM.cdata
    except AttributeError: 
        pass
    
    try:
        s2220_evtmonit_dados['ufcrm'] = evtMonit.exMedOcup.respMonit.ufCRM.cdata
    except AttributeError: 
        pass
        
    s2220_evtmonit = s2220evtMonit.objects.create(**s2220_evtmonit_dados)
    
    if 'exame' in dir(evtMonit.exMedOcup.aso):
    
        for exame in evtMonit.exMedOcup.aso.exame:
    
            s2220_exame_dados = {}
            s2220_exame_dados['s2220_evtmonit_id'] = s2220_evtmonit.id
            
            try:
                s2220_exame_dados['dtexm'] = exame.dtExm.cdata
            except AttributeError: 
                pass
            
            try:
                s2220_exame_dados['procrealizado'] = exame.procRealizado.cdata
            except AttributeError: 
                pass
            
            try:
                s2220_exame_dados['obsproc'] = exame.obsProc.cdata
            except AttributeError: 
                pass
            
            try:
                s2220_exame_dados['interprexm'] = exame.interprExm.cdata
            except AttributeError: 
                pass
            
            try:
                s2220_exame_dados['ordexame'] = exame.ordExame.cdata
            except AttributeError: 
                pass
            
            try:
                s2220_exame_dados['dtinimonit'] = exame.dtIniMonit.cdata
            except AttributeError: 
                pass
            
            try:
                s2220_exame_dados['dtfimmonit'] = exame.dtFimMonit.cdata
            except AttributeError: 
                pass
            
            try:
                s2220_exame_dados['indresult'] = exame.indResult.cdata
            except AttributeError: 
                pass
    
            s2220_exame = s2220exame.objects.create(**s2220_exame_dados)    
    s2220_evtmonit_dados['evento'] = 's2220'
    s2220_evtmonit_dados['id'] = s2220_evtmonit.id
    s2220_evtmonit_dados['identidade_evento'] = doc.eSocial.evtMonit['Id']
    s2220_evtmonit_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s2220_evtmonit_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(s2220_evtmonit.id)
    return s2220_evtmonit_dados