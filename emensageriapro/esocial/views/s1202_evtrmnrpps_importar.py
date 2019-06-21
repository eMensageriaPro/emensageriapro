#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1202.models import *



def read_s1202_evtrmnrpps_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1202_evtrmnrpps_obj(request, doc, status, validar)
    return dados



def read_s1202_evtrmnrpps(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1202_evtrmnrpps_obj(request, doc, status, validar)

    s1202evtRmnRPPS.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s1202_evtrmnrpps_obj(request, doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1202_evtrmnrpps_dados = {}
    s1202_evtrmnrpps_dados['status'] = status
    s1202_evtrmnrpps_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1202_evtrmnrpps_dados['identidade'] = doc.eSocial.evtRmnRPPS['Id']
    evtRmnRPPS = doc.eSocial.evtRmnRPPS
    
    try:
        s1202_evtrmnrpps_dados['indretif'] = evtRmnRPPS.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        s1202_evtrmnrpps_dados['nrrecibo'] = evtRmnRPPS.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        s1202_evtrmnrpps_dados['indapuracao'] = evtRmnRPPS.ideEvento.indApuracao.cdata
    except AttributeError: 
        pass
    
    try:
        s1202_evtrmnrpps_dados['perapur'] = evtRmnRPPS.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        s1202_evtrmnrpps_dados['tpamb'] = evtRmnRPPS.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s1202_evtrmnrpps_dados['procemi'] = evtRmnRPPS.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s1202_evtrmnrpps_dados['verproc'] = evtRmnRPPS.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s1202_evtrmnrpps_dados['tpinsc'] = evtRmnRPPS.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s1202_evtrmnrpps_dados['nrinsc'] = evtRmnRPPS.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s1202_evtrmnrpps_dados['cpftrab'] = evtRmnRPPS.ideTrabalhador.cpfTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s1202_evtrmnrpps_dados['nistrab'] = evtRmnRPPS.ideTrabalhador.nisTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s1202_evtrmnrpps_dados['qtddepfp'] = evtRmnRPPS.ideTrabalhador.qtdDepFP.cdata
    except AttributeError: 
        pass
        
    s1202_evtrmnrpps = s1202evtRmnRPPS.objects.create(**s1202_evtrmnrpps_dados)
    
    if 'ideTrabalhador' in dir(evtRmnRPPS) and 'procJudTrab' in dir(evtRmnRPPS.ideTrabalhador):
    
        for procJudTrab in evtRmnRPPS.ideTrabalhador.procJudTrab:
    
            s1202_procjudtrab_dados = {}
            s1202_procjudtrab_dados['s1202_evtrmnrpps_id'] = s1202_evtrmnrpps.id
            
            try:
                s1202_procjudtrab_dados['tptrib'] = procJudTrab.tpTrib.cdata
            except AttributeError: 
                pass
            
            try:
                s1202_procjudtrab_dados['nrprocjud'] = procJudTrab.nrProcJud.cdata
            except AttributeError: 
                pass
            
            try:
                s1202_procjudtrab_dados['codsusp'] = procJudTrab.codSusp.cdata
            except AttributeError: 
                pass
    
            s1202_procjudtrab = s1202procJudTrab.objects.create(**s1202_procjudtrab_dados)
    
    if 'dmDev' in dir(evtRmnRPPS):
    
        for dmDev in evtRmnRPPS.dmDev:
    
            s1202_dmdev_dados = {}
            s1202_dmdev_dados['s1202_evtrmnrpps_id'] = s1202_evtrmnrpps.id
            
            try:
                s1202_dmdev_dados['idedmdev'] = dmDev.ideDmDev.cdata
            except AttributeError: 
                pass
            
            try:
                s1202_dmdev_dados['codcateg'] = dmDev.codCateg.cdata
            except AttributeError: 
                pass
    
            s1202_dmdev = s1202dmDev.objects.create(**s1202_dmdev_dados)
            
            if 'infoPerApur' in dir(dmDev):
            
                for infoPerApur in dmDev.infoPerApur:
            
                    s1202_infoperapur_dados = {}
                    s1202_infoperapur_dados['s1202_dmdev_id'] = s1202_dmdev.id
            
                    s1202_infoperapur = s1202infoPerApur.objects.create(**s1202_infoperapur_dados)
                    
                    if 'ideEstab' in dir(infoPerApur):
                    
                        for ideEstab in infoPerApur.ideEstab:
                    
                            s1202_infoperapur_ideestab_dados = {}
                            s1202_infoperapur_ideestab_dados['s1202_infoperapur_id'] = s1202_infoperapur.id
                            
                            try:
                                s1202_infoperapur_ideestab_dados['tpinsc'] = ideEstab.tpInsc.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1202_infoperapur_ideestab_dados['nrinsc'] = ideEstab.nrInsc.cdata
                            except AttributeError: 
                                pass
                    
                            s1202_infoperapur_ideestab = s1202infoPerApurideEstab.objects.create(**s1202_infoperapur_ideestab_dados)
                            
                            if 'remunPerApur' in dir(ideEstab):
                            
                                for remunPerApur in ideEstab.remunPerApur:
                            
                                    s1202_infoperapur_remunperapur_dados = {}
                                    s1202_infoperapur_remunperapur_dados['s1202_infoperapur_ideestab_id'] = s1202_infoperapur_ideestab.id
                                    
                                    try:
                                        s1202_infoperapur_remunperapur_dados['matricula'] = remunPerApur.matricula.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        s1202_infoperapur_remunperapur_dados['codcateg'] = remunPerApur.codCateg.cdata
                                    except AttributeError: 
                                        pass
                            
                                    s1202_infoperapur_remunperapur = s1202infoPerApurremunPerApur.objects.create(**s1202_infoperapur_remunperapur_dados)
                                    
                                    if 'itensRemun' in dir(remunPerApur):
                                    
                                        for itensRemun in remunPerApur.itensRemun:
                                    
                                            s1202_infoperapur_itensremun_dados = {}
                                            s1202_infoperapur_itensremun_dados['s1202_infoperapur_remunperapur_id'] = s1202_infoperapur_remunperapur.id
                                            
                                            try:
                                                s1202_infoperapur_itensremun_dados['codrubr'] = itensRemun.codRubr.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                s1202_infoperapur_itensremun_dados['idetabrubr'] = itensRemun.ideTabRubr.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                s1202_infoperapur_itensremun_dados['qtdrubr'] = itensRemun.qtdRubr.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                s1202_infoperapur_itensremun_dados['fatorrubr'] = itensRemun.fatorRubr.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                s1202_infoperapur_itensremun_dados['vrunit'] = itensRemun.vrUnit.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                s1202_infoperapur_itensremun_dados['vrrubr'] = itensRemun.vrRubr.cdata
                                            except AttributeError: 
                                                pass
                                    
                                            s1202_infoperapur_itensremun = s1202infoPerApuritensRemun.objects.create(**s1202_infoperapur_itensremun_dados)
                                    
                                    if 'infoSaudeColet' in dir(remunPerApur):
                                    
                                        for infoSaudeColet in remunPerApur.infoSaudeColet:
                                    
                                            s1202_infoperapur_infosaudecolet_dados = {}
                                            s1202_infoperapur_infosaudecolet_dados['s1202_infoperapur_remunperapur_id'] = s1202_infoperapur_remunperapur.id
                                    
                                            s1202_infoperapur_infosaudecolet = s1202infoPerApurinfoSaudeColet.objects.create(**s1202_infoperapur_infosaudecolet_dados)
                                            
                                            if 'detOper' in dir(infoSaudeColet):
                                            
                                                for detOper in infoSaudeColet.detOper:
                                            
                                                    s1202_infoperapur_detoper_dados = {}
                                                    s1202_infoperapur_detoper_dados['s1202_infoperapur_infosaudecolet_id'] = s1202_infoperapur_infosaudecolet.id
                                                    
                                                    try:
                                                        s1202_infoperapur_detoper_dados['cnpjoper'] = detOper.cnpjOper.cdata
                                                    except AttributeError: 
                                                        pass
                                                    
                                                    try:
                                                        s1202_infoperapur_detoper_dados['regans'] = detOper.regANS.cdata
                                                    except AttributeError: 
                                                        pass
                                                    
                                                    try:
                                                        s1202_infoperapur_detoper_dados['vrpgtit'] = detOper.vrPgTit.cdata
                                                    except AttributeError: 
                                                        pass
                                            
                                                    s1202_infoperapur_detoper = s1202infoPerApurdetOper.objects.create(**s1202_infoperapur_detoper_dados)
                                                    
                                                    if 'detPlano' in dir(detOper):
                                                    
                                                        for detPlano in detOper.detPlano:
                                                    
                                                            s1202_infoperapur_detplano_dados = {}
                                                            s1202_infoperapur_detplano_dados['s1202_infoperapur_detoper_id'] = s1202_infoperapur_detoper.id
                                                            
                                                            try:
                                                                s1202_infoperapur_detplano_dados['tpdep'] = detPlano.tpDep.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1202_infoperapur_detplano_dados['cpfdep'] = detPlano.cpfDep.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1202_infoperapur_detplano_dados['nmdep'] = detPlano.nmDep.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1202_infoperapur_detplano_dados['dtnascto'] = detPlano.dtNascto.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1202_infoperapur_detplano_dados['vlrpgdep'] = detPlano.vlrPgDep.cdata
                                                            except AttributeError: 
                                                                pass
                                                    
                                                            s1202_infoperapur_detplano = s1202infoPerApurdetPlano.objects.create(**s1202_infoperapur_detplano_dados)
            
            if 'infoPerAnt' in dir(dmDev):
            
                for infoPerAnt in dmDev.infoPerAnt:
            
                    s1202_infoperant_dados = {}
                    s1202_infoperant_dados['s1202_dmdev_id'] = s1202_dmdev.id
            
                    s1202_infoperant = s1202infoPerAnt.objects.create(**s1202_infoperant_dados)
                    
                    if 'ideADC' in dir(infoPerAnt):
                    
                        for ideADC in infoPerAnt.ideADC:
                    
                            s1202_infoperant_ideadc_dados = {}
                            s1202_infoperant_ideadc_dados['s1202_infoperant_id'] = s1202_infoperant.id
                            
                            try:
                                s1202_infoperant_ideadc_dados['dtlei'] = ideADC.dtLei.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1202_infoperant_ideadc_dados['nrlei'] = ideADC.nrLei.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1202_infoperant_ideadc_dados['dtef'] = ideADC.dtEf.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1202_infoperant_ideadc_dados['dtacconv'] = ideADC.dtAcConv.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1202_infoperant_ideadc_dados['tpacconv'] = ideADC.tpAcConv.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1202_infoperant_ideadc_dados['compacconv'] = ideADC.compAcConv.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1202_infoperant_ideadc_dados['dtefacconv'] = ideADC.dtEfAcConv.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1202_infoperant_ideadc_dados['dsc'] = ideADC.dsc.cdata
                            except AttributeError: 
                                pass
                    
                            s1202_infoperant_ideadc = s1202infoPerAntideADC.objects.create(**s1202_infoperant_ideadc_dados)
                            
                            if 'idePeriodo' in dir(ideADC):
                            
                                for idePeriodo in ideADC.idePeriodo:
                            
                                    s1202_infoperant_ideperiodo_dados = {}
                                    s1202_infoperant_ideperiodo_dados['s1202_infoperant_ideadc_id'] = s1202_infoperant_ideadc.id
                                    
                                    try:
                                        s1202_infoperant_ideperiodo_dados['perref'] = idePeriodo.perRef.cdata
                                    except AttributeError: 
                                        pass
                            
                                    s1202_infoperant_ideperiodo = s1202infoPerAntidePeriodo.objects.create(**s1202_infoperant_ideperiodo_dados)
                                    
                                    if 'ideEstab' in dir(idePeriodo):
                                    
                                        for ideEstab in idePeriodo.ideEstab:
                                    
                                            s1202_infoperant_ideestab_dados = {}
                                            s1202_infoperant_ideestab_dados['s1202_infoperant_ideperiodo_id'] = s1202_infoperant_ideperiodo.id
                                            
                                            try:
                                                s1202_infoperant_ideestab_dados['tpinsc'] = ideEstab.tpInsc.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                s1202_infoperant_ideestab_dados['nrinsc'] = ideEstab.nrInsc.cdata
                                            except AttributeError: 
                                                pass
                                    
                                            s1202_infoperant_ideestab = s1202infoPerAntideEstab.objects.create(**s1202_infoperant_ideestab_dados)
                                            
                                            if 'remunPerAnt' in dir(ideEstab):
                                            
                                                for remunPerAnt in ideEstab.remunPerAnt:
                                            
                                                    s1202_infoperant_remunperant_dados = {}
                                                    s1202_infoperant_remunperant_dados['s1202_infoperant_ideestab_id'] = s1202_infoperant_ideestab.id
                                                    
                                                    try:
                                                        s1202_infoperant_remunperant_dados['matricula'] = remunPerAnt.matricula.cdata
                                                    except AttributeError: 
                                                        pass
                                                    
                                                    try:
                                                        s1202_infoperant_remunperant_dados['codcateg'] = remunPerAnt.codCateg.cdata
                                                    except AttributeError: 
                                                        pass
                                            
                                                    s1202_infoperant_remunperant = s1202infoPerAntremunPerAnt.objects.create(**s1202_infoperant_remunperant_dados)
                                                    
                                                    if 'itensRemun' in dir(remunPerAnt):
                                                    
                                                        for itensRemun in remunPerAnt.itensRemun:
                                                    
                                                            s1202_infoperant_itensremun_dados = {}
                                                            s1202_infoperant_itensremun_dados['s1202_infoperant_remunperant_id'] = s1202_infoperant_remunperant.id
                                                            
                                                            try:
                                                                s1202_infoperant_itensremun_dados['codrubr'] = itensRemun.codRubr.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1202_infoperant_itensremun_dados['idetabrubr'] = itensRemun.ideTabRubr.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1202_infoperant_itensremun_dados['qtdrubr'] = itensRemun.qtdRubr.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1202_infoperant_itensremun_dados['fatorrubr'] = itensRemun.fatorRubr.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1202_infoperant_itensremun_dados['vrunit'] = itensRemun.vrUnit.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1202_infoperant_itensremun_dados['vrrubr'] = itensRemun.vrRubr.cdata
                                                            except AttributeError: 
                                                                pass
                                                    
                                                            s1202_infoperant_itensremun = s1202infoPerAntitensRemun.objects.create(**s1202_infoperant_itensremun_dados)    
    s1202_evtrmnrpps_dados['evento'] = 's1202'
    s1202_evtrmnrpps_dados['id'] = s1202_evtrmnrpps.id
    s1202_evtrmnrpps_dados['identidade_evento'] = doc.eSocial.evtRmnRPPS['Id']
    s1202_evtrmnrpps_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s1202_evtrmnrpps_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, s1202_evtrmnrpps.id)
    
    return s1202_evtrmnrpps_dados