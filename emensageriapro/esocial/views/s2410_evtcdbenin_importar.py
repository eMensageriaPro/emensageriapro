#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2410.models import *



def read_s2410_evtcdbenin_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2410_evtcdbenin_obj(doc, status, validar)
    return dados



def read_s2410_evtcdbenin(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2410_evtcdbenin_obj(doc, status, validar)
    return dados



def read_s2410_evtcdbenin_obj(doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2410_evtcdbenin_dados = {}
    s2410_evtcdbenin_dados['status'] = status
    s2410_evtcdbenin_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2410_evtcdbenin_dados['identidade'] = doc.eSocial.evtCdBenIn['Id']
    evtCdBenIn = doc.eSocial.evtCdBenIn
    
    try:
        s2410_evtcdbenin_dados['indretif'] = evtCdBenIn.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['nrrecibo'] = evtCdBenIn.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['tpamb'] = evtCdBenIn.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['procemi'] = evtCdBenIn.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['verproc'] = evtCdBenIn.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['tpinsc'] = evtCdBenIn.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['nrinsc'] = evtCdBenIn.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['cpfbenef'] = evtCdBenIn.beneficiario.cpfBenef.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['matricula'] = evtCdBenIn.beneficiario.matricula.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['cnpjorigem'] = evtCdBenIn.beneficiario.cnpjOrigem.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['cadini'] = evtCdBenIn.infoBenInicio.cadIni.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['nrbeneficio'] = evtCdBenIn.infoBenInicio.nrBeneficio.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['dtinibeneficio'] = evtCdBenIn.infoBenInicio.dtIniBeneficio.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['tpbeneficio'] = evtCdBenIn.infoBenInicio.dadosBeneficio.tpBeneficio.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['vrbeneficio'] = evtCdBenIn.infoBenInicio.dadosBeneficio.vrBeneficio.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['tpplanrp'] = evtCdBenIn.infoBenInicio.dadosBeneficio.tpPlanRP.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['dsc'] = evtCdBenIn.infoBenInicio.dadosBeneficio.dsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['inddecjud'] = evtCdBenIn.infoBenInicio.dadosBeneficio.indDecJud.cdata
    except AttributeError: 
        pass
    
    try:
        s2410_evtcdbenin_dados['indhomologtc'] = evtCdBenIn.infoBenInicio.dadosBeneficio.indHomologTC.cdata
    except AttributeError: 
        pass
        
    s2410_evtcdbenin = s2410evtCdBenIn.objects.create(**s2410_evtcdbenin_dados)
    
    if 'infoPenMorte' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio):
    
        for infoPenMorte in evtCdBenIn.infoBenInicio.dadosBeneficio.infoPenMorte:
    
            s2410_infopenmorte_dados = {}
            s2410_infopenmorte_dados['s2410_evtcdbenin_id'] = s2410_evtcdbenin.id
            
            try:
                s2410_infopenmorte_dados['tppenmorte'] = infoPenMorte.tpPenMorte.cdata
            except AttributeError: 
                pass
    
            s2410_infopenmorte = s2410infoPenMorte.objects.create(**s2410_infopenmorte_dados)
            
            if 'instPenMorte' in dir(infoPenMorte):
            
                for instPenMorte in infoPenMorte.instPenMorte:
            
                    s2410_instpenmorte_dados = {}
                    s2410_instpenmorte_dados['s2410_infopenmorte_id'] = s2410_infopenmorte.id
                    
                    try:
                        s2410_instpenmorte_dados['cpfinst'] = instPenMorte.cpfInst.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2410_instpenmorte_dados['dtinst'] = instPenMorte.dtInst.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2410_instpenmorte_dados['intaposentado'] = instPenMorte.intAposentado.cdata
                    except AttributeError: 
                        pass
            
                    s2410_instpenmorte = s2410instPenMorte.objects.create(**s2410_instpenmorte_dados)
    
    if 'homologTC' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio):
    
        for homologTC in evtCdBenIn.infoBenInicio.dadosBeneficio.homologTC:
    
            s2410_homologtc_dados = {}
            s2410_homologtc_dados['s2410_evtcdbenin_id'] = s2410_evtcdbenin.id
            
            try:
                s2410_homologtc_dados['dthomol'] = homologTC.dtHomol.cdata
            except AttributeError: 
                pass
            
            try:
                s2410_homologtc_dados['nratolegal'] = homologTC.nrAtoLegal.cdata
            except AttributeError: 
                pass
    
            s2410_homologtc = s2410homologTC.objects.create(**s2410_homologtc_dados)    
    s2410_evtcdbenin_dados['evento'] = 's2410'
    s2410_evtcdbenin_dados['id'] = s2410_evtcdbenin.id
    s2410_evtcdbenin_dados['identidade_evento'] = doc.eSocial.evtCdBenIn['Id']
    s2410_evtcdbenin_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s2410_evtcdbenin_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(s2410_evtcdbenin.id)
    return s2410_evtcdbenin_dados