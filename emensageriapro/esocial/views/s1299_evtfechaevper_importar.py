#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1299.models import *
from emensageriapro.functions import read_from_xml



def read_s1299_evtfechaevper_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1299_evtfechaevper_obj(request, doc, status, validar)
    return dados



def read_s1299_evtfechaevper(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1299_evtfechaevper_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1299evtFechaEvPer.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1299_evtfechaevper_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1299_evtfechaevper_dados = {}
    s1299_evtfechaevper_dados['status'] = status
    s1299_evtfechaevper_dados['arquivo_original'] = 1
    if arquivo:
        s1299_evtfechaevper_dados['arquivo'] = arquivo.arquivo
    s1299_evtfechaevper_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1299_evtfechaevper_dados['identidade'] = doc.eSocial.evtFechaEvPer['Id']
    evtFechaEvPer = doc.eSocial.evtFechaEvPer

    try:
        s1299_evtfechaevper_dados['indapuracao'] = read_from_xml(evtFechaEvPer.ideEvento.indApuracao.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1299_evtfechaevper_dados['perapur'] = read_from_xml(evtFechaEvPer.ideEvento.perApur.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1299_evtfechaevper_dados['tpamb'] = read_from_xml(evtFechaEvPer.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1299_evtfechaevper_dados['procemi'] = read_from_xml(evtFechaEvPer.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1299_evtfechaevper_dados['verproc'] = read_from_xml(evtFechaEvPer.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1299_evtfechaevper_dados['tpinsc'] = read_from_xml(evtFechaEvPer.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1299_evtfechaevper_dados['nrinsc'] = read_from_xml(evtFechaEvPer.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1299_evtfechaevper_dados['evtremun'] = read_from_xml(evtFechaEvPer.infoFech.evtRemun.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1299_evtfechaevper_dados['evtpgtos'] = read_from_xml(evtFechaEvPer.infoFech.evtPgtos.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1299_evtfechaevper_dados['evtaqprod'] = read_from_xml(evtFechaEvPer.infoFech.evtAqProd.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1299_evtfechaevper_dados['evtcomprod'] = read_from_xml(evtFechaEvPer.infoFech.evtComProd.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1299_evtfechaevper_dados['evtcontratavnp'] = read_from_xml(evtFechaEvPer.infoFech.evtContratAvNP.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1299_evtfechaevper_dados['evtinfocomplper'] = read_from_xml(evtFechaEvPer.infoFech.evtInfoComplPer.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1299_evtfechaevper_dados['compsemmovto'] = read_from_xml(evtFechaEvPer.infoFech.compSemMovto.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1299_evtfechaevper = s1299evtFechaEvPer.objects.create(**s1299_evtfechaevper_dados)

    if 'ideRespInf' in dir(evtFechaEvPer):

        for ideRespInf in evtFechaEvPer.ideRespInf:

            s1299_iderespinf_dados = {}
            s1299_iderespinf_dados['s1299_evtfechaevper_id'] = s1299_evtfechaevper.id

            try:
                s1299_iderespinf_dados['nmresp'] = read_from_xml(ideRespInf.nmResp.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1299_iderespinf_dados['cpfresp'] = read_from_xml(ideRespInf.cpfResp.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1299_iderespinf_dados['telefone'] = read_from_xml(ideRespInf.telefone.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1299_iderespinf_dados['email'] = read_from_xml(ideRespInf.email.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1299_iderespinf = s1299ideRespInf.objects.create(**s1299_iderespinf_dados)
    s1299_evtfechaevper_dados['evento'] = 's1299'
    s1299_evtfechaevper_dados['id'] = s1299_evtfechaevper.id
    s1299_evtfechaevper_dados['identidade_evento'] = doc.eSocial.evtFechaEvPer['Id']

    from emensageriapro.esocial.views.s1299_evtfechaevper_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1299_evtfechaevper.id)

    return s1299_evtfechaevper_dados