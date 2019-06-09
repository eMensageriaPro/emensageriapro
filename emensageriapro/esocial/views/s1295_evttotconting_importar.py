#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1295.models import *



def read_s1295_evttotconting_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1295_evttotconting_obj(request, doc, status, validar)
    return dados



def read_s1295_evttotconting(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1295_evttotconting_obj(request, doc, status, validar)

    s1295evtTotConting.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s1295_evttotconting_obj(request, doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1295_evttotconting_dados = {}
    s1295_evttotconting_dados['status'] = status
    s1295_evttotconting_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1295_evttotconting_dados['identidade'] = doc.eSocial.evtTotConting['Id']
    evtTotConting = doc.eSocial.evtTotConting
    
    try:
        s1295_evttotconting_dados['indapuracao'] = evtTotConting.ideEvento.indApuracao.cdata
    except AttributeError: 
        pass
    
    try:
        s1295_evttotconting_dados['perapur'] = evtTotConting.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        s1295_evttotconting_dados['tpamb'] = evtTotConting.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s1295_evttotconting_dados['procemi'] = evtTotConting.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s1295_evttotconting_dados['verproc'] = evtTotConting.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s1295_evttotconting_dados['tpinsc'] = evtTotConting.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s1295_evttotconting_dados['nrinsc'] = evtTotConting.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
        
    s1295_evttotconting = s1295evtTotConting.objects.create(**s1295_evttotconting_dados)
    
    if 'ideRespInf' in dir(evtTotConting):
    
        for ideRespInf in evtTotConting.ideRespInf:
    
            s1295_iderespinf_dados = {}
            s1295_iderespinf_dados['s1295_evttotconting_id'] = s1295_evttotconting.id
            
            try:
                s1295_iderespinf_dados['nmresp'] = ideRespInf.nmResp.cdata
            except AttributeError: 
                pass
            
            try:
                s1295_iderespinf_dados['cpfresp'] = ideRespInf.cpfResp.cdata
            except AttributeError: 
                pass
            
            try:
                s1295_iderespinf_dados['telefone'] = ideRespInf.telefone.cdata
            except AttributeError: 
                pass
            
            try:
                s1295_iderespinf_dados['email'] = ideRespInf.email.cdata
            except AttributeError: 
                pass
    
            s1295_iderespinf = s1295ideRespInf.objects.create(**s1295_iderespinf_dados)    
    s1295_evttotconting_dados['evento'] = 's1295'
    s1295_evttotconting_dados['id'] = s1295_evttotconting.id
    s1295_evttotconting_dados['identidade_evento'] = doc.eSocial.evtTotConting['Id']
    s1295_evttotconting_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s1295_evttotconting_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, s1295_evttotconting.id)
    
    return s1295_evttotconting_dados