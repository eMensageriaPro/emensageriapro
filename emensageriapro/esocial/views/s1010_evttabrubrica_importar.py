#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1010.models import *
from emensageriapro.functions import read_from_xml



def read_s1010_evttabrubrica_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1010_evttabrubrica_obj(request, doc, status, validar)
    return dados



def read_s1010_evttabrubrica(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1010_evttabrubrica_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1010evtTabRubrica.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1010_evttabrubrica_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1010_evttabrubrica_dados = {}
    s1010_evttabrubrica_dados['status'] = status
    s1010_evttabrubrica_dados['arquivo_original'] = 1
    if arquivo:
        s1010_evttabrubrica_dados['arquivo'] = arquivo.arquivo
    s1010_evttabrubrica_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1010_evttabrubrica_dados['identidade'] = doc.eSocial.evtTabRubrica['Id']
    evtTabRubrica = doc.eSocial.evtTabRubrica

    if 'inclusao' in dir(evtTabRubrica.infoRubrica): s1010_evttabrubrica_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabRubrica.infoRubrica): s1010_evttabrubrica_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabRubrica.infoRubrica): s1010_evttabrubrica_dados['operacao'] = 3

    try:
        s1010_evttabrubrica_dados['tpamb'] = read_from_xml(evtTabRubrica.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1010_evttabrubrica_dados['procemi'] = read_from_xml(evtTabRubrica.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1010_evttabrubrica_dados['verproc'] = read_from_xml(evtTabRubrica.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1010_evttabrubrica_dados['tpinsc'] = read_from_xml(evtTabRubrica.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1010_evttabrubrica_dados['nrinsc'] = read_from_xml(evtTabRubrica.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1010_evttabrubrica = s1010evtTabRubrica.objects.create(**s1010_evttabrubrica_dados)

    if 'infoRubrica' in dir(evtTabRubrica) and 'inclusao' in dir(evtTabRubrica.infoRubrica):

        for inclusao in evtTabRubrica.infoRubrica.inclusao:

            s1010_inclusao_dados = {}
            s1010_inclusao_dados['s1010_evttabrubrica_id'] = s1010_evttabrubrica.id

            try:
                s1010_inclusao_dados['codrubr'] = read_from_xml(inclusao.ideRubrica.codRubr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['idetabrubr'] = read_from_xml(inclusao.ideRubrica.ideTabRubr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['inivalid'] = read_from_xml(inclusao.ideRubrica.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['fimvalid'] = read_from_xml(inclusao.ideRubrica.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['dscrubr'] = read_from_xml(inclusao.dadosRubrica.dscRubr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['natrubr'] = read_from_xml(inclusao.dadosRubrica.natRubr.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['tprubr'] = read_from_xml(inclusao.dadosRubrica.tpRubr.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['codinccp'] = read_from_xml(inclusao.dadosRubrica.codIncCP.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['codincirrf'] = read_from_xml(inclusao.dadosRubrica.codIncIRRF.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['codincfgts'] = read_from_xml(inclusao.dadosRubrica.codIncFGTS.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['codincsind'] = read_from_xml(inclusao.dadosRubrica.codIncSIND.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['codinccprp'] = read_from_xml(inclusao.dadosRubrica.codIncCPRP.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['tetoremun'] = read_from_xml(inclusao.dadosRubrica.tetoRemun.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['observacao'] = read_from_xml(inclusao.dadosRubrica.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1010_inclusao = s1010inclusao.objects.create(**s1010_inclusao_dados)

            if 'dadosRubrica' in dir(inclusao) and 'ideProcessoCP' in dir(inclusao.dadosRubrica):

                for ideProcessoCP in inclusao.dadosRubrica.ideProcessoCP:

                    s1010_inclusao_ideprocessocp_dados = {}
                    s1010_inclusao_ideprocessocp_dados['s1010_inclusao_id'] = s1010_inclusao.id

                    try:
                        s1010_inclusao_ideprocessocp_dados['tpproc'] = read_from_xml(ideProcessoCP.tpProc.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1010_inclusao_ideprocessocp_dados['nrproc'] = read_from_xml(ideProcessoCP.nrProc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1010_inclusao_ideprocessocp_dados['extdecisao'] = read_from_xml(ideProcessoCP.extDecisao.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1010_inclusao_ideprocessocp_dados['codsusp'] = read_from_xml(ideProcessoCP.codSusp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1010_inclusao_ideprocessocp = s1010inclusaoideProcessoCP.objects.create(**s1010_inclusao_ideprocessocp_dados)

            if 'dadosRubrica' in dir(inclusao) and 'ideProcessoIRRF' in dir(inclusao.dadosRubrica):

                for ideProcessoIRRF in inclusao.dadosRubrica.ideProcessoIRRF:

                    s1010_inclusao_ideprocessoirrf_dados = {}
                    s1010_inclusao_ideprocessoirrf_dados['s1010_inclusao_id'] = s1010_inclusao.id

                    try:
                        s1010_inclusao_ideprocessoirrf_dados['nrproc'] = read_from_xml(ideProcessoIRRF.nrProc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1010_inclusao_ideprocessoirrf_dados['codsusp'] = read_from_xml(ideProcessoIRRF.codSusp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1010_inclusao_ideprocessoirrf = s1010inclusaoideProcessoIRRF.objects.create(**s1010_inclusao_ideprocessoirrf_dados)

            if 'dadosRubrica' in dir(inclusao) and 'ideProcessoFGTS' in dir(inclusao.dadosRubrica):

                for ideProcessoFGTS in inclusao.dadosRubrica.ideProcessoFGTS:

                    s1010_inclusao_ideprocessofgts_dados = {}
                    s1010_inclusao_ideprocessofgts_dados['s1010_inclusao_id'] = s1010_inclusao.id

                    try:
                        s1010_inclusao_ideprocessofgts_dados['nrproc'] = read_from_xml(ideProcessoFGTS.nrProc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1010_inclusao_ideprocessofgts = s1010inclusaoideProcessoFGTS.objects.create(**s1010_inclusao_ideprocessofgts_dados)

            if 'dadosRubrica' in dir(inclusao) and 'ideProcessoSIND' in dir(inclusao.dadosRubrica):

                for ideProcessoSIND in inclusao.dadosRubrica.ideProcessoSIND:

                    s1010_inclusao_ideprocessosind_dados = {}
                    s1010_inclusao_ideprocessosind_dados['s1010_inclusao_id'] = s1010_inclusao.id

                    try:
                        s1010_inclusao_ideprocessosind_dados['nrproc'] = read_from_xml(ideProcessoSIND.nrProc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1010_inclusao_ideprocessosind = s1010inclusaoideProcessoSIND.objects.create(**s1010_inclusao_ideprocessosind_dados)

            if 'dadosRubrica' in dir(inclusao) and 'ideProcessoCPRP' in dir(inclusao.dadosRubrica):

                for ideProcessoCPRP in inclusao.dadosRubrica.ideProcessoCPRP:

                    s1010_inclusao_ideprocessocprp_dados = {}
                    s1010_inclusao_ideprocessocprp_dados['s1010_inclusao_id'] = s1010_inclusao.id

                    try:
                        s1010_inclusao_ideprocessocprp_dados['tpproc'] = read_from_xml(ideProcessoCPRP.tpProc.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1010_inclusao_ideprocessocprp_dados['nrproc'] = read_from_xml(ideProcessoCPRP.nrProc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1010_inclusao_ideprocessocprp_dados['extdecisao'] = read_from_xml(ideProcessoCPRP.extDecisao.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1010_inclusao_ideprocessocprp = s1010inclusaoideProcessoCPRP.objects.create(**s1010_inclusao_ideprocessocprp_dados)

    if 'infoRubrica' in dir(evtTabRubrica) and 'alteracao' in dir(evtTabRubrica.infoRubrica):

        for alteracao in evtTabRubrica.infoRubrica.alteracao:

            s1010_alteracao_dados = {}
            s1010_alteracao_dados['s1010_evttabrubrica_id'] = s1010_evttabrubrica.id

            try:
                s1010_alteracao_dados['codrubr'] = read_from_xml(alteracao.ideRubrica.codRubr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['idetabrubr'] = read_from_xml(alteracao.ideRubrica.ideTabRubr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['inivalid'] = read_from_xml(alteracao.ideRubrica.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['fimvalid'] = read_from_xml(alteracao.ideRubrica.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['dscrubr'] = read_from_xml(alteracao.dadosRubrica.dscRubr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['natrubr'] = read_from_xml(alteracao.dadosRubrica.natRubr.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['tprubr'] = read_from_xml(alteracao.dadosRubrica.tpRubr.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['codinccp'] = read_from_xml(alteracao.dadosRubrica.codIncCP.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['codincirrf'] = read_from_xml(alteracao.dadosRubrica.codIncIRRF.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['codincfgts'] = read_from_xml(alteracao.dadosRubrica.codIncFGTS.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['codincsind'] = read_from_xml(alteracao.dadosRubrica.codIncSIND.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['codinccprp'] = read_from_xml(alteracao.dadosRubrica.codIncCPRP.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['tetoremun'] = read_from_xml(alteracao.dadosRubrica.tetoRemun.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['observacao'] = read_from_xml(alteracao.dadosRubrica.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1010_alteracao = s1010alteracao.objects.create(**s1010_alteracao_dados)

            if 'dadosRubrica' in dir(alteracao) and 'ideProcessoCP' in dir(alteracao.dadosRubrica):

                for ideProcessoCP in alteracao.dadosRubrica.ideProcessoCP:

                    s1010_alteracao_ideprocessocp_dados = {}
                    s1010_alteracao_ideprocessocp_dados['s1010_alteracao_id'] = s1010_alteracao.id

                    try:
                        s1010_alteracao_ideprocessocp_dados['tpproc'] = read_from_xml(ideProcessoCP.tpProc.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1010_alteracao_ideprocessocp_dados['nrproc'] = read_from_xml(ideProcessoCP.nrProc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1010_alteracao_ideprocessocp_dados['extdecisao'] = read_from_xml(ideProcessoCP.extDecisao.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1010_alteracao_ideprocessocp_dados['codsusp'] = read_from_xml(ideProcessoCP.codSusp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1010_alteracao_ideprocessocp = s1010alteracaoideProcessoCP.objects.create(**s1010_alteracao_ideprocessocp_dados)

            if 'dadosRubrica' in dir(alteracao) and 'ideProcessoIRRF' in dir(alteracao.dadosRubrica):

                for ideProcessoIRRF in alteracao.dadosRubrica.ideProcessoIRRF:

                    s1010_alteracao_ideprocessoirrf_dados = {}
                    s1010_alteracao_ideprocessoirrf_dados['s1010_alteracao_id'] = s1010_alteracao.id

                    try:
                        s1010_alteracao_ideprocessoirrf_dados['nrproc'] = read_from_xml(ideProcessoIRRF.nrProc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1010_alteracao_ideprocessoirrf_dados['codsusp'] = read_from_xml(ideProcessoIRRF.codSusp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1010_alteracao_ideprocessoirrf = s1010alteracaoideProcessoIRRF.objects.create(**s1010_alteracao_ideprocessoirrf_dados)

            if 'dadosRubrica' in dir(alteracao) and 'ideProcessoFGTS' in dir(alteracao.dadosRubrica):

                for ideProcessoFGTS in alteracao.dadosRubrica.ideProcessoFGTS:

                    s1010_alteracao_ideprocessofgts_dados = {}
                    s1010_alteracao_ideprocessofgts_dados['s1010_alteracao_id'] = s1010_alteracao.id

                    try:
                        s1010_alteracao_ideprocessofgts_dados['nrproc'] = read_from_xml(ideProcessoFGTS.nrProc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1010_alteracao_ideprocessofgts = s1010alteracaoideProcessoFGTS.objects.create(**s1010_alteracao_ideprocessofgts_dados)

            if 'dadosRubrica' in dir(alteracao) and 'ideProcessoSIND' in dir(alteracao.dadosRubrica):

                for ideProcessoSIND in alteracao.dadosRubrica.ideProcessoSIND:

                    s1010_alteracao_ideprocessosind_dados = {}
                    s1010_alteracao_ideprocessosind_dados['s1010_alteracao_id'] = s1010_alteracao.id

                    try:
                        s1010_alteracao_ideprocessosind_dados['nrproc'] = read_from_xml(ideProcessoSIND.nrProc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1010_alteracao_ideprocessosind = s1010alteracaoideProcessoSIND.objects.create(**s1010_alteracao_ideprocessosind_dados)

            if 'dadosRubrica' in dir(alteracao) and 'ideProcessoCPRP' in dir(alteracao.dadosRubrica):

                for ideProcessoCPRP in alteracao.dadosRubrica.ideProcessoCPRP:

                    s1010_alteracao_ideprocessocprp_dados = {}
                    s1010_alteracao_ideprocessocprp_dados['s1010_alteracao_id'] = s1010_alteracao.id

                    try:
                        s1010_alteracao_ideprocessocprp_dados['tpproc'] = read_from_xml(ideProcessoCPRP.tpProc.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1010_alteracao_ideprocessocprp_dados['nrproc'] = read_from_xml(ideProcessoCPRP.nrProc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1010_alteracao_ideprocessocprp_dados['extdecisao'] = read_from_xml(ideProcessoCPRP.extDecisao.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1010_alteracao_ideprocessocprp = s1010alteracaoideProcessoCPRP.objects.create(**s1010_alteracao_ideprocessocprp_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    s1010_alteracao_novavalidade_dados = {}
                    s1010_alteracao_novavalidade_dados['s1010_alteracao_id'] = s1010_alteracao.id

                    try:
                        s1010_alteracao_novavalidade_dados['inivalid'] = read_from_xml(novaValidade.iniValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1010_alteracao_novavalidade_dados['fimvalid'] = read_from_xml(novaValidade.fimValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1010_alteracao_novavalidade = s1010alteracaonovaValidade.objects.create(**s1010_alteracao_novavalidade_dados)

    if 'infoRubrica' in dir(evtTabRubrica) and 'exclusao' in dir(evtTabRubrica.infoRubrica):

        for exclusao in evtTabRubrica.infoRubrica.exclusao:

            s1010_exclusao_dados = {}
            s1010_exclusao_dados['s1010_evttabrubrica_id'] = s1010_evttabrubrica.id

            try:
                s1010_exclusao_dados['codrubr'] = read_from_xml(exclusao.ideRubrica.codRubr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_exclusao_dados['idetabrubr'] = read_from_xml(exclusao.ideRubrica.ideTabRubr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_exclusao_dados['inivalid'] = read_from_xml(exclusao.ideRubrica.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1010_exclusao_dados['fimvalid'] = read_from_xml(exclusao.ideRubrica.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1010_exclusao = s1010exclusao.objects.create(**s1010_exclusao_dados)
    s1010_evttabrubrica_dados['evento'] = 's1010'
    s1010_evttabrubrica_dados['id'] = s1010_evttabrubrica.id
    s1010_evttabrubrica_dados['identidade_evento'] = doc.eSocial.evtTabRubrica['Id']

    from emensageriapro.esocial.views.s1010_evttabrubrica_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1010_evttabrubrica.id)

    return s1010_evttabrubrica_dados