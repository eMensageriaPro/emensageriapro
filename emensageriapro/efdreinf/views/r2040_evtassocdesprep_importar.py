# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r2040.models import *
from emensageriapro.functions import read_from_xml



def read_r2040_evtassocdesprep_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2040_evtassocdesprep_obj(request, doc, status, validar)
    return dados



def read_r2040_evtassocdesprep(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r2040_evtassocdesprep_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r2040evtAssocDespRep.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r2040_evtassocdesprep_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r2040_evtassocdesprep_dados = {}
    r2040_evtassocdesprep_dados['status'] = status
    r2040_evtassocdesprep_dados['arquivo_original'] = 1
    if arquivo:
        r2040_evtassocdesprep_dados['arquivo'] = arquivo.arquivo
    r2040_evtassocdesprep_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2040_evtassocdesprep_dados['identidade'] = doc.Reinf.evtAssocDespRep['id']
    evtAssocDespRep = doc.Reinf.evtAssocDespRep

    try:
        r2040_evtassocdesprep_dados['indretif'] = read_from_xml(evtAssocDespRep.ideEvento.indRetif.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['nrrecibo'] = read_from_xml(evtAssocDespRep.ideEvento.nrRecibo.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['perapur'] = read_from_xml(evtAssocDespRep.ideEvento.perApur.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['tpamb'] = read_from_xml(evtAssocDespRep.ideEvento.tpAmb.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['procemi'] = read_from_xml(evtAssocDespRep.ideEvento.procEmi.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['verproc'] = read_from_xml(evtAssocDespRep.ideEvento.verProc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['tpinsc'] = read_from_xml(evtAssocDespRep.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['nrinsc'] = read_from_xml(evtAssocDespRep.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['tpinscestab'] = read_from_xml(evtAssocDespRep.ideContri.ideEstab.tpInscEstab.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['nrinscestab'] = read_from_xml(evtAssocDespRep.ideContri.ideEstab.nrInscEstab.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    r2040_evtassocdesprep = r2040evtAssocDespRep.objects.create(**r2040_evtassocdesprep_dados)

    if 'ideContri' in dir(evtAssocDespRep) and 'ideEstab' in dir(evtAssocDespRep.ideContri) and 'recursosRep' in dir(evtAssocDespRep.ideContri.ideEstab):

        for recursosRep in evtAssocDespRep.ideContri.ideEstab.recursosRep:

            r2040_recursosrep_dados = {}
            r2040_recursosrep_dados['r2040_evtassocdesprep_id'] = r2040_evtassocdesprep.id

            try:
                r2040_recursosrep_dados['cnpjassocdesp'] = read_from_xml(recursosRep.cnpjAssocDesp.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2040_recursosrep_dados['vlrtotalrep'] = read_from_xml(recursosRep.vlrTotalRep.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            try:
                r2040_recursosrep_dados['vlrtotalret'] = read_from_xml(recursosRep.vlrTotalRet.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            try:
                r2040_recursosrep_dados['vlrtotalnret'] = read_from_xml(recursosRep.vlrTotalNRet.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            r2040_recursosrep = r2040recursosRep.objects.create(**r2040_recursosrep_dados)

            if 'infoRecurso' in dir(recursosRep):

                for infoRecurso in recursosRep.infoRecurso:

                    r2040_inforecurso_dados = {}
                    r2040_inforecurso_dados['r2040_recursosrep_id'] = r2040_recursosrep.id

                    try:
                        r2040_inforecurso_dados['tprepasse'] = read_from_xml(infoRecurso.tpRepasse.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r2040_inforecurso_dados['descrecurso'] = read_from_xml(infoRecurso.descRecurso.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r2040_inforecurso_dados['vlrbruto'] = read_from_xml(infoRecurso.vlrBruto.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2040_inforecurso_dados['vlrretapur'] = read_from_xml(infoRecurso.vlrRetApur.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r2040_inforecurso = r2040infoRecurso.objects.create(**r2040_inforecurso_dados)

            if 'infoProc' in dir(recursosRep):

                for infoProc in recursosRep.infoProc:

                    r2040_infoproc_dados = {}
                    r2040_infoproc_dados['r2040_recursosrep_id'] = r2040_recursosrep.id

                    try:
                        r2040_infoproc_dados['tpproc'] = read_from_xml(infoProc.tpProc.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r2040_infoproc_dados['nrproc'] = read_from_xml(infoProc.nrProc.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r2040_infoproc_dados['codsusp'] = read_from_xml(infoProc.codSusp.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r2040_infoproc_dados['vlrnret'] = read_from_xml(infoProc.vlrNRet.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r2040_infoproc = r2040infoProc.objects.create(**r2040_infoproc_dados)
    r2040_evtassocdesprep_dados['evento'] = 'r2040'
    r2040_evtassocdesprep_dados['id'] = r2040_evtassocdesprep.id
    r2040_evtassocdesprep_dados['identidade_evento'] = doc.Reinf.evtAssocDespRep['id']

    from emensageriapro.efdreinf.views.r2040_evtassocdesprep_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r2040_evtassocdesprep.id)

    return r2040_evtassocdesprep_dados