#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r2040.models import *



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

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_r2040_evtassocdesprep_obj(request, doc, status, validar, arquivo)
    novo_arquivo = arquivo.replace('/aguardando/', '/processado/')
    r2040evtAssocDespRep.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_r2040_evtassocdesprep_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r2040_evtassocdesprep_dados = {}
    r2040_evtassocdesprep_dados['status'] = status
    r2040_evtassocdesprep_dados['arquivo_original'] = 1
    if arquivo:
        r2040_evtassocdesprep_dados['arquivo'] = arquivo
    r2040_evtassocdesprep_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2040_evtassocdesprep_dados['identidade'] = doc.Reinf.evtAssocDespRep['id']
    evtAssocDespRep = doc.Reinf.evtAssocDespRep

    try:
        r2040_evtassocdesprep_dados['indretif'] = evtAssocDespRep.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['nrrecibo'] = evtAssocDespRep.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['perapur'] = evtAssocDespRep.ideEvento.perApur.cdata
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['tpamb'] = evtAssocDespRep.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['procemi'] = evtAssocDespRep.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['verproc'] = evtAssocDespRep.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['tpinsc'] = evtAssocDespRep.ideContri.tpInsc.cdata
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['nrinsc'] = evtAssocDespRep.ideContri.nrInsc.cdata
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['tpinscestab'] = evtAssocDespRep.ideContri.ideEstab.tpInscEstab.cdata
    except AttributeError:
        pass

    try:
        r2040_evtassocdesprep_dados['nrinscestab'] = evtAssocDespRep.ideContri.ideEstab.nrInscEstab.cdata
    except AttributeError:
        pass

    r2040_evtassocdesprep = r2040evtAssocDespRep.objects.create(**r2040_evtassocdesprep_dados)

    if 'ideContri' in dir(evtAssocDespRep) and 'ideEstab' in dir(evtAssocDespRep.ideContri) and 'recursosRep' in dir(evtAssocDespRep.ideContri.ideEstab):

        for recursosRep in evtAssocDespRep.ideContri.ideEstab.recursosRep:

            r2040_recursosrep_dados = {}
            r2040_recursosrep_dados['r2040_evtassocdesprep_id'] = r2040_evtassocdesprep.id

            try:
                r2040_recursosrep_dados['cnpjassocdesp'] = recursosRep.cnpjAssocDesp.cdata
            except AttributeError:
                pass

            try:
                r2040_recursosrep_dados['vlrtotalrep'] = recursosRep.vlrTotalRep.cdata.replace('.', '').replace(',', '.')
            except AttributeError:
                pass

            try:
                r2040_recursosrep_dados['vlrtotalret'] = recursosRep.vlrTotalRet.cdata.replace('.', '').replace(',', '.')
            except AttributeError:
                pass

            try:
                r2040_recursosrep_dados['vlrtotalnret'] = recursosRep.vlrTotalNRet.cdata.replace('.', '').replace(',', '.')
            except AttributeError:
                pass

            r2040_recursosrep = r2040recursosRep.objects.create(**r2040_recursosrep_dados)

            if 'infoRecurso' in dir(recursosRep):

                for infoRecurso in recursosRep.infoRecurso:

                    r2040_inforecurso_dados = {}
                    r2040_inforecurso_dados['r2040_recursosrep_id'] = r2040_recursosrep.id

                    try:
                        r2040_inforecurso_dados['tprepasse'] = infoRecurso.tpRepasse.cdata
                    except AttributeError:
                        pass

                    try:
                        r2040_inforecurso_dados['descrecurso'] = infoRecurso.descRecurso.cdata
                    except AttributeError:
                        pass

                    try:
                        r2040_inforecurso_dados['vlrbruto'] = infoRecurso.vlrBruto.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r2040_inforecurso_dados['vlrretapur'] = infoRecurso.vlrRetApur.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    r2040_inforecurso = r2040infoRecurso.objects.create(**r2040_inforecurso_dados)

            if 'infoProc' in dir(recursosRep):

                for infoProc in recursosRep.infoProc:

                    r2040_infoproc_dados = {}
                    r2040_infoproc_dados['r2040_recursosrep_id'] = r2040_recursosrep.id

                    try:
                        r2040_infoproc_dados['tpproc'] = infoProc.tpProc.cdata
                    except AttributeError:
                        pass

                    try:
                        r2040_infoproc_dados['nrproc'] = infoProc.nrProc.cdata
                    except AttributeError:
                        pass

                    try:
                        r2040_infoproc_dados['codsusp'] = infoProc.codSusp.cdata
                    except AttributeError:
                        pass

                    try:
                        r2040_infoproc_dados['vlrnret'] = infoProc.vlrNRet.cdata.replace('.', '').replace(',', '.')
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