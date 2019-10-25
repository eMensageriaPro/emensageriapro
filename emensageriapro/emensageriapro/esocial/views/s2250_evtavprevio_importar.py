#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2250.models import *
from emensageriapro.functions import read_from_xml



def read_s2250_evtavprevio_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2250_evtavprevio_obj(request, doc, status, validar)
    return dados



def read_s2250_evtavprevio(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2250_evtavprevio_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2250evtAvPrevio.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2250_evtavprevio_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2250_evtavprevio_dados = {}
    s2250_evtavprevio_dados['status'] = status
    s2250_evtavprevio_dados['arquivo_original'] = 1
    if arquivo:
        s2250_evtavprevio_dados['arquivo'] = arquivo.arquivo
    s2250_evtavprevio_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2250_evtavprevio_dados['identidade'] = doc.eSocial.evtAvPrevio['Id']
    evtAvPrevio = doc.eSocial.evtAvPrevio

    try:
        s2250_evtavprevio_dados['indretif'] = read_from_xml(evtAvPrevio.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['nrrecibo'] = read_from_xml(evtAvPrevio.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['tpamb'] = read_from_xml(evtAvPrevio.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['procemi'] = read_from_xml(evtAvPrevio.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['verproc'] = read_from_xml(evtAvPrevio.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['tpinsc'] = read_from_xml(evtAvPrevio.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['nrinsc'] = read_from_xml(evtAvPrevio.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['cpftrab'] = read_from_xml(evtAvPrevio.ideVinculo.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['nistrab'] = read_from_xml(evtAvPrevio.ideVinculo.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['matricula'] = read_from_xml(evtAvPrevio.ideVinculo.matricula.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s2250_evtavprevio = s2250evtAvPrevio.objects.create(**s2250_evtavprevio_dados)

    if 'infoAvPrevio' in dir(evtAvPrevio) and 'detAvPrevio' in dir(evtAvPrevio.infoAvPrevio):

        for detAvPrevio in evtAvPrevio.infoAvPrevio.detAvPrevio:

            s2250_detavprevio_dados = {}
            s2250_detavprevio_dados['s2250_evtavprevio_id'] = s2250_evtavprevio.id

            try:
                s2250_detavprevio_dados['dtavprv'] = read_from_xml(detAvPrevio.dtAvPrv.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2250_detavprevio_dados['dtprevdeslig'] = read_from_xml(detAvPrevio.dtPrevDeslig.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2250_detavprevio_dados['tpavprevio'] = read_from_xml(detAvPrevio.tpAvPrevio.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2250_detavprevio_dados['observacao'] = read_from_xml(detAvPrevio.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2250_detavprevio = s2250detAvPrevio.objects.create(**s2250_detavprevio_dados)

    if 'infoAvPrevio' in dir(evtAvPrevio) and 'cancAvPrevio' in dir(evtAvPrevio.infoAvPrevio):

        for cancAvPrevio in evtAvPrevio.infoAvPrevio.cancAvPrevio:

            s2250_cancavprevio_dados = {}
            s2250_cancavprevio_dados['s2250_evtavprevio_id'] = s2250_evtavprevio.id

            try:
                s2250_cancavprevio_dados['dtcancavprv'] = read_from_xml(cancAvPrevio.dtCancAvPrv.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2250_cancavprevio_dados['observacao'] = read_from_xml(cancAvPrevio.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2250_cancavprevio_dados['mtvcancavprevio'] = read_from_xml(cancAvPrevio.mtvCancAvPrevio.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s2250_cancavprevio = s2250cancAvPrevio.objects.create(**s2250_cancavprevio_dados)
    s2250_evtavprevio_dados['evento'] = 's2250'
    s2250_evtavprevio_dados['id'] = s2250_evtavprevio.id
    s2250_evtavprevio_dados['identidade_evento'] = doc.eSocial.evtAvPrevio['Id']

    from emensageriapro.esocial.views.s2250_evtavprevio_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2250_evtavprevio.id)

    return s2250_evtavprevio_dados