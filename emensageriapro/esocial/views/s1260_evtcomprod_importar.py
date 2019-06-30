#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1260.models import *
from emensageriapro.functions import read_from_xml



def read_s1260_evtcomprod_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1260_evtcomprod_obj(request, doc, status, validar)
    return dados



def read_s1260_evtcomprod(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1260_evtcomprod_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1260evtComProd.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1260_evtcomprod_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1260_evtcomprod_dados = {}
    s1260_evtcomprod_dados['status'] = status
    s1260_evtcomprod_dados['arquivo_original'] = 1
    if arquivo:
        s1260_evtcomprod_dados['arquivo'] = arquivo.arquivo
    s1260_evtcomprod_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1260_evtcomprod_dados['identidade'] = doc.eSocial.evtComProd['Id']
    evtComProd = doc.eSocial.evtComProd

    try:
        s1260_evtcomprod_dados['indretif'] = read_from_xml(evtComProd.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['nrrecibo'] = read_from_xml(evtComProd.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['indapuracao'] = read_from_xml(evtComProd.ideEvento.indApuracao.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['perapur'] = read_from_xml(evtComProd.ideEvento.perApur.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['tpamb'] = read_from_xml(evtComProd.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['procemi'] = read_from_xml(evtComProd.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['verproc'] = read_from_xml(evtComProd.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['tpinsc'] = read_from_xml(evtComProd.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['nrinsc'] = read_from_xml(evtComProd.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['nrinscestabrural'] = read_from_xml(evtComProd.infoComProd.ideEstabel.nrInscEstabRural.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1260_evtcomprod = s1260evtComProd.objects.create(**s1260_evtcomprod_dados)

    if 'infoComProd' in dir(evtComProd) and 'ideEstabel' in dir(evtComProd.infoComProd) and 'tpComerc' in dir(evtComProd.infoComProd.ideEstabel):

        for tpComerc in evtComProd.infoComProd.ideEstabel.tpComerc:

            s1260_tpcomerc_dados = {}
            s1260_tpcomerc_dados['s1260_evtcomprod_id'] = s1260_evtcomprod.id

            try:
                s1260_tpcomerc_dados['indcomerc'] = read_from_xml(tpComerc.indComerc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1260_tpcomerc_dados['vrtotcom'] = read_from_xml(tpComerc.vrTotCom.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            s1260_tpcomerc = s1260tpComerc.objects.create(**s1260_tpcomerc_dados)

            if 'ideAdquir' in dir(tpComerc):

                for ideAdquir in tpComerc.ideAdquir:

                    s1260_ideadquir_dados = {}
                    s1260_ideadquir_dados['s1260_tpcomerc_id'] = s1260_tpcomerc.id

                    try:
                        s1260_ideadquir_dados['tpinsc'] = read_from_xml(ideAdquir.tpInsc.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1260_ideadquir_dados['nrinsc'] = read_from_xml(ideAdquir.nrInsc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1260_ideadquir_dados['vrcomerc'] = read_from_xml(ideAdquir.vrComerc.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    s1260_ideadquir = s1260ideAdquir.objects.create(**s1260_ideadquir_dados)

                    if 'nfs' in dir(ideAdquir):

                        for nfs in ideAdquir.nfs:

                            s1260_nfs_dados = {}
                            s1260_nfs_dados['s1260_ideadquir_id'] = s1260_ideadquir.id
        
                            try:
                                s1260_nfs_dados['serie'] = read_from_xml(nfs.serie.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1260_nfs_dados['nrdocto'] = read_from_xml(nfs.nrDocto.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1260_nfs_dados['dtemisnf'] = read_from_xml(nfs.dtEmisNF.cdata, 'esocial', 'D', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1260_nfs_dados['vlrbruto'] = read_from_xml(nfs.vlrBruto.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1260_nfs_dados['vrcpdescpr'] = read_from_xml(nfs.vrCPDescPR.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1260_nfs_dados['vrratdescpr'] = read_from_xml(nfs.vrRatDescPR.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1260_nfs_dados['vrsenardesc'] = read_from_xml(nfs.vrSenarDesc.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s1260_nfs = s1260nfs.objects.create(**s1260_nfs_dados)

            if 'infoProcJud' in dir(tpComerc):

                for infoProcJud in tpComerc.infoProcJud:

                    s1260_infoprocjud_dados = {}
                    s1260_infoprocjud_dados['s1260_tpcomerc_id'] = s1260_tpcomerc.id

                    try:
                        s1260_infoprocjud_dados['tpproc'] = read_from_xml(infoProcJud.tpProc.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1260_infoprocjud_dados['nrproc'] = read_from_xml(infoProcJud.nrProc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1260_infoprocjud_dados['codsusp'] = read_from_xml(infoProcJud.codSusp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1260_infoprocjud_dados['vrcpsusp'] = read_from_xml(infoProcJud.vrCPSusp.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s1260_infoprocjud_dados['vrratsusp'] = read_from_xml(infoProcJud.vrRatSusp.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s1260_infoprocjud_dados['vrsenarsusp'] = read_from_xml(infoProcJud.vrSenarSusp.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    s1260_infoprocjud = s1260infoProcJud.objects.create(**s1260_infoprocjud_dados)
    s1260_evtcomprod_dados['evento'] = 's1260'
    s1260_evtcomprod_dados['id'] = s1260_evtcomprod.id
    s1260_evtcomprod_dados['identidade_evento'] = doc.eSocial.evtComProd['Id']

    from emensageriapro.esocial.views.s1260_evtcomprod_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1260_evtcomprod.id)

    return s1260_evtcomprod_dados