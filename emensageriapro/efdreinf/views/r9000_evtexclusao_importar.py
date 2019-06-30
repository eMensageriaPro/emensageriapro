#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r9000.models import *
from emensageriapro.functions import read_from_xml



def read_r9000_evtexclusao_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r9000_evtexclusao_obj(request, doc, status, validar)
    return dados



def read_r9000_evtexclusao(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r9000_evtexclusao_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r9000evtExclusao.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r9000_evtexclusao_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r9000_evtexclusao_dados = {}
    r9000_evtexclusao_dados['status'] = status
    r9000_evtexclusao_dados['arquivo_original'] = 1
    if arquivo:
        r9000_evtexclusao_dados['arquivo'] = arquivo.arquivo
    r9000_evtexclusao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r9000_evtexclusao_dados['identidade'] = doc.Reinf.evtExclusao['id']
    evtExclusao = doc.Reinf.evtExclusao

    try:
        r9000_evtexclusao_dados['tpamb'] = read_from_xml(evtExclusao.ideEvento.tpAmb.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r9000_evtexclusao_dados['procemi'] = read_from_xml(evtExclusao.ideEvento.procEmi.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r9000_evtexclusao_dados['verproc'] = read_from_xml(evtExclusao.ideEvento.verProc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9000_evtexclusao_dados['tpinsc'] = read_from_xml(evtExclusao.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r9000_evtexclusao_dados['nrinsc'] = read_from_xml(evtExclusao.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9000_evtexclusao_dados['tpevento'] = read_from_xml(evtExclusao.infoExclusao.tpEvento.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9000_evtexclusao_dados['nrrecevt'] = read_from_xml(evtExclusao.infoExclusao.nrRecEvt.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9000_evtexclusao_dados['perapur'] = read_from_xml(evtExclusao.infoExclusao.perApur.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    r9000_evtexclusao = r9000evtExclusao.objects.create(**r9000_evtexclusao_dados)
    r9000_evtexclusao_dados['evento'] = 'r9000'
    r9000_evtexclusao_dados['id'] = r9000_evtexclusao.id
    r9000_evtexclusao_dados['identidade_evento'] = doc.Reinf.evtExclusao['id']

    from emensageriapro.efdreinf.views.r9000_evtexclusao_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r9000_evtexclusao.id)

    return r9000_evtexclusao_dados