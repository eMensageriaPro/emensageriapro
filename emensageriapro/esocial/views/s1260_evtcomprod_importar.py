#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1260.models import *



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

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_s1260_evtcomprod_obj(request, doc, status, validar, arquivo)

    s1260evtComProd.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s1260_evtcomprod_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1260_evtcomprod_dados = {}
    s1260_evtcomprod_dados['status'] = status
    s1260_evtcomprod_dados['arquivo_original'] = 1
    if arquivo:
        s1260_evtcomprod_dados['arquivo'] = arquivo
    s1260_evtcomprod_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1260_evtcomprod_dados['identidade'] = doc.eSocial.evtComProd['Id']
    evtComProd = doc.eSocial.evtComProd

    try:
        s1260_evtcomprod_dados['indretif'] = evtComProd.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['nrrecibo'] = evtComProd.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['indapuracao'] = evtComProd.ideEvento.indApuracao.cdata
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['perapur'] = evtComProd.ideEvento.perApur.cdata
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['tpamb'] = evtComProd.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['procemi'] = evtComProd.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['verproc'] = evtComProd.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['tpinsc'] = evtComProd.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['nrinsc'] = evtComProd.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    try:
        s1260_evtcomprod_dados['nrinscestabrural'] = evtComProd.infoComProd.ideEstabel.nrInscEstabRural.cdata
    except AttributeError:
        pass

    s1260_evtcomprod = s1260evtComProd.objects.create(**s1260_evtcomprod_dados)

    if 'infoComProd' in dir(evtComProd) and 'ideEstabel' in dir(evtComProd.infoComProd) and 'tpComerc' in dir(evtComProd.infoComProd.ideEstabel):

        for tpComerc in evtComProd.infoComProd.ideEstabel.tpComerc:

            s1260_tpcomerc_dados = {}
            s1260_tpcomerc_dados['s1260_evtcomprod_id'] = s1260_evtcomprod.id

            try:
                s1260_tpcomerc_dados['indcomerc'] = tpComerc.indComerc.cdata
            except AttributeError:
                pass

            try:
                s1260_tpcomerc_dados['vrtotcom'] = tpComerc.vrTotCom.cdata
            except AttributeError:
                pass

            s1260_tpcomerc = s1260tpComerc.objects.create(**s1260_tpcomerc_dados)

            if 'ideAdquir' in dir(tpComerc):

                for ideAdquir in tpComerc.ideAdquir:

                    s1260_ideadquir_dados = {}
                    s1260_ideadquir_dados['s1260_tpcomerc_id'] = s1260_tpcomerc.id

                    try:
                        s1260_ideadquir_dados['tpinsc'] = ideAdquir.tpInsc.cdata
                    except AttributeError:
                        pass

                    try:
                        s1260_ideadquir_dados['nrinsc'] = ideAdquir.nrInsc.cdata
                    except AttributeError:
                        pass

                    try:
                        s1260_ideadquir_dados['vrcomerc'] = ideAdquir.vrComerc.cdata
                    except AttributeError:
                        pass

                    s1260_ideadquir = s1260ideAdquir.objects.create(**s1260_ideadquir_dados)

                    if 'nfs' in dir(ideAdquir):

                        for nfs in ideAdquir.nfs:

                            s1260_nfs_dados = {}
                            s1260_nfs_dados['s1260_ideadquir_id'] = s1260_ideadquir.id
        
                            try:
                                s1260_nfs_dados['serie'] = nfs.serie.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1260_nfs_dados['nrdocto'] = nfs.nrDocto.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1260_nfs_dados['dtemisnf'] = nfs.dtEmisNF.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1260_nfs_dados['vlrbruto'] = nfs.vlrBruto.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1260_nfs_dados['vrcpdescpr'] = nfs.vrCPDescPR.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1260_nfs_dados['vrratdescpr'] = nfs.vrRatDescPR.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1260_nfs_dados['vrsenardesc'] = nfs.vrSenarDesc.cdata
                            except AttributeError:
                                pass

                            s1260_nfs = s1260nfs.objects.create(**s1260_nfs_dados)

            if 'infoProcJud' in dir(tpComerc):

                for infoProcJud in tpComerc.infoProcJud:

                    s1260_infoprocjud_dados = {}
                    s1260_infoprocjud_dados['s1260_tpcomerc_id'] = s1260_tpcomerc.id

                    try:
                        s1260_infoprocjud_dados['tpproc'] = infoProcJud.tpProc.cdata
                    except AttributeError:
                        pass

                    try:
                        s1260_infoprocjud_dados['nrproc'] = infoProcJud.nrProc.cdata
                    except AttributeError:
                        pass

                    try:
                        s1260_infoprocjud_dados['codsusp'] = infoProcJud.codSusp.cdata
                    except AttributeError:
                        pass

                    try:
                        s1260_infoprocjud_dados['vrcpsusp'] = infoProcJud.vrCPSusp.cdata
                    except AttributeError:
                        pass

                    try:
                        s1260_infoprocjud_dados['vrratsusp'] = infoProcJud.vrRatSusp.cdata
                    except AttributeError:
                        pass

                    try:
                        s1260_infoprocjud_dados['vrsenarsusp'] = infoProcJud.vrSenarSusp.cdata
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