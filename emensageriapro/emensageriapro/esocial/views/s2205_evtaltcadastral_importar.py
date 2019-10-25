#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2205.models import *
from emensageriapro.functions import read_from_xml



def read_s2205_evtaltcadastral_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2205_evtaltcadastral_obj(request, doc, status, validar)
    return dados



def read_s2205_evtaltcadastral(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2205_evtaltcadastral_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2205evtAltCadastral.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2205_evtaltcadastral_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2205_evtaltcadastral_dados = {}
    s2205_evtaltcadastral_dados['status'] = status
    s2205_evtaltcadastral_dados['arquivo_original'] = 1
    if arquivo:
        s2205_evtaltcadastral_dados['arquivo'] = arquivo.arquivo
    s2205_evtaltcadastral_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2205_evtaltcadastral_dados['identidade'] = doc.eSocial.evtAltCadastral['Id']
    evtAltCadastral = doc.eSocial.evtAltCadastral

    try:
        s2205_evtaltcadastral_dados['indretif'] = read_from_xml(evtAltCadastral.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['nrrecibo'] = read_from_xml(evtAltCadastral.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['tpamb'] = read_from_xml(evtAltCadastral.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['procemi'] = read_from_xml(evtAltCadastral.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['verproc'] = read_from_xml(evtAltCadastral.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['tpinsc'] = read_from_xml(evtAltCadastral.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['nrinsc'] = read_from_xml(evtAltCadastral.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['cpftrab'] = read_from_xml(evtAltCadastral.ideTrabalhador.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['dtalteracao'] = read_from_xml(evtAltCadastral.alteracao.dtAlteracao.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['nistrab'] = read_from_xml(evtAltCadastral.alteracao.dadosTrabalhador.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['nmtrab'] = read_from_xml(evtAltCadastral.alteracao.dadosTrabalhador.nmTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['sexo'] = read_from_xml(evtAltCadastral.alteracao.dadosTrabalhador.sexo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['racacor'] = read_from_xml(evtAltCadastral.alteracao.dadosTrabalhador.racaCor.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['estciv'] = read_from_xml(evtAltCadastral.alteracao.dadosTrabalhador.estCiv.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['grauinstr'] = read_from_xml(evtAltCadastral.alteracao.dadosTrabalhador.grauInstr.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['nmsoc'] = read_from_xml(evtAltCadastral.alteracao.dadosTrabalhador.nmSoc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['dtnascto'] = read_from_xml(evtAltCadastral.alteracao.dadosTrabalhador.nascimento.dtNascto.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['codmunic'] = read_from_xml(evtAltCadastral.alteracao.dadosTrabalhador.nascimento.codMunic.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['uf'] = read_from_xml(evtAltCadastral.alteracao.dadosTrabalhador.nascimento.uf.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['paisnascto'] = read_from_xml(evtAltCadastral.alteracao.dadosTrabalhador.nascimento.paisNascto.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['paisnac'] = read_from_xml(evtAltCadastral.alteracao.dadosTrabalhador.nascimento.paisNac.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['nmmae'] = read_from_xml(evtAltCadastral.alteracao.dadosTrabalhador.nascimento.nmMae.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2205_evtaltcadastral_dados['nmpai'] = read_from_xml(evtAltCadastral.alteracao.dadosTrabalhador.nascimento.nmPai.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s2205_evtaltcadastral = s2205evtAltCadastral.objects.create(**s2205_evtaltcadastral_dados)

    if 'alteracao' in dir(evtAltCadastral) and 'dadosTrabalhador' in dir(evtAltCadastral.alteracao) and 'documentos' in dir(evtAltCadastral.alteracao.dadosTrabalhador):

        for documentos in evtAltCadastral.alteracao.dadosTrabalhador.documentos:

            s2205_documentos_dados = {}
            s2205_documentos_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral.id

            s2205_documentos = s2205documentos.objects.create(**s2205_documentos_dados)

            if 'CTPS' in dir(documentos):

                for CTPS in documentos.CTPS:

                    s2205_ctps_dados = {}
                    s2205_ctps_dados['s2205_documentos_id'] = s2205_documentos.id

                    try:
                        s2205_ctps_dados['nrctps'] = read_from_xml(CTPS.nrCtps.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2205_ctps_dados['seriectps'] = read_from_xml(CTPS.serieCtps.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2205_ctps_dados['ufctps'] = read_from_xml(CTPS.ufCtps.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2205_ctps = s2205CTPS.objects.create(**s2205_ctps_dados)

            if 'RIC' in dir(documentos):

                for RIC in documentos.RIC:

                    s2205_ric_dados = {}
                    s2205_ric_dados['s2205_documentos_id'] = s2205_documentos.id

                    try:
                        s2205_ric_dados['nrric'] = read_from_xml(RIC.nrRic.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2205_ric_dados['orgaoemissor'] = read_from_xml(RIC.orgaoEmissor.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2205_ric_dados['dtexped'] = read_from_xml(RIC.dtExped.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    s2205_ric = s2205RIC.objects.create(**s2205_ric_dados)

            if 'RG' in dir(documentos):

                for RG in documentos.RG:

                    s2205_rg_dados = {}
                    s2205_rg_dados['s2205_documentos_id'] = s2205_documentos.id

                    try:
                        s2205_rg_dados['nrrg'] = read_from_xml(RG.nrRg.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2205_rg_dados['orgaoemissor'] = read_from_xml(RG.orgaoEmissor.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2205_rg_dados['dtexped'] = read_from_xml(RG.dtExped.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    s2205_rg = s2205RG.objects.create(**s2205_rg_dados)

            if 'RNE' in dir(documentos):

                for RNE in documentos.RNE:

                    s2205_rne_dados = {}
                    s2205_rne_dados['s2205_documentos_id'] = s2205_documentos.id

                    try:
                        s2205_rne_dados['nrrne'] = read_from_xml(RNE.nrRne.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2205_rne_dados['orgaoemissor'] = read_from_xml(RNE.orgaoEmissor.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2205_rne_dados['dtexped'] = read_from_xml(RNE.dtExped.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    s2205_rne = s2205RNE.objects.create(**s2205_rne_dados)

            if 'OC' in dir(documentos):

                for OC in documentos.OC:

                    s2205_oc_dados = {}
                    s2205_oc_dados['s2205_documentos_id'] = s2205_documentos.id

                    try:
                        s2205_oc_dados['nroc'] = read_from_xml(OC.nrOc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2205_oc_dados['orgaoemissor'] = read_from_xml(OC.orgaoEmissor.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2205_oc_dados['dtexped'] = read_from_xml(OC.dtExped.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s2205_oc_dados['dtvalid'] = read_from_xml(OC.dtValid.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    s2205_oc = s2205OC.objects.create(**s2205_oc_dados)

            if 'CNH' in dir(documentos):

                for CNH in documentos.CNH:

                    s2205_cnh_dados = {}
                    s2205_cnh_dados['s2205_documentos_id'] = s2205_documentos.id

                    try:
                        s2205_cnh_dados['nrregcnh'] = read_from_xml(CNH.nrRegCnh.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2205_cnh_dados['dtexped'] = read_from_xml(CNH.dtExped.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s2205_cnh_dados['ufcnh'] = read_from_xml(CNH.ufCnh.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2205_cnh_dados['dtvalid'] = read_from_xml(CNH.dtValid.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s2205_cnh_dados['dtprihab'] = read_from_xml(CNH.dtPriHab.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s2205_cnh_dados['categoriacnh'] = read_from_xml(CNH.categoriaCnh.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2205_cnh = s2205CNH.objects.create(**s2205_cnh_dados)

    if 'alteracao' in dir(evtAltCadastral) and 'dadosTrabalhador' in dir(evtAltCadastral.alteracao) and 'endereco' in dir(evtAltCadastral.alteracao.dadosTrabalhador) and 'brasil' in dir(evtAltCadastral.alteracao.dadosTrabalhador.endereco):

        for brasil in evtAltCadastral.alteracao.dadosTrabalhador.endereco.brasil:

            s2205_brasil_dados = {}
            s2205_brasil_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral.id

            try:
                s2205_brasil_dados['tplograd'] = read_from_xml(brasil.tpLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_brasil_dados['dsclograd'] = read_from_xml(brasil.dscLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_brasil_dados['nrlograd'] = read_from_xml(brasil.nrLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_brasil_dados['complemento'] = read_from_xml(brasil.complemento.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_brasil_dados['bairro'] = read_from_xml(brasil.bairro.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_brasil_dados['cep'] = read_from_xml(brasil.cep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_brasil_dados['codmunic'] = read_from_xml(brasil.codMunic.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2205_brasil_dados['uf'] = read_from_xml(brasil.uf.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2205_brasil = s2205brasil.objects.create(**s2205_brasil_dados)

    if 'alteracao' in dir(evtAltCadastral) and 'dadosTrabalhador' in dir(evtAltCadastral.alteracao) and 'endereco' in dir(evtAltCadastral.alteracao.dadosTrabalhador) and 'exterior' in dir(evtAltCadastral.alteracao.dadosTrabalhador.endereco):

        for exterior in evtAltCadastral.alteracao.dadosTrabalhador.endereco.exterior:

            s2205_exterior_dados = {}
            s2205_exterior_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral.id

            try:
                s2205_exterior_dados['paisresid'] = read_from_xml(exterior.paisResid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_exterior_dados['dsclograd'] = read_from_xml(exterior.dscLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_exterior_dados['nrlograd'] = read_from_xml(exterior.nrLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_exterior_dados['complemento'] = read_from_xml(exterior.complemento.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_exterior_dados['bairro'] = read_from_xml(exterior.bairro.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_exterior_dados['nmcid'] = read_from_xml(exterior.nmCid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_exterior_dados['codpostal'] = read_from_xml(exterior.codPostal.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2205_exterior = s2205exterior.objects.create(**s2205_exterior_dados)

    if 'alteracao' in dir(evtAltCadastral) and 'dadosTrabalhador' in dir(evtAltCadastral.alteracao) and 'trabEstrangeiro' in dir(evtAltCadastral.alteracao.dadosTrabalhador):

        for trabEstrangeiro in evtAltCadastral.alteracao.dadosTrabalhador.trabEstrangeiro:

            s2205_trabestrangeiro_dados = {}
            s2205_trabestrangeiro_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral.id

            try:
                s2205_trabestrangeiro_dados['dtchegada'] = read_from_xml(trabEstrangeiro.dtChegada.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2205_trabestrangeiro_dados['classtrabestrang'] = read_from_xml(trabEstrangeiro.classTrabEstrang.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2205_trabestrangeiro_dados['casadobr'] = read_from_xml(trabEstrangeiro.casadoBr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_trabestrangeiro_dados['filhosbr'] = read_from_xml(trabEstrangeiro.filhosBr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2205_trabestrangeiro = s2205trabEstrangeiro.objects.create(**s2205_trabestrangeiro_dados)

    if 'alteracao' in dir(evtAltCadastral) and 'dadosTrabalhador' in dir(evtAltCadastral.alteracao) and 'infoDeficiencia' in dir(evtAltCadastral.alteracao.dadosTrabalhador):

        for infoDeficiencia in evtAltCadastral.alteracao.dadosTrabalhador.infoDeficiencia:

            s2205_infodeficiencia_dados = {}
            s2205_infodeficiencia_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral.id

            try:
                s2205_infodeficiencia_dados['deffisica'] = read_from_xml(infoDeficiencia.defFisica.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_infodeficiencia_dados['defvisual'] = read_from_xml(infoDeficiencia.defVisual.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_infodeficiencia_dados['defauditiva'] = read_from_xml(infoDeficiencia.defAuditiva.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_infodeficiencia_dados['defmental'] = read_from_xml(infoDeficiencia.defMental.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_infodeficiencia_dados['defintelectual'] = read_from_xml(infoDeficiencia.defIntelectual.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_infodeficiencia_dados['reabreadap'] = read_from_xml(infoDeficiencia.reabReadap.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_infodeficiencia_dados['infocota'] = read_from_xml(infoDeficiencia.infoCota.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_infodeficiencia_dados['observacao'] = read_from_xml(infoDeficiencia.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2205_infodeficiencia = s2205infoDeficiencia.objects.create(**s2205_infodeficiencia_dados)

    if 'alteracao' in dir(evtAltCadastral) and 'dadosTrabalhador' in dir(evtAltCadastral.alteracao) and 'dependente' in dir(evtAltCadastral.alteracao.dadosTrabalhador):

        for dependente in evtAltCadastral.alteracao.dadosTrabalhador.dependente:

            s2205_dependente_dados = {}
            s2205_dependente_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral.id

            try:
                s2205_dependente_dados['tpdep'] = read_from_xml(dependente.tpDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_dependente_dados['nmdep'] = read_from_xml(dependente.nmDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_dependente_dados['dtnascto'] = read_from_xml(dependente.dtNascto.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2205_dependente_dados['cpfdep'] = read_from_xml(dependente.cpfDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_dependente_dados['sexodep'] = read_from_xml(dependente.sexoDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_dependente_dados['depirrf'] = read_from_xml(dependente.depIRRF.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_dependente_dados['depsf'] = read_from_xml(dependente.depSF.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_dependente_dados['inctrab'] = read_from_xml(dependente.incTrab.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_dependente_dados['depfinsprev'] = read_from_xml(dependente.depFinsPrev.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2205_dependente = s2205dependente.objects.create(**s2205_dependente_dados)

    if 'alteracao' in dir(evtAltCadastral) and 'dadosTrabalhador' in dir(evtAltCadastral.alteracao) and 'aposentadoria' in dir(evtAltCadastral.alteracao.dadosTrabalhador):

        for aposentadoria in evtAltCadastral.alteracao.dadosTrabalhador.aposentadoria:

            s2205_aposentadoria_dados = {}
            s2205_aposentadoria_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral.id

            try:
                s2205_aposentadoria_dados['trabaposent'] = read_from_xml(aposentadoria.trabAposent.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2205_aposentadoria = s2205aposentadoria.objects.create(**s2205_aposentadoria_dados)

    if 'alteracao' in dir(evtAltCadastral) and 'dadosTrabalhador' in dir(evtAltCadastral.alteracao) and 'contato' in dir(evtAltCadastral.alteracao.dadosTrabalhador):

        for contato in evtAltCadastral.alteracao.dadosTrabalhador.contato:

            s2205_contato_dados = {}
            s2205_contato_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral.id

            try:
                s2205_contato_dados['foneprinc'] = read_from_xml(contato.fonePrinc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_contato_dados['fonealternat'] = read_from_xml(contato.foneAlternat.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_contato_dados['emailprinc'] = read_from_xml(contato.emailPrinc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2205_contato_dados['emailalternat'] = read_from_xml(contato.emailAlternat.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2205_contato = s2205contato.objects.create(**s2205_contato_dados)
    s2205_evtaltcadastral_dados['evento'] = 's2205'
    s2205_evtaltcadastral_dados['id'] = s2205_evtaltcadastral.id
    s2205_evtaltcadastral_dados['identidade_evento'] = doc.eSocial.evtAltCadastral['Id']

    from emensageriapro.esocial.views.s2205_evtaltcadastral_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2205_evtaltcadastral.id)

    return s2205_evtaltcadastral_dados