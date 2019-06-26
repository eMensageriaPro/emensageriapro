#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r2050.models import *



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

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_r2050_evtcomprod_obj(request, doc, status, validar, arquivo)
    novo_arquivo = arquivo.replace('/aguardando/', '/processado/')
    r2050evtComProd.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_r2050_evtcomprod_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r2050_evtcomprod_dados = {}
    r2050_evtcomprod_dados['status'] = status
    r2050_evtcomprod_dados['arquivo_original'] = 1
    if arquivo:
        r2050_evtcomprod_dados['arquivo'] = arquivo
    r2050_evtcomprod_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2050_evtcomprod_dados['identidade'] = doc.Reinf.evtComProd['id']
    evtComProd = doc.Reinf.evtComProd

    try:
        r2050_evtcomprod_dados['indretif'] = evtComProd.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['nrrecibo'] = evtComProd.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['perapur'] = evtComProd.ideEvento.perApur.cdata
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['tpamb'] = evtComProd.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['procemi'] = evtComProd.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['verproc'] = evtComProd.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['tpinsc'] = evtComProd.ideContri.tpInsc.cdata
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['nrinsc'] = evtComProd.ideContri.nrInsc.cdata
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['tpinscestab'] = evtComProd.infoComProd.ideEstab.tpInscEstab.cdata
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['nrinscestab'] = evtComProd.infoComProd.ideEstab.nrInscEstab.cdata
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['vlrrecbrutatotal'] = evtComProd.infoComProd.ideEstab.vlrRecBrutaTotal.cdata.replace('.', '').replace(',', '.')
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['vlrcpapur'] = evtComProd.infoComProd.ideEstab.vlrCPApur.cdata.replace('.', '').replace(',', '.')
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['vlrratapur'] = evtComProd.infoComProd.ideEstab.vlrRatApur.cdata.replace('.', '').replace(',', '.')
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['vlrsenarapur'] = evtComProd.infoComProd.ideEstab.vlrSenarApur.cdata.replace('.', '').replace(',', '.')
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['vlrcpsusptotal'] = evtComProd.infoComProd.ideEstab.vlrCPSuspTotal.cdata.replace('.', '').replace(',', '.')
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['vlrratsusptotal'] = evtComProd.infoComProd.ideEstab.vlrRatSuspTotal.cdata.replace('.', '').replace(',', '.')
    except AttributeError:
        pass

    try:
        r2050_evtcomprod_dados['vlrsenarsusptotal'] = evtComProd.infoComProd.ideEstab.vlrSenarSuspTotal.cdata.replace('.', '').replace(',', '.')
    except AttributeError:
        pass

    r2050_evtcomprod = r2050evtComProd.objects.create(**r2050_evtcomprod_dados)

    if 'infoComProd' in dir(evtComProd) and 'ideEstab' in dir(evtComProd.infoComProd) and 'tipoCom' in dir(evtComProd.infoComProd.ideEstab):

        for tipoCom in evtComProd.infoComProd.ideEstab.tipoCom:

            r2050_tipocom_dados = {}
            r2050_tipocom_dados['r2050_evtcomprod_id'] = r2050_evtcomprod.id

            try:
                r2050_tipocom_dados['indcom'] = tipoCom.indCom.cdata
            except AttributeError:
                pass

            try:
                r2050_tipocom_dados['vlrrecbruta'] = tipoCom.vlrRecBruta.cdata.replace('.', '').replace(',', '.')
            except AttributeError:
                pass

            r2050_tipocom = r2050tipoCom.objects.create(**r2050_tipocom_dados)

            if 'infoProc' in dir(tipoCom):

                for infoProc in tipoCom.infoProc:

                    r2050_infoproc_dados = {}
                    r2050_infoproc_dados['r2050_tipocom_id'] = r2050_tipocom.id

                    try:
                        r2050_infoproc_dados['tpproc'] = infoProc.tpProc.cdata
                    except AttributeError:
                        pass

                    try:
                        r2050_infoproc_dados['nrproc'] = infoProc.nrProc.cdata
                    except AttributeError:
                        pass

                    try:
                        r2050_infoproc_dados['codsusp'] = infoProc.codSusp.cdata
                    except AttributeError:
                        pass

                    try:
                        r2050_infoproc_dados['vlrcpsusp'] = infoProc.vlrCPSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r2050_infoproc_dados['vlrratsusp'] = infoProc.vlrRatSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r2050_infoproc_dados['vlrsenarsusp'] = infoProc.vlrSenarSusp.cdata.replace('.', '').replace(',', '.')
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