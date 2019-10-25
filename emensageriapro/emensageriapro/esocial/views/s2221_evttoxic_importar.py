#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2221.models import *
from emensageriapro.functions import read_from_xml



def read_s2221_evttoxic_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2221_evttoxic_obj(request, doc, status, validar)
    return dados



def read_s2221_evttoxic(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2221_evttoxic_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2221evtToxic.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2221_evttoxic_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2221_evttoxic_dados = {}
    s2221_evttoxic_dados['status'] = status
    s2221_evttoxic_dados['arquivo_original'] = 1
    if arquivo:
        s2221_evttoxic_dados['arquivo'] = arquivo.arquivo
    s2221_evttoxic_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2221_evttoxic_dados['identidade'] = doc.eSocial.evtToxic['Id']
    evtToxic = doc.eSocial.evtToxic

    try:
        s2221_evttoxic_dados['indretif'] = read_from_xml(evtToxic.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['nrrecibo'] = read_from_xml(evtToxic.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['tpamb'] = read_from_xml(evtToxic.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['procemi'] = read_from_xml(evtToxic.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['verproc'] = read_from_xml(evtToxic.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['tpinsc'] = read_from_xml(evtToxic.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['nrinsc'] = read_from_xml(evtToxic.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['cpftrab'] = read_from_xml(evtToxic.ideVinculo.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['nistrab'] = read_from_xml(evtToxic.ideVinculo.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['matricula'] = read_from_xml(evtToxic.ideVinculo.matricula.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['codcateg'] = read_from_xml(evtToxic.ideVinculo.codCateg.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['dtexame'] = read_from_xml(evtToxic.toxicologico.dtExame.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['cnpjlab'] = read_from_xml(evtToxic.toxicologico.cnpjLab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['codseqexame'] = read_from_xml(evtToxic.toxicologico.codSeqExame.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['nmmed'] = read_from_xml(evtToxic.toxicologico.nmMed.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['nrcrm'] = read_from_xml(evtToxic.toxicologico.nrCRM.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['ufcrm'] = read_from_xml(evtToxic.toxicologico.ufCRM.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['indrecusa'] = read_from_xml(evtToxic.toxicologico.indRecusa.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s2221_evttoxic = s2221evtToxic.objects.create(**s2221_evttoxic_dados)
    s2221_evttoxic_dados['evento'] = 's2221'
    s2221_evttoxic_dados['id'] = s2221_evttoxic.id
    s2221_evttoxic_dados['identidade_evento'] = doc.eSocial.evtToxic['Id']

    from emensageriapro.esocial.views.s2221_evttoxic_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2221_evttoxic.id)

    return s2221_evttoxic_dados