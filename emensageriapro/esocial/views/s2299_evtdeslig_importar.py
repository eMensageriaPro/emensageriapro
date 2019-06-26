#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2299.models import *



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

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_s2299_evtdeslig_obj(request, doc, status, validar, arquivo)

    s2299evtDeslig.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s2299_evtdeslig_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2299_evtdeslig_dados = {}
    s2299_evtdeslig_dados['status'] = status
    s2299_evtdeslig_dados['arquivo_original'] = 1
    if arquivo:
        s2299_evtdeslig_dados['arquivo'] = arquivo
    s2299_evtdeslig_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2299_evtdeslig_dados['identidade'] = doc.eSocial.evtDeslig['Id']
    evtDeslig = doc.eSocial.evtDeslig

    try:
        s2299_evtdeslig_dados['indretif'] = evtDeslig.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['nrrecibo'] = evtDeslig.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['tpamb'] = evtDeslig.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['procemi'] = evtDeslig.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['verproc'] = evtDeslig.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['tpinsc'] = evtDeslig.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['nrinsc'] = evtDeslig.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['cpftrab'] = evtDeslig.ideVinculo.cpfTrab.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['nistrab'] = evtDeslig.ideVinculo.nisTrab.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['matricula'] = evtDeslig.ideVinculo.matricula.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['mtvdeslig'] = evtDeslig.infoDeslig.mtvDeslig.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['dtdeslig'] = evtDeslig.infoDeslig.dtDeslig.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['indpagtoapi'] = evtDeslig.infoDeslig.indPagtoAPI.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['dtprojfimapi'] = evtDeslig.infoDeslig.dtProjFimAPI.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['pensalim'] = evtDeslig.infoDeslig.pensAlim.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['percaliment'] = evtDeslig.infoDeslig.percAliment.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['vralim'] = evtDeslig.infoDeslig.vrAlim.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['nrcertobito'] = evtDeslig.infoDeslig.nrCertObito.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['nrproctrab'] = evtDeslig.infoDeslig.nrProcTrab.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['indcumprparc'] = evtDeslig.infoDeslig.indCumprParc.cdata
    except AttributeError:
        pass

    try:
        s2299_evtdeslig_dados['qtddiasinterm'] = evtDeslig.infoDeslig.qtdDiasInterm.cdata
    except AttributeError:
        pass

    s2299_evtdeslig = s2299evtDeslig.objects.create(**s2299_evtdeslig_dados)

    if 'infoDeslig' in dir(evtDeslig) and 'observacoes' in dir(evtDeslig.infoDeslig):

        for observacoes in evtDeslig.infoDeslig.observacoes:

            s2299_observacoes_dados = {}
            s2299_observacoes_dados['s2299_evtdeslig_id'] = s2299_evtdeslig.id

            try:
                s2299_observacoes_dados['observacao'] = observacoes.observacao.cdata
            except AttributeError:
                pass

            s2299_observacoes = s2299observacoes.objects.create(**s2299_observacoes_dados)

    if 'infoDeslig' in dir(evtDeslig) and 'sucessaoVinc' in dir(evtDeslig.infoDeslig):

        for sucessaoVinc in evtDeslig.infoDeslig.sucessaoVinc:

            s2299_sucessaovinc_dados = {}
            s2299_sucessaovinc_dados['s2299_evtdeslig_id'] = s2299_evtdeslig.id

            try:
                s2299_sucessaovinc_dados['tpinscsuc'] = sucessaoVinc.tpInscSuc.cdata
            except AttributeError:
                pass

            try:
                s2299_sucessaovinc_dados['cnpjsucessora'] = sucessaoVinc.cnpjSucessora.cdata
            except AttributeError:
                pass

            s2299_sucessaovinc = s2299sucessaoVinc.objects.create(**s2299_sucessaovinc_dados)

    if 'infoDeslig' in dir(evtDeslig) and 'transfTit' in dir(evtDeslig.infoDeslig):

        for transfTit in evtDeslig.infoDeslig.transfTit:

            s2299_transftit_dados = {}
            s2299_transftit_dados['s2299_evtdeslig_id'] = s2299_evtdeslig.id

            try:
                s2299_transftit_dados['cpfsubstituto'] = transfTit.cpfSubstituto.cdata
            except AttributeError:
                pass

            try:
                s2299_transftit_dados['dtnascto'] = transfTit.dtNascto.cdata
            except AttributeError:
                pass

            s2299_transftit = s2299transfTit.objects.create(**s2299_transftit_dados)

    if 'infoDeslig' in dir(evtDeslig) and 'mudancaCPF' in dir(evtDeslig.infoDeslig):

        for mudancaCPF in evtDeslig.infoDeslig.mudancaCPF:

            s2299_mudancacpf_dados = {}
            s2299_mudancacpf_dados['s2299_evtdeslig_id'] = s2299_evtdeslig.id

            try:
                s2299_mudancacpf_dados['novocpf'] = mudancaCPF.novoCPF.cdata
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
                        s2299_dmdev_dados['idedmdev'] = dmDev.ideDmDev.cdata
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
                                        s2299_infoperapur_ideestablot_dados['tpinsc'] = ideEstabLot.tpInsc.cdata
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2299_infoperapur_ideestablot_dados['nrinsc'] = ideEstabLot.nrInsc.cdata
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2299_infoperapur_ideestablot_dados['codlotacao'] = ideEstabLot.codLotacao.cdata
                                    except AttributeError:
                                        pass
        
                                    s2299_infoperapur_ideestablot = s2299infoPerApurideEstabLot.objects.create(**s2299_infoperapur_ideestablot_dados)
                
                                    if 'detVerbas' in dir(ideEstabLot):
                
                                        for detVerbas in ideEstabLot.detVerbas:
                
                                            s2299_infoperapur_detverbas_dados = {}
                                            s2299_infoperapur_detverbas_dados['s2299_infoperapur_ideestablot_id'] = s2299_infoperapur_ideestablot.id
                        
                                            try:
                                                s2299_infoperapur_detverbas_dados['codrubr'] = detVerbas.codRubr.cdata
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s2299_infoperapur_detverbas_dados['idetabrubr'] = detVerbas.ideTabRubr.cdata
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s2299_infoperapur_detverbas_dados['qtdrubr'] = detVerbas.qtdRubr.cdata
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s2299_infoperapur_detverbas_dados['fatorrubr'] = detVerbas.fatorRubr.cdata
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s2299_infoperapur_detverbas_dados['vrunit'] = detVerbas.vrUnit.cdata
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s2299_infoperapur_detverbas_dados['vrrubr'] = detVerbas.vrRubr.cdata
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
                                                        s2299_infoperapur_detoper_dados['cnpjoper'] = detOper.cnpjOper.cdata
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s2299_infoperapur_detoper_dados['regans'] = detOper.regANS.cdata
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s2299_infoperapur_detoper_dados['vrpgtit'] = detOper.vrPgTit.cdata
                                                    except AttributeError:
                                                        pass
                        
                                                    s2299_infoperapur_detoper = s2299infoPerApurdetOper.objects.create(**s2299_infoperapur_detoper_dados)
                                
                                                    if 'detPlano' in dir(detOper):
                                
                                                        for detPlano in detOper.detPlano:
                                
                                                            s2299_infoperapur_detplano_dados = {}
                                                            s2299_infoperapur_detplano_dados['s2299_infoperapur_detoper_id'] = s2299_infoperapur_detoper.id
                                        
                                                            try:
                                                                s2299_infoperapur_detplano_dados['tpdep'] = detPlano.tpDep.cdata
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperapur_detplano_dados['cpfdep'] = detPlano.cpfDep.cdata
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperapur_detplano_dados['nmdep'] = detPlano.nmDep.cdata
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperapur_detplano_dados['dtnascto'] = detPlano.dtNascto.cdata
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperapur_detplano_dados['vlrpgdep'] = detPlano.vlrPgDep.cdata
                                                            except AttributeError:
                                                                pass
                                
                                                            s2299_infoperapur_detplano = s2299infoPerApurdetPlano.objects.create(**s2299_infoperapur_detplano_dados)
                
                                    if 'infoAgNocivo' in dir(ideEstabLot):
                
                                        for infoAgNocivo in ideEstabLot.infoAgNocivo:
                
                                            s2299_infoperapur_infoagnocivo_dados = {}
                                            s2299_infoperapur_infoagnocivo_dados['s2299_infoperapur_ideestablot_id'] = s2299_infoperapur_ideestablot.id
                        
                                            try:
                                                s2299_infoperapur_infoagnocivo_dados['grauexp'] = infoAgNocivo.grauExp.cdata
                                            except AttributeError:
                                                pass
                
                                            s2299_infoperapur_infoagnocivo = s2299infoPerApurinfoAgNocivo.objects.create(**s2299_infoperapur_infoagnocivo_dados)
                
                                    if 'infoSimples' in dir(ideEstabLot):
                
                                        for infoSimples in ideEstabLot.infoSimples:
                
                                            s2299_infoperapur_infosimples_dados = {}
                                            s2299_infoperapur_infosimples_dados['s2299_infoperapur_ideestablot_id'] = s2299_infoperapur_ideestablot.id
                        
                                            try:
                                                s2299_infoperapur_infosimples_dados['indsimples'] = infoSimples.indSimples.cdata
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
                                        s2299_infoperant_ideadc_dados['dtacconv'] = ideADC.dtAcConv.cdata
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2299_infoperant_ideadc_dados['tpacconv'] = ideADC.tpAcConv.cdata
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2299_infoperant_ideadc_dados['compacconv'] = ideADC.compAcConv.cdata
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2299_infoperant_ideadc_dados['dtefacconv'] = ideADC.dtEfAcConv.cdata
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2299_infoperant_ideadc_dados['dsc'] = ideADC.dsc.cdata
                                    except AttributeError:
                                        pass
        
                                    s2299_infoperant_ideadc = s2299infoPerAntideADC.objects.create(**s2299_infoperant_ideadc_dados)
                
                                    if 'idePeriodo' in dir(ideADC):
                
                                        for idePeriodo in ideADC.idePeriodo:
                
                                            s2299_infoperant_ideperiodo_dados = {}
                                            s2299_infoperant_ideperiodo_dados['s2299_infoperant_ideadc_id'] = s2299_infoperant_ideadc.id
                        
                                            try:
                                                s2299_infoperant_ideperiodo_dados['perref'] = idePeriodo.perRef.cdata
                                            except AttributeError:
                                                pass
                
                                            s2299_infoperant_ideperiodo = s2299infoPerAntidePeriodo.objects.create(**s2299_infoperant_ideperiodo_dados)
                        
                                            if 'ideEstabLot' in dir(idePeriodo):
                        
                                                for ideEstabLot in idePeriodo.ideEstabLot:
                        
                                                    s2299_infoperant_ideestablot_dados = {}
                                                    s2299_infoperant_ideestablot_dados['s2299_infoperant_ideperiodo_id'] = s2299_infoperant_ideperiodo.id
                                
                                                    try:
                                                        s2299_infoperant_ideestablot_dados['tpinsc'] = ideEstabLot.tpInsc.cdata
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s2299_infoperant_ideestablot_dados['nrinsc'] = ideEstabLot.nrInsc.cdata
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s2299_infoperant_ideestablot_dados['codlotacao'] = ideEstabLot.codLotacao.cdata
                                                    except AttributeError:
                                                        pass
                        
                                                    s2299_infoperant_ideestablot = s2299infoPerAntideEstabLot.objects.create(**s2299_infoperant_ideestablot_dados)
                                
                                                    if 'detVerbas' in dir(ideEstabLot):
                                
                                                        for detVerbas in ideEstabLot.detVerbas:
                                
                                                            s2299_infoperant_detverbas_dados = {}
                                                            s2299_infoperant_detverbas_dados['s2299_infoperant_ideestablot_id'] = s2299_infoperant_ideestablot.id
                                        
                                                            try:
                                                                s2299_infoperant_detverbas_dados['codrubr'] = detVerbas.codRubr.cdata
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperant_detverbas_dados['idetabrubr'] = detVerbas.ideTabRubr.cdata
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperant_detverbas_dados['qtdrubr'] = detVerbas.qtdRubr.cdata
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperant_detverbas_dados['fatorrubr'] = detVerbas.fatorRubr.cdata
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperant_detverbas_dados['vrunit'] = detVerbas.vrUnit.cdata
                                                            except AttributeError:
                                                                pass
                                        
                                                            try:
                                                                s2299_infoperant_detverbas_dados['vrrubr'] = detVerbas.vrRubr.cdata
                                                            except AttributeError:
                                                                pass
                                
                                                            s2299_infoperant_detverbas = s2299infoPerAntdetVerbas.objects.create(**s2299_infoperant_detverbas_dados)
                                
                                                    if 'infoAgNocivo' in dir(ideEstabLot):
                                
                                                        for infoAgNocivo in ideEstabLot.infoAgNocivo:
                                
                                                            s2299_infoperant_infoagnocivo_dados = {}
                                                            s2299_infoperant_infoagnocivo_dados['s2299_infoperant_ideestablot_id'] = s2299_infoperant_ideestablot.id
                                        
                                                            try:
                                                                s2299_infoperant_infoagnocivo_dados['grauexp'] = infoAgNocivo.grauExp.cdata
                                                            except AttributeError:
                                                                pass
                                
                                                            s2299_infoperant_infoagnocivo = s2299infoPerAntinfoAgNocivo.objects.create(**s2299_infoperant_infoagnocivo_dados)
                                
                                                    if 'infoSimples' in dir(ideEstabLot):
                                
                                                        for infoSimples in ideEstabLot.infoSimples:
                                
                                                            s2299_infoperant_infosimples_dados = {}
                                                            s2299_infoperant_infosimples_dados['s2299_infoperant_ideestablot_id'] = s2299_infoperant_ideestablot.id
                                        
                                                            try:
                                                                s2299_infoperant_infosimples_dados['indsimples'] = infoSimples.indSimples.cdata
                                                            except AttributeError:
                                                                pass
                                
                                                            s2299_infoperant_infosimples = s2299infoPerAntinfoSimples.objects.create(**s2299_infoperant_infosimples_dados)

                    if 'infoTrabInterm' in dir(dmDev):

                        for infoTrabInterm in dmDev.infoTrabInterm:

                            s2299_infotrabinterm_dados = {}
                            s2299_infotrabinterm_dados['s2299_dmdev_id'] = s2299_dmdev.id
        
                            try:
                                s2299_infotrabinterm_dados['codconv'] = infoTrabInterm.codConv.cdata
                            except AttributeError:
                                pass

                            s2299_infotrabinterm = s2299infoTrabInterm.objects.create(**s2299_infotrabinterm_dados)

            if 'procJudTrab' in dir(verbasResc):

                for procJudTrab in verbasResc.procJudTrab:

                    s2299_infotrabinterm_procjudtrab_dados = {}
                    s2299_infotrabinterm_procjudtrab_dados['s2299_verbasresc_id'] = s2299_verbasresc.id

                    try:
                        s2299_infotrabinterm_procjudtrab_dados['tptrib'] = procJudTrab.tpTrib.cdata
                    except AttributeError:
                        pass

                    try:
                        s2299_infotrabinterm_procjudtrab_dados['nrprocjud'] = procJudTrab.nrProcJud.cdata
                    except AttributeError:
                        pass

                    try:
                        s2299_infotrabinterm_procjudtrab_dados['codsusp'] = procJudTrab.codSusp.cdata
                    except AttributeError:
                        pass

                    s2299_infotrabinterm_procjudtrab = s2299infoTrabIntermprocJudTrab.objects.create(**s2299_infotrabinterm_procjudtrab_dados)

            if 'infoMV' in dir(verbasResc):

                for infoMV in verbasResc.infoMV:

                    s2299_infotrabinterm_infomv_dados = {}
                    s2299_infotrabinterm_infomv_dados['s2299_verbasresc_id'] = s2299_verbasresc.id

                    try:
                        s2299_infotrabinterm_infomv_dados['indmv'] = infoMV.indMV.cdata
                    except AttributeError:
                        pass

                    s2299_infotrabinterm_infomv = s2299infoTrabInterminfoMV.objects.create(**s2299_infotrabinterm_infomv_dados)

                    if 'remunOutrEmpr' in dir(infoMV):

                        for remunOutrEmpr in infoMV.remunOutrEmpr:

                            s2299_infotrabinterm_remunoutrempr_dados = {}
                            s2299_infotrabinterm_remunoutrempr_dados['s2299_infotrabinterm_infomv_id'] = s2299_infotrabinterm_infomv.id
        
                            try:
                                s2299_infotrabinterm_remunoutrempr_dados['tpinsc'] = remunOutrEmpr.tpInsc.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2299_infotrabinterm_remunoutrempr_dados['nrinsc'] = remunOutrEmpr.nrInsc.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2299_infotrabinterm_remunoutrempr_dados['codcateg'] = remunOutrEmpr.codCateg.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2299_infotrabinterm_remunoutrempr_dados['vlrremunoe'] = remunOutrEmpr.vlrRemunOE.cdata
                            except AttributeError:
                                pass

                            s2299_infotrabinterm_remunoutrempr = s2299infoTrabIntermremunOutrEmpr.objects.create(**s2299_infotrabinterm_remunoutrempr_dados)

            if 'procCS' in dir(verbasResc):

                for procCS in verbasResc.procCS:

                    s2299_infotrabinterm_proccs_dados = {}
                    s2299_infotrabinterm_proccs_dados['s2299_verbasresc_id'] = s2299_verbasresc.id

                    try:
                        s2299_infotrabinterm_proccs_dados['nrprocjud'] = procCS.nrProcJud.cdata
                    except AttributeError:
                        pass

                    s2299_infotrabinterm_proccs = s2299infoTrabIntermprocCS.objects.create(**s2299_infotrabinterm_proccs_dados)

    if 'infoDeslig' in dir(evtDeslig) and 'quarentena' in dir(evtDeslig.infoDeslig):

        for quarentena in evtDeslig.infoDeslig.quarentena:

            s2299_infotrabinterm_quarentena_dados = {}
            s2299_infotrabinterm_quarentena_dados['s2299_evtdeslig_id'] = s2299_evtdeslig.id

            try:
                s2299_infotrabinterm_quarentena_dados['dtfimquar'] = quarentena.dtFimQuar.cdata
            except AttributeError:
                pass

            s2299_infotrabinterm_quarentena = s2299infoTrabIntermquarentena.objects.create(**s2299_infotrabinterm_quarentena_dados)

    if 'infoDeslig' in dir(evtDeslig) and 'consigFGTS' in dir(evtDeslig.infoDeslig):

        for consigFGTS in evtDeslig.infoDeslig.consigFGTS:

            s2299_infotrabinterm_consigfgts_dados = {}
            s2299_infotrabinterm_consigfgts_dados['s2299_evtdeslig_id'] = s2299_evtdeslig.id

            try:
                s2299_infotrabinterm_consigfgts_dados['insconsig'] = consigFGTS.insConsig.cdata
            except AttributeError:
                pass

            try:
                s2299_infotrabinterm_consigfgts_dados['nrcontr'] = consigFGTS.nrContr.cdata
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