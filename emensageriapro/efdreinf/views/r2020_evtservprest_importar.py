# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r2020.models import *
from emensageriapro.functions import read_from_xml



def read_r2020_evtservprest_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2020_evtservprest_obj(request, doc, status, validar)
    return dados



def read_r2020_evtservprest(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r2020_evtservprest_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r2020evtServPrest.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r2020_evtservprest_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r2020_evtservprest_dados = {}
    r2020_evtservprest_dados['status'] = status
    r2020_evtservprest_dados['arquivo_original'] = 1
    if arquivo:
        r2020_evtservprest_dados['arquivo'] = arquivo.arquivo
    r2020_evtservprest_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2020_evtservprest_dados['identidade'] = doc.Reinf.evtServPrest['id']
    evtServPrest = doc.Reinf.evtServPrest

    try:
        r2020_evtservprest_dados['indretif'] = read_from_xml(evtServPrest.ideEvento.indRetif.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['nrrecibo'] = read_from_xml(evtServPrest.ideEvento.nrRecibo.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['perapur'] = read_from_xml(evtServPrest.ideEvento.perApur.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['tpamb'] = read_from_xml(evtServPrest.ideEvento.tpAmb.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['procemi'] = read_from_xml(evtServPrest.ideEvento.procEmi.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['verproc'] = read_from_xml(evtServPrest.ideEvento.verProc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['tpinsc'] = read_from_xml(evtServPrest.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['nrinsc'] = read_from_xml(evtServPrest.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['tpinscestabprest'] = read_from_xml(evtServPrest.infoServPrest.ideEstabPrest.tpInscEstabPrest.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['nrinscestabprest'] = read_from_xml(evtServPrest.infoServPrest.ideEstabPrest.nrInscEstabPrest.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['tpinsctomador'] = read_from_xml(evtServPrest.infoServPrest.ideEstabPrest.ideTomador.tpInscTomador.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['nrinsctomador'] = read_from_xml(evtServPrest.infoServPrest.ideEstabPrest.ideTomador.nrInscTomador.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['indobra'] = read_from_xml(evtServPrest.infoServPrest.ideEstabPrest.ideTomador.indObra.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['vlrtotalbruto'] = read_from_xml(evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalBruto.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['vlrtotalbaseret'] = read_from_xml(evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalBaseRet.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['vlrtotalretprinc'] = read_from_xml(evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalRetPrinc.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['vlrtotalretadic'] = read_from_xml(evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalRetAdic.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['vlrtotalnretprinc'] = read_from_xml(evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalNRetPrinc.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2020_evtservprest_dados['vlrtotalnretadic'] = read_from_xml(evtServPrest.infoServPrest.ideEstabPrest.ideTomador.vlrTotalNRetAdic.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    r2020_evtservprest = r2020evtServPrest.objects.create(**r2020_evtservprest_dados)

    if 'infoServPrest' in dir(evtServPrest) and 'ideEstabPrest' in dir(evtServPrest.infoServPrest) and 'ideTomador' in dir(evtServPrest.infoServPrest.ideEstabPrest) and 'nfs' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador):

        for nfs in evtServPrest.infoServPrest.ideEstabPrest.ideTomador.nfs:

            r2020_nfs_dados = {}
            r2020_nfs_dados['r2020_evtservprest_id'] = r2020_evtservprest.id

            try:
                r2020_nfs_dados['serie'] = read_from_xml(nfs.serie.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2020_nfs_dados['numdocto'] = read_from_xml(nfs.numDocto.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2020_nfs_dados['dtemissaonf'] = read_from_xml(nfs.dtEmissaoNF.cdata, 'efdreinf', 'D', None)
            except AttributeError:
                pass

            try:
                r2020_nfs_dados['vlrbruto'] = read_from_xml(nfs.vlrBruto.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            try:
                r2020_nfs_dados['obs'] = read_from_xml(nfs.obs.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r2020_nfs = r2020nfs.objects.create(**r2020_nfs_dados)

            if 'infoTpServ' in dir(nfs):

                for infoTpServ in nfs.infoTpServ:

                    r2020_infotpserv_dados = {}
                    r2020_infotpserv_dados['r2020_nfs_id'] = r2020_nfs.id

                    try:
                        r2020_infotpserv_dados['tpservico'] = read_from_xml(infoTpServ.tpServico.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r2020_infotpserv_dados['vlrbaseret'] = read_from_xml(infoTpServ.vlrBaseRet.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2020_infotpserv_dados['vlrretencao'] = read_from_xml(infoTpServ.vlrRetencao.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2020_infotpserv_dados['vlrretsub'] = read_from_xml(infoTpServ.vlrRetSub.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2020_infotpserv_dados['vlrnretprinc'] = read_from_xml(infoTpServ.vlrNRetPrinc.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2020_infotpserv_dados['vlrservicos15'] = read_from_xml(infoTpServ.vlrServicos15.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2020_infotpserv_dados['vlrservicos20'] = read_from_xml(infoTpServ.vlrServicos20.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2020_infotpserv_dados['vlrservicos25'] = read_from_xml(infoTpServ.vlrServicos25.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2020_infotpserv_dados['vlradicional'] = read_from_xml(infoTpServ.vlrAdicional.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2020_infotpserv_dados['vlrnretadic'] = read_from_xml(infoTpServ.vlrNRetAdic.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r2020_infotpserv = r2020infoTpServ.objects.create(**r2020_infotpserv_dados)

    if 'infoServPrest' in dir(evtServPrest) and 'ideEstabPrest' in dir(evtServPrest.infoServPrest) and 'ideTomador' in dir(evtServPrest.infoServPrest.ideEstabPrest) and 'infoProcRetPr' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador):

        for infoProcRetPr in evtServPrest.infoServPrest.ideEstabPrest.ideTomador.infoProcRetPr:

            r2020_infoprocretpr_dados = {}
            r2020_infoprocretpr_dados['r2020_evtservprest_id'] = r2020_evtservprest.id

            try:
                r2020_infoprocretpr_dados['tpprocretprinc'] = read_from_xml(infoProcRetPr.tpProcRetPrinc.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r2020_infoprocretpr_dados['nrprocretprinc'] = read_from_xml(infoProcRetPr.nrProcRetPrinc.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2020_infoprocretpr_dados['codsuspprinc'] = read_from_xml(infoProcRetPr.codSuspPrinc.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r2020_infoprocretpr_dados['valorprinc'] = read_from_xml(infoProcRetPr.valorPrinc.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            r2020_infoprocretpr = r2020infoProcRetPr.objects.create(**r2020_infoprocretpr_dados)

    if 'infoServPrest' in dir(evtServPrest) and 'ideEstabPrest' in dir(evtServPrest.infoServPrest) and 'ideTomador' in dir(evtServPrest.infoServPrest.ideEstabPrest) and 'infoProcRetAd' in dir(evtServPrest.infoServPrest.ideEstabPrest.ideTomador):

        for infoProcRetAd in evtServPrest.infoServPrest.ideEstabPrest.ideTomador.infoProcRetAd:

            r2020_infoprocretad_dados = {}
            r2020_infoprocretad_dados['r2020_evtservprest_id'] = r2020_evtservprest.id

            try:
                r2020_infoprocretad_dados['tpprocretadic'] = read_from_xml(infoProcRetAd.tpProcRetAdic.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r2020_infoprocretad_dados['nrprocretadic'] = read_from_xml(infoProcRetAd.nrProcRetAdic.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2020_infoprocretad_dados['codsuspadic'] = read_from_xml(infoProcRetAd.codSuspAdic.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r2020_infoprocretad_dados['valoradic'] = read_from_xml(infoProcRetAd.valorAdic.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            r2020_infoprocretad = r2020infoProcRetAd.objects.create(**r2020_infoprocretad_dados)
    r2020_evtservprest_dados['evento'] = 'r2020'
    r2020_evtservprest_dados['id'] = r2020_evtservprest.id
    r2020_evtservprest_dados['identidade_evento'] = doc.Reinf.evtServPrest['id']

    from emensageriapro.efdreinf.views.r2020_evtservprest_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r2020_evtservprest.id)

    return r2020_evtservprest_dados