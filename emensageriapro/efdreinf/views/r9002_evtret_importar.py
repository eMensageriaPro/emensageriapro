#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r9002.models import *



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

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_r9002_evtret_obj(request, doc, status, validar, arquivo)

    r9002evtRet.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_r9002_evtret_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r9002_evtret_dados = {}
    r9002_evtret_dados['status'] = status
    r9002_evtret_dados['arquivo_original'] = 1
    if arquivo:
        r9002_evtret_dados['arquivo'] = arquivo
    r9002_evtret_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r9002_evtret_dados['identidade'] = doc.Reinf.evtRet['id']
    evtRet = doc.Reinf.evtRet

    try:
        r9002_evtret_dados['perref'] = evtRet.ideEvento.perRef.cdata
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['tpinsc'] = evtRet.ideContri.tpInsc.cdata
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['nrinsc'] = evtRet.ideContri.nrInsc.cdata
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['cdretorno'] = evtRet.ideRecRetorno.ideStatus.cdRetorno.cdata
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['descretorno'] = evtRet.ideRecRetorno.ideStatus.descRetorno.cdata
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['nrprotentr'] = evtRet.infoRecEv.nrProtEntr.cdata
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['dhprocess'] = evtRet.infoRecEv.dhProcess.cdata
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['tpev'] = evtRet.infoRecEv.tpEv.cdata
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['idev'] = evtRet.infoRecEv.idEv.cdata
    except AttributeError:
        pass

    try:
        r9002_evtret_dados['hash'] = evtRet.infoRecEv.hash.cdata
    except AttributeError:
        pass

    r9002_evtret = r9002evtRet.objects.create(**r9002_evtret_dados)

    if 'ideRecRetorno' in dir(evtRet) and 'ideStatus' in dir(evtRet.ideRecRetorno) and 'regOcorrs' in dir(evtRet.ideRecRetorno.ideStatus):

        for regOcorrs in evtRet.ideRecRetorno.ideStatus.regOcorrs:

            r9002_regocorrs_dados = {}
            r9002_regocorrs_dados['r9002_evtret_id'] = r9002_evtret.id

            try:
                r9002_regocorrs_dados['tpocorr'] = regOcorrs.tpOcorr.cdata
            except AttributeError:
                pass

            try:
                r9002_regocorrs_dados['localerroaviso'] = regOcorrs.localErroAviso.cdata
            except AttributeError:
                pass

            try:
                r9002_regocorrs_dados['codresp'] = regOcorrs.codResp.cdata
            except AttributeError:
                pass

            try:
                r9002_regocorrs_dados['dscresp'] = regOcorrs.dscResp.cdata
            except AttributeError:
                pass

            r9002_regocorrs = r9002regOcorrs.objects.create(**r9002_regocorrs_dados)

    if 'infoTotal' in dir(evtRet):

        for infoTotal in evtRet.infoTotal:

            r9002_infototal_dados = {}
            r9002_infototal_dados['r9002_evtret_id'] = r9002_evtret.id

            try:
                r9002_infototal_dados['nrrecarqbase'] = infoTotal.nrRecArqBase.cdata
            except AttributeError:
                pass

            try:
                r9002_infototal_dados['tpinsc'] = infoTotal.ideEstab.tpInsc.cdata
            except AttributeError:
                pass

            try:
                r9002_infototal_dados['nrinsc'] = infoTotal.ideEstab.nrInsc.cdata
            except AttributeError:
                pass

            r9002_infototal = r9002infoTotal.objects.create(**r9002_infototal_dados)

            if 'ideEstab' in dir(infoTotal) and 'totApurMen' in dir(infoTotal.ideEstab):

                for totApurMen in infoTotal.ideEstab.totApurMen:

                    r9002_totapurmen_dados = {}
                    r9002_totapurmen_dados['r9002_infototal_id'] = r9002_infototal.id

                    try:
                        r9002_totapurmen_dados['crmen'] = totApurMen.CRMen.cdata
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurmen_dados['vlrbasecrmen'] = totApurMen.vlrBaseCRMen.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurmen_dados['vlrcrmen'] = totApurMen.vlrCRMen.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurmen_dados['vlrbasecrmensusp'] = totApurMen.vlrBaseCRMenSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurmen_dados['vlrcrmensusp'] = totApurMen.vlrCRMenSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    r9002_totapurmen = r9002totApurMen.objects.create(**r9002_totapurmen_dados)

            if 'ideEstab' in dir(infoTotal) and 'totApurQui' in dir(infoTotal.ideEstab):

                for totApurQui in infoTotal.ideEstab.totApurQui:

                    r9002_totapurqui_dados = {}
                    r9002_totapurqui_dados['r9002_infototal_id'] = r9002_infototal.id

                    try:
                        r9002_totapurqui_dados['perapurqui'] = totApurQui.perApurQui.cdata
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurqui_dados['crqui'] = totApurQui.CRQui.cdata
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurqui_dados['vlrbasecrqui'] = totApurQui.vlrBaseCRQui.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurqui_dados['vlrcrqui'] = totApurQui.vlrCRQui.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurqui_dados['vlrbasecrquisusp'] = totApurQui.vlrBaseCRQuiSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurqui_dados['vlrcrquisusp'] = totApurQui.vlrCRQuiSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    r9002_totapurqui = r9002totApurQui.objects.create(**r9002_totapurqui_dados)

            if 'ideEstab' in dir(infoTotal) and 'totApurDec' in dir(infoTotal.ideEstab):

                for totApurDec in infoTotal.ideEstab.totApurDec:

                    r9002_totapurdec_dados = {}
                    r9002_totapurdec_dados['r9002_infototal_id'] = r9002_infototal.id

                    try:
                        r9002_totapurdec_dados['perapurdec'] = totApurDec.perApurDec.cdata
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdec_dados['crdec'] = totApurDec.CRDec.cdata
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdec_dados['vlrbasecrdec'] = totApurDec.vlrBaseCRDec.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdec_dados['vlrcrdec'] = totApurDec.vlrCRDec.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdec_dados['vlrbasecrdecsusp'] = totApurDec.vlrBaseCRDecSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdec_dados['vlrcrdecsusp'] = totApurDec.vlrCRDecSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    r9002_totapurdec = r9002totApurDec.objects.create(**r9002_totapurdec_dados)

            if 'ideEstab' in dir(infoTotal) and 'totApurSem' in dir(infoTotal.ideEstab):

                for totApurSem in infoTotal.ideEstab.totApurSem:

                    r9002_totapursem_dados = {}
                    r9002_totapursem_dados['r9002_infototal_id'] = r9002_infototal.id

                    try:
                        r9002_totapursem_dados['perapursem'] = totApurSem.perApurSem.cdata
                    except AttributeError:
                        pass

                    try:
                        r9002_totapursem_dados['crsem'] = totApurSem.CRSem.cdata
                    except AttributeError:
                        pass

                    try:
                        r9002_totapursem_dados['vlrbasecrsem'] = totApurSem.vlrBaseCRSem.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9002_totapursem_dados['vlrcrsem'] = totApurSem.vlrCRSem.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9002_totapursem_dados['vlrbasecrsemsusp'] = totApurSem.vlrBaseCRSemSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9002_totapursem_dados['vlrcrsemsusp'] = totApurSem.vlrCRSemSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    r9002_totapursem = r9002totApurSem.objects.create(**r9002_totapursem_dados)

            if 'ideEstab' in dir(infoTotal) and 'totApurDia' in dir(infoTotal.ideEstab):

                for totApurDia in infoTotal.ideEstab.totApurDia:

                    r9002_totapurdia_dados = {}
                    r9002_totapurdia_dados['r9002_infototal_id'] = r9002_infototal.id

                    try:
                        r9002_totapurdia_dados['perapurdia'] = totApurDia.perApurDia.cdata
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdia_dados['crdia'] = totApurDia.CRDia.cdata
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdia_dados['vlrbasecrdia'] = totApurDia.vlrBaseCRDia.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdia_dados['vlrcrdia'] = totApurDia.vlrCRDia.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdia_dados['vlrbasecrdiasusp'] = totApurDia.vlrBaseCRDiaSusp.cdata.replace('.', '').replace(',', '.')
                    except AttributeError:
                        pass

                    try:
                        r9002_totapurdia_dados['vlrcrdiasusp'] = totApurDia.vlrCRDiaSusp.cdata.replace('.', '').replace(',', '.')
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