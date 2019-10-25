#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1295.models import *
from emensageriapro.functions import read_from_xml



def read_s1295_evttotconting_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1295_evttotconting_obj(request, doc, status, validar)
    return dados



def read_s1295_evttotconting(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1295_evttotconting_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1295evtTotConting.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1295_evttotconting_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1295_evttotconting_dados = {}
    s1295_evttotconting_dados['status'] = status
    s1295_evttotconting_dados['arquivo_original'] = 1
    if arquivo:
        s1295_evttotconting_dados['arquivo'] = arquivo.arquivo
    s1295_evttotconting_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1295_evttotconting_dados['identidade'] = doc.eSocial.evtTotConting['Id']
    evtTotConting = doc.eSocial.evtTotConting

    try:
        s1295_evttotconting_dados['indapuracao'] = read_from_xml(evtTotConting.ideEvento.indApuracao.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1295_evttotconting_dados['perapur'] = read_from_xml(evtTotConting.ideEvento.perApur.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1295_evttotconting_dados['tpamb'] = read_from_xml(evtTotConting.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1295_evttotconting_dados['procemi'] = read_from_xml(evtTotConting.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1295_evttotconting_dados['verproc'] = read_from_xml(evtTotConting.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1295_evttotconting_dados['tpinsc'] = read_from_xml(evtTotConting.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1295_evttotconting_dados['nrinsc'] = read_from_xml(evtTotConting.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1295_evttotconting = s1295evtTotConting.objects.create(**s1295_evttotconting_dados)

    if 'ideRespInf' in dir(evtTotConting):

        for ideRespInf in evtTotConting.ideRespInf:

            s1295_iderespinf_dados = {}
            s1295_iderespinf_dados['s1295_evttotconting_id'] = s1295_evttotconting.id

            try:
                s1295_iderespinf_dados['nmresp'] = read_from_xml(ideRespInf.nmResp.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1295_iderespinf_dados['cpfresp'] = read_from_xml(ideRespInf.cpfResp.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1295_iderespinf_dados['telefone'] = read_from_xml(ideRespInf.telefone.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1295_iderespinf_dados['email'] = read_from_xml(ideRespInf.email.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1295_iderespinf = s1295ideRespInf.objects.create(**s1295_iderespinf_dados)
    s1295_evttotconting_dados['evento'] = 's1295'
    s1295_evttotconting_dados['id'] = s1295_evttotconting.id
    s1295_evttotconting_dados['identidade_evento'] = doc.eSocial.evtTotConting['Id']

    from emensageriapro.esocial.views.s1295_evttotconting_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1295_evttotconting.id)

    return s1295_evttotconting_dados