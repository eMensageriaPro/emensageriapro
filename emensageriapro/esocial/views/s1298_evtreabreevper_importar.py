# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1298.models import *
from emensageriapro.functions import read_from_xml



def read_s1298_evtreabreevper_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1298_evtreabreevper_obj(request, doc, status, validar)
    return dados



def read_s1298_evtreabreevper(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1298_evtreabreevper_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1298evtReabreEvPer.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1298_evtreabreevper_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1298_evtreabreevper_dados = {}
    s1298_evtreabreevper_dados['status'] = status
    s1298_evtreabreevper_dados['arquivo_original'] = 1
    if arquivo:
        s1298_evtreabreevper_dados['arquivo'] = arquivo.arquivo
    s1298_evtreabreevper_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1298_evtreabreevper_dados['identidade'] = doc.eSocial.evtReabreEvPer['Id']
    evtReabreEvPer = doc.eSocial.evtReabreEvPer

    try:
        s1298_evtreabreevper_dados['indapuracao'] = read_from_xml(evtReabreEvPer.ideEvento.indApuracao.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1298_evtreabreevper_dados['perapur'] = read_from_xml(evtReabreEvPer.ideEvento.perApur.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1298_evtreabreevper_dados['tpamb'] = read_from_xml(evtReabreEvPer.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1298_evtreabreevper_dados['procemi'] = read_from_xml(evtReabreEvPer.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1298_evtreabreevper_dados['verproc'] = read_from_xml(evtReabreEvPer.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1298_evtreabreevper_dados['tpinsc'] = read_from_xml(evtReabreEvPer.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1298_evtreabreevper_dados['nrinsc'] = read_from_xml(evtReabreEvPer.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1298_evtreabreevper = s1298evtReabreEvPer.objects.create(**s1298_evtreabreevper_dados)
    s1298_evtreabreevper_dados['evento'] = 's1298'
    s1298_evtreabreevper_dados['id'] = s1298_evtreabreevper.id
    s1298_evtreabreevper_dados['identidade_evento'] = doc.eSocial.evtReabreEvPer['Id']

    from emensageriapro.esocial.views.s1298_evtreabreevper_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1298_evtreabreevper.id)

    return s1298_evtreabreevper_dados