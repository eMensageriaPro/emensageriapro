#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2420.models import *



def read_s2420_evtcdbenterm_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2420_evtcdbenterm_obj(request, doc, status, validar)
    return dados



def read_s2420_evtcdbenterm(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2420_evtcdbenterm_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2420evtCdBenTerm.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2420_evtcdbenterm_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2420_evtcdbenterm_dados = {}
    s2420_evtcdbenterm_dados['status'] = status
    s2420_evtcdbenterm_dados['arquivo_original'] = 1
    if arquivo:
        s2420_evtcdbenterm_dados['arquivo'] = arquivo.arquivo
    s2420_evtcdbenterm_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2420_evtcdbenterm_dados['identidade'] = doc.eSocial.evtCdBenTerm['Id']
    evtCdBenTerm = doc.eSocial.evtCdBenTerm

    try:
        s2420_evtcdbenterm_dados['indretif'] = evtCdBenTerm.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        s2420_evtcdbenterm_dados['nrrecibo'] = evtCdBenTerm.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        s2420_evtcdbenterm_dados['tpamb'] = evtCdBenTerm.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s2420_evtcdbenterm_dados['procemi'] = evtCdBenTerm.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s2420_evtcdbenterm_dados['verproc'] = evtCdBenTerm.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s2420_evtcdbenterm_dados['tpinsc'] = evtCdBenTerm.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s2420_evtcdbenterm_dados['nrinsc'] = evtCdBenTerm.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    try:
        s2420_evtcdbenterm_dados['cpfbenef'] = evtCdBenTerm.ideBeneficio.cpfBenef.cdata
    except AttributeError:
        pass

    try:
        s2420_evtcdbenterm_dados['nrbeneficio'] = evtCdBenTerm.ideBeneficio.nrBeneficio.cdata
    except AttributeError:
        pass

    try:
        s2420_evtcdbenterm_dados['dttermbeneficio'] = evtCdBenTerm.infoBenTermino.dtTermBeneficio.cdata
    except AttributeError:
        pass

    try:
        s2420_evtcdbenterm_dados['mtvtermino'] = evtCdBenTerm.infoBenTermino.mtvTermino.cdata
    except AttributeError:
        pass

    s2420_evtcdbenterm = s2420evtCdBenTerm.objects.create(**s2420_evtcdbenterm_dados)
    s2420_evtcdbenterm_dados['evento'] = 's2420'
    s2420_evtcdbenterm_dados['id'] = s2420_evtcdbenterm.id
    s2420_evtcdbenterm_dados['identidade_evento'] = doc.eSocial.evtCdBenTerm['Id']

    from emensageriapro.esocial.views.s2420_evtcdbenterm_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2420_evtcdbenterm.id)

    return s2420_evtcdbenterm_dados