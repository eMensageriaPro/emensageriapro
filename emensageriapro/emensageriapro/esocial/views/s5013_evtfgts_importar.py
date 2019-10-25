#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s5013.models import *
from emensageriapro.functions import read_from_xml



def read_s5013_evtfgts_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s5013_evtfgts_obj(request, doc, status, validar)
    return dados



def read_s5013_evtfgts(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s5013_evtfgts_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s5013evtFGTS.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s5013_evtfgts_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s5013_evtfgts_dados = {}
    s5013_evtfgts_dados['status'] = status
    s5013_evtfgts_dados['arquivo_original'] = 1
    if arquivo:
        s5013_evtfgts_dados['arquivo'] = arquivo.arquivo
    s5013_evtfgts_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5013_evtfgts_dados['identidade'] = doc.eSocial.evtFGTS['Id']
    evtFGTS = doc.eSocial.evtFGTS

    try:
        s5013_evtfgts_dados['perapur'] = read_from_xml(evtFGTS.ideEvento.perApur.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5013_evtfgts_dados['tpinsc'] = read_from_xml(evtFGTS.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s5013_evtfgts_dados['nrinsc'] = read_from_xml(evtFGTS.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5013_evtfgts_dados['nrrecarqbase'] = read_from_xml(evtFGTS.infoFGTS.nrRecArqBase.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5013_evtfgts_dados['indexistinfo'] = read_from_xml(evtFGTS.infoFGTS.indExistInfo.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    s5013_evtfgts = s5013evtFGTS.objects.create(**s5013_evtfgts_dados)

    if 'infoFGTS' in dir(evtFGTS) and 'infoBaseFGTS' in dir(evtFGTS.infoFGTS):

        for infoBaseFGTS in evtFGTS.infoFGTS.infoBaseFGTS:

            s5013_infobasefgts_dados = {}
            s5013_infobasefgts_dados['s5013_evtfgts_id'] = s5013_evtfgts.id

            s5013_infobasefgts = s5013infoBaseFGTS.objects.create(**s5013_infobasefgts_dados)

            if 'basePerApur' in dir(infoBaseFGTS):

                for basePerApur in infoBaseFGTS.basePerApur:

                    s5013_baseperapur_dados = {}
                    s5013_baseperapur_dados['s5013_infobasefgts_id'] = s5013_infobasefgts.id

                    try:
                        s5013_baseperapur_dados['tpvalor'] = read_from_xml(basePerApur.tpValor.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s5013_baseperapur_dados['basefgts'] = read_from_xml(basePerApur.baseFGTS.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    s5013_baseperapur = s5013basePerApur.objects.create(**s5013_baseperapur_dados)

            if 'infoBasePerAntE' in dir(infoBaseFGTS):

                for infoBasePerAntE in infoBaseFGTS.infoBasePerAntE:

                    s5013_infobaseperante_dados = {}
                    s5013_infobaseperante_dados['s5013_infobasefgts_id'] = s5013_infobasefgts.id

                    try:
                        s5013_infobaseperante_dados['perref'] = read_from_xml(infoBasePerAntE.perRef.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s5013_infobaseperante = s5013infoBasePerAntE.objects.create(**s5013_infobaseperante_dados)

                    if 'basePerAntE' in dir(infoBasePerAntE):

                        for basePerAntE in infoBasePerAntE.basePerAntE:

                            s5013_baseperante_dados = {}
                            s5013_baseperante_dados['s5013_infobaseperante_id'] = s5013_infobaseperante.id
        
                            try:
                                s5013_baseperante_dados['tpvalore'] = read_from_xml(basePerAntE.tpValorE.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s5013_baseperante_dados['basefgtse'] = read_from_xml(basePerAntE.baseFGTSE.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s5013_baseperante = s5013basePerAntE.objects.create(**s5013_baseperante_dados)

    if 'infoFGTS' in dir(evtFGTS) and 'infoDpsFGTS' in dir(evtFGTS.infoFGTS):

        for infoDpsFGTS in evtFGTS.infoFGTS.infoDpsFGTS:

            s5013_infodpsfgts_dados = {}
            s5013_infodpsfgts_dados['s5013_evtfgts_id'] = s5013_evtfgts.id

            s5013_infodpsfgts = s5013infoDpsFGTS.objects.create(**s5013_infodpsfgts_dados)

            if 'dpsPerApur' in dir(infoDpsFGTS):

                for dpsPerApur in infoDpsFGTS.dpsPerApur:

                    s5013_dpsperapur_dados = {}
                    s5013_dpsperapur_dados['s5013_infodpsfgts_id'] = s5013_infodpsfgts.id

                    try:
                        s5013_dpsperapur_dados['tpdps'] = read_from_xml(dpsPerApur.tpDps.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s5013_dpsperapur_dados['vrfgts'] = read_from_xml(dpsPerApur.vrFGTS.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    s5013_dpsperapur = s5013dpsPerApur.objects.create(**s5013_dpsperapur_dados)

            if 'infoDpsPerAntE' in dir(infoDpsFGTS):

                for infoDpsPerAntE in infoDpsFGTS.infoDpsPerAntE:

                    s5013_infodpsperante_dados = {}
                    s5013_infodpsperante_dados['s5013_infodpsfgts_id'] = s5013_infodpsfgts.id

                    try:
                        s5013_infodpsperante_dados['perref'] = read_from_xml(infoDpsPerAntE.perRef.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s5013_infodpsperante = s5013infoDpsPerAntE.objects.create(**s5013_infodpsperante_dados)

                    if 'dpsPerAntE' in dir(infoDpsPerAntE):

                        for dpsPerAntE in infoDpsPerAntE.dpsPerAntE:

                            s5013_dpsperante_dados = {}
                            s5013_dpsperante_dados['s5013_infodpsperante_id'] = s5013_infodpsperante.id
        
                            try:
                                s5013_dpsperante_dados['tpdpse'] = read_from_xml(dpsPerAntE.tpDpsE.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s5013_dpsperante_dados['vrfgtse'] = read_from_xml(dpsPerAntE.vrFGTSE.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s5013_dpsperante = s5013dpsPerAntE.objects.create(**s5013_dpsperante_dados)
    s5013_evtfgts_dados['evento'] = 's5013'
    s5013_evtfgts_dados['id'] = s5013_evtfgts.id
    s5013_evtfgts_dados['identidade_evento'] = doc.eSocial.evtFGTS['Id']

    from emensageriapro.esocial.views.s5013_evtfgts_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s5013_evtfgts.id)

    return s5013_evtfgts_dados