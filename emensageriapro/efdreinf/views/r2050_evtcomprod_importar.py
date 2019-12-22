# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r2050.models import *
from emensageriapro.functions import read_from_xml



def read_r2050_evtcomprod_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2050_evtcomprod_obj(request, doc, status, validar)
    return dados



def read_r2050_evtcomprod(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r2050_evtcomprod_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r2050evtComProd.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r2050_evtcomprod_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r2050_evtcomprod_dados = {}
    r2050_evtcomprod_dados['status'] = status
    r2050_evtcomprod_dados['arquivo_original'] = 1
    if arquivo:
        r2050_evtcomprod_dados['arquivo'] = arquivo.arquivo
    r2050_evtcomprod_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2050_evtcomprod_dados['identidade'] = doc.Reinf.evtComProd['id']
    evtComProd = doc.Reinf.evtComProd

    try:
        r2050_evtcomprod_dados['indretif'] = read_from_xml(evtComProd.ideEvento.indRetif.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['nrrecibo'] = read_from_xml(evtComProd.ideEvento.nrRecibo.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['perapur'] = read_from_xml(evtComProd.ideEvento.perApur.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['tpamb'] = read_from_xml(evtComProd.ideEvento.tpAmb.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['procemi'] = read_from_xml(evtComProd.ideEvento.procEmi.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['verproc'] = read_from_xml(evtComProd.ideEvento.verProc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['tpinsc'] = read_from_xml(evtComProd.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['nrinsc'] = read_from_xml(evtComProd.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['tpinscestab'] = read_from_xml(evtComProd.infoComProd.ideEstab.tpInscEstab.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['nrinscestab'] = read_from_xml(evtComProd.infoComProd.ideEstab.nrInscEstab.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['vlrrecbrutatotal'] = read_from_xml(evtComProd.infoComProd.ideEstab.vlrRecBrutaTotal.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['vlrcpapur'] = read_from_xml(evtComProd.infoComProd.ideEstab.vlrCPApur.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['vlrratapur'] = read_from_xml(evtComProd.infoComProd.ideEstab.vlrRatApur.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['vlrsenarapur'] = read_from_xml(evtComProd.infoComProd.ideEstab.vlrSenarApur.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['vlrcpsusptotal'] = read_from_xml(evtComProd.infoComProd.ideEstab.vlrCPSuspTotal.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['vlrratsusptotal'] = read_from_xml(evtComProd.infoComProd.ideEstab.vlrRatSuspTotal.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['vlrsenarsusptotal'] = read_from_xml(evtComProd.infoComProd.ideEstab.vlrSenarSuspTotal.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    r2050_evtcomprod = r2050evtComProd.objects.create(**r2050_evtcomprod_dados)

    if 'infoComProd' in dir(evtComProd) and 'ideEstab' in dir(evtComProd.infoComProd) and 'tipoCom' in dir(evtComProd.infoComProd.ideEstab):

        for tipoCom in evtComProd.infoComProd.ideEstab.tipoCom:

            r2050_tipocom_dados = {}
            r2050_tipocom_dados['r2050_evtcomprod_id'] = r2050_evtcomprod.id

            try:
                r2050_tipocom_dados['indcom'] = read_from_xml(tipoCom.indCom.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r2050_tipocom_dados['vlrrecbruta'] = read_from_xml(tipoCom.vlrRecBruta.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            r2050_tipocom = r2050tipoCom.objects.create(**r2050_tipocom_dados)

            if 'infoProc' in dir(tipoCom):

                for infoProc in tipoCom.infoProc:

                    r2050_infoproc_dados = {}
                    r2050_infoproc_dados['r2050_tipocom_id'] = r2050_tipocom.id

                    try:
                        r2050_infoproc_dados['tpproc'] = read_from_xml(infoProc.tpProc.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r2050_infoproc_dados['nrproc'] = read_from_xml(infoProc.nrProc.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r2050_infoproc_dados['codsusp'] = read_from_xml(infoProc.codSusp.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r2050_infoproc_dados['vlrcpsusp'] = read_from_xml(infoProc.vlrCPSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2050_infoproc_dados['vlrratsusp'] = read_from_xml(infoProc.vlrRatSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2050_infoproc_dados['vlrsenarsusp'] = read_from_xml(infoProc.vlrSenarSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r2050_infoproc = r2050infoProc.objects.create(**r2050_infoproc_dados)
    r2050_evtcomprod_dados['evento'] = 'r2050'
    r2050_evtcomprod_dados['id'] = r2050_evtcomprod.id
    r2050_evtcomprod_dados['identidade_evento'] = doc.Reinf.evtComProd['id']

    from emensageriapro.efdreinf.views.r2050_evtcomprod_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r2050_evtcomprod.id)

    return r2050_evtcomprod_dados