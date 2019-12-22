# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2298.models import *
from emensageriapro.functions import read_from_xml



def read_s2298_evtreintegr_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2298_evtreintegr_obj(request, doc, status, validar)
    return dados



def read_s2298_evtreintegr(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2298_evtreintegr_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2298evtReintegr.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2298_evtreintegr_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2298_evtreintegr_dados = {}
    s2298_evtreintegr_dados['status'] = status
    s2298_evtreintegr_dados['arquivo_original'] = 1
    if arquivo:
        s2298_evtreintegr_dados['arquivo'] = arquivo.arquivo
    s2298_evtreintegr_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2298_evtreintegr_dados['identidade'] = doc.eSocial.evtReintegr['Id']
    evtReintegr = doc.eSocial.evtReintegr

    try:
        s2298_evtreintegr_dados['indretif'] = read_from_xml(evtReintegr.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['nrrecibo'] = read_from_xml(evtReintegr.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['tpamb'] = read_from_xml(evtReintegr.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['procemi'] = read_from_xml(evtReintegr.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['verproc'] = read_from_xml(evtReintegr.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['tpinsc'] = read_from_xml(evtReintegr.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['nrinsc'] = read_from_xml(evtReintegr.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['cpftrab'] = read_from_xml(evtReintegr.ideVinculo.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['nistrab'] = read_from_xml(evtReintegr.ideVinculo.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['matricula'] = read_from_xml(evtReintegr.ideVinculo.matricula.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['tpreint'] = read_from_xml(evtReintegr.infoReintegr.tpReint.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['nrprocjud'] = read_from_xml(evtReintegr.infoReintegr.nrProcJud.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['nrleianistia'] = read_from_xml(evtReintegr.infoReintegr.nrLeiAnistia.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['dtefetretorno'] = read_from_xml(evtReintegr.infoReintegr.dtEfetRetorno.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['dtefeito'] = read_from_xml(evtReintegr.infoReintegr.dtEfeito.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['indpagtojuizo'] = read_from_xml(evtReintegr.infoReintegr.indPagtoJuizo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s2298_evtreintegr = s2298evtReintegr.objects.create(**s2298_evtreintegr_dados)
    s2298_evtreintegr_dados['evento'] = 's2298'
    s2298_evtreintegr_dados['id'] = s2298_evtreintegr.id
    s2298_evtreintegr_dados['identidade_evento'] = doc.eSocial.evtReintegr['Id']

    from emensageriapro.esocial.views.s2298_evtreintegr_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2298_evtreintegr.id)

    return s2298_evtreintegr_dados