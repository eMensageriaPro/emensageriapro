#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r9011.models import *
from emensageriapro.functions import read_from_xml



def read_r9011_evttotalcontrib_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r9011_evttotalcontrib_obj(request, doc, status, validar)
    return dados



def read_r9011_evttotalcontrib(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r9011_evttotalcontrib_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r9011evtTotalContrib.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r9011_evttotalcontrib_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r9011_evttotalcontrib_dados = {}
    r9011_evttotalcontrib_dados['status'] = status
    r9011_evttotalcontrib_dados['arquivo_original'] = 1
    if arquivo:
        r9011_evttotalcontrib_dados['arquivo'] = arquivo.arquivo
    r9011_evttotalcontrib_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r9011_evttotalcontrib_dados['identidade'] = doc.Reinf.evtTotalContrib['id']
    evtTotalContrib = doc.Reinf.evtTotalContrib

    try:
        r9011_evttotalcontrib_dados['perapur'] = read_from_xml(evtTotalContrib.ideEvento.perApur.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9011_evttotalcontrib_dados['tpinsc'] = read_from_xml(evtTotalContrib.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r9011_evttotalcontrib_dados['nrinsc'] = read_from_xml(evtTotalContrib.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9011_evttotalcontrib_dados['cdretorno'] = read_from_xml(evtTotalContrib.ideRecRetorno.ideStatus.cdRetorno.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r9011_evttotalcontrib_dados['descretorno'] = read_from_xml(evtTotalContrib.ideRecRetorno.ideStatus.descRetorno.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9011_evttotalcontrib_dados['nrprotentr'] = read_from_xml(evtTotalContrib.infoRecEv.nrProtEntr.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9011_evttotalcontrib_dados['dhprocess'] = read_from_xml(evtTotalContrib.infoRecEv.dhProcess.cdata, 'efdreinf', 'D', None)
    except AttributeError:
        pass

    try:
        r9011_evttotalcontrib_dados['tpev'] = read_from_xml(evtTotalContrib.infoRecEv.tpEv.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9011_evttotalcontrib_dados['idev'] = read_from_xml(evtTotalContrib.infoRecEv.idEv.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r9011_evttotalcontrib_dados['hash'] = read_from_xml(evtTotalContrib.infoRecEv.hash.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    r9011_evttotalcontrib = r9011evtTotalContrib.objects.create(**r9011_evttotalcontrib_dados)

    if 'ideRecRetorno' in dir(evtTotalContrib) and 'ideStatus' in dir(evtTotalContrib.ideRecRetorno) and 'regOcorrs' in dir(evtTotalContrib.ideRecRetorno.ideStatus):

        for regOcorrs in evtTotalContrib.ideRecRetorno.ideStatus.regOcorrs:

            r9011_regocorrs_dados = {}
            r9011_regocorrs_dados['r9011_evttotalcontrib_id'] = r9011_evttotalcontrib.id

            try:
                r9011_regocorrs_dados['tpocorr'] = read_from_xml(regOcorrs.tpOcorr.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r9011_regocorrs_dados['localerroaviso'] = read_from_xml(regOcorrs.localErroAviso.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r9011_regocorrs_dados['codresp'] = read_from_xml(regOcorrs.codResp.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r9011_regocorrs_dados['dscresp'] = read_from_xml(regOcorrs.dscResp.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r9011_regocorrs = r9011regOcorrs.objects.create(**r9011_regocorrs_dados)

    if 'infoTotalContrib' in dir(evtTotalContrib):

        for infoTotalContrib in evtTotalContrib.infoTotalContrib:

            r9011_infototalcontrib_dados = {}
            r9011_infototalcontrib_dados['r9011_evttotalcontrib_id'] = r9011_evttotalcontrib.id

            try:
                r9011_infototalcontrib_dados['nrrecarqbase'] = read_from_xml(infoTotalContrib.nrRecArqBase.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r9011_infototalcontrib_dados['indexistinfo'] = read_from_xml(infoTotalContrib.indExistInfo.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            r9011_infototalcontrib = r9011infoTotalContrib.objects.create(**r9011_infototalcontrib_dados)

            if 'RTom' in dir(infoTotalContrib):

                for RTom in infoTotalContrib.RTom:

                    r9011_rtom_dados = {}
                    r9011_rtom_dados['r9011_infototalcontrib_id'] = r9011_infototalcontrib.id

                    try:
                        r9011_rtom_dados['cnpjprestador'] = read_from_xml(RTom.cnpjPrestador.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r9011_rtom_dados['cno'] = read_from_xml(RTom.cno.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r9011_rtom_dados['vlrtotalbaseret'] = read_from_xml(RTom.vlrTotalBaseRet.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r9011_rtom = r9011RTom.objects.create(**r9011_rtom_dados)

                    if 'infoCRTom' in dir(RTom):

                        for infoCRTom in RTom.infoCRTom:

                            r9011_infocrtom_dados = {}
                            r9011_infocrtom_dados['r9011_rtom_id'] = r9011_rtom.id
        
                            try:
                                r9011_infocrtom_dados['crtom'] = read_from_xml(infoCRTom.CRTom.cdata, 'efdreinf', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                r9011_infocrtom_dados['vlrcrtom'] = read_from_xml(infoCRTom.vlrCRTom.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r9011_infocrtom_dados['vlrcrtomsusp'] = read_from_xml(infoCRTom.vlrCRTomSusp.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass

                            r9011_infocrtom = r9011infoCRTom.objects.create(**r9011_infocrtom_dados)

            if 'RPrest' in dir(infoTotalContrib):

                for RPrest in infoTotalContrib.RPrest:

                    r9011_rprest_dados = {}
                    r9011_rprest_dados['r9011_infototalcontrib_id'] = r9011_infototalcontrib.id

                    try:
                        r9011_rprest_dados['tpinsctomador'] = read_from_xml(RPrest.tpInscTomador.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r9011_rprest_dados['nrinsctomador'] = read_from_xml(RPrest.nrInscTomador.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r9011_rprest_dados['vlrtotalbaseret'] = read_from_xml(RPrest.vlrTotalBaseRet.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9011_rprest_dados['vlrtotalretprinc'] = read_from_xml(RPrest.vlrTotalRetPrinc.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9011_rprest_dados['vlrtotalretadic'] = read_from_xml(RPrest.vlrTotalRetAdic.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9011_rprest_dados['vlrtotalnretprinc'] = read_from_xml(RPrest.vlrTotalNRetPrinc.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9011_rprest_dados['vlrtotalnretadic'] = read_from_xml(RPrest.vlrTotalNRetAdic.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r9011_rprest = r9011RPrest.objects.create(**r9011_rprest_dados)

            if 'RRecRepAD' in dir(infoTotalContrib):

                for RRecRepAD in infoTotalContrib.RRecRepAD:

                    r9011_rrecrepad_dados = {}
                    r9011_rrecrepad_dados['r9011_infototalcontrib_id'] = r9011_infototalcontrib.id

                    try:
                        r9011_rrecrepad_dados['crrecrepad'] = read_from_xml(RRecRepAD.CRRecRepAD.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r9011_rrecrepad_dados['vlrcrrecrepad'] = read_from_xml(RRecRepAD.vlrCRRecRepAD.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9011_rrecrepad_dados['vlrcrrecrepadsusp'] = read_from_xml(RRecRepAD.vlrCRRecRepADSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r9011_rrecrepad = r9011RRecRepAD.objects.create(**r9011_rrecrepad_dados)

            if 'RComl' in dir(infoTotalContrib):

                for RComl in infoTotalContrib.RComl:

                    r9011_rcoml_dados = {}
                    r9011_rcoml_dados['r9011_infototalcontrib_id'] = r9011_infototalcontrib.id

                    try:
                        r9011_rcoml_dados['crcoml'] = read_from_xml(RComl.CRComl.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r9011_rcoml_dados['vlrcrcoml'] = read_from_xml(RComl.vlrCRComl.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9011_rcoml_dados['vlrcrcomlsusp'] = read_from_xml(RComl.vlrCRComlSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r9011_rcoml = r9011RComl.objects.create(**r9011_rcoml_dados)

            if 'RCPRB' in dir(infoTotalContrib):

                for RCPRB in infoTotalContrib.RCPRB:

                    r9011_rcprb_dados = {}
                    r9011_rcprb_dados['r9011_infototalcontrib_id'] = r9011_infototalcontrib.id

                    try:
                        r9011_rcprb_dados['crcprb'] = read_from_xml(RCPRB.CRCPRB.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r9011_rcprb_dados['vlrcrcprb'] = read_from_xml(RCPRB.vlrCRCPRB.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r9011_rcprb_dados['vlrcrcprbsusp'] = read_from_xml(RCPRB.vlrCRCPRBSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r9011_rcprb = r9011RCPRB.objects.create(**r9011_rcprb_dados)
    r9011_evttotalcontrib_dados['evento'] = 'r9011'
    r9011_evttotalcontrib_dados['id'] = r9011_evttotalcontrib.id
    r9011_evttotalcontrib_dados['identidade_evento'] = doc.Reinf.evtTotalContrib['id']

    from emensageriapro.efdreinf.views.r9011_evttotalcontrib_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r9011_evttotalcontrib.id)

    return r9011_evttotalcontrib_dados