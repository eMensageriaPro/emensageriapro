#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r1070.models import *
from emensageriapro.functions import read_from_xml



def read_r1070_evttabprocesso_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r1070_evttabprocesso_obj(request, doc, status, validar)
    return dados



def read_r1070_evttabprocesso(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r1070_evttabprocesso_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r1070evtTabProcesso.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r1070_evttabprocesso_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r1070_evttabprocesso_dados = {}
    r1070_evttabprocesso_dados['status'] = status
    r1070_evttabprocesso_dados['arquivo_original'] = 1
    if arquivo:
        r1070_evttabprocesso_dados['arquivo'] = arquivo.arquivo
    r1070_evttabprocesso_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r1070_evttabprocesso_dados['identidade'] = doc.Reinf.evtTabProcesso['id']
    evtTabProcesso = doc.Reinf.evtTabProcesso

    if 'inclusao' in dir(evtTabProcesso.infoProcesso): r1070_evttabprocesso_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabProcesso.infoProcesso): r1070_evttabprocesso_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabProcesso.infoProcesso): r1070_evttabprocesso_dados['operacao'] = 3

    try:
        r1070_evttabprocesso_dados['tpamb'] = read_from_xml(evtTabProcesso.ideEvento.tpAmb.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r1070_evttabprocesso_dados['procemi'] = read_from_xml(evtTabProcesso.ideEvento.procEmi.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r1070_evttabprocesso_dados['verproc'] = read_from_xml(evtTabProcesso.ideEvento.verProc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r1070_evttabprocesso_dados['tpinsc'] = read_from_xml(evtTabProcesso.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r1070_evttabprocesso_dados['nrinsc'] = read_from_xml(evtTabProcesso.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    r1070_evttabprocesso = r1070evtTabProcesso.objects.create(**r1070_evttabprocesso_dados)

    if 'infoProcesso' in dir(evtTabProcesso) and 'inclusao' in dir(evtTabProcesso.infoProcesso):

        for inclusao in evtTabProcesso.infoProcesso.inclusao:

            r1070_inclusao_dados = {}
            r1070_inclusao_dados['r1070_evttabprocesso_id'] = r1070_evttabprocesso.id

            try:
                r1070_inclusao_dados['tpproc'] = read_from_xml(inclusao.ideProcesso.tpProc.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r1070_inclusao_dados['nrproc'] = read_from_xml(inclusao.ideProcesso.nrProc.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1070_inclusao_dados['inivalid'] = read_from_xml(inclusao.ideProcesso.iniValid.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1070_inclusao_dados['fimvalid'] = read_from_xml(inclusao.ideProcesso.fimValid.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1070_inclusao_dados['indautoria'] = read_from_xml(inclusao.ideProcesso.indAutoria.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            r1070_inclusao = r1070inclusao.objects.create(**r1070_inclusao_dados)

            if 'ideProcesso' in dir(inclusao) and 'infoSusp' in dir(inclusao.ideProcesso):

                for infoSusp in inclusao.ideProcesso.infoSusp:

                    r1070_inclusao_infosusp_dados = {}
                    r1070_inclusao_infosusp_dados['r1070_inclusao_id'] = r1070_inclusao.id

                    try:
                        r1070_inclusao_infosusp_dados['codsusp'] = read_from_xml(infoSusp.codSusp.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r1070_inclusao_infosusp_dados['indsusp'] = read_from_xml(infoSusp.indSusp.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r1070_inclusao_infosusp_dados['dtdecisao'] = read_from_xml(infoSusp.dtDecisao.cdata, 'efdreinf', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        r1070_inclusao_infosusp_dados['inddeposito'] = read_from_xml(infoSusp.indDeposito.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    r1070_inclusao_infosusp = r1070inclusaoinfoSusp.objects.create(**r1070_inclusao_infosusp_dados)

            if 'ideProcesso' in dir(inclusao) and 'dadosProcJud' in dir(inclusao.ideProcesso):

                for dadosProcJud in inclusao.ideProcesso.dadosProcJud:

                    r1070_inclusao_dadosprocjud_dados = {}
                    r1070_inclusao_dadosprocjud_dados['r1070_inclusao_id'] = r1070_inclusao.id

                    try:
                        r1070_inclusao_dadosprocjud_dados['ufvara'] = read_from_xml(dadosProcJud.ufVara.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r1070_inclusao_dadosprocjud_dados['codmunic'] = read_from_xml(dadosProcJud.codMunic.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r1070_inclusao_dadosprocjud_dados['idvara'] = read_from_xml(dadosProcJud.idVara.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    r1070_inclusao_dadosprocjud = r1070inclusaodadosProcJud.objects.create(**r1070_inclusao_dadosprocjud_dados)

    if 'infoProcesso' in dir(evtTabProcesso) and 'alteracao' in dir(evtTabProcesso.infoProcesso):

        for alteracao in evtTabProcesso.infoProcesso.alteracao:

            r1070_alteracao_dados = {}
            r1070_alteracao_dados['r1070_evttabprocesso_id'] = r1070_evttabprocesso.id

            try:
                r1070_alteracao_dados['tpproc'] = read_from_xml(alteracao.ideProcesso.tpProc.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r1070_alteracao_dados['nrproc'] = read_from_xml(alteracao.ideProcesso.nrProc.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1070_alteracao_dados['inivalid'] = read_from_xml(alteracao.ideProcesso.iniValid.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1070_alteracao_dados['fimvalid'] = read_from_xml(alteracao.ideProcesso.fimValid.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1070_alteracao_dados['indautoria'] = read_from_xml(alteracao.ideProcesso.indAutoria.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            r1070_alteracao = r1070alteracao.objects.create(**r1070_alteracao_dados)

            if 'ideProcesso' in dir(alteracao) and 'infoSusp' in dir(alteracao.ideProcesso):

                for infoSusp in alteracao.ideProcesso.infoSusp:

                    r1070_alteracao_infosusp_dados = {}
                    r1070_alteracao_infosusp_dados['r1070_alteracao_id'] = r1070_alteracao.id

                    try:
                        r1070_alteracao_infosusp_dados['codsusp'] = read_from_xml(infoSusp.codSusp.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r1070_alteracao_infosusp_dados['indsusp'] = read_from_xml(infoSusp.indSusp.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r1070_alteracao_infosusp_dados['dtdecisao'] = read_from_xml(infoSusp.dtDecisao.cdata, 'efdreinf', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        r1070_alteracao_infosusp_dados['inddeposito'] = read_from_xml(infoSusp.indDeposito.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    r1070_alteracao_infosusp = r1070alteracaoinfoSusp.objects.create(**r1070_alteracao_infosusp_dados)

            if 'ideProcesso' in dir(alteracao) and 'dadosProcJud' in dir(alteracao.ideProcesso):

                for dadosProcJud in alteracao.ideProcesso.dadosProcJud:

                    r1070_alteracao_dadosprocjud_dados = {}
                    r1070_alteracao_dadosprocjud_dados['r1070_alteracao_id'] = r1070_alteracao.id

                    try:
                        r1070_alteracao_dadosprocjud_dados['ufvara'] = read_from_xml(dadosProcJud.ufVara.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r1070_alteracao_dadosprocjud_dados['codmunic'] = read_from_xml(dadosProcJud.codMunic.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r1070_alteracao_dadosprocjud_dados['idvara'] = read_from_xml(dadosProcJud.idVara.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    r1070_alteracao_dadosprocjud = r1070alteracaodadosProcJud.objects.create(**r1070_alteracao_dadosprocjud_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    r1070_alteracao_novavalidade_dados = {}
                    r1070_alteracao_novavalidade_dados['r1070_alteracao_id'] = r1070_alteracao.id

                    try:
                        r1070_alteracao_novavalidade_dados['inivalid'] = read_from_xml(novaValidade.iniValid.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r1070_alteracao_novavalidade_dados['fimvalid'] = read_from_xml(novaValidade.fimValid.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    r1070_alteracao_novavalidade = r1070alteracaonovaValidade.objects.create(**r1070_alteracao_novavalidade_dados)

    if 'infoProcesso' in dir(evtTabProcesso) and 'exclusao' in dir(evtTabProcesso.infoProcesso):

        for exclusao in evtTabProcesso.infoProcesso.exclusao:

            r1070_exclusao_dados = {}
            r1070_exclusao_dados['r1070_evttabprocesso_id'] = r1070_evttabprocesso.id

            try:
                r1070_exclusao_dados['tpproc'] = read_from_xml(exclusao.ideProcesso.tpProc.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r1070_exclusao_dados['nrproc'] = read_from_xml(exclusao.ideProcesso.nrProc.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1070_exclusao_dados['inivalid'] = read_from_xml(exclusao.ideProcesso.iniValid.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1070_exclusao_dados['fimvalid'] = read_from_xml(exclusao.ideProcesso.fimValid.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r1070_exclusao = r1070exclusao.objects.create(**r1070_exclusao_dados)
    r1070_evttabprocesso_dados['evento'] = 'r1070'
    r1070_evttabprocesso_dados['id'] = r1070_evttabprocesso.id
    r1070_evttabprocesso_dados['identidade_evento'] = doc.Reinf.evtTabProcesso['id']

    from emensageriapro.efdreinf.views.r1070_evttabprocesso_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r1070_evttabprocesso.id)

    return r1070_evttabprocesso_dados