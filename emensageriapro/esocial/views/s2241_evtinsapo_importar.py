#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2241.models import *



def read_s2241_evtinsapo_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2241_evtinsapo_obj(request, doc, status, validar)
    return dados



def read_s2241_evtinsapo(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2241_evtinsapo_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2241evtInsApo.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2241_evtinsapo_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2241_evtinsapo_dados = {}
    s2241_evtinsapo_dados['status'] = status
    s2241_evtinsapo_dados['arquivo_original'] = 1
    if arquivo:
        s2241_evtinsapo_dados['arquivo'] = arquivo.arquivo
    s2241_evtinsapo_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2241_evtinsapo_dados['identidade'] = doc.eSocial.evtInsApo['Id']
    evtInsApo = doc.eSocial.evtInsApo

    try:
        s2241_evtinsapo_dados['indretif'] = evtInsApo.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        s2241_evtinsapo_dados['nrrecibo'] = evtInsApo.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        s2241_evtinsapo_dados['tpamb'] = evtInsApo.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s2241_evtinsapo_dados['procemi'] = evtInsApo.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s2241_evtinsapo_dados['verproc'] = evtInsApo.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s2241_evtinsapo_dados['tpinsc'] = evtInsApo.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s2241_evtinsapo_dados['nrinsc'] = evtInsApo.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    try:
        s2241_evtinsapo_dados['cpftrab'] = evtInsApo.ideVinculo.cpfTrab.cdata
    except AttributeError:
        pass

    try:
        s2241_evtinsapo_dados['nistrab'] = evtInsApo.ideVinculo.nisTrab.cdata
    except AttributeError:
        pass

    try:
        s2241_evtinsapo_dados['matricula'] = evtInsApo.ideVinculo.matricula.cdata
    except AttributeError:
        pass

    s2241_evtinsapo = s2241evtInsApo.objects.create(**s2241_evtinsapo_dados)

    if 'insalPeric' in dir(evtInsApo):

        for insalPeric in evtInsApo.insalPeric:

            s2241_insalperic_dados = {}
            s2241_insalperic_dados['s2241_evtinsapo_id'] = s2241_evtinsapo.id

            s2241_insalperic = s2241insalPeric.objects.create(**s2241_insalperic_dados)

            if 'iniInsalPeric' in dir(insalPeric):

                for iniInsalPeric in insalPeric.iniInsalPeric:

                    s2241_iniinsalperic_dados = {}
                    s2241_iniinsalperic_dados['s2241_insalperic_id'] = s2241_insalperic.id

                    try:
                        s2241_iniinsalperic_dados['dtinicondicao'] = iniInsalPeric.dtIniCondicao.cdata
                    except AttributeError:
                        pass

                    s2241_iniinsalperic = s2241iniInsalPeric.objects.create(**s2241_iniinsalperic_dados)

                    if 'infoAmb' in dir(iniInsalPeric):

                        for infoAmb in iniInsalPeric.infoAmb:

                            s2241_iniinsalperic_infoamb_dados = {}
                            s2241_iniinsalperic_infoamb_dados['s2241_iniinsalperic_id'] = s2241_iniinsalperic.id
        
                            try:
                                s2241_iniinsalperic_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
                            except AttributeError:
                                pass

                            s2241_iniinsalperic_infoamb = s2241iniInsalPericinfoAmb.objects.create(**s2241_iniinsalperic_infoamb_dados)
        
                            if 'fatRisco' in dir(infoAmb):
        
                                for fatRisco in infoAmb.fatRisco:
        
                                    s2241_iniinsalperic_fatrisco_dados = {}
                                    s2241_iniinsalperic_fatrisco_dados['s2241_iniinsalperic_infoamb_id'] = s2241_iniinsalperic_infoamb.id
                
                                    try:
                                        s2241_iniinsalperic_fatrisco_dados['codfatris'] = fatRisco.codFatRis.cdata
                                    except AttributeError:
                                        pass
        
                                    s2241_iniinsalperic_fatrisco = s2241iniInsalPericfatRisco.objects.create(**s2241_iniinsalperic_fatrisco_dados)

            if 'altInsalPeric' in dir(insalPeric):

                for altInsalPeric in insalPeric.altInsalPeric:

                    s2241_altinsalperic_dados = {}
                    s2241_altinsalperic_dados['s2241_insalperic_id'] = s2241_insalperic.id

                    try:
                        s2241_altinsalperic_dados['dtaltcondicao'] = altInsalPeric.dtAltCondicao.cdata
                    except AttributeError:
                        pass

                    s2241_altinsalperic = s2241altInsalPeric.objects.create(**s2241_altinsalperic_dados)

                    if 'infoamb' in dir(altInsalPeric):

                        for infoamb in altInsalPeric.infoamb:

                            s2241_altinsalperic_infoamb_dados = {}
                            s2241_altinsalperic_infoamb_dados['s2241_altinsalperic_id'] = s2241_altinsalperic.id
        
                            try:
                                s2241_altinsalperic_infoamb_dados['codamb'] = infoamb.codAmb.cdata
                            except AttributeError:
                                pass

                            s2241_altinsalperic_infoamb = s2241altInsalPericinfoamb.objects.create(**s2241_altinsalperic_infoamb_dados)
        
                            if 'fatRisco' in dir(infoamb):
        
                                for fatRisco in infoamb.fatRisco:
        
                                    s2241_altinsalperic_fatrisco_dados = {}
                                    s2241_altinsalperic_fatrisco_dados['s2241_altinsalperic_infoamb_id'] = s2241_altinsalperic_infoamb.id
                
                                    try:
                                        s2241_altinsalperic_fatrisco_dados['codfatris'] = fatRisco.codFatRis.cdata
                                    except AttributeError:
                                        pass
        
                                    s2241_altinsalperic_fatrisco = s2241altInsalPericfatRisco.objects.create(**s2241_altinsalperic_fatrisco_dados)

            if 'fimInsalPeric' in dir(insalPeric):

                for fimInsalPeric in insalPeric.fimInsalPeric:

                    s2241_fiminsalperic_dados = {}
                    s2241_fiminsalperic_dados['s2241_insalperic_id'] = s2241_insalperic.id

                    try:
                        s2241_fiminsalperic_dados['dtfimcondicao'] = fimInsalPeric.dtFimCondicao.cdata
                    except AttributeError:
                        pass

                    s2241_fiminsalperic = s2241fimInsalPeric.objects.create(**s2241_fiminsalperic_dados)

                    if 'infoAmb' in dir(fimInsalPeric):

                        for infoAmb in fimInsalPeric.infoAmb:

                            s2241_fiminsalperic_infoamb_dados = {}
                            s2241_fiminsalperic_infoamb_dados['s2241_fiminsalperic_id'] = s2241_fiminsalperic.id
        
                            try:
                                s2241_fiminsalperic_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
                            except AttributeError:
                                pass

                            s2241_fiminsalperic_infoamb = s2241fimInsalPericinfoAmb.objects.create(**s2241_fiminsalperic_infoamb_dados)

    if 'aposentEsp' in dir(evtInsApo):

        for aposentEsp in evtInsApo.aposentEsp:

            s2241_aposentesp_dados = {}
            s2241_aposentesp_dados['s2241_evtinsapo_id'] = s2241_evtinsapo.id

            s2241_aposentesp = s2241aposentEsp.objects.create(**s2241_aposentesp_dados)

            if 'iniAposentEsp' in dir(aposentEsp):

                for iniAposentEsp in aposentEsp.iniAposentEsp:

                    s2241_iniaposentesp_dados = {}
                    s2241_iniaposentesp_dados['s2241_aposentesp_id'] = s2241_aposentesp.id

                    try:
                        s2241_iniaposentesp_dados['dtinicondicao'] = iniAposentEsp.dtIniCondicao.cdata
                    except AttributeError:
                        pass

                    s2241_iniaposentesp = s2241iniAposentEsp.objects.create(**s2241_iniaposentesp_dados)

                    if 'infoAmb' in dir(iniAposentEsp):

                        for infoAmb in iniAposentEsp.infoAmb:

                            s2241_iniaposentesp_infoamb_dados = {}
                            s2241_iniaposentesp_infoamb_dados['s2241_iniaposentesp_id'] = s2241_iniaposentesp.id
        
                            try:
                                s2241_iniaposentesp_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
                            except AttributeError:
                                pass

                            s2241_iniaposentesp_infoamb = s2241iniAposentEspinfoAmb.objects.create(**s2241_iniaposentesp_infoamb_dados)
        
                            if 'fatRisco' in dir(infoAmb):
        
                                for fatRisco in infoAmb.fatRisco:
        
                                    s2241_iniaposentesp_fatrisco_dados = {}
                                    s2241_iniaposentesp_fatrisco_dados['s2241_iniaposentesp_infoamb_id'] = s2241_iniaposentesp_infoamb.id
                
                                    try:
                                        s2241_iniaposentesp_fatrisco_dados['codfatris'] = fatRisco.codFatRis.cdata
                                    except AttributeError:
                                        pass
        
                                    s2241_iniaposentesp_fatrisco = s2241iniAposentEspfatRisco.objects.create(**s2241_iniaposentesp_fatrisco_dados)

            if 'altAposentEsp' in dir(aposentEsp):

                for altAposentEsp in aposentEsp.altAposentEsp:

                    s2241_altaposentesp_dados = {}
                    s2241_altaposentesp_dados['s2241_aposentesp_id'] = s2241_aposentesp.id

                    try:
                        s2241_altaposentesp_dados['dtaltcondicao'] = altAposentEsp.dtAltCondicao.cdata
                    except AttributeError:
                        pass

                    s2241_altaposentesp = s2241altAposentEsp.objects.create(**s2241_altaposentesp_dados)

                    if 'infoamb' in dir(altAposentEsp):

                        for infoamb in altAposentEsp.infoamb:

                            s2241_altaposentesp_infoamb_dados = {}
                            s2241_altaposentesp_infoamb_dados['s2241_altaposentesp_id'] = s2241_altaposentesp.id
        
                            try:
                                s2241_altaposentesp_infoamb_dados['codamb'] = infoamb.codAmb.cdata
                            except AttributeError:
                                pass

                            s2241_altaposentesp_infoamb = s2241altAposentEspinfoamb.objects.create(**s2241_altaposentesp_infoamb_dados)
        
                            if 'fatRisco' in dir(infoamb):
        
                                for fatRisco in infoamb.fatRisco:
        
                                    s2241_altaposentesp_fatrisco_dados = {}
                                    s2241_altaposentesp_fatrisco_dados['s2241_altaposentesp_infoamb_id'] = s2241_altaposentesp_infoamb.id
                
                                    try:
                                        s2241_altaposentesp_fatrisco_dados['codfatris'] = fatRisco.codFatRis.cdata
                                    except AttributeError:
                                        pass
        
                                    s2241_altaposentesp_fatrisco = s2241altAposentEspfatRisco.objects.create(**s2241_altaposentesp_fatrisco_dados)

            if 'fimAposentEsp' in dir(aposentEsp):

                for fimAposentEsp in aposentEsp.fimAposentEsp:

                    s2241_fimaposentesp_dados = {}
                    s2241_fimaposentesp_dados['s2241_aposentesp_id'] = s2241_aposentesp.id

                    try:
                        s2241_fimaposentesp_dados['dtfimcondicao'] = fimAposentEsp.dtFimCondicao.cdata
                    except AttributeError:
                        pass

                    s2241_fimaposentesp = s2241fimAposentEsp.objects.create(**s2241_fimaposentesp_dados)

                    if 'infoAmb' in dir(fimAposentEsp):

                        for infoAmb in fimAposentEsp.infoAmb:

                            s2241_fimaposentesp_infoamb_dados = {}
                            s2241_fimaposentesp_infoamb_dados['s2241_fimaposentesp_id'] = s2241_fimaposentesp.id
        
                            try:
                                s2241_fimaposentesp_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
                            except AttributeError:
                                pass

                            s2241_fimaposentesp_infoamb = s2241fimAposentEspinfoAmb.objects.create(**s2241_fimaposentesp_infoamb_dados)
    s2241_evtinsapo_dados['evento'] = 's2241'
    s2241_evtinsapo_dados['id'] = s2241_evtinsapo.id
    s2241_evtinsapo_dados['identidade_evento'] = doc.eSocial.evtInsApo['Id']

    from emensageriapro.esocial.views.s2241_evtinsapo_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2241_evtinsapo.id)

    return s2241_evtinsapo_dados