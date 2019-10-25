#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1300.models import *
from emensageriapro.functions import read_from_xml



def read_s1300_evtcontrsindpatr_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1300_evtcontrsindpatr_obj(request, doc, status, validar)
    return dados



def read_s1300_evtcontrsindpatr(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1300_evtcontrsindpatr_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1300evtContrSindPatr.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1300_evtcontrsindpatr_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1300_evtcontrsindpatr_dados = {}
    s1300_evtcontrsindpatr_dados['status'] = status
    s1300_evtcontrsindpatr_dados['arquivo_original'] = 1
    if arquivo:
        s1300_evtcontrsindpatr_dados['arquivo'] = arquivo.arquivo
    s1300_evtcontrsindpatr_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1300_evtcontrsindpatr_dados['identidade'] = doc.eSocial.evtContrSindPatr['Id']
    evtContrSindPatr = doc.eSocial.evtContrSindPatr

    try:
        s1300_evtcontrsindpatr_dados['indretif'] = read_from_xml(evtContrSindPatr.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1300_evtcontrsindpatr_dados['nrrecibo'] = read_from_xml(evtContrSindPatr.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1300_evtcontrsindpatr_dados['indapuracao'] = read_from_xml(evtContrSindPatr.ideEvento.indApuracao.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1300_evtcontrsindpatr_dados['perapur'] = read_from_xml(evtContrSindPatr.ideEvento.perApur.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1300_evtcontrsindpatr_dados['tpamb'] = read_from_xml(evtContrSindPatr.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1300_evtcontrsindpatr_dados['procemi'] = read_from_xml(evtContrSindPatr.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1300_evtcontrsindpatr_dados['verproc'] = read_from_xml(evtContrSindPatr.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1300_evtcontrsindpatr_dados['tpinsc'] = read_from_xml(evtContrSindPatr.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1300_evtcontrsindpatr_dados['nrinsc'] = read_from_xml(evtContrSindPatr.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1300_evtcontrsindpatr = s1300evtContrSindPatr.objects.create(**s1300_evtcontrsindpatr_dados)

    if 'contribSind' in dir(evtContrSindPatr):

        for contribSind in evtContrSindPatr.contribSind:

            s1300_contribsind_dados = {}
            s1300_contribsind_dados['s1300_evtcontrsindpatr_id'] = s1300_evtcontrsindpatr.id

            try:
                s1300_contribsind_dados['cnpjsindic'] = read_from_xml(contribSind.cnpjSindic.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1300_contribsind_dados['tpcontribsind'] = read_from_xml(contribSind.tpContribSind.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1300_contribsind_dados['vlrcontribsind'] = read_from_xml(contribSind.vlrContribSind.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            s1300_contribsind = s1300contribSind.objects.create(**s1300_contribsind_dados)
    s1300_evtcontrsindpatr_dados['evento'] = 's1300'
    s1300_evtcontrsindpatr_dados['id'] = s1300_evtcontrsindpatr.id
    s1300_evtcontrsindpatr_dados['identidade_evento'] = doc.eSocial.evtContrSindPatr['Id']

    from emensageriapro.esocial.views.s1300_evtcontrsindpatr_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1300_evtcontrsindpatr.id)

    return s1300_evtcontrsindpatr_dados