# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2231.models import *
from emensageriapro.functions import read_from_xml



def read_s2231_evtcessao_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2231_evtcessao_obj(request, doc, status, validar)
    return dados



def read_s2231_evtcessao(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2231_evtcessao_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2231evtCessao.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2231_evtcessao_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2231_evtcessao_dados = {}
    s2231_evtcessao_dados['status'] = status
    s2231_evtcessao_dados['arquivo_original'] = 1
    if arquivo:
        s2231_evtcessao_dados['arquivo'] = arquivo.arquivo
    s2231_evtcessao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2231_evtcessao_dados['identidade'] = doc.eSocial.evtCessao['Id']
    evtCessao = doc.eSocial.evtCessao

    try:
        s2231_evtcessao_dados['indretif'] = read_from_xml(evtCessao.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2231_evtcessao_dados['nrrecibo'] = read_from_xml(evtCessao.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2231_evtcessao_dados['tpamb'] = read_from_xml(evtCessao.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2231_evtcessao_dados['procemi'] = read_from_xml(evtCessao.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2231_evtcessao_dados['verproc'] = read_from_xml(evtCessao.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2231_evtcessao_dados['tpinsc'] = read_from_xml(evtCessao.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2231_evtcessao_dados['nrinsc'] = read_from_xml(evtCessao.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2231_evtcessao_dados['cpftrab'] = read_from_xml(evtCessao.ideVinculo.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2231_evtcessao_dados['nistrab'] = read_from_xml(evtCessao.ideVinculo.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2231_evtcessao_dados['matricula'] = read_from_xml(evtCessao.ideVinculo.matricula.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s2231_evtcessao = s2231evtCessao.objects.create(**s2231_evtcessao_dados)

    if 'infoCessao' in dir(evtCessao) and 'iniCessao' in dir(evtCessao.infoCessao):

        for iniCessao in evtCessao.infoCessao.iniCessao:

            s2231_inicessao_dados = {}
            s2231_inicessao_dados['s2231_evtcessao_id'] = s2231_evtcessao.id

            try:
                s2231_inicessao_dados['dtinicessao'] = read_from_xml(iniCessao.dtIniCessao.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2231_inicessao_dados['cnpjcess'] = read_from_xml(iniCessao.cnpjCess.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2231_inicessao_dados['infonus'] = read_from_xml(iniCessao.infOnus.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2231_inicessao_dados['indcessao'] = read_from_xml(iniCessao.indCessao.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2231_inicessao_dados['dscsituacao'] = read_from_xml(iniCessao.dscSituacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2231_inicessao = s2231iniCessao.objects.create(**s2231_inicessao_dados)

    if 'infoCessao' in dir(evtCessao) and 'fimCessao' in dir(evtCessao.infoCessao):

        for fimCessao in evtCessao.infoCessao.fimCessao:

            s2231_fimcessao_dados = {}
            s2231_fimcessao_dados['s2231_evtcessao_id'] = s2231_evtcessao.id

            try:
                s2231_fimcessao_dados['dttermcessao'] = read_from_xml(fimCessao.dtTermCessao.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            s2231_fimcessao = s2231fimCessao.objects.create(**s2231_fimcessao_dados)
    s2231_evtcessao_dados['evento'] = 's2231'
    s2231_evtcessao_dados['id'] = s2231_evtcessao.id
    s2231_evtcessao_dados['identidade_evento'] = doc.eSocial.evtCessao['Id']

    from emensageriapro.esocial.views.s2231_evtcessao_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2231_evtcessao.id)

    return s2231_evtcessao_dados