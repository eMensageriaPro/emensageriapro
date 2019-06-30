#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r2060.models import *
from emensageriapro.functions import read_from_xml



def read_r2060_evtcprb_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2060_evtcprb_obj(request, doc, status, validar)
    return dados



def read_r2060_evtcprb(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r2060_evtcprb_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r2060evtCPRB.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r2060_evtcprb_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r2060_evtcprb_dados = {}
    r2060_evtcprb_dados['status'] = status
    r2060_evtcprb_dados['arquivo_original'] = 1
    if arquivo:
        r2060_evtcprb_dados['arquivo'] = arquivo.arquivo
    r2060_evtcprb_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2060_evtcprb_dados['identidade'] = doc.Reinf.evtCPRB['id']
    evtCPRB = doc.Reinf.evtCPRB

    try:
        r2060_evtcprb_dados['indretif'] = read_from_xml(evtCPRB.ideEvento.indRetif.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2060_evtcprb_dados['nrrecibo'] = read_from_xml(evtCPRB.ideEvento.nrRecibo.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2060_evtcprb_dados['perapur'] = read_from_xml(evtCPRB.ideEvento.perApur.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2060_evtcprb_dados['tpamb'] = read_from_xml(evtCPRB.ideEvento.tpAmb.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2060_evtcprb_dados['procemi'] = read_from_xml(evtCPRB.ideEvento.procEmi.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2060_evtcprb_dados['verproc'] = read_from_xml(evtCPRB.ideEvento.verProc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2060_evtcprb_dados['tpinsc'] = read_from_xml(evtCPRB.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2060_evtcprb_dados['nrinsc'] = read_from_xml(evtCPRB.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2060_evtcprb_dados['tpinscestab'] = read_from_xml(evtCPRB.infoCPRB.ideEstab.tpInscEstab.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2060_evtcprb_dados['nrinscestab'] = read_from_xml(evtCPRB.infoCPRB.ideEstab.nrInscEstab.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2060_evtcprb_dados['vlrrecbrutatotal'] = read_from_xml(evtCPRB.infoCPRB.ideEstab.vlrRecBrutaTotal.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2060_evtcprb_dados['vlrcpapurtotal'] = read_from_xml(evtCPRB.infoCPRB.ideEstab.vlrCPApurTotal.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2060_evtcprb_dados['vlrcprbsusptotal'] = read_from_xml(evtCPRB.infoCPRB.ideEstab.vlrCPRBSuspTotal.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    r2060_evtcprb = r2060evtCPRB.objects.create(**r2060_evtcprb_dados)

    if 'infoCPRB' in dir(evtCPRB) and 'ideEstab' in dir(evtCPRB.infoCPRB) and 'tipoCod' in dir(evtCPRB.infoCPRB.ideEstab):

        for tipoCod in evtCPRB.infoCPRB.ideEstab.tipoCod:

            r2060_tipocod_dados = {}
            r2060_tipocod_dados['r2060_evtcprb_id'] = r2060_evtcprb.id

            try:
                r2060_tipocod_dados['codativecon'] = read_from_xml(tipoCod.codAtivEcon.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2060_tipocod_dados['vlrrecbrutaativ'] = read_from_xml(tipoCod.vlrRecBrutaAtiv.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            try:
                r2060_tipocod_dados['vlrexcrecbruta'] = read_from_xml(tipoCod.vlrExcRecBruta.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            try:
                r2060_tipocod_dados['vlradicrecbruta'] = read_from_xml(tipoCod.vlrAdicRecBruta.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            try:
                r2060_tipocod_dados['vlrbccprb'] = read_from_xml(tipoCod.vlrBcCPRB.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            try:
                r2060_tipocod_dados['vlrcprbapur'] = read_from_xml(tipoCod.vlrCPRBapur.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            try:
                r2060_tipocod_dados['observ'] = read_from_xml(tipoCod.observ.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r2060_tipocod = r2060tipoCod.objects.create(**r2060_tipocod_dados)

            if 'tipoAjuste' in dir(tipoCod):

                for tipoAjuste in tipoCod.tipoAjuste:

                    r2060_tipoajuste_dados = {}
                    r2060_tipoajuste_dados['r2060_tipocod_id'] = r2060_tipocod.id

                    try:
                        r2060_tipoajuste_dados['tpajuste'] = read_from_xml(tipoAjuste.tpAjuste.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r2060_tipoajuste_dados['codajuste'] = read_from_xml(tipoAjuste.codAjuste.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r2060_tipoajuste_dados['vlrajuste'] = read_from_xml(tipoAjuste.vlrAjuste.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2060_tipoajuste_dados['descajuste'] = read_from_xml(tipoAjuste.descAjuste.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r2060_tipoajuste_dados['dtajuste'] = read_from_xml(tipoAjuste.dtAjuste.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    r2060_tipoajuste = r2060tipoAjuste.objects.create(**r2060_tipoajuste_dados)

            if 'infoProc' in dir(tipoCod):

                for infoProc in tipoCod.infoProc:

                    r2060_infoproc_dados = {}
                    r2060_infoproc_dados['r2060_tipocod_id'] = r2060_tipocod.id

                    try:
                        r2060_infoproc_dados['tpproc'] = read_from_xml(infoProc.tpProc.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r2060_infoproc_dados['nrproc'] = read_from_xml(infoProc.nrProc.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r2060_infoproc_dados['codsusp'] = read_from_xml(infoProc.codSusp.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r2060_infoproc_dados['vlrcprbsusp'] = read_from_xml(infoProc.vlrCPRBSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r2060_infoproc = r2060infoProc.objects.create(**r2060_infoproc_dados)
    r2060_evtcprb_dados['evento'] = 'r2060'
    r2060_evtcprb_dados['id'] = r2060_evtcprb.id
    r2060_evtcprb_dados['identidade_evento'] = doc.Reinf.evtCPRB['id']

    from emensageriapro.efdreinf.views.r2060_evtcprb_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r2060_evtcprb.id)

    return r2060_evtcprb_dados