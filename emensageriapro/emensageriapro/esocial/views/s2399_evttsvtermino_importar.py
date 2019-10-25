#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2399.models import *
from emensageriapro.functions import read_from_xml



def read_s2399_evttsvtermino_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2399_evttsvtermino_obj(request, doc, status, validar)
    return dados



def read_s2399_evttsvtermino(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2399_evttsvtermino_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2399evtTSVTermino.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2399_evttsvtermino_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2399_evttsvtermino_dados = {}
    s2399_evttsvtermino_dados['status'] = status
    s2399_evttsvtermino_dados['arquivo_original'] = 1
    if arquivo:
        s2399_evttsvtermino_dados['arquivo'] = arquivo.arquivo
    s2399_evttsvtermino_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2399_evttsvtermino_dados['identidade'] = doc.eSocial.evtTSVTermino['Id']
    evtTSVTermino = doc.eSocial.evtTSVTermino

    try:
        s2399_evttsvtermino_dados['indretif'] = read_from_xml(evtTSVTermino.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2399_evttsvtermino_dados['nrrecibo'] = read_from_xml(evtTSVTermino.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2399_evttsvtermino_dados['tpamb'] = read_from_xml(evtTSVTermino.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2399_evttsvtermino_dados['procemi'] = read_from_xml(evtTSVTermino.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2399_evttsvtermino_dados['verproc'] = read_from_xml(evtTSVTermino.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2399_evttsvtermino_dados['tpinsc'] = read_from_xml(evtTSVTermino.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2399_evttsvtermino_dados['nrinsc'] = read_from_xml(evtTSVTermino.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2399_evttsvtermino_dados['cpftrab'] = read_from_xml(evtTSVTermino.ideTrabSemVinculo.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2399_evttsvtermino_dados['nistrab'] = read_from_xml(evtTSVTermino.ideTrabSemVinculo.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2399_evttsvtermino_dados['codcateg'] = read_from_xml(evtTSVTermino.ideTrabSemVinculo.codCateg.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2399_evttsvtermino_dados['dtterm'] = read_from_xml(evtTSVTermino.infoTSVTermino.dtTerm.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2399_evttsvtermino_dados['mtvdesligtsv'] = read_from_xml(evtTSVTermino.infoTSVTermino.mtvDesligTSV.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2399_evttsvtermino_dados['pensalim'] = read_from_xml(evtTSVTermino.infoTSVTermino.pensAlim.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2399_evttsvtermino_dados['percaliment'] = read_from_xml(evtTSVTermino.infoTSVTermino.percAliment.cdata, 'esocial', 'N', 2)
    except AttributeError:
        pass

    try:
        s2399_evttsvtermino_dados['vralim'] = read_from_xml(evtTSVTermino.infoTSVTermino.vrAlim.cdata, 'esocial', 'N', 2)
    except AttributeError:
        pass

    s2399_evttsvtermino = s2399evtTSVTermino.objects.create(**s2399_evttsvtermino_dados)

    if 'infoTSVTermino' in dir(evtTSVTermino) and 'mudancaCPF' in dir(evtTSVTermino.infoTSVTermino):

        for mudancaCPF in evtTSVTermino.infoTSVTermino.mudancaCPF:

            s2399_mudancacpf_dados = {}
            s2399_mudancacpf_dados['s2399_evttsvtermino_id'] = s2399_evttsvtermino.id

            try:
                s2399_mudancacpf_dados['novocpf'] = read_from_xml(mudancaCPF.novoCPF.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2399_mudancacpf = s2399mudancaCPF.objects.create(**s2399_mudancacpf_dados)

    if 'infoTSVTermino' in dir(evtTSVTermino) and 'verbasResc' in dir(evtTSVTermino.infoTSVTermino):

        for verbasResc in evtTSVTermino.infoTSVTermino.verbasResc:

            s2399_verbasresc_dados = {}
            s2399_verbasresc_dados['s2399_evttsvtermino_id'] = s2399_evttsvtermino.id

            s2399_verbasresc = s2399verbasResc.objects.create(**s2399_verbasresc_dados)

            if 'dmDev' in dir(verbasResc):

                for dmDev in verbasResc.dmDev:

                    s2399_dmdev_dados = {}
                    s2399_dmdev_dados['s2399_verbasresc_id'] = s2399_verbasresc.id

                    try:
                        s2399_dmdev_dados['idedmdev'] = read_from_xml(dmDev.ideDmDev.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2399_dmdev = s2399dmDev.objects.create(**s2399_dmdev_dados)

                    if 'ideEstabLot' in dir(dmDev):

                        for ideEstabLot in dmDev.ideEstabLot:

                            s2399_ideestablot_dados = {}
                            s2399_ideestablot_dados['s2399_dmdev_id'] = s2399_dmdev.id
        
                            try:
                                s2399_ideestablot_dados['tpinsc'] = read_from_xml(ideEstabLot.tpInsc.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2399_ideestablot_dados['nrinsc'] = read_from_xml(ideEstabLot.nrInsc.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2399_ideestablot_dados['codlotacao'] = read_from_xml(ideEstabLot.codLotacao.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s2399_ideestablot = s2399ideEstabLot.objects.create(**s2399_ideestablot_dados)
        
                            if 'detVerbas' in dir(ideEstabLot):
        
                                for detVerbas in ideEstabLot.detVerbas:
        
                                    s2399_detverbas_dados = {}
                                    s2399_detverbas_dados['s2399_ideestablot_id'] = s2399_ideestablot.id
                
                                    try:
                                        s2399_detverbas_dados['codrubr'] = read_from_xml(detVerbas.codRubr.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2399_detverbas_dados['idetabrubr'] = read_from_xml(detVerbas.ideTabRubr.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2399_detverbas_dados['qtdrubr'] = read_from_xml(detVerbas.qtdRubr.cdata, 'esocial', 'N', 2)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2399_detverbas_dados['fatorrubr'] = read_from_xml(detVerbas.fatorRubr.cdata, 'esocial', 'N', 2)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2399_detverbas_dados['vrunit'] = read_from_xml(detVerbas.vrUnit.cdata, 'esocial', 'N', 2)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2399_detverbas_dados['vrrubr'] = read_from_xml(detVerbas.vrRubr.cdata, 'esocial', 'N', 2)
                                    except AttributeError:
                                        pass
        
                                    s2399_detverbas = s2399detVerbas.objects.create(**s2399_detverbas_dados)
        
                            if 'infoSaudeColet' in dir(ideEstabLot):
        
                                for infoSaudeColet in ideEstabLot.infoSaudeColet:
        
                                    s2399_infosaudecolet_dados = {}
                                    s2399_infosaudecolet_dados['s2399_ideestablot_id'] = s2399_ideestablot.id
        
                                    s2399_infosaudecolet = s2399infoSaudeColet.objects.create(**s2399_infosaudecolet_dados)
                
                                    if 'detOper' in dir(infoSaudeColet):
                
                                        for detOper in infoSaudeColet.detOper:
                
                                            s2399_detoper_dados = {}
                                            s2399_detoper_dados['s2399_infosaudecolet_id'] = s2399_infosaudecolet.id
                        
                                            try:
                                                s2399_detoper_dados['cnpjoper'] = read_from_xml(detOper.cnpjOper.cdata, 'esocial', 'C', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s2399_detoper_dados['regans'] = read_from_xml(detOper.regANS.cdata, 'esocial', 'C', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                s2399_detoper_dados['vrpgtit'] = read_from_xml(detOper.vrPgTit.cdata, 'esocial', 'N', 2)
                                            except AttributeError:
                                                pass
                
                                            s2399_detoper = s2399detOper.objects.create(**s2399_detoper_dados)
                        
                                            if 'detPlano' in dir(detOper):
                        
                                                for detPlano in detOper.detPlano:
                        
                                                    s2399_detplano_dados = {}
                                                    s2399_detplano_dados['s2399_detoper_id'] = s2399_detoper.id
                                
                                                    try:
                                                        s2399_detplano_dados['tpdep'] = read_from_xml(detPlano.tpDep.cdata, 'esocial', 'C', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s2399_detplano_dados['cpfdep'] = read_from_xml(detPlano.cpfDep.cdata, 'esocial', 'C', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s2399_detplano_dados['nmdep'] = read_from_xml(detPlano.nmDep.cdata, 'esocial', 'C', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s2399_detplano_dados['dtnascto'] = read_from_xml(detPlano.dtNascto.cdata, 'esocial', 'D', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        s2399_detplano_dados['vlrpgdep'] = read_from_xml(detPlano.vlrPgDep.cdata, 'esocial', 'N', 2)
                                                    except AttributeError:
                                                        pass
                        
                                                    s2399_detplano = s2399detPlano.objects.create(**s2399_detplano_dados)
        
                            if 'infoAgNocivo' in dir(ideEstabLot):
        
                                for infoAgNocivo in ideEstabLot.infoAgNocivo:
        
                                    s2399_infoagnocivo_dados = {}
                                    s2399_infoagnocivo_dados['s2399_ideestablot_id'] = s2399_ideestablot.id
                
                                    try:
                                        s2399_infoagnocivo_dados['grauexp'] = read_from_xml(infoAgNocivo.grauExp.cdata, 'esocial', 'N', None)
                                    except AttributeError:
                                        pass
        
                                    s2399_infoagnocivo = s2399infoAgNocivo.objects.create(**s2399_infoagnocivo_dados)
        
                            if 'infoSimples' in dir(ideEstabLot):
        
                                for infoSimples in ideEstabLot.infoSimples:
        
                                    s2399_infosimples_dados = {}
                                    s2399_infosimples_dados['s2399_ideestablot_id'] = s2399_ideestablot.id
                
                                    try:
                                        s2399_infosimples_dados['indsimples'] = read_from_xml(infoSimples.indSimples.cdata, 'esocial', 'N', None)
                                    except AttributeError:
                                        pass
        
                                    s2399_infosimples = s2399infoSimples.objects.create(**s2399_infosimples_dados)

            if 'procJudTrab' in dir(verbasResc):

                for procJudTrab in verbasResc.procJudTrab:

                    s2399_procjudtrab_dados = {}
                    s2399_procjudtrab_dados['s2399_verbasresc_id'] = s2399_verbasresc.id

                    try:
                        s2399_procjudtrab_dados['tptrib'] = read_from_xml(procJudTrab.tpTrib.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2399_procjudtrab_dados['nrprocjud'] = read_from_xml(procJudTrab.nrProcJud.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2399_procjudtrab_dados['codsusp'] = read_from_xml(procJudTrab.codSusp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s2399_procjudtrab = s2399procJudTrab.objects.create(**s2399_procjudtrab_dados)

            if 'infoMV' in dir(verbasResc):

                for infoMV in verbasResc.infoMV:

                    s2399_infomv_dados = {}
                    s2399_infomv_dados['s2399_verbasresc_id'] = s2399_verbasresc.id

                    try:
                        s2399_infomv_dados['indmv'] = read_from_xml(infoMV.indMV.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s2399_infomv = s2399infoMV.objects.create(**s2399_infomv_dados)

                    if 'remunOutrEmpr' in dir(infoMV):

                        for remunOutrEmpr in infoMV.remunOutrEmpr:

                            s2399_remunoutrempr_dados = {}
                            s2399_remunoutrempr_dados['s2399_infomv_id'] = s2399_infomv.id
        
                            try:
                                s2399_remunoutrempr_dados['tpinsc'] = read_from_xml(remunOutrEmpr.tpInsc.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2399_remunoutrempr_dados['nrinsc'] = read_from_xml(remunOutrEmpr.nrInsc.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2399_remunoutrempr_dados['codcateg'] = read_from_xml(remunOutrEmpr.codCateg.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2399_remunoutrempr_dados['vlrremunoe'] = read_from_xml(remunOutrEmpr.vlrRemunOE.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s2399_remunoutrempr = s2399remunOutrEmpr.objects.create(**s2399_remunoutrempr_dados)

    if 'infoTSVTermino' in dir(evtTSVTermino) and 'quarentena' in dir(evtTSVTermino.infoTSVTermino):

        for quarentena in evtTSVTermino.infoTSVTermino.quarentena:

            s2399_quarentena_dados = {}
            s2399_quarentena_dados['s2399_evttsvtermino_id'] = s2399_evttsvtermino.id

            try:
                s2399_quarentena_dados['dtfimquar'] = read_from_xml(quarentena.dtFimQuar.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            s2399_quarentena = s2399quarentena.objects.create(**s2399_quarentena_dados)
    s2399_evttsvtermino_dados['evento'] = 's2399'
    s2399_evttsvtermino_dados['id'] = s2399_evttsvtermino.id
    s2399_evttsvtermino_dados['identidade_evento'] = doc.eSocial.evtTSVTermino['Id']

    from emensageriapro.esocial.views.s2399_evttsvtermino_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2399_evttsvtermino.id)

    return s2399_evttsvtermino_dados