#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2260.models import *
from emensageriapro.functions import read_from_xml



def read_s2260_evtconvinterm_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2260_evtconvinterm_obj(request, doc, status, validar)
    return dados



def read_s2260_evtconvinterm(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2260_evtconvinterm_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2260evtConvInterm.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2260_evtconvinterm_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2260_evtconvinterm_dados = {}
    s2260_evtconvinterm_dados['status'] = status
    s2260_evtconvinterm_dados['arquivo_original'] = 1
    if arquivo:
        s2260_evtconvinterm_dados['arquivo'] = arquivo.arquivo
    s2260_evtconvinterm_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2260_evtconvinterm_dados['identidade'] = doc.eSocial.evtConvInterm['Id']
    evtConvInterm = doc.eSocial.evtConvInterm

    try:
        s2260_evtconvinterm_dados['indretif'] = read_from_xml(evtConvInterm.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2260_evtconvinterm_dados['nrrecibo'] = read_from_xml(evtConvInterm.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2260_evtconvinterm_dados['tpamb'] = read_from_xml(evtConvInterm.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2260_evtconvinterm_dados['procemi'] = read_from_xml(evtConvInterm.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2260_evtconvinterm_dados['verproc'] = read_from_xml(evtConvInterm.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2260_evtconvinterm_dados['tpinsc'] = read_from_xml(evtConvInterm.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2260_evtconvinterm_dados['nrinsc'] = read_from_xml(evtConvInterm.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2260_evtconvinterm_dados['cpftrab'] = read_from_xml(evtConvInterm.ideVinculo.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2260_evtconvinterm_dados['nistrab'] = read_from_xml(evtConvInterm.ideVinculo.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2260_evtconvinterm_dados['matricula'] = read_from_xml(evtConvInterm.ideVinculo.matricula.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2260_evtconvinterm_dados['codconv'] = read_from_xml(evtConvInterm.infoConvInterm.codConv.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2260_evtconvinterm_dados['dtinicio'] = read_from_xml(evtConvInterm.infoConvInterm.dtInicio.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2260_evtconvinterm_dados['dtfim'] = read_from_xml(evtConvInterm.infoConvInterm.dtFim.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2260_evtconvinterm_dados['dtprevpgto'] = read_from_xml(evtConvInterm.infoConvInterm.dtPrevPgto.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2260_evtconvinterm_dados['codhorcontrat'] = read_from_xml(evtConvInterm.infoConvInterm.jornada.codHorContrat.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2260_evtconvinterm_dados['dscjornada'] = read_from_xml(evtConvInterm.infoConvInterm.jornada.dscJornada.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2260_evtconvinterm_dados['indlocal'] = read_from_xml(evtConvInterm.infoConvInterm.localTrab.indLocal.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    s2260_evtconvinterm = s2260evtConvInterm.objects.create(**s2260_evtconvinterm_dados)

    if 'infoConvInterm' in dir(evtConvInterm) and 'localTrab' in dir(evtConvInterm.infoConvInterm) and 'localTrabInterm' in dir(evtConvInterm.infoConvInterm.localTrab):

        for localTrabInterm in evtConvInterm.infoConvInterm.localTrab.localTrabInterm:

            s2260_localtrabinterm_dados = {}
            s2260_localtrabinterm_dados['s2260_evtconvinterm_id'] = s2260_evtconvinterm.id

            try:
                s2260_localtrabinterm_dados['tplograd'] = read_from_xml(localTrabInterm.tpLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2260_localtrabinterm_dados['dsclograd'] = read_from_xml(localTrabInterm.dscLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2260_localtrabinterm_dados['nrlograd'] = read_from_xml(localTrabInterm.nrLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2260_localtrabinterm_dados['complem'] = read_from_xml(localTrabInterm.complem.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2260_localtrabinterm_dados['bairro'] = read_from_xml(localTrabInterm.bairro.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2260_localtrabinterm_dados['cep'] = read_from_xml(localTrabInterm.cep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2260_localtrabinterm_dados['codmunic'] = read_from_xml(localTrabInterm.codMunic.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2260_localtrabinterm_dados['uf'] = read_from_xml(localTrabInterm.uf.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2260_localtrabinterm = s2260localTrabInterm.objects.create(**s2260_localtrabinterm_dados)
    s2260_evtconvinterm_dados['evento'] = 's2260'
    s2260_evtconvinterm_dados['id'] = s2260_evtconvinterm.id
    s2260_evtconvinterm_dados['identidade_evento'] = doc.eSocial.evtConvInterm['Id']

    from emensageriapro.esocial.views.s2260_evtconvinterm_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2260_evtconvinterm.id)

    return s2260_evtconvinterm_dados