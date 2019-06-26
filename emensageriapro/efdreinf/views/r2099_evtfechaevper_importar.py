#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r2099.models import *



def read_r2099_evtfechaevper_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2099_evtfechaevper_obj(request, doc, status, validar)
    return dados



def read_r2099_evtfechaevper(request, dados, arquivo, validar=False):

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
    dados = read_r2099_evtfechaevper_obj(request, doc, status, validar, arquivo)

    r2099evtFechaEvPer.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_r2099_evtfechaevper_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r2099_evtfechaevper_dados = {}
    r2099_evtfechaevper_dados['status'] = status
    r2099_evtfechaevper_dados['arquivo_original'] = 1
    if arquivo:
        r2099_evtfechaevper_dados['arquivo'] = arquivo
    r2099_evtfechaevper_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2099_evtfechaevper_dados['identidade'] = doc.Reinf.evtFechaEvPer['id']
    evtFechaEvPer = doc.Reinf.evtFechaEvPer

    try:
        r2099_evtfechaevper_dados['perapur'] = evtFechaEvPer.ideEvento.perApur.cdata
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['tpamb'] = evtFechaEvPer.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['procemi'] = evtFechaEvPer.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['verproc'] = evtFechaEvPer.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['tpinsc'] = evtFechaEvPer.ideContri.tpInsc.cdata
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['nrinsc'] = evtFechaEvPer.ideContri.nrInsc.cdata
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['evtservtm'] = evtFechaEvPer.infoFech.evtServTm.cdata
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['evtservpr'] = evtFechaEvPer.infoFech.evtServPr.cdata
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['evtassdesprec'] = evtFechaEvPer.infoFech.evtAssDespRec.cdata
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['evtassdesprep'] = evtFechaEvPer.infoFech.evtAssDespRep.cdata
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['evtcomprod'] = evtFechaEvPer.infoFech.evtComProd.cdata
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['evtcprb'] = evtFechaEvPer.infoFech.evtCPRB.cdata
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['evtpgtos'] = evtFechaEvPer.infoFech.evtPgtos.cdata
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['compsemmovto'] = evtFechaEvPer.infoFech.compSemMovto.cdata
    except AttributeError:
        pass

    r2099_evtfechaevper = r2099evtFechaEvPer.objects.create(**r2099_evtfechaevper_dados)

    if 'ideRespInf' in dir(evtFechaEvPer):

        for ideRespInf in evtFechaEvPer.ideRespInf:

            r2099_iderespinf_dados = {}
            r2099_iderespinf_dados['r2099_evtfechaevper_id'] = r2099_evtfechaevper.id

            try:
                r2099_iderespinf_dados['nmresp'] = ideRespInf.nmResp.cdata
            except AttributeError:
                pass

            try:
                r2099_iderespinf_dados['cpfresp'] = ideRespInf.cpfResp.cdata
            except AttributeError:
                pass

            try:
                r2099_iderespinf_dados['telefone'] = ideRespInf.telefone.cdata
            except AttributeError:
                pass

            try:
                r2099_iderespinf_dados['email'] = ideRespInf.email.cdata
            except AttributeError:
                pass

            r2099_iderespinf = r2099ideRespInf.objects.create(**r2099_iderespinf_dados)
    r2099_evtfechaevper_dados['evento'] = 'r2099'
    r2099_evtfechaevper_dados['id'] = r2099_evtfechaevper.id
    r2099_evtfechaevper_dados['identidade_evento'] = doc.Reinf.evtFechaEvPer['id']

    from emensageriapro.efdreinf.views.r2099_evtfechaevper_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r2099_evtfechaevper.id)

    return r2099_evtfechaevper_dados