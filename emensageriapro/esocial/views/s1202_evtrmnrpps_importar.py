# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1202.models import *
from emensageriapro.functions import read_from_xml



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
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1202_evtrmnrpps_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1202evtRmnRPPS.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1202_evtrmnrpps_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1202_evtrmnrpps_dados = {}
    s1202_evtrmnrpps_dados['status'] = status
    s1202_evtrmnrpps_dados['arquivo_original'] = 1
    if arquivo:
        s1202_evtrmnrpps_dados['arquivo'] = arquivo.arquivo
    s1202_evtrmnrpps_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1202_evtrmnrpps_dados['identidade'] = doc.eSocial.evtRmnRPPS['Id']
    evtRmnRPPS = doc.eSocial.evtRmnRPPS

    try:
        s1202_evtrmnrpps_dados['indretif'] = read_from_xml(evtRmnRPPS.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1202_evtrmnrpps_dados['nrrecibo'] = read_from_xml(evtRmnRPPS.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1202_evtrmnrpps_dados['indapuracao'] = read_from_xml(evtRmnRPPS.ideEvento.indApuracao.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1202_evtrmnrpps_dados['perapur'] = read_from_xml(evtRmnRPPS.ideEvento.perApur.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1202_evtrmnrpps_dados['tpamb'] = read_from_xml(evtRmnRPPS.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1202_evtrmnrpps_dados['procemi'] = read_from_xml(evtRmnRPPS.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1202_evtrmnrpps_dados['verproc'] = read_from_xml(evtRmnRPPS.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1202_evtrmnrpps_dados['tpinsc'] = read_from_xml(evtRmnRPPS.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1202_evtrmnrpps_dados['nrinsc'] = read_from_xml(evtRmnRPPS.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1202_evtrmnrpps_dados['cpftrab'] = read_from_xml(evtRmnRPPS.ideTrabalhador.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1202_evtrmnrpps_dados['nistrab'] = read_from_xml(evtRmnRPPS.ideTrabalhador.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1202_evtrmnrpps_dados['qtddepfp'] = read_from_xml(evtRmnRPPS.ideTrabalhador.qtdDepFP.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    s1202_evtrmnrpps = s1202evtRmnRPPS.objects.create(**s1202_evtrmnrpps_dados)

    if 'ideTrabalhador' in dir(evtRmnRPPS) and 'procJudTrab' in dir(evtRmnRPPS.ideTrabalhador):

        for procJudTrab in evtRmnRPPS.ideTrabalhador.procJudTrab:

            s1202_procjudtrab_dados = {}
            s1202_procjudtrab_dados['s1202_evtrmnrpps_id'] = s1202_evtrmnrpps.id

            try:
                s1202_procjudtrab_dados['tptrib'] = read_from_xml(procJudTrab.tpTrib.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1202_procjudtrab_dados['nrprocjud'] = read_from_xml(procJudTrab.nrProcJud.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1202_procjudtrab_dados['codsusp'] = read_from_xml(procJudTrab.codSusp.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s1202_procjudtrab = s1202procJudTrab.objects.create(**s1202_procjudtrab_dados)

    if 'dmDev' in dir(evtRmnRPPS):

        for dmDev in evtRmnRPPS.dmDev:

            s1202_dmdev_dados = {}
            s1202_dmdev_dados['s1202_evtrmnrpps_id'] = s1202_evtrmnrpps.id

            try:
                s1202_dmdev_dados['idedmdev'] = read_from_xml(dmDev.ideDmDev.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1202_dmdev_dados['codcateg'] = read_from_xml(dmDev.codCateg.cdata, 'esocial', 'N', None)
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
                                s1202_infoperapur_ideestab_dados['tpinsc'] = read_from_xml(ideEstab.tpInsc.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1202_infoperapur_ideestab_dados['nrinsc'] = read_from_xml(ideEstab.nrInsc.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s1202_infoperapur_ideestab = s1202infoPerApurideEstab.objects.create(**s1202_infoperapur_ideestab_dados)
        
                            if 'remunPerApur' in dir(ideEstab):
        
                                for remunPerApur in ideEstab.remunPerApur:
        
                                    s1202_infoperapur_remunperapur_dados = {}
                                    s1202_infoperapur_remunperapur_dados['s1202_infoperapur_ideestab_id'] = s1202_infoperapur_ideestab.id
                
                                    try:
                                        s1202_infoperapur_remunperapur_dados['matricula'] = read_from_xml(remunPerApur.matricula.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s1202_infoperapur_remunperapur_dados['codcateg'] = read_from_xml(remunPerApur.codCateg.cdata, 'esocial', 'N', None)
                                    except AttributeError:
                                        pass
        
                                    s1202_infoperapur_remunperapur = s1202infoPerApurremunPerApur.objects.create(**s1202_infoperapur_remunperapur_dados)
                
                                    if 'itensRemun' in dir(remunPerApur):
                
                                        for itensRemun in remunPerApur.itensRemun:
                
                                            s1202_infoperapur_itensremun_dados = {}
                                            s1202_infoperapur_itensremun_dados['s1202_infoperapur_remunperapur_id'] = s1202_infoperapur_remunperapur.id
                        
                                            try:
                                                s1202_infoperapur_itensremun_dados['codrubr'] = read_from_xml(itensRemun.codRubr.cdata, 'esocial', 'C', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1202_infoperapur_itensremun_dados['idetabrubr'] = read_from_xml(itensRemun.ideTabRubr.cdata, 'esocial', 'C', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1202_infoperapur_itensremun_dados['qtdrubr'] = read_from_xml(itensRemun.qtdRubr.cdata, 'esocial', 'N', 2)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1202_infoperapur_itensremun_dados['fatorrubr'] = read_from_xml(itensRemun.fatorRubr.cdata, 'esocial', 'N', 2)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1202_infoperapur_itensremun_dados['vrunit'] = read_from_xml(itensRemun.vrUnit.cdata, 'esocial', 'N', 2)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1202_infoperapur_itensremun_dados['vrrubr'] = read_from_xml(itensRemun.vrRubr.cdata, 'esocial', 'N', 2)
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
                                                        s1202_infoperapur_detoper_dados['cnpjoper'] = read_from_xml(detOper.cnpjOper.cdata, 'esocial', 'C', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s1202_infoperapur_detoper_dados['regans'] = read_from_xml(detOper.regANS.cdata, 'esocial', 'C', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s1202_infoperapur_detoper_dados['vrpgtit'] = read_from_xml(detOper.vrPgTit.cdata, 'esocial', 'N', 2)
                                                    except AttributeError:
                                                        pass
                        
                                                    s1202_infoperapur_detoper = s1202infoPerApurdetOper.objects.create(**s1202_infoperapur_detoper_dados)
                                
                                                    if 'detPlano' in dir(detOper):
                                
                                                        for detPlano in detOper.detPlano:
                                
                                                            s1202_infoperapur_detplano_dados = {}
                                                            s1202_infoperapur_detplano_dados['s1202_infoperapur_detoper_id'] = s1202_infoperapur_detoper.id
                                        
                                                            try:
                                                                s1202_infoperapur_detplano_dados['tpdep'] = read_from_xml(detPlano.tpDep.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1202_infoperapur_detplano_dados['cpfdep'] = read_from_xml(detPlano.cpfDep.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1202_infoperapur_detplano_dados['nmdep'] = read_from_xml(detPlano.nmDep.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1202_infoperapur_detplano_dados['dtnascto'] = read_from_xml(detPlano.dtNascto.cdata, 'esocial', 'D', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1202_infoperapur_detplano_dados['vlrpgdep'] = read_from_xml(detPlano.vlrPgDep.cdata, 'esocial', 'N', 2)
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
                                s1202_infoperant_ideadc_dados['dtlei'] = read_from_xml(ideADC.dtLei.cdata, 'esocial', 'D', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1202_infoperant_ideadc_dados['nrlei'] = read_from_xml(ideADC.nrLei.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1202_infoperant_ideadc_dados['dtef'] = read_from_xml(ideADC.dtEf.cdata, 'esocial', 'D', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1202_infoperant_ideadc_dados['dtacconv'] = read_from_xml(ideADC.dtAcConv.cdata, 'esocial', 'D', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1202_infoperant_ideadc_dados['tpacconv'] = read_from_xml(ideADC.tpAcConv.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1202_infoperant_ideadc_dados['compacconv'] = read_from_xml(ideADC.compAcConv.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1202_infoperant_ideadc_dados['dtefacconv'] = read_from_xml(ideADC.dtEfAcConv.cdata, 'esocial', 'D', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1202_infoperant_ideadc_dados['dsc'] = read_from_xml(ideADC.dsc.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s1202_infoperant_ideadc = s1202infoPerAntideADC.objects.create(**s1202_infoperant_ideadc_dados)
        
                            if 'idePeriodo' in dir(ideADC):
        
                                for idePeriodo in ideADC.idePeriodo:
        
                                    s1202_infoperant_ideperiodo_dados = {}
                                    s1202_infoperant_ideperiodo_dados['s1202_infoperant_ideadc_id'] = s1202_infoperant_ideadc.id
                
                                    try:
                                        s1202_infoperant_ideperiodo_dados['perref'] = read_from_xml(idePeriodo.perRef.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
        
                                    s1202_infoperant_ideperiodo = s1202infoPerAntidePeriodo.objects.create(**s1202_infoperant_ideperiodo_dados)
                
                                    if 'ideEstab' in dir(idePeriodo):
                
                                        for ideEstab in idePeriodo.ideEstab:
                
                                            s1202_infoperant_ideestab_dados = {}
                                            s1202_infoperant_ideestab_dados['s1202_infoperant_ideperiodo_id'] = s1202_infoperant_ideperiodo.id
                        
                                            try:
                                                s1202_infoperant_ideestab_dados['tpinsc'] = read_from_xml(ideEstab.tpInsc.cdata, 'esocial', 'N', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1202_infoperant_ideestab_dados['nrinsc'] = read_from_xml(ideEstab.nrInsc.cdata, 'esocial', 'C', None)
                                            except AttributeError:
                                                pass
                
                                            s1202_infoperant_ideestab = s1202infoPerAntideEstab.objects.create(**s1202_infoperant_ideestab_dados)
                        
                                            if 'remunPerAnt' in dir(ideEstab):
                        
                                                for remunPerAnt in ideEstab.remunPerAnt:
                        
                                                    s1202_infoperant_remunperant_dados = {}
                                                    s1202_infoperant_remunperant_dados['s1202_infoperant_ideestab_id'] = s1202_infoperant_ideestab.id
                                
                                                    try:
                                                        s1202_infoperant_remunperant_dados['matricula'] = read_from_xml(remunPerAnt.matricula.cdata, 'esocial', 'C', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s1202_infoperant_remunperant_dados['codcateg'] = read_from_xml(remunPerAnt.codCateg.cdata, 'esocial', 'N', None)
                                                    except AttributeError:
                                                        pass
                        
                                                    s1202_infoperant_remunperant = s1202infoPerAntremunPerAnt.objects.create(**s1202_infoperant_remunperant_dados)
                                
                                                    if 'itensRemun' in dir(remunPerAnt):
                                
                                                        for itensRemun in remunPerAnt.itensRemun:
                                
                                                            s1202_infoperant_itensremun_dados = {}
                                                            s1202_infoperant_itensremun_dados['s1202_infoperant_remunperant_id'] = s1202_infoperant_remunperant.id
                                        
                                                            try:
                                                                s1202_infoperant_itensremun_dados['codrubr'] = read_from_xml(itensRemun.codRubr.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1202_infoperant_itensremun_dados['idetabrubr'] = read_from_xml(itensRemun.ideTabRubr.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1202_infoperant_itensremun_dados['qtdrubr'] = read_from_xml(itensRemun.qtdRubr.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1202_infoperant_itensremun_dados['fatorrubr'] = read_from_xml(itensRemun.fatorRubr.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1202_infoperant_itensremun_dados['vrunit'] = read_from_xml(itensRemun.vrUnit.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1202_infoperant_itensremun_dados['vrrubr'] = read_from_xml(itensRemun.vrRubr.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                
                                                            s1202_infoperant_itensremun = s1202infoPerAntitensRemun.objects.create(**s1202_infoperant_itensremun_dados)
    s1202_evtrmnrpps_dados['evento'] = 's1202'
    s1202_evtrmnrpps_dados['id'] = s1202_evtrmnrpps.id
    s1202_evtrmnrpps_dados['identidade_evento'] = doc.eSocial.evtRmnRPPS['Id']

    from emensageriapro.esocial.views.s1202_evtrmnrpps_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1202_evtrmnrpps.id)

    return s1202_evtrmnrpps_dados