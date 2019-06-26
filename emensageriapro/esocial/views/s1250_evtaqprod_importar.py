#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1250.models import *



def read_s1250_evtaqprod_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1250_evtaqprod_obj(request, doc, status, validar)
    return dados



def read_s1250_evtaqprod(request, dados, arquivo, validar=False):

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
    dados = read_s1250_evtaqprod_obj(request, doc, status, validar, arquivo)

    s1250evtAqProd.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s1250_evtaqprod_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1250_evtaqprod_dados = {}
    s1250_evtaqprod_dados['status'] = status
    s1250_evtaqprod_dados['arquivo_original'] = 1
    if arquivo:
        s1250_evtaqprod_dados['arquivo'] = arquivo
    s1250_evtaqprod_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1250_evtaqprod_dados['identidade'] = doc.eSocial.evtAqProd['Id']
    evtAqProd = doc.eSocial.evtAqProd

    try:
        s1250_evtaqprod_dados['indretif'] = evtAqProd.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['nrrecibo'] = evtAqProd.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['indapuracao'] = evtAqProd.ideEvento.indApuracao.cdata
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['perapur'] = evtAqProd.ideEvento.perApur.cdata
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['tpamb'] = evtAqProd.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['procemi'] = evtAqProd.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['verproc'] = evtAqProd.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['tpinsc'] = evtAqProd.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['nrinsc'] = evtAqProd.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['tpinscadq'] = evtAqProd.infoAquisProd.ideEstabAdquir.tpInscAdq.cdata
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['nrinscadq'] = evtAqProd.infoAquisProd.ideEstabAdquir.nrInscAdq.cdata
    except AttributeError:
        pass

    s1250_evtaqprod = s1250evtAqProd.objects.create(**s1250_evtaqprod_dados)

    if 'infoAquisProd' in dir(evtAqProd) and 'ideEstabAdquir' in dir(evtAqProd.infoAquisProd) and 'tpAquis' in dir(evtAqProd.infoAquisProd.ideEstabAdquir):

        for tpAquis in evtAqProd.infoAquisProd.ideEstabAdquir.tpAquis:

            s1250_tpaquis_dados = {}
            s1250_tpaquis_dados['s1250_evtaqprod_id'] = s1250_evtaqprod.id

            try:
                s1250_tpaquis_dados['indaquis'] = tpAquis.indAquis.cdata
            except AttributeError:
                pass

            try:
                s1250_tpaquis_dados['vlrtotaquis'] = tpAquis.vlrTotAquis.cdata
            except AttributeError:
                pass

            s1250_tpaquis = s1250tpAquis.objects.create(**s1250_tpaquis_dados)

            if 'ideProdutor' in dir(tpAquis):

                for ideProdutor in tpAquis.ideProdutor:

                    s1250_ideprodutor_dados = {}
                    s1250_ideprodutor_dados['s1250_tpaquis_id'] = s1250_tpaquis.id

                    try:
                        s1250_ideprodutor_dados['tpinscprod'] = ideProdutor.tpInscProd.cdata
                    except AttributeError:
                        pass

                    try:
                        s1250_ideprodutor_dados['nrinscprod'] = ideProdutor.nrInscProd.cdata
                    except AttributeError:
                        pass

                    try:
                        s1250_ideprodutor_dados['vlrbruto'] = ideProdutor.vlrBruto.cdata
                    except AttributeError:
                        pass

                    try:
                        s1250_ideprodutor_dados['vrcpdescpr'] = ideProdutor.vrCPDescPR.cdata
                    except AttributeError:
                        pass

                    try:
                        s1250_ideprodutor_dados['vrratdescpr'] = ideProdutor.vrRatDescPR.cdata
                    except AttributeError:
                        pass

                    try:
                        s1250_ideprodutor_dados['vrsenardesc'] = ideProdutor.vrSenarDesc.cdata
                    except AttributeError:
                        pass

                    try:
                        s1250_ideprodutor_dados['indopccp'] = ideProdutor.indOpcCP.cdata
                    except AttributeError:
                        pass

                    s1250_ideprodutor = s1250ideProdutor.objects.create(**s1250_ideprodutor_dados)

                    if 'nfs' in dir(ideProdutor):

                        for nfs in ideProdutor.nfs:

                            s1250_nfs_dados = {}
                            s1250_nfs_dados['s1250_ideprodutor_id'] = s1250_ideprodutor.id
        
                            try:
                                s1250_nfs_dados['serie'] = nfs.serie.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1250_nfs_dados['nrdocto'] = nfs.nrDocto.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1250_nfs_dados['dtemisnf'] = nfs.dtEmisNF.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1250_nfs_dados['vlrbruto'] = nfs.vlrBruto.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1250_nfs_dados['vrcpdescpr'] = nfs.vrCPDescPR.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1250_nfs_dados['vrratdescpr'] = nfs.vrRatDescPR.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1250_nfs_dados['vrsenardesc'] = nfs.vrSenarDesc.cdata
                            except AttributeError:
                                pass

                            s1250_nfs = s1250nfs.objects.create(**s1250_nfs_dados)

                    if 'infoProcJud' in dir(ideProdutor):

                        for infoProcJud in ideProdutor.infoProcJud:

                            s1250_infoprocjud_dados = {}
                            s1250_infoprocjud_dados['s1250_ideprodutor_id'] = s1250_ideprodutor.id
        
                            try:
                                s1250_infoprocjud_dados['nrprocjud'] = infoProcJud.nrProcJud.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1250_infoprocjud_dados['codsusp'] = infoProcJud.codSusp.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1250_infoprocjud_dados['vrcpnret'] = infoProcJud.vrCPNRet.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1250_infoprocjud_dados['vrratnret'] = infoProcJud.vrRatNRet.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1250_infoprocjud_dados['vrsenarnret'] = infoProcJud.vrSenarNRet.cdata
                            except AttributeError:
                                pass

                            s1250_infoprocjud = s1250infoProcJud.objects.create(**s1250_infoprocjud_dados)

            if 'infoProcJ' in dir(tpAquis):

                for infoProcJ in tpAquis.infoProcJ:

                    s1250_infoprocj_dados = {}
                    s1250_infoprocj_dados['s1250_tpaquis_id'] = s1250_tpaquis.id

                    try:
                        s1250_infoprocj_dados['nrprocjud'] = infoProcJ.nrProcJud.cdata
                    except AttributeError:
                        pass

                    try:
                        s1250_infoprocj_dados['codsusp'] = infoProcJ.codSusp.cdata
                    except AttributeError:
                        pass

                    try:
                        s1250_infoprocj_dados['vrcpnret'] = infoProcJ.vrCPNRet.cdata
                    except AttributeError:
                        pass

                    try:
                        s1250_infoprocj_dados['vrratnret'] = infoProcJ.vrRatNRet.cdata
                    except AttributeError:
                        pass

                    try:
                        s1250_infoprocj_dados['vrsenarnret'] = infoProcJ.vrSenarNRet.cdata
                    except AttributeError:
                        pass

                    s1250_infoprocj = s1250infoProcJ.objects.create(**s1250_infoprocj_dados)
    s1250_evtaqprod_dados['evento'] = 's1250'
    s1250_evtaqprod_dados['id'] = s1250_evtaqprod.id
    s1250_evtaqprod_dados['identidade_evento'] = doc.eSocial.evtAqProd['Id']

    from emensageriapro.esocial.views.s1250_evtaqprod_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1250_evtaqprod.id)

    return s1250_evtaqprod_dados