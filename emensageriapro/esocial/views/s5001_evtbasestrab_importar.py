# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s5001.models import *
from emensageriapro.functions import read_from_xml



def read_s5001_evtbasestrab_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s5001_evtbasestrab_obj(request, doc, status, validar)
    return dados



def read_s5001_evtbasestrab(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s5001_evtbasestrab_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s5001evtBasesTrab.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s5001_evtbasestrab_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s5001_evtbasestrab_dados = {}
    s5001_evtbasestrab_dados['status'] = status
    s5001_evtbasestrab_dados['arquivo_original'] = 1
    if arquivo:
        s5001_evtbasestrab_dados['arquivo'] = arquivo.arquivo
    s5001_evtbasestrab_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5001_evtbasestrab_dados['identidade'] = doc.eSocial.evtBasesTrab['Id']
    evtBasesTrab = doc.eSocial.evtBasesTrab

    try:
        s5001_evtbasestrab_dados['nrrecarqbase'] = read_from_xml(evtBasesTrab.ideEvento.nrRecArqBase.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5001_evtbasestrab_dados['indapuracao'] = read_from_xml(evtBasesTrab.ideEvento.indApuracao.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s5001_evtbasestrab_dados['perapur'] = read_from_xml(evtBasesTrab.ideEvento.perApur.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5001_evtbasestrab_dados['tpinsc'] = read_from_xml(evtBasesTrab.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s5001_evtbasestrab_dados['nrinsc'] = read_from_xml(evtBasesTrab.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5001_evtbasestrab_dados['cpftrab'] = read_from_xml(evtBasesTrab.ideTrabalhador.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s5001_evtbasestrab = s5001evtBasesTrab.objects.create(**s5001_evtbasestrab_dados)

    if 'ideTrabalhador' in dir(evtBasesTrab) and 'procJudTrab' in dir(evtBasesTrab.ideTrabalhador):

        for procJudTrab in evtBasesTrab.ideTrabalhador.procJudTrab:

            s5001_procjudtrab_dados = {}
            s5001_procjudtrab_dados['s5001_evtbasestrab_id'] = s5001_evtbasestrab.id

            try:
                s5001_procjudtrab_dados['nrprocjud'] = read_from_xml(procJudTrab.nrProcJud.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s5001_procjudtrab_dados['codsusp'] = read_from_xml(procJudTrab.codSusp.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s5001_procjudtrab = s5001procJudTrab.objects.create(**s5001_procjudtrab_dados)

    if 'infoCpCalc' in dir(evtBasesTrab):

        for infoCpCalc in evtBasesTrab.infoCpCalc:

            s5001_infocpcalc_dados = {}
            s5001_infocpcalc_dados['s5001_evtbasestrab_id'] = s5001_evtbasestrab.id

            try:
                s5001_infocpcalc_dados['tpcr'] = read_from_xml(infoCpCalc.tpCR.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s5001_infocpcalc_dados['vrcpseg'] = read_from_xml(infoCpCalc.vrCpSeg.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            try:
                s5001_infocpcalc_dados['vrdescseg'] = read_from_xml(infoCpCalc.vrDescSeg.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            s5001_infocpcalc = s5001infoCpCalc.objects.create(**s5001_infocpcalc_dados)

    if 'infoCp' in dir(evtBasesTrab):

        for infoCp in evtBasesTrab.infoCp:

            s5001_infocp_dados = {}
            s5001_infocp_dados['s5001_evtbasestrab_id'] = s5001_evtbasestrab.id

            s5001_infocp = s5001infoCp.objects.create(**s5001_infocp_dados)

            if 'ideEstabLot' in dir(infoCp):

                for ideEstabLot in infoCp.ideEstabLot:

                    s5001_ideestablot_dados = {}
                    s5001_ideestablot_dados['s5001_infocp_id'] = s5001_infocp.id

                    try:
                        s5001_ideestablot_dados['tpinsc'] = read_from_xml(ideEstabLot.tpInsc.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s5001_ideestablot_dados['nrinsc'] = read_from_xml(ideEstabLot.nrInsc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s5001_ideestablot_dados['codlotacao'] = read_from_xml(ideEstabLot.codLotacao.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s5001_ideestablot = s5001ideEstabLot.objects.create(**s5001_ideestablot_dados)

                    if 'infoCategIncid' in dir(ideEstabLot):

                        for infoCategIncid in ideEstabLot.infoCategIncid:

                            s5001_infocategincid_dados = {}
                            s5001_infocategincid_dados['s5001_ideestablot_id'] = s5001_ideestablot.id
        
                            try:
                                s5001_infocategincid_dados['matricula'] = read_from_xml(infoCategIncid.matricula.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s5001_infocategincid_dados['codcateg'] = read_from_xml(infoCategIncid.codCateg.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s5001_infocategincid_dados['indsimples'] = read_from_xml(infoCategIncid.indSimples.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass

                            s5001_infocategincid = s5001infoCategIncid.objects.create(**s5001_infocategincid_dados)
        
                            if 'infoBaseCS' in dir(infoCategIncid):
        
                                for infoBaseCS in infoCategIncid.infoBaseCS:
        
                                    s5001_infobasecs_dados = {}
                                    s5001_infobasecs_dados['s5001_infocategincid_id'] = s5001_infocategincid.id
                
                                    try:
                                        s5001_infobasecs_dados['ind13'] = read_from_xml(infoBaseCS.ind13.cdata, 'esocial', 'N', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s5001_infobasecs_dados['tpvalor'] = read_from_xml(infoBaseCS.tpValor.cdata, 'esocial', 'N', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s5001_infobasecs_dados['valor'] = read_from_xml(infoBaseCS.valor.cdata, 'esocial', 'N', 2)
                                    except AttributeError:
                                        pass
        
                                    s5001_infobasecs = s5001infoBaseCS.objects.create(**s5001_infobasecs_dados)
        
                            if 'calcTerc' in dir(infoCategIncid):
        
                                for calcTerc in infoCategIncid.calcTerc:
        
                                    s5001_calcterc_dados = {}
                                    s5001_calcterc_dados['s5001_infocategincid_id'] = s5001_infocategincid.id
                
                                    try:
                                        s5001_calcterc_dados['tpcr'] = read_from_xml(calcTerc.tpCR.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s5001_calcterc_dados['vrcssegterc'] = read_from_xml(calcTerc.vrCsSegTerc.cdata, 'esocial', 'N', 2)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s5001_calcterc_dados['vrdescterc'] = read_from_xml(calcTerc.vrDescTerc.cdata, 'esocial', 'N', 2)
                                    except AttributeError:
                                        pass
        
                                    s5001_calcterc = s5001calcTerc.objects.create(**s5001_calcterc_dados)
        
                            if 'infoPerRef' in dir(infoCategIncid):
        
                                for infoPerRef in infoCategIncid.infoPerRef:
        
                                    s5001_infoperref_dados = {}
                                    s5001_infoperref_dados['s5001_infocategincid_id'] = s5001_infocategincid.id
                
                                    try:
                                        s5001_infoperref_dados['perref'] = read_from_xml(infoPerRef.perRef.cdata, 'esocial', 'N', None)
                                    except AttributeError:
                                        pass
        
                                    s5001_infoperref = s5001infoPerRef.objects.create(**s5001_infoperref_dados)
                
                                    if 'detInfoPerRef' in dir(infoPerRef):
                
                                        for detInfoPerRef in infoPerRef.detInfoPerRef:
                
                                            s5001_detinfoperref_dados = {}
                                            s5001_detinfoperref_dados['s5001_infoperref_id'] = s5001_infoperref.id
                        
                                            try:
                                                s5001_detinfoperref_dados['ind13'] = read_from_xml(detInfoPerRef.ind13.cdata, 'esocial', 'N', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s5001_detinfoperref_dados['tpvalor'] = read_from_xml(detInfoPerRef.tpValor.cdata, 'esocial', 'N', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s5001_detinfoperref_dados['vrperref'] = read_from_xml(detInfoPerRef.vrPerRef.cdata, 'esocial', 'N', 2)
                                            except AttributeError:
                                                pass
                
                                            s5001_detinfoperref = s5001detInfoPerRef.objects.create(**s5001_detinfoperref_dados)
    s5001_evtbasestrab_dados['evento'] = 's5001'
    s5001_evtbasestrab_dados['id'] = s5001_evtbasestrab.id
    s5001_evtbasestrab_dados['identidade_evento'] = doc.eSocial.evtBasesTrab['Id']

    from emensageriapro.esocial.views.s5001_evtbasestrab_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s5001_evtbasestrab.id)

    return s5001_evtbasestrab_dados