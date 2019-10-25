#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2245.models import *
from emensageriapro.functions import read_from_xml



def read_s2245_evttreicap_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2245_evttreicap_obj(request, doc, status, validar)
    return dados



def read_s2245_evttreicap(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2245_evttreicap_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2245evtTreiCap.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2245_evttreicap_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2245_evttreicap_dados = {}
    s2245_evttreicap_dados['status'] = status
    s2245_evttreicap_dados['arquivo_original'] = 1
    if arquivo:
        s2245_evttreicap_dados['arquivo'] = arquivo.arquivo
    s2245_evttreicap_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2245_evttreicap_dados['identidade'] = doc.eSocial.evtTreiCap['Id']
    evtTreiCap = doc.eSocial.evtTreiCap

    try:
        s2245_evttreicap_dados['indretif'] = read_from_xml(evtTreiCap.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['nrrecibo'] = read_from_xml(evtTreiCap.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['tpamb'] = read_from_xml(evtTreiCap.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['procemi'] = read_from_xml(evtTreiCap.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['verproc'] = read_from_xml(evtTreiCap.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['tpinsc'] = read_from_xml(evtTreiCap.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['nrinsc'] = read_from_xml(evtTreiCap.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['cpftrab'] = read_from_xml(evtTreiCap.ideVinculo.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['nistrab'] = read_from_xml(evtTreiCap.ideVinculo.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['matricula'] = read_from_xml(evtTreiCap.ideVinculo.matricula.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['codcateg'] = read_from_xml(evtTreiCap.ideVinculo.codCateg.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['codtreicap'] = read_from_xml(evtTreiCap.treiCap.codTreiCap.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['obstreicap'] = read_from_xml(evtTreiCap.treiCap.obsTreiCap.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['observacao'] = read_from_xml(evtTreiCap.treiCap.observacao.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['dttreicap'] = read_from_xml(evtTreiCap.treiCap.infoComplem.dtTreiCap.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['durtreicap'] = read_from_xml(evtTreiCap.treiCap.infoComplem.durTreiCap.cdata, 'esocial', 'N', 2)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['modtreicap'] = read_from_xml(evtTreiCap.treiCap.infoComplem.modTreiCap.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['tptreicap'] = read_from_xml(evtTreiCap.treiCap.infoComplem.tpTreiCap.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2245_evttreicap_dados['indtreinant'] = read_from_xml(evtTreiCap.treiCap.infoComplem.indTreinAnt.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s2245_evttreicap = s2245evtTreiCap.objects.create(**s2245_evttreicap_dados)

    if 'treiCap' in dir(evtTreiCap) and 'infoComplem' in dir(evtTreiCap.treiCap) and 'ideProfResp' in dir(evtTreiCap.treiCap.infoComplem):

        for ideProfResp in evtTreiCap.treiCap.infoComplem.ideProfResp:

            s2245_ideprofresp_dados = {}
            s2245_ideprofresp_dados['s2245_evttreicap_id'] = s2245_evttreicap.id

            try:
                s2245_ideprofresp_dados['cpfprof'] = read_from_xml(ideProfResp.cpfProf.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2245_ideprofresp_dados['nmprof'] = read_from_xml(ideProfResp.nmProf.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2245_ideprofresp_dados['tpprof'] = read_from_xml(ideProfResp.tpProf.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2245_ideprofresp_dados['formprof'] = read_from_xml(ideProfResp.formProf.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2245_ideprofresp_dados['codcbo'] = read_from_xml(ideProfResp.codCBO.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2245_ideprofresp_dados['nacprof'] = read_from_xml(ideProfResp.nacProf.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s2245_ideprofresp = s2245ideProfResp.objects.create(**s2245_ideprofresp_dados)
    s2245_evttreicap_dados['evento'] = 's2245'
    s2245_evttreicap_dados['id'] = s2245_evttreicap.id
    s2245_evttreicap_dados['identidade_evento'] = doc.eSocial.evtTreiCap['Id']

    from emensageriapro.esocial.views.s2245_evttreicap_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2245_evttreicap.id)

    return s2245_evttreicap_dados