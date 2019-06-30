#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s3000.models import *
from emensageriapro.functions import read_from_xml



def read_s3000_evtexclusao_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s3000_evtexclusao_obj(request, doc, status, validar)
    return dados



def read_s3000_evtexclusao(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s3000_evtexclusao_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s3000evtExclusao.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s3000_evtexclusao_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s3000_evtexclusao_dados = {}
    s3000_evtexclusao_dados['status'] = status
    s3000_evtexclusao_dados['arquivo_original'] = 1
    if arquivo:
        s3000_evtexclusao_dados['arquivo'] = arquivo.arquivo
    s3000_evtexclusao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s3000_evtexclusao_dados['identidade'] = doc.eSocial.evtExclusao['Id']
    evtExclusao = doc.eSocial.evtExclusao

    try:
        s3000_evtexclusao_dados['tpamb'] = read_from_xml(evtExclusao.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s3000_evtexclusao_dados['procemi'] = read_from_xml(evtExclusao.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s3000_evtexclusao_dados['verproc'] = read_from_xml(evtExclusao.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s3000_evtexclusao_dados['tpinsc'] = read_from_xml(evtExclusao.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s3000_evtexclusao_dados['nrinsc'] = read_from_xml(evtExclusao.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s3000_evtexclusao_dados['tpevento'] = read_from_xml(evtExclusao.infoExclusao.tpEvento.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s3000_evtexclusao_dados['nrrecevt'] = read_from_xml(evtExclusao.infoExclusao.nrRecEvt.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s3000_evtexclusao = s3000evtExclusao.objects.create(**s3000_evtexclusao_dados)

    if 'infoExclusao' in dir(evtExclusao) and 'ideTrabalhador' in dir(evtExclusao.infoExclusao):

        for ideTrabalhador in evtExclusao.infoExclusao.ideTrabalhador:

            s3000_idetrabalhador_dados = {}
            s3000_idetrabalhador_dados['s3000_evtexclusao_id'] = s3000_evtexclusao.id

            try:
                s3000_idetrabalhador_dados['cpftrab'] = read_from_xml(ideTrabalhador.cpfTrab.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s3000_idetrabalhador_dados['nistrab'] = read_from_xml(ideTrabalhador.nisTrab.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s3000_idetrabalhador = s3000ideTrabalhador.objects.create(**s3000_idetrabalhador_dados)

    if 'infoExclusao' in dir(evtExclusao) and 'ideFolhaPagto' in dir(evtExclusao.infoExclusao):

        for ideFolhaPagto in evtExclusao.infoExclusao.ideFolhaPagto:

            s3000_idefolhapagto_dados = {}
            s3000_idefolhapagto_dados['s3000_evtexclusao_id'] = s3000_evtexclusao.id

            try:
                s3000_idefolhapagto_dados['indapuracao'] = read_from_xml(ideFolhaPagto.indApuracao.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s3000_idefolhapagto_dados['perapur'] = read_from_xml(ideFolhaPagto.perApur.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s3000_idefolhapagto = s3000ideFolhaPagto.objects.create(**s3000_idefolhapagto_dados)
    s3000_evtexclusao_dados['evento'] = 's3000'
    s3000_evtexclusao_dados['id'] = s3000_evtexclusao.id
    s3000_evtexclusao_dados['identidade_evento'] = doc.eSocial.evtExclusao['Id']

    from emensageriapro.esocial.views.s3000_evtexclusao_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s3000_evtexclusao.id)

    return s3000_evtexclusao_dados