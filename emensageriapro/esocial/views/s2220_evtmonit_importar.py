# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2220.models import *
from emensageriapro.functions import read_from_xml



def read_s2220_evtmonit_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2220_evtmonit_obj(request, doc, status, validar)
    return dados



def read_s2220_evtmonit(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2220_evtmonit_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2220evtMonit.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2220_evtmonit_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2220_evtmonit_dados = {}
    s2220_evtmonit_dados['status'] = status
    s2220_evtmonit_dados['arquivo_original'] = 1
    if arquivo:
        s2220_evtmonit_dados['arquivo'] = arquivo.arquivo
    s2220_evtmonit_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2220_evtmonit_dados['identidade'] = doc.eSocial.evtMonit['Id']
    evtMonit = doc.eSocial.evtMonit

    try:
        s2220_evtmonit_dados['indretif'] = read_from_xml(evtMonit.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['nrrecibo'] = read_from_xml(evtMonit.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['tpamb'] = read_from_xml(evtMonit.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['procemi'] = read_from_xml(evtMonit.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['verproc'] = read_from_xml(evtMonit.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['tpinsc'] = read_from_xml(evtMonit.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['nrinsc'] = read_from_xml(evtMonit.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['cpftrab'] = read_from_xml(evtMonit.ideVinculo.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['nistrab'] = read_from_xml(evtMonit.ideVinculo.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['matricula'] = read_from_xml(evtMonit.ideVinculo.matricula.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['codcateg'] = read_from_xml(evtMonit.ideVinculo.codCateg.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['tpexameocup'] = read_from_xml(evtMonit.exMedOcup.tpExameOcup.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['dtaso'] = read_from_xml(evtMonit.exMedOcup.aso.dtAso.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['tpaso'] = read_from_xml(evtMonit.exMedOcup.aso.tpAso.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['resaso'] = read_from_xml(evtMonit.exMedOcup.aso.resAso.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['cpfmed'] = read_from_xml(evtMonit.exMedOcup.aso.medico.cpfMed.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['nismed'] = read_from_xml(evtMonit.exMedOcup.aso.medico.nisMed.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['nmmed'] = read_from_xml(evtMonit.exMedOcup.aso.medico.nmMed.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['nrcrm'] = read_from_xml(evtMonit.exMedOcup.aso.medico.nrCRM.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['ufcrm'] = read_from_xml(evtMonit.exMedOcup.aso.medico.ufCRM.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['nisresp'] = read_from_xml(evtMonit.exMedOcup.respMonit.nisResp.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['nrconsclasse'] = read_from_xml(evtMonit.exMedOcup.respMonit.nrConsClasse.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['ufconsclasse'] = read_from_xml(evtMonit.exMedOcup.respMonit.ufConsClasse.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['cpfresp'] = read_from_xml(evtMonit.exMedOcup.respMonit.cpfResp.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['nmresp'] = read_from_xml(evtMonit.exMedOcup.respMonit.nmResp.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['nrcrm'] = read_from_xml(evtMonit.exMedOcup.respMonit.nrCRM.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2220_evtmonit_dados['ufcrm'] = read_from_xml(evtMonit.exMedOcup.respMonit.ufCRM.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s2220_evtmonit = s2220evtMonit.objects.create(**s2220_evtmonit_dados)

    if 'exMedOcup' in dir(evtMonit) and 'aso' in dir(evtMonit.exMedOcup) and 'exame' in dir(evtMonit.exMedOcup.aso):

        for exame in evtMonit.exMedOcup.aso.exame:

            s2220_exame_dados = {}
            s2220_exame_dados['s2220_evtmonit_id'] = s2220_evtmonit.id

            try:
                s2220_exame_dados['dtexm'] = read_from_xml(exame.dtExm.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2220_exame_dados['procrealizado'] = read_from_xml(exame.procRealizado.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2220_exame_dados['obsproc'] = read_from_xml(exame.obsProc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2220_exame_dados['interprexm'] = read_from_xml(exame.interprExm.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2220_exame_dados['ordexame'] = read_from_xml(exame.ordExame.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2220_exame_dados['dtinimonit'] = read_from_xml(exame.dtIniMonit.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2220_exame_dados['dtfimmonit'] = read_from_xml(exame.dtFimMonit.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2220_exame_dados['indresult'] = read_from_xml(exame.indResult.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s2220_exame = s2220exame.objects.create(**s2220_exame_dados)
    s2220_evtmonit_dados['evento'] = 's2220'
    s2220_evtmonit_dados['id'] = s2220_evtmonit.id
    s2220_evtmonit_dados['identidade_evento'] = doc.eSocial.evtMonit['Id']

    from emensageriapro.esocial.views.s2220_evtmonit_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2220_evtmonit.id)

    return s2220_evtmonit_dados