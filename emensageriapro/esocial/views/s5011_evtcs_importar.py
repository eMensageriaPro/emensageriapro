#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s5011.models import *



def read_s5011_evtcs_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s5011_evtcs_obj(doc, status, validar)
    return dados



def read_s5011_evtcs(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s5011_evtcs_obj(doc, status, validar)
    return dados



def read_s5011_evtcs_obj(doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s5011_evtcs_dados = {}
    s5011_evtcs_dados['status'] = status
    s5011_evtcs_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5011_evtcs_dados['identidade'] = doc.eSocial.evtCS['Id']
    evtCS = doc.eSocial.evtCS
    
    try:
        s5011_evtcs_dados['indapuracao'] = evtCS.ideEvento.indApuracao.cdata
    except AttributeError: 
        pass
    
    try:
        s5011_evtcs_dados['perapur'] = evtCS.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        s5011_evtcs_dados['tpinsc'] = evtCS.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s5011_evtcs_dados['nrinsc'] = evtCS.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s5011_evtcs_dados['nrrecarqbase'] = evtCS.infoCS.nrRecArqBase.cdata
    except AttributeError: 
        pass
    
    try:
        s5011_evtcs_dados['indexistinfo'] = evtCS.infoCS.indExistInfo.cdata
    except AttributeError: 
        pass
    
    try:
        s5011_evtcs_dados['classtrib'] = evtCS.infoCS.infoContrib.classTrib.cdata
    except AttributeError: 
        pass
        
    s5011_evtcs = s5011evtCS.objects.create(**s5011_evtcs_dados)
    
    if 'infoCPSeg' in dir(evtCS.infoCS):
    
        for infoCPSeg in evtCS.infoCS.infoCPSeg:
    
            s5011_infocpseg_dados = {}
            s5011_infocpseg_dados['s5011_evtcs_id'] = s5011_evtcs.id
            
            try:
                s5011_infocpseg_dados['vrdesccp'] = infoCPSeg.vrDescCP.cdata
            except AttributeError: 
                pass
            
            try:
                s5011_infocpseg_dados['vrcpseg'] = infoCPSeg.vrCpSeg.cdata
            except AttributeError: 
                pass
    
            s5011_infocpseg = s5011infoCPSeg.objects.create(**s5011_infocpseg_dados)
    
    if 'infoPJ' in dir(evtCS.infoCS.infoContrib):
    
        for infoPJ in evtCS.infoCS.infoContrib.infoPJ:
    
            s5011_infopj_dados = {}
            s5011_infopj_dados['s5011_evtcs_id'] = s5011_evtcs.id
            
            try:
                s5011_infopj_dados['indcoop'] = infoPJ.indCoop.cdata
            except AttributeError: 
                pass
            
            try:
                s5011_infopj_dados['indconstr'] = infoPJ.indConstr.cdata
            except AttributeError: 
                pass
            
            try:
                s5011_infopj_dados['indsubstpatr'] = infoPJ.indSubstPatr.cdata
            except AttributeError: 
                pass
            
            try:
                s5011_infopj_dados['percredcontrib'] = infoPJ.percRedContrib.cdata
            except AttributeError: 
                pass
    
            s5011_infopj = s5011infoPJ.objects.create(**s5011_infopj_dados)
            
            if 'infoAtConc' in dir(infoPJ):
            
                for infoAtConc in infoPJ.infoAtConc:
            
                    s5011_infoatconc_dados = {}
                    s5011_infoatconc_dados['s5011_infopj_id'] = s5011_infopj.id
                    
                    try:
                        s5011_infoatconc_dados['fatormes'] = infoAtConc.fatorMes.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_infoatconc_dados['fator13'] = infoAtConc.fator13.cdata
                    except AttributeError: 
                        pass
            
                    s5011_infoatconc = s5011infoAtConc.objects.create(**s5011_infoatconc_dados)
    
    if 'ideEstab' in dir(evtCS.infoCS):
    
        for ideEstab in evtCS.infoCS.ideEstab:
    
            s5011_ideestab_dados = {}
            s5011_ideestab_dados['s5011_evtcs_id'] = s5011_evtcs.id
            
            try:
                s5011_ideestab_dados['tpinsc'] = ideEstab.tpInsc.cdata
            except AttributeError: 
                pass
            
            try:
                s5011_ideestab_dados['nrinsc'] = ideEstab.nrInsc.cdata
            except AttributeError: 
                pass
    
            s5011_ideestab = s5011ideEstab.objects.create(**s5011_ideestab_dados)
            
            if 'infoEstab' in dir(ideEstab):
            
                for infoEstab in ideEstab.infoEstab:
            
                    s5011_infoestab_dados = {}
                    s5011_infoestab_dados['s5011_ideestab_id'] = s5011_ideestab.id
                    
                    try:
                        s5011_infoestab_dados['cnaeprep'] = infoEstab.cnaePrep.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_infoestab_dados['aliqrat'] = infoEstab.aliqRat.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_infoestab_dados['fap'] = infoEstab.fap.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_infoestab_dados['aliqratajust'] = infoEstab.aliqRatAjust.cdata
                    except AttributeError: 
                        pass
            
                    s5011_infoestab = s5011infoEstab.objects.create(**s5011_infoestab_dados)
                    
                    if 'infoComplObra' in dir(infoEstab):
                    
                        for infoComplObra in infoEstab.infoComplObra:
                    
                            s5011_infocomplobra_dados = {}
                            s5011_infocomplobra_dados['s5011_infoestab_id'] = s5011_infoestab.id
                            
                            try:
                                s5011_infocomplobra_dados['indsubstpatrobra'] = infoComplObra.indSubstPatrObra.cdata
                            except AttributeError: 
                                pass
                    
                            s5011_infocomplobra = s5011infoComplObra.objects.create(**s5011_infocomplobra_dados)
            
            if 'ideLotacao' in dir(ideEstab):
            
                for ideLotacao in ideEstab.ideLotacao:
            
                    s5011_idelotacao_dados = {}
                    s5011_idelotacao_dados['s5011_ideestab_id'] = s5011_ideestab.id
                    
                    try:
                        s5011_idelotacao_dados['codlotacao'] = ideLotacao.codLotacao.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_idelotacao_dados['fpas'] = ideLotacao.fpas.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_idelotacao_dados['codtercs'] = ideLotacao.codTercs.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_idelotacao_dados['codtercssusp'] = ideLotacao.codTercsSusp.cdata
                    except AttributeError: 
                        pass
            
                    s5011_idelotacao = s5011ideLotacao.objects.create(**s5011_idelotacao_dados)
                    
                    if 'infoTercSusp' in dir(ideLotacao):
                    
                        for infoTercSusp in ideLotacao.infoTercSusp:
                    
                            s5011_infotercsusp_dados = {}
                            s5011_infotercsusp_dados['s5011_idelotacao_id'] = s5011_idelotacao.id
                            
                            try:
                                s5011_infotercsusp_dados['codterc'] = infoTercSusp.codTerc.cdata
                            except AttributeError: 
                                pass
                    
                            s5011_infotercsusp = s5011infoTercSusp.objects.create(**s5011_infotercsusp_dados)
                    
                    if 'infoEmprParcial' in dir(ideLotacao):
                    
                        for infoEmprParcial in ideLotacao.infoEmprParcial:
                    
                            s5011_infoemprparcial_dados = {}
                            s5011_infoemprparcial_dados['s5011_idelotacao_id'] = s5011_idelotacao.id
                            
                            try:
                                s5011_infoemprparcial_dados['tpinsccontrat'] = infoEmprParcial.tpInscContrat.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_infoemprparcial_dados['nrinsccontrat'] = infoEmprParcial.nrInscContrat.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_infoemprparcial_dados['tpinscprop'] = infoEmprParcial.tpInscProp.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_infoemprparcial_dados['nrinscprop'] = infoEmprParcial.nrInscProp.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_infoemprparcial_dados['cnoobra'] = infoEmprParcial.cnoObra.cdata
                            except AttributeError: 
                                pass
                    
                            s5011_infoemprparcial = s5011infoEmprParcial.objects.create(**s5011_infoemprparcial_dados)
                    
                    if 'dadosOpPort' in dir(ideLotacao):
                    
                        for dadosOpPort in ideLotacao.dadosOpPort:
                    
                            s5011_dadosopport_dados = {}
                            s5011_dadosopport_dados['s5011_idelotacao_id'] = s5011_idelotacao.id
                            
                            try:
                                s5011_dadosopport_dados['cnpjopportuario'] = dadosOpPort.cnpjOpPortuario.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_dadosopport_dados['aliqrat'] = dadosOpPort.aliqRat.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_dadosopport_dados['fap'] = dadosOpPort.fap.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_dadosopport_dados['aliqratajust'] = dadosOpPort.aliqRatAjust.cdata
                            except AttributeError: 
                                pass
                    
                            s5011_dadosopport = s5011dadosOpPort.objects.create(**s5011_dadosopport_dados)
                    
                    if 'basesRemun' in dir(ideLotacao):
                    
                        for basesRemun in ideLotacao.basesRemun:
                    
                            s5011_basesremun_dados = {}
                            s5011_basesremun_dados['s5011_idelotacao_id'] = s5011_idelotacao.id
                            
                            try:
                                s5011_basesremun_dados['indincid'] = basesRemun.indIncid.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesremun_dados['codcateg'] = basesRemun.codCateg.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesremun_dados['vrbccp00'] = basesRemun.basesCp.vrBcCp00.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesremun_dados['vrbccp15'] = basesRemun.basesCp.vrBcCp15.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesremun_dados['vrbccp20'] = basesRemun.basesCp.vrBcCp20.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesremun_dados['vrbccp25'] = basesRemun.basesCp.vrBcCp25.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesremun_dados['vrsuspbccp00'] = basesRemun.basesCp.vrSuspBcCp00.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesremun_dados['vrsuspbccp15'] = basesRemun.basesCp.vrSuspBcCp15.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesremun_dados['vrsuspbccp20'] = basesRemun.basesCp.vrSuspBcCp20.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesremun_dados['vrsuspbccp25'] = basesRemun.basesCp.vrSuspBcCp25.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesremun_dados['vrdescsest'] = basesRemun.basesCp.vrDescSest.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesremun_dados['vrcalcsest'] = basesRemun.basesCp.vrCalcSest.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesremun_dados['vrdescsenat'] = basesRemun.basesCp.vrDescSenat.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesremun_dados['vrcalcsenat'] = basesRemun.basesCp.vrCalcSenat.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesremun_dados['vrsalfam'] = basesRemun.basesCp.vrSalFam.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesremun_dados['vrsalmat'] = basesRemun.basesCp.vrSalMat.cdata
                            except AttributeError: 
                                pass
                    
                            s5011_basesremun = s5011basesRemun.objects.create(**s5011_basesremun_dados)
                    
                    if 'basesAvNPort' in dir(ideLotacao):
                    
                        for basesAvNPort in ideLotacao.basesAvNPort:
                    
                            s5011_basesavnport_dados = {}
                            s5011_basesavnport_dados['s5011_idelotacao_id'] = s5011_idelotacao.id
                            
                            try:
                                s5011_basesavnport_dados['vrbccp00'] = basesAvNPort.vrBcCp00.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesavnport_dados['vrbccp15'] = basesAvNPort.vrBcCp15.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesavnport_dados['vrbccp20'] = basesAvNPort.vrBcCp20.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesavnport_dados['vrbccp25'] = basesAvNPort.vrBcCp25.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesavnport_dados['vrbccp13'] = basesAvNPort.vrBcCp13.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesavnport_dados['vrbcfgts'] = basesAvNPort.vrBcFgts.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s5011_basesavnport_dados['vrdesccp'] = basesAvNPort.vrDescCP.cdata
                            except AttributeError: 
                                pass
                    
                            s5011_basesavnport = s5011basesAvNPort.objects.create(**s5011_basesavnport_dados)
                    
                    if 'infoSubstPatrOpPort' in dir(ideLotacao):
                    
                        for infoSubstPatrOpPort in ideLotacao.infoSubstPatrOpPort:
                    
                            s5011_infosubstpatropport_dados = {}
                            s5011_infosubstpatropport_dados['s5011_idelotacao_id'] = s5011_idelotacao.id
                            
                            try:
                                s5011_infosubstpatropport_dados['cnpjopportuario'] = infoSubstPatrOpPort.cnpjOpPortuario.cdata
                            except AttributeError: 
                                pass
                    
                            s5011_infosubstpatropport = s5011infoSubstPatrOpPort.objects.create(**s5011_infosubstpatropport_dados)
            
            if 'basesAquis' in dir(ideEstab):
            
                for basesAquis in ideEstab.basesAquis:
            
                    s5011_basesaquis_dados = {}
                    s5011_basesaquis_dados['s5011_ideestab_id'] = s5011_ideestab.id
                    
                    try:
                        s5011_basesaquis_dados['indaquis'] = basesAquis.indAquis.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_basesaquis_dados['vlraquis'] = basesAquis.vlrAquis.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_basesaquis_dados['vrcpdescpr'] = basesAquis.vrCPDescPR.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_basesaquis_dados['vrcpnret'] = basesAquis.vrCPNRet.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_basesaquis_dados['vrratnret'] = basesAquis.vrRatNRet.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_basesaquis_dados['vrsenarnret'] = basesAquis.vrSenarNRet.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_basesaquis_dados['vrcpcalcpr'] = basesAquis.vrCPCalcPR.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_basesaquis_dados['vrratdescpr'] = basesAquis.vrRatDescPR.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_basesaquis_dados['vrratcalcpr'] = basesAquis.vrRatCalcPR.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_basesaquis_dados['vrsenardesc'] = basesAquis.vrSenarDesc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_basesaquis_dados['vrsenarcalc'] = basesAquis.vrSenarCalc.cdata
                    except AttributeError: 
                        pass
            
                    s5011_basesaquis = s5011basesAquis.objects.create(**s5011_basesaquis_dados)
            
            if 'basesComerc' in dir(ideEstab):
            
                for basesComerc in ideEstab.basesComerc:
            
                    s5011_basescomerc_dados = {}
                    s5011_basescomerc_dados['s5011_ideestab_id'] = s5011_ideestab.id
                    
                    try:
                        s5011_basescomerc_dados['indcomerc'] = basesComerc.indComerc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_basescomerc_dados['vrbccompr'] = basesComerc.vrBcComPR.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_basescomerc_dados['vrcpsusp'] = basesComerc.vrCPSusp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_basescomerc_dados['vrratsusp'] = basesComerc.vrRatSusp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_basescomerc_dados['vrsenarsusp'] = basesComerc.vrSenarSusp.cdata
                    except AttributeError: 
                        pass
            
                    s5011_basescomerc = s5011basesComerc.objects.create(**s5011_basescomerc_dados)
            
            if 'infoCREstab' in dir(ideEstab):
            
                for infoCREstab in ideEstab.infoCREstab:
            
                    s5011_infocrestab_dados = {}
                    s5011_infocrestab_dados['s5011_ideestab_id'] = s5011_ideestab.id
                    
                    try:
                        s5011_infocrestab_dados['tpcr'] = infoCREstab.tpCR.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_infocrestab_dados['vrcr'] = infoCREstab.vrCR.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s5011_infocrestab_dados['vrsuspcr'] = infoCREstab.vrSuspCR.cdata
                    except AttributeError: 
                        pass
            
                    s5011_infocrestab = s5011infoCREstab.objects.create(**s5011_infocrestab_dados)
    
    if 'infoCRContrib' in dir(evtCS.infoCS):
    
        for infoCRContrib in evtCS.infoCS.infoCRContrib:
    
            s5011_infocrcontrib_dados = {}
            s5011_infocrcontrib_dados['s5011_evtcs_id'] = s5011_evtcs.id
            
            try:
                s5011_infocrcontrib_dados['tpcr'] = infoCRContrib.tpCR.cdata
            except AttributeError: 
                pass
            
            try:
                s5011_infocrcontrib_dados['vrcr'] = infoCRContrib.vrCR.cdata
            except AttributeError: 
                pass
            
            try:
                s5011_infocrcontrib_dados['vrcrsusp'] = infoCRContrib.vrCRSusp.cdata
            except AttributeError: 
                pass
    
            s5011_infocrcontrib = s5011infoCRContrib.objects.create(**s5011_infocrcontrib_dados)    
    s5011_evtcs_dados['evento'] = 's5011'
    s5011_evtcs_dados['id'] = s5011_evtcs.id
    s5011_evtcs_dados['identidade_evento'] = doc.eSocial.evtCS['Id']
    s5011_evtcs_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s5011_evtcs_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(s5011_evtcs.id)
    return s5011_evtcs_dados