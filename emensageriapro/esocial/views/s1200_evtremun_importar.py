#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1200.models import *



def read_s1200_evtremun_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1200_evtremun_obj(request, doc, status, validar)
    return dados



def read_s1200_evtremun(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1200_evtremun_obj(request, doc, status, validar)

    s1200evtRemun.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s1200_evtremun_obj(request, doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1200_evtremun_dados = {}
    s1200_evtremun_dados['status'] = status
    s1200_evtremun_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1200_evtremun_dados['identidade'] = doc.eSocial.evtRemun['Id']
    evtRemun = doc.eSocial.evtRemun
    
    try:
        s1200_evtremun_dados['indretif'] = evtRemun.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        s1200_evtremun_dados['nrrecibo'] = evtRemun.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        s1200_evtremun_dados['indapuracao'] = evtRemun.ideEvento.indApuracao.cdata
    except AttributeError: 
        pass
    
    try:
        s1200_evtremun_dados['perapur'] = evtRemun.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        s1200_evtremun_dados['tpamb'] = evtRemun.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s1200_evtremun_dados['procemi'] = evtRemun.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s1200_evtremun_dados['verproc'] = evtRemun.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s1200_evtremun_dados['tpinsc'] = evtRemun.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s1200_evtremun_dados['nrinsc'] = evtRemun.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s1200_evtremun_dados['cpftrab'] = evtRemun.ideTrabalhador.cpfTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s1200_evtremun_dados['nistrab'] = evtRemun.ideTrabalhador.nisTrab.cdata
    except AttributeError: 
        pass
        
    s1200_evtremun = s1200evtRemun.objects.create(**s1200_evtremun_dados)
    
    if 'ideTrabalhador' in dir(evtRemun) and 'infoMV' in dir(evtRemun.ideTrabalhador):
    
        for infoMV in evtRemun.ideTrabalhador.infoMV:
    
            s1200_infomv_dados = {}
            s1200_infomv_dados['s1200_evtremun_id'] = s1200_evtremun.id
            
            try:
                s1200_infomv_dados['indmv'] = infoMV.indMV.cdata
            except AttributeError: 
                pass
    
            s1200_infomv = s1200infoMV.objects.create(**s1200_infomv_dados)
            
            if 'remunOutrEmpr' in dir(infoMV):
            
                for remunOutrEmpr in infoMV.remunOutrEmpr:
            
                    s1200_remunoutrempr_dados = {}
                    s1200_remunoutrempr_dados['s1200_infomv_id'] = s1200_infomv.id
                    
                    try:
                        s1200_remunoutrempr_dados['tpinsc'] = remunOutrEmpr.tpInsc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1200_remunoutrempr_dados['nrinsc'] = remunOutrEmpr.nrInsc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1200_remunoutrempr_dados['codcateg'] = remunOutrEmpr.codCateg.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1200_remunoutrempr_dados['vlrremunoe'] = remunOutrEmpr.vlrRemunOE.cdata
                    except AttributeError: 
                        pass
            
                    s1200_remunoutrempr = s1200remunOutrEmpr.objects.create(**s1200_remunoutrempr_dados)
    
    if 'ideTrabalhador' in dir(evtRemun) and 'infoComplem' in dir(evtRemun.ideTrabalhador):
    
        for infoComplem in evtRemun.ideTrabalhador.infoComplem:
    
            s1200_infocomplem_dados = {}
            s1200_infocomplem_dados['s1200_evtremun_id'] = s1200_evtremun.id
            
            try:
                s1200_infocomplem_dados['nmtrab'] = infoComplem.nmTrab.cdata
            except AttributeError: 
                pass
            
            try:
                s1200_infocomplem_dados['dtnascto'] = infoComplem.dtNascto.cdata
            except AttributeError: 
                pass
    
            s1200_infocomplem = s1200infoComplem.objects.create(**s1200_infocomplem_dados)
            
            if 'sucessaoVinc' in dir(infoComplem):
            
                for sucessaoVinc in infoComplem.sucessaoVinc:
            
                    s1200_sucessaovinc_dados = {}
                    s1200_sucessaovinc_dados['s1200_infocomplem_id'] = s1200_infocomplem.id
                    
                    try:
                        s1200_sucessaovinc_dados['tpinscant'] = sucessaoVinc.tpInscAnt.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1200_sucessaovinc_dados['cnpjempregant'] = sucessaoVinc.cnpjEmpregAnt.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1200_sucessaovinc_dados['matricant'] = sucessaoVinc.matricAnt.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1200_sucessaovinc_dados['dtadm'] = sucessaoVinc.dtAdm.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1200_sucessaovinc_dados['observacao'] = sucessaoVinc.observacao.cdata
                    except AttributeError: 
                        pass
            
                    s1200_sucessaovinc = s1200sucessaoVinc.objects.create(**s1200_sucessaovinc_dados)
    
    if 'ideTrabalhador' in dir(evtRemun) and 'procJudTrab' in dir(evtRemun.ideTrabalhador):
    
        for procJudTrab in evtRemun.ideTrabalhador.procJudTrab:
    
            s1200_procjudtrab_dados = {}
            s1200_procjudtrab_dados['s1200_evtremun_id'] = s1200_evtremun.id
            
            try:
                s1200_procjudtrab_dados['tptrib'] = procJudTrab.tpTrib.cdata
            except AttributeError: 
                pass
            
            try:
                s1200_procjudtrab_dados['nrprocjud'] = procJudTrab.nrProcJud.cdata
            except AttributeError: 
                pass
            
            try:
                s1200_procjudtrab_dados['codsusp'] = procJudTrab.codSusp.cdata
            except AttributeError: 
                pass
    
            s1200_procjudtrab = s1200procJudTrab.objects.create(**s1200_procjudtrab_dados)
    
    if 'ideTrabalhador' in dir(evtRemun) and 'infoInterm' in dir(evtRemun.ideTrabalhador):
    
        for infoInterm in evtRemun.ideTrabalhador.infoInterm:
    
            s1200_infointerm_dados = {}
            s1200_infointerm_dados['s1200_evtremun_id'] = s1200_evtremun.id
            
            try:
                s1200_infointerm_dados['qtddiasinterm'] = infoInterm.qtdDiasInterm.cdata
            except AttributeError: 
                pass
    
            s1200_infointerm = s1200infoInterm.objects.create(**s1200_infointerm_dados)
    
    if 'dmDev' in dir(evtRemun):
    
        for dmDev in evtRemun.dmDev:
    
            s1200_dmdev_dados = {}
            s1200_dmdev_dados['s1200_evtremun_id'] = s1200_evtremun.id
            
            try:
                s1200_dmdev_dados['idedmdev'] = dmDev.ideDmDev.cdata
            except AttributeError: 
                pass
            
            try:
                s1200_dmdev_dados['codcateg'] = dmDev.codCateg.cdata
            except AttributeError: 
                pass
    
            s1200_dmdev = s1200dmDev.objects.create(**s1200_dmdev_dados)
            
            if 'infoPerApur' in dir(dmDev):
            
                for infoPerApur in dmDev.infoPerApur:
            
                    s1200_infoperapur_dados = {}
                    s1200_infoperapur_dados['s1200_dmdev_id'] = s1200_dmdev.id
            
                    s1200_infoperapur = s1200infoPerApur.objects.create(**s1200_infoperapur_dados)
                    
                    if 'ideEstabLot' in dir(infoPerApur):
                    
                        for ideEstabLot in infoPerApur.ideEstabLot:
                    
                            s1200_infoperapur_ideestablot_dados = {}
                            s1200_infoperapur_ideestablot_dados['s1200_infoperapur_id'] = s1200_infoperapur.id
                            
                            try:
                                s1200_infoperapur_ideestablot_dados['tpinsc'] = ideEstabLot.tpInsc.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1200_infoperapur_ideestablot_dados['nrinsc'] = ideEstabLot.nrInsc.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1200_infoperapur_ideestablot_dados['codlotacao'] = ideEstabLot.codLotacao.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1200_infoperapur_ideestablot_dados['qtddiasav'] = ideEstabLot.qtdDiasAv.cdata
                            except AttributeError: 
                                pass
                    
                            s1200_infoperapur_ideestablot = s1200infoPerApurideEstabLot.objects.create(**s1200_infoperapur_ideestablot_dados)
                            
                            if 'remunPerApur' in dir(ideEstabLot):
                            
                                for remunPerApur in ideEstabLot.remunPerApur:
                            
                                    s1200_infoperapur_remunperapur_dados = {}
                                    s1200_infoperapur_remunperapur_dados['s1200_infoperapur_ideestablot_id'] = s1200_infoperapur_ideestablot.id
                                    
                                    try:
                                        s1200_infoperapur_remunperapur_dados['matricula'] = remunPerApur.matricula.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        s1200_infoperapur_remunperapur_dados['indsimples'] = remunPerApur.indSimples.cdata
                                    except AttributeError: 
                                        pass
                            
                                    s1200_infoperapur_remunperapur = s1200infoPerApurremunPerApur.objects.create(**s1200_infoperapur_remunperapur_dados)
                                    
                                    if 'itensRemun' in dir(remunPerApur):
                                    
                                        for itensRemun in remunPerApur.itensRemun:
                                    
                                            s1200_infoperapur_itensremun_dados = {}
                                            s1200_infoperapur_itensremun_dados['s1200_infoperapur_remunperapur_id'] = s1200_infoperapur_remunperapur.id
                                            
                                            try:
                                                s1200_infoperapur_itensremun_dados['codrubr'] = itensRemun.codRubr.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                s1200_infoperapur_itensremun_dados['idetabrubr'] = itensRemun.ideTabRubr.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                s1200_infoperapur_itensremun_dados['qtdrubr'] = itensRemun.qtdRubr.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                s1200_infoperapur_itensremun_dados['fatorrubr'] = itensRemun.fatorRubr.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                s1200_infoperapur_itensremun_dados['vrunit'] = itensRemun.vrUnit.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                s1200_infoperapur_itensremun_dados['vrrubr'] = itensRemun.vrRubr.cdata
                                            except AttributeError: 
                                                pass
                                    
                                            s1200_infoperapur_itensremun = s1200infoPerApuritensRemun.objects.create(**s1200_infoperapur_itensremun_dados)
                                    
                                    if 'infoSaudeColet' in dir(remunPerApur):
                                    
                                        for infoSaudeColet in remunPerApur.infoSaudeColet:
                                    
                                            s1200_infoperapur_infosaudecolet_dados = {}
                                            s1200_infoperapur_infosaudecolet_dados['s1200_infoperapur_remunperapur_id'] = s1200_infoperapur_remunperapur.id
                                    
                                            s1200_infoperapur_infosaudecolet = s1200infoPerApurinfoSaudeColet.objects.create(**s1200_infoperapur_infosaudecolet_dados)
                                            
                                            if 'detOper' in dir(infoSaudeColet):
                                            
                                                for detOper in infoSaudeColet.detOper:
                                            
                                                    s1200_infoperapur_detoper_dados = {}
                                                    s1200_infoperapur_detoper_dados['s1200_infoperapur_infosaudecolet_id'] = s1200_infoperapur_infosaudecolet.id
                                                    
                                                    try:
                                                        s1200_infoperapur_detoper_dados['cnpjoper'] = detOper.cnpjOper.cdata
                                                    except AttributeError: 
                                                        pass
                                                    
                                                    try:
                                                        s1200_infoperapur_detoper_dados['regans'] = detOper.regANS.cdata
                                                    except AttributeError: 
                                                        pass
                                                    
                                                    try:
                                                        s1200_infoperapur_detoper_dados['vrpgtit'] = detOper.vrPgTit.cdata
                                                    except AttributeError: 
                                                        pass
                                            
                                                    s1200_infoperapur_detoper = s1200infoPerApurdetOper.objects.create(**s1200_infoperapur_detoper_dados)
                                                    
                                                    if 'detPlano' in dir(detOper):
                                                    
                                                        for detPlano in detOper.detPlano:
                                                    
                                                            s1200_infoperapur_detplano_dados = {}
                                                            s1200_infoperapur_detplano_dados['s1200_infoperapur_detoper_id'] = s1200_infoperapur_detoper.id
                                                            
                                                            try:
                                                                s1200_infoperapur_detplano_dados['tpdep'] = detPlano.tpDep.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1200_infoperapur_detplano_dados['cpfdep'] = detPlano.cpfDep.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1200_infoperapur_detplano_dados['nmdep'] = detPlano.nmDep.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1200_infoperapur_detplano_dados['dtnascto'] = detPlano.dtNascto.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1200_infoperapur_detplano_dados['vlrpgdep'] = detPlano.vlrPgDep.cdata
                                                            except AttributeError: 
                                                                pass
                                                    
                                                            s1200_infoperapur_detplano = s1200infoPerApurdetPlano.objects.create(**s1200_infoperapur_detplano_dados)
                                    
                                    if 'infoAgNocivo' in dir(remunPerApur):
                                    
                                        for infoAgNocivo in remunPerApur.infoAgNocivo:
                                    
                                            s1200_infoperapur_infoagnocivo_dados = {}
                                            s1200_infoperapur_infoagnocivo_dados['s1200_infoperapur_remunperapur_id'] = s1200_infoperapur_remunperapur.id
                                            
                                            try:
                                                s1200_infoperapur_infoagnocivo_dados['grauexp'] = infoAgNocivo.grauExp.cdata
                                            except AttributeError: 
                                                pass
                                    
                                            s1200_infoperapur_infoagnocivo = s1200infoPerApurinfoAgNocivo.objects.create(**s1200_infoperapur_infoagnocivo_dados)
                                    
                                    if 'infoTrabInterm' in dir(remunPerApur):
                                    
                                        for infoTrabInterm in remunPerApur.infoTrabInterm:
                                    
                                            s1200_infoperapur_infotrabinterm_dados = {}
                                            s1200_infoperapur_infotrabinterm_dados['s1200_infoperapur_remunperapur_id'] = s1200_infoperapur_remunperapur.id
                                            
                                            try:
                                                s1200_infoperapur_infotrabinterm_dados['codconv'] = infoTrabInterm.codConv.cdata
                                            except AttributeError: 
                                                pass
                                    
                                            s1200_infoperapur_infotrabinterm = s1200infoPerApurinfoTrabInterm.objects.create(**s1200_infoperapur_infotrabinterm_dados)
            
            if 'infoPerAnt' in dir(dmDev):
            
                for infoPerAnt in dmDev.infoPerAnt:
            
                    s1200_infoperant_dados = {}
                    s1200_infoperant_dados['s1200_dmdev_id'] = s1200_dmdev.id
            
                    s1200_infoperant = s1200infoPerAnt.objects.create(**s1200_infoperant_dados)
                    
                    if 'ideADC' in dir(infoPerAnt):
                    
                        for ideADC in infoPerAnt.ideADC:
                    
                            s1200_infoperant_ideadc_dados = {}
                            s1200_infoperant_ideadc_dados['s1200_infoperant_id'] = s1200_infoperant.id
                            
                            try:
                                s1200_infoperant_ideadc_dados['dtacconv'] = ideADC.dtAcConv.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1200_infoperant_ideadc_dados['tpacconv'] = ideADC.tpAcConv.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1200_infoperant_ideadc_dados['compacconv'] = ideADC.compAcConv.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1200_infoperant_ideadc_dados['dtefacconv'] = ideADC.dtEfAcConv.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1200_infoperant_ideadc_dados['dsc'] = ideADC.dsc.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1200_infoperant_ideadc_dados['remunsuc'] = ideADC.remunSuc.cdata
                            except AttributeError: 
                                pass
                    
                            s1200_infoperant_ideadc = s1200infoPerAntideADC.objects.create(**s1200_infoperant_ideadc_dados)
                            
                            if 'idePeriodo' in dir(ideADC):
                            
                                for idePeriodo in ideADC.idePeriodo:
                            
                                    s1200_infoperant_ideperiodo_dados = {}
                                    s1200_infoperant_ideperiodo_dados['s1200_infoperant_ideadc_id'] = s1200_infoperant_ideadc.id
                                    
                                    try:
                                        s1200_infoperant_ideperiodo_dados['perref'] = idePeriodo.perRef.cdata
                                    except AttributeError: 
                                        pass
                            
                                    s1200_infoperant_ideperiodo = s1200infoPerAntidePeriodo.objects.create(**s1200_infoperant_ideperiodo_dados)
                                    
                                    if 'ideEstabLot' in dir(idePeriodo):
                                    
                                        for ideEstabLot in idePeriodo.ideEstabLot:
                                    
                                            s1200_infoperant_ideestablot_dados = {}
                                            s1200_infoperant_ideestablot_dados['s1200_infoperant_ideperiodo_id'] = s1200_infoperant_ideperiodo.id
                                            
                                            try:
                                                s1200_infoperant_ideestablot_dados['tpinsc'] = ideEstabLot.tpInsc.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                s1200_infoperant_ideestablot_dados['nrinsc'] = ideEstabLot.nrInsc.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                s1200_infoperant_ideestablot_dados['codlotacao'] = ideEstabLot.codLotacao.cdata
                                            except AttributeError: 
                                                pass
                                    
                                            s1200_infoperant_ideestablot = s1200infoPerAntideEstabLot.objects.create(**s1200_infoperant_ideestablot_dados)
                                            
                                            if 'remunPerAnt' in dir(ideEstabLot):
                                            
                                                for remunPerAnt in ideEstabLot.remunPerAnt:
                                            
                                                    s1200_infoperant_remunperant_dados = {}
                                                    s1200_infoperant_remunperant_dados['s1200_infoperant_ideestablot_id'] = s1200_infoperant_ideestablot.id
                                                    
                                                    try:
                                                        s1200_infoperant_remunperant_dados['matricula'] = remunPerAnt.matricula.cdata
                                                    except AttributeError: 
                                                        pass
                                                    
                                                    try:
                                                        s1200_infoperant_remunperant_dados['indsimples'] = remunPerAnt.indSimples.cdata
                                                    except AttributeError: 
                                                        pass
                                            
                                                    s1200_infoperant_remunperant = s1200infoPerAntremunPerAnt.objects.create(**s1200_infoperant_remunperant_dados)
                                                    
                                                    if 'itensRemun' in dir(remunPerAnt):
                                                    
                                                        for itensRemun in remunPerAnt.itensRemun:
                                                    
                                                            s1200_infoperant_itensremun_dados = {}
                                                            s1200_infoperant_itensremun_dados['s1200_infoperant_remunperant_id'] = s1200_infoperant_remunperant.id
                                                            
                                                            try:
                                                                s1200_infoperant_itensremun_dados['codrubr'] = itensRemun.codRubr.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1200_infoperant_itensremun_dados['idetabrubr'] = itensRemun.ideTabRubr.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1200_infoperant_itensremun_dados['qtdrubr'] = itensRemun.qtdRubr.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1200_infoperant_itensremun_dados['fatorrubr'] = itensRemun.fatorRubr.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1200_infoperant_itensremun_dados['vrunit'] = itensRemun.vrUnit.cdata
                                                            except AttributeError: 
                                                                pass
                                                            
                                                            try:
                                                                s1200_infoperant_itensremun_dados['vrrubr'] = itensRemun.vrRubr.cdata
                                                            except AttributeError: 
                                                                pass
                                                    
                                                            s1200_infoperant_itensremun = s1200infoPerAntitensRemun.objects.create(**s1200_infoperant_itensremun_dados)
                                                    
                                                    if 'infoAgNocivo' in dir(remunPerAnt):
                                                    
                                                        for infoAgNocivo in remunPerAnt.infoAgNocivo:
                                                    
                                                            s1200_infoperant_infoagnocivo_dados = {}
                                                            s1200_infoperant_infoagnocivo_dados['s1200_infoperant_remunperant_id'] = s1200_infoperant_remunperant.id
                                                            
                                                            try:
                                                                s1200_infoperant_infoagnocivo_dados['grauexp'] = infoAgNocivo.grauExp.cdata
                                                            except AttributeError: 
                                                                pass
                                                    
                                                            s1200_infoperant_infoagnocivo = s1200infoPerAntinfoAgNocivo.objects.create(**s1200_infoperant_infoagnocivo_dados)
                                                    
                                                    if 'infoTrabInterm' in dir(remunPerAnt):
                                                    
                                                        for infoTrabInterm in remunPerAnt.infoTrabInterm:
                                                    
                                                            s1200_infoperant_infotrabinterm_dados = {}
                                                            s1200_infoperant_infotrabinterm_dados['s1200_infoperant_remunperant_id'] = s1200_infoperant_remunperant.id
                                                            
                                                            try:
                                                                s1200_infoperant_infotrabinterm_dados['codconv'] = infoTrabInterm.codConv.cdata
                                                            except AttributeError: 
                                                                pass
                                                    
                                                            s1200_infoperant_infotrabinterm = s1200infoPerAntinfoTrabInterm.objects.create(**s1200_infoperant_infotrabinterm_dados)
            
            if 'infoComplCont' in dir(dmDev):
            
                for infoComplCont in dmDev.infoComplCont:
            
                    s1200_infoperant_infocomplcont_dados = {}
                    s1200_infoperant_infocomplcont_dados['s1200_dmdev_id'] = s1200_dmdev.id
                    
                    try:
                        s1200_infoperant_infocomplcont_dados['codcbo'] = infoComplCont.codCBO.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1200_infoperant_infocomplcont_dados['natatividade'] = infoComplCont.natAtividade.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1200_infoperant_infocomplcont_dados['qtddiastrab'] = infoComplCont.qtdDiasTrab.cdata
                    except AttributeError: 
                        pass
            
                    s1200_infoperant_infocomplcont = s1200infoPerAntinfoComplCont.objects.create(**s1200_infoperant_infocomplcont_dados)    
    s1200_evtremun_dados['evento'] = 's1200'
    s1200_evtremun_dados['id'] = s1200_evtremun.id
    s1200_evtremun_dados['identidade_evento'] = doc.eSocial.evtRemun['Id']
    s1200_evtremun_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s1200_evtremun_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, s1200_evtremun.id)
    
    return s1200_evtremun_dados