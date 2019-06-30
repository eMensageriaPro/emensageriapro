#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1250.models import *
from emensageriapro.functions import read_from_xml



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
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1250_evtaqprod_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1250evtAqProd.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1250_evtaqprod_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1250_evtaqprod_dados = {}
    s1250_evtaqprod_dados['status'] = status
    s1250_evtaqprod_dados['arquivo_original'] = 1
    if arquivo:
        s1250_evtaqprod_dados['arquivo'] = arquivo.arquivo
    s1250_evtaqprod_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1250_evtaqprod_dados['identidade'] = doc.eSocial.evtAqProd['Id']
    evtAqProd = doc.eSocial.evtAqProd

    try:
        s1250_evtaqprod_dados['indretif'] = read_from_xml(evtAqProd.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['nrrecibo'] = read_from_xml(evtAqProd.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['indapuracao'] = read_from_xml(evtAqProd.ideEvento.indApuracao.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['perapur'] = read_from_xml(evtAqProd.ideEvento.perApur.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['tpamb'] = read_from_xml(evtAqProd.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['procemi'] = read_from_xml(evtAqProd.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['verproc'] = read_from_xml(evtAqProd.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['tpinsc'] = read_from_xml(evtAqProd.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['nrinsc'] = read_from_xml(evtAqProd.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['tpinscadq'] = read_from_xml(evtAqProd.infoAquisProd.ideEstabAdquir.tpInscAdq.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1250_evtaqprod_dados['nrinscadq'] = read_from_xml(evtAqProd.infoAquisProd.ideEstabAdquir.nrInscAdq.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1250_evtaqprod = s1250evtAqProd.objects.create(**s1250_evtaqprod_dados)

    if 'infoAquisProd' in dir(evtAqProd) and 'ideEstabAdquir' in dir(evtAqProd.infoAquisProd) and 'tpAquis' in dir(evtAqProd.infoAquisProd.ideEstabAdquir):

        for tpAquis in evtAqProd.infoAquisProd.ideEstabAdquir.tpAquis:

            s1250_tpaquis_dados = {}
            s1250_tpaquis_dados['s1250_evtaqprod_id'] = s1250_evtaqprod.id

            try:
                s1250_tpaquis_dados['indaquis'] = read_from_xml(tpAquis.indAquis.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1250_tpaquis_dados['vlrtotaquis'] = read_from_xml(tpAquis.vlrTotAquis.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            s1250_tpaquis = s1250tpAquis.objects.create(**s1250_tpaquis_dados)

            if 'ideProdutor' in dir(tpAquis):

                for ideProdutor in tpAquis.ideProdutor:

                    s1250_ideprodutor_dados = {}
                    s1250_ideprodutor_dados['s1250_tpaquis_id'] = s1250_tpaquis.id

                    try:
                        s1250_ideprodutor_dados['tpinscprod'] = read_from_xml(ideProdutor.tpInscProd.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1250_ideprodutor_dados['nrinscprod'] = read_from_xml(ideProdutor.nrInscProd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1250_ideprodutor_dados['vlrbruto'] = read_from_xml(ideProdutor.vlrBruto.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s1250_ideprodutor_dados['vrcpdescpr'] = read_from_xml(ideProdutor.vrCPDescPR.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s1250_ideprodutor_dados['vrratdescpr'] = read_from_xml(ideProdutor.vrRatDescPR.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s1250_ideprodutor_dados['vrsenardesc'] = read_from_xml(ideProdutor.vrSenarDesc.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s1250_ideprodutor_dados['indopccp'] = read_from_xml(ideProdutor.indOpcCP.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1250_ideprodutor = s1250ideProdutor.objects.create(**s1250_ideprodutor_dados)

                    if 'nfs' in dir(ideProdutor):

                        for nfs in ideProdutor.nfs:

                            s1250_nfs_dados = {}
                            s1250_nfs_dados['s1250_ideprodutor_id'] = s1250_ideprodutor.id
        
                            try:
                                s1250_nfs_dados['serie'] = read_from_xml(nfs.serie.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1250_nfs_dados['nrdocto'] = read_from_xml(nfs.nrDocto.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1250_nfs_dados['dtemisnf'] = read_from_xml(nfs.dtEmisNF.cdata, 'esocial', 'D', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1250_nfs_dados['vlrbruto'] = read_from_xml(nfs.vlrBruto.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1250_nfs_dados['vrcpdescpr'] = read_from_xml(nfs.vrCPDescPR.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1250_nfs_dados['vrratdescpr'] = read_from_xml(nfs.vrRatDescPR.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1250_nfs_dados['vrsenardesc'] = read_from_xml(nfs.vrSenarDesc.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s1250_nfs = s1250nfs.objects.create(**s1250_nfs_dados)

                    if 'infoProcJud' in dir(ideProdutor):

                        for infoProcJud in ideProdutor.infoProcJud:

                            s1250_infoprocjud_dados = {}
                            s1250_infoprocjud_dados['s1250_ideprodutor_id'] = s1250_ideprodutor.id
        
                            try:
                                s1250_infoprocjud_dados['nrprocjud'] = read_from_xml(infoProcJud.nrProcJud.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1250_infoprocjud_dados['codsusp'] = read_from_xml(infoProcJud.codSusp.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1250_infoprocjud_dados['vrcpnret'] = read_from_xml(infoProcJud.vrCPNRet.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1250_infoprocjud_dados['vrratnret'] = read_from_xml(infoProcJud.vrRatNRet.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1250_infoprocjud_dados['vrsenarnret'] = read_from_xml(infoProcJud.vrSenarNRet.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s1250_infoprocjud = s1250infoProcJud.objects.create(**s1250_infoprocjud_dados)

            if 'infoProcJ' in dir(tpAquis):

                for infoProcJ in tpAquis.infoProcJ:

                    s1250_infoprocj_dados = {}
                    s1250_infoprocj_dados['s1250_tpaquis_id'] = s1250_tpaquis.id

                    try:
                        s1250_infoprocj_dados['nrprocjud'] = read_from_xml(infoProcJ.nrProcJud.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1250_infoprocj_dados['codsusp'] = read_from_xml(infoProcJ.codSusp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1250_infoprocj_dados['vrcpnret'] = read_from_xml(infoProcJ.vrCPNRet.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s1250_infoprocj_dados['vrratnret'] = read_from_xml(infoProcJ.vrRatNRet.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s1250_infoprocj_dados['vrsenarnret'] = read_from_xml(infoProcJ.vrSenarNRet.cdata, 'esocial', 'N', 2)
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