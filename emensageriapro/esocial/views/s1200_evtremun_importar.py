# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1200.models import *
from emensageriapro.functions import read_from_xml



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
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1200_evtremun_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1200evtRemun.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1200_evtremun_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1200_evtremun_dados = {}
    s1200_evtremun_dados['status'] = status
    s1200_evtremun_dados['arquivo_original'] = 1
    if arquivo:
        s1200_evtremun_dados['arquivo'] = arquivo.arquivo
    s1200_evtremun_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1200_evtremun_dados['identidade'] = doc.eSocial.evtRemun['Id']
    evtRemun = doc.eSocial.evtRemun

    try:
        s1200_evtremun_dados['indretif'] = read_from_xml(evtRemun.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1200_evtremun_dados['nrrecibo'] = read_from_xml(evtRemun.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1200_evtremun_dados['indapuracao'] = read_from_xml(evtRemun.ideEvento.indApuracao.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1200_evtremun_dados['perapur'] = read_from_xml(evtRemun.ideEvento.perApur.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1200_evtremun_dados['tpamb'] = read_from_xml(evtRemun.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1200_evtremun_dados['procemi'] = read_from_xml(evtRemun.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1200_evtremun_dados['verproc'] = read_from_xml(evtRemun.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1200_evtremun_dados['tpinsc'] = read_from_xml(evtRemun.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1200_evtremun_dados['nrinsc'] = read_from_xml(evtRemun.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1200_evtremun_dados['cpftrab'] = read_from_xml(evtRemun.ideTrabalhador.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1200_evtremun_dados['nistrab'] = read_from_xml(evtRemun.ideTrabalhador.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1200_evtremun = s1200evtRemun.objects.create(**s1200_evtremun_dados)

    if 'ideTrabalhador' in dir(evtRemun) and 'infoMV' in dir(evtRemun.ideTrabalhador):

        for infoMV in evtRemun.ideTrabalhador.infoMV:

            s1200_infomv_dados = {}
            s1200_infomv_dados['s1200_evtremun_id'] = s1200_evtremun.id

            try:
                s1200_infomv_dados['indmv'] = read_from_xml(infoMV.indMV.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s1200_infomv = s1200infoMV.objects.create(**s1200_infomv_dados)

            if 'remunOutrEmpr' in dir(infoMV):

                for remunOutrEmpr in infoMV.remunOutrEmpr:

                    s1200_remunoutrempr_dados = {}
                    s1200_remunoutrempr_dados['s1200_infomv_id'] = s1200_infomv.id

                    try:
                        s1200_remunoutrempr_dados['tpinsc'] = read_from_xml(remunOutrEmpr.tpInsc.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1200_remunoutrempr_dados['nrinsc'] = read_from_xml(remunOutrEmpr.nrInsc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1200_remunoutrempr_dados['codcateg'] = read_from_xml(remunOutrEmpr.codCateg.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1200_remunoutrempr_dados['vlrremunoe'] = read_from_xml(remunOutrEmpr.vlrRemunOE.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    s1200_remunoutrempr = s1200remunOutrEmpr.objects.create(**s1200_remunoutrempr_dados)

    if 'ideTrabalhador' in dir(evtRemun) and 'infoComplem' in dir(evtRemun.ideTrabalhador):

        for infoComplem in evtRemun.ideTrabalhador.infoComplem:

            s1200_infocomplem_dados = {}
            s1200_infocomplem_dados['s1200_evtremun_id'] = s1200_evtremun.id

            try:
                s1200_infocomplem_dados['nmtrab'] = read_from_xml(infoComplem.nmTrab.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1200_infocomplem_dados['dtnascto'] = read_from_xml(infoComplem.dtNascto.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            s1200_infocomplem = s1200infoComplem.objects.create(**s1200_infocomplem_dados)

            if 'sucessaoVinc' in dir(infoComplem):

                for sucessaoVinc in infoComplem.sucessaoVinc:

                    s1200_sucessaovinc_dados = {}
                    s1200_sucessaovinc_dados['s1200_infocomplem_id'] = s1200_infocomplem.id

                    try:
                        s1200_sucessaovinc_dados['tpinscant'] = read_from_xml(sucessaoVinc.tpInscAnt.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1200_sucessaovinc_dados['cnpjempregant'] = read_from_xml(sucessaoVinc.cnpjEmpregAnt.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1200_sucessaovinc_dados['matricant'] = read_from_xml(sucessaoVinc.matricAnt.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1200_sucessaovinc_dados['dtadm'] = read_from_xml(sucessaoVinc.dtAdm.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s1200_sucessaovinc_dados['observacao'] = read_from_xml(sucessaoVinc.observacao.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1200_sucessaovinc = s1200sucessaoVinc.objects.create(**s1200_sucessaovinc_dados)

    if 'ideTrabalhador' in dir(evtRemun) and 'procJudTrab' in dir(evtRemun.ideTrabalhador):

        for procJudTrab in evtRemun.ideTrabalhador.procJudTrab:

            s1200_procjudtrab_dados = {}
            s1200_procjudtrab_dados['s1200_evtremun_id'] = s1200_evtremun.id

            try:
                s1200_procjudtrab_dados['tptrib'] = read_from_xml(procJudTrab.tpTrib.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1200_procjudtrab_dados['nrprocjud'] = read_from_xml(procJudTrab.nrProcJud.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1200_procjudtrab_dados['codsusp'] = read_from_xml(procJudTrab.codSusp.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s1200_procjudtrab = s1200procJudTrab.objects.create(**s1200_procjudtrab_dados)

    if 'ideTrabalhador' in dir(evtRemun) and 'infoInterm' in dir(evtRemun.ideTrabalhador):

        for infoInterm in evtRemun.ideTrabalhador.infoInterm:

            s1200_infointerm_dados = {}
            s1200_infointerm_dados['s1200_evtremun_id'] = s1200_evtremun.id

            try:
                s1200_infointerm_dados['qtddiasinterm'] = read_from_xml(infoInterm.qtdDiasInterm.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s1200_infointerm = s1200infoInterm.objects.create(**s1200_infointerm_dados)

    if 'dmDev' in dir(evtRemun):

        for dmDev in evtRemun.dmDev:

            s1200_dmdev_dados = {}
            s1200_dmdev_dados['s1200_evtremun_id'] = s1200_evtremun.id

            try:
                s1200_dmdev_dados['idedmdev'] = read_from_xml(dmDev.ideDmDev.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1200_dmdev_dados['codcateg'] = read_from_xml(dmDev.codCateg.cdata, 'esocial', 'N', None)
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
                                s1200_infoperapur_ideestablot_dados['tpinsc'] = read_from_xml(ideEstabLot.tpInsc.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1200_infoperapur_ideestablot_dados['nrinsc'] = read_from_xml(ideEstabLot.nrInsc.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1200_infoperapur_ideestablot_dados['codlotacao'] = read_from_xml(ideEstabLot.codLotacao.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1200_infoperapur_ideestablot_dados['qtddiasav'] = read_from_xml(ideEstabLot.qtdDiasAv.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass

                            s1200_infoperapur_ideestablot = s1200infoPerApurideEstabLot.objects.create(**s1200_infoperapur_ideestablot_dados)
        
                            if 'remunPerApur' in dir(ideEstabLot):
        
                                for remunPerApur in ideEstabLot.remunPerApur:
        
                                    s1200_infoperapur_remunperapur_dados = {}
                                    s1200_infoperapur_remunperapur_dados['s1200_infoperapur_ideestablot_id'] = s1200_infoperapur_ideestablot.id
                
                                    try:
                                        s1200_infoperapur_remunperapur_dados['matricula'] = read_from_xml(remunPerApur.matricula.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s1200_infoperapur_remunperapur_dados['indsimples'] = read_from_xml(remunPerApur.indSimples.cdata, 'esocial', 'N', None)
                                    except AttributeError:
                                        pass
        
                                    s1200_infoperapur_remunperapur = s1200infoPerApurremunPerApur.objects.create(**s1200_infoperapur_remunperapur_dados)
                
                                    if 'itensRemun' in dir(remunPerApur):
                
                                        for itensRemun in remunPerApur.itensRemun:
                
                                            s1200_infoperapur_itensremun_dados = {}
                                            s1200_infoperapur_itensremun_dados['s1200_infoperapur_remunperapur_id'] = s1200_infoperapur_remunperapur.id
                        
                                            try:
                                                s1200_infoperapur_itensremun_dados['codrubr'] = read_from_xml(itensRemun.codRubr.cdata, 'esocial', 'C', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1200_infoperapur_itensremun_dados['idetabrubr'] = read_from_xml(itensRemun.ideTabRubr.cdata, 'esocial', 'C', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1200_infoperapur_itensremun_dados['qtdrubr'] = read_from_xml(itensRemun.qtdRubr.cdata, 'esocial', 'N', 2)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1200_infoperapur_itensremun_dados['fatorrubr'] = read_from_xml(itensRemun.fatorRubr.cdata, 'esocial', 'N', 2)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1200_infoperapur_itensremun_dados['vrunit'] = read_from_xml(itensRemun.vrUnit.cdata, 'esocial', 'N', 2)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1200_infoperapur_itensremun_dados['vrrubr'] = read_from_xml(itensRemun.vrRubr.cdata, 'esocial', 'N', 2)
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
                                                        s1200_infoperapur_detoper_dados['cnpjoper'] = read_from_xml(detOper.cnpjOper.cdata, 'esocial', 'C', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s1200_infoperapur_detoper_dados['regans'] = read_from_xml(detOper.regANS.cdata, 'esocial', 'C', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s1200_infoperapur_detoper_dados['vrpgtit'] = read_from_xml(detOper.vrPgTit.cdata, 'esocial', 'N', 2)
                                                    except AttributeError:
                                                        pass
                        
                                                    s1200_infoperapur_detoper = s1200infoPerApurdetOper.objects.create(**s1200_infoperapur_detoper_dados)
                                
                                                    if 'detPlano' in dir(detOper):
                                
                                                        for detPlano in detOper.detPlano:
                                
                                                            s1200_infoperapur_detplano_dados = {}
                                                            s1200_infoperapur_detplano_dados['s1200_infoperapur_detoper_id'] = s1200_infoperapur_detoper.id
                                        
                                                            try:
                                                                s1200_infoperapur_detplano_dados['tpdep'] = read_from_xml(detPlano.tpDep.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1200_infoperapur_detplano_dados['cpfdep'] = read_from_xml(detPlano.cpfDep.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1200_infoperapur_detplano_dados['nmdep'] = read_from_xml(detPlano.nmDep.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1200_infoperapur_detplano_dados['dtnascto'] = read_from_xml(detPlano.dtNascto.cdata, 'esocial', 'D', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1200_infoperapur_detplano_dados['vlrpgdep'] = read_from_xml(detPlano.vlrPgDep.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                
                                                            s1200_infoperapur_detplano = s1200infoPerApurdetPlano.objects.create(**s1200_infoperapur_detplano_dados)
                
                                    if 'infoAgNocivo' in dir(remunPerApur):
                
                                        for infoAgNocivo in remunPerApur.infoAgNocivo:
                
                                            s1200_infoperapur_infoagnocivo_dados = {}
                                            s1200_infoperapur_infoagnocivo_dados['s1200_infoperapur_remunperapur_id'] = s1200_infoperapur_remunperapur.id
                        
                                            try:
                                                s1200_infoperapur_infoagnocivo_dados['grauexp'] = read_from_xml(infoAgNocivo.grauExp.cdata, 'esocial', 'N', None)
                                            except AttributeError:
                                                pass
                
                                            s1200_infoperapur_infoagnocivo = s1200infoPerApurinfoAgNocivo.objects.create(**s1200_infoperapur_infoagnocivo_dados)
                
                                    if 'infoTrabInterm' in dir(remunPerApur):
                
                                        for infoTrabInterm in remunPerApur.infoTrabInterm:
                
                                            s1200_infoperapur_infotrabinterm_dados = {}
                                            s1200_infoperapur_infotrabinterm_dados['s1200_infoperapur_remunperapur_id'] = s1200_infoperapur_remunperapur.id
                        
                                            try:
                                                s1200_infoperapur_infotrabinterm_dados['codconv'] = read_from_xml(infoTrabInterm.codConv.cdata, 'esocial', 'C', None)
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
                                s1200_infoperant_ideadc_dados['dtacconv'] = read_from_xml(ideADC.dtAcConv.cdata, 'esocial', 'D', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1200_infoperant_ideadc_dados['tpacconv'] = read_from_xml(ideADC.tpAcConv.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1200_infoperant_ideadc_dados['compacconv'] = read_from_xml(ideADC.compAcConv.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1200_infoperant_ideadc_dados['dtefacconv'] = read_from_xml(ideADC.dtEfAcConv.cdata, 'esocial', 'D', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1200_infoperant_ideadc_dados['dsc'] = read_from_xml(ideADC.dsc.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1200_infoperant_ideadc_dados['remunsuc'] = read_from_xml(ideADC.remunSuc.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s1200_infoperant_ideadc = s1200infoPerAntideADC.objects.create(**s1200_infoperant_ideadc_dados)
        
                            if 'idePeriodo' in dir(ideADC):
        
                                for idePeriodo in ideADC.idePeriodo:
        
                                    s1200_infoperant_ideperiodo_dados = {}
                                    s1200_infoperant_ideperiodo_dados['s1200_infoperant_ideadc_id'] = s1200_infoperant_ideadc.id
                
                                    try:
                                        s1200_infoperant_ideperiodo_dados['perref'] = read_from_xml(idePeriodo.perRef.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
        
                                    s1200_infoperant_ideperiodo = s1200infoPerAntidePeriodo.objects.create(**s1200_infoperant_ideperiodo_dados)
                
                                    if 'ideEstabLot' in dir(idePeriodo):
                
                                        for ideEstabLot in idePeriodo.ideEstabLot:
                
                                            s1200_infoperant_ideestablot_dados = {}
                                            s1200_infoperant_ideestablot_dados['s1200_infoperant_ideperiodo_id'] = s1200_infoperant_ideperiodo.id
                        
                                            try:
                                                s1200_infoperant_ideestablot_dados['tpinsc'] = read_from_xml(ideEstabLot.tpInsc.cdata, 'esocial', 'N', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1200_infoperant_ideestablot_dados['nrinsc'] = read_from_xml(ideEstabLot.nrInsc.cdata, 'esocial', 'C', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1200_infoperant_ideestablot_dados['codlotacao'] = read_from_xml(ideEstabLot.codLotacao.cdata, 'esocial', 'C', None)
                                            except AttributeError:
                                                pass
                
                                            s1200_infoperant_ideestablot = s1200infoPerAntideEstabLot.objects.create(**s1200_infoperant_ideestablot_dados)
                        
                                            if 'remunPerAnt' in dir(ideEstabLot):
                        
                                                for remunPerAnt in ideEstabLot.remunPerAnt:
                        
                                                    s1200_infoperant_remunperant_dados = {}
                                                    s1200_infoperant_remunperant_dados['s1200_infoperant_ideestablot_id'] = s1200_infoperant_ideestablot.id
                                
                                                    try:
                                                        s1200_infoperant_remunperant_dados['matricula'] = read_from_xml(remunPerAnt.matricula.cdata, 'esocial', 'C', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s1200_infoperant_remunperant_dados['indsimples'] = read_from_xml(remunPerAnt.indSimples.cdata, 'esocial', 'N', None)
                                                    except AttributeError:
                                                        pass
                        
                                                    s1200_infoperant_remunperant = s1200infoPerAntremunPerAnt.objects.create(**s1200_infoperant_remunperant_dados)
                                
                                                    if 'itensRemun' in dir(remunPerAnt):
                                
                                                        for itensRemun in remunPerAnt.itensRemun:
                                
                                                            s1200_infoperant_itensremun_dados = {}
                                                            s1200_infoperant_itensremun_dados['s1200_infoperant_remunperant_id'] = s1200_infoperant_remunperant.id
                                        
                                                            try:
                                                                s1200_infoperant_itensremun_dados['codrubr'] = read_from_xml(itensRemun.codRubr.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1200_infoperant_itensremun_dados['idetabrubr'] = read_from_xml(itensRemun.ideTabRubr.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1200_infoperant_itensremun_dados['qtdrubr'] = read_from_xml(itensRemun.qtdRubr.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1200_infoperant_itensremun_dados['fatorrubr'] = read_from_xml(itensRemun.fatorRubr.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1200_infoperant_itensremun_dados['vrunit'] = read_from_xml(itensRemun.vrUnit.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1200_infoperant_itensremun_dados['vrrubr'] = read_from_xml(itensRemun.vrRubr.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                
                                                            s1200_infoperant_itensremun = s1200infoPerAntitensRemun.objects.create(**s1200_infoperant_itensremun_dados)
                                
                                                    if 'infoAgNocivo' in dir(remunPerAnt):
                                
                                                        for infoAgNocivo in remunPerAnt.infoAgNocivo:
                                
                                                            s1200_infoperant_infoagnocivo_dados = {}
                                                            s1200_infoperant_infoagnocivo_dados['s1200_infoperant_remunperant_id'] = s1200_infoperant_remunperant.id
                                        
                                                            try:
                                                                s1200_infoperant_infoagnocivo_dados['grauexp'] = read_from_xml(infoAgNocivo.grauExp.cdata, 'esocial', 'N', None)
                                                            except AttributeError:
                                                                pass
                                
                                                            s1200_infoperant_infoagnocivo = s1200infoPerAntinfoAgNocivo.objects.create(**s1200_infoperant_infoagnocivo_dados)
                                
                                                    if 'infoTrabInterm' in dir(remunPerAnt):
                                
                                                        for infoTrabInterm in remunPerAnt.infoTrabInterm:
                                
                                                            s1200_infoperant_infotrabinterm_dados = {}
                                                            s1200_infoperant_infotrabinterm_dados['s1200_infoperant_remunperant_id'] = s1200_infoperant_remunperant.id
                                        
                                                            try:
                                                                s1200_infoperant_infotrabinterm_dados['codconv'] = read_from_xml(infoTrabInterm.codConv.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                
                                                            s1200_infoperant_infotrabinterm = s1200infoPerAntinfoTrabInterm.objects.create(**s1200_infoperant_infotrabinterm_dados)

            if 'infoComplCont' in dir(dmDev):

                for infoComplCont in dmDev.infoComplCont:

                    s1200_infoperant_infocomplcont_dados = {}
                    s1200_infoperant_infocomplcont_dados['s1200_dmdev_id'] = s1200_dmdev.id

                    try:
                        s1200_infoperant_infocomplcont_dados['codcbo'] = read_from_xml(infoComplCont.codCBO.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1200_infoperant_infocomplcont_dados['natatividade'] = read_from_xml(infoComplCont.natAtividade.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1200_infoperant_infocomplcont_dados['qtddiastrab'] = read_from_xml(infoComplCont.qtdDiasTrab.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1200_infoperant_infocomplcont = s1200infoPerAntinfoComplCont.objects.create(**s1200_infoperant_infocomplcont_dados)
    s1200_evtremun_dados['evento'] = 's1200'
    s1200_evtremun_dados['id'] = s1200_evtremun.id
    s1200_evtremun_dados['identidade_evento'] = doc.eSocial.evtRemun['Id']

    from emensageriapro.esocial.views.s1200_evtremun_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1200_evtremun.id)

    return s1200_evtremun_dados