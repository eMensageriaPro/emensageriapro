#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2221.models import *



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

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_s2221_evttoxic_obj(request, doc, status, validar, arquivo)
    novo_arquivo = arquivo.replace('/aguardando/', '/processado/')
    s2221evtToxic.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s2221_evttoxic_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2221_evttoxic_dados = {}
    s2221_evttoxic_dados['status'] = status
    s2221_evttoxic_dados['arquivo_original'] = 1
    if arquivo:
        s2221_evttoxic_dados['arquivo'] = arquivo
    s2221_evttoxic_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2221_evttoxic_dados['identidade'] = doc.eSocial.evtToxic['Id']
    evtToxic = doc.eSocial.evtToxic

    try:
        s2221_evttoxic_dados['indretif'] = evtToxic.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['nrrecibo'] = evtToxic.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['tpamb'] = evtToxic.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['procemi'] = evtToxic.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['verproc'] = evtToxic.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['tpinsc'] = evtToxic.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['nrinsc'] = evtToxic.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['cpftrab'] = evtToxic.ideVinculo.cpfTrab.cdata
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['nistrab'] = evtToxic.ideVinculo.nisTrab.cdata
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['matricula'] = evtToxic.ideVinculo.matricula.cdata
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['codcateg'] = evtToxic.ideVinculo.codCateg.cdata
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['dtexame'] = evtToxic.toxicologico.dtExame.cdata
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['cnpjlab'] = evtToxic.toxicologico.cnpjLab.cdata
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['codseqexame'] = evtToxic.toxicologico.codSeqExame.cdata
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['nmmed'] = evtToxic.toxicologico.nmMed.cdata
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['nrcrm'] = evtToxic.toxicologico.nrCRM.cdata
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['ufcrm'] = evtToxic.toxicologico.ufCRM.cdata
    except AttributeError:
        pass

    try:
        s2221_evttoxic_dados['indrecusa'] = evtToxic.toxicologico.indRecusa.cdata
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