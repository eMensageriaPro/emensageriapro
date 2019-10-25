#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r9012.models import *
from emensageriapro.functions import read_from_xml



def read_r9012_evtretcons_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r9012_evtretcons_obj(request, doc, status, validar)
    return dados



def read_r9012_evtretcons(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r9012_evtretcons_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r9012evtRetCons.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r9012_evtretcons_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r9012_evtretcons_dados = {}
    r9012_evtretcons_dados['status'] = status
    r9012_evtretcons_dados['arquivo_original'] = 1
    if arquivo:
        r9012_evtretcons_dados['arquivo'] = arquivo.arquivo
    r9012_evtretcons_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r9012_evtretcons_dados['identidade'] = doc.Reinf.evtRetCons['id']
    evtRetCons = doc.Reinf.evtRetCons

    try:
        r9012_evtretcons_dados['perapur'] = read_from_xml(evtRetCons.ideEvento.perApur.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9012_evtretcons_dados['tpinsc'] = read_from_xml(evtRetCons.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r9012_evtretcons_dados['nrinsc'] = read_from_xml(evtRetCons.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9012_evtretcons_dados['cdretorno'] = read_from_xml(evtRetCons.ideRecRetorno.ideStatus.cdRetorno.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r9012_evtretcons_dados['descretorno'] = read_from_xml(evtRetCons.ideRecRetorno.ideStatus.descRetorno.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9012_evtretcons_dados['nrprotentr'] = read_from_xml(evtRetCons.infoRecEv.nrProtEntr.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9012_evtretcons_dados['dhprocess'] = read_from_xml(evtRetCons.infoRecEv.dhProcess.cdata, 'efdreinf', 'D', None)
    except AttributeError:
        pass

    try:
        r9012_evtretcons_dados['tpev'] = read_from_xml(evtRetCons.infoRecEv.tpEv.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9012_evtretcons_dados['idev'] = read_from_xml(evtRetCons.infoRecEv.idEv.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9012_evtretcons_dados['hash'] = read_from_xml(evtRetCons.infoRecEv.hash.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    r9012_evtretcons = r9012evtRetCons.objects.create(**r9012_evtretcons_dados)

    if 'ideRecRetorno' in dir(evtRetCons) and 'ideStatus' in dir(evtRetCons.ideRecRetorno) and 'regOcorrs' in dir(evtRetCons.ideRecRetorno.ideStatus):

        for regOcorrs in evtRetCons.ideRecRetorno.ideStatus.regOcorrs:

            r9012_regocorrs_dados = {}
            r9012_regocorrs_dados['r9012_evtretcons_id'] = r9012_evtretcons.id

            try:
                r9012_regocorrs_dados['tpocorr'] = read_from_xml(regOcorrs.tpOcorr.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r9012_regocorrs_dados['localerroaviso'] = read_from_xml(regOcorrs.localErroAviso.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r9012_regocorrs_dados['codresp'] = read_from_xml(regOcorrs.codResp.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r9012_regocorrs_dados['dscresp'] = read_from_xml(regOcorrs.dscResp.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r9012_regocorrs = r9012regOcorrs.objects.create(**r9012_regocorrs_dados)

    if 'infoTotalContrib' in dir(evtRetCons):

        for infoTotalContrib in evtRetCons.infoTotalContrib:

            r9012_infototalcontrib_dados = {}
            r9012_infototalcontrib_dados['r9012_evtretcons_id'] = r9012_evtretcons.id

            try:
                r9012_infototalcontrib_dados['nrrecarqbase'] = read_from_xml(infoTotalContrib.nrRecArqBase.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r9012_infototalcontrib_dados['indexistinfo'] = read_from_xml(infoTotalContrib.indExistInfo.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            r9012_infototalcontrib = r9012infoTotalContrib.objects.create(**r9012_infototalcontrib_dados)

            if 'totApurMen' in dir(infoTotalContrib):

                for totApurMen in infoTotalContrib.totApurMen:

                    r9012_totapurmen_dados = {}
                    r9012_totapurmen_dados['r9012_infototalcontrib_id'] = r9012_infototalcontrib.id

                    try:
                        r9012_totapurmen_dados['crmen'] = read_from_xml(totApurMen.CRMen.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurmen_dados['vlrbasecrmen'] = read_from_xml(totApurMen.vlrBaseCRMen.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurmen_dados['vlrcrmen'] = read_from_xml(totApurMen.vlrCRMen.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurmen_dados['vlrbasecrmensusp'] = read_from_xml(totApurMen.vlrBaseCRMenSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurmen_dados['vlrcrmensusp'] = read_from_xml(totApurMen.vlrCRMenSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r9012_totapurmen = r9012totApurMen.objects.create(**r9012_totapurmen_dados)

            if 'totApurQui' in dir(infoTotalContrib):

                for totApurQui in infoTotalContrib.totApurQui:

                    r9012_totapurqui_dados = {}
                    r9012_totapurqui_dados['r9012_infototalcontrib_id'] = r9012_infototalcontrib.id

                    try:
                        r9012_totapurqui_dados['perapurqui'] = read_from_xml(totApurQui.perApurQui.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurqui_dados['crqui'] = read_from_xml(totApurQui.CRQui.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurqui_dados['vlrbasecrqui'] = read_from_xml(totApurQui.vlrBaseCRQui.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurqui_dados['vlrcrqui'] = read_from_xml(totApurQui.vlrCRQui.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurqui_dados['vlrbasecrquisusp'] = read_from_xml(totApurQui.vlrBaseCRQuiSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurqui_dados['vlrcrquisusp'] = read_from_xml(totApurQui.vlrCRQuiSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r9012_totapurqui = r9012totApurQui.objects.create(**r9012_totapurqui_dados)

            if 'totApurDec' in dir(infoTotalContrib):

                for totApurDec in infoTotalContrib.totApurDec:

                    r9012_totapurdec_dados = {}
                    r9012_totapurdec_dados['r9012_infototalcontrib_id'] = r9012_infototalcontrib.id

                    try:
                        r9012_totapurdec_dados['perapurdec'] = read_from_xml(totApurDec.perApurDec.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurdec_dados['crdec'] = read_from_xml(totApurDec.CRDec.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurdec_dados['vlrbasecrdec'] = read_from_xml(totApurDec.vlrBaseCRDec.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurdec_dados['vlrcrdec'] = read_from_xml(totApurDec.vlrCRDec.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurdec_dados['vlrbasecrdecsusp'] = read_from_xml(totApurDec.vlrBaseCRDecSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurdec_dados['vlrcrdecsusp'] = read_from_xml(totApurDec.vlrCRDecSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r9012_totapurdec = r9012totApurDec.objects.create(**r9012_totapurdec_dados)

            if 'totApurSem' in dir(infoTotalContrib):

                for totApurSem in infoTotalContrib.totApurSem:

                    r9012_totapursem_dados = {}
                    r9012_totapursem_dados['r9012_infototalcontrib_id'] = r9012_infototalcontrib.id

                    try:
                        r9012_totapursem_dados['perapursem'] = read_from_xml(totApurSem.perApurSem.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapursem_dados['crsem'] = read_from_xml(totApurSem.CRSem.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapursem_dados['vlrbasecrsem'] = read_from_xml(totApurSem.vlrBaseCRSem.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapursem_dados['vlrcrsem'] = read_from_xml(totApurSem.vlrCRSem.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapursem_dados['vlrbasecrsemsusp'] = read_from_xml(totApurSem.vlrBaseCRSemSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapursem_dados['vlrcrsemsusp'] = read_from_xml(totApurSem.vlrCRSemSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r9012_totapursem = r9012totApurSem.objects.create(**r9012_totapursem_dados)

            if 'totApurDia' in dir(infoTotalContrib):

                for totApurDia in infoTotalContrib.totApurDia:

                    r9012_totapurdia_dados = {}
                    r9012_totapurdia_dados['r9012_infototalcontrib_id'] = r9012_infototalcontrib.id

                    try:
                        r9012_totapurdia_dados['perapurdia'] = read_from_xml(totApurDia.perApurDia.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurdia_dados['crdia'] = read_from_xml(totApurDia.CRDia.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurdia_dados['vlrbasecrdia'] = read_from_xml(totApurDia.vlrBaseCRDia.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurdia_dados['vlrcrdia'] = read_from_xml(totApurDia.vlrCRDia.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurdia_dados['vlrbasecrdiasusp'] = read_from_xml(totApurDia.vlrBaseCRDiaSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9012_totapurdia_dados['vlrcrdiasusp'] = read_from_xml(totApurDia.vlrCRDiaSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r9012_totapurdia = r9012totApurDia.objects.create(**r9012_totapurdia_dados)
    r9012_evtretcons_dados['evento'] = 'r9012'
    r9012_evtretcons_dados['id'] = r9012_evtretcons.id
    r9012_evtretcons_dados['identidade_evento'] = doc.Reinf.evtRetCons['id']

    from emensageriapro.efdreinf.views.r9012_evtretcons_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r9012_evtretcons.id)

    return r9012_evtretcons_dados