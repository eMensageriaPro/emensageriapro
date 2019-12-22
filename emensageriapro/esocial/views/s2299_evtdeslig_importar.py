# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2299.models import *
from emensageriapro.functions import read_from_xml



def read_s2299_evtdeslig_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2299_evtdeslig_obj(request, doc, status, validar)
    return dados



def read_s2299_evtdeslig(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2299_evtdeslig_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2299evtDeslig.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2299_evtdeslig_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2299_evtdeslig_dados = {}
    s2299_evtdeslig_dados['status'] = status
    s2299_evtdeslig_dados['arquivo_original'] = 1
    if arquivo:
        s2299_evtdeslig_dados['arquivo'] = arquivo.arquivo
    s2299_evtdeslig_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2299_evtdeslig_dados['identidade'] = doc.eSocial.evtDeslig['Id']
    evtDeslig = doc.eSocial.evtDeslig

    try:
        s2299_evtdeslig_dados['indretif'] = read_from_xml(evtDeslig.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['nrrecibo'] = read_from_xml(evtDeslig.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['tpamb'] = read_from_xml(evtDeslig.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['procemi'] = read_from_xml(evtDeslig.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['verproc'] = read_from_xml(evtDeslig.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['tpinsc'] = read_from_xml(evtDeslig.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['nrinsc'] = read_from_xml(evtDeslig.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['cpftrab'] = read_from_xml(evtDeslig.ideVinculo.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['nistrab'] = read_from_xml(evtDeslig.ideVinculo.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['matricula'] = read_from_xml(evtDeslig.ideVinculo.matricula.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['mtvdeslig'] = read_from_xml(evtDeslig.infoDeslig.mtvDeslig.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['dtdeslig'] = read_from_xml(evtDeslig.infoDeslig.dtDeslig.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['indpagtoapi'] = read_from_xml(evtDeslig.infoDeslig.indPagtoAPI.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['dtprojfimapi'] = read_from_xml(evtDeslig.infoDeslig.dtProjFimAPI.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['pensalim'] = read_from_xml(evtDeslig.infoDeslig.pensAlim.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['percaliment'] = read_from_xml(evtDeslig.infoDeslig.percAliment.cdata, 'esocial', 'N', 2)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['vralim'] = read_from_xml(evtDeslig.infoDeslig.vrAlim.cdata, 'esocial', 'N', 2)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['nrcertobito'] = read_from_xml(evtDeslig.infoDeslig.nrCertObito.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['nrproctrab'] = read_from_xml(evtDeslig.infoDeslig.nrProcTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['indcumprparc'] = read_from_xml(evtDeslig.infoDeslig.indCumprParc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['qtddiasinterm'] = read_from_xml(evtDeslig.infoDeslig.qtdDiasInterm.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    s2299_evtdeslig = s2299evtDeslig.objects.create(**s2299_evtdeslig_dados)

    if 'infoDeslig' in dir(evtDeslig) and 'observacoes' in dir(evtDeslig.infoDeslig):

        for observacoes in evtDeslig.infoDeslig.observacoes:

            s2299_observacoes_dados = {}
            s2299_observacoes_dados['s2299_evtdeslig_id'] = s2299_evtdeslig.id

            try:
                s2299_observacoes_dados['observacao'] = read_from_xml(observacoes.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2299_observacoes = s2299observacoes.objects.create(**s2299_observacoes_dados)

    if 'infoDeslig' in dir(evtDeslig) and 'sucessaoVinc' in dir(evtDeslig.infoDeslig):

        for sucessaoVinc in evtDeslig.infoDeslig.sucessaoVinc:

            s2299_sucessaovinc_dados = {}
            s2299_sucessaovinc_dados['s2299_evtdeslig_id'] = s2299_evtdeslig.id

            try:
                s2299_sucessaovinc_dados['tpinscsuc'] = read_from_xml(sucessaoVinc.tpInscSuc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2299_sucessaovinc_dados['cnpjsucessora'] = read_from_xml(sucessaoVinc.cnpjSucessora.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2299_sucessaovinc = s2299sucessaoVinc.objects.create(**s2299_sucessaovinc_dados)

    if 'infoDeslig' in dir(evtDeslig) and 'transfTit' in dir(evtDeslig.infoDeslig):

        for transfTit in evtDeslig.infoDeslig.transfTit:

            s2299_transftit_dados = {}
            s2299_transftit_dados['s2299_evtdeslig_id'] = s2299_evtdeslig.id

            try:
                s2299_transftit_dados['cpfsubstituto'] = read_from_xml(transfTit.cpfSubstituto.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2299_transftit_dados['dtnascto'] = read_from_xml(transfTit.dtNascto.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            s2299_transftit = s2299transfTit.objects.create(**s2299_transftit_dados)

    if 'infoDeslig' in dir(evtDeslig) and 'mudancaCPF' in dir(evtDeslig.infoDeslig):

        for mudancaCPF in evtDeslig.infoDeslig.mudancaCPF:

            s2299_mudancacpf_dados = {}
            s2299_mudancacpf_dados['s2299_evtdeslig_id'] = s2299_evtdeslig.id

            try:
                s2299_mudancacpf_dados['novocpf'] = read_from_xml(mudancaCPF.novoCPF.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2299_mudancacpf = s2299mudancaCPF.objects.create(**s2299_mudancacpf_dados)

    if 'infoDeslig' in dir(evtDeslig) and 'verbasResc' in dir(evtDeslig.infoDeslig):

        for verbasResc in evtDeslig.infoDeslig.verbasResc:

            s2299_verbasresc_dados = {}
            s2299_verbasresc_dados['s2299_evtdeslig_id'] = s2299_evtdeslig.id

            s2299_verbasresc = s2299verbasResc.objects.create(**s2299_verbasresc_dados)

            if 'dmDev' in dir(verbasResc):

                for dmDev in verbasResc.dmDev:

                    s2299_dmdev_dados = {}
                    s2299_dmdev_dados['s2299_verbasresc_id'] = s2299_verbasresc.id

                    try:
                        s2299_dmdev_dados['idedmdev'] = read_from_xml(dmDev.ideDmDev.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2299_dmdev = s2299dmDev.objects.create(**s2299_dmdev_dados)

                    if 'infoPerApur' in dir(dmDev):

                        for infoPerApur in dmDev.infoPerApur:

                            s2299_infoperapur_dados = {}
                            s2299_infoperapur_dados['s2299_dmdev_id'] = s2299_dmdev.id

                            s2299_infoperapur = s2299infoPerApur.objects.create(**s2299_infoperapur_dados)
        
                            if 'ideEstabLot' in dir(infoPerApur):
        
                                for ideEstabLot in infoPerApur.ideEstabLot:
        
                                    s2299_infoperapur_ideestablot_dados = {}
                                    s2299_infoperapur_ideestablot_dados['s2299_infoperapur_id'] = s2299_infoperapur.id
                
                                    try:
                                        s2299_infoperapur_ideestablot_dados['tpinsc'] = read_from_xml(ideEstabLot.tpInsc.cdata, 'esocial', 'N', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2299_infoperapur_ideestablot_dados['nrinsc'] = read_from_xml(ideEstabLot.nrInsc.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2299_infoperapur_ideestablot_dados['codlotacao'] = read_from_xml(ideEstabLot.codLotacao.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
        
                                    s2299_infoperapur_ideestablot = s2299infoPerApurideEstabLot.objects.create(**s2299_infoperapur_ideestablot_dados)
                
                                    if 'detVerbas' in dir(ideEstabLot):
                
                                        for detVerbas in ideEstabLot.detVerbas:
                
                                            s2299_infoperapur_detverbas_dados = {}
                                            s2299_infoperapur_detverbas_dados['s2299_infoperapur_ideestablot_id'] = s2299_infoperapur_ideestablot.id
                        
                                            try:
                                                s2299_infoperapur_detverbas_dados['codrubr'] = read_from_xml(detVerbas.codRubr.cdata, 'esocial', 'C', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s2299_infoperapur_detverbas_dados['idetabrubr'] = read_from_xml(detVerbas.ideTabRubr.cdata, 'esocial', 'C', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s2299_infoperapur_detverbas_dados['qtdrubr'] = read_from_xml(detVerbas.qtdRubr.cdata, 'esocial', 'N', 2)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s2299_infoperapur_detverbas_dados['fatorrubr'] = read_from_xml(detVerbas.fatorRubr.cdata, 'esocial', 'N', 2)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s2299_infoperapur_detverbas_dados['vrunit'] = read_from_xml(detVerbas.vrUnit.cdata, 'esocial', 'N', 2)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s2299_infoperapur_detverbas_dados['vrrubr'] = read_from_xml(detVerbas.vrRubr.cdata, 'esocial', 'N', 2)
                                            except AttributeError:
                                                pass
                
                                            s2299_infoperapur_detverbas = s2299infoPerApurdetVerbas.objects.create(**s2299_infoperapur_detverbas_dados)
                
                                    if 'infoSaudeColet' in dir(ideEstabLot):
                
                                        for infoSaudeColet in ideEstabLot.infoSaudeColet:
                
                                            s2299_infoperapur_infosaudecolet_dados = {}
                                            s2299_infoperapur_infosaudecolet_dados['s2299_infoperapur_ideestablot_id'] = s2299_infoperapur_ideestablot.id
                
                                            s2299_infoperapur_infosaudecolet = s2299infoPerApurinfoSaudeColet.objects.create(**s2299_infoperapur_infosaudecolet_dados)
                        
                                            if 'detOper' in dir(infoSaudeColet):
                        
                                                for detOper in infoSaudeColet.detOper:
                        
                                                    s2299_infoperapur_detoper_dados = {}
                                                    s2299_infoperapur_detoper_dados['s2299_infoperapur_infosaudecolet_id'] = s2299_infoperapur_infosaudecolet.id
                                
                                                    try:
                                                        s2299_infoperapur_detoper_dados['cnpjoper'] = read_from_xml(detOper.cnpjOper.cdata, 'esocial', 'C', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s2299_infoperapur_detoper_dados['regans'] = read_from_xml(detOper.regANS.cdata, 'esocial', 'C', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s2299_infoperapur_detoper_dados['vrpgtit'] = read_from_xml(detOper.vrPgTit.cdata, 'esocial', 'N', 2)
                                                    except AttributeError:
                                                        pass
                        
                                                    s2299_infoperapur_detoper = s2299infoPerApurdetOper.objects.create(**s2299_infoperapur_detoper_dados)
                                
                                                    if 'detPlano' in dir(detOper):
                                
                                                        for detPlano in detOper.detPlano:
                                
                                                            s2299_infoperapur_detplano_dados = {}
                                                            s2299_infoperapur_detplano_dados['s2299_infoperapur_detoper_id'] = s2299_infoperapur_detoper.id
                                        
                                                            try:
                                                                s2299_infoperapur_detplano_dados['tpdep'] = read_from_xml(detPlano.tpDep.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperapur_detplano_dados['cpfdep'] = read_from_xml(detPlano.cpfDep.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperapur_detplano_dados['nmdep'] = read_from_xml(detPlano.nmDep.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperapur_detplano_dados['dtnascto'] = read_from_xml(detPlano.dtNascto.cdata, 'esocial', 'D', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperapur_detplano_dados['vlrpgdep'] = read_from_xml(detPlano.vlrPgDep.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                
                                                            s2299_infoperapur_detplano = s2299infoPerApurdetPlano.objects.create(**s2299_infoperapur_detplano_dados)
                
                                    if 'infoAgNocivo' in dir(ideEstabLot):
                
                                        for infoAgNocivo in ideEstabLot.infoAgNocivo:
                
                                            s2299_infoperapur_infoagnocivo_dados = {}
                                            s2299_infoperapur_infoagnocivo_dados['s2299_infoperapur_ideestablot_id'] = s2299_infoperapur_ideestablot.id
                        
                                            try:
                                                s2299_infoperapur_infoagnocivo_dados['grauexp'] = read_from_xml(infoAgNocivo.grauExp.cdata, 'esocial', 'N', None)
                                            except AttributeError:
                                                pass
                
                                            s2299_infoperapur_infoagnocivo = s2299infoPerApurinfoAgNocivo.objects.create(**s2299_infoperapur_infoagnocivo_dados)
                
                                    if 'infoSimples' in dir(ideEstabLot):
                
                                        for infoSimples in ideEstabLot.infoSimples:
                
                                            s2299_infoperapur_infosimples_dados = {}
                                            s2299_infoperapur_infosimples_dados['s2299_infoperapur_ideestablot_id'] = s2299_infoperapur_ideestablot.id
                        
                                            try:
                                                s2299_infoperapur_infosimples_dados['indsimples'] = read_from_xml(infoSimples.indSimples.cdata, 'esocial', 'N', None)
                                            except AttributeError:
                                                pass
                
                                            s2299_infoperapur_infosimples = s2299infoPerApurinfoSimples.objects.create(**s2299_infoperapur_infosimples_dados)

                    if 'infoPerAnt' in dir(dmDev):

                        for infoPerAnt in dmDev.infoPerAnt:

                            s2299_infoperant_dados = {}
                            s2299_infoperant_dados['s2299_dmdev_id'] = s2299_dmdev.id

                            s2299_infoperant = s2299infoPerAnt.objects.create(**s2299_infoperant_dados)
        
                            if 'ideADC' in dir(infoPerAnt):
        
                                for ideADC in infoPerAnt.ideADC:
        
                                    s2299_infoperant_ideadc_dados = {}
                                    s2299_infoperant_ideadc_dados['s2299_infoperant_id'] = s2299_infoperant.id
                
                                    try:
                                        s2299_infoperant_ideadc_dados['dtacconv'] = read_from_xml(ideADC.dtAcConv.cdata, 'esocial', 'D', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2299_infoperant_ideadc_dados['tpacconv'] = read_from_xml(ideADC.tpAcConv.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2299_infoperant_ideadc_dados['compacconv'] = read_from_xml(ideADC.compAcConv.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2299_infoperant_ideadc_dados['dtefacconv'] = read_from_xml(ideADC.dtEfAcConv.cdata, 'esocial', 'D', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2299_infoperant_ideadc_dados['dsc'] = read_from_xml(ideADC.dsc.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
        
                                    s2299_infoperant_ideadc = s2299infoPerAntideADC.objects.create(**s2299_infoperant_ideadc_dados)
                
                                    if 'idePeriodo' in dir(ideADC):
                
                                        for idePeriodo in ideADC.idePeriodo:
                
                                            s2299_infoperant_ideperiodo_dados = {}
                                            s2299_infoperant_ideperiodo_dados['s2299_infoperant_ideadc_id'] = s2299_infoperant_ideadc.id
                        
                                            try:
                                                s2299_infoperant_ideperiodo_dados['perref'] = read_from_xml(idePeriodo.perRef.cdata, 'esocial', 'C', None)
                                            except AttributeError:
                                                pass
                
                                            s2299_infoperant_ideperiodo = s2299infoPerAntidePeriodo.objects.create(**s2299_infoperant_ideperiodo_dados)
                        
                                            if 'ideEstabLot' in dir(idePeriodo):
                        
                                                for ideEstabLot in idePeriodo.ideEstabLot:
                        
                                                    s2299_infoperant_ideestablot_dados = {}
                                                    s2299_infoperant_ideestablot_dados['s2299_infoperant_ideperiodo_id'] = s2299_infoperant_ideperiodo.id
                                
                                                    try:
                                                        s2299_infoperant_ideestablot_dados['tpinsc'] = read_from_xml(ideEstabLot.tpInsc.cdata, 'esocial', 'N', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s2299_infoperant_ideestablot_dados['nrinsc'] = read_from_xml(ideEstabLot.nrInsc.cdata, 'esocial', 'C', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s2299_infoperant_ideestablot_dados['codlotacao'] = read_from_xml(ideEstabLot.codLotacao.cdata, 'esocial', 'C', None)
                                                    except AttributeError:
                                                        pass
                        
                                                    s2299_infoperant_ideestablot = s2299infoPerAntideEstabLot.objects.create(**s2299_infoperant_ideestablot_dados)
                                
                                                    if 'detVerbas' in dir(ideEstabLot):
                                
                                                        for detVerbas in ideEstabLot.detVerbas:
                                
                                                            s2299_infoperant_detverbas_dados = {}
                                                            s2299_infoperant_detverbas_dados['s2299_infoperant_ideestablot_id'] = s2299_infoperant_ideestablot.id
                                        
                                                            try:
                                                                s2299_infoperant_detverbas_dados['codrubr'] = read_from_xml(detVerbas.codRubr.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperant_detverbas_dados['idetabrubr'] = read_from_xml(detVerbas.ideTabRubr.cdata, 'esocial', 'C', None)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperant_detverbas_dados['qtdrubr'] = read_from_xml(detVerbas.qtdRubr.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperant_detverbas_dados['fatorrubr'] = read_from_xml(detVerbas.fatorRubr.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperant_detverbas_dados['vrunit'] = read_from_xml(detVerbas.vrUnit.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperant_detverbas_dados['vrrubr'] = read_from_xml(detVerbas.vrRubr.cdata, 'esocial', 'N', 2)
                                                            except AttributeError:
                                                                pass
                                
                                                            s2299_infoperant_detverbas = s2299infoPerAntdetVerbas.objects.create(**s2299_infoperant_detverbas_dados)
                                
                                                    if 'infoAgNocivo' in dir(ideEstabLot):
                                
                                                        for infoAgNocivo in ideEstabLot.infoAgNocivo:
                                
                                                            s2299_infoperant_infoagnocivo_dados = {}
                                                            s2299_infoperant_infoagnocivo_dados['s2299_infoperant_ideestablot_id'] = s2299_infoperant_ideestablot.id
                                        
                                                            try:
                                                                s2299_infoperant_infoagnocivo_dados['grauexp'] = read_from_xml(infoAgNocivo.grauExp.cdata, 'esocial', 'N', None)
                                                            except AttributeError:
                                                                pass
                                
                                                            s2299_infoperant_infoagnocivo = s2299infoPerAntinfoAgNocivo.objects.create(**s2299_infoperant_infoagnocivo_dados)
                                
                                                    if 'infoSimples' in dir(ideEstabLot):
                                
                                                        for infoSimples in ideEstabLot.infoSimples:
                                
                                                            s2299_infoperant_infosimples_dados = {}
                                                            s2299_infoperant_infosimples_dados['s2299_infoperant_ideestablot_id'] = s2299_infoperant_ideestablot.id
                                        
                                                            try:
                                                                s2299_infoperant_infosimples_dados['indsimples'] = read_from_xml(infoSimples.indSimples.cdata, 'esocial', 'N', None)
                                                            except AttributeError:
                                                                pass
                                
                                                            s2299_infoperant_infosimples = s2299infoPerAntinfoSimples.objects.create(**s2299_infoperant_infosimples_dados)

                    if 'infoTrabInterm' in dir(dmDev):

                        for infoTrabInterm in dmDev.infoTrabInterm:

                            s2299_infotrabinterm_dados = {}
                            s2299_infotrabinterm_dados['s2299_dmdev_id'] = s2299_dmdev.id
        
                            try:
                                s2299_infotrabinterm_dados['codconv'] = read_from_xml(infoTrabInterm.codConv.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s2299_infotrabinterm = s2299infoTrabInterm.objects.create(**s2299_infotrabinterm_dados)

            if 'procJudTrab' in dir(verbasResc):

                for procJudTrab in verbasResc.procJudTrab:

                    s2299_infotrabinterm_procjudtrab_dados = {}
                    s2299_infotrabinterm_procjudtrab_dados['s2299_verbasresc_id'] = s2299_verbasresc.id

                    try:
                        s2299_infotrabinterm_procjudtrab_dados['tptrib'] = read_from_xml(procJudTrab.tpTrib.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2299_infotrabinterm_procjudtrab_dados['nrprocjud'] = read_from_xml(procJudTrab.nrProcJud.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2299_infotrabinterm_procjudtrab_dados['codsusp'] = read_from_xml(procJudTrab.codSusp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s2299_infotrabinterm_procjudtrab = s2299infoTrabIntermprocJudTrab.objects.create(**s2299_infotrabinterm_procjudtrab_dados)

            if 'infoMV' in dir(verbasResc):

                for infoMV in verbasResc.infoMV:

                    s2299_infotrabinterm_infomv_dados = {}
                    s2299_infotrabinterm_infomv_dados['s2299_verbasresc_id'] = s2299_verbasresc.id

                    try:
                        s2299_infotrabinterm_infomv_dados['indmv'] = read_from_xml(infoMV.indMV.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s2299_infotrabinterm_infomv = s2299infoTrabInterminfoMV.objects.create(**s2299_infotrabinterm_infomv_dados)

                    if 'remunOutrEmpr' in dir(infoMV):

                        for remunOutrEmpr in infoMV.remunOutrEmpr:

                            s2299_infotrabinterm_remunoutrempr_dados = {}
                            s2299_infotrabinterm_remunoutrempr_dados['s2299_infotrabinterm_infomv_id'] = s2299_infotrabinterm_infomv.id
        
                            try:
                                s2299_infotrabinterm_remunoutrempr_dados['tpinsc'] = read_from_xml(remunOutrEmpr.tpInsc.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2299_infotrabinterm_remunoutrempr_dados['nrinsc'] = read_from_xml(remunOutrEmpr.nrInsc.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2299_infotrabinterm_remunoutrempr_dados['codcateg'] = read_from_xml(remunOutrEmpr.codCateg.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2299_infotrabinterm_remunoutrempr_dados['vlrremunoe'] = read_from_xml(remunOutrEmpr.vlrRemunOE.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s2299_infotrabinterm_remunoutrempr = s2299infoTrabIntermremunOutrEmpr.objects.create(**s2299_infotrabinterm_remunoutrempr_dados)

            if 'procCS' in dir(verbasResc):

                for procCS in verbasResc.procCS:

                    s2299_infotrabinterm_proccs_dados = {}
                    s2299_infotrabinterm_proccs_dados['s2299_verbasresc_id'] = s2299_verbasresc.id

                    try:
                        s2299_infotrabinterm_proccs_dados['nrprocjud'] = read_from_xml(procCS.nrProcJud.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2299_infotrabinterm_proccs = s2299infoTrabIntermprocCS.objects.create(**s2299_infotrabinterm_proccs_dados)

    if 'infoDeslig' in dir(evtDeslig) and 'quarentena' in dir(evtDeslig.infoDeslig):

        for quarentena in evtDeslig.infoDeslig.quarentena:

            s2299_infotrabinterm_quarentena_dados = {}
            s2299_infotrabinterm_quarentena_dados['s2299_evtdeslig_id'] = s2299_evtdeslig.id

            try:
                s2299_infotrabinterm_quarentena_dados['dtfimquar'] = read_from_xml(quarentena.dtFimQuar.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            s2299_infotrabinterm_quarentena = s2299infoTrabIntermquarentena.objects.create(**s2299_infotrabinterm_quarentena_dados)

    if 'infoDeslig' in dir(evtDeslig) and 'consigFGTS' in dir(evtDeslig.infoDeslig):

        for consigFGTS in evtDeslig.infoDeslig.consigFGTS:

            s2299_infotrabinterm_consigfgts_dados = {}
            s2299_infotrabinterm_consigfgts_dados['s2299_evtdeslig_id'] = s2299_evtdeslig.id

            try:
                s2299_infotrabinterm_consigfgts_dados['insconsig'] = read_from_xml(consigFGTS.insConsig.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2299_infotrabinterm_consigfgts_dados['nrcontr'] = read_from_xml(consigFGTS.nrContr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2299_infotrabinterm_consigfgts = s2299infoTrabIntermconsigFGTS.objects.create(**s2299_infotrabinterm_consigfgts_dados)
    s2299_evtdeslig_dados['evento'] = 's2299'
    s2299_evtdeslig_dados['id'] = s2299_evtdeslig.id
    s2299_evtdeslig_dados['identidade_evento'] = doc.eSocial.evtDeslig['Id']

    from emensageriapro.esocial.views.s2299_evtdeslig_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2299_evtdeslig.id)

    return s2299_evtdeslig_dados