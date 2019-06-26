#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1280.models import *



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

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_s1280_evtinfocomplper_obj(request, doc, status, validar, arquivo)

    s1280evtInfoComplPer.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s1280_evtinfocomplper_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1280_evtinfocomplper_dados = {}
    s1280_evtinfocomplper_dados['status'] = status
    s1280_evtinfocomplper_dados['arquivo_original'] = 1
    if arquivo:
        s1280_evtinfocomplper_dados['arquivo'] = arquivo
    s1280_evtinfocomplper_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1280_evtinfocomplper_dados['identidade'] = doc.eSocial.evtInfoComplPer['Id']
    evtInfoComplPer = doc.eSocial.evtInfoComplPer

    try:
        s1280_evtinfocomplper_dados['indretif'] = evtInfoComplPer.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        s1280_evtinfocomplper_dados['nrrecibo'] = evtInfoComplPer.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        s1280_evtinfocomplper_dados['indapuracao'] = evtInfoComplPer.ideEvento.indApuracao.cdata
    except AttributeError:
        pass

    try:
        s1280_evtinfocomplper_dados['perapur'] = evtInfoComplPer.ideEvento.perApur.cdata
    except AttributeError:
        pass

    try:
        s1280_evtinfocomplper_dados['tpamb'] = evtInfoComplPer.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s1280_evtinfocomplper_dados['procemi'] = evtInfoComplPer.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s1280_evtinfocomplper_dados['verproc'] = evtInfoComplPer.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s1280_evtinfocomplper_dados['tpinsc'] = evtInfoComplPer.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s1280_evtinfocomplper_dados['nrinsc'] = evtInfoComplPer.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    s1280_evtinfocomplper = s1280evtInfoComplPer.objects.create(**s1280_evtinfocomplper_dados)

    if 'infoSubstPatr' in dir(evtInfoComplPer):

        for infoSubstPatr in evtInfoComplPer.infoSubstPatr:

            s1280_infosubstpatr_dados = {}
            s1280_infosubstpatr_dados['s1280_evtinfocomplper_id'] = s1280_evtinfocomplper.id

            try:
                s1280_infosubstpatr_dados['indsubstpatr'] = infoSubstPatr.indSubstPatr.cdata
            except AttributeError:
                pass

            try:
                s1280_infosubstpatr_dados['percredcontrib'] = infoSubstPatr.percRedContrib.cdata
            except AttributeError:
                pass

            s1280_infosubstpatr = s1280infoSubstPatr.objects.create(**s1280_infosubstpatr_dados)

    if 'infoSubstPatrOpPort' in dir(evtInfoComplPer):

        for infoSubstPatrOpPort in evtInfoComplPer.infoSubstPatrOpPort:

            s1280_infosubstpatropport_dados = {}
            s1280_infosubstpatropport_dados['s1280_evtinfocomplper_id'] = s1280_evtinfocomplper.id

            try:
                s1280_infosubstpatropport_dados['cnpjopportuario'] = infoSubstPatrOpPort.cnpjOpPortuario.cdata
            except AttributeError:
                pass

            s1280_infosubstpatropport = s1280infoSubstPatrOpPort.objects.create(**s1280_infosubstpatropport_dados)

    if 'infoAtivConcom' in dir(evtInfoComplPer):

        for infoAtivConcom in evtInfoComplPer.infoAtivConcom:

            s1280_infoativconcom_dados = {}
            s1280_infoativconcom_dados['s1280_evtinfocomplper_id'] = s1280_evtinfocomplper.id

            try:
                s1280_infoativconcom_dados['fatormes'] = infoAtivConcom.fatorMes.cdata
            except AttributeError:
                pass

            try:
                s1280_infoativconcom_dados['fator13'] = infoAtivConcom.fator13.cdata
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