#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s5013.models import *



def read_s5013_evtfgts_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s5013_evtfgts_obj(doc, status, validar)
    return dados



def read_s5013_evtfgts(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s5013_evtfgts_obj(doc, status, validar)
    return dados



def read_s5013_evtfgts_obj(doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s5013_evtfgts_dados = {}
    s5013_evtfgts_dados['status'] = status
    s5013_evtfgts_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5013_evtfgts_dados['identidade'] = doc.eSocial.evtFGTS['Id']
    evtFGTS = doc.eSocial.evtFGTS
    
    try:
        s5013_evtfgts_dados['perapur'] = evtFGTS.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        s5013_evtfgts_dados['tpinsc'] = evtFGTS.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s5013_evtfgts_dados['nrinsc'] = evtFGTS.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s5013_evtfgts_dados['nrrecarqbase'] = evtFGTS.infoFGTS.nrRecArqBase.cdata
    except AttributeError: 
        pass
    
    try:
        s5013_evtfgts_dados['indexistinfo'] = evtFGTS.infoFGTS.indExistInfo.cdata
    except AttributeError: 
        pass
        
    s5013_evtfgts = s5013evtFGTS.objects.create(**s5013_evtfgts_dados)
    
    if 'infoBaseFGTS' in dir(evtFGTS.infoFGTS):
    
        for infoBaseFGTS in evtFGTS.infoFGTS.infoBaseFGTS:
    
            s5013_infobasefgts_dados = {}
            s5013_infobasefgts_dados['s5013_evtfgts_id'] = s5013_evtfgts.id
    
            s5013_infobasefgts = s5013infoBaseFGTS.objects.create(**s5013_infobasefgts_dados)
            
            if 'basePerApur' in dir(infoBaseFGTS):
            
                for basePerApur in infoBaseFGTS.basePerApur:
            
                    s5013_baseperapur_dados = {}
                    s5013_baseperapur_dados['s5013_infobasefgts_id'] = s5013_infobasefgts.id
                    
                    try:
                        s5013_baseperapur_dados['tpvalor'] = basePerApur.tpValor.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5013_baseperapur_dados['basefgts'] = basePerApur.baseFGTS.cdata
                    except AttributeError: 
                        pass
            
                    s5013_baseperapur = s5013basePerApur.objects.create(**s5013_baseperapur_dados)
            
            if 'infoBasePerAntE' in dir(infoBaseFGTS):
            
                for infoBasePerAntE in infoBaseFGTS.infoBasePerAntE:
            
                    s5013_infobaseperante_dados = {}
                    s5013_infobaseperante_dados['s5013_infobasefgts_id'] = s5013_infobasefgts.id
                    
                    try:
                        s5013_infobaseperante_dados['perref'] = infoBasePerAntE.perRef.cdata
                    except AttributeError: 
                        pass
            
                    s5013_infobaseperante = s5013infoBasePerAntE.objects.create(**s5013_infobaseperante_dados)
                    
                    if 'basePerAntE' in dir(infoBasePerAntE):
                    
                        for basePerAntE in infoBasePerAntE.basePerAntE:
                    
                            s5013_baseperante_dados = {}
                            s5013_baseperante_dados['s5013_infobaseperante_id'] = s5013_infobaseperante.id
                            
                            try:
                                s5013_baseperante_dados['tpvalore'] = basePerAntE.tpValorE.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5013_baseperante_dados['basefgtse'] = basePerAntE.baseFGTSE.cdata
                            except AttributeError: 
                                pass
                    
                            s5013_baseperante = s5013basePerAntE.objects.create(**s5013_baseperante_dados)
    
    if 'infoDpsFGTS' in dir(evtFGTS.infoFGTS):
    
        for infoDpsFGTS in evtFGTS.infoFGTS.infoDpsFGTS:
    
            s5013_infodpsfgts_dados = {}
            s5013_infodpsfgts_dados['s5013_evtfgts_id'] = s5013_evtfgts.id
    
            s5013_infodpsfgts = s5013infoDpsFGTS.objects.create(**s5013_infodpsfgts_dados)
            
            if 'dpsPerApur' in dir(infoDpsFGTS):
            
                for dpsPerApur in infoDpsFGTS.dpsPerApur:
            
                    s5013_dpsperapur_dados = {}
                    s5013_dpsperapur_dados['s5013_infodpsfgts_id'] = s5013_infodpsfgts.id
                    
                    try:
                        s5013_dpsperapur_dados['tpdps'] = dpsPerApur.tpDps.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5013_dpsperapur_dados['vrfgts'] = dpsPerApur.vrFGTS.cdata
                    except AttributeError: 
                        pass
            
                    s5013_dpsperapur = s5013dpsPerApur.objects.create(**s5013_dpsperapur_dados)
            
            if 'infoDpsPerAntE' in dir(infoDpsFGTS):
            
                for infoDpsPerAntE in infoDpsFGTS.infoDpsPerAntE:
            
                    s5013_infodpsperante_dados = {}
                    s5013_infodpsperante_dados['s5013_infodpsfgts_id'] = s5013_infodpsfgts.id
                    
                    try:
                        s5013_infodpsperante_dados['perref'] = infoDpsPerAntE.perRef.cdata
                    except AttributeError: 
                        pass
            
                    s5013_infodpsperante = s5013infoDpsPerAntE.objects.create(**s5013_infodpsperante_dados)
                    
                    if 'dpsPerAntE' in dir(infoDpsPerAntE):
                    
                        for dpsPerAntE in infoDpsPerAntE.dpsPerAntE:
                    
                            s5013_dpsperante_dados = {}
                            s5013_dpsperante_dados['s5013_infodpsperante_id'] = s5013_infodpsperante.id
                            
                            try:
                                s5013_dpsperante_dados['tpdpse'] = dpsPerAntE.tpDpsE.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5013_dpsperante_dados['vrfgtse'] = dpsPerAntE.vrFGTSE.cdata
                            except AttributeError: 
                                pass
                    
                            s5013_dpsperante = s5013dpsPerAntE.objects.create(**s5013_dpsperante_dados)    
    s5013_evtfgts_dados['evento'] = 's5013'
    s5013_evtfgts_dados['id'] = s5013_evtfgts.id
    s5013_evtfgts_dados['identidade_evento'] = doc.eSocial.evtFGTS['Id']
    s5013_evtfgts_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s5013_evtfgts_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(s5013_evtfgts.id)
    return s5013_evtfgts_dados