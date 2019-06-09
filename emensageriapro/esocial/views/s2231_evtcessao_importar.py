#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2231.models import *



def read_s2231_evtcessao_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2231_evtcessao_obj(request, doc, status, validar)
    return dados



def read_s2231_evtcessao(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2231_evtcessao_obj(request, doc, status, validar)

    s2231evtCessao.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s2231_evtcessao_obj(request, doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2231_evtcessao_dados = {}
    s2231_evtcessao_dados['status'] = status
    s2231_evtcessao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2231_evtcessao_dados['identidade'] = doc.eSocial.evtCessao['Id']
    evtCessao = doc.eSocial.evtCessao
    
    try:
        s2231_evtcessao_dados['indretif'] = evtCessao.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        s2231_evtcessao_dados['nrrecibo'] = evtCessao.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        s2231_evtcessao_dados['tpamb'] = evtCessao.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s2231_evtcessao_dados['procemi'] = evtCessao.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s2231_evtcessao_dados['verproc'] = evtCessao.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s2231_evtcessao_dados['tpinsc'] = evtCessao.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2231_evtcessao_dados['nrinsc'] = evtCessao.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2231_evtcessao_dados['cpftrab'] = evtCessao.ideVinculo.cpfTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2231_evtcessao_dados['nistrab'] = evtCessao.ideVinculo.nisTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2231_evtcessao_dados['matricula'] = evtCessao.ideVinculo.matricula.cdata
    except AttributeError: 
        pass
        
    s2231_evtcessao = s2231evtCessao.objects.create(**s2231_evtcessao_dados)
    
    if 'iniCessao' in dir(evtCessao.infoCessao):
    
        for iniCessao in evtCessao.infoCessao.iniCessao:
    
            s2231_inicessao_dados = {}
            s2231_inicessao_dados['s2231_evtcessao_id'] = s2231_evtcessao.id
            
            try:
                s2231_inicessao_dados['dtinicessao'] = iniCessao.dtIniCessao.cdata
            except AttributeError: 
                pass
            
            try:
                s2231_inicessao_dados['cnpjcess'] = iniCessao.cnpjCess.cdata
            except AttributeError: 
                pass
            
            try:
                s2231_inicessao_dados['infonus'] = iniCessao.infOnus.cdata
            except AttributeError: 
                pass
            
            try:
                s2231_inicessao_dados['indcessao'] = iniCessao.indCessao.cdata
            except AttributeError: 
                pass
            
            try:
                s2231_inicessao_dados['dscsituacao'] = iniCessao.dscSituacao.cdata
            except AttributeError: 
                pass
    
            s2231_inicessao = s2231iniCessao.objects.create(**s2231_inicessao_dados)
    
    if 'fimCessao' in dir(evtCessao.infoCessao):
    
        for fimCessao in evtCessao.infoCessao.fimCessao:
    
            s2231_fimcessao_dados = {}
            s2231_fimcessao_dados['s2231_evtcessao_id'] = s2231_evtcessao.id
            
            try:
                s2231_fimcessao_dados['dttermcessao'] = fimCessao.dtTermCessao.cdata
            except AttributeError: 
                pass
    
            s2231_fimcessao = s2231fimCessao.objects.create(**s2231_fimcessao_dados)    
    s2231_evtcessao_dados['evento'] = 's2231'
    s2231_evtcessao_dados['id'] = s2231_evtcessao.id
    s2231_evtcessao_dados['identidade_evento'] = doc.eSocial.evtCessao['Id']
    s2231_evtcessao_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s2231_evtcessao_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, s2231_evtcessao.id)
    
    return s2231_evtcessao_dados