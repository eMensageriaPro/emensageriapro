#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1040.models import *



def read_s1040_evttabfuncao_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1040_evttabfuncao_obj(request, doc, status, validar)
    return dados



def read_s1040_evttabfuncao(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1040_evttabfuncao_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1040evtTabFuncao.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1040_evttabfuncao_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1040_evttabfuncao_dados = {}
    s1040_evttabfuncao_dados['status'] = status
    s1040_evttabfuncao_dados['arquivo_original'] = 1
    if arquivo:
        s1040_evttabfuncao_dados['arquivo'] = arquivo.arquivo
    s1040_evttabfuncao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1040_evttabfuncao_dados['identidade'] = doc.eSocial.evtTabFuncao['Id']
    evtTabFuncao = doc.eSocial.evtTabFuncao

    if 'inclusao' in dir(evtTabFuncao.infoFuncao): s1040_evttabfuncao_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabFuncao.infoFuncao): s1040_evttabfuncao_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabFuncao.infoFuncao): s1040_evttabfuncao_dados['operacao'] = 3

    try:
        s1040_evttabfuncao_dados['tpamb'] = evtTabFuncao.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s1040_evttabfuncao_dados['procemi'] = evtTabFuncao.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s1040_evttabfuncao_dados['verproc'] = evtTabFuncao.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s1040_evttabfuncao_dados['tpinsc'] = evtTabFuncao.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s1040_evttabfuncao_dados['nrinsc'] = evtTabFuncao.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    s1040_evttabfuncao = s1040evtTabFuncao.objects.create(**s1040_evttabfuncao_dados)

    if 'infoFuncao' in dir(evtTabFuncao) and 'inclusao' in dir(evtTabFuncao.infoFuncao):

        for inclusao in evtTabFuncao.infoFuncao.inclusao:

            s1040_inclusao_dados = {}
            s1040_inclusao_dados['s1040_evttabfuncao_id'] = s1040_evttabfuncao.id

            try:
                s1040_inclusao_dados['codfuncao'] = inclusao.ideFuncao.codFuncao.cdata
            except AttributeError:
                pass

            try:
                s1040_inclusao_dados['inivalid'] = inclusao.ideFuncao.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1040_inclusao_dados['fimvalid'] = inclusao.ideFuncao.fimValid.cdata
            except AttributeError:
                pass

            try:
                s1040_inclusao_dados['dscfuncao'] = inclusao.dadosFuncao.dscFuncao.cdata
            except AttributeError:
                pass

            try:
                s1040_inclusao_dados['codcbo'] = inclusao.dadosFuncao.codCBO.cdata
            except AttributeError:
                pass

            s1040_inclusao = s1040inclusao.objects.create(**s1040_inclusao_dados)

    if 'infoFuncao' in dir(evtTabFuncao) and 'alteracao' in dir(evtTabFuncao.infoFuncao):

        for alteracao in evtTabFuncao.infoFuncao.alteracao:

            s1040_alteracao_dados = {}
            s1040_alteracao_dados['s1040_evttabfuncao_id'] = s1040_evttabfuncao.id

            try:
                s1040_alteracao_dados['codfuncao'] = alteracao.ideFuncao.codFuncao.cdata
            except AttributeError:
                pass

            try:
                s1040_alteracao_dados['inivalid'] = alteracao.ideFuncao.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1040_alteracao_dados['fimvalid'] = alteracao.ideFuncao.fimValid.cdata
            except AttributeError:
                pass

            try:
                s1040_alteracao_dados['dscfuncao'] = alteracao.dadosFuncao.dscFuncao.cdata
            except AttributeError:
                pass

            try:
                s1040_alteracao_dados['codcbo'] = alteracao.dadosFuncao.codCBO.cdata
            except AttributeError:
                pass

            s1040_alteracao = s1040alteracao.objects.create(**s1040_alteracao_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    s1040_alteracao_novavalidade_dados = {}
                    s1040_alteracao_novavalidade_dados['s1040_alteracao_id'] = s1040_alteracao.id

                    try:
                        s1040_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError:
                        pass

                    try:
                        s1040_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError:
                        pass

                    s1040_alteracao_novavalidade = s1040alteracaonovaValidade.objects.create(**s1040_alteracao_novavalidade_dados)

    if 'infoFuncao' in dir(evtTabFuncao) and 'exclusao' in dir(evtTabFuncao.infoFuncao):

        for exclusao in evtTabFuncao.infoFuncao.exclusao:

            s1040_exclusao_dados = {}
            s1040_exclusao_dados['s1040_evttabfuncao_id'] = s1040_evttabfuncao.id

            try:
                s1040_exclusao_dados['codfuncao'] = exclusao.ideFuncao.codFuncao.cdata
            except AttributeError:
                pass

            try:
                s1040_exclusao_dados['inivalid'] = exclusao.ideFuncao.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1040_exclusao_dados['fimvalid'] = exclusao.ideFuncao.fimValid.cdata
            except AttributeError:
                pass

            s1040_exclusao = s1040exclusao.objects.create(**s1040_exclusao_dados)
    s1040_evttabfuncao_dados['evento'] = 's1040'
    s1040_evttabfuncao_dados['id'] = s1040_evttabfuncao.id
    s1040_evttabfuncao_dados['identidade_evento'] = doc.eSocial.evtTabFuncao['Id']

    from emensageriapro.esocial.views.s1040_evttabfuncao_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1040_evttabfuncao.id)

    return s1040_evttabfuncao_dados