# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1070.models import *
from emensageriapro.functions import read_from_xml



def read_s1070_evttabprocesso_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1070_evttabprocesso_obj(request, doc, status, validar)
    return dados



def read_s1070_evttabprocesso(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1070_evttabprocesso_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1070evtTabProcesso.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1070_evttabprocesso_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1070_evttabprocesso_dados = {}
    s1070_evttabprocesso_dados['status'] = status
    s1070_evttabprocesso_dados['arquivo_original'] = 1
    if arquivo:
        s1070_evttabprocesso_dados['arquivo'] = arquivo.arquivo
    s1070_evttabprocesso_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1070_evttabprocesso_dados['identidade'] = doc.eSocial.evtTabProcesso['Id']
    evtTabProcesso = doc.eSocial.evtTabProcesso

    if 'inclusao' in dir(evtTabProcesso.infoProcesso): s1070_evttabprocesso_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabProcesso.infoProcesso): s1070_evttabprocesso_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabProcesso.infoProcesso): s1070_evttabprocesso_dados['operacao'] = 3

    try:
        s1070_evttabprocesso_dados['tpamb'] = read_from_xml(evtTabProcesso.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1070_evttabprocesso_dados['procemi'] = read_from_xml(evtTabProcesso.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1070_evttabprocesso_dados['verproc'] = read_from_xml(evtTabProcesso.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1070_evttabprocesso_dados['tpinsc'] = read_from_xml(evtTabProcesso.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1070_evttabprocesso_dados['nrinsc'] = read_from_xml(evtTabProcesso.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1070_evttabprocesso = s1070evtTabProcesso.objects.create(**s1070_evttabprocesso_dados)

    if 'infoProcesso' in dir(evtTabProcesso) and 'inclusao' in dir(evtTabProcesso.infoProcesso):

        for inclusao in evtTabProcesso.infoProcesso.inclusao:

            s1070_inclusao_dados = {}
            s1070_inclusao_dados['s1070_evttabprocesso_id'] = s1070_evttabprocesso.id

            try:
                s1070_inclusao_dados['tpproc'] = read_from_xml(inclusao.ideProcesso.tpProc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1070_inclusao_dados['nrproc'] = read_from_xml(inclusao.ideProcesso.nrProc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1070_inclusao_dados['inivalid'] = read_from_xml(inclusao.ideProcesso.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1070_inclusao_dados['fimvalid'] = read_from_xml(inclusao.ideProcesso.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1070_inclusao_dados['indautoria'] = read_from_xml(inclusao.dadosProc.indAutoria.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1070_inclusao_dados['indmatproc'] = read_from_xml(inclusao.dadosProc.indMatProc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1070_inclusao_dados['observacao'] = read_from_xml(inclusao.dadosProc.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1070_inclusao = s1070inclusao.objects.create(**s1070_inclusao_dados)

            if 'dadosProc' in dir(inclusao) and 'dadosProcJud' in dir(inclusao.dadosProc):

                for dadosProcJud in inclusao.dadosProc.dadosProcJud:

                    s1070_inclusao_dadosprocjud_dados = {}
                    s1070_inclusao_dadosprocjud_dados['s1070_inclusao_id'] = s1070_inclusao.id

                    try:
                        s1070_inclusao_dadosprocjud_dados['ufvara'] = read_from_xml(dadosProcJud.ufVara.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1070_inclusao_dadosprocjud_dados['codmunic'] = read_from_xml(dadosProcJud.codMunic.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1070_inclusao_dadosprocjud_dados['idvara'] = read_from_xml(dadosProcJud.idVara.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1070_inclusao_dadosprocjud = s1070inclusaodadosProcJud.objects.create(**s1070_inclusao_dadosprocjud_dados)

            if 'dadosProc' in dir(inclusao) and 'infoSusp' in dir(inclusao.dadosProc):

                for infoSusp in inclusao.dadosProc.infoSusp:

                    s1070_inclusao_infosusp_dados = {}
                    s1070_inclusao_infosusp_dados['s1070_inclusao_id'] = s1070_inclusao.id

                    try:
                        s1070_inclusao_infosusp_dados['codsusp'] = read_from_xml(infoSusp.codSusp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1070_inclusao_infosusp_dados['indsusp'] = read_from_xml(infoSusp.indSusp.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1070_inclusao_infosusp_dados['dtdecisao'] = read_from_xml(infoSusp.dtDecisao.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s1070_inclusao_infosusp_dados['inddeposito'] = read_from_xml(infoSusp.indDeposito.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1070_inclusao_infosusp = s1070inclusaoinfoSusp.objects.create(**s1070_inclusao_infosusp_dados)

    if 'infoProcesso' in dir(evtTabProcesso) and 'alteracao' in dir(evtTabProcesso.infoProcesso):

        for alteracao in evtTabProcesso.infoProcesso.alteracao:

            s1070_alteracao_dados = {}
            s1070_alteracao_dados['s1070_evttabprocesso_id'] = s1070_evttabprocesso.id

            try:
                s1070_alteracao_dados['tpproc'] = read_from_xml(alteracao.ideProcesso.tpProc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1070_alteracao_dados['nrproc'] = read_from_xml(alteracao.ideProcesso.nrProc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1070_alteracao_dados['inivalid'] = read_from_xml(alteracao.ideProcesso.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1070_alteracao_dados['fimvalid'] = read_from_xml(alteracao.ideProcesso.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1070_alteracao_dados['indautoria'] = read_from_xml(alteracao.dadosProc.indAutoria.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1070_alteracao_dados['indmatproc'] = read_from_xml(alteracao.dadosProc.indMatProc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1070_alteracao_dados['observacao'] = read_from_xml(alteracao.dadosProc.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1070_alteracao = s1070alteracao.objects.create(**s1070_alteracao_dados)

            if 'dadosProc' in dir(alteracao) and 'dadosProcJud' in dir(alteracao.dadosProc):

                for dadosProcJud in alteracao.dadosProc.dadosProcJud:

                    s1070_alteracao_dadosprocjud_dados = {}
                    s1070_alteracao_dadosprocjud_dados['s1070_alteracao_id'] = s1070_alteracao.id

                    try:
                        s1070_alteracao_dadosprocjud_dados['ufvara'] = read_from_xml(dadosProcJud.ufVara.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1070_alteracao_dadosprocjud_dados['codmunic'] = read_from_xml(dadosProcJud.codMunic.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1070_alteracao_dadosprocjud_dados['idvara'] = read_from_xml(dadosProcJud.idVara.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1070_alteracao_dadosprocjud = s1070alteracaodadosProcJud.objects.create(**s1070_alteracao_dadosprocjud_dados)

            if 'dadosProc' in dir(alteracao) and 'infoSusp' in dir(alteracao.dadosProc):

                for infoSusp in alteracao.dadosProc.infoSusp:

                    s1070_alteracao_infosusp_dados = {}
                    s1070_alteracao_infosusp_dados['s1070_alteracao_id'] = s1070_alteracao.id

                    try:
                        s1070_alteracao_infosusp_dados['codsusp'] = read_from_xml(infoSusp.codSusp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1070_alteracao_infosusp_dados['indsusp'] = read_from_xml(infoSusp.indSusp.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1070_alteracao_infosusp_dados['dtdecisao'] = read_from_xml(infoSusp.dtDecisao.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s1070_alteracao_infosusp_dados['inddeposito'] = read_from_xml(infoSusp.indDeposito.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1070_alteracao_infosusp = s1070alteracaoinfoSusp.objects.create(**s1070_alteracao_infosusp_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    s1070_alteracao_novavalidade_dados = {}
                    s1070_alteracao_novavalidade_dados['s1070_alteracao_id'] = s1070_alteracao.id

                    try:
                        s1070_alteracao_novavalidade_dados['inivalid'] = read_from_xml(novaValidade.iniValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1070_alteracao_novavalidade_dados['fimvalid'] = read_from_xml(novaValidade.fimValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1070_alteracao_novavalidade = s1070alteracaonovaValidade.objects.create(**s1070_alteracao_novavalidade_dados)

    if 'infoProcesso' in dir(evtTabProcesso) and 'exclusao' in dir(evtTabProcesso.infoProcesso):

        for exclusao in evtTabProcesso.infoProcesso.exclusao:

            s1070_exclusao_dados = {}
            s1070_exclusao_dados['s1070_evttabprocesso_id'] = s1070_evttabprocesso.id

            try:
                s1070_exclusao_dados['tpproc'] = read_from_xml(exclusao.ideProcesso.tpProc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1070_exclusao_dados['nrproc'] = read_from_xml(exclusao.ideProcesso.nrProc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1070_exclusao_dados['inivalid'] = read_from_xml(exclusao.ideProcesso.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1070_exclusao_dados['fimvalid'] = read_from_xml(exclusao.ideProcesso.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1070_exclusao = s1070exclusao.objects.create(**s1070_exclusao_dados)
    s1070_evttabprocesso_dados['evento'] = 's1070'
    s1070_evttabprocesso_dados['id'] = s1070_evttabprocesso.id
    s1070_evttabprocesso_dados['identidade_evento'] = doc.eSocial.evtTabProcesso['Id']

    from emensageriapro.esocial.views.s1070_evttabprocesso_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1070_evttabprocesso.id)

    return s1070_evttabprocesso_dados