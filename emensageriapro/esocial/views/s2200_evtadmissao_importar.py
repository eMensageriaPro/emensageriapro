# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2200.models import *
from emensageriapro.functions import read_from_xml



def read_s2200_evtadmissao_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2200_evtadmissao_obj(request, doc, status, validar)
    return dados



def read_s2200_evtadmissao(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2200_evtadmissao_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2200evtAdmissao.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2200_evtadmissao_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2200_evtadmissao_dados = {}
    s2200_evtadmissao_dados['status'] = status
    s2200_evtadmissao_dados['arquivo_original'] = 1
    if arquivo:
        s2200_evtadmissao_dados['arquivo'] = arquivo.arquivo
    s2200_evtadmissao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2200_evtadmissao_dados['identidade'] = doc.eSocial.evtAdmissao['Id']
    evtAdmissao = doc.eSocial.evtAdmissao

    try:
        s2200_evtadmissao_dados['indretif'] = read_from_xml(evtAdmissao.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['nrrecibo'] = read_from_xml(evtAdmissao.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['tpamb'] = read_from_xml(evtAdmissao.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['procemi'] = read_from_xml(evtAdmissao.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['verproc'] = read_from_xml(evtAdmissao.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['tpinsc'] = read_from_xml(evtAdmissao.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['nrinsc'] = read_from_xml(evtAdmissao.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['cpftrab'] = read_from_xml(evtAdmissao.trabalhador.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['nistrab'] = read_from_xml(evtAdmissao.trabalhador.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['nmtrab'] = read_from_xml(evtAdmissao.trabalhador.nmTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['sexo'] = read_from_xml(evtAdmissao.trabalhador.sexo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['racacor'] = read_from_xml(evtAdmissao.trabalhador.racaCor.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['estciv'] = read_from_xml(evtAdmissao.trabalhador.estCiv.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['grauinstr'] = read_from_xml(evtAdmissao.trabalhador.grauInstr.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['indpriempr'] = read_from_xml(evtAdmissao.trabalhador.indPriEmpr.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['nmsoc'] = read_from_xml(evtAdmissao.trabalhador.nmSoc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['dtnascto'] = read_from_xml(evtAdmissao.trabalhador.nascimento.dtNascto.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['codmunic'] = read_from_xml(evtAdmissao.trabalhador.nascimento.codMunic.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['uf'] = read_from_xml(evtAdmissao.trabalhador.nascimento.uf.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['paisnascto'] = read_from_xml(evtAdmissao.trabalhador.nascimento.paisNascto.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['paisnac'] = read_from_xml(evtAdmissao.trabalhador.nascimento.paisNac.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['nmmae'] = read_from_xml(evtAdmissao.trabalhador.nascimento.nmMae.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['nmpai'] = read_from_xml(evtAdmissao.trabalhador.nascimento.nmPai.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['matricula'] = read_from_xml(evtAdmissao.vinculo.matricula.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['tpregtrab'] = read_from_xml(evtAdmissao.vinculo.tpRegTrab.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['tpregprev'] = read_from_xml(evtAdmissao.vinculo.tpRegPrev.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['nrrecinfprelim'] = read_from_xml(evtAdmissao.vinculo.nrRecInfPrelim.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['cadini'] = read_from_xml(evtAdmissao.vinculo.cadIni.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['codcargo'] = read_from_xml(evtAdmissao.vinculo.infoContrato.codCargo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['dtingrcargo'] = read_from_xml(evtAdmissao.vinculo.infoContrato.dtIngrCargo.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['codfuncao'] = read_from_xml(evtAdmissao.vinculo.infoContrato.codFuncao.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['codcateg'] = read_from_xml(evtAdmissao.vinculo.infoContrato.codCateg.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['codcarreira'] = read_from_xml(evtAdmissao.vinculo.infoContrato.codCarreira.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['dtingrcarr'] = read_from_xml(evtAdmissao.vinculo.infoContrato.dtIngrCarr.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['vrsalfx'] = read_from_xml(evtAdmissao.vinculo.infoContrato.remuneracao.vrSalFx.cdata, 'esocial', 'N', 2)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['undsalfixo'] = read_from_xml(evtAdmissao.vinculo.infoContrato.remuneracao.undSalFixo.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['dscsalvar'] = read_from_xml(evtAdmissao.vinculo.infoContrato.remuneracao.dscSalVar.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['tpcontr'] = read_from_xml(evtAdmissao.vinculo.infoContrato.duracao.tpContr.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['dtterm'] = read_from_xml(evtAdmissao.vinculo.infoContrato.duracao.dtTerm.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['clauassec'] = read_from_xml(evtAdmissao.vinculo.infoContrato.duracao.clauAssec.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2200_evtadmissao_dados['objdet'] = read_from_xml(evtAdmissao.vinculo.infoContrato.duracao.objDet.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s2200_evtadmissao = s2200evtAdmissao.objects.create(**s2200_evtadmissao_dados)

    if 'trabalhador' in dir(evtAdmissao) and 'documentos' in dir(evtAdmissao.trabalhador):

        for documentos in evtAdmissao.trabalhador.documentos:

            s2200_documentos_dados = {}
            s2200_documentos_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            s2200_documentos = s2200documentos.objects.create(**s2200_documentos_dados)

            if 'CTPS' in dir(documentos):

                for CTPS in documentos.CTPS:

                    s2200_ctps_dados = {}
                    s2200_ctps_dados['s2200_documentos_id'] = s2200_documentos.id

                    try:
                        s2200_ctps_dados['nrctps'] = read_from_xml(CTPS.nrCtps.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_ctps_dados['seriectps'] = read_from_xml(CTPS.serieCtps.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_ctps_dados['ufctps'] = read_from_xml(CTPS.ufCtps.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2200_ctps = s2200CTPS.objects.create(**s2200_ctps_dados)

            if 'RIC' in dir(documentos):

                for RIC in documentos.RIC:

                    s2200_ric_dados = {}
                    s2200_ric_dados['s2200_documentos_id'] = s2200_documentos.id

                    try:
                        s2200_ric_dados['nrric'] = read_from_xml(RIC.nrRic.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_ric_dados['orgaoemissor'] = read_from_xml(RIC.orgaoEmissor.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_ric_dados['dtexped'] = read_from_xml(RIC.dtExped.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    s2200_ric = s2200RIC.objects.create(**s2200_ric_dados)

            if 'RG' in dir(documentos):

                for RG in documentos.RG:

                    s2200_rg_dados = {}
                    s2200_rg_dados['s2200_documentos_id'] = s2200_documentos.id

                    try:
                        s2200_rg_dados['nrrg'] = read_from_xml(RG.nrRg.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_rg_dados['orgaoemissor'] = read_from_xml(RG.orgaoEmissor.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_rg_dados['dtexped'] = read_from_xml(RG.dtExped.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    s2200_rg = s2200RG.objects.create(**s2200_rg_dados)

            if 'RNE' in dir(documentos):

                for RNE in documentos.RNE:

                    s2200_rne_dados = {}
                    s2200_rne_dados['s2200_documentos_id'] = s2200_documentos.id

                    try:
                        s2200_rne_dados['nrrne'] = read_from_xml(RNE.nrRne.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_rne_dados['orgaoemissor'] = read_from_xml(RNE.orgaoEmissor.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_rne_dados['dtexped'] = read_from_xml(RNE.dtExped.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    s2200_rne = s2200RNE.objects.create(**s2200_rne_dados)

            if 'OC' in dir(documentos):

                for OC in documentos.OC:

                    s2200_oc_dados = {}
                    s2200_oc_dados['s2200_documentos_id'] = s2200_documentos.id

                    try:
                        s2200_oc_dados['nroc'] = read_from_xml(OC.nrOc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_oc_dados['orgaoemissor'] = read_from_xml(OC.orgaoEmissor.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_oc_dados['dtexped'] = read_from_xml(OC.dtExped.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_oc_dados['dtvalid'] = read_from_xml(OC.dtValid.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    s2200_oc = s2200OC.objects.create(**s2200_oc_dados)

            if 'CNH' in dir(documentos):

                for CNH in documentos.CNH:

                    s2200_cnh_dados = {}
                    s2200_cnh_dados['s2200_documentos_id'] = s2200_documentos.id

                    try:
                        s2200_cnh_dados['nrregcnh'] = read_from_xml(CNH.nrRegCnh.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_cnh_dados['dtexped'] = read_from_xml(CNH.dtExped.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_cnh_dados['ufcnh'] = read_from_xml(CNH.ufCnh.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_cnh_dados['dtvalid'] = read_from_xml(CNH.dtValid.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_cnh_dados['dtprihab'] = read_from_xml(CNH.dtPriHab.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_cnh_dados['categoriacnh'] = read_from_xml(CNH.categoriaCnh.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2200_cnh = s2200CNH.objects.create(**s2200_cnh_dados)

    if 'trabalhador' in dir(evtAdmissao) and 'endereco' in dir(evtAdmissao.trabalhador) and 'brasil' in dir(evtAdmissao.trabalhador.endereco):

        for brasil in evtAdmissao.trabalhador.endereco.brasil:

            s2200_brasil_dados = {}
            s2200_brasil_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_brasil_dados['tplograd'] = read_from_xml(brasil.tpLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_brasil_dados['dsclograd'] = read_from_xml(brasil.dscLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_brasil_dados['nrlograd'] = read_from_xml(brasil.nrLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_brasil_dados['complemento'] = read_from_xml(brasil.complemento.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_brasil_dados['bairro'] = read_from_xml(brasil.bairro.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_brasil_dados['cep'] = read_from_xml(brasil.cep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_brasil_dados['codmunic'] = read_from_xml(brasil.codMunic.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2200_brasil_dados['uf'] = read_from_xml(brasil.uf.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2200_brasil = s2200brasil.objects.create(**s2200_brasil_dados)

    if 'trabalhador' in dir(evtAdmissao) and 'endereco' in dir(evtAdmissao.trabalhador) and 'exterior' in dir(evtAdmissao.trabalhador.endereco):

        for exterior in evtAdmissao.trabalhador.endereco.exterior:

            s2200_exterior_dados = {}
            s2200_exterior_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_exterior_dados['paisresid'] = read_from_xml(exterior.paisResid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_exterior_dados['dsclograd'] = read_from_xml(exterior.dscLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_exterior_dados['nrlograd'] = read_from_xml(exterior.nrLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_exterior_dados['complemento'] = read_from_xml(exterior.complemento.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_exterior_dados['bairro'] = read_from_xml(exterior.bairro.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_exterior_dados['nmcid'] = read_from_xml(exterior.nmCid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_exterior_dados['codpostal'] = read_from_xml(exterior.codPostal.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2200_exterior = s2200exterior.objects.create(**s2200_exterior_dados)

    if 'trabalhador' in dir(evtAdmissao) and 'trabEstrangeiro' in dir(evtAdmissao.trabalhador):

        for trabEstrangeiro in evtAdmissao.trabalhador.trabEstrangeiro:

            s2200_trabestrangeiro_dados = {}
            s2200_trabestrangeiro_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_trabestrangeiro_dados['dtchegada'] = read_from_xml(trabEstrangeiro.dtChegada.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2200_trabestrangeiro_dados['classtrabestrang'] = read_from_xml(trabEstrangeiro.classTrabEstrang.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2200_trabestrangeiro_dados['casadobr'] = read_from_xml(trabEstrangeiro.casadoBr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_trabestrangeiro_dados['filhosbr'] = read_from_xml(trabEstrangeiro.filhosBr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2200_trabestrangeiro = s2200trabEstrangeiro.objects.create(**s2200_trabestrangeiro_dados)

    if 'trabalhador' in dir(evtAdmissao) and 'infoDeficiencia' in dir(evtAdmissao.trabalhador):

        for infoDeficiencia in evtAdmissao.trabalhador.infoDeficiencia:

            s2200_infodeficiencia_dados = {}
            s2200_infodeficiencia_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_infodeficiencia_dados['deffisica'] = read_from_xml(infoDeficiencia.defFisica.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_infodeficiencia_dados['defvisual'] = read_from_xml(infoDeficiencia.defVisual.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_infodeficiencia_dados['defauditiva'] = read_from_xml(infoDeficiencia.defAuditiva.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_infodeficiencia_dados['defmental'] = read_from_xml(infoDeficiencia.defMental.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_infodeficiencia_dados['defintelectual'] = read_from_xml(infoDeficiencia.defIntelectual.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_infodeficiencia_dados['reabreadap'] = read_from_xml(infoDeficiencia.reabReadap.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_infodeficiencia_dados['infocota'] = read_from_xml(infoDeficiencia.infoCota.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_infodeficiencia_dados['observacao'] = read_from_xml(infoDeficiencia.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2200_infodeficiencia = s2200infoDeficiencia.objects.create(**s2200_infodeficiencia_dados)

    if 'trabalhador' in dir(evtAdmissao) and 'dependente' in dir(evtAdmissao.trabalhador):

        for dependente in evtAdmissao.trabalhador.dependente:

            s2200_dependente_dados = {}
            s2200_dependente_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_dependente_dados['tpdep'] = read_from_xml(dependente.tpDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_dependente_dados['nmdep'] = read_from_xml(dependente.nmDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_dependente_dados['dtnascto'] = read_from_xml(dependente.dtNascto.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2200_dependente_dados['cpfdep'] = read_from_xml(dependente.cpfDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_dependente_dados['sexodep'] = read_from_xml(dependente.sexoDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_dependente_dados['depirrf'] = read_from_xml(dependente.depIRRF.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_dependente_dados['depsf'] = read_from_xml(dependente.depSF.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_dependente_dados['inctrab'] = read_from_xml(dependente.incTrab.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_dependente_dados['depfinsprev'] = read_from_xml(dependente.depFinsPrev.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2200_dependente = s2200dependente.objects.create(**s2200_dependente_dados)

    if 'trabalhador' in dir(evtAdmissao) and 'aposentadoria' in dir(evtAdmissao.trabalhador):

        for aposentadoria in evtAdmissao.trabalhador.aposentadoria:

            s2200_aposentadoria_dados = {}
            s2200_aposentadoria_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_aposentadoria_dados['trabaposent'] = read_from_xml(aposentadoria.trabAposent.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2200_aposentadoria = s2200aposentadoria.objects.create(**s2200_aposentadoria_dados)

    if 'trabalhador' in dir(evtAdmissao) and 'contato' in dir(evtAdmissao.trabalhador):

        for contato in evtAdmissao.trabalhador.contato:

            s2200_contato_dados = {}
            s2200_contato_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_contato_dados['foneprinc'] = read_from_xml(contato.fonePrinc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_contato_dados['fonealternat'] = read_from_xml(contato.foneAlternat.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_contato_dados['emailprinc'] = read_from_xml(contato.emailPrinc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_contato_dados['emailalternat'] = read_from_xml(contato.emailAlternat.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2200_contato = s2200contato.objects.create(**s2200_contato_dados)

    if 'vinculo' in dir(evtAdmissao) and 'infoRegimeTrab' in dir(evtAdmissao.vinculo) and 'infoCeletista' in dir(evtAdmissao.vinculo.infoRegimeTrab):

        for infoCeletista in evtAdmissao.vinculo.infoRegimeTrab.infoCeletista:

            s2200_infoceletista_dados = {}
            s2200_infoceletista_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_infoceletista_dados['dtadm'] = read_from_xml(infoCeletista.dtAdm.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2200_infoceletista_dados['tpadmissao'] = read_from_xml(infoCeletista.tpAdmissao.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2200_infoceletista_dados['indadmissao'] = read_from_xml(infoCeletista.indAdmissao.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2200_infoceletista_dados['tpregjor'] = read_from_xml(infoCeletista.tpRegJor.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2200_infoceletista_dados['natatividade'] = read_from_xml(infoCeletista.natAtividade.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2200_infoceletista_dados['dtbase'] = read_from_xml(infoCeletista.dtBase.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2200_infoceletista_dados['cnpjsindcategprof'] = read_from_xml(infoCeletista.cnpjSindCategProf.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_infoceletista_dados['opcfgts'] = read_from_xml(infoCeletista.FGTS.opcFGTS.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2200_infoceletista_dados['dtopcfgts'] = read_from_xml(infoCeletista.FGTS.dtOpcFGTS.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            s2200_infoceletista = s2200infoCeletista.objects.create(**s2200_infoceletista_dados)

            if 'trabTemporario' in dir(infoCeletista):

                for trabTemporario in infoCeletista.trabTemporario:

                    s2200_trabtemporario_dados = {}
                    s2200_trabtemporario_dados['s2200_infoceletista_id'] = s2200_infoceletista.id

                    try:
                        s2200_trabtemporario_dados['hipleg'] = read_from_xml(trabTemporario.hipLeg.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_trabtemporario_dados['justcontr'] = read_from_xml(trabTemporario.justContr.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_trabtemporario_dados['tpinclcontr'] = read_from_xml(trabTemporario.tpInclContr.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_trabtemporario_dados['tpinsc'] = read_from_xml(trabTemporario.ideTomadorServ.tpInsc.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_trabtemporario_dados['nrinsc'] = read_from_xml(trabTemporario.ideTomadorServ.nrInsc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2200_trabtemporario = s2200trabTemporario.objects.create(**s2200_trabtemporario_dados)

                    if 'ideTomadorServ' in dir(trabTemporario) and 'ideEstabVinc' in dir(trabTemporario.ideTomadorServ):

                        for ideEstabVinc in trabTemporario.ideTomadorServ.ideEstabVinc:

                            s2200_ideestabvinc_dados = {}
                            s2200_ideestabvinc_dados['s2200_trabtemporario_id'] = s2200_trabtemporario.id
        
                            try:
                                s2200_ideestabvinc_dados['tpinsc'] = read_from_xml(ideEstabVinc.tpInsc.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2200_ideestabvinc_dados['nrinsc'] = read_from_xml(ideEstabVinc.nrInsc.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s2200_ideestabvinc = s2200ideEstabVinc.objects.create(**s2200_ideestabvinc_dados)

                    if 'ideTrabSubstituido' in dir(trabTemporario):

                        for ideTrabSubstituido in trabTemporario.ideTrabSubstituido:

                            s2200_idetrabsubstituido_dados = {}
                            s2200_idetrabsubstituido_dados['s2200_trabtemporario_id'] = s2200_trabtemporario.id
        
                            try:
                                s2200_idetrabsubstituido_dados['cpftrabsubst'] = read_from_xml(ideTrabSubstituido.cpfTrabSubst.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s2200_idetrabsubstituido = s2200ideTrabSubstituido.objects.create(**s2200_idetrabsubstituido_dados)

            if 'aprend' in dir(infoCeletista):

                for aprend in infoCeletista.aprend:

                    s2200_aprend_dados = {}
                    s2200_aprend_dados['s2200_infoceletista_id'] = s2200_infoceletista.id

                    try:
                        s2200_aprend_dados['tpinsc'] = read_from_xml(aprend.tpInsc.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_aprend_dados['nrinsc'] = read_from_xml(aprend.nrInsc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2200_aprend = s2200aprend.objects.create(**s2200_aprend_dados)

    if 'vinculo' in dir(evtAdmissao) and 'infoRegimeTrab' in dir(evtAdmissao.vinculo) and 'infoEstatutario' in dir(evtAdmissao.vinculo.infoRegimeTrab):

        for infoEstatutario in evtAdmissao.vinculo.infoRegimeTrab.infoEstatutario:

            s2200_infoestatutario_dados = {}
            s2200_infoestatutario_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_infoestatutario_dados['indprovim'] = read_from_xml(infoEstatutario.indProvim.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2200_infoestatutario_dados['tpprov'] = read_from_xml(infoEstatutario.tpProv.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2200_infoestatutario_dados['dtnomeacao'] = read_from_xml(infoEstatutario.dtNomeacao.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2200_infoestatutario_dados['dtposse'] = read_from_xml(infoEstatutario.dtPosse.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2200_infoestatutario_dados['dtexercicio'] = read_from_xml(infoEstatutario.dtExercicio.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2200_infoestatutario_dados['dtingsvpub'] = read_from_xml(infoEstatutario.dtIngSvPub.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2200_infoestatutario_dados['tpplanrp'] = read_from_xml(infoEstatutario.tpPlanRP.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2200_infoestatutario_dados['indtetorgps'] = read_from_xml(infoEstatutario.indTetoRGPS.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_infoestatutario_dados['indabonoperm'] = read_from_xml(infoEstatutario.indAbonoPerm.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_infoestatutario_dados['dtiniabono'] = read_from_xml(infoEstatutario.dtIniAbono.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2200_infoestatutario_dados['indparcremun'] = read_from_xml(infoEstatutario.indParcRemun.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_infoestatutario_dados['dtiniparc'] = read_from_xml(infoEstatutario.dtIniParc.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            s2200_infoestatutario = s2200infoEstatutario.objects.create(**s2200_infoestatutario_dados)

            if 'infoDecJud' in dir(infoEstatutario):

                for infoDecJud in infoEstatutario.infoDecJud:

                    s2200_infodecjud_dados = {}
                    s2200_infodecjud_dados['s2200_infoestatutario_id'] = s2200_infoestatutario.id

                    try:
                        s2200_infodecjud_dados['nrprocjud'] = read_from_xml(infoDecJud.nrProcJud.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2200_infodecjud = s2200infoDecJud.objects.create(**s2200_infodecjud_dados)

    if 'vinculo' in dir(evtAdmissao) and 'infoContrato' in dir(evtAdmissao.vinculo) and 'localTrabalho' in dir(evtAdmissao.vinculo.infoContrato) and 'localTrabGeral' in dir(evtAdmissao.vinculo.infoContrato.localTrabalho):

        for localTrabGeral in evtAdmissao.vinculo.infoContrato.localTrabalho.localTrabGeral:

            s2200_localtrabgeral_dados = {}
            s2200_localtrabgeral_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_localtrabgeral_dados['tpinsc'] = read_from_xml(localTrabGeral.tpInsc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2200_localtrabgeral_dados['nrinsc'] = read_from_xml(localTrabGeral.nrInsc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_localtrabgeral_dados['desccomp'] = read_from_xml(localTrabGeral.descComp.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2200_localtrabgeral = s2200localTrabGeral.objects.create(**s2200_localtrabgeral_dados)

    if 'vinculo' in dir(evtAdmissao) and 'infoContrato' in dir(evtAdmissao.vinculo) and 'localTrabalho' in dir(evtAdmissao.vinculo.infoContrato) and 'localTrabDom' in dir(evtAdmissao.vinculo.infoContrato.localTrabalho):

        for localTrabDom in evtAdmissao.vinculo.infoContrato.localTrabalho.localTrabDom:

            s2200_localtrabdom_dados = {}
            s2200_localtrabdom_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_localtrabdom_dados['tplograd'] = read_from_xml(localTrabDom.tpLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_localtrabdom_dados['dsclograd'] = read_from_xml(localTrabDom.dscLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_localtrabdom_dados['nrlograd'] = read_from_xml(localTrabDom.nrLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_localtrabdom_dados['complemento'] = read_from_xml(localTrabDom.complemento.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_localtrabdom_dados['bairro'] = read_from_xml(localTrabDom.bairro.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_localtrabdom_dados['cep'] = read_from_xml(localTrabDom.cep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_localtrabdom_dados['codmunic'] = read_from_xml(localTrabDom.codMunic.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2200_localtrabdom_dados['uf'] = read_from_xml(localTrabDom.uf.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2200_localtrabdom = s2200localTrabDom.objects.create(**s2200_localtrabdom_dados)

    if 'vinculo' in dir(evtAdmissao) and 'infoContrato' in dir(evtAdmissao.vinculo) and 'horContratual' in dir(evtAdmissao.vinculo.infoContrato):

        for horContratual in evtAdmissao.vinculo.infoContrato.horContratual:

            s2200_horcontratual_dados = {}
            s2200_horcontratual_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_horcontratual_dados['qtdhrssem'] = read_from_xml(horContratual.qtdHrsSem.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            try:
                s2200_horcontratual_dados['tpjornada'] = read_from_xml(horContratual.tpJornada.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2200_horcontratual_dados['dsctpjorn'] = read_from_xml(horContratual.dscTpJorn.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_horcontratual_dados['tmpparc'] = read_from_xml(horContratual.tmpParc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s2200_horcontratual = s2200horContratual.objects.create(**s2200_horcontratual_dados)

            if 'horario' in dir(horContratual):

                for horario in horContratual.horario:

                    s2200_horario_dados = {}
                    s2200_horario_dados['s2200_horcontratual_id'] = s2200_horcontratual.id

                    try:
                        s2200_horario_dados['dia'] = read_from_xml(horario.dia.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2200_horario_dados['codhorcontrat'] = read_from_xml(horario.codHorContrat.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2200_horario = s2200horario.objects.create(**s2200_horario_dados)

    if 'vinculo' in dir(evtAdmissao) and 'infoContrato' in dir(evtAdmissao.vinculo) and 'filiacaoSindical' in dir(evtAdmissao.vinculo.infoContrato):

        for filiacaoSindical in evtAdmissao.vinculo.infoContrato.filiacaoSindical:

            s2200_filiacaosindical_dados = {}
            s2200_filiacaosindical_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_filiacaosindical_dados['cnpjsindtrab'] = read_from_xml(filiacaoSindical.cnpjSindTrab.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2200_filiacaosindical = s2200filiacaoSindical.objects.create(**s2200_filiacaosindical_dados)

    if 'vinculo' in dir(evtAdmissao) and 'infoContrato' in dir(evtAdmissao.vinculo) and 'alvaraJudicial' in dir(evtAdmissao.vinculo.infoContrato):

        for alvaraJudicial in evtAdmissao.vinculo.infoContrato.alvaraJudicial:

            s2200_alvarajudicial_dados = {}
            s2200_alvarajudicial_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_alvarajudicial_dados['nrprocjud'] = read_from_xml(alvaraJudicial.nrProcJud.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2200_alvarajudicial = s2200alvaraJudicial.objects.create(**s2200_alvarajudicial_dados)

    if 'vinculo' in dir(evtAdmissao) and 'infoContrato' in dir(evtAdmissao.vinculo) and 'observacoes' in dir(evtAdmissao.vinculo.infoContrato):

        for observacoes in evtAdmissao.vinculo.infoContrato.observacoes:

            s2200_observacoes_dados = {}
            s2200_observacoes_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_observacoes_dados['observacao'] = read_from_xml(observacoes.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2200_observacoes = s2200observacoes.objects.create(**s2200_observacoes_dados)

    if 'vinculo' in dir(evtAdmissao) and 'sucessaoVinc' in dir(evtAdmissao.vinculo):

        for sucessaoVinc in evtAdmissao.vinculo.sucessaoVinc:

            s2200_sucessaovinc_dados = {}
            s2200_sucessaovinc_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_sucessaovinc_dados['tpinscant'] = read_from_xml(sucessaoVinc.tpInscAnt.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2200_sucessaovinc_dados['cnpjempregant'] = read_from_xml(sucessaoVinc.cnpjEmpregAnt.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_sucessaovinc_dados['matricant'] = read_from_xml(sucessaoVinc.matricAnt.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_sucessaovinc_dados['dttransf'] = read_from_xml(sucessaoVinc.dtTransf.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2200_sucessaovinc_dados['observacao'] = read_from_xml(sucessaoVinc.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2200_sucessaovinc = s2200sucessaoVinc.objects.create(**s2200_sucessaovinc_dados)

    if 'vinculo' in dir(evtAdmissao) and 'transfDom' in dir(evtAdmissao.vinculo):

        for transfDom in evtAdmissao.vinculo.transfDom:

            s2200_transfdom_dados = {}
            s2200_transfdom_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_transfdom_dados['cpfsubstituido'] = read_from_xml(transfDom.cpfSubstituido.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_transfdom_dados['matricant'] = read_from_xml(transfDom.matricAnt.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_transfdom_dados['dttransf'] = read_from_xml(transfDom.dtTransf.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            s2200_transfdom = s2200transfDom.objects.create(**s2200_transfdom_dados)

    if 'vinculo' in dir(evtAdmissao) and 'mudancaCPF' in dir(evtAdmissao.vinculo):

        for mudancaCPF in evtAdmissao.vinculo.mudancaCPF:

            s2200_mudancacpf_dados = {}
            s2200_mudancacpf_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_mudancacpf_dados['cpfant'] = read_from_xml(mudancaCPF.cpfAnt.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_mudancacpf_dados['matricant'] = read_from_xml(mudancaCPF.matricAnt.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2200_mudancacpf_dados['dtaltcpf'] = read_from_xml(mudancaCPF.dtAltCPF.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2200_mudancacpf_dados['observacao'] = read_from_xml(mudancaCPF.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2200_mudancacpf = s2200mudancaCPF.objects.create(**s2200_mudancacpf_dados)

    if 'vinculo' in dir(evtAdmissao) and 'afastamento' in dir(evtAdmissao.vinculo):

        for afastamento in evtAdmissao.vinculo.afastamento:

            s2200_afastamento_dados = {}
            s2200_afastamento_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_afastamento_dados['dtiniafast'] = read_from_xml(afastamento.dtIniAfast.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2200_afastamento_dados['codmotafast'] = read_from_xml(afastamento.codMotAfast.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2200_afastamento = s2200afastamento.objects.create(**s2200_afastamento_dados)

    if 'vinculo' in dir(evtAdmissao) and 'desligamento' in dir(evtAdmissao.vinculo):

        for desligamento in evtAdmissao.vinculo.desligamento:

            s2200_desligamento_dados = {}
            s2200_desligamento_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_desligamento_dados['dtdeslig'] = read_from_xml(desligamento.dtDeslig.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            s2200_desligamento = s2200desligamento.objects.create(**s2200_desligamento_dados)

    if 'vinculo' in dir(evtAdmissao) and 'cessao' in dir(evtAdmissao.vinculo):

        for cessao in evtAdmissao.vinculo.cessao:

            s2200_cessao_dados = {}
            s2200_cessao_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id

            try:
                s2200_cessao_dados['dtinicessao'] = read_from_xml(cessao.dtIniCessao.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            s2200_cessao = s2200cessao.objects.create(**s2200_cessao_dados)
    s2200_evtadmissao_dados['evento'] = 's2200'
    s2200_evtadmissao_dados['id'] = s2200_evtadmissao.id
    s2200_evtadmissao_dados['identidade_evento'] = doc.eSocial.evtAdmissao['Id']

    from emensageriapro.esocial.views.s2200_evtadmissao_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2200_evtadmissao.id)

    return s2200_evtadmissao_dados