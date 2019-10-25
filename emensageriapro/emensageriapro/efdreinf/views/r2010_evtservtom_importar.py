#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r2010.models import *
from emensageriapro.functions import read_from_xml



def read_r2010_evtservtom_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2010_evtservtom_obj(request, doc, status, validar)
    return dados



def read_r2010_evtservtom(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r2010_evtservtom_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r2010evtServTom.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r2010_evtservtom_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r2010_evtservtom_dados = {}
    r2010_evtservtom_dados['status'] = status
    r2010_evtservtom_dados['arquivo_original'] = 1
    if arquivo:
        r2010_evtservtom_dados['arquivo'] = arquivo.arquivo
    r2010_evtservtom_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2010_evtservtom_dados['identidade'] = doc.Reinf.evtServTom['id']
    evtServTom = doc.Reinf.evtServTom

    try:
        r2010_evtservtom_dados['indretif'] = read_from_xml(evtServTom.ideEvento.indRetif.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['nrrecibo'] = read_from_xml(evtServTom.ideEvento.nrRecibo.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['perapur'] = read_from_xml(evtServTom.ideEvento.perApur.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['tpamb'] = read_from_xml(evtServTom.ideEvento.tpAmb.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['procemi'] = read_from_xml(evtServTom.ideEvento.procEmi.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['verproc'] = read_from_xml(evtServTom.ideEvento.verProc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['tpinsc'] = read_from_xml(evtServTom.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['nrinsc'] = read_from_xml(evtServTom.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['tpinscestab'] = read_from_xml(evtServTom.infoServTom.ideEstabObra.tpInscEstab.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['nrinscestab'] = read_from_xml(evtServTom.infoServTom.ideEstabObra.nrInscEstab.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['indobra'] = read_from_xml(evtServTom.infoServTom.ideEstabObra.indObra.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['cnpjprestador'] = read_from_xml(evtServTom.infoServTom.ideEstabObra.idePrestServ.cnpjPrestador.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['vlrtotalbruto'] = read_from_xml(evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalBruto.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['vlrtotalbaseret'] = read_from_xml(evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalBaseRet.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['vlrtotalretprinc'] = read_from_xml(evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalRetPrinc.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['vlrtotalretadic'] = read_from_xml(evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalRetAdic.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['vlrtotalnretprinc'] = read_from_xml(evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalNRetPrinc.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['vlrtotalnretadic'] = read_from_xml(evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalNRetAdic.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r2010_evtservtom_dados['indcprb'] = read_from_xml(evtServTom.infoServTom.ideEstabObra.idePrestServ.indCPRB.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    r2010_evtservtom = r2010evtServTom.objects.create(**r2010_evtservtom_dados)

    if 'infoServTom' in dir(evtServTom) and 'ideEstabObra' in dir(evtServTom.infoServTom) and 'idePrestServ' in dir(evtServTom.infoServTom.ideEstabObra) and 'nfs' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ):

        for nfs in evtServTom.infoServTom.ideEstabObra.idePrestServ.nfs:

            r2010_nfs_dados = {}
            r2010_nfs_dados['r2010_evtservtom_id'] = r2010_evtservtom.id

            try:
                r2010_nfs_dados['serie'] = read_from_xml(nfs.serie.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2010_nfs_dados['numdocto'] = read_from_xml(nfs.numDocto.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2010_nfs_dados['dtemissaonf'] = read_from_xml(nfs.dtEmissaoNF.cdata, 'efdreinf', 'D', None)
            except AttributeError:
                pass

            try:
                r2010_nfs_dados['vlrbruto'] = read_from_xml(nfs.vlrBruto.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            try:
                r2010_nfs_dados['obs'] = read_from_xml(nfs.obs.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r2010_nfs = r2010nfs.objects.create(**r2010_nfs_dados)

            if 'infoTpServ' in dir(nfs):

                for infoTpServ in nfs.infoTpServ:

                    r2010_infotpserv_dados = {}
                    r2010_infotpserv_dados['r2010_nfs_id'] = r2010_nfs.id

                    try:
                        r2010_infotpserv_dados['tpservico'] = read_from_xml(infoTpServ.tpServico.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r2010_infotpserv_dados['vlrbaseret'] = read_from_xml(infoTpServ.vlrBaseRet.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2010_infotpserv_dados['vlrretencao'] = read_from_xml(infoTpServ.vlrRetencao.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2010_infotpserv_dados['vlrretsub'] = read_from_xml(infoTpServ.vlrRetSub.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2010_infotpserv_dados['vlrnretprinc'] = read_from_xml(infoTpServ.vlrNRetPrinc.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2010_infotpserv_dados['vlrservicos15'] = read_from_xml(infoTpServ.vlrServicos15.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2010_infotpserv_dados['vlrservicos20'] = read_from_xml(infoTpServ.vlrServicos20.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2010_infotpserv_dados['vlrservicos25'] = read_from_xml(infoTpServ.vlrServicos25.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2010_infotpserv_dados['vlradicional'] = read_from_xml(infoTpServ.vlrAdicional.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2010_infotpserv_dados['vlrnretadic'] = read_from_xml(infoTpServ.vlrNRetAdic.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r2010_infotpserv = r2010infoTpServ.objects.create(**r2010_infotpserv_dados)

    if 'infoServTom' in dir(evtServTom) and 'ideEstabObra' in dir(evtServTom.infoServTom) and 'idePrestServ' in dir(evtServTom.infoServTom.ideEstabObra) and 'infoProcRetPr' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ):

        for infoProcRetPr in evtServTom.infoServTom.ideEstabObra.idePrestServ.infoProcRetPr:

            r2010_infoprocretpr_dados = {}
            r2010_infoprocretpr_dados['r2010_evtservtom_id'] = r2010_evtservtom.id

            try:
                r2010_infoprocretpr_dados['tpprocretprinc'] = read_from_xml(infoProcRetPr.tpProcRetPrinc.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r2010_infoprocretpr_dados['nrprocretprinc'] = read_from_xml(infoProcRetPr.nrProcRetPrinc.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2010_infoprocretpr_dados['codsuspprinc'] = read_from_xml(infoProcRetPr.codSuspPrinc.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r2010_infoprocretpr_dados['valorprinc'] = read_from_xml(infoProcRetPr.valorPrinc.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            r2010_infoprocretpr = r2010infoProcRetPr.objects.create(**r2010_infoprocretpr_dados)

    if 'infoServTom' in dir(evtServTom) and 'ideEstabObra' in dir(evtServTom.infoServTom) and 'idePrestServ' in dir(evtServTom.infoServTom.ideEstabObra) and 'infoProcRetAd' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ):

        for infoProcRetAd in evtServTom.infoServTom.ideEstabObra.idePrestServ.infoProcRetAd:

            r2010_infoprocretad_dados = {}
            r2010_infoprocretad_dados['r2010_evtservtom_id'] = r2010_evtservtom.id

            try:
                r2010_infoprocretad_dados['tpprocretadic'] = read_from_xml(infoProcRetAd.tpProcRetAdic.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r2010_infoprocretad_dados['nrprocretadic'] = read_from_xml(infoProcRetAd.nrProcRetAdic.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2010_infoprocretad_dados['codsuspadic'] = read_from_xml(infoProcRetAd.codSuspAdic.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r2010_infoprocretad_dados['valoradic'] = read_from_xml(infoProcRetAd.valorAdic.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            r2010_infoprocretad = r2010infoProcRetAd.objects.create(**r2010_infoprocretad_dados)
    r2010_evtservtom_dados['evento'] = 'r2010'
    r2010_evtservtom_dados['id'] = r2010_evtservtom.id
    r2010_evtservtom_dados['identidade_evento'] = doc.Reinf.evtServTom['id']

    from emensageriapro.efdreinf.views.r2010_evtservtom_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r2010_evtservtom.id)

    return r2010_evtservtom_dados