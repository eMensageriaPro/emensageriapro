#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r9001.models import *



def read_r9001_evttotal_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r9001_evttotal_obj(request, doc, status, validar)
    return dados



def read_r9001_evttotal(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r9001_evttotal_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r9001evtTotal.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r9001_evttotal_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r9001_evttotal_dados = {}
    r9001_evttotal_dados['status'] = status
    r9001_evttotal_dados['arquivo_original'] = 1
    if arquivo:
        r9001_evttotal_dados['arquivo'] = arquivo.arquivo
    r9001_evttotal_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r9001_evttotal_dados['identidade'] = doc.Reinf.evtTotal['id']
    evtTotal = doc.Reinf.evtTotal

    try:
        r9001_evttotal_dados['perapur'] = evtTotal.ideEvento.perApur.cdata
    except AttributeError:
        pass

    try:
        r9001_evttotal_dados['tpinsc'] = evtTotal.ideContri.tpInsc.cdata
    except AttributeError:
        pass

    try:
        r9001_evttotal_dados['nrinsc'] = evtTotal.ideContri.nrInsc.cdata
    except AttributeError:
        pass

    try:
        r9001_evttotal_dados['cdretorno'] = evtTotal.ideRecRetorno.ideStatus.cdRetorno.cdata
    except AttributeError:
        pass

    try:
        r9001_evttotal_dados['descretorno'] = evtTotal.ideRecRetorno.ideStatus.descRetorno.cdata
    except AttributeError:
        pass

    try:
        r9001_evttotal_dados['nrprotentr'] = evtTotal.infoRecEv.nrProtEntr.cdata
    except AttributeError:
        pass

    try:
        r9001_evttotal_dados['dhprocess'] = evtTotal.infoRecEv.dhProcess.cdata
    except AttributeError:
        pass

    try:
        r9001_evttotal_dados['tpev'] = evtTotal.infoRecEv.tpEv.cdata
    except AttributeError:
        pass

    try:
        r9001_evttotal_dados['idev'] = evtTotal.infoRecEv.idEv.cdata
    except AttributeError:
        pass

    try:
        r9001_evttotal_dados['hash'] = evtTotal.infoRecEv.hash.cdata
    except AttributeError:
        pass

    r9001_evttotal = r9001evtTotal.objects.create(**r9001_evttotal_dados)

    if 'ideRecRetorno' in dir(evtTotal) and 'ideStatus' in dir(evtTotal.ideRecRetorno) and 'regOcorrs' in dir(evtTotal.ideRecRetorno.ideStatus):

        for regOcorrs in evtTotal.ideRecRetorno.ideStatus.regOcorrs:

            r9001_regocorrs_dados = {}
            r9001_regocorrs_dados['r9001_evttotal_id'] = r9001_evttotal.id

            try:
                r9001_regocorrs_dados['tpocorr'] = regOcorrs.tpOcorr.cdata
            except AttributeError:
                pass

            try:
                r9001_regocorrs_dados['localerroaviso'] = regOcorrs.localErroAviso.cdata
            except AttributeError:
                pass

            try:
                r9001_regocorrs_dados['codresp'] = regOcorrs.codResp.cdata
            except AttributeError:
                pass

            try:
                r9001_regocorrs_dados['dscresp'] = regOcorrs.dscResp.cdata
            except AttributeError:
                pass

            r9001_regocorrs = r9001regOcorrs.objects.create(**r9001_regocorrs_dados)

    if 'infoTotal' in dir(evtTotal):

        for infoTotal in evtTotal.infoTotal:

            r9001_infototal_dados = {}
            r9001_infototal_dados['r9001_evttotal_id'] = r9001_evttotal.id

            try:
                r9001_infototal_dados['nrrecarqbase'] = infoTotal.nrRecArqBase.cdata
            except AttributeError:
                pass

            try:
                r9001_infototal_dados['tpinsc'] = infoTotal.ideEstab.tpInsc.cdata
            except AttributeError:
                pass

            try:
                r9001_infototal_dados['nrinsc'] = infoTotal.ideEstab.nrInsc.cdata
            except AttributeError:
                pass

            r9001_infototal = r9001infoTotal.objects.create(**r9001_infototal_dados)

            if 'ideEstab' in dir(infoTotal) and 'RTom' in dir(infoTotal.ideEstab):

                for RTom in infoTotal.ideEstab.RTom:

                    r9001_rtom_dados = {}
                    r9001_rtom_dados['r9001_infototal_id'] = r9001_infototal.id

                    try:
                        r9001_rtom_dados['cnpjprestador'] = RTom.cnpjPrestador.cdata
                    except AttributeError:
                        pass

                    try:
                        r9001_rtom_dados['cno'] = RTom.cno.cdata
                    except AttributeError:
                        pass

                    try:
                        r9001_rtom_dados['vlrtotalbaseret'] = RTom.vlrTotalBaseRet.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    r9001_rtom = r9001RTom.objects.create(**r9001_rtom_dados)

                    if 'infoCRTom' in dir(RTom):

                        for infoCRTom in RTom.infoCRTom:

                            r9001_infocrtom_dados = {}
                            r9001_infocrtom_dados['r9001_rtom_id'] = r9001_rtom.id
        
                            try:
                                r9001_infocrtom_dados['crtom'] = infoCRTom.CRTom.cdata
                            except AttributeError:
                                pass
        
                            try:
                                r9001_infocrtom_dados['vlrcrtom'] = infoCRTom.vlrCRTom.cdata.replace('.', '').replace(',', '.')
                            except AttributeError:
                                pass
        
                            try:
                                r9001_infocrtom_dados['vlrcrtomsusp'] = infoCRTom.vlrCRTomSusp.cdata.replace('.', '').replace(',', '.')
                            except AttributeError:
                                pass

                            r9001_infocrtom = r9001infoCRTom.objects.create(**r9001_infocrtom_dados)

            if 'ideEstab' in dir(infoTotal) and 'RPrest' in dir(infoTotal.ideEstab):

                for RPrest in infoTotal.ideEstab.RPrest:

                    r9001_rprest_dados = {}
                    r9001_rprest_dados['r9001_infototal_id'] = r9001_infototal.id

                    try:
                        r9001_rprest_dados['tpinsctomador'] = RPrest.tpInscTomador.cdata
                    except AttributeError:
                        pass

                    try:
                        r9001_rprest_dados['nrinsctomador'] = RPrest.nrInscTomador.cdata
                    except AttributeError:
                        pass

                    try:
                        r9001_rprest_dados['vlrtotalbaseret'] = RPrest.vlrTotalBaseRet.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9001_rprest_dados['vlrtotalretprinc'] = RPrest.vlrTotalRetPrinc.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9001_rprest_dados['vlrtotalretadic'] = RPrest.vlrTotalRetAdic.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9001_rprest_dados['vlrtotalnretprinc'] = RPrest.vlrTotalNRetPrinc.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9001_rprest_dados['vlrtotalnretadic'] = RPrest.vlrTotalNRetAdic.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    r9001_rprest = r9001RPrest.objects.create(**r9001_rprest_dados)

            if 'ideEstab' in dir(infoTotal) and 'RRecRepAD' in dir(infoTotal.ideEstab):

                for RRecRepAD in infoTotal.ideEstab.RRecRepAD:

                    r9001_rrecrepad_dados = {}
                    r9001_rrecrepad_dados['r9001_infototal_id'] = r9001_infototal.id

                    try:
                        r9001_rrecrepad_dados['cnpjassocdesp'] = RRecRepAD.cnpjAssocDesp.cdata
                    except AttributeError:
                        pass

                    try:
                        r9001_rrecrepad_dados['vlrtotalrep'] = RRecRepAD.vlrTotalRep.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9001_rrecrepad_dados['crrecrepad'] = RRecRepAD.CRRecRepAD.cdata
                    except AttributeError:
                        pass

                    try:
                        r9001_rrecrepad_dados['vlrcrrecrepad'] = RRecRepAD.vlrCRRecRepAD.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9001_rrecrepad_dados['vlrcrrecrepadsusp'] = RRecRepAD.vlrCRRecRepADSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    r9001_rrecrepad = r9001RRecRepAD.objects.create(**r9001_rrecrepad_dados)

            if 'ideEstab' in dir(infoTotal) and 'RComl' in dir(infoTotal.ideEstab):

                for RComl in infoTotal.ideEstab.RComl:

                    r9001_rcoml_dados = {}
                    r9001_rcoml_dados['r9001_infototal_id'] = r9001_infototal.id

                    try:
                        r9001_rcoml_dados['crcoml'] = RComl.CRComl.cdata
                    except AttributeError:
                        pass

                    try:
                        r9001_rcoml_dados['vlrcrcoml'] = RComl.vlrCRComl.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9001_rcoml_dados['vlrcrcomlsusp'] = RComl.vlrCRComlSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    r9001_rcoml = r9001RComl.objects.create(**r9001_rcoml_dados)

            if 'ideEstab' in dir(infoTotal) and 'RCPRB' in dir(infoTotal.ideEstab):

                for RCPRB in infoTotal.ideEstab.RCPRB:

                    r9001_rcprb_dados = {}
                    r9001_rcprb_dados['r9001_infototal_id'] = r9001_infototal.id

                    try:
                        r9001_rcprb_dados['crcprb'] = RCPRB.CRCPRB.cdata
                    except AttributeError:
                        pass

                    try:
                        r9001_rcprb_dados['vlrcrcprb'] = RCPRB.vlrCRCPRB.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9001_rcprb_dados['vlrcrcprbsusp'] = RCPRB.vlrCRCPRBSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    r9001_rcprb = r9001RCPRB.objects.create(**r9001_rcprb_dados)

            if 'ideEstab' in dir(infoTotal) and 'RRecEspetDesp' in dir(infoTotal.ideEstab):

                for RRecEspetDesp in infoTotal.ideEstab.RRecEspetDesp:

                    r9001_rrecespetdesp_dados = {}
                    r9001_rrecespetdesp_dados['r9001_infototal_id'] = r9001_infototal.id

                    try:
                        r9001_rrecespetdesp_dados['crrecespetdesp'] = RRecEspetDesp.CRRecEspetDesp.cdata
                    except AttributeError:
                        pass

                    try:
                        r9001_rrecespetdesp_dados['vlrreceitatotal'] = RRecEspetDesp.vlrReceitaTotal.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9001_rrecespetdesp_dados['vlrcrrecespetdesp'] = RRecEspetDesp.vlrCRRecEspetDesp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9001_rrecespetdesp_dados['vlrcrrecespetdespsusp'] = RRecEspetDesp.vlrCRRecEspetDespSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    r9001_rrecespetdesp = r9001RRecEspetDesp.objects.create(**r9001_rrecespetdesp_dados)
    r9001_evttotal_dados['evento'] = 'r9001'
    r9001_evttotal_dados['id'] = r9001_evttotal.id
    r9001_evttotal_dados['identidade_evento'] = doc.Reinf.evtTotal['id']

    from emensageriapro.efdreinf.views.r9001_evttotal_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r9001_evttotal.id)

    return r9001_evttotal_dados