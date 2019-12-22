# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2416.models import *
from emensageriapro.functions import read_from_xml



def read_s2416_evtcdbenalt_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2416_evtcdbenalt_obj(request, doc, status, validar)
    return dados



def read_s2416_evtcdbenalt(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2416_evtcdbenalt_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2416evtCdBenAlt.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2416_evtcdbenalt_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2416_evtcdbenalt_dados = {}
    s2416_evtcdbenalt_dados['status'] = status
    s2416_evtcdbenalt_dados['arquivo_original'] = 1
    if arquivo:
        s2416_evtcdbenalt_dados['arquivo'] = arquivo.arquivo
    s2416_evtcdbenalt_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2416_evtcdbenalt_dados['identidade'] = doc.eSocial.evtCdBenAlt['Id']
    evtCdBenAlt = doc.eSocial.evtCdBenAlt

    try:
        s2416_evtcdbenalt_dados['indretif'] = read_from_xml(evtCdBenAlt.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2416_evtcdbenalt_dados['nrrecibo'] = read_from_xml(evtCdBenAlt.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2416_evtcdbenalt_dados['tpamb'] = read_from_xml(evtCdBenAlt.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2416_evtcdbenalt_dados['procemi'] = read_from_xml(evtCdBenAlt.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2416_evtcdbenalt_dados['verproc'] = read_from_xml(evtCdBenAlt.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2416_evtcdbenalt_dados['tpinsc'] = read_from_xml(evtCdBenAlt.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2416_evtcdbenalt_dados['nrinsc'] = read_from_xml(evtCdBenAlt.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2416_evtcdbenalt_dados['cpfbenef'] = read_from_xml(evtCdBenAlt.ideBeneficio.cpfBenef.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2416_evtcdbenalt_dados['nrbeneficio'] = read_from_xml(evtCdBenAlt.ideBeneficio.nrBeneficio.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2416_evtcdbenalt_dados['dtaltbeneficio'] = read_from_xml(evtCdBenAlt.infoBenAlteracao.dtAltBeneficio.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2416_evtcdbenalt_dados['tpbeneficio'] = read_from_xml(evtCdBenAlt.infoBenAlteracao.dadosBeneficio.tpBeneficio.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2416_evtcdbenalt_dados['tpplanrp'] = read_from_xml(evtCdBenAlt.infoBenAlteracao.dadosBeneficio.tpPlanRP.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2416_evtcdbenalt_dados['dsc'] = read_from_xml(evtCdBenAlt.infoBenAlteracao.dadosBeneficio.dsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2416_evtcdbenalt_dados['inddecjud'] = read_from_xml(evtCdBenAlt.infoBenAlteracao.dadosBeneficio.indDecJud.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2416_evtcdbenalt_dados['indhomologtc'] = read_from_xml(evtCdBenAlt.infoBenAlteracao.dadosBeneficio.indHomologTC.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2416_evtcdbenalt_dados['indsuspensao'] = read_from_xml(evtCdBenAlt.infoBenAlteracao.dadosBeneficio.indSuspensao.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s2416_evtcdbenalt = s2416evtCdBenAlt.objects.create(**s2416_evtcdbenalt_dados)

    if 'infoBenAlteracao' in dir(evtCdBenAlt) and 'dadosBeneficio' in dir(evtCdBenAlt.infoBenAlteracao) and 'infoPenMorte' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio):

        for infoPenMorte in evtCdBenAlt.infoBenAlteracao.dadosBeneficio.infoPenMorte:

            s2416_infopenmorte_dados = {}
            s2416_infopenmorte_dados['s2416_evtcdbenalt_id'] = s2416_evtcdbenalt.id

            try:
                s2416_infopenmorte_dados['tppenmorte'] = read_from_xml(infoPenMorte.tpPenMorte.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s2416_infopenmorte = s2416infoPenMorte.objects.create(**s2416_infopenmorte_dados)

    if 'infoBenAlteracao' in dir(evtCdBenAlt) and 'dadosBeneficio' in dir(evtCdBenAlt.infoBenAlteracao) and 'homologTC' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio):

        for homologTC in evtCdBenAlt.infoBenAlteracao.dadosBeneficio.homologTC:

            s2416_homologtc_dados = {}
            s2416_homologtc_dados['s2416_evtcdbenalt_id'] = s2416_evtcdbenalt.id

            try:
                s2416_homologtc_dados['nratolegal'] = read_from_xml(homologTC.nrAtoLegal.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2416_homologtc = s2416homologTC.objects.create(**s2416_homologtc_dados)

    if 'infoBenAlteracao' in dir(evtCdBenAlt) and 'dadosBeneficio' in dir(evtCdBenAlt.infoBenAlteracao) and 'suspensao' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio):

        for suspensao in evtCdBenAlt.infoBenAlteracao.dadosBeneficio.suspensao:

            s2416_suspensao_dados = {}
            s2416_suspensao_dados['s2416_evtcdbenalt_id'] = s2416_evtcdbenalt.id

            try:
                s2416_suspensao_dados['mtvsuspensao'] = read_from_xml(suspensao.mtvSuspensao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2416_suspensao_dados['dscsuspensao'] = read_from_xml(suspensao.dscSuspensao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2416_suspensao = s2416suspensao.objects.create(**s2416_suspensao_dados)
    s2416_evtcdbenalt_dados['evento'] = 's2416'
    s2416_evtcdbenalt_dados['id'] = s2416_evtcdbenalt.id
    s2416_evtcdbenalt_dados['identidade_evento'] = doc.eSocial.evtCdBenAlt['Id']

    from emensageriapro.esocial.views.s2416_evtcdbenalt_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2416_evtcdbenalt.id)

    return s2416_evtcdbenalt_dados