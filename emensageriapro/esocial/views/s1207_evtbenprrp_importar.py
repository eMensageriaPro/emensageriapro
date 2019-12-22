# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1207.models import *
from emensageriapro.functions import read_from_xml



def read_s1207_evtbenprrp_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1207_evtbenprrp_obj(request, doc, status, validar)
    return dados



def read_s1207_evtbenprrp(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1207_evtbenprrp_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1207evtBenPrRP.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1207_evtbenprrp_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1207_evtbenprrp_dados = {}
    s1207_evtbenprrp_dados['status'] = status
    s1207_evtbenprrp_dados['arquivo_original'] = 1
    if arquivo:
        s1207_evtbenprrp_dados['arquivo'] = arquivo.arquivo
    s1207_evtbenprrp_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1207_evtbenprrp_dados['identidade'] = doc.eSocial.evtBenPrRP['Id']
    evtBenPrRP = doc.eSocial.evtBenPrRP

    try:
        s1207_evtbenprrp_dados['indretif'] = read_from_xml(evtBenPrRP.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1207_evtbenprrp_dados['nrrecibo'] = read_from_xml(evtBenPrRP.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1207_evtbenprrp_dados['indapuracao'] = read_from_xml(evtBenPrRP.ideEvento.indApuracao.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1207_evtbenprrp_dados['perapur'] = read_from_xml(evtBenPrRP.ideEvento.perApur.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1207_evtbenprrp_dados['tpamb'] = read_from_xml(evtBenPrRP.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1207_evtbenprrp_dados['procemi'] = read_from_xml(evtBenPrRP.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1207_evtbenprrp_dados['verproc'] = read_from_xml(evtBenPrRP.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1207_evtbenprrp_dados['tpinsc'] = read_from_xml(evtBenPrRP.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1207_evtbenprrp_dados['nrinsc'] = read_from_xml(evtBenPrRP.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1207_evtbenprrp_dados['cpfbenef'] = read_from_xml(evtBenPrRP.ideBenef.cpfBenef.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1207_evtbenprrp = s1207evtBenPrRP.objects.create(**s1207_evtbenprrp_dados)

    if 'ideBenef' in dir(evtBenPrRP) and 'procJudTrab' in dir(evtBenPrRP.ideBenef):

        for procJudTrab in evtBenPrRP.ideBenef.procJudTrab:

            s1207_procjudtrab_dados = {}
            s1207_procjudtrab_dados['s1207_evtbenprrp_id'] = s1207_evtbenprrp.id

            try:
                s1207_procjudtrab_dados['tptrib'] = read_from_xml(procJudTrab.tpTrib.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1207_procjudtrab_dados['nrprocjud'] = read_from_xml(procJudTrab.nrProcJud.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1207_procjudtrab_dados['codsusp'] = read_from_xml(procJudTrab.codSusp.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s1207_procjudtrab = s1207procJudTrab.objects.create(**s1207_procjudtrab_dados)

    if 'dmDev' in dir(evtBenPrRP):

        for dmDev in evtBenPrRP.dmDev:

            s1207_dmdev_dados = {}
            s1207_dmdev_dados['s1207_evtbenprrp_id'] = s1207_evtbenprrp.id

            try:
                s1207_dmdev_dados['tpbenef'] = read_from_xml(dmDev.tpBenef.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1207_dmdev_dados['nrbenefic'] = read_from_xml(dmDev.nrBenefic.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1207_dmdev_dados['idedmdev'] = read_from_xml(dmDev.ideDmDev.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1207_dmdev = s1207dmDev.objects.create(**s1207_dmdev_dados)

            if 'itens' in dir(dmDev):

                for itens in dmDev.itens:

                    s1207_itens_dados = {}
                    s1207_itens_dados['s1207_dmdev_id'] = s1207_dmdev.id

                    try:
                        s1207_itens_dados['codrubr'] = read_from_xml(itens.codRubr.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1207_itens_dados['idetabrubr'] = read_from_xml(itens.ideTabRubr.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1207_itens_dados['vrrubr'] = read_from_xml(itens.vrRubr.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    s1207_itens = s1207itens.objects.create(**s1207_itens_dados)

            if 'infoPerApur' in dir(dmDev):

                for infoPerApur in dmDev.infoPerApur:

                    s1207_infoperapur_dados = {}
                    s1207_infoperapur_dados['s1207_dmdev_id'] = s1207_dmdev.id

                    s1207_infoperapur = s1207infoPerApur.objects.create(**s1207_infoperapur_dados)

                    if 'ideEstab' in dir(infoPerApur):

                        for ideEstab in infoPerApur.ideEstab:

                            s1207_infoperapur_ideestab_dados = {}
                            s1207_infoperapur_ideestab_dados['s1207_infoperapur_id'] = s1207_infoperapur.id
        
                            try:
                                s1207_infoperapur_ideestab_dados['tpinsc'] = read_from_xml(ideEstab.tpInsc.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1207_infoperapur_ideestab_dados['nrinsc'] = read_from_xml(ideEstab.nrInsc.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s1207_infoperapur_ideestab = s1207infoPerApurideEstab.objects.create(**s1207_infoperapur_ideestab_dados)
        
                            if 'remunPerApur' in dir(ideEstab):
        
                                for remunPerApur in ideEstab.remunPerApur:
        
                                    s1207_infoperapur_remunperapur_dados = {}
                                    s1207_infoperapur_remunperapur_dados['s1207_infoperapur_ideestab_id'] = s1207_infoperapur_ideestab.id
        
                                    s1207_infoperapur_remunperapur = s1207infoPerApurremunPerApur.objects.create(**s1207_infoperapur_remunperapur_dados)
                
                                    if 'itensRemun' in dir(remunPerApur):
                
                                        for itensRemun in remunPerApur.itensRemun:
                
                                            s1207_infoperapur_itensremun_dados = {}
                                            s1207_infoperapur_itensremun_dados['s1207_infoperapur_remunperapur_id'] = s1207_infoperapur_remunperapur.id
                        
                                            try:
                                                s1207_infoperapur_itensremun_dados['codrubr'] = read_from_xml(itensRemun.codRubr.cdata, 'esocial', 'C', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1207_infoperapur_itensremun_dados['idetabrubr'] = read_from_xml(itensRemun.ideTabRubr.cdata, 'esocial', 'C', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1207_infoperapur_itensremun_dados['qtdrubr'] = read_from_xml(itensRemun.qtdRubr.cdata, 'esocial', 'N', 2)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1207_infoperapur_itensremun_dados['fatorrubr'] = read_from_xml(itensRemun.fatorRubr.cdata, 'esocial', 'N', 2)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1207_infoperapur_itensremun_dados['vrunit'] = read_from_xml(itensRemun.vrUnit.cdata, 'esocial', 'N', 2)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1207_infoperapur_itensremun_dados['vrrubr'] = read_from_xml(itensRemun.vrRubr.cdata, 'esocial', 'N', 2)
                                            except AttributeError:
                                                pass
                
                                            s1207_infoperapur_itensremun = s1207infoPerApuritensRemun.objects.create(**s1207_infoperapur_itensremun_dados)

            if 'infoPerAnt' in dir(dmDev):

                for infoPerAnt in dmDev.infoPerAnt:

                    s1207_infoperant_dados = {}
                    s1207_infoperant_dados['s1207_dmdev_id'] = s1207_dmdev.id

                    s1207_infoperant = s1207infoPerAnt.objects.create(**s1207_infoperant_dados)

                    if 'ideADC' in dir(infoPerAnt):

                        for ideADC in infoPerAnt.ideADC:

                            s1207_infoperant_ideadc_dados = {}
                            s1207_infoperant_ideadc_dados['s1207_infoperant_id'] = s1207_infoperant.id
        
                            try:
                                s1207_infoperant_ideadc_dados['dtacconv'] = read_from_xml(ideADC.dtAcConv.cdata, 'esocial', 'D', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1207_infoperant_ideadc_dados['tpacconv'] = read_from_xml(ideADC.tpAcConv.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1207_infoperant_ideadc_dados['compacconv'] = read_from_xml(ideADC.compAcConv.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1207_infoperant_ideadc_dados['dtefacconv'] = read_from_xml(ideADC.dtEfAcConv.cdata, 'esocial', 'D', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1207_infoperant_ideadc_dados['dsc'] = read_from_xml(ideADC.dsc.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s1207_infoperant_ideadc = s1207infoPerAntideADC.objects.create(**s1207_infoperant_ideadc_dados)
        
                            if 'idePeriodo' in dir(ideADC):
        
                                for idePeriodo in ideADC.idePeriodo:
        
                                    s1207_infoperant_ideperiodo_dados = {}
                                    s1207_infoperant_ideperiodo_dados['s1207_infoperant_ideadc_id'] = s1207_infoperant_ideadc.id
                
                                    try:
                                        s1207_infoperant_ideperiodo_dados['perref'] = read_from_xml(idePeriodo.perRef.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
        
                                    s1207_infoperant_ideperiodo = s1207infoPerAntidePeriodo.objects.create(**s1207_infoperant_ideperiodo_dados)
                
                                    if 'ideEstab' in dir(idePeriodo):
                
                                        for ideEstab in idePeriodo.ideEstab:
                
                                            s1207_infoperant_ideestab_dados = {}
                                            s1207_infoperant_ideestab_dados['s1207_infoperant_ideperiodo_id'] = s1207_infoperant_ideperiodo.id
                        
                                            try:
                                                s1207_infoperant_ideestab_dados['tpinsc'] = read_from_xml(ideEstab.tpInsc.cdata, 'esocial', 'N', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s1207_infoperant_ideestab_dados['nrinsc'] = read_from_xml(ideEstab.nrInsc.cdata, 'esocial', 'C', None)
                                            except AttributeError:
                                                pass
                
                                            s1207_infoperant_ideestab = s1207infoPerAntideEstab.objects.create(**s1207_infoperant_ideestab_dados)
                        
                                            if 'remunPerAnt' in dir(ideEstab):
                        
                                                for remunPerAnt in ideEstab.remunPerAnt:
                        
                                                    s1207_infoperant_remunperant_dados = {}
                                                    s1207_infoperant_remunperant_dados['s1207_infoperant_ideestab_id'] = s1207_infoperant_ideestab.id
                        
                                                    s1207_infoperant_remunperant = s1207infoPerAntremunPerAnt.objects.create(**s1207_infoperant_remunperant_dados)
                                
                                                    if 'itensRemun' in dir(remunPerAnt):
                                
                                                        for itensRemun in remunPerAnt.itensRemun:
                                
                                                            s1207_infoperant_itensremun_dados = {}
                                                            s1207_infoperant_itensremun_dados['s1207_infoperant_remunperant_id'] = s1207_infoperant_remunperant.id
                                        
                                                            try:
                                                                s1207_infoperant_itensremun_dados['codrubr'] = read_from_xml(itensRemun.codRubr.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1207_infoperant_itensremun_dados['idetabrubr'] = read_from_xml(itensRemun.ideTabRubr.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1207_infoperant_itensremun_dados['qtdrubr'] = read_from_xml(itensRemun.qtdRubr.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1207_infoperant_itensremun_dados['fatorrubr'] = read_from_xml(itensRemun.fatorRubr.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1207_infoperant_itensremun_dados['vrunit'] = read_from_xml(itensRemun.vrUnit.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s1207_infoperant_itensremun_dados['vrrubr'] = read_from_xml(itensRemun.vrRubr.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                
                                                            s1207_infoperant_itensremun = s1207infoPerAntitensRemun.objects.create(**s1207_infoperant_itensremun_dados)
    s1207_evtbenprrp_dados['evento'] = 's1207'
    s1207_evtbenprrp_dados['id'] = s1207_evtbenprrp.id
    s1207_evtbenprrp_dados['identidade_evento'] = doc.eSocial.evtBenPrRP['Id']

    from emensageriapro.esocial.views.s1207_evtbenprrp_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1207_evtbenprrp.id)

    return s1207_evtbenprrp_dados