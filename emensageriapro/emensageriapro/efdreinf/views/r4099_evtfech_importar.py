#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r4099.models import *
from emensageriapro.functions import read_from_xml



def read_r4099_evtfech_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r4099_evtfech_obj(request, doc, status, validar)
    return dados



def read_r4099_evtfech(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r4099_evtfech_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r4099evtFech.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r4099_evtfech_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r4099_evtfech_dados = {}
    r4099_evtfech_dados['status'] = status
    r4099_evtfech_dados['arquivo_original'] = 1
    if arquivo:
        r4099_evtfech_dados['arquivo'] = arquivo.arquivo
    r4099_evtfech_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r4099_evtfech_dados['identidade'] = doc.Reinf.evtFech['id']
    evtFech = doc.Reinf.evtFech

    try:
        r4099_evtfech_dados['perapur'] = read_from_xml(evtFech.ideEvento.perApur.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4099_evtfech_dados['tpamb'] = read_from_xml(evtFech.ideEvento.tpAmb.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4099_evtfech_dados['procemi'] = read_from_xml(evtFech.ideEvento.procEmi.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4099_evtfech_dados['verproc'] = read_from_xml(evtFech.ideEvento.verProc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4099_evtfech_dados['tpinsc'] = read_from_xml(evtFech.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4099_evtfech_dados['nrinsc'] = read_from_xml(evtFech.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4099_evtfech_dados['evtretpf'] = read_from_xml(evtFech.infoFech.evtRetPF.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4099_evtfech_dados['evtretpj'] = read_from_xml(evtFech.infoFech.evtRetPJ.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4099_evtfech_dados['evtpgtosnid'] = read_from_xml(evtFech.infoFech.evtPgtosNId.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    r4099_evtfech = r4099evtFech.objects.create(**r4099_evtfech_dados)

    if 'ideRespInf' in dir(evtFech):

        for ideRespInf in evtFech.ideRespInf:

            r4099_iderespinf_dados = {}
            r4099_iderespinf_dados['r4099_evtfech_id'] = r4099_evtfech.id

            try:
                r4099_iderespinf_dados['nmresp'] = read_from_xml(ideRespInf.nmResp.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r4099_iderespinf_dados['cpfresp'] = read_from_xml(ideRespInf.cpfResp.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r4099_iderespinf_dados['telefone'] = read_from_xml(ideRespInf.telefone.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r4099_iderespinf_dados['email'] = read_from_xml(ideRespInf.email.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r4099_iderespinf = r4099ideRespInf.objects.create(**r4099_iderespinf_dados)
    r4099_evtfech_dados['evento'] = 'r4099'
    r4099_evtfech_dados['id'] = r4099_evtfech.id
    r4099_evtfech_dados['identidade_evento'] = doc.Reinf.evtFech['id']

    from emensageriapro.efdreinf.views.r4099_evtfech_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r4099_evtfech.id)

    return r4099_evtfech_dados