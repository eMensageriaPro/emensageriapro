# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2300.models import *
from emensageriapro.functions import read_from_xml



def read_s2300_evttsvinicio_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2300_evttsvinicio_obj(request, doc, status, validar)
    return dados



def read_s2300_evttsvinicio(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2300_evttsvinicio_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2300evtTSVInicio.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2300_evttsvinicio_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2300_evttsvinicio_dados = {}
    s2300_evttsvinicio_dados['status'] = status
    s2300_evttsvinicio_dados['arquivo_original'] = 1
    if arquivo:
        s2300_evttsvinicio_dados['arquivo'] = arquivo.arquivo
    s2300_evttsvinicio_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2300_evttsvinicio_dados['identidade'] = doc.eSocial.evtTSVInicio['Id']
    evtTSVInicio = doc.eSocial.evtTSVInicio

    try:
        s2300_evttsvinicio_dados['indretif'] = read_from_xml(evtTSVInicio.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['nrrecibo'] = read_from_xml(evtTSVInicio.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['tpamb'] = read_from_xml(evtTSVInicio.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['procemi'] = read_from_xml(evtTSVInicio.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['verproc'] = read_from_xml(evtTSVInicio.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['tpinsc'] = read_from_xml(evtTSVInicio.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['nrinsc'] = read_from_xml(evtTSVInicio.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['cpftrab'] = read_from_xml(evtTSVInicio.trabalhador.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['nistrab'] = read_from_xml(evtTSVInicio.trabalhador.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['nmtrab'] = read_from_xml(evtTSVInicio.trabalhador.nmTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['sexo'] = read_from_xml(evtTSVInicio.trabalhador.sexo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['racacor'] = read_from_xml(evtTSVInicio.trabalhador.racaCor.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['estciv'] = read_from_xml(evtTSVInicio.trabalhador.estCiv.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['grauinstr'] = read_from_xml(evtTSVInicio.trabalhador.grauInstr.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['nmsoc'] = read_from_xml(evtTSVInicio.trabalhador.nmSoc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['dtnascto'] = read_from_xml(evtTSVInicio.trabalhador.nascimento.dtNascto.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['codmunic'] = read_from_xml(evtTSVInicio.trabalhador.nascimento.codMunic.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['uf'] = read_from_xml(evtTSVInicio.trabalhador.nascimento.uf.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['paisnascto'] = read_from_xml(evtTSVInicio.trabalhador.nascimento.paisNascto.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['paisnac'] = read_from_xml(evtTSVInicio.trabalhador.nascimento.paisNac.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['nmmae'] = read_from_xml(evtTSVInicio.trabalhador.nascimento.nmMae.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['nmpai'] = read_from_xml(evtTSVInicio.trabalhador.nascimento.nmPai.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['cadini'] = read_from_xml(evtTSVInicio.infoTSVInicio.cadIni.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['codcateg'] = read_from_xml(evtTSVInicio.infoTSVInicio.codCateg.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['dtinicio'] = read_from_xml(evtTSVInicio.infoTSVInicio.dtInicio.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['natatividade'] = read_from_xml(evtTSVInicio.infoTSVInicio.natAtividade.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    s2300_evttsvinicio = s2300evtTSVInicio.objects.create(**s2300_evttsvinicio_dados)

    if 'trabalhador' in dir(evtTSVInicio) and 'documentos' in dir(evtTSVInicio.trabalhador):

        for documentos in evtTSVInicio.trabalhador.documentos:

            s2300_documentos_dados = {}
            s2300_documentos_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            s2300_documentos = s2300documentos.objects.create(**s2300_documentos_dados)

            if 'CTPS' in dir(documentos):

                for CTPS in documentos.CTPS:

                    s2300_ctps_dados = {}
                    s2300_ctps_dados['s2300_documentos_id'] = s2300_documentos.id

                    try:
                        s2300_ctps_dados['nrctps'] = read_from_xml(CTPS.nrCtps.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_ctps_dados['seriectps'] = read_from_xml(CTPS.serieCtps.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_ctps_dados['ufctps'] = read_from_xml(CTPS.ufCtps.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2300_ctps = s2300CTPS.objects.create(**s2300_ctps_dados)

            if 'RIC' in dir(documentos):

                for RIC in documentos.RIC:

                    s2300_ric_dados = {}
                    s2300_ric_dados['s2300_documentos_id'] = s2300_documentos.id

                    try:
                        s2300_ric_dados['nrric'] = read_from_xml(RIC.nrRic.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_ric_dados['orgaoemissor'] = read_from_xml(RIC.orgaoEmissor.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_ric_dados['dtexped'] = read_from_xml(RIC.dtExped.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    s2300_ric = s2300RIC.objects.create(**s2300_ric_dados)

            if 'RG' in dir(documentos):

                for RG in documentos.RG:

                    s2300_rg_dados = {}
                    s2300_rg_dados['s2300_documentos_id'] = s2300_documentos.id

                    try:
                        s2300_rg_dados['nrrg'] = read_from_xml(RG.nrRg.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_rg_dados['orgaoemissor'] = read_from_xml(RG.orgaoEmissor.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_rg_dados['dtexped'] = read_from_xml(RG.dtExped.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    s2300_rg = s2300RG.objects.create(**s2300_rg_dados)

            if 'RNE' in dir(documentos):

                for RNE in documentos.RNE:

                    s2300_rne_dados = {}
                    s2300_rne_dados['s2300_documentos_id'] = s2300_documentos.id

                    try:
                        s2300_rne_dados['nrrne'] = read_from_xml(RNE.nrRne.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_rne_dados['orgaoemissor'] = read_from_xml(RNE.orgaoEmissor.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_rne_dados['dtexped'] = read_from_xml(RNE.dtExped.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    s2300_rne = s2300RNE.objects.create(**s2300_rne_dados)

            if 'OC' in dir(documentos):

                for OC in documentos.OC:

                    s2300_oc_dados = {}
                    s2300_oc_dados['s2300_documentos_id'] = s2300_documentos.id

                    try:
                        s2300_oc_dados['nroc'] = read_from_xml(OC.nrOc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_oc_dados['orgaoemissor'] = read_from_xml(OC.orgaoEmissor.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_oc_dados['dtexped'] = read_from_xml(OC.dtExped.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_oc_dados['dtvalid'] = read_from_xml(OC.dtValid.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    s2300_oc = s2300OC.objects.create(**s2300_oc_dados)

            if 'CNH' in dir(documentos):

                for CNH in documentos.CNH:

                    s2300_cnh_dados = {}
                    s2300_cnh_dados['s2300_documentos_id'] = s2300_documentos.id

                    try:
                        s2300_cnh_dados['nrregcnh'] = read_from_xml(CNH.nrRegCnh.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_cnh_dados['dtexped'] = read_from_xml(CNH.dtExped.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_cnh_dados['ufcnh'] = read_from_xml(CNH.ufCnh.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_cnh_dados['dtvalid'] = read_from_xml(CNH.dtValid.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_cnh_dados['dtprihab'] = read_from_xml(CNH.dtPriHab.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_cnh_dados['categoriacnh'] = read_from_xml(CNH.categoriaCnh.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2300_cnh = s2300CNH.objects.create(**s2300_cnh_dados)

    if 'trabalhador' in dir(evtTSVInicio) and 'endereco' in dir(evtTSVInicio.trabalhador) and 'brasil' in dir(evtTSVInicio.trabalhador.endereco):

        for brasil in evtTSVInicio.trabalhador.endereco.brasil:

            s2300_brasil_dados = {}
            s2300_brasil_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_brasil_dados['tplograd'] = read_from_xml(brasil.tpLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_brasil_dados['dsclograd'] = read_from_xml(brasil.dscLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_brasil_dados['nrlograd'] = read_from_xml(brasil.nrLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_brasil_dados['complemento'] = read_from_xml(brasil.complemento.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_brasil_dados['bairro'] = read_from_xml(brasil.bairro.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_brasil_dados['cep'] = read_from_xml(brasil.cep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_brasil_dados['codmunic'] = read_from_xml(brasil.codMunic.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2300_brasil_dados['uf'] = read_from_xml(brasil.uf.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2300_brasil = s2300brasil.objects.create(**s2300_brasil_dados)

    if 'trabalhador' in dir(evtTSVInicio) and 'endereco' in dir(evtTSVInicio.trabalhador) and 'exterior' in dir(evtTSVInicio.trabalhador.endereco):

        for exterior in evtTSVInicio.trabalhador.endereco.exterior:

            s2300_exterior_dados = {}
            s2300_exterior_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_exterior_dados['paisresid'] = read_from_xml(exterior.paisResid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_exterior_dados['dsclograd'] = read_from_xml(exterior.dscLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_exterior_dados['nrlograd'] = read_from_xml(exterior.nrLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_exterior_dados['complemento'] = read_from_xml(exterior.complemento.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_exterior_dados['bairro'] = read_from_xml(exterior.bairro.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_exterior_dados['nmcid'] = read_from_xml(exterior.nmCid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_exterior_dados['codpostal'] = read_from_xml(exterior.codPostal.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2300_exterior = s2300exterior.objects.create(**s2300_exterior_dados)

    if 'trabalhador' in dir(evtTSVInicio) and 'trabEstrangeiro' in dir(evtTSVInicio.trabalhador):

        for trabEstrangeiro in evtTSVInicio.trabalhador.trabEstrangeiro:

            s2300_trabestrangeiro_dados = {}
            s2300_trabestrangeiro_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_trabestrangeiro_dados['dtchegada'] = read_from_xml(trabEstrangeiro.dtChegada.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2300_trabestrangeiro_dados['classtrabestrang'] = read_from_xml(trabEstrangeiro.classTrabEstrang.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2300_trabestrangeiro_dados['casadobr'] = read_from_xml(trabEstrangeiro.casadoBr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_trabestrangeiro_dados['filhosbr'] = read_from_xml(trabEstrangeiro.filhosBr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2300_trabestrangeiro = s2300trabEstrangeiro.objects.create(**s2300_trabestrangeiro_dados)

    if 'trabalhador' in dir(evtTSVInicio) and 'infoDeficiencia' in dir(evtTSVInicio.trabalhador):

        for infoDeficiencia in evtTSVInicio.trabalhador.infoDeficiencia:

            s2300_infodeficiencia_dados = {}
            s2300_infodeficiencia_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_infodeficiencia_dados['deffisica'] = read_from_xml(infoDeficiencia.defFisica.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_infodeficiencia_dados['defvisual'] = read_from_xml(infoDeficiencia.defVisual.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_infodeficiencia_dados['defauditiva'] = read_from_xml(infoDeficiencia.defAuditiva.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_infodeficiencia_dados['defmental'] = read_from_xml(infoDeficiencia.defMental.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_infodeficiencia_dados['defintelectual'] = read_from_xml(infoDeficiencia.defIntelectual.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_infodeficiencia_dados['reabreadap'] = read_from_xml(infoDeficiencia.reabReadap.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_infodeficiencia_dados['observacao'] = read_from_xml(infoDeficiencia.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2300_infodeficiencia = s2300infoDeficiencia.objects.create(**s2300_infodeficiencia_dados)

    if 'trabalhador' in dir(evtTSVInicio) and 'dependente' in dir(evtTSVInicio.trabalhador):

        for dependente in evtTSVInicio.trabalhador.dependente:

            s2300_dependente_dados = {}
            s2300_dependente_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_dependente_dados['tpdep'] = read_from_xml(dependente.tpDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_dependente_dados['nmdep'] = read_from_xml(dependente.nmDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_dependente_dados['dtnascto'] = read_from_xml(dependente.dtNascto.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2300_dependente_dados['cpfdep'] = read_from_xml(dependente.cpfDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_dependente_dados['sexodep'] = read_from_xml(dependente.sexoDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_dependente_dados['depirrf'] = read_from_xml(dependente.depIRRF.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_dependente_dados['depsf'] = read_from_xml(dependente.depSF.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_dependente_dados['inctrab'] = read_from_xml(dependente.incTrab.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_dependente_dados['depfinsprev'] = read_from_xml(dependente.depFinsPrev.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2300_dependente = s2300dependente.objects.create(**s2300_dependente_dados)

    if 'trabalhador' in dir(evtTSVInicio) and 'contato' in dir(evtTSVInicio.trabalhador):

        for contato in evtTSVInicio.trabalhador.contato:

            s2300_contato_dados = {}
            s2300_contato_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_contato_dados['foneprinc'] = read_from_xml(contato.fonePrinc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_contato_dados['fonealternat'] = read_from_xml(contato.foneAlternat.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_contato_dados['emailprinc'] = read_from_xml(contato.emailPrinc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_contato_dados['emailalternat'] = read_from_xml(contato.emailAlternat.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2300_contato = s2300contato.objects.create(**s2300_contato_dados)

    if 'infoTSVInicio' in dir(evtTSVInicio) and 'infoComplementares' in dir(evtTSVInicio.infoTSVInicio):

        for infoComplementares in evtTSVInicio.infoTSVInicio.infoComplementares:

            s2300_infocomplementares_dados = {}
            s2300_infocomplementares_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            s2300_infocomplementares = s2300infoComplementares.objects.create(**s2300_infocomplementares_dados)

            if 'cargoFuncao' in dir(infoComplementares):

                for cargoFuncao in infoComplementares.cargoFuncao:

                    s2300_cargofuncao_dados = {}
                    s2300_cargofuncao_dados['s2300_infocomplementares_id'] = s2300_infocomplementares.id

                    try:
                        s2300_cargofuncao_dados['codcargo'] = read_from_xml(cargoFuncao.codCargo.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_cargofuncao_dados['codfuncao'] = read_from_xml(cargoFuncao.codFuncao.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2300_cargofuncao = s2300cargoFuncao.objects.create(**s2300_cargofuncao_dados)

            if 'remuneracao' in dir(infoComplementares):

                for remuneracao in infoComplementares.remuneracao:

                    s2300_remuneracao_dados = {}
                    s2300_remuneracao_dados['s2300_infocomplementares_id'] = s2300_infocomplementares.id

                    try:
                        s2300_remuneracao_dados['vrsalfx'] = read_from_xml(remuneracao.vrSalFx.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s2300_remuneracao_dados['undsalfixo'] = read_from_xml(remuneracao.undSalFixo.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_remuneracao_dados['dscsalvar'] = read_from_xml(remuneracao.dscSalVar.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2300_remuneracao = s2300remuneracao.objects.create(**s2300_remuneracao_dados)

            if 'fgts' in dir(infoComplementares):

                for fgts in infoComplementares.fgts:

                    s2300_fgts_dados = {}
                    s2300_fgts_dados['s2300_infocomplementares_id'] = s2300_infocomplementares.id

                    try:
                        s2300_fgts_dados['opcfgts'] = read_from_xml(fgts.opcFGTS.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_fgts_dados['dtopcfgts'] = read_from_xml(fgts.dtOpcFGTS.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    s2300_fgts = s2300fgts.objects.create(**s2300_fgts_dados)

            if 'infoDirigenteSindical' in dir(infoComplementares):

                for infoDirigenteSindical in infoComplementares.infoDirigenteSindical:

                    s2300_infodirigentesindical_dados = {}
                    s2300_infodirigentesindical_dados['s2300_infocomplementares_id'] = s2300_infocomplementares.id

                    try:
                        s2300_infodirigentesindical_dados['categorig'] = read_from_xml(infoDirigenteSindical.categOrig.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infodirigentesindical_dados['cnpjorigem'] = read_from_xml(infoDirigenteSindical.cnpjOrigem.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infodirigentesindical_dados['dtadmorig'] = read_from_xml(infoDirigenteSindical.dtAdmOrig.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infodirigentesindical_dados['matricorig'] = read_from_xml(infoDirigenteSindical.matricOrig.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2300_infodirigentesindical = s2300infoDirigenteSindical.objects.create(**s2300_infodirigentesindical_dados)

            if 'infoTrabCedido' in dir(infoComplementares):

                for infoTrabCedido in infoComplementares.infoTrabCedido:

                    s2300_infotrabcedido_dados = {}
                    s2300_infotrabcedido_dados['s2300_infocomplementares_id'] = s2300_infocomplementares.id

                    try:
                        s2300_infotrabcedido_dados['categorig'] = read_from_xml(infoTrabCedido.categOrig.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infotrabcedido_dados['cnpjcednt'] = read_from_xml(infoTrabCedido.cnpjCednt.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infotrabcedido_dados['matricced'] = read_from_xml(infoTrabCedido.matricCed.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infotrabcedido_dados['dtadmced'] = read_from_xml(infoTrabCedido.dtAdmCed.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infotrabcedido_dados['tpregtrab'] = read_from_xml(infoTrabCedido.tpRegTrab.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infotrabcedido_dados['tpregprev'] = read_from_xml(infoTrabCedido.tpRegPrev.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infotrabcedido_dados['infonus'] = read_from_xml(infoTrabCedido.infOnus.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infotrabcedido_dados['indremuncargo'] = read_from_xml(infoTrabCedido.indRemunCargo.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2300_infotrabcedido = s2300infoTrabCedido.objects.create(**s2300_infotrabcedido_dados)

            if 'infoEstagiario' in dir(infoComplementares):

                for infoEstagiario in infoComplementares.infoEstagiario:

                    s2300_infoestagiario_dados = {}
                    s2300_infoestagiario_dados['s2300_infocomplementares_id'] = s2300_infocomplementares.id

                    try:
                        s2300_infoestagiario_dados['natestagio'] = read_from_xml(infoEstagiario.natEstagio.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['nivestagio'] = read_from_xml(infoEstagiario.nivEstagio.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['areaatuacao'] = read_from_xml(infoEstagiario.areaAtuacao.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['nrapol'] = read_from_xml(infoEstagiario.nrApol.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['vlrbolsa'] = read_from_xml(infoEstagiario.vlrBolsa.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['dtprevterm'] = read_from_xml(infoEstagiario.dtPrevTerm.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['cnpjinstensino'] = read_from_xml(infoEstagiario.instEnsino.cnpjInstEnsino.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['nmrazao'] = read_from_xml(infoEstagiario.instEnsino.nmRazao.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['dsclograd'] = read_from_xml(infoEstagiario.instEnsino.dscLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['nrlograd'] = read_from_xml(infoEstagiario.instEnsino.nrLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['bairro'] = read_from_xml(infoEstagiario.instEnsino.bairro.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['cep'] = read_from_xml(infoEstagiario.instEnsino.cep.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['codmunic'] = read_from_xml(infoEstagiario.instEnsino.codMunic.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['uf'] = read_from_xml(infoEstagiario.instEnsino.uf.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2300_infoestagiario = s2300infoEstagiario.objects.create(**s2300_infoestagiario_dados)

                    if 'ageIntegracao' in dir(infoEstagiario):

                        for ageIntegracao in infoEstagiario.ageIntegracao:

                            s2300_ageintegracao_dados = {}
                            s2300_ageintegracao_dados['s2300_infoestagiario_id'] = s2300_infoestagiario.id
        
                            try:
                                s2300_ageintegracao_dados['cnpjagntinteg'] = read_from_xml(ageIntegracao.cnpjAgntInteg.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2300_ageintegracao_dados['nmrazao'] = read_from_xml(ageIntegracao.nmRazao.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2300_ageintegracao_dados['dsclograd'] = read_from_xml(ageIntegracao.dscLograd.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2300_ageintegracao_dados['nrlograd'] = read_from_xml(ageIntegracao.nrLograd.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2300_ageintegracao_dados['bairro'] = read_from_xml(ageIntegracao.bairro.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2300_ageintegracao_dados['cep'] = read_from_xml(ageIntegracao.cep.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2300_ageintegracao_dados['codmunic'] = read_from_xml(ageIntegracao.codMunic.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2300_ageintegracao_dados['uf'] = read_from_xml(ageIntegracao.uf.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s2300_ageintegracao = s2300ageIntegracao.objects.create(**s2300_ageintegracao_dados)

                    if 'supervisorEstagio' in dir(infoEstagiario):

                        for supervisorEstagio in infoEstagiario.supervisorEstagio:

                            s2300_supervisorestagio_dados = {}
                            s2300_supervisorestagio_dados['s2300_infoestagiario_id'] = s2300_infoestagiario.id
        
                            try:
                                s2300_supervisorestagio_dados['cpfsupervisor'] = read_from_xml(supervisorEstagio.cpfSupervisor.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2300_supervisorestagio_dados['nmsuperv'] = read_from_xml(supervisorEstagio.nmSuperv.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s2300_supervisorestagio = s2300supervisorEstagio.objects.create(**s2300_supervisorestagio_dados)

    if 'infoTSVInicio' in dir(evtTSVInicio) and 'mudancaCPF' in dir(evtTSVInicio.infoTSVInicio):

        for mudancaCPF in evtTSVInicio.infoTSVInicio.mudancaCPF:

            s2300_mudancacpf_dados = {}
            s2300_mudancacpf_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_mudancacpf_dados['cpfant'] = read_from_xml(mudancaCPF.cpfAnt.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2300_mudancacpf_dados['dtaltcpf'] = read_from_xml(mudancaCPF.dtAltCPF.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2300_mudancacpf_dados['observacao'] = read_from_xml(mudancaCPF.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2300_mudancacpf = s2300mudancaCPF.objects.create(**s2300_mudancacpf_dados)

    if 'infoTSVInicio' in dir(evtTSVInicio) and 'afastamento' in dir(evtTSVInicio.infoTSVInicio):

        for afastamento in evtTSVInicio.infoTSVInicio.afastamento:

            s2300_afastamento_dados = {}
            s2300_afastamento_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_afastamento_dados['dtiniafast'] = read_from_xml(afastamento.dtIniAfast.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2300_afastamento_dados['codmotafast'] = read_from_xml(afastamento.codMotAfast.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2300_afastamento = s2300afastamento.objects.create(**s2300_afastamento_dados)

    if 'infoTSVInicio' in dir(evtTSVInicio) and 'termino' in dir(evtTSVInicio.infoTSVInicio):

        for termino in evtTSVInicio.infoTSVInicio.termino:

            s2300_termino_dados = {}
            s2300_termino_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_termino_dados['dtterm'] = read_from_xml(termino.dtTerm.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            s2300_termino = s2300termino.objects.create(**s2300_termino_dados)
    s2300_evttsvinicio_dados['evento'] = 's2300'
    s2300_evttsvinicio_dados['id'] = s2300_evttsvinicio.id
    s2300_evttsvinicio_dados['identidade_evento'] = doc.eSocial.evtTSVInicio['Id']

    from emensageriapro.esocial.views.s2300_evttsvinicio_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2300_evttsvinicio.id)

    return s2300_evttsvinicio_dados