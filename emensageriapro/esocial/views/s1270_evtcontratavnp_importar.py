#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1270.models import *



def read_s1270_evtcontratavnp_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1270_evtcontratavnp_obj(request, doc, status, validar)
    return dados



def read_s1270_evtcontratavnp(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_s1270_evtcontratavnp_obj(request, doc, status, validar, arquivo)
    novo_arquivo = arquivo.replace('/aguardando/', '/processado/')
    s1270evtContratAvNP.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s1270_evtcontratavnp_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1270_evtcontratavnp_dados = {}
    s1270_evtcontratavnp_dados['status'] = status
    s1270_evtcontratavnp_dados['arquivo_original'] = 1
    if arquivo:
        s1270_evtcontratavnp_dados['arquivo'] = arquivo
    s1270_evtcontratavnp_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1270_evtcontratavnp_dados['identidade'] = doc.eSocial.evtContratAvNP['Id']
    evtContratAvNP = doc.eSocial.evtContratAvNP

    try:
        s1270_evtcontratavnp_dados['indretif'] = evtContratAvNP.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        s1270_evtcontratavnp_dados['nrrecibo'] = evtContratAvNP.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        s1270_evtcontratavnp_dados['indapuracao'] = evtContratAvNP.ideEvento.indApuracao.cdata
    except AttributeError:
        pass

    try:
        s1270_evtcontratavnp_dados['perapur'] = evtContratAvNP.ideEvento.perApur.cdata
    except AttributeError:
        pass

    try:
        s1270_evtcontratavnp_dados['tpamb'] = evtContratAvNP.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s1270_evtcontratavnp_dados['procemi'] = evtContratAvNP.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s1270_evtcontratavnp_dados['verproc'] = evtContratAvNP.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s1270_evtcontratavnp_dados['tpinsc'] = evtContratAvNP.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s1270_evtcontratavnp_dados['nrinsc'] = evtContratAvNP.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    s1270_evtcontratavnp = s1270evtContratAvNP.objects.create(**s1270_evtcontratavnp_dados)

    if 'remunAvNP' in dir(evtContratAvNP):

        for remunAvNP in evtContratAvNP.remunAvNP:

            s1270_remunavnp_dados = {}
            s1270_remunavnp_dados['s1270_evtcontratavnp_id'] = s1270_evtcontratavnp.id

            try:
                s1270_remunavnp_dados['tpinsc'] = remunAvNP.tpInsc.cdata
            except AttributeError:
                pass

            try:
                s1270_remunavnp_dados['nrinsc'] = remunAvNP.nrInsc.cdata
            except AttributeError:
                pass

            try:
                s1270_remunavnp_dados['codlotacao'] = remunAvNP.codLotacao.cdata
            except AttributeError:
                pass

            try:
                s1270_remunavnp_dados['vrbccp00'] = remunAvNP.vrBcCp00.cdata
            except AttributeError:
                pass

            try:
                s1270_remunavnp_dados['vrbccp15'] = remunAvNP.vrBcCp15.cdata
            except AttributeError:
                pass

            try:
                s1270_remunavnp_dados['vrbccp20'] = remunAvNP.vrBcCp20.cdata
            except AttributeError:
                pass

            try:
                s1270_remunavnp_dados['vrbccp25'] = remunAvNP.vrBcCp25.cdata
            except AttributeError:
                pass

            try:
                s1270_remunavnp_dados['vrbccp13'] = remunAvNP.vrBcCp13.cdata
            except AttributeError:
                pass

            try:
                s1270_remunavnp_dados['vrbcfgts'] = remunAvNP.vrBcFgts.cdata
            except AttributeError:
                pass

            try:
                s1270_remunavnp_dados['vrdesccp'] = remunAvNP.vrDescCP.cdata
            except AttributeError:
                pass

            s1270_remunavnp = s1270remunAvNP.objects.create(**s1270_remunavnp_dados)
    s1270_evtcontratavnp_dados['evento'] = 's1270'
    s1270_evtcontratavnp_dados['id'] = s1270_evtcontratavnp.id
    s1270_evtcontratavnp_dados['identidade_evento'] = doc.eSocial.evtContratAvNP['Id']

    from emensageriapro.esocial.views.s1270_evtcontratavnp_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1270_evtcontratavnp.id)

    return s1270_evtcontratavnp_dados