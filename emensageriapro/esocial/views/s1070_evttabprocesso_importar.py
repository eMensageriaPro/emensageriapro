#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1070.models import *



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

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_s1070_evttabprocesso_obj(request, doc, status, validar, arquivo)
    novo_arquivo = arquivo.replace('/aguardando/', '/processado/')
    s1070evtTabProcesso.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s1070_evttabprocesso_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1070_evttabprocesso_dados = {}
    s1070_evttabprocesso_dados['status'] = status
    s1070_evttabprocesso_dados['arquivo_original'] = 1
    if arquivo:
        s1070_evttabprocesso_dados['arquivo'] = arquivo
    s1070_evttabprocesso_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1070_evttabprocesso_dados['identidade'] = doc.eSocial.evtTabProcesso['Id']
    evtTabProcesso = doc.eSocial.evtTabProcesso

    if 'inclusao' in dir(evtTabProcesso.infoProcesso): s1070_evttabprocesso_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabProcesso.infoProcesso): s1070_evttabprocesso_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabProcesso.infoProcesso): s1070_evttabprocesso_dados['operacao'] = 3

    try:
        s1070_evttabprocesso_dados['tpamb'] = evtTabProcesso.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s1070_evttabprocesso_dados['procemi'] = evtTabProcesso.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s1070_evttabprocesso_dados['verproc'] = evtTabProcesso.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s1070_evttabprocesso_dados['tpinsc'] = evtTabProcesso.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s1070_evttabprocesso_dados['nrinsc'] = evtTabProcesso.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    s1070_evttabprocesso = s1070evtTabProcesso.objects.create(**s1070_evttabprocesso_dados)

    if 'infoProcesso' in dir(evtTabProcesso) and 'inclusao' in dir(evtTabProcesso.infoProcesso):

        for inclusao in evtTabProcesso.infoProcesso.inclusao:

            s1070_inclusao_dados = {}
            s1070_inclusao_dados['s1070_evttabprocesso_id'] = s1070_evttabprocesso.id

            try:
                s1070_inclusao_dados['tpproc'] = inclusao.ideProcesso.tpProc.cdata
            except AttributeError:
                pass

            try:
                s1070_inclusao_dados['nrproc'] = inclusao.ideProcesso.nrProc.cdata
            except AttributeError:
                pass

            try:
                s1070_inclusao_dados['inivalid'] = inclusao.ideProcesso.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1070_inclusao_dados['fimvalid'] = inclusao.ideProcesso.fimValid.cdata
            except AttributeError:
                pass

            try:
                s1070_inclusao_dados['indautoria'] = inclusao.dadosProc.indAutoria.cdata
            except AttributeError:
                pass

            try:
                s1070_inclusao_dados['indmatproc'] = inclusao.dadosProc.indMatProc.cdata
            except AttributeError:
                pass

            try:
                s1070_inclusao_dados['observacao'] = inclusao.dadosProc.observacao.cdata
            except AttributeError:
                pass

            s1070_inclusao = s1070inclusao.objects.create(**s1070_inclusao_dados)

            if 'dadosProc' in dir(inclusao) and 'dadosProcJud' in dir(inclusao.dadosProc):

                for dadosProcJud in inclusao.dadosProc.dadosProcJud:

                    s1070_inclusao_dadosprocjud_dados = {}
                    s1070_inclusao_dadosprocjud_dados['s1070_inclusao_id'] = s1070_inclusao.id

                    try:
                        s1070_inclusao_dadosprocjud_dados['ufvara'] = dadosProcJud.ufVara.cdata
                    except AttributeError:
                        pass

                    try:
                        s1070_inclusao_dadosprocjud_dados['codmunic'] = dadosProcJud.codMunic.cdata
                    except AttributeError:
                        pass

                    try:
                        s1070_inclusao_dadosprocjud_dados['idvara'] = dadosProcJud.idVara.cdata
                    except AttributeError:
                        pass

                    s1070_inclusao_dadosprocjud = s1070inclusaodadosProcJud.objects.create(**s1070_inclusao_dadosprocjud_dados)

            if 'dadosProc' in dir(inclusao) and 'infoSusp' in dir(inclusao.dadosProc):

                for infoSusp in inclusao.dadosProc.infoSusp:

                    s1070_inclusao_infosusp_dados = {}
                    s1070_inclusao_infosusp_dados['s1070_inclusao_id'] = s1070_inclusao.id

                    try:
                        s1070_inclusao_infosusp_dados['codsusp'] = infoSusp.codSusp.cdata
                    except AttributeError:
                        pass

                    try:
                        s1070_inclusao_infosusp_dados['indsusp'] = infoSusp.indSusp.cdata
                    except AttributeError:
                        pass

                    try:
                        s1070_inclusao_infosusp_dados['dtdecisao'] = infoSusp.dtDecisao.cdata
                    except AttributeError:
                        pass

                    try:
                        s1070_inclusao_infosusp_dados['inddeposito'] = infoSusp.indDeposito.cdata
                    except AttributeError:
                        pass

                    s1070_inclusao_infosusp = s1070inclusaoinfoSusp.objects.create(**s1070_inclusao_infosusp_dados)

    if 'infoProcesso' in dir(evtTabProcesso) and 'alteracao' in dir(evtTabProcesso.infoProcesso):

        for alteracao in evtTabProcesso.infoProcesso.alteracao:

            s1070_alteracao_dados = {}
            s1070_alteracao_dados['s1070_evttabprocesso_id'] = s1070_evttabprocesso.id

            try:
                s1070_alteracao_dados['tpproc'] = alteracao.ideProcesso.tpProc.cdata
            except AttributeError:
                pass

            try:
                s1070_alteracao_dados['nrproc'] = alteracao.ideProcesso.nrProc.cdata
            except AttributeError:
                pass

            try:
                s1070_alteracao_dados['inivalid'] = alteracao.ideProcesso.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1070_alteracao_dados['fimvalid'] = alteracao.ideProcesso.fimValid.cdata
            except AttributeError:
                pass

            try:
                s1070_alteracao_dados['indautoria'] = alteracao.dadosProc.indAutoria.cdata
            except AttributeError:
                pass

            try:
                s1070_alteracao_dados['indmatproc'] = alteracao.dadosProc.indMatProc.cdata
            except AttributeError:
                pass

            try:
                s1070_alteracao_dados['observacao'] = alteracao.dadosProc.observacao.cdata
            except AttributeError:
                pass

            s1070_alteracao = s1070alteracao.objects.create(**s1070_alteracao_dados)

            if 'dadosProc' in dir(alteracao) and 'dadosProcJud' in dir(alteracao.dadosProc):

                for dadosProcJud in alteracao.dadosProc.dadosProcJud:

                    s1070_alteracao_dadosprocjud_dados = {}
                    s1070_alteracao_dadosprocjud_dados['s1070_alteracao_id'] = s1070_alteracao.id

                    try:
                        s1070_alteracao_dadosprocjud_dados['ufvara'] = dadosProcJud.ufVara.cdata
                    except AttributeError:
                        pass

                    try:
                        s1070_alteracao_dadosprocjud_dados['codmunic'] = dadosProcJud.codMunic.cdata
                    except AttributeError:
                        pass

                    try:
                        s1070_alteracao_dadosprocjud_dados['idvara'] = dadosProcJud.idVara.cdata
                    except AttributeError:
                        pass

                    s1070_alteracao_dadosprocjud = s1070alteracaodadosProcJud.objects.create(**s1070_alteracao_dadosprocjud_dados)

            if 'dadosProc' in dir(alteracao) and 'infoSusp' in dir(alteracao.dadosProc):

                for infoSusp in alteracao.dadosProc.infoSusp:

                    s1070_alteracao_infosusp_dados = {}
                    s1070_alteracao_infosusp_dados['s1070_alteracao_id'] = s1070_alteracao.id

                    try:
                        s1070_alteracao_infosusp_dados['codsusp'] = infoSusp.codSusp.cdata
                    except AttributeError:
                        pass

                    try:
                        s1070_alteracao_infosusp_dados['indsusp'] = infoSusp.indSusp.cdata
                    except AttributeError:
                        pass

                    try:
                        s1070_alteracao_infosusp_dados['dtdecisao'] = infoSusp.dtDecisao.cdata
                    except AttributeError:
                        pass

                    try:
                        s1070_alteracao_infosusp_dados['inddeposito'] = infoSusp.indDeposito.cdata
                    except AttributeError:
                        pass

                    s1070_alteracao_infosusp = s1070alteracaoinfoSusp.objects.create(**s1070_alteracao_infosusp_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    s1070_alteracao_novavalidade_dados = {}
                    s1070_alteracao_novavalidade_dados['s1070_alteracao_id'] = s1070_alteracao.id

                    try:
                        s1070_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError:
                        pass

                    try:
                        s1070_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError:
                        pass

                    s1070_alteracao_novavalidade = s1070alteracaonovaValidade.objects.create(**s1070_alteracao_novavalidade_dados)

    if 'infoProcesso' in dir(evtTabProcesso) and 'exclusao' in dir(evtTabProcesso.infoProcesso):

        for exclusao in evtTabProcesso.infoProcesso.exclusao:

            s1070_exclusao_dados = {}
            s1070_exclusao_dados['s1070_evttabprocesso_id'] = s1070_evttabprocesso.id

            try:
                s1070_exclusao_dados['tpproc'] = exclusao.ideProcesso.tpProc.cdata
            except AttributeError:
                pass

            try:
                s1070_exclusao_dados['nrproc'] = exclusao.ideProcesso.nrProc.cdata
            except AttributeError:
                pass

            try:
                s1070_exclusao_dados['inivalid'] = exclusao.ideProcesso.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1070_exclusao_dados['fimvalid'] = exclusao.ideProcesso.fimValid.cdata
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