#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1280.models import *
from emensageriapro.functions import read_from_xml



def read_s1280_evtinfocomplper_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1280_evtinfocomplper_obj(request, doc, status, validar)
    return dados



def read_s1280_evtinfocomplper(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1280_evtinfocomplper_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1280evtInfoComplPer.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1280_evtinfocomplper_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1280_evtinfocomplper_dados = {}
    s1280_evtinfocomplper_dados['status'] = status
    s1280_evtinfocomplper_dados['arquivo_original'] = 1
    if arquivo:
        s1280_evtinfocomplper_dados['arquivo'] = arquivo.arquivo
    s1280_evtinfocomplper_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1280_evtinfocomplper_dados['identidade'] = doc.eSocial.evtInfoComplPer['Id']
    evtInfoComplPer = doc.eSocial.evtInfoComplPer

    try:
        s1280_evtinfocomplper_dados['indretif'] = read_from_xml(evtInfoComplPer.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1280_evtinfocomplper_dados['nrrecibo'] = read_from_xml(evtInfoComplPer.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1280_evtinfocomplper_dados['indapuracao'] = read_from_xml(evtInfoComplPer.ideEvento.indApuracao.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1280_evtinfocomplper_dados['perapur'] = read_from_xml(evtInfoComplPer.ideEvento.perApur.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1280_evtinfocomplper_dados['tpamb'] = read_from_xml(evtInfoComplPer.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1280_evtinfocomplper_dados['procemi'] = read_from_xml(evtInfoComplPer.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1280_evtinfocomplper_dados['verproc'] = read_from_xml(evtInfoComplPer.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1280_evtinfocomplper_dados['tpinsc'] = read_from_xml(evtInfoComplPer.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1280_evtinfocomplper_dados['nrinsc'] = read_from_xml(evtInfoComplPer.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1280_evtinfocomplper = s1280evtInfoComplPer.objects.create(**s1280_evtinfocomplper_dados)

    if 'infoSubstPatr' in dir(evtInfoComplPer):

        for infoSubstPatr in evtInfoComplPer.infoSubstPatr:

            s1280_infosubstpatr_dados = {}
            s1280_infosubstpatr_dados['s1280_evtinfocomplper_id'] = s1280_evtinfocomplper.id

            try:
                s1280_infosubstpatr_dados['indsubstpatr'] = read_from_xml(infoSubstPatr.indSubstPatr.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1280_infosubstpatr_dados['percredcontrib'] = read_from_xml(infoSubstPatr.percRedContrib.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            s1280_infosubstpatr = s1280infoSubstPatr.objects.create(**s1280_infosubstpatr_dados)

    if 'infoSubstPatrOpPort' in dir(evtInfoComplPer):

        for infoSubstPatrOpPort in evtInfoComplPer.infoSubstPatrOpPort:

            s1280_infosubstpatropport_dados = {}
            s1280_infosubstpatropport_dados['s1280_evtinfocomplper_id'] = s1280_evtinfocomplper.id

            try:
                s1280_infosubstpatropport_dados['cnpjopportuario'] = read_from_xml(infoSubstPatrOpPort.cnpjOpPortuario.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1280_infosubstpatropport = s1280infoSubstPatrOpPort.objects.create(**s1280_infosubstpatropport_dados)

    if 'infoAtivConcom' in dir(evtInfoComplPer):

        for infoAtivConcom in evtInfoComplPer.infoAtivConcom:

            s1280_infoativconcom_dados = {}
            s1280_infoativconcom_dados['s1280_evtinfocomplper_id'] = s1280_evtinfocomplper.id

            try:
                s1280_infoativconcom_dados['fatormes'] = read_from_xml(infoAtivConcom.fatorMes.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            try:
                s1280_infoativconcom_dados['fator13'] = read_from_xml(infoAtivConcom.fator13.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            s1280_infoativconcom = s1280infoAtivConcom.objects.create(**s1280_infoativconcom_dados)
    s1280_evtinfocomplper_dados['evento'] = 's1280'
    s1280_evtinfocomplper_dados['id'] = s1280_evtinfocomplper.id
    s1280_evtinfocomplper_dados['identidade_evento'] = doc.eSocial.evtInfoComplPer['Id']

    from emensageriapro.esocial.views.s1280_evtinfocomplper_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1280_evtinfocomplper.id)

    return s1280_evtinfocomplper_dados