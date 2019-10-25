#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r9002.models import *
from emensageriapro.functions import read_from_xml



def read_r9002_evtret_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r9002_evtret_obj(request, doc, status, validar)
    return dados



def read_r9002_evtret(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r9002_evtret_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r9002evtRet.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r9002_evtret_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r9002_evtret_dados = {}
    r9002_evtret_dados['status'] = status
    r9002_evtret_dados['arquivo_original'] = 1
    if arquivo:
        r9002_evtret_dados['arquivo'] = arquivo.arquivo
    r9002_evtret_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r9002_evtret_dados['identidade'] = doc.Reinf.evtRet['id']
    evtRet = doc.Reinf.evtRet

    try:
        r9002_evtret_dados['perref'] = read_from_xml(evtRet.ideEvento.perRef.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['tpinsc'] = read_from_xml(evtRet.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['nrinsc'] = read_from_xml(evtRet.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['cdretorno'] = read_from_xml(evtRet.ideRecRetorno.ideStatus.cdRetorno.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['descretorno'] = read_from_xml(evtRet.ideRecRetorno.ideStatus.descRetorno.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['nrprotentr'] = read_from_xml(evtRet.infoRecEv.nrProtEntr.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['dhprocess'] = read_from_xml(evtRet.infoRecEv.dhProcess.cdata, 'efdreinf', 'D', None)
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['tpev'] = read_from_xml(evtRet.infoRecEv.tpEv.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['idev'] = read_from_xml(evtRet.infoRecEv.idEv.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['hash'] = read_from_xml(evtRet.infoRecEv.hash.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    r9002_evtret = r9002evtRet.objects.create(**r9002_evtret_dados)

    if 'ideRecRetorno' in dir(evtRet) and 'ideStatus' in dir(evtRet.ideRecRetorno) and 'regOcorrs' in dir(evtRet.ideRecRetorno.ideStatus):

        for regOcorrs in evtRet.ideRecRetorno.ideStatus.regOcorrs:

            r9002_regocorrs_dados = {}
            r9002_regocorrs_dados['r9002_evtret_id'] = r9002_evtret.id

            try:
                r9002_regocorrs_dados['tpocorr'] = read_from_xml(regOcorrs.tpOcorr.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r9002_regocorrs_dados['localerroaviso'] = read_from_xml(regOcorrs.localErroAviso.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r9002_regocorrs_dados['codresp'] = read_from_xml(regOcorrs.codResp.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r9002_regocorrs_dados['dscresp'] = read_from_xml(regOcorrs.dscResp.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r9002_regocorrs = r9002regOcorrs.objects.create(**r9002_regocorrs_dados)

    if 'infoTotal' in dir(evtRet):

        for infoTotal in evtRet.infoTotal:

            r9002_infototal_dados = {}
            r9002_infototal_dados['r9002_evtret_id'] = r9002_evtret.id

            try:
                r9002_infototal_dados['nrrecarqbase'] = read_from_xml(infoTotal.nrRecArqBase.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r9002_infototal_dados['tpinsc'] = read_from_xml(infoTotal.ideEstab.tpInsc.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r9002_infototal_dados['nrinsc'] = read_from_xml(infoTotal.ideEstab.nrInsc.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r9002_infototal = r9002infoTotal.objects.create(**r9002_infototal_dados)

            if 'ideEstab' in dir(infoTotal) and 'totApurMen' in dir(infoTotal.ideEstab):

                for totApurMen in infoTotal.ideEstab.totApurMen:

                    r9002_totapurmen_dados = {}
                    r9002_totapurmen_dados['r9002_infototal_id'] = r9002_infototal.id

                    try:
                        r9002_totapurmen_dados['crmen'] = read_from_xml(totApurMen.CRMen.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurmen_dados['vlrbasecrmen'] = read_from_xml(totApurMen.vlrBaseCRMen.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurmen_dados['vlrcrmen'] = read_from_xml(totApurMen.vlrCRMen.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurmen_dados['vlrbasecrmensusp'] = read_from_xml(totApurMen.vlrBaseCRMenSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurmen_dados['vlrcrmensusp'] = read_from_xml(totApurMen.vlrCRMenSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r9002_totapurmen = r9002totApurMen.objects.create(**r9002_totapurmen_dados)

            if 'ideEstab' in dir(infoTotal) and 'totApurQui' in dir(infoTotal.ideEstab):

                for totApurQui in infoTotal.ideEstab.totApurQui:

                    r9002_totapurqui_dados = {}
                    r9002_totapurqui_dados['r9002_infototal_id'] = r9002_infototal.id

                    try:
                        r9002_totapurqui_dados['perapurqui'] = read_from_xml(totApurQui.perApurQui.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurqui_dados['crqui'] = read_from_xml(totApurQui.CRQui.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurqui_dados['vlrbasecrqui'] = read_from_xml(totApurQui.vlrBaseCRQui.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurqui_dados['vlrcrqui'] = read_from_xml(totApurQui.vlrCRQui.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurqui_dados['vlrbasecrquisusp'] = read_from_xml(totApurQui.vlrBaseCRQuiSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurqui_dados['vlrcrquisusp'] = read_from_xml(totApurQui.vlrCRQuiSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r9002_totapurqui = r9002totApurQui.objects.create(**r9002_totapurqui_dados)

            if 'ideEstab' in dir(infoTotal) and 'totApurDec' in dir(infoTotal.ideEstab):

                for totApurDec in infoTotal.ideEstab.totApurDec:

                    r9002_totapurdec_dados = {}
                    r9002_totapurdec_dados['r9002_infototal_id'] = r9002_infototal.id

                    try:
                        r9002_totapurdec_dados['perapurdec'] = read_from_xml(totApurDec.perApurDec.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdec_dados['crdec'] = read_from_xml(totApurDec.CRDec.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdec_dados['vlrbasecrdec'] = read_from_xml(totApurDec.vlrBaseCRDec.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdec_dados['vlrcrdec'] = read_from_xml(totApurDec.vlrCRDec.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdec_dados['vlrbasecrdecsusp'] = read_from_xml(totApurDec.vlrBaseCRDecSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdec_dados['vlrcrdecsusp'] = read_from_xml(totApurDec.vlrCRDecSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r9002_totapurdec = r9002totApurDec.objects.create(**r9002_totapurdec_dados)

            if 'ideEstab' in dir(infoTotal) and 'totApurSem' in dir(infoTotal.ideEstab):

                for totApurSem in infoTotal.ideEstab.totApurSem:

                    r9002_totapursem_dados = {}
                    r9002_totapursem_dados['r9002_infototal_id'] = r9002_infototal.id

                    try:
                        r9002_totapursem_dados['perapursem'] = read_from_xml(totApurSem.perApurSem.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapursem_dados['crsem'] = read_from_xml(totApurSem.CRSem.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapursem_dados['vlrbasecrsem'] = read_from_xml(totApurSem.vlrBaseCRSem.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapursem_dados['vlrcrsem'] = read_from_xml(totApurSem.vlrCRSem.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapursem_dados['vlrbasecrsemsusp'] = read_from_xml(totApurSem.vlrBaseCRSemSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapursem_dados['vlrcrsemsusp'] = read_from_xml(totApurSem.vlrCRSemSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r9002_totapursem = r9002totApurSem.objects.create(**r9002_totapursem_dados)

            if 'ideEstab' in dir(infoTotal) and 'totApurDia' in dir(infoTotal.ideEstab):

                for totApurDia in infoTotal.ideEstab.totApurDia:

                    r9002_totapurdia_dados = {}
                    r9002_totapurdia_dados['r9002_infototal_id'] = r9002_infototal.id

                    try:
                        r9002_totapurdia_dados['perapurdia'] = read_from_xml(totApurDia.perApurDia.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdia_dados['crdia'] = read_from_xml(totApurDia.CRDia.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdia_dados['vlrbasecrdia'] = read_from_xml(totApurDia.vlrBaseCRDia.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdia_dados['vlrcrdia'] = read_from_xml(totApurDia.vlrCRDia.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdia_dados['vlrbasecrdiasusp'] = read_from_xml(totApurDia.vlrBaseCRDiaSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdia_dados['vlrcrdiasusp'] = read_from_xml(totApurDia.vlrCRDiaSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r9002_totapurdia = r9002totApurDia.objects.create(**r9002_totapurdia_dados)
    r9002_evtret_dados['evento'] = 'r9002'
    r9002_evtret_dados['id'] = r9002_evtret.id
    r9002_evtret_dados['identidade_evento'] = doc.Reinf.evtRet['id']

    from emensageriapro.efdreinf.views.r9002_evtret_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r9002_evtret.id)

    return r9002_evtret_dados