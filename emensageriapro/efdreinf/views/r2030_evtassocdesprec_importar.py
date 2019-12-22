# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r2030.models import *
from emensageriapro.functions import read_from_xml



def read_r2030_evtassocdesprec_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2030_evtassocdesprec_obj(request, doc, status, validar)
    return dados



def read_r2030_evtassocdesprec(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r2030_evtassocdesprec_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r2030evtAssocDespRec.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r2030_evtassocdesprec_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r2030_evtassocdesprec_dados = {}
    r2030_evtassocdesprec_dados['status'] = status
    r2030_evtassocdesprec_dados['arquivo_original'] = 1
    if arquivo:
        r2030_evtassocdesprec_dados['arquivo'] = arquivo.arquivo
    r2030_evtassocdesprec_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2030_evtassocdesprec_dados['identidade'] = doc.Reinf.evtAssocDespRec['id']
    evtAssocDespRec = doc.Reinf.evtAssocDespRec

    try:
        r2030_evtassocdesprec_dados['indretif'] = read_from_xml(evtAssocDespRec.ideEvento.indRetif.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2030_evtassocdesprec_dados['nrrecibo'] = read_from_xml(evtAssocDespRec.ideEvento.nrRecibo.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2030_evtassocdesprec_dados['perapur'] = read_from_xml(evtAssocDespRec.ideEvento.perApur.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2030_evtassocdesprec_dados['tpamb'] = read_from_xml(evtAssocDespRec.ideEvento.tpAmb.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2030_evtassocdesprec_dados['procemi'] = read_from_xml(evtAssocDespRec.ideEvento.procEmi.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2030_evtassocdesprec_dados['verproc'] = read_from_xml(evtAssocDespRec.ideEvento.verProc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2030_evtassocdesprec_dados['tpinsc'] = read_from_xml(evtAssocDespRec.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2030_evtassocdesprec_dados['nrinsc'] = read_from_xml(evtAssocDespRec.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2030_evtassocdesprec_dados['tpinscestab'] = read_from_xml(evtAssocDespRec.ideContri.ideEstab.tpInscEstab.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2030_evtassocdesprec_dados['nrinscestab'] = read_from_xml(evtAssocDespRec.ideContri.ideEstab.nrInscEstab.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    r2030_evtassocdesprec = r2030evtAssocDespRec.objects.create(**r2030_evtassocdesprec_dados)

    if 'ideContri' in dir(evtAssocDespRec) and 'ideEstab' in dir(evtAssocDespRec.ideContri) and 'recursosRec' in dir(evtAssocDespRec.ideContri.ideEstab):

        for recursosRec in evtAssocDespRec.ideContri.ideEstab.recursosRec:

            r2030_recursosrec_dados = {}
            r2030_recursosrec_dados['r2030_evtassocdesprec_id'] = r2030_evtassocdesprec.id

            try:
                r2030_recursosrec_dados['cnpjorigrecurso'] = read_from_xml(recursosRec.cnpjOrigRecurso.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2030_recursosrec_dados['vlrtotalrec'] = read_from_xml(recursosRec.vlrTotalRec.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            try:
                r2030_recursosrec_dados['vlrtotalret'] = read_from_xml(recursosRec.vlrTotalRet.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            try:
                r2030_recursosrec_dados['vlrtotalnret'] = read_from_xml(recursosRec.vlrTotalNRet.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            r2030_recursosrec = r2030recursosRec.objects.create(**r2030_recursosrec_dados)

            if 'infoRecurso' in dir(recursosRec):

                for infoRecurso in recursosRec.infoRecurso:

                    r2030_inforecurso_dados = {}
                    r2030_inforecurso_dados['r2030_recursosrec_id'] = r2030_recursosrec.id

                    try:
                        r2030_inforecurso_dados['tprepasse'] = read_from_xml(infoRecurso.tpRepasse.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r2030_inforecurso_dados['descrecurso'] = read_from_xml(infoRecurso.descRecurso.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r2030_inforecurso_dados['vlrbruto'] = read_from_xml(infoRecurso.vlrBruto.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2030_inforecurso_dados['vlrretapur'] = read_from_xml(infoRecurso.vlrRetApur.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r2030_inforecurso = r2030infoRecurso.objects.create(**r2030_inforecurso_dados)

            if 'infoProc' in dir(recursosRec):

                for infoProc in recursosRec.infoProc:

                    r2030_infoproc_dados = {}
                    r2030_infoproc_dados['r2030_recursosrec_id'] = r2030_recursosrec.id

                    try:
                        r2030_infoproc_dados['tpproc'] = read_from_xml(infoProc.tpProc.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r2030_infoproc_dados['nrproc'] = read_from_xml(infoProc.nrProc.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r2030_infoproc_dados['codsusp'] = read_from_xml(infoProc.codSusp.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r2030_infoproc_dados['vlrnret'] = read_from_xml(infoProc.vlrNRet.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r2030_infoproc = r2030infoProc.objects.create(**r2030_infoproc_dados)
    r2030_evtassocdesprec_dados['evento'] = 'r2030'
    r2030_evtassocdesprec_dados['id'] = r2030_evtassocdesprec.id
    r2030_evtassocdesprec_dados['identidade_evento'] = doc.Reinf.evtAssocDespRec['id']

    from emensageriapro.efdreinf.views.r2030_evtassocdesprec_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r2030_evtassocdesprec.id)

    return r2030_evtassocdesprec_dados