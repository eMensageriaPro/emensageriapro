#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2399.models import *



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
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2399_evttsvtermino_obj(request, doc, status, validar)

    s2399evtTSVTermino.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s2399_evttsvtermino_obj(request, doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2399_evttsvtermino_dados = {}
    s2399_evttsvtermino_dados['status'] = status
    s2399_evttsvtermino_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2399_evttsvtermino_dados['identidade'] = doc.eSocial.evtTSVTermino['Id']
    evtTSVTermino = doc.eSocial.evtTSVTermino
    
    try:
        s2399_evttsvtermino_dados['indretif'] = evtTSVTermino.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        s2399_evttsvtermino_dados['nrrecibo'] = evtTSVTermino.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        s2399_evttsvtermino_dados['tpamb'] = evtTSVTermino.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s2399_evttsvtermino_dados['procemi'] = evtTSVTermino.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s2399_evttsvtermino_dados['verproc'] = evtTSVTermino.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s2399_evttsvtermino_dados['tpinsc'] = evtTSVTermino.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2399_evttsvtermino_dados['nrinsc'] = evtTSVTermino.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2399_evttsvtermino_dados['cpftrab'] = evtTSVTermino.ideTrabSemVinculo.cpfTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2399_evttsvtermino_dados['nistrab'] = evtTSVTermino.ideTrabSemVinculo.nisTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2399_evttsvtermino_dados['codcateg'] = evtTSVTermino.ideTrabSemVinculo.codCateg.cdata
    except AttributeError: 
        pass
    
    try:
        s2399_evttsvtermino_dados['dtterm'] = evtTSVTermino.infoTSVTermino.dtTerm.cdata
    except AttributeError: 
        pass
    
    try:
        s2399_evttsvtermino_dados['mtvdesligtsv'] = evtTSVTermino.infoTSVTermino.mtvDesligTSV.cdata
    except AttributeError: 
        pass
    
    try:
        s2399_evttsvtermino_dados['pensalim'] = evtTSVTermino.infoTSVTermino.pensAlim.cdata
    except AttributeError: 
        pass
    
    try:
        s2399_evttsvtermino_dados['percaliment'] = evtTSVTermino.infoTSVTermino.percAliment.cdata
    except AttributeError: 
        pass
    
    try:
        s2399_evttsvtermino_dados['vralim'] = evtTSVTermino.infoTSVTermino.vrAlim.cdata
    except AttributeError: 
        pass
        
    s2399_evttsvtermino = s2399evtTSVTermino.objects.create(**s2399_evttsvtermino_dados)
    
    if 'infoTSVTermino' in dir(evtTSVTermino) and 'mudancaCPF' in dir(evtTSVTermino.infoTSVTermino):
    
        for mudancaCPF in evtTSVTermino.infoTSVTermino.mudancaCPF:
    
            s2399_mudancacpf_dados = {}
            s2399_mudancacpf_dados['s2399_evttsvtermino_id'] = s2399_evttsvtermino.id
            
            try:
                s2399_mudancacpf_dados['novocpf'] = mudancaCPF.novoCPF.cdata
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
                        s2399_dmdev_dados['idedmdev'] = dmDev.ideDmDev.cdata
                    except AttributeError: 
                        pass
            
                    s2399_dmdev = s2399dmDev.objects.create(**s2399_dmdev_dados)
                    
                    if 'ideEstabLot' in dir(dmDev):
                    
                        for ideEstabLot in dmDev.ideEstabLot:
                    
                            s2399_ideestablot_dados = {}
                            s2399_ideestablot_dados['s2399_dmdev_id'] = s2399_dmdev.id
                            
                            try:
                                s2399_ideestablot_dados['tpinsc'] = ideEstabLot.tpInsc.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s2399_ideestablot_dados['nrinsc'] = ideEstabLot.nrInsc.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s2399_ideestablot_dados['codlotacao'] = ideEstabLot.codLotacao.cdata
                            except AttributeError: 
                                pass
                    
                            s2399_ideestablot = s2399ideEstabLot.objects.create(**s2399_ideestablot_dados)
                            
                            if 'detVerbas' in dir(ideEstabLot):
                            
                                for detVerbas in ideEstabLot.detVerbas:
                            
                                    s2399_detverbas_dados = {}
                                    s2399_detverbas_dados['s2399_ideestablot_id'] = s2399_ideestablot.id
                                    
                                    try:
                                        s2399_detverbas_dados['codrubr'] = detVerbas.codRubr.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        s2399_detverbas_dados['idetabrubr'] = detVerbas.ideTabRubr.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        s2399_detverbas_dados['qtdrubr'] = detVerbas.qtdRubr.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        s2399_detverbas_dados['fatorrubr'] = detVerbas.fatorRubr.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        s2399_detverbas_dados['vrunit'] = detVerbas.vrUnit.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        s2399_detverbas_dados['vrrubr'] = detVerbas.vrRubr.cdata
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
                                                s2399_detoper_dados['cnpjoper'] = detOper.cnpjOper.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                s2399_detoper_dados['regans'] = detOper.regANS.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                s2399_detoper_dados['vrpgtit'] = detOper.vrPgTit.cdata
                                            except AttributeError: 
                                                pass
                                    
                                            s2399_detoper = s2399detOper.objects.create(**s2399_detoper_dados)
                                            
                                            if 'detPlano' in dir(detOper):
                                            
                                                for detPlano in detOper.detPlano:
                                            
                                                    s2399_detplano_dados = {}
                                                    s2399_detplano_dados['s2399_detoper_id'] = s2399_detoper.id
                                                    
                                                    try:
                                                        s2399_detplano_dados['tpdep'] = detPlano.tpDep.cdata
                                                    except AttributeError: 
                                                        pass
                                                    
                                                    try:
                                                        s2399_detplano_dados['cpfdep'] = detPlano.cpfDep.cdata
                                                    except AttributeError: 
                                                        pass
                                                    
                                                    try:
                                                        s2399_detplano_dados['nmdep'] = detPlano.nmDep.cdata
                                                    except AttributeError: 
                                                        pass
                                                    
                                                    try:
                                                        s2399_detplano_dados['dtnascto'] = detPlano.dtNascto.cdata
                                                    except AttributeError: 
                                                        pass
                                                    
                                                    try:
                                                        s2399_detplano_dados['vlrpgdep'] = detPlano.vlrPgDep.cdata
                                                    except AttributeError: 
                                                        pass
                                            
                                                    s2399_detplano = s2399detPlano.objects.create(**s2399_detplano_dados)
                            
                            if 'infoAgNocivo' in dir(ideEstabLot):
                            
                                for infoAgNocivo in ideEstabLot.infoAgNocivo:
                            
                                    s2399_infoagnocivo_dados = {}
                                    s2399_infoagnocivo_dados['s2399_ideestablot_id'] = s2399_ideestablot.id
                                    
                                    try:
                                        s2399_infoagnocivo_dados['grauexp'] = infoAgNocivo.grauExp.cdata
                                    except AttributeError: 
                                        pass
                            
                                    s2399_infoagnocivo = s2399infoAgNocivo.objects.create(**s2399_infoagnocivo_dados)
                            
                            if 'infoSimples' in dir(ideEstabLot):
                            
                                for infoSimples in ideEstabLot.infoSimples:
                            
                                    s2399_infosimples_dados = {}
                                    s2399_infosimples_dados['s2399_ideestablot_id'] = s2399_ideestablot.id
                                    
                                    try:
                                        s2399_infosimples_dados['indsimples'] = infoSimples.indSimples.cdata
                                    except AttributeError: 
                                        pass
                            
                                    s2399_infosimples = s2399infoSimples.objects.create(**s2399_infosimples_dados)
            
            if 'procJudTrab' in dir(verbasResc):
            
                for procJudTrab in verbasResc.procJudTrab:
            
                    s2399_procjudtrab_dados = {}
                    s2399_procjudtrab_dados['s2399_verbasresc_id'] = s2399_verbasresc.id
                    
                    try:
                        s2399_procjudtrab_dados['tptrib'] = procJudTrab.tpTrib.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2399_procjudtrab_dados['nrprocjud'] = procJudTrab.nrProcJud.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2399_procjudtrab_dados['codsusp'] = procJudTrab.codSusp.cdata
                    except AttributeError: 
                        pass
            
                    s2399_procjudtrab = s2399procJudTrab.objects.create(**s2399_procjudtrab_dados)
            
            if 'infoMV' in dir(verbasResc):
            
                for infoMV in verbasResc.infoMV:
            
                    s2399_infomv_dados = {}
                    s2399_infomv_dados['s2399_verbasresc_id'] = s2399_verbasresc.id
                    
                    try:
                        s2399_infomv_dados['indmv'] = infoMV.indMV.cdata
                    except AttributeError: 
                        pass
            
                    s2399_infomv = s2399infoMV.objects.create(**s2399_infomv_dados)
                    
                    if 'remunOutrEmpr' in dir(infoMV):
                    
                        for remunOutrEmpr in infoMV.remunOutrEmpr:
                    
                            s2399_remunoutrempr_dados = {}
                            s2399_remunoutrempr_dados['s2399_infomv_id'] = s2399_infomv.id
                            
                            try:
                                s2399_remunoutrempr_dados['tpinsc'] = remunOutrEmpr.tpInsc.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s2399_remunoutrempr_dados['nrinsc'] = remunOutrEmpr.nrInsc.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s2399_remunoutrempr_dados['codcateg'] = remunOutrEmpr.codCateg.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s2399_remunoutrempr_dados['vlrremunoe'] = remunOutrEmpr.vlrRemunOE.cdata
                            except AttributeError: 
                                pass
                    
                            s2399_remunoutrempr = s2399remunOutrEmpr.objects.create(**s2399_remunoutrempr_dados)
    
    if 'infoTSVTermino' in dir(evtTSVTermino) and 'quarentena' in dir(evtTSVTermino.infoTSVTermino):
    
        for quarentena in evtTSVTermino.infoTSVTermino.quarentena:
    
            s2399_quarentena_dados = {}
            s2399_quarentena_dados['s2399_evttsvtermino_id'] = s2399_evttsvtermino.id
            
            try:
                s2399_quarentena_dados['dtfimquar'] = quarentena.dtFimQuar.cdata
            except AttributeError: 
                pass
    
            s2399_quarentena = s2399quarentena.objects.create(**s2399_quarentena_dados)    
    s2399_evttsvtermino_dados['evento'] = 's2399'
    s2399_evttsvtermino_dados['id'] = s2399_evttsvtermino.id
    s2399_evttsvtermino_dados['identidade_evento'] = doc.eSocial.evtTSVTermino['Id']
    s2399_evttsvtermino_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s2399_evttsvtermino_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, s2399_evttsvtermino.id)
    
    return s2399_evttsvtermino_dados