#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s5011.models import *
from emensageriapro.functions import read_from_xml



def read_s5011_evtcs_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s5011_evtcs_obj(request, doc, status, validar)
    return dados



def read_s5011_evtcs(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s5011_evtcs_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s5011evtCS.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s5011_evtcs_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s5011_evtcs_dados = {}
    s5011_evtcs_dados['status'] = status
    s5011_evtcs_dados['arquivo_original'] = 1
    if arquivo:
        s5011_evtcs_dados['arquivo'] = arquivo.arquivo
    s5011_evtcs_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5011_evtcs_dados['identidade'] = doc.eSocial.evtCS['Id']
    evtCS = doc.eSocial.evtCS

    try:
        s5011_evtcs_dados['indapuracao'] = read_from_xml(evtCS.ideEvento.indApuracao.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s5011_evtcs_dados['perapur'] = read_from_xml(evtCS.ideEvento.perApur.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5011_evtcs_dados['tpinsc'] = read_from_xml(evtCS.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s5011_evtcs_dados['nrinsc'] = read_from_xml(evtCS.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5011_evtcs_dados['nrrecarqbase'] = read_from_xml(evtCS.infoCS.nrRecArqBase.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5011_evtcs_dados['indexistinfo'] = read_from_xml(evtCS.infoCS.indExistInfo.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s5011_evtcs_dados['classtrib'] = read_from_xml(evtCS.infoCS.infoContrib.classTrib.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s5011_evtcs = s5011evtCS.objects.create(**s5011_evtcs_dados)

    if 'infoCS' in dir(evtCS) and 'infoCPSeg' in dir(evtCS.infoCS):

        for infoCPSeg in evtCS.infoCS.infoCPSeg:

            s5011_infocpseg_dados = {}
            s5011_infocpseg_dados['s5011_evtcs_id'] = s5011_evtcs.id

            try:
                s5011_infocpseg_dados['vrdesccp'] = read_from_xml(infoCPSeg.vrDescCP.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            try:
                s5011_infocpseg_dados['vrcpseg'] = read_from_xml(infoCPSeg.vrCpSeg.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            s5011_infocpseg = s5011infoCPSeg.objects.create(**s5011_infocpseg_dados)

    if 'infoCS' in dir(evtCS) and 'infoContrib' in dir(evtCS.infoCS) and 'infoPJ' in dir(evtCS.infoCS.infoContrib):

        for infoPJ in evtCS.infoCS.infoContrib.infoPJ:

            s5011_infopj_dados = {}
            s5011_infopj_dados['s5011_evtcs_id'] = s5011_evtcs.id

            try:
                s5011_infopj_dados['indcoop'] = read_from_xml(infoPJ.indCoop.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s5011_infopj_dados['indconstr'] = read_from_xml(infoPJ.indConstr.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s5011_infopj_dados['indsubstpatr'] = read_from_xml(infoPJ.indSubstPatr.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s5011_infopj_dados['percredcontrib'] = read_from_xml(infoPJ.percRedContrib.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            s5011_infopj = s5011infoPJ.objects.create(**s5011_infopj_dados)

            if 'infoAtConc' in dir(infoPJ):

                for infoAtConc in infoPJ.infoAtConc:

                    s5011_infoatconc_dados = {}
                    s5011_infoatconc_dados['s5011_infopj_id'] = s5011_infopj.id

                    try:
                        s5011_infoatconc_dados['fatormes'] = read_from_xml(infoAtConc.fatorMes.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s5011_infoatconc_dados['fator13'] = read_from_xml(infoAtConc.fator13.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    s5011_infoatconc = s5011infoAtConc.objects.create(**s5011_infoatconc_dados)

    if 'infoCS' in dir(evtCS) and 'ideEstab' in dir(evtCS.infoCS):

        for ideEstab in evtCS.infoCS.ideEstab:

            s5011_ideestab_dados = {}
            s5011_ideestab_dados['s5011_evtcs_id'] = s5011_evtcs.id

            try:
                s5011_ideestab_dados['tpinsc'] = read_from_xml(ideEstab.tpInsc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s5011_ideestab_dados['nrinsc'] = read_from_xml(ideEstab.nrInsc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s5011_ideestab = s5011ideEstab.objects.create(**s5011_ideestab_dados)

            if 'infoEstab' in dir(ideEstab):

                for infoEstab in ideEstab.infoEstab:

                    s5011_infoestab_dados = {}
                    s5011_infoestab_dados['s5011_ideestab_id'] = s5011_ideestab.id

                    try:
                        s5011_infoestab_dados['cnaeprep'] = read_from_xml(infoEstab.cnaePrep.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s5011_infoestab_dados['aliqrat'] = read_from_xml(infoEstab.aliqRat.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s5011_infoestab_dados['fap'] = read_from_xml(infoEstab.fap.cdata, 'esocial', 'N', 4)
                    except AttributeError:
                        pass

                    try:
                        s5011_infoestab_dados['aliqratajust'] = read_from_xml(infoEstab.aliqRatAjust.cdata, 'esocial', 'N', 4)
                    except AttributeError:
                        pass

                    s5011_infoestab = s5011infoEstab.objects.create(**s5011_infoestab_dados)

                    if 'infoComplObra' in dir(infoEstab):

                        for infoComplObra in infoEstab.infoComplObra:

                            s5011_infocomplobra_dados = {}
                            s5011_infocomplobra_dados['s5011_infoestab_id'] = s5011_infoestab.id
        
                            try:
                                s5011_infocomplobra_dados['indsubstpatrobra'] = read_from_xml(infoComplObra.indSubstPatrObra.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass

                            s5011_infocomplobra = s5011infoComplObra.objects.create(**s5011_infocomplobra_dados)

            if 'ideLotacao' in dir(ideEstab):

                for ideLotacao in ideEstab.ideLotacao:

                    s5011_idelotacao_dados = {}
                    s5011_idelotacao_dados['s5011_ideestab_id'] = s5011_ideestab.id

                    try:
                        s5011_idelotacao_dados['codlotacao'] = read_from_xml(ideLotacao.codLotacao.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s5011_idelotacao_dados['fpas'] = read_from_xml(ideLotacao.fpas.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s5011_idelotacao_dados['codtercs'] = read_from_xml(ideLotacao.codTercs.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s5011_idelotacao_dados['codtercssusp'] = read_from_xml(ideLotacao.codTercsSusp.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s5011_idelotacao = s5011ideLotacao.objects.create(**s5011_idelotacao_dados)

                    if 'infoTercSusp' in dir(ideLotacao):

                        for infoTercSusp in ideLotacao.infoTercSusp:

                            s5011_infotercsusp_dados = {}
                            s5011_infotercsusp_dados['s5011_idelotacao_id'] = s5011_idelotacao.id
        
                            try:
                                s5011_infotercsusp_dados['codterc'] = read_from_xml(infoTercSusp.codTerc.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s5011_infotercsusp = s5011infoTercSusp.objects.create(**s5011_infotercsusp_dados)

                    if 'infoEmprParcial' in dir(ideLotacao):

                        for infoEmprParcial in ideLotacao.infoEmprParcial:

                            s5011_infoemprparcial_dados = {}
                            s5011_infoemprparcial_dados['s5011_idelotacao_id'] = s5011_idelotacao.id
        
                            try:
                                s5011_infoemprparcial_dados['tpinsccontrat'] = read_from_xml(infoEmprParcial.tpInscContrat.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_infoemprparcial_dados['nrinsccontrat'] = read_from_xml(infoEmprParcial.nrInscContrat.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_infoemprparcial_dados['tpinscprop'] = read_from_xml(infoEmprParcial.tpInscProp.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_infoemprparcial_dados['nrinscprop'] = read_from_xml(infoEmprParcial.nrInscProp.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_infoemprparcial_dados['cnoobra'] = read_from_xml(infoEmprParcial.cnoObra.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s5011_infoemprparcial = s5011infoEmprParcial.objects.create(**s5011_infoemprparcial_dados)

                    if 'dadosOpPort' in dir(ideLotacao):

                        for dadosOpPort in ideLotacao.dadosOpPort:

                            s5011_dadosopport_dados = {}
                            s5011_dadosopport_dados['s5011_idelotacao_id'] = s5011_idelotacao.id
        
                            try:
                                s5011_dadosopport_dados['cnpjopportuario'] = read_from_xml(dadosOpPort.cnpjOpPortuario.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_dadosopport_dados['aliqrat'] = read_from_xml(dadosOpPort.aliqRat.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_dadosopport_dados['fap'] = read_from_xml(dadosOpPort.fap.cdata, 'esocial', 'N', 4)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_dadosopport_dados['aliqratajust'] = read_from_xml(dadosOpPort.aliqRatAjust.cdata, 'esocial', 'N', 4)
                            except AttributeError:
                                pass

                            s5011_dadosopport = s5011dadosOpPort.objects.create(**s5011_dadosopport_dados)

                    if 'basesRemun' in dir(ideLotacao):

                        for basesRemun in ideLotacao.basesRemun:

                            s5011_basesremun_dados = {}
                            s5011_basesremun_dados['s5011_idelotacao_id'] = s5011_idelotacao.id
        
                            try:
                                s5011_basesremun_dados['indincid'] = read_from_xml(basesRemun.indIncid.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesremun_dados['codcateg'] = read_from_xml(basesRemun.codCateg.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesremun_dados['vrbccp00'] = read_from_xml(basesRemun.basesCp.vrBcCp00.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesremun_dados['vrbccp15'] = read_from_xml(basesRemun.basesCp.vrBcCp15.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesremun_dados['vrbccp20'] = read_from_xml(basesRemun.basesCp.vrBcCp20.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesremun_dados['vrbccp25'] = read_from_xml(basesRemun.basesCp.vrBcCp25.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesremun_dados['vrsuspbccp00'] = read_from_xml(basesRemun.basesCp.vrSuspBcCp00.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesremun_dados['vrsuspbccp15'] = read_from_xml(basesRemun.basesCp.vrSuspBcCp15.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesremun_dados['vrsuspbccp20'] = read_from_xml(basesRemun.basesCp.vrSuspBcCp20.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesremun_dados['vrsuspbccp25'] = read_from_xml(basesRemun.basesCp.vrSuspBcCp25.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesremun_dados['vrdescsest'] = read_from_xml(basesRemun.basesCp.vrDescSest.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesremun_dados['vrcalcsest'] = read_from_xml(basesRemun.basesCp.vrCalcSest.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesremun_dados['vrdescsenat'] = read_from_xml(basesRemun.basesCp.vrDescSenat.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesremun_dados['vrcalcsenat'] = read_from_xml(basesRemun.basesCp.vrCalcSenat.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesremun_dados['vrsalfam'] = read_from_xml(basesRemun.basesCp.vrSalFam.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesremun_dados['vrsalmat'] = read_from_xml(basesRemun.basesCp.vrSalMat.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s5011_basesremun = s5011basesRemun.objects.create(**s5011_basesremun_dados)

                    if 'basesAvNPort' in dir(ideLotacao):

                        for basesAvNPort in ideLotacao.basesAvNPort:

                            s5011_basesavnport_dados = {}
                            s5011_basesavnport_dados['s5011_idelotacao_id'] = s5011_idelotacao.id
        
                            try:
                                s5011_basesavnport_dados['vrbccp00'] = read_from_xml(basesAvNPort.vrBcCp00.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesavnport_dados['vrbccp15'] = read_from_xml(basesAvNPort.vrBcCp15.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesavnport_dados['vrbccp20'] = read_from_xml(basesAvNPort.vrBcCp20.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesavnport_dados['vrbccp25'] = read_from_xml(basesAvNPort.vrBcCp25.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesavnport_dados['vrbccp13'] = read_from_xml(basesAvNPort.vrBcCp13.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesavnport_dados['vrbcfgts'] = read_from_xml(basesAvNPort.vrBcFgts.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s5011_basesavnport_dados['vrdesccp'] = read_from_xml(basesAvNPort.vrDescCP.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s5011_basesavnport = s5011basesAvNPort.objects.create(**s5011_basesavnport_dados)

                    if 'infoSubstPatrOpPort' in dir(ideLotacao):

                        for infoSubstPatrOpPort in ideLotacao.infoSubstPatrOpPort:

                            s5011_infosubstpatropport_dados = {}
                            s5011_infosubstpatropport_dados['s5011_idelotacao_id'] = s5011_idelotacao.id
        
                            try:
                                s5011_infosubstpatropport_dados['cnpjopportuario'] = read_from_xml(infoSubstPatrOpPort.cnpjOpPortuario.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s5011_infosubstpatropport = s5011infoSubstPatrOpPort.objects.create(**s5011_infosubstpatropport_dados)

            if 'basesAquis' in dir(ideEstab):

                for basesAquis in ideEstab.basesAquis:

                    s5011_basesaquis_dados = {}
                    s5011_basesaquis_dados['s5011_ideestab_id'] = s5011_ideestab.id

                    try:
                        s5011_basesaquis_dados['indaquis'] = read_from_xml(basesAquis.indAquis.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s5011_basesaquis_dados['vlraquis'] = read_from_xml(basesAquis.vlrAquis.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s5011_basesaquis_dados['vrcpdescpr'] = read_from_xml(basesAquis.vrCPDescPR.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s5011_basesaquis_dados['vrcpnret'] = read_from_xml(basesAquis.vrCPNRet.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s5011_basesaquis_dados['vrratnret'] = read_from_xml(basesAquis.vrRatNRet.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s5011_basesaquis_dados['vrsenarnret'] = read_from_xml(basesAquis.vrSenarNRet.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s5011_basesaquis_dados['vrcpcalcpr'] = read_from_xml(basesAquis.vrCPCalcPR.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s5011_basesaquis_dados['vrratdescpr'] = read_from_xml(basesAquis.vrRatDescPR.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s5011_basesaquis_dados['vrratcalcpr'] = read_from_xml(basesAquis.vrRatCalcPR.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s5011_basesaquis_dados['vrsenardesc'] = read_from_xml(basesAquis.vrSenarDesc.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s5011_basesaquis_dados['vrsenarcalc'] = read_from_xml(basesAquis.vrSenarCalc.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    s5011_basesaquis = s5011basesAquis.objects.create(**s5011_basesaquis_dados)

            if 'basesComerc' in dir(ideEstab):

                for basesComerc in ideEstab.basesComerc:

                    s5011_basescomerc_dados = {}
                    s5011_basescomerc_dados['s5011_ideestab_id'] = s5011_ideestab.id

                    try:
                        s5011_basescomerc_dados['indcomerc'] = read_from_xml(basesComerc.indComerc.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s5011_basescomerc_dados['vrbccompr'] = read_from_xml(basesComerc.vrBcComPR.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s5011_basescomerc_dados['vrcpsusp'] = read_from_xml(basesComerc.vrCPSusp.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s5011_basescomerc_dados['vrratsusp'] = read_from_xml(basesComerc.vrRatSusp.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s5011_basescomerc_dados['vrsenarsusp'] = read_from_xml(basesComerc.vrSenarSusp.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    s5011_basescomerc = s5011basesComerc.objects.create(**s5011_basescomerc_dados)

            if 'infoCREstab' in dir(ideEstab):

                for infoCREstab in ideEstab.infoCREstab:

                    s5011_infocrestab_dados = {}
                    s5011_infocrestab_dados['s5011_ideestab_id'] = s5011_ideestab.id

                    try:
                        s5011_infocrestab_dados['tpcr'] = read_from_xml(infoCREstab.tpCR.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s5011_infocrestab_dados['vrcr'] = read_from_xml(infoCREstab.vrCR.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s5011_infocrestab_dados['vrsuspcr'] = read_from_xml(infoCREstab.vrSuspCR.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    s5011_infocrestab = s5011infoCREstab.objects.create(**s5011_infocrestab_dados)

    if 'infoCS' in dir(evtCS) and 'infoCRContrib' in dir(evtCS.infoCS):

        for infoCRContrib in evtCS.infoCS.infoCRContrib:

            s5011_infocrcontrib_dados = {}
            s5011_infocrcontrib_dados['s5011_evtcs_id'] = s5011_evtcs.id

            try:
                s5011_infocrcontrib_dados['tpcr'] = read_from_xml(infoCRContrib.tpCR.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s5011_infocrcontrib_dados['vrcr'] = read_from_xml(infoCRContrib.vrCR.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            try:
                s5011_infocrcontrib_dados['vrcrsusp'] = read_from_xml(infoCRContrib.vrCRSusp.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            s5011_infocrcontrib = s5011infoCRContrib.objects.create(**s5011_infocrcontrib_dados)
    s5011_evtcs_dados['evento'] = 's5011'
    s5011_evtcs_dados['id'] = s5011_evtcs.id
    s5011_evtcs_dados['identidade_evento'] = doc.eSocial.evtCS['Id']

    from emensageriapro.esocial.views.s5011_evtcs_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s5011_evtcs.id)

    return s5011_evtcs_dados