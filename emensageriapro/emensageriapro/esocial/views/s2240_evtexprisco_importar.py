#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2240.models import *
from emensageriapro.functions import read_from_xml



def read_s2240_evtexprisco_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2240_evtexprisco_obj(request, doc, status, validar)
    return dados



def read_s2240_evtexprisco(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2240_evtexprisco_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2240evtExpRisco.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2240_evtexprisco_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2240_evtexprisco_dados = {}
    s2240_evtexprisco_dados['status'] = status
    s2240_evtexprisco_dados['arquivo_original'] = 1
    if arquivo:
        s2240_evtexprisco_dados['arquivo'] = arquivo.arquivo
    s2240_evtexprisco_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2240_evtexprisco_dados['identidade'] = doc.eSocial.evtExpRisco['Id']
    evtExpRisco = doc.eSocial.evtExpRisco

    try:
        s2240_evtexprisco_dados['indretif'] = read_from_xml(evtExpRisco.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['nrrecibo'] = read_from_xml(evtExpRisco.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['tpamb'] = read_from_xml(evtExpRisco.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['procemi'] = read_from_xml(evtExpRisco.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['verproc'] = read_from_xml(evtExpRisco.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['tpinsc'] = read_from_xml(evtExpRisco.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['nrinsc'] = read_from_xml(evtExpRisco.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['cpftrab'] = read_from_xml(evtExpRisco.ideVinculo.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['nistrab'] = read_from_xml(evtExpRisco.ideVinculo.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['matricula'] = read_from_xml(evtExpRisco.ideVinculo.matricula.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['codcateg'] = read_from_xml(evtExpRisco.ideVinculo.codCateg.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['dtinicondicao'] = read_from_xml(evtExpRisco.infoExpRisco.dtIniCondicao.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['dscativdes'] = read_from_xml(evtExpRisco.infoExpRisco.infoAtiv.dscAtivDes.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s2240_evtexprisco = s2240evtExpRisco.objects.create(**s2240_evtexprisco_dados)

    if 'infoExpRisco' in dir(evtExpRisco) and 'infoAmb' in dir(evtExpRisco.infoExpRisco):

        for infoAmb in evtExpRisco.infoExpRisco.infoAmb:

            s2240_iniexprisco_infoamb_dados = {}
            s2240_iniexprisco_infoamb_dados['s2240_evtexprisco_id'] = s2240_evtexprisco.id

            try:
                s2240_iniexprisco_infoamb_dados['codamb'] = read_from_xml(infoAmb.codAmb.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2240_iniexprisco_infoamb = s2240iniExpRiscoinfoAmb.objects.create(**s2240_iniexprisco_infoamb_dados)

    if 'infoExpRisco' in dir(evtExpRisco) and 'infoAtiv' in dir(evtExpRisco.infoExpRisco) and 'ativPericInsal' in dir(evtExpRisco.infoExpRisco.infoAtiv):

        for ativPericInsal in evtExpRisco.infoExpRisco.infoAtiv.ativPericInsal:

            s2240_iniexprisco_ativpericinsal_dados = {}
            s2240_iniexprisco_ativpericinsal_dados['s2240_evtexprisco_id'] = s2240_evtexprisco.id

            try:
                s2240_iniexprisco_ativpericinsal_dados['codativ'] = read_from_xml(ativPericInsal.codAtiv.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2240_iniexprisco_ativpericinsal = s2240iniExpRiscoativPericInsal.objects.create(**s2240_iniexprisco_ativpericinsal_dados)

    if 'infoExpRisco' in dir(evtExpRisco) and 'fatRisco' in dir(evtExpRisco.infoExpRisco):

        for fatRisco in evtExpRisco.infoExpRisco.fatRisco:

            s2240_iniexprisco_fatrisco_dados = {}
            s2240_iniexprisco_fatrisco_dados['s2240_evtexprisco_id'] = s2240_evtexprisco.id

            try:
                s2240_iniexprisco_fatrisco_dados['codfatris'] = read_from_xml(fatRisco.codFatRis.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['dscfatrisc'] = read_from_xml(fatRisco.dscFatRisc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['tpaval'] = read_from_xml(fatRisco.tpAval.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['intconc'] = read_from_xml(fatRisco.intConc.cdata, 'esocial', 'N', 4)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['limtol'] = read_from_xml(fatRisco.limTol.cdata, 'esocial', 'N', 4)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['unmed'] = read_from_xml(fatRisco.unMed.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['tecmedicao'] = read_from_xml(fatRisco.tecMedicao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['insalubridade'] = read_from_xml(fatRisco.insalubridade.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['periculosidade'] = read_from_xml(fatRisco.periculosidade.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['aposentesp'] = read_from_xml(fatRisco.aposentEsp.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['utilizepc'] = read_from_xml(fatRisco.epcEpi.utilizEPC.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['eficepc'] = read_from_xml(fatRisco.epcEpi.eficEpc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['utilizepi'] = read_from_xml(fatRisco.epcEpi.utilizEPI.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s2240_iniexprisco_fatrisco = s2240iniExpRiscofatRisco.objects.create(**s2240_iniexprisco_fatrisco_dados)

            if 'epcEpi' in dir(fatRisco) and 'epc' in dir(fatRisco.epcEpi):

                for epc in fatRisco.epcEpi.epc:

                    s2240_iniexprisco_epc_dados = {}
                    s2240_iniexprisco_epc_dados['s2240_iniexprisco_fatrisco_id'] = s2240_iniexprisco_fatrisco.id

                    try:
                        s2240_iniexprisco_epc_dados['codep'] = read_from_xml(epc.codEP.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epc_dados['dscepc'] = read_from_xml(epc.dscEpc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epc_dados['eficepc'] = read_from_xml(epc.eficEpc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2240_iniexprisco_epc = s2240iniExpRiscoepc.objects.create(**s2240_iniexprisco_epc_dados)

            if 'epcEpi' in dir(fatRisco) and 'epi' in dir(fatRisco.epcEpi):

                for epi in fatRisco.epcEpi.epi:

                    s2240_iniexprisco_epi_dados = {}
                    s2240_iniexprisco_epi_dados['s2240_iniexprisco_fatrisco_id'] = s2240_iniexprisco_fatrisco.id

                    try:
                        s2240_iniexprisco_epi_dados['caepi'] = read_from_xml(epi.caEPI.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epi_dados['dscepi'] = read_from_xml(epi.dscEPI.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epi_dados['eficepi'] = read_from_xml(epi.eficEpi.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epi_dados['medprotecao'] = read_from_xml(epi.medProtecao.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epi_dados['condfuncto'] = read_from_xml(epi.condFuncto.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epi_dados['usoinint'] = read_from_xml(epi.usoInint.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epi_dados['przvalid'] = read_from_xml(epi.przValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epi_dados['periodictroca'] = read_from_xml(epi.periodicTroca.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epi_dados['higienizacao'] = read_from_xml(epi.higienizacao.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2240_iniexprisco_epi = s2240iniExpRiscoepi.objects.create(**s2240_iniexprisco_epi_dados)

    if 'infoExpRisco' in dir(evtExpRisco) and 'respReg' in dir(evtExpRisco.infoExpRisco):

        for respReg in evtExpRisco.infoExpRisco.respReg:

            s2240_iniexprisco_respreg_dados = {}
            s2240_iniexprisco_respreg_dados['s2240_evtexprisco_id'] = s2240_evtexprisco.id

            try:
                s2240_iniexprisco_respreg_dados['cpfresp'] = read_from_xml(respReg.cpfResp.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_respreg_dados['nisresp'] = read_from_xml(respReg.nisResp.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_respreg_dados['nmresp'] = read_from_xml(respReg.nmResp.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_respreg_dados['ideoc'] = read_from_xml(respReg.ideOC.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_respreg_dados['dscoc'] = read_from_xml(respReg.dscOC.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_respreg_dados['nroc'] = read_from_xml(respReg.nrOC.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_respreg_dados['ufoc'] = read_from_xml(respReg.ufOC.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2240_iniexprisco_respreg = s2240iniExpRiscorespReg.objects.create(**s2240_iniexprisco_respreg_dados)

    if 'infoExpRisco' in dir(evtExpRisco) and 'obs' in dir(evtExpRisco.infoExpRisco):

        for obs in evtExpRisco.infoExpRisco.obs:

            s2240_iniexprisco_obs_dados = {}
            s2240_iniexprisco_obs_dados['s2240_evtexprisco_id'] = s2240_evtexprisco.id

            try:
                s2240_iniexprisco_obs_dados['meterg'] = read_from_xml(obs.metErg.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_obs_dados['obscompl'] = read_from_xml(obs.obsCompl.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_obs_dados['observacao'] = read_from_xml(obs.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2240_iniexprisco_obs = s2240iniExpRiscoobs.objects.create(**s2240_iniexprisco_obs_dados)

    if 'infoExpRisco' in dir(evtExpRisco) and 'altExpRisco' in dir(evtExpRisco.infoExpRisco):

        for altExpRisco in evtExpRisco.infoExpRisco.altExpRisco:

            s2240_altexprisco_dados = {}
            s2240_altexprisco_dados['s2240_evtexprisco_id'] = s2240_evtexprisco.id

            try:
                s2240_altexprisco_dados['dtaltcondicao'] = read_from_xml(altExpRisco.dtAltCondicao.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            s2240_altexprisco = s2240altExpRisco.objects.create(**s2240_altexprisco_dados)

            if 'infoAmb' in dir(altExpRisco):

                for infoAmb in altExpRisco.infoAmb:

                    s2240_altexprisco_infoamb_dados = {}
                    s2240_altexprisco_infoamb_dados['s2240_altexprisco_id'] = s2240_altexprisco.id

                    try:
                        s2240_altexprisco_infoamb_dados['codamb'] = read_from_xml(infoAmb.codAmb.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2240_altexprisco_infoamb_dados['dscativdes'] = read_from_xml(infoAmb.infoAtiv.dscAtivDes.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2240_altexprisco_infoamb = s2240altExpRiscoinfoAmb.objects.create(**s2240_altexprisco_infoamb_dados)

                    if 'fatRisco' in dir(infoAmb):

                        for fatRisco in infoAmb.fatRisco:

                            s2240_altexprisco_fatrisco_dados = {}
                            s2240_altexprisco_fatrisco_dados['s2240_altexprisco_infoamb_id'] = s2240_altexprisco_infoamb.id
        
                            try:
                                s2240_altexprisco_fatrisco_dados['codfatris'] = read_from_xml(fatRisco.codFatRis.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2240_altexprisco_fatrisco_dados['intconc'] = read_from_xml(fatRisco.intConc.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2240_altexprisco_fatrisco_dados['tecmedicao'] = read_from_xml(fatRisco.tecMedicao.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2240_altexprisco_fatrisco_dados['utilizepc'] = read_from_xml(fatRisco.epcEpi.utilizEPC.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2240_altexprisco_fatrisco_dados['utilizepi'] = read_from_xml(fatRisco.epcEpi.utilizEPI.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass

                            s2240_altexprisco_fatrisco = s2240altExpRiscofatRisco.objects.create(**s2240_altexprisco_fatrisco_dados)
        
                            if 'epcEpi' in dir(fatRisco) and 'epc' in dir(fatRisco.epcEpi):
        
                                for epc in fatRisco.epcEpi.epc:
        
                                    s2240_altexprisco_epc_dados = {}
                                    s2240_altexprisco_epc_dados['s2240_altexprisco_fatrisco_id'] = s2240_altexprisco_fatrisco.id
                
                                    try:
                                        s2240_altexprisco_epc_dados['dscepc'] = read_from_xml(epc.dscEpc.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2240_altexprisco_epc_dados['eficepc'] = read_from_xml(epc.eficEpc.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
        
                                    s2240_altexprisco_epc = s2240altExpRiscoepc.objects.create(**s2240_altexprisco_epc_dados)
        
                            if 'epcEpi' in dir(fatRisco) and 'epi' in dir(fatRisco.epcEpi):
        
                                for epi in fatRisco.epcEpi.epi:
        
                                    s2240_altexprisco_epi_dados = {}
                                    s2240_altexprisco_epi_dados['s2240_altexprisco_fatrisco_id'] = s2240_altexprisco_fatrisco.id
                
                                    try:
                                        s2240_altexprisco_epi_dados['caepi'] = read_from_xml(epi.caEPI.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2240_altexprisco_epi_dados['eficepi'] = read_from_xml(epi.eficEpi.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2240_altexprisco_epi_dados['medprotecao'] = read_from_xml(epi.medProtecao.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2240_altexprisco_epi_dados['condfuncto'] = read_from_xml(epi.condFuncto.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2240_altexprisco_epi_dados['przvalid'] = read_from_xml(epi.przValid.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2240_altexprisco_epi_dados['periodictroca'] = read_from_xml(epi.periodicTroca.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2240_altexprisco_epi_dados['higienizacao'] = read_from_xml(epi.higienizacao.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
        
                                    s2240_altexprisco_epi = s2240altExpRiscoepi.objects.create(**s2240_altexprisco_epi_dados)

    if 'infoExpRisco' in dir(evtExpRisco) and 'fimExpRisco' in dir(evtExpRisco.infoExpRisco):

        for fimExpRisco in evtExpRisco.infoExpRisco.fimExpRisco:

            s2240_fimexprisco_dados = {}
            s2240_fimexprisco_dados['s2240_evtexprisco_id'] = s2240_evtexprisco.id

            try:
                s2240_fimexprisco_dados['dtfimcondicao'] = read_from_xml(fimExpRisco.dtFimCondicao.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            s2240_fimexprisco = s2240fimExpRisco.objects.create(**s2240_fimexprisco_dados)

            if 'infoAmb' in dir(fimExpRisco):

                for infoAmb in fimExpRisco.infoAmb:

                    s2240_fimexprisco_infoamb_dados = {}
                    s2240_fimexprisco_infoamb_dados['s2240_fimexprisco_id'] = s2240_fimexprisco.id

                    try:
                        s2240_fimexprisco_infoamb_dados['codamb'] = read_from_xml(infoAmb.codAmb.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2240_fimexprisco_infoamb = s2240fimExpRiscoinfoAmb.objects.create(**s2240_fimexprisco_infoamb_dados)

    if 'infoExpRisco' in dir(evtExpRisco) and 'respReg' in dir(evtExpRisco.infoExpRisco):

        for respReg in evtExpRisco.infoExpRisco.respReg:

            s2240_fimexprisco_respreg_dados = {}
            s2240_fimexprisco_respreg_dados['s2240_evtexprisco_id'] = s2240_evtexprisco.id

            try:
                s2240_fimexprisco_respreg_dados['dtini'] = read_from_xml(respReg.dtIni.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2240_fimexprisco_respreg_dados['dtfim'] = read_from_xml(respReg.dtFim.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2240_fimexprisco_respreg_dados['nisresp'] = read_from_xml(respReg.nisResp.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2240_fimexprisco_respreg_dados['nroc'] = read_from_xml(respReg.nrOc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2240_fimexprisco_respreg_dados['ufoc'] = read_from_xml(respReg.ufOC.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2240_fimexprisco_respreg = s2240fimExpRiscorespReg.objects.create(**s2240_fimexprisco_respreg_dados)
    s2240_evtexprisco_dados['evento'] = 's2240'
    s2240_evtexprisco_dados['id'] = s2240_evtexprisco.id
    s2240_evtexprisco_dados['identidade_evento'] = doc.eSocial.evtExpRisco['Id']

    from emensageriapro.esocial.views.s2240_evtexprisco_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2240_evtexprisco.id)

    return s2240_evtexprisco_dados