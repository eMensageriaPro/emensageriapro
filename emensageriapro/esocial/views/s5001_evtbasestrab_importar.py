#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s5001.models import *



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

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_s5001_evtbasestrab_obj(request, doc, status, validar, arquivo)

    s5001evtBasesTrab.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s5001_evtbasestrab_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s5001_evtbasestrab_dados = {}
    s5001_evtbasestrab_dados['status'] = status
    s5001_evtbasestrab_dados['arquivo_original'] = 1
    if arquivo:
        s5001_evtbasestrab_dados['arquivo'] = arquivo
    s5001_evtbasestrab_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5001_evtbasestrab_dados['identidade'] = doc.eSocial.evtBasesTrab['Id']
    evtBasesTrab = doc.eSocial.evtBasesTrab

    try:
        s5001_evtbasestrab_dados['nrrecarqbase'] = evtBasesTrab.ideEvento.nrRecArqBase.cdata
    except AttributeError:
        pass

    try:
        s5001_evtbasestrab_dados['indapuracao'] = evtBasesTrab.ideEvento.indApuracao.cdata
    except AttributeError:
        pass

    try:
        s5001_evtbasestrab_dados['perapur'] = evtBasesTrab.ideEvento.perApur.cdata
    except AttributeError:
        pass

    try:
        s5001_evtbasestrab_dados['tpinsc'] = evtBasesTrab.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s5001_evtbasestrab_dados['nrinsc'] = evtBasesTrab.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    try:
        s5001_evtbasestrab_dados['cpftrab'] = evtBasesTrab.ideTrabalhador.cpfTrab.cdata
    except AttributeError:
        pass

    s5001_evtbasestrab = s5001evtBasesTrab.objects.create(**s5001_evtbasestrab_dados)

    if 'ideTrabalhador' in dir(evtBasesTrab) and 'procJudTrab' in dir(evtBasesTrab.ideTrabalhador):

        for procJudTrab in evtBasesTrab.ideTrabalhador.procJudTrab:

            s5001_procjudtrab_dados = {}
            s5001_procjudtrab_dados['s5001_evtbasestrab_id'] = s5001_evtbasestrab.id

            try:
                s5001_procjudtrab_dados['nrprocjud'] = procJudTrab.nrProcJud.cdata
            except AttributeError:
                pass

            try:
                s5001_procjudtrab_dados['codsusp'] = procJudTrab.codSusp.cdata
            except AttributeError:
                pass

            s5001_procjudtrab = s5001procJudTrab.objects.create(**s5001_procjudtrab_dados)

    if 'infoCpCalc' in dir(evtBasesTrab):

        for infoCpCalc in evtBasesTrab.infoCpCalc:

            s5001_infocpcalc_dados = {}
            s5001_infocpcalc_dados['s5001_evtbasestrab_id'] = s5001_evtbasestrab.id

            try:
                s5001_infocpcalc_dados['tpcr'] = infoCpCalc.tpCR.cdata
            except AttributeError:
                pass

            try:
                s5001_infocpcalc_dados['vrcpseg'] = infoCpCalc.vrCpSeg.cdata
            except AttributeError:
                pass

            try:
                s5001_infocpcalc_dados['vrdescseg'] = infoCpCalc.vrDescSeg.cdata
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
                        s5001_ideestablot_dados['tpinsc'] = ideEstabLot.tpInsc.cdata
                    except AttributeError:
                        pass

                    try:
                        s5001_ideestablot_dados['nrinsc'] = ideEstabLot.nrInsc.cdata
                    except AttributeError:
                        pass

                    try:
                        s5001_ideestablot_dados['codlotacao'] = ideEstabLot.codLotacao.cdata
                    except AttributeError:
                        pass

                    s5001_ideestablot = s5001ideEstabLot.objects.create(**s5001_ideestablot_dados)

                    if 'infoCategIncid' in dir(ideEstabLot):

                        for infoCategIncid in ideEstabLot.infoCategIncid:

                            s5001_infocategincid_dados = {}
                            s5001_infocategincid_dados['s5001_ideestablot_id'] = s5001_ideestablot.id
        
                            try:
                                s5001_infocategincid_dados['matricula'] = infoCategIncid.matricula.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s5001_infocategincid_dados['codcateg'] = infoCategIncid.codCateg.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s5001_infocategincid_dados['indsimples'] = infoCategIncid.indSimples.cdata
                            except AttributeError:
                                pass

                            s5001_infocategincid = s5001infoCategIncid.objects.create(**s5001_infocategincid_dados)
        
                            if 'infoBaseCS' in dir(infoCategIncid):
        
                                for infoBaseCS in infoCategIncid.infoBaseCS:
        
                                    s5001_infobasecs_dados = {}
                                    s5001_infobasecs_dados['s5001_infocategincid_id'] = s5001_infocategincid.id
                
                                    try:
                                        s5001_infobasecs_dados['ind13'] = infoBaseCS.ind13.cdata
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s5001_infobasecs_dados['tpvalor'] = infoBaseCS.tpValor.cdata
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s5001_infobasecs_dados['valor'] = infoBaseCS.valor.cdata
                                    except AttributeError:
                                        pass
        
                                    s5001_infobasecs = s5001infoBaseCS.objects.create(**s5001_infobasecs_dados)
        
                            if 'calcTerc' in dir(infoCategIncid):
        
                                for calcTerc in infoCategIncid.calcTerc:
        
                                    s5001_calcterc_dados = {}
                                    s5001_calcterc_dados['s5001_infocategincid_id'] = s5001_infocategincid.id
                
                                    try:
                                        s5001_calcterc_dados['tpcr'] = calcTerc.tpCR.cdata
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s5001_calcterc_dados['vrcssegterc'] = calcTerc.vrCsSegTerc.cdata
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s5001_calcterc_dados['vrdescterc'] = calcTerc.vrDescTerc.cdata
                                    except AttributeError:
                                        pass
        
                                    s5001_calcterc = s5001calcTerc.objects.create(**s5001_calcterc_dados)
    s5001_evtbasestrab_dados['evento'] = 's5001'
    s5001_evtbasestrab_dados['id'] = s5001_evtbasestrab.id
    s5001_evtbasestrab_dados['identidade_evento'] = doc.eSocial.evtBasesTrab['Id']

    from emensageriapro.esocial.views.s5001_evtbasestrab_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s5001_evtbasestrab.id)

    return s5001_evtbasestrab_dados