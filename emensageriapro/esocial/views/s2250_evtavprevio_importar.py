#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2250.models import *



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
        s2250_evtavprevio_dados['indretif'] = evtAvPrevio.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['nrrecibo'] = evtAvPrevio.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['tpamb'] = evtAvPrevio.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['procemi'] = evtAvPrevio.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['verproc'] = evtAvPrevio.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['tpinsc'] = evtAvPrevio.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['nrinsc'] = evtAvPrevio.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['cpftrab'] = evtAvPrevio.ideVinculo.cpfTrab.cdata
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['nistrab'] = evtAvPrevio.ideVinculo.nisTrab.cdata
    except AttributeError:
        pass

    try:
        s2250_evtavprevio_dados['matricula'] = evtAvPrevio.ideVinculo.matricula.cdata
    except AttributeError:
        pass

    s2250_evtavprevio = s2250evtAvPrevio.objects.create(**s2250_evtavprevio_dados)

    if 'infoAvPrevio' in dir(evtAvPrevio) and 'detAvPrevio' in dir(evtAvPrevio.infoAvPrevio):

        for detAvPrevio in evtAvPrevio.infoAvPrevio.detAvPrevio:

            s2250_detavprevio_dados = {}
            s2250_detavprevio_dados['s2250_evtavprevio_id'] = s2250_evtavprevio.id

            try:
                s2250_detavprevio_dados['dtavprv'] = detAvPrevio.dtAvPrv.cdata
            except AttributeError:
                pass

            try:
                s2250_detavprevio_dados['dtprevdeslig'] = detAvPrevio.dtPrevDeslig.cdata
            except AttributeError:
                pass

            try:
                s2250_detavprevio_dados['tpavprevio'] = detAvPrevio.tpAvPrevio.cdata
            except AttributeError:
                pass

            try:
                s2250_detavprevio_dados['observacao'] = detAvPrevio.observacao.cdata
            except AttributeError:
                pass

            s2250_detavprevio = s2250detAvPrevio.objects.create(**s2250_detavprevio_dados)

    if 'infoAvPrevio' in dir(evtAvPrevio) and 'cancAvPrevio' in dir(evtAvPrevio.infoAvPrevio):

        for cancAvPrevio in evtAvPrevio.infoAvPrevio.cancAvPrevio:

            s2250_cancavprevio_dados = {}
            s2250_cancavprevio_dados['s2250_evtavprevio_id'] = s2250_evtavprevio.id

            try:
                s2250_cancavprevio_dados['dtcancavprv'] = cancAvPrevio.dtCancAvPrv.cdata
            except AttributeError:
                pass

            try:
                s2250_cancavprevio_dados['observacao'] = cancAvPrevio.observacao.cdata
            except AttributeError:
                pass

            try:
                s2250_cancavprevio_dados['mtvcancavprevio'] = cancAvPrevio.mtvCancAvPrevio.cdata
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