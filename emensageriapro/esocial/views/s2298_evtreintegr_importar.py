#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2298.models import *



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

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_s2298_evtreintegr_obj(request, doc, status, validar, arquivo)
    novo_arquivo = arquivo.replace('/aguardando/', '/processado/')
    s2298evtReintegr.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s2298_evtreintegr_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2298_evtreintegr_dados = {}
    s2298_evtreintegr_dados['status'] = status
    s2298_evtreintegr_dados['arquivo_original'] = 1
    if arquivo:
        s2298_evtreintegr_dados['arquivo'] = arquivo
    s2298_evtreintegr_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2298_evtreintegr_dados['identidade'] = doc.eSocial.evtReintegr['Id']
    evtReintegr = doc.eSocial.evtReintegr

    try:
        s2298_evtreintegr_dados['indretif'] = evtReintegr.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['nrrecibo'] = evtReintegr.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['tpamb'] = evtReintegr.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['procemi'] = evtReintegr.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['verproc'] = evtReintegr.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['tpinsc'] = evtReintegr.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['nrinsc'] = evtReintegr.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['cpftrab'] = evtReintegr.ideVinculo.cpfTrab.cdata
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['nistrab'] = evtReintegr.ideVinculo.nisTrab.cdata
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['matricula'] = evtReintegr.ideVinculo.matricula.cdata
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['tpreint'] = evtReintegr.infoReintegr.tpReint.cdata
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['nrprocjud'] = evtReintegr.infoReintegr.nrProcJud.cdata
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['nrleianistia'] = evtReintegr.infoReintegr.nrLeiAnistia.cdata
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['dtefetretorno'] = evtReintegr.infoReintegr.dtEfetRetorno.cdata
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['dtefeito'] = evtReintegr.infoReintegr.dtEfeito.cdata
    except AttributeError:
        pass

    try:
        s2298_evtreintegr_dados['indpagtojuizo'] = evtReintegr.infoReintegr.indPagtoJuizo.cdata
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