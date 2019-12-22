# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s5003.models import *
from emensageriapro.functions import read_from_xml



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
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s5003_evtbasesfgts_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s5003evtBasesFGTS.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s5003_evtbasesfgts_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s5003_evtbasesfgts_dados = {}
    s5003_evtbasesfgts_dados['status'] = status
    s5003_evtbasesfgts_dados['arquivo_original'] = 1
    if arquivo:
        s5003_evtbasesfgts_dados['arquivo'] = arquivo.arquivo
    s5003_evtbasesfgts_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5003_evtbasesfgts_dados['identidade'] = doc.eSocial.evtBasesFGTS['Id']
    evtBasesFGTS = doc.eSocial.evtBasesFGTS

    try:
        s5003_evtbasesfgts_dados['nrrecarqbase'] = read_from_xml(evtBasesFGTS.ideEvento.nrRecArqBase.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5003_evtbasesfgts_dados['perapur'] = read_from_xml(evtBasesFGTS.ideEvento.perApur.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5003_evtbasesfgts_dados['tpinsc'] = read_from_xml(evtBasesFGTS.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s5003_evtbasesfgts_dados['nrinsc'] = read_from_xml(evtBasesFGTS.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5003_evtbasesfgts_dados['cpftrab'] = read_from_xml(evtBasesFGTS.ideTrabalhador.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5003_evtbasesfgts_dados['nistrab'] = read_from_xml(evtBasesFGTS.ideTrabalhador.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5003_evtbasesfgts_dados['dtvenc'] = read_from_xml(evtBasesFGTS.infoFGTS.dtVenc.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    s5003_evtbasesfgts = s5003evtBasesFGTS.objects.create(**s5003_evtbasesfgts_dados)

    if 'infoFGTS' in dir(evtBasesFGTS) and 'ideEstabLot' in dir(evtBasesFGTS.infoFGTS):

        for ideEstabLot in evtBasesFGTS.infoFGTS.ideEstabLot:

            s5003_ideestablot_dados = {}
            s5003_ideestablot_dados['s5003_evtbasesfgts_id'] = s5003_evtbasesfgts.id

            try:
                s5003_ideestablot_dados['tpinsc'] = read_from_xml(ideEstabLot.tpInsc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s5003_ideestablot_dados['nrinsc'] = read_from_xml(ideEstabLot.nrInsc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s5003_ideestablot_dados['codlotacao'] = read_from_xml(ideEstabLot.codLotacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s5003_ideestablot = s5003ideEstabLot.objects.create(**s5003_ideestablot_dados)

            if 'infoTrabFGTS' in dir(ideEstabLot):

                for infoTrabFGTS in ideEstabLot.infoTrabFGTS:

                    s5003_infotrabfgts_dados = {}
                    s5003_infotrabfgts_dados['s5003_ideestablot_id'] = s5003_ideestablot.id

                    try:
                        s5003_infotrabfgts_dados['matricula'] = read_from_xml(infoTrabFGTS.matricula.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s5003_infotrabfgts_dados['codcateg'] = read_from_xml(infoTrabFGTS.codCateg.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s5003_infotrabfgts_dados['dtadm'] = read_from_xml(infoTrabFGTS.dtAdm.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s5003_infotrabfgts_dados['dtdeslig'] = read_from_xml(infoTrabFGTS.dtDeslig.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s5003_infotrabfgts_dados['dtinicio'] = read_from_xml(infoTrabFGTS.dtInicio.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s5003_infotrabfgts_dados['mtvdeslig'] = read_from_xml(infoTrabFGTS.mtvDeslig.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s5003_infotrabfgts_dados['dtterm'] = read_from_xml(infoTrabFGTS.dtTerm.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s5003_infotrabfgts_dados['mtvdesligtsv'] = read_from_xml(infoTrabFGTS.mtvDesligTSV.cdata, 'esocial', 'C', None)
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
                                        s5003_baseperapur_dados['tpvalor'] = read_from_xml(basePerApur.tpValor.cdata, 'esocial', 'N', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s5003_baseperapur_dados['remfgts'] = read_from_xml(basePerApur.remFGTS.cdata, 'esocial', 'N', 2)
                                    except AttributeError:
                                        pass
        
                                    s5003_baseperapur = s5003basePerApur.objects.create(**s5003_baseperapur_dados)
        
                            if 'infoBasePerAntE' in dir(infoBaseFGTS):
        
                                for infoBasePerAntE in infoBaseFGTS.infoBasePerAntE:
        
                                    s5003_infobaseperante_dados = {}
                                    s5003_infobaseperante_dados['s5003_infobasefgts_id'] = s5003_infobasefgts.id
                
                                    try:
                                        s5003_infobaseperante_dados['perref'] = read_from_xml(infoBasePerAntE.perRef.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
        
                                    s5003_infobaseperante = s5003infoBasePerAntE.objects.create(**s5003_infobaseperante_dados)
                
                                    if 'basePerAntE' in dir(infoBasePerAntE):
                
                                        for basePerAntE in infoBasePerAntE.basePerAntE:
                
                                            s5003_baseperante_dados = {}
                                            s5003_baseperante_dados['s5003_infobaseperante_id'] = s5003_infobaseperante.id
                        
                                            try:
                                                s5003_baseperante_dados['tpvalore'] = read_from_xml(basePerAntE.tpValorE.cdata, 'esocial', 'N', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s5003_baseperante_dados['remfgtse'] = read_from_xml(basePerAntE.remFGTSE.cdata, 'esocial', 'N', 2)
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
                        s5003_infotrabdps_dados['matricula'] = read_from_xml(infoTrabDps.matricula.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s5003_infotrabdps_dados['codcateg'] = read_from_xml(infoTrabDps.codCateg.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s5003_infotrabdps = s5003infoTrabDps.objects.create(**s5003_infotrabdps_dados)

                    if 'dpsPerApur' in dir(infoTrabDps):

                        for dpsPerApur in infoTrabDps.dpsPerApur:

                            s5003_dpsperapur_dados = {}
                            s5003_dpsperapur_dados['s5003_infotrabdps_id'] = s5003_infotrabdps.id
        
                            try:
                                s5003_dpsperapur_dados['tpdps'] = read_from_xml(dpsPerApur.tpDps.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s5003_dpsperapur_dados['dpsfgts'] = read_from_xml(dpsPerApur.dpsFGTS.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s5003_dpsperapur = s5003dpsPerApur.objects.create(**s5003_dpsperapur_dados)

                    if 'infoDpsPerAntE' in dir(infoTrabDps):

                        for infoDpsPerAntE in infoTrabDps.infoDpsPerAntE:

                            s5003_infodpsperante_dados = {}
                            s5003_infodpsperante_dados['s5003_infotrabdps_id'] = s5003_infotrabdps.id
        
                            try:
                                s5003_infodpsperante_dados['perref'] = read_from_xml(infoDpsPerAntE.perRef.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s5003_infodpsperante = s5003infoDpsPerAntE.objects.create(**s5003_infodpsperante_dados)
        
                            if 'dpsPerAntE' in dir(infoDpsPerAntE):
        
                                for dpsPerAntE in infoDpsPerAntE.dpsPerAntE:
        
                                    s5003_dpsperante_dados = {}
                                    s5003_dpsperante_dados['s5003_infodpsperante_id'] = s5003_infodpsperante.id
                
                                    try:
                                        s5003_dpsperante_dados['tpdpse'] = read_from_xml(dpsPerAntE.tpDpsE.cdata, 'esocial', 'N', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s5003_dpsperante_dados['dpsfgtse'] = read_from_xml(dpsPerAntE.dpsFGTSE.cdata, 'esocial', 'N', 2)
                                    except AttributeError:
                                        pass
        
                                    s5003_dpsperante = s5003dpsPerAntE.objects.create(**s5003_dpsperante_dados)
    s5003_evtbasesfgts_dados['evento'] = 's5003'
    s5003_evtbasesfgts_dados['id'] = s5003_evtbasesfgts.id
    s5003_evtbasesfgts_dados['identidade_evento'] = doc.eSocial.evtBasesFGTS['Id']

    from emensageriapro.esocial.views.s5003_evtbasesfgts_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s5003_evtbasesfgts.id)

    return s5003_evtbasesfgts_dados