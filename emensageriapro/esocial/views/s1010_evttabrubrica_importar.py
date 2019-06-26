#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1010.models import *



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

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_s1010_evttabrubrica_obj(request, doc, status, validar, arquivo)

    s1010evtTabRubrica.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s1010_evttabrubrica_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1010_evttabrubrica_dados = {}
    s1010_evttabrubrica_dados['status'] = status
    s1010_evttabrubrica_dados['arquivo_original'] = 1
    if arquivo:
        s1010_evttabrubrica_dados['arquivo'] = arquivo
    s1010_evttabrubrica_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1010_evttabrubrica_dados['identidade'] = doc.eSocial.evtTabRubrica['Id']
    evtTabRubrica = doc.eSocial.evtTabRubrica

    if 'inclusao' in dir(evtTabRubrica.infoRubrica): s1010_evttabrubrica_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabRubrica.infoRubrica): s1010_evttabrubrica_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabRubrica.infoRubrica): s1010_evttabrubrica_dados['operacao'] = 3

    try:
        s1010_evttabrubrica_dados['tpamb'] = evtTabRubrica.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s1010_evttabrubrica_dados['procemi'] = evtTabRubrica.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s1010_evttabrubrica_dados['verproc'] = evtTabRubrica.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s1010_evttabrubrica_dados['tpinsc'] = evtTabRubrica.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s1010_evttabrubrica_dados['nrinsc'] = evtTabRubrica.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    s1010_evttabrubrica = s1010evtTabRubrica.objects.create(**s1010_evttabrubrica_dados)

    if 'infoRubrica' in dir(evtTabRubrica) and 'inclusao' in dir(evtTabRubrica.infoRubrica):

        for inclusao in evtTabRubrica.infoRubrica.inclusao:

            s1010_inclusao_dados = {}
            s1010_inclusao_dados['s1010_evttabrubrica_id'] = s1010_evttabrubrica.id

            try:
                s1010_inclusao_dados['codrubr'] = inclusao.ideRubrica.codRubr.cdata
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['idetabrubr'] = inclusao.ideRubrica.ideTabRubr.cdata
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['inivalid'] = inclusao.ideRubrica.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['fimvalid'] = inclusao.ideRubrica.fimValid.cdata
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['dscrubr'] = inclusao.dadosRubrica.dscRubr.cdata
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['natrubr'] = inclusao.dadosRubrica.natRubr.cdata
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['tprubr'] = inclusao.dadosRubrica.tpRubr.cdata
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['codinccp'] = inclusao.dadosRubrica.codIncCP.cdata
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['codincirrf'] = inclusao.dadosRubrica.codIncIRRF.cdata
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['codincfgts'] = inclusao.dadosRubrica.codIncFGTS.cdata
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['codincsind'] = inclusao.dadosRubrica.codIncSIND.cdata
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['codinccprp'] = inclusao.dadosRubrica.codIncCPRP.cdata
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['tetoremun'] = inclusao.dadosRubrica.tetoRemun.cdata
            except AttributeError:
                pass

            try:
                s1010_inclusao_dados['observacao'] = inclusao.dadosRubrica.observacao.cdata
            except AttributeError:
                pass

            s1010_inclusao = s1010inclusao.objects.create(**s1010_inclusao_dados)

            if 'dadosRubrica' in dir(inclusao) and 'ideProcessoCP' in dir(inclusao.dadosRubrica):

                for ideProcessoCP in inclusao.dadosRubrica.ideProcessoCP:

                    s1010_inclusao_ideprocessocp_dados = {}
                    s1010_inclusao_ideprocessocp_dados['s1010_inclusao_id'] = s1010_inclusao.id

                    try:
                        s1010_inclusao_ideprocessocp_dados['tpproc'] = ideProcessoCP.tpProc.cdata
                    except AttributeError:
                        pass

                    try:
                        s1010_inclusao_ideprocessocp_dados['nrproc'] = ideProcessoCP.nrProc.cdata
                    except AttributeError:
                        pass

                    try:
                        s1010_inclusao_ideprocessocp_dados['extdecisao'] = ideProcessoCP.extDecisao.cdata
                    except AttributeError:
                        pass

                    try:
                        s1010_inclusao_ideprocessocp_dados['codsusp'] = ideProcessoCP.codSusp.cdata
                    except AttributeError:
                        pass

                    s1010_inclusao_ideprocessocp = s1010inclusaoideProcessoCP.objects.create(**s1010_inclusao_ideprocessocp_dados)

            if 'dadosRubrica' in dir(inclusao) and 'ideProcessoIRRF' in dir(inclusao.dadosRubrica):

                for ideProcessoIRRF in inclusao.dadosRubrica.ideProcessoIRRF:

                    s1010_inclusao_ideprocessoirrf_dados = {}
                    s1010_inclusao_ideprocessoirrf_dados['s1010_inclusao_id'] = s1010_inclusao.id

                    try:
                        s1010_inclusao_ideprocessoirrf_dados['nrproc'] = ideProcessoIRRF.nrProc.cdata
                    except AttributeError:
                        pass

                    try:
                        s1010_inclusao_ideprocessoirrf_dados['codsusp'] = ideProcessoIRRF.codSusp.cdata
                    except AttributeError:
                        pass

                    s1010_inclusao_ideprocessoirrf = s1010inclusaoideProcessoIRRF.objects.create(**s1010_inclusao_ideprocessoirrf_dados)

            if 'dadosRubrica' in dir(inclusao) and 'ideProcessoFGTS' in dir(inclusao.dadosRubrica):

                for ideProcessoFGTS in inclusao.dadosRubrica.ideProcessoFGTS:

                    s1010_inclusao_ideprocessofgts_dados = {}
                    s1010_inclusao_ideprocessofgts_dados['s1010_inclusao_id'] = s1010_inclusao.id

                    try:
                        s1010_inclusao_ideprocessofgts_dados['nrproc'] = ideProcessoFGTS.nrProc.cdata
                    except AttributeError:
                        pass

                    s1010_inclusao_ideprocessofgts = s1010inclusaoideProcessoFGTS.objects.create(**s1010_inclusao_ideprocessofgts_dados)

            if 'dadosRubrica' in dir(inclusao) and 'ideProcessoSIND' in dir(inclusao.dadosRubrica):

                for ideProcessoSIND in inclusao.dadosRubrica.ideProcessoSIND:

                    s1010_inclusao_ideprocessosind_dados = {}
                    s1010_inclusao_ideprocessosind_dados['s1010_inclusao_id'] = s1010_inclusao.id

                    try:
                        s1010_inclusao_ideprocessosind_dados['nrproc'] = ideProcessoSIND.nrProc.cdata
                    except AttributeError:
                        pass

                    s1010_inclusao_ideprocessosind = s1010inclusaoideProcessoSIND.objects.create(**s1010_inclusao_ideprocessosind_dados)

            if 'dadosRubrica' in dir(inclusao) and 'ideProcessoCPRP' in dir(inclusao.dadosRubrica):

                for ideProcessoCPRP in inclusao.dadosRubrica.ideProcessoCPRP:

                    s1010_inclusao_ideprocessocprp_dados = {}
                    s1010_inclusao_ideprocessocprp_dados['s1010_inclusao_id'] = s1010_inclusao.id

                    try:
                        s1010_inclusao_ideprocessocprp_dados['tpproc'] = ideProcessoCPRP.tpProc.cdata
                    except AttributeError:
                        pass

                    try:
                        s1010_inclusao_ideprocessocprp_dados['nrproc'] = ideProcessoCPRP.nrProc.cdata
                    except AttributeError:
                        pass

                    try:
                        s1010_inclusao_ideprocessocprp_dados['extdecisao'] = ideProcessoCPRP.extDecisao.cdata
                    except AttributeError:
                        pass

                    s1010_inclusao_ideprocessocprp = s1010inclusaoideProcessoCPRP.objects.create(**s1010_inclusao_ideprocessocprp_dados)

    if 'infoRubrica' in dir(evtTabRubrica) and 'alteracao' in dir(evtTabRubrica.infoRubrica):

        for alteracao in evtTabRubrica.infoRubrica.alteracao:

            s1010_alteracao_dados = {}
            s1010_alteracao_dados['s1010_evttabrubrica_id'] = s1010_evttabrubrica.id

            try:
                s1010_alteracao_dados['codrubr'] = alteracao.ideRubrica.codRubr.cdata
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['idetabrubr'] = alteracao.ideRubrica.ideTabRubr.cdata
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['inivalid'] = alteracao.ideRubrica.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['fimvalid'] = alteracao.ideRubrica.fimValid.cdata
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['dscrubr'] = alteracao.dadosRubrica.dscRubr.cdata
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['natrubr'] = alteracao.dadosRubrica.natRubr.cdata
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['tprubr'] = alteracao.dadosRubrica.tpRubr.cdata
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['codinccp'] = alteracao.dadosRubrica.codIncCP.cdata
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['codincirrf'] = alteracao.dadosRubrica.codIncIRRF.cdata
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['codincfgts'] = alteracao.dadosRubrica.codIncFGTS.cdata
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['codincsind'] = alteracao.dadosRubrica.codIncSIND.cdata
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['codinccprp'] = alteracao.dadosRubrica.codIncCPRP.cdata
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['tetoremun'] = alteracao.dadosRubrica.tetoRemun.cdata
            except AttributeError:
                pass

            try:
                s1010_alteracao_dados['observacao'] = alteracao.dadosRubrica.observacao.cdata
            except AttributeError:
                pass

            s1010_alteracao = s1010alteracao.objects.create(**s1010_alteracao_dados)

            if 'dadosRubrica' in dir(alteracao) and 'ideProcessoCP' in dir(alteracao.dadosRubrica):

                for ideProcessoCP in alteracao.dadosRubrica.ideProcessoCP:

                    s1010_alteracao_ideprocessocp_dados = {}
                    s1010_alteracao_ideprocessocp_dados['s1010_alteracao_id'] = s1010_alteracao.id

                    try:
                        s1010_alteracao_ideprocessocp_dados['tpproc'] = ideProcessoCP.tpProc.cdata
                    except AttributeError:
                        pass

                    try:
                        s1010_alteracao_ideprocessocp_dados['nrproc'] = ideProcessoCP.nrProc.cdata
                    except AttributeError:
                        pass

                    try:
                        s1010_alteracao_ideprocessocp_dados['extdecisao'] = ideProcessoCP.extDecisao.cdata
                    except AttributeError:
                        pass

                    try:
                        s1010_alteracao_ideprocessocp_dados['codsusp'] = ideProcessoCP.codSusp.cdata
                    except AttributeError:
                        pass

                    s1010_alteracao_ideprocessocp = s1010alteracaoideProcessoCP.objects.create(**s1010_alteracao_ideprocessocp_dados)

            if 'dadosRubrica' in dir(alteracao) and 'ideProcessoIRRF' in dir(alteracao.dadosRubrica):

                for ideProcessoIRRF in alteracao.dadosRubrica.ideProcessoIRRF:

                    s1010_alteracao_ideprocessoirrf_dados = {}
                    s1010_alteracao_ideprocessoirrf_dados['s1010_alteracao_id'] = s1010_alteracao.id

                    try:
                        s1010_alteracao_ideprocessoirrf_dados['nrproc'] = ideProcessoIRRF.nrProc.cdata
                    except AttributeError:
                        pass

                    try:
                        s1010_alteracao_ideprocessoirrf_dados['codsusp'] = ideProcessoIRRF.codSusp.cdata
                    except AttributeError:
                        pass

                    s1010_alteracao_ideprocessoirrf = s1010alteracaoideProcessoIRRF.objects.create(**s1010_alteracao_ideprocessoirrf_dados)

            if 'dadosRubrica' in dir(alteracao) and 'ideProcessoFGTS' in dir(alteracao.dadosRubrica):

                for ideProcessoFGTS in alteracao.dadosRubrica.ideProcessoFGTS:

                    s1010_alteracao_ideprocessofgts_dados = {}
                    s1010_alteracao_ideprocessofgts_dados['s1010_alteracao_id'] = s1010_alteracao.id

                    try:
                        s1010_alteracao_ideprocessofgts_dados['nrproc'] = ideProcessoFGTS.nrProc.cdata
                    except AttributeError:
                        pass

                    s1010_alteracao_ideprocessofgts = s1010alteracaoideProcessoFGTS.objects.create(**s1010_alteracao_ideprocessofgts_dados)

            if 'dadosRubrica' in dir(alteracao) and 'ideProcessoSIND' in dir(alteracao.dadosRubrica):

                for ideProcessoSIND in alteracao.dadosRubrica.ideProcessoSIND:

                    s1010_alteracao_ideprocessosind_dados = {}
                    s1010_alteracao_ideprocessosind_dados['s1010_alteracao_id'] = s1010_alteracao.id

                    try:
                        s1010_alteracao_ideprocessosind_dados['nrproc'] = ideProcessoSIND.nrProc.cdata
                    except AttributeError:
                        pass

                    s1010_alteracao_ideprocessosind = s1010alteracaoideProcessoSIND.objects.create(**s1010_alteracao_ideprocessosind_dados)

            if 'dadosRubrica' in dir(alteracao) and 'ideProcessoCPRP' in dir(alteracao.dadosRubrica):

                for ideProcessoCPRP in alteracao.dadosRubrica.ideProcessoCPRP:

                    s1010_alteracao_ideprocessocprp_dados = {}
                    s1010_alteracao_ideprocessocprp_dados['s1010_alteracao_id'] = s1010_alteracao.id

                    try:
                        s1010_alteracao_ideprocessocprp_dados['tpproc'] = ideProcessoCPRP.tpProc.cdata
                    except AttributeError:
                        pass

                    try:
                        s1010_alteracao_ideprocessocprp_dados['nrproc'] = ideProcessoCPRP.nrProc.cdata
                    except AttributeError:
                        pass

                    try:
                        s1010_alteracao_ideprocessocprp_dados['extdecisao'] = ideProcessoCPRP.extDecisao.cdata
                    except AttributeError:
                        pass

                    s1010_alteracao_ideprocessocprp = s1010alteracaoideProcessoCPRP.objects.create(**s1010_alteracao_ideprocessocprp_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    s1010_alteracao_novavalidade_dados = {}
                    s1010_alteracao_novavalidade_dados['s1010_alteracao_id'] = s1010_alteracao.id

                    try:
                        s1010_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError:
                        pass

                    try:
                        s1010_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError:
                        pass

                    s1010_alteracao_novavalidade = s1010alteracaonovaValidade.objects.create(**s1010_alteracao_novavalidade_dados)

    if 'infoRubrica' in dir(evtTabRubrica) and 'exclusao' in dir(evtTabRubrica.infoRubrica):

        for exclusao in evtTabRubrica.infoRubrica.exclusao:

            s1010_exclusao_dados = {}
            s1010_exclusao_dados['s1010_evttabrubrica_id'] = s1010_evttabrubrica.id

            try:
                s1010_exclusao_dados['codrubr'] = exclusao.ideRubrica.codRubr.cdata
            except AttributeError:
                pass

            try:
                s1010_exclusao_dados['idetabrubr'] = exclusao.ideRubrica.ideTabRubr.cdata
            except AttributeError:
                pass

            try:
                s1010_exclusao_dados['inivalid'] = exclusao.ideRubrica.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1010_exclusao_dados['fimvalid'] = exclusao.ideRubrica.fimValid.cdata
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