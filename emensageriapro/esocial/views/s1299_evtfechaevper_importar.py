#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1299.models import *



def read_s1299_evtfechaevper_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1299_evtfechaevper_obj(request, doc, status, validar)
    return dados



def read_s1299_evtfechaevper(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1299_evtfechaevper_obj(request, doc, status, validar)

    s1299evtFechaEvPer.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s1299_evtfechaevper_obj(request, doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1299_evtfechaevper_dados = {}
    s1299_evtfechaevper_dados['status'] = status
    s1299_evtfechaevper_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1299_evtfechaevper_dados['identidade'] = doc.eSocial.evtFechaEvPer['Id']
    evtFechaEvPer = doc.eSocial.evtFechaEvPer
    
    try:
        s1299_evtfechaevper_dados['indapuracao'] = evtFechaEvPer.ideEvento.indApuracao.cdata
    except AttributeError: 
        pass
    
    try:
        s1299_evtfechaevper_dados['perapur'] = evtFechaEvPer.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        s1299_evtfechaevper_dados['tpamb'] = evtFechaEvPer.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s1299_evtfechaevper_dados['procemi'] = evtFechaEvPer.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s1299_evtfechaevper_dados['verproc'] = evtFechaEvPer.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s1299_evtfechaevper_dados['tpinsc'] = evtFechaEvPer.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s1299_evtfechaevper_dados['nrinsc'] = evtFechaEvPer.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s1299_evtfechaevper_dados['evtremun'] = evtFechaEvPer.infoFech.evtRemun.cdata
    except AttributeError: 
        pass
    
    try:
        s1299_evtfechaevper_dados['evtpgtos'] = evtFechaEvPer.infoFech.evtPgtos.cdata
    except AttributeError: 
        pass
    
    try:
        s1299_evtfechaevper_dados['evtaqprod'] = evtFechaEvPer.infoFech.evtAqProd.cdata
    except AttributeError: 
        pass
    
    try:
        s1299_evtfechaevper_dados['evtcomprod'] = evtFechaEvPer.infoFech.evtComProd.cdata
    except AttributeError: 
        pass
    
    try:
        s1299_evtfechaevper_dados['evtcontratavnp'] = evtFechaEvPer.infoFech.evtContratAvNP.cdata
    except AttributeError: 
        pass
    
    try:
        s1299_evtfechaevper_dados['evtinfocomplper'] = evtFechaEvPer.infoFech.evtInfoComplPer.cdata
    except AttributeError: 
        pass
    
    try:
        s1299_evtfechaevper_dados['compsemmovto'] = evtFechaEvPer.infoFech.compSemMovto.cdata
    except AttributeError: 
        pass
        
    s1299_evtfechaevper = s1299evtFechaEvPer.objects.create(**s1299_evtfechaevper_dados)
    
    if 'ideRespInf' in dir(evtFechaEvPer):
    
        for ideRespInf in evtFechaEvPer.ideRespInf:
    
            s1299_iderespinf_dados = {}
            s1299_iderespinf_dados['s1299_evtfechaevper_id'] = s1299_evtfechaevper.id
            
            try:
                s1299_iderespinf_dados['nmresp'] = ideRespInf.nmResp.cdata
            except AttributeError: 
                pass
            
            try:
                s1299_iderespinf_dados['cpfresp'] = ideRespInf.cpfResp.cdata
            except AttributeError: 
                pass
            
            try:
                s1299_iderespinf_dados['telefone'] = ideRespInf.telefone.cdata
            except AttributeError: 
                pass
            
            try:
                s1299_iderespinf_dados['email'] = ideRespInf.email.cdata
            except AttributeError: 
                pass
    
            s1299_iderespinf = s1299ideRespInf.objects.create(**s1299_iderespinf_dados)    
    s1299_evtfechaevper_dados['evento'] = 's1299'
    s1299_evtfechaevper_dados['id'] = s1299_evtfechaevper.id
    s1299_evtfechaevper_dados['identidade_evento'] = doc.eSocial.evtFechaEvPer['Id']
    s1299_evtfechaevper_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s1299_evtfechaevper_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, s1299_evtfechaevper.id)
    
    return s1299_evtfechaevper_dados