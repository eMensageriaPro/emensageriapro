#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s5003.models import *



def read_s5003_evtbasesfgts_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s5003_evtbasesfgts_obj(request, doc, status, validar)
    return dados



def read_s5003_evtbasesfgts(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s5003_evtbasesfgts_obj(request, doc, status, validar)

    s5003evtBasesFGTS.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s5003_evtbasesfgts_obj(request, doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s5003_evtbasesfgts_dados = {}
    s5003_evtbasesfgts_dados['status'] = status
    s5003_evtbasesfgts_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5003_evtbasesfgts_dados['identidade'] = doc.eSocial.evtBasesFGTS['Id']
    evtBasesFGTS = doc.eSocial.evtBasesFGTS
    
    try:
        s5003_evtbasesfgts_dados['nrrecarqbase'] = evtBasesFGTS.ideEvento.nrRecArqBase.cdata
    except AttributeError: 
        pass
    
    try:
        s5003_evtbasesfgts_dados['perapur'] = evtBasesFGTS.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        s5003_evtbasesfgts_dados['tpinsc'] = evtBasesFGTS.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s5003_evtbasesfgts_dados['nrinsc'] = evtBasesFGTS.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s5003_evtbasesfgts_dados['cpftrab'] = evtBasesFGTS.ideTrabalhador.cpfTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s5003_evtbasesfgts_dados['nistrab'] = evtBasesFGTS.ideTrabalhador.nisTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s5003_evtbasesfgts_dados['dtvenc'] = evtBasesFGTS.infoFGTS.dtVenc.cdata
    except AttributeError: 
        pass
        
    s5003_evtbasesfgts = s5003evtBasesFGTS.objects.create(**s5003_evtbasesfgts_dados)
    
    if 'infoFGTS' in dir(evtBasesFGTS) and 'ideEstabLot' in dir(evtBasesFGTS.infoFGTS):
    
        for ideEstabLot in evtBasesFGTS.infoFGTS.ideEstabLot:
    
            s5003_ideestablot_dados = {}
            s5003_ideestablot_dados['s5003_evtbasesfgts_id'] = s5003_evtbasesfgts.id
            
            try:
                s5003_ideestablot_dados['tpinsc'] = ideEstabLot.tpInsc.cdata
            except AttributeError: 
                pass
            
            try:
                s5003_ideestablot_dados['nrinsc'] = ideEstabLot.nrInsc.cdata
            except AttributeError: 
                pass
            
            try:
                s5003_ideestablot_dados['codlotacao'] = ideEstabLot.codLotacao.cdata
            except AttributeError: 
                pass
    
            s5003_ideestablot = s5003ideEstabLot.objects.create(**s5003_ideestablot_dados)
            
            if 'infoTrabFGTS' in dir(ideEstabLot):
            
                for infoTrabFGTS in ideEstabLot.infoTrabFGTS:
            
                    s5003_infotrabfgts_dados = {}
                    s5003_infotrabfgts_dados['s5003_ideestablot_id'] = s5003_ideestablot.id
                    
                    try:
                        s5003_infotrabfgts_dados['matricula'] = infoTrabFGTS.matricula.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5003_infotrabfgts_dados['codcateg'] = infoTrabFGTS.codCateg.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5003_infotrabfgts_dados['dtadm'] = infoTrabFGTS.dtAdm.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5003_infotrabfgts_dados['dtdeslig'] = infoTrabFGTS.dtDeslig.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5003_infotrabfgts_dados['dtinicio'] = infoTrabFGTS.dtInicio.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5003_infotrabfgts_dados['mtvdeslig'] = infoTrabFGTS.mtvDeslig.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5003_infotrabfgts_dados['dtterm'] = infoTrabFGTS.dtTerm.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5003_infotrabfgts_dados['mtvdesligtsv'] = infoTrabFGTS.mtvDesligTSV.cdata
                    except AttributeError: 
                        pass
            
                    s5003_infotrabfgts = s5003infoTrabFGTS.objects.create(**s5003_infotrabfgts_dados)
                    
                    if 'infoBaseFGTS' in dir(infoTrabFGTS):
                    
                        for infoBaseFGTS in infoTrabFGTS.infoBaseFGTS:
                    
                            s5003_infobasefgts_dados = {}
                            s5003_infobasefgts_dados['s5003_infotrabfgts_id'] = s5003_infotrabfgts.id
                    
                            s5003_infobasefgts = s5003infoBaseFGTS.objects.create(**s5003_infobasefgts_dados)
                            
                            if 'basePerApur' in dir(infoBaseFGTS):
                            
                                for basePerApur in infoBaseFGTS.basePerApur:
                            
                                    s5003_baseperapur_dados = {}
                                    s5003_baseperapur_dados['s5003_infobasefgts_id'] = s5003_infobasefgts.id
                                    
                                    try:
                                        s5003_baseperapur_dados['tpvalor'] = basePerApur.tpValor.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        s5003_baseperapur_dados['remfgts'] = basePerApur.remFGTS.cdata
                                    except AttributeError: 
                                        pass
                            
                                    s5003_baseperapur = s5003basePerApur.objects.create(**s5003_baseperapur_dados)
                            
                            if 'infoBasePerAntE' in dir(infoBaseFGTS):
                            
                                for infoBasePerAntE in infoBaseFGTS.infoBasePerAntE:
                            
                                    s5003_infobaseperante_dados = {}
                                    s5003_infobaseperante_dados['s5003_infobasefgts_id'] = s5003_infobasefgts.id
                                    
                                    try:
                                        s5003_infobaseperante_dados['perref'] = infoBasePerAntE.perRef.cdata
                                    except AttributeError: 
                                        pass
                            
                                    s5003_infobaseperante = s5003infoBasePerAntE.objects.create(**s5003_infobaseperante_dados)
                                    
                                    if 'basePerAntE' in dir(infoBasePerAntE):
                                    
                                        for basePerAntE in infoBasePerAntE.basePerAntE:
                                    
                                            s5003_baseperante_dados = {}
                                            s5003_baseperante_dados['s5003_infobaseperante_id'] = s5003_infobaseperante.id
                                            
                                            try:
                                                s5003_baseperante_dados['tpvalore'] = basePerAntE.tpValorE.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                s5003_baseperante_dados['remfgtse'] = basePerAntE.remFGTSE.cdata
                                            except AttributeError: 
                                                pass
                                    
                                            s5003_baseperante = s5003basePerAntE.objects.create(**s5003_baseperante_dados)
    
    if 'infoFGTS' in dir(evtBasesFGTS) and 'infoDpsFGTS' in dir(evtBasesFGTS.infoFGTS):
    
        for infoDpsFGTS in evtBasesFGTS.infoFGTS.infoDpsFGTS:
    
            s5003_infodpsfgts_dados = {}
            s5003_infodpsfgts_dados['s5003_evtbasesfgts_id'] = s5003_evtbasesfgts.id
    
            s5003_infodpsfgts = s5003infoDpsFGTS.objects.create(**s5003_infodpsfgts_dados)
            
            if 'infoTrabDps' in dir(infoDpsFGTS):
            
                for infoTrabDps in infoDpsFGTS.infoTrabDps:
            
                    s5003_infotrabdps_dados = {}
                    s5003_infotrabdps_dados['s5003_infodpsfgts_id'] = s5003_infodpsfgts.id
                    
                    try:
                        s5003_infotrabdps_dados['matricula'] = infoTrabDps.matricula.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5003_infotrabdps_dados['codcateg'] = infoTrabDps.codCateg.cdata
                    except AttributeError: 
                        pass
            
                    s5003_infotrabdps = s5003infoTrabDps.objects.create(**s5003_infotrabdps_dados)
                    
                    if 'dpsPerApur' in dir(infoTrabDps):
                    
                        for dpsPerApur in infoTrabDps.dpsPerApur:
                    
                            s5003_dpsperapur_dados = {}
                            s5003_dpsperapur_dados['s5003_infotrabdps_id'] = s5003_infotrabdps.id
                            
                            try:
                                s5003_dpsperapur_dados['tpdps'] = dpsPerApur.tpDps.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5003_dpsperapur_dados['dpsfgts'] = dpsPerApur.dpsFGTS.cdata
                            except AttributeError: 
                                pass
                    
                            s5003_dpsperapur = s5003dpsPerApur.objects.create(**s5003_dpsperapur_dados)
                    
                    if 'infoDpsPerAntE' in dir(infoTrabDps):
                    
                        for infoDpsPerAntE in infoTrabDps.infoDpsPerAntE:
                    
                            s5003_infodpsperante_dados = {}
                            s5003_infodpsperante_dados['s5003_infotrabdps_id'] = s5003_infotrabdps.id
                            
                            try:
                                s5003_infodpsperante_dados['perref'] = infoDpsPerAntE.perRef.cdata
                            except AttributeError: 
                                pass
                    
                            s5003_infodpsperante = s5003infoDpsPerAntE.objects.create(**s5003_infodpsperante_dados)
                            
                            if 'dpsPerAntE' in dir(infoDpsPerAntE):
                            
                                for dpsPerAntE in infoDpsPerAntE.dpsPerAntE:
                            
                                    s5003_dpsperante_dados = {}
                                    s5003_dpsperante_dados['s5003_infodpsperante_id'] = s5003_infodpsperante.id
                                    
                                    try:
                                        s5003_dpsperante_dados['tpdpse'] = dpsPerAntE.tpDpsE.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        s5003_dpsperante_dados['dpsfgtse'] = dpsPerAntE.dpsFGTSE.cdata
                                    except AttributeError: 
                                        pass
                            
                                    s5003_dpsperante = s5003dpsPerAntE.objects.create(**s5003_dpsperante_dados)    
    s5003_evtbasesfgts_dados['evento'] = 's5003'
    s5003_evtbasesfgts_dados['id'] = s5003_evtbasesfgts.id
    s5003_evtbasesfgts_dados['identidade_evento'] = doc.eSocial.evtBasesFGTS['Id']
    s5003_evtbasesfgts_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s5003_evtbasesfgts_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, s5003_evtbasesfgts.id)
    
    return s5003_evtbasesfgts_dados