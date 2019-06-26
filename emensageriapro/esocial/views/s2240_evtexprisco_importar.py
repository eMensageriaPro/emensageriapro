#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2240.models import *



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

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_s2240_evtexprisco_obj(request, doc, status, validar, arquivo)

    s2240evtExpRisco.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s2240_evtexprisco_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2240_evtexprisco_dados = {}
    s2240_evtexprisco_dados['status'] = status
    s2240_evtexprisco_dados['arquivo_original'] = 1
    if arquivo:
        s2240_evtexprisco_dados['arquivo'] = arquivo
    s2240_evtexprisco_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2240_evtexprisco_dados['identidade'] = doc.eSocial.evtExpRisco['Id']
    evtExpRisco = doc.eSocial.evtExpRisco

    try:
        s2240_evtexprisco_dados['indretif'] = evtExpRisco.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['nrrecibo'] = evtExpRisco.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['tpamb'] = evtExpRisco.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['procemi'] = evtExpRisco.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['verproc'] = evtExpRisco.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['tpinsc'] = evtExpRisco.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['nrinsc'] = evtExpRisco.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['cpftrab'] = evtExpRisco.ideVinculo.cpfTrab.cdata
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['nistrab'] = evtExpRisco.ideVinculo.nisTrab.cdata
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['matricula'] = evtExpRisco.ideVinculo.matricula.cdata
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['codcateg'] = evtExpRisco.ideVinculo.codCateg.cdata
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['dtinicondicao'] = evtExpRisco.infoExpRisco.dtIniCondicao.cdata
    except AttributeError:
        pass

    try:
        s2240_evtexprisco_dados['dscativdes'] = evtExpRisco.infoExpRisco.infoAtiv.dscAtivDes.cdata
    except AttributeError:
        pass

    s2240_evtexprisco = s2240evtExpRisco.objects.create(**s2240_evtexprisco_dados)

    if 'infoExpRisco' in dir(evtExpRisco) and 'infoAmb' in dir(evtExpRisco.infoExpRisco):

        for infoAmb in evtExpRisco.infoExpRisco.infoAmb:

            s2240_iniexprisco_infoamb_dados = {}
            s2240_iniexprisco_infoamb_dados['s2240_evtexprisco_id'] = s2240_evtexprisco.id

            try:
                s2240_iniexprisco_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
            except AttributeError:
                pass

            s2240_iniexprisco_infoamb = s2240iniExpRiscoinfoAmb.objects.create(**s2240_iniexprisco_infoamb_dados)

    if 'infoExpRisco' in dir(evtExpRisco) and 'infoAtiv' in dir(evtExpRisco.infoExpRisco) and 'ativPericInsal' in dir(evtExpRisco.infoExpRisco.infoAtiv):

        for ativPericInsal in evtExpRisco.infoExpRisco.infoAtiv.ativPericInsal:

            s2240_iniexprisco_ativpericinsal_dados = {}
            s2240_iniexprisco_ativpericinsal_dados['s2240_evtexprisco_id'] = s2240_evtexprisco.id

            try:
                s2240_iniexprisco_ativpericinsal_dados['codativ'] = ativPericInsal.codAtiv.cdata
            except AttributeError:
                pass

            s2240_iniexprisco_ativpericinsal = s2240iniExpRiscoativPericInsal.objects.create(**s2240_iniexprisco_ativpericinsal_dados)

    if 'infoExpRisco' in dir(evtExpRisco) and 'fatRisco' in dir(evtExpRisco.infoExpRisco):

        for fatRisco in evtExpRisco.infoExpRisco.fatRisco:

            s2240_iniexprisco_fatrisco_dados = {}
            s2240_iniexprisco_fatrisco_dados['s2240_evtexprisco_id'] = s2240_evtexprisco.id

            try:
                s2240_iniexprisco_fatrisco_dados['codfatris'] = fatRisco.codFatRis.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['tpaval'] = fatRisco.tpAval.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['intconc'] = fatRisco.intConc.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['limtol'] = fatRisco.limTol.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['unmed'] = fatRisco.unMed.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['tecmedicao'] = fatRisco.tecMedicao.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['insalubridade'] = fatRisco.insalubridade.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['periculosidade'] = fatRisco.periculosidade.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['aposentesp'] = fatRisco.aposentEsp.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['dscfatrisc'] = fatRisco.dscFatRisc.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['utilizepc'] = fatRisco.epcEpi.utilizEPC.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['eficepc'] = fatRisco.epcEpi.eficEpc.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_fatrisco_dados['utilizepi'] = fatRisco.epcEpi.utilizEPI.cdata
            except AttributeError:
                pass

            s2240_iniexprisco_fatrisco = s2240iniExpRiscofatRisco.objects.create(**s2240_iniexprisco_fatrisco_dados)

            if 'epcEpi' in dir(fatRisco) and 'epc' in dir(fatRisco.epcEpi):

                for epc in fatRisco.epcEpi.epc:

                    s2240_iniexprisco_epc_dados = {}
                    s2240_iniexprisco_epc_dados['s2240_iniexprisco_fatrisco_id'] = s2240_iniexprisco_fatrisco.id

                    try:
                        s2240_iniexprisco_epc_dados['codep'] = epc.codEP.cdata
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epc_dados['dscepc'] = epc.dscEpc.cdata
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epc_dados['eficepc'] = epc.eficEpc.cdata
                    except AttributeError:
                        pass

                    s2240_iniexprisco_epc = s2240iniExpRiscoepc.objects.create(**s2240_iniexprisco_epc_dados)

            if 'epcEpi' in dir(fatRisco) and 'epi' in dir(fatRisco.epcEpi):

                for epi in fatRisco.epcEpi.epi:

                    s2240_iniexprisco_epi_dados = {}
                    s2240_iniexprisco_epi_dados['s2240_iniexprisco_fatrisco_id'] = s2240_iniexprisco_fatrisco.id

                    try:
                        s2240_iniexprisco_epi_dados['caepi'] = epi.caEPI.cdata
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epi_dados['dscepi'] = epi.dscEPI.cdata
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epi_dados['eficepi'] = epi.eficEpi.cdata
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epi_dados['medprotecao'] = epi.medProtecao.cdata
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epi_dados['condfuncto'] = epi.condFuncto.cdata
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epi_dados['usoinint'] = epi.usoInint.cdata
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epi_dados['przvalid'] = epi.przValid.cdata
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epi_dados['periodictroca'] = epi.periodicTroca.cdata
                    except AttributeError:
                        pass

                    try:
                        s2240_iniexprisco_epi_dados['higienizacao'] = epi.higienizacao.cdata
                    except AttributeError:
                        pass

                    s2240_iniexprisco_epi = s2240iniExpRiscoepi.objects.create(**s2240_iniexprisco_epi_dados)

    if 'infoExpRisco' in dir(evtExpRisco) and 'respReg' in dir(evtExpRisco.infoExpRisco):

        for respReg in evtExpRisco.infoExpRisco.respReg:

            s2240_iniexprisco_respreg_dados = {}
            s2240_iniexprisco_respreg_dados['s2240_evtexprisco_id'] = s2240_evtexprisco.id

            try:
                s2240_iniexprisco_respreg_dados['cpfresp'] = respReg.cpfResp.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_respreg_dados['nisresp'] = respReg.nisResp.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_respreg_dados['nmresp'] = respReg.nmResp.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_respreg_dados['ideoc'] = respReg.ideOC.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_respreg_dados['dscoc'] = respReg.dscOC.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_respreg_dados['nroc'] = respReg.nrOC.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_respreg_dados['ufoc'] = respReg.ufOC.cdata
            except AttributeError:
                pass

            s2240_iniexprisco_respreg = s2240iniExpRiscorespReg.objects.create(**s2240_iniexprisco_respreg_dados)

    if 'infoExpRisco' in dir(evtExpRisco) and 'obs' in dir(evtExpRisco.infoExpRisco):

        for obs in evtExpRisco.infoExpRisco.obs:

            s2240_iniexprisco_obs_dados = {}
            s2240_iniexprisco_obs_dados['s2240_evtexprisco_id'] = s2240_evtexprisco.id

            try:
                s2240_iniexprisco_obs_dados['meterg'] = obs.metErg.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_obs_dados['obscompl'] = obs.obsCompl.cdata
            except AttributeError:
                pass

            try:
                s2240_iniexprisco_obs_dados['observacao'] = obs.observacao.cdata
            except AttributeError:
                pass

            s2240_iniexprisco_obs = s2240iniExpRiscoobs.objects.create(**s2240_iniexprisco_obs_dados)

    if 'infoExpRisco' in dir(evtExpRisco) and 'altExpRisco' in dir(evtExpRisco.infoExpRisco):

        for altExpRisco in evtExpRisco.infoExpRisco.altExpRisco:

            s2240_altexprisco_dados = {}
            s2240_altexprisco_dados['s2240_evtexprisco_id'] = s2240_evtexprisco.id

            try:
                s2240_altexprisco_dados['dtaltcondicao'] = altExpRisco.dtAltCondicao.cdata
            except AttributeError:
                pass

            s2240_altexprisco = s2240altExpRisco.objects.create(**s2240_altexprisco_dados)

            if 'infoAmb' in dir(altExpRisco):

                for infoAmb in altExpRisco.infoAmb:

                    s2240_altexprisco_infoamb_dados = {}
                    s2240_altexprisco_infoamb_dados['s2240_altexprisco_id'] = s2240_altexprisco.id

                    try:
                        s2240_altexprisco_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
                    except AttributeError:
                        pass

                    try:
                        s2240_altexprisco_infoamb_dados['dscativdes'] = infoAmb.infoAtiv.dscAtivDes.cdata
                    except AttributeError:
                        pass

                    s2240_altexprisco_infoamb = s2240altExpRiscoinfoAmb.objects.create(**s2240_altexprisco_infoamb_dados)

                    if 'fatRisco' in dir(infoAmb):

                        for fatRisco in infoAmb.fatRisco:

                            s2240_altexprisco_fatrisco_dados = {}
                            s2240_altexprisco_fatrisco_dados['s2240_altexprisco_infoamb_id'] = s2240_altexprisco_infoamb.id
        
                            try:
                                s2240_altexprisco_fatrisco_dados['codfatris'] = fatRisco.codFatRis.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2240_altexprisco_fatrisco_dados['intconc'] = fatRisco.intConc.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2240_altexprisco_fatrisco_dados['tecmedicao'] = fatRisco.tecMedicao.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2240_altexprisco_fatrisco_dados['utilizepc'] = fatRisco.epcEpi.utilizEPC.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2240_altexprisco_fatrisco_dados['utilizepi'] = fatRisco.epcEpi.utilizEPI.cdata
                            except AttributeError:
                                pass

                            s2240_altexprisco_fatrisco = s2240altExpRiscofatRisco.objects.create(**s2240_altexprisco_fatrisco_dados)
        
                            if 'epcEpi' in dir(fatRisco) and 'epc' in dir(fatRisco.epcEpi):
        
                                for epc in fatRisco.epcEpi.epc:
        
                                    s2240_altexprisco_epc_dados = {}
                                    s2240_altexprisco_epc_dados['s2240_altexprisco_fatrisco_id'] = s2240_altexprisco_fatrisco.id
                
                                    try:
                                        s2240_altexprisco_epc_dados['dscepc'] = epc.dscEpc.cdata
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2240_altexprisco_epc_dados['eficepc'] = epc.eficEpc.cdata
                                    except AttributeError:
                                        pass
        
                                    s2240_altexprisco_epc = s2240altExpRiscoepc.objects.create(**s2240_altexprisco_epc_dados)
        
                            if 'epcEpi' in dir(fatRisco) and 'epi' in dir(fatRisco.epcEpi):
        
                                for epi in fatRisco.epcEpi.epi:
        
                                    s2240_altexprisco_epi_dados = {}
                                    s2240_altexprisco_epi_dados['s2240_altexprisco_fatrisco_id'] = s2240_altexprisco_fatrisco.id
                
                                    try:
                                        s2240_altexprisco_epi_dados['caepi'] = epi.caEPI.cdata
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2240_altexprisco_epi_dados['eficepi'] = epi.eficEpi.cdata
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2240_altexprisco_epi_dados['medprotecao'] = epi.medProtecao.cdata
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2240_altexprisco_epi_dados['condfuncto'] = epi.condFuncto.cdata
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2240_altexprisco_epi_dados['przvalid'] = epi.przValid.cdata
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2240_altexprisco_epi_dados['periodictroca'] = epi.periodicTroca.cdata
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s2240_altexprisco_epi_dados['higienizacao'] = epi.higienizacao.cdata
                                    except AttributeError:
                                        pass
        
                                    s2240_altexprisco_epi = s2240altExpRiscoepi.objects.create(**s2240_altexprisco_epi_dados)

    if 'infoExpRisco' in dir(evtExpRisco) and 'fimExpRisco' in dir(evtExpRisco.infoExpRisco):

        for fimExpRisco in evtExpRisco.infoExpRisco.fimExpRisco:

            s2240_fimexprisco_dados = {}
            s2240_fimexprisco_dados['s2240_evtexprisco_id'] = s2240_evtexprisco.id

            try:
                s2240_fimexprisco_dados['dtfimcondicao'] = fimExpRisco.dtFimCondicao.cdata
            except AttributeError:
                pass

            s2240_fimexprisco = s2240fimExpRisco.objects.create(**s2240_fimexprisco_dados)

            if 'infoAmb' in dir(fimExpRisco):

                for infoAmb in fimExpRisco.infoAmb:

                    s2240_fimexprisco_infoamb_dados = {}
                    s2240_fimexprisco_infoamb_dados['s2240_fimexprisco_id'] = s2240_fimexprisco.id

                    try:
                        s2240_fimexprisco_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
                    except AttributeError:
                        pass

                    s2240_fimexprisco_infoamb = s2240fimExpRiscoinfoAmb.objects.create(**s2240_fimexprisco_infoamb_dados)

    if 'infoExpRisco' in dir(evtExpRisco) and 'respReg' in dir(evtExpRisco.infoExpRisco):

        for respReg in evtExpRisco.infoExpRisco.respReg:

            s2240_fimexprisco_respreg_dados = {}
            s2240_fimexprisco_respreg_dados['s2240_evtexprisco_id'] = s2240_evtexprisco.id

            try:
                s2240_fimexprisco_respreg_dados['dtini'] = respReg.dtIni.cdata
            except AttributeError:
                pass

            try:
                s2240_fimexprisco_respreg_dados['dtfim'] = respReg.dtFim.cdata
            except AttributeError:
                pass

            try:
                s2240_fimexprisco_respreg_dados['nisresp'] = respReg.nisResp.cdata
            except AttributeError:
                pass

            try:
                s2240_fimexprisco_respreg_dados['nroc'] = respReg.nrOc.cdata
            except AttributeError:
                pass

            try:
                s2240_fimexprisco_respreg_dados['ufoc'] = respReg.ufOC.cdata
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