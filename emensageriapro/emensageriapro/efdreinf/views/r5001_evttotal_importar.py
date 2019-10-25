#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r5001.models import *
from emensageriapro.functions import read_from_xml



def read_r5001_evttotal_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r5001_evttotal_obj(request, doc, status, validar)
    return dados



def read_r5001_evttotal(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r5001_evttotal_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r5001evtTotal.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r5001_evttotal_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r5001_evttotal_dados = {}
    r5001_evttotal_dados['status'] = status
    r5001_evttotal_dados['arquivo_original'] = 1
    if arquivo:
        r5001_evttotal_dados['arquivo'] = arquivo.arquivo
    r5001_evttotal_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r5001_evttotal_dados['identidade'] = doc.Reinf.evtTotal['id']
    evtTotal = doc.Reinf.evtTotal

    try:
        r5001_evttotal_dados['perapur'] = read_from_xml(evtTotal.ideEvento.perApur.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r5001_evttotal_dados['tpinsc'] = read_from_xml(evtTotal.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r5001_evttotal_dados['nrinsc'] = read_from_xml(evtTotal.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r5001_evttotal_dados['cdretorno'] = read_from_xml(evtTotal.ideRecRetorno.ideStatus.cdRetorno.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r5001_evttotal_dados['descretorno'] = read_from_xml(evtTotal.ideRecRetorno.ideStatus.descRetorno.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r5001_evttotal_dados['nrprotentr'] = read_from_xml(evtTotal.infoRecEv.nrProtEntr.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r5001_evttotal_dados['dhprocess'] = read_from_xml(evtTotal.infoRecEv.dhProcess.cdata, 'efdreinf', 'D', None)
    except AttributeError:
        pass

    try:
        r5001_evttotal_dados['tpev'] = read_from_xml(evtTotal.infoRecEv.tpEv.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r5001_evttotal_dados['idev'] = read_from_xml(evtTotal.infoRecEv.idEv.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r5001_evttotal_dados['hash'] = read_from_xml(evtTotal.infoRecEv.hash.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    r5001_evttotal = r5001evtTotal.objects.create(**r5001_evttotal_dados)

    if 'ideRecRetorno' in dir(evtTotal) and 'ideStatus' in dir(evtTotal.ideRecRetorno) and 'regOcorrs' in dir(evtTotal.ideRecRetorno.ideStatus):

        for regOcorrs in evtTotal.ideRecRetorno.ideStatus.regOcorrs:

            r5001_regocorrs_dados = {}
            r5001_regocorrs_dados['r5001_evttotal_id'] = r5001_evttotal.id

            try:
                r5001_regocorrs_dados['tpocorr'] = read_from_xml(regOcorrs.tpOcorr.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r5001_regocorrs_dados['localerroaviso'] = read_from_xml(regOcorrs.localErroAviso.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r5001_regocorrs_dados['codresp'] = read_from_xml(regOcorrs.codResp.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r5001_regocorrs_dados['dscresp'] = read_from_xml(regOcorrs.dscResp.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r5001_regocorrs = r5001regOcorrs.objects.create(**r5001_regocorrs_dados)

    if 'infoTotal' in dir(evtTotal):

        for infoTotal in evtTotal.infoTotal:

            r5001_infototal_dados = {}
            r5001_infototal_dados['r5001_evttotal_id'] = r5001_evttotal.id

            try:
                r5001_infototal_dados['nrrecarqbase'] = read_from_xml(infoTotal.nrRecArqBase.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r5001_infototal_dados['tpinsc'] = read_from_xml(infoTotal.ideEstab.tpInsc.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r5001_infototal_dados['nrinsc'] = read_from_xml(infoTotal.ideEstab.nrInsc.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r5001_infototal = r5001infoTotal.objects.create(**r5001_infototal_dados)

            if 'ideEstab' in dir(infoTotal) and 'RTom' in dir(infoTotal.ideEstab):

                for RTom in infoTotal.ideEstab.RTom:

                    r5001_rtom_dados = {}
                    r5001_rtom_dados['r5001_infototal_id'] = r5001_infototal.id

                    try:
                        r5001_rtom_dados['cnpjprestador'] = read_from_xml(RTom.cnpjPrestador.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r5001_rtom_dados['cno'] = read_from_xml(RTom.cno.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r5001_rtom_dados['vlrtotalbaseret'] = read_from_xml(RTom.vlrTotalBaseRet.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r5001_rtom = r5001RTom.objects.create(**r5001_rtom_dados)

                    if 'infoCRTom' in dir(RTom):

                        for infoCRTom in RTom.infoCRTom:

                            r5001_infocrtom_dados = {}
                            r5001_infocrtom_dados['r5001_rtom_id'] = r5001_rtom.id
        
                            try:
                                r5001_infocrtom_dados['crtom'] = read_from_xml(infoCRTom.CRTom.cdata, 'efdreinf', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                r5001_infocrtom_dados['vlrcrtom'] = read_from_xml(infoCRTom.vlrCRTom.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r5001_infocrtom_dados['vlrcrtomsusp'] = read_from_xml(infoCRTom.vlrCRTomSusp.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass

                            r5001_infocrtom = r5001infoCRTom.objects.create(**r5001_infocrtom_dados)

            if 'ideEstab' in dir(infoTotal) and 'RPrest' in dir(infoTotal.ideEstab):

                for RPrest in infoTotal.ideEstab.RPrest:

                    r5001_rprest_dados = {}
                    r5001_rprest_dados['r5001_infototal_id'] = r5001_infototal.id

                    try:
                        r5001_rprest_dados['tpinsctomador'] = read_from_xml(RPrest.tpInscTomador.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r5001_rprest_dados['nrinsctomador'] = read_from_xml(RPrest.nrInscTomador.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r5001_rprest_dados['vlrtotalbaseret'] = read_from_xml(RPrest.vlrTotalBaseRet.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r5001_rprest_dados['vlrtotalretprinc'] = read_from_xml(RPrest.vlrTotalRetPrinc.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r5001_rprest_dados['vlrtotalretadic'] = read_from_xml(RPrest.vlrTotalRetAdic.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r5001_rprest_dados['vlrtotalnretprinc'] = read_from_xml(RPrest.vlrTotalNRetPrinc.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r5001_rprest_dados['vlrtotalnretadic'] = read_from_xml(RPrest.vlrTotalNRetAdic.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r5001_rprest = r5001RPrest.objects.create(**r5001_rprest_dados)

            if 'ideEstab' in dir(infoTotal) and 'RRecRepAD' in dir(infoTotal.ideEstab):

                for RRecRepAD in infoTotal.ideEstab.RRecRepAD:

                    r5001_rrecrepad_dados = {}
                    r5001_rrecrepad_dados['r5001_infototal_id'] = r5001_infototal.id

                    try:
                        r5001_rrecrepad_dados['cnpjassocdesp'] = read_from_xml(RRecRepAD.cnpjAssocDesp.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r5001_rrecrepad_dados['vlrtotalrep'] = read_from_xml(RRecRepAD.vlrTotalRep.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r5001_rrecrepad_dados['crrecrepad'] = read_from_xml(RRecRepAD.CRRecRepAD.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r5001_rrecrepad_dados['vlrcrrecrepad'] = read_from_xml(RRecRepAD.vlrCRRecRepAD.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r5001_rrecrepad_dados['vlrcrrecrepadsusp'] = read_from_xml(RRecRepAD.vlrCRRecRepADSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r5001_rrecrepad = r5001RRecRepAD.objects.create(**r5001_rrecrepad_dados)

            if 'ideEstab' in dir(infoTotal) and 'RComl' in dir(infoTotal.ideEstab):

                for RComl in infoTotal.ideEstab.RComl:

                    r5001_rcoml_dados = {}
                    r5001_rcoml_dados['r5001_infototal_id'] = r5001_infototal.id

                    try:
                        r5001_rcoml_dados['crcoml'] = read_from_xml(RComl.CRComl.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r5001_rcoml_dados['vlrcrcoml'] = read_from_xml(RComl.vlrCRComl.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r5001_rcoml_dados['vlrcrcomlsusp'] = read_from_xml(RComl.vlrCRComlSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r5001_rcoml = r5001RComl.objects.create(**r5001_rcoml_dados)

            if 'ideEstab' in dir(infoTotal) and 'RCPRB' in dir(infoTotal.ideEstab):

                for RCPRB in infoTotal.ideEstab.RCPRB:

                    r5001_rcprb_dados = {}
                    r5001_rcprb_dados['r5001_infototal_id'] = r5001_infototal.id

                    try:
                        r5001_rcprb_dados['crcprb'] = read_from_xml(RCPRB.CRCPRB.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r5001_rcprb_dados['vlrcrcprb'] = read_from_xml(RCPRB.vlrCRCPRB.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r5001_rcprb_dados['vlrcrcprbsusp'] = read_from_xml(RCPRB.vlrCRCPRBSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r5001_rcprb = r5001RCPRB.objects.create(**r5001_rcprb_dados)

            if 'ideEstab' in dir(infoTotal) and 'RRecEspetDesp' in dir(infoTotal.ideEstab):

                for RRecEspetDesp in infoTotal.ideEstab.RRecEspetDesp:

                    r5001_rrecespetdesp_dados = {}
                    r5001_rrecespetdesp_dados['r5001_infototal_id'] = r5001_infototal.id

                    try:
                        r5001_rrecespetdesp_dados['crrecespetdesp'] = read_from_xml(RRecEspetDesp.CRRecEspetDesp.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r5001_rrecespetdesp_dados['vlrreceitatotal'] = read_from_xml(RRecEspetDesp.vlrReceitaTotal.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r5001_rrecespetdesp_dados['vlrcrrecespetdesp'] = read_from_xml(RRecEspetDesp.vlrCRRecEspetDesp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r5001_rrecespetdesp_dados['vlrcrrecespetdespsusp'] = read_from_xml(RRecEspetDesp.vlrCRRecEspetDespSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r5001_rrecespetdesp = r5001RRecEspetDesp.objects.create(**r5001_rrecespetdesp_dados)
    r5001_evttotal_dados['evento'] = 'r5001'
    r5001_evttotal_dados['id'] = r5001_evttotal.id
    r5001_evttotal_dados['identidade_evento'] = doc.Reinf.evtTotal['id']

    from emensageriapro.efdreinf.views.r5001_evttotal_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r5001_evttotal.id)

    return r5001_evttotal_dados