# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1005.models import *
from emensageriapro.functions import read_from_xml



def read_s1005_evttabestab_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1005_evttabestab_obj(request, doc, status, validar)
    return dados



def read_s1005_evttabestab(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1005_evttabestab_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1005evtTabEstab.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1005_evttabestab_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1005_evttabestab_dados = {}
    s1005_evttabestab_dados['status'] = status
    s1005_evttabestab_dados['arquivo_original'] = 1
    if arquivo:
        s1005_evttabestab_dados['arquivo'] = arquivo.arquivo
    s1005_evttabestab_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1005_evttabestab_dados['identidade'] = doc.eSocial.evtTabEstab['Id']
    evtTabEstab = doc.eSocial.evtTabEstab

    if 'inclusao' in dir(evtTabEstab.infoEstab): s1005_evttabestab_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabEstab.infoEstab): s1005_evttabestab_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabEstab.infoEstab): s1005_evttabestab_dados['operacao'] = 3

    try:
        s1005_evttabestab_dados['tpamb'] = read_from_xml(evtTabEstab.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1005_evttabestab_dados['procemi'] = read_from_xml(evtTabEstab.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1005_evttabestab_dados['verproc'] = read_from_xml(evtTabEstab.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1005_evttabestab_dados['tpinsc'] = read_from_xml(evtTabEstab.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1005_evttabestab_dados['nrinsc'] = read_from_xml(evtTabEstab.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1005_evttabestab = s1005evtTabEstab.objects.create(**s1005_evttabestab_dados)

    if 'infoEstab' in dir(evtTabEstab) and 'inclusao' in dir(evtTabEstab.infoEstab):

        for inclusao in evtTabEstab.infoEstab.inclusao:

            s1005_inclusao_dados = {}
            s1005_inclusao_dados['s1005_evttabestab_id'] = s1005_evttabestab.id

            try:
                s1005_inclusao_dados['tpinsc'] = read_from_xml(inclusao.ideEstab.tpInsc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1005_inclusao_dados['nrinsc'] = read_from_xml(inclusao.ideEstab.nrInsc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1005_inclusao_dados['inivalid'] = read_from_xml(inclusao.ideEstab.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1005_inclusao_dados['fimvalid'] = read_from_xml(inclusao.ideEstab.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1005_inclusao_dados['cnaeprep'] = read_from_xml(inclusao.dadosEstab.cnaePrep.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1005_inclusao_dados['aliqrat'] = read_from_xml(inclusao.dadosEstab.aliqGilrat.aliqRat.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1005_inclusao_dados['fap'] = read_from_xml(inclusao.dadosEstab.aliqGilrat.fap.cdata, 'esocial', 'N', 4)
            except AttributeError:
                pass

            try:
                s1005_inclusao_dados['aliqratajust'] = read_from_xml(inclusao.dadosEstab.aliqGilrat.aliqRatAjust.cdata, 'esocial', 'N', 4)
            except AttributeError:
                pass

            try:
                s1005_inclusao_dados['regpt'] = read_from_xml(inclusao.dadosEstab.infoTrab.regPt.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1005_inclusao_dados['contapr'] = read_from_xml(inclusao.dadosEstab.infoTrab.infoApr.contApr.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1005_inclusao_dados['nrprocjud'] = read_from_xml(inclusao.dadosEstab.infoTrab.infoApr.nrProcJud.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1005_inclusao_dados['contented'] = read_from_xml(inclusao.dadosEstab.infoTrab.infoApr.contEntEd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1005_inclusao = s1005inclusao.objects.create(**s1005_inclusao_dados)

            if 'dadosEstab' in dir(inclusao) and 'aliqGilrat' in dir(inclusao.dadosEstab) and 'procAdmJudRat' in dir(inclusao.dadosEstab.aliqGilrat):

                for procAdmJudRat in inclusao.dadosEstab.aliqGilrat.procAdmJudRat:

                    s1005_inclusao_procadmjudrat_dados = {}
                    s1005_inclusao_procadmjudrat_dados['s1005_inclusao_id'] = s1005_inclusao.id

                    try:
                        s1005_inclusao_procadmjudrat_dados['tpproc'] = read_from_xml(procAdmJudRat.tpProc.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1005_inclusao_procadmjudrat_dados['nrproc'] = read_from_xml(procAdmJudRat.nrProc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1005_inclusao_procadmjudrat_dados['codsusp'] = read_from_xml(procAdmJudRat.codSusp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1005_inclusao_procadmjudrat = s1005inclusaoprocAdmJudRat.objects.create(**s1005_inclusao_procadmjudrat_dados)

            if 'dadosEstab' in dir(inclusao) and 'aliqGilrat' in dir(inclusao.dadosEstab) and 'procAdmJudFap' in dir(inclusao.dadosEstab.aliqGilrat):

                for procAdmJudFap in inclusao.dadosEstab.aliqGilrat.procAdmJudFap:

                    s1005_inclusao_procadmjudfap_dados = {}
                    s1005_inclusao_procadmjudfap_dados['s1005_inclusao_id'] = s1005_inclusao.id

                    try:
                        s1005_inclusao_procadmjudfap_dados['tpproc'] = read_from_xml(procAdmJudFap.tpProc.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1005_inclusao_procadmjudfap_dados['nrproc'] = read_from_xml(procAdmJudFap.nrProc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1005_inclusao_procadmjudfap_dados['codsusp'] = read_from_xml(procAdmJudFap.codSusp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1005_inclusao_procadmjudfap = s1005inclusaoprocAdmJudFap.objects.create(**s1005_inclusao_procadmjudfap_dados)

            if 'dadosEstab' in dir(inclusao) and 'infoCaepf' in dir(inclusao.dadosEstab):

                for infoCaepf in inclusao.dadosEstab.infoCaepf:

                    s1005_inclusao_infocaepf_dados = {}
                    s1005_inclusao_infocaepf_dados['s1005_inclusao_id'] = s1005_inclusao.id

                    try:
                        s1005_inclusao_infocaepf_dados['tpcaepf'] = read_from_xml(infoCaepf.tpCaepf.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1005_inclusao_infocaepf = s1005inclusaoinfoCaepf.objects.create(**s1005_inclusao_infocaepf_dados)

            if 'dadosEstab' in dir(inclusao) and 'infoObra' in dir(inclusao.dadosEstab):

                for infoObra in inclusao.dadosEstab.infoObra:

                    s1005_inclusao_infoobra_dados = {}
                    s1005_inclusao_infoobra_dados['s1005_inclusao_id'] = s1005_inclusao.id

                    try:
                        s1005_inclusao_infoobra_dados['indsubstpatrobra'] = read_from_xml(infoObra.indSubstPatrObra.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1005_inclusao_infoobra = s1005inclusaoinfoObra.objects.create(**s1005_inclusao_infoobra_dados)

            if 'dadosEstab' in dir(inclusao) and 'infoTrab' in dir(inclusao.dadosEstab) and 'infoApr' in dir(inclusao.dadosEstab.infoTrab) and 'infoEntEduc' in dir(inclusao.dadosEstab.infoTrab.infoApr):

                for infoEntEduc in inclusao.dadosEstab.infoTrab.infoApr.infoEntEduc:

                    s1005_inclusao_infoenteduc_dados = {}
                    s1005_inclusao_infoenteduc_dados['s1005_inclusao_id'] = s1005_inclusao.id

                    try:
                        s1005_inclusao_infoenteduc_dados['nrinsc'] = read_from_xml(infoEntEduc.nrInsc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1005_inclusao_infoenteduc = s1005inclusaoinfoEntEduc.objects.create(**s1005_inclusao_infoenteduc_dados)

            if 'dadosEstab' in dir(inclusao) and 'infoTrab' in dir(inclusao.dadosEstab) and 'infoPCD' in dir(inclusao.dadosEstab.infoTrab):

                for infoPCD in inclusao.dadosEstab.infoTrab.infoPCD:

                    s1005_inclusao_infopcd_dados = {}
                    s1005_inclusao_infopcd_dados['s1005_inclusao_id'] = s1005_inclusao.id

                    try:
                        s1005_inclusao_infopcd_dados['contpcd'] = read_from_xml(infoPCD.contPCD.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1005_inclusao_infopcd_dados['nrprocjud'] = read_from_xml(infoPCD.nrProcJud.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1005_inclusao_infopcd = s1005inclusaoinfoPCD.objects.create(**s1005_inclusao_infopcd_dados)

    if 'infoEstab' in dir(evtTabEstab) and 'alteracao' in dir(evtTabEstab.infoEstab):

        for alteracao in evtTabEstab.infoEstab.alteracao:

            s1005_alteracao_dados = {}
            s1005_alteracao_dados['s1005_evttabestab_id'] = s1005_evttabestab.id

            try:
                s1005_alteracao_dados['tpinsc'] = read_from_xml(alteracao.ideEstab.tpInsc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1005_alteracao_dados['nrinsc'] = read_from_xml(alteracao.ideEstab.nrInsc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1005_alteracao_dados['inivalid'] = read_from_xml(alteracao.ideEstab.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1005_alteracao_dados['fimvalid'] = read_from_xml(alteracao.ideEstab.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1005_alteracao_dados['cnaeprep'] = read_from_xml(alteracao.dadosEstab.cnaePrep.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1005_alteracao_dados['aliqrat'] = read_from_xml(alteracao.dadosEstab.aliqGilrat.aliqRat.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1005_alteracao_dados['fap'] = read_from_xml(alteracao.dadosEstab.aliqGilrat.fap.cdata, 'esocial', 'N', 4)
            except AttributeError:
                pass

            try:
                s1005_alteracao_dados['aliqratajust'] = read_from_xml(alteracao.dadosEstab.aliqGilrat.aliqRatAjust.cdata, 'esocial', 'N', 4)
            except AttributeError:
                pass

            try:
                s1005_alteracao_dados['regpt'] = read_from_xml(alteracao.dadosEstab.infoTrab.regPt.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1005_alteracao_dados['contapr'] = read_from_xml(alteracao.dadosEstab.infoTrab.infoApr.contApr.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1005_alteracao_dados['nrprocjud'] = read_from_xml(alteracao.dadosEstab.infoTrab.infoApr.nrProcJud.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1005_alteracao_dados['contented'] = read_from_xml(alteracao.dadosEstab.infoTrab.infoApr.contEntEd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1005_alteracao = s1005alteracao.objects.create(**s1005_alteracao_dados)

            if 'dadosEstab' in dir(alteracao) and 'aliqGilrat' in dir(alteracao.dadosEstab) and 'procAdmJudRat' in dir(alteracao.dadosEstab.aliqGilrat):

                for procAdmJudRat in alteracao.dadosEstab.aliqGilrat.procAdmJudRat:

                    s1005_alteracao_procadmjudrat_dados = {}
                    s1005_alteracao_procadmjudrat_dados['s1005_alteracao_id'] = s1005_alteracao.id

                    try:
                        s1005_alteracao_procadmjudrat_dados['tpproc'] = read_from_xml(procAdmJudRat.tpProc.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1005_alteracao_procadmjudrat_dados['nrproc'] = read_from_xml(procAdmJudRat.nrProc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1005_alteracao_procadmjudrat_dados['codsusp'] = read_from_xml(procAdmJudRat.codSusp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1005_alteracao_procadmjudrat = s1005alteracaoprocAdmJudRat.objects.create(**s1005_alteracao_procadmjudrat_dados)

            if 'dadosEstab' in dir(alteracao) and 'aliqGilrat' in dir(alteracao.dadosEstab) and 'procAdmJudFap' in dir(alteracao.dadosEstab.aliqGilrat):

                for procAdmJudFap in alteracao.dadosEstab.aliqGilrat.procAdmJudFap:

                    s1005_alteracao_procadmjudfap_dados = {}
                    s1005_alteracao_procadmjudfap_dados['s1005_alteracao_id'] = s1005_alteracao.id

                    try:
                        s1005_alteracao_procadmjudfap_dados['tpproc'] = read_from_xml(procAdmJudFap.tpProc.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1005_alteracao_procadmjudfap_dados['nrproc'] = read_from_xml(procAdmJudFap.nrProc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1005_alteracao_procadmjudfap_dados['codsusp'] = read_from_xml(procAdmJudFap.codSusp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1005_alteracao_procadmjudfap = s1005alteracaoprocAdmJudFap.objects.create(**s1005_alteracao_procadmjudfap_dados)

            if 'dadosEstab' in dir(alteracao) and 'infoCaepf' in dir(alteracao.dadosEstab):

                for infoCaepf in alteracao.dadosEstab.infoCaepf:

                    s1005_alteracao_infocaepf_dados = {}
                    s1005_alteracao_infocaepf_dados['s1005_alteracao_id'] = s1005_alteracao.id

                    try:
                        s1005_alteracao_infocaepf_dados['tpcaepf'] = read_from_xml(infoCaepf.tpCaepf.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1005_alteracao_infocaepf = s1005alteracaoinfoCaepf.objects.create(**s1005_alteracao_infocaepf_dados)

            if 'dadosEstab' in dir(alteracao) and 'infoObra' in dir(alteracao.dadosEstab):

                for infoObra in alteracao.dadosEstab.infoObra:

                    s1005_alteracao_infoobra_dados = {}
                    s1005_alteracao_infoobra_dados['s1005_alteracao_id'] = s1005_alteracao.id

                    try:
                        s1005_alteracao_infoobra_dados['indsubstpatrobra'] = read_from_xml(infoObra.indSubstPatrObra.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1005_alteracao_infoobra = s1005alteracaoinfoObra.objects.create(**s1005_alteracao_infoobra_dados)

            if 'dadosEstab' in dir(alteracao) and 'infoTrab' in dir(alteracao.dadosEstab) and 'infoApr' in dir(alteracao.dadosEstab.infoTrab) and 'infoEntEduc' in dir(alteracao.dadosEstab.infoTrab.infoApr):

                for infoEntEduc in alteracao.dadosEstab.infoTrab.infoApr.infoEntEduc:

                    s1005_alteracao_infoenteduc_dados = {}
                    s1005_alteracao_infoenteduc_dados['s1005_alteracao_id'] = s1005_alteracao.id

                    try:
                        s1005_alteracao_infoenteduc_dados['nrinsc'] = read_from_xml(infoEntEduc.nrInsc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1005_alteracao_infoenteduc = s1005alteracaoinfoEntEduc.objects.create(**s1005_alteracao_infoenteduc_dados)

            if 'dadosEstab' in dir(alteracao) and 'infoTrab' in dir(alteracao.dadosEstab) and 'infoPCD' in dir(alteracao.dadosEstab.infoTrab):

                for infoPCD in alteracao.dadosEstab.infoTrab.infoPCD:

                    s1005_alteracao_infopcd_dados = {}
                    s1005_alteracao_infopcd_dados['s1005_alteracao_id'] = s1005_alteracao.id

                    try:
                        s1005_alteracao_infopcd_dados['contpcd'] = read_from_xml(infoPCD.contPCD.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1005_alteracao_infopcd_dados['nrprocjud'] = read_from_xml(infoPCD.nrProcJud.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1005_alteracao_infopcd = s1005alteracaoinfoPCD.objects.create(**s1005_alteracao_infopcd_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    s1005_alteracao_novavalidade_dados = {}
                    s1005_alteracao_novavalidade_dados['s1005_alteracao_id'] = s1005_alteracao.id

                    try:
                        s1005_alteracao_novavalidade_dados['inivalid'] = read_from_xml(novaValidade.iniValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1005_alteracao_novavalidade_dados['fimvalid'] = read_from_xml(novaValidade.fimValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1005_alteracao_novavalidade = s1005alteracaonovaValidade.objects.create(**s1005_alteracao_novavalidade_dados)

    if 'infoEstab' in dir(evtTabEstab) and 'exclusao' in dir(evtTabEstab.infoEstab):

        for exclusao in evtTabEstab.infoEstab.exclusao:

            s1005_exclusao_dados = {}
            s1005_exclusao_dados['s1005_evttabestab_id'] = s1005_evttabestab.id

            try:
                s1005_exclusao_dados['tpinsc'] = read_from_xml(exclusao.ideEstab.tpInsc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1005_exclusao_dados['nrinsc'] = read_from_xml(exclusao.ideEstab.nrInsc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1005_exclusao_dados['inivalid'] = read_from_xml(exclusao.ideEstab.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1005_exclusao_dados['fimvalid'] = read_from_xml(exclusao.ideEstab.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1005_exclusao = s1005exclusao.objects.create(**s1005_exclusao_dados)
    s1005_evttabestab_dados['evento'] = 's1005'
    s1005_evttabestab_dados['id'] = s1005_evttabestab.id
    s1005_evttabestab_dados['identidade_evento'] = doc.eSocial.evtTabEstab['Id']

    from emensageriapro.esocial.views.s1005_evttabestab_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1005_evttabestab.id)

    return s1005_evttabestab_dados