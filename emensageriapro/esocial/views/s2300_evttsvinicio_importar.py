#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2300.models import *



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

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_s2300_evttsvinicio_obj(request, doc, status, validar, arquivo)
    novo_arquivo = arquivo.replace('/aguardando/', '/processado/')
    s2300evtTSVInicio.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s2300_evttsvinicio_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2300_evttsvinicio_dados = {}
    s2300_evttsvinicio_dados['status'] = status
    s2300_evttsvinicio_dados['arquivo_original'] = 1
    if arquivo:
        s2300_evttsvinicio_dados['arquivo'] = arquivo
    s2300_evttsvinicio_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2300_evttsvinicio_dados['identidade'] = doc.eSocial.evtTSVInicio['Id']
    evtTSVInicio = doc.eSocial.evtTSVInicio

    try:
        s2300_evttsvinicio_dados['indretif'] = evtTSVInicio.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['nrrecibo'] = evtTSVInicio.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['tpamb'] = evtTSVInicio.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['procemi'] = evtTSVInicio.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['verproc'] = evtTSVInicio.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['tpinsc'] = evtTSVInicio.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['nrinsc'] = evtTSVInicio.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['cpftrab'] = evtTSVInicio.trabalhador.cpfTrab.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['nistrab'] = evtTSVInicio.trabalhador.nisTrab.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['nmtrab'] = evtTSVInicio.trabalhador.nmTrab.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['sexo'] = evtTSVInicio.trabalhador.sexo.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['racacor'] = evtTSVInicio.trabalhador.racaCor.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['estciv'] = evtTSVInicio.trabalhador.estCiv.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['grauinstr'] = evtTSVInicio.trabalhador.grauInstr.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['nmsoc'] = evtTSVInicio.trabalhador.nmSoc.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['dtnascto'] = evtTSVInicio.trabalhador.nascimento.dtNascto.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['codmunic'] = evtTSVInicio.trabalhador.nascimento.codMunic.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['uf'] = evtTSVInicio.trabalhador.nascimento.uf.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['paisnascto'] = evtTSVInicio.trabalhador.nascimento.paisNascto.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['paisnac'] = evtTSVInicio.trabalhador.nascimento.paisNac.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['nmmae'] = evtTSVInicio.trabalhador.nascimento.nmMae.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['nmpai'] = evtTSVInicio.trabalhador.nascimento.nmPai.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['cadini'] = evtTSVInicio.infoTSVInicio.cadIni.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['codcateg'] = evtTSVInicio.infoTSVInicio.codCateg.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['dtinicio'] = evtTSVInicio.infoTSVInicio.dtInicio.cdata
    except AttributeError:
        pass

    try:
        s2300_evttsvinicio_dados['natatividade'] = evtTSVInicio.infoTSVInicio.natAtividade.cdata
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
                        s2300_ctps_dados['nrctps'] = CTPS.nrCtps.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_ctps_dados['seriectps'] = CTPS.serieCtps.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_ctps_dados['ufctps'] = CTPS.ufCtps.cdata
                    except AttributeError:
                        pass

                    s2300_ctps = s2300CTPS.objects.create(**s2300_ctps_dados)

            if 'RIC' in dir(documentos):

                for RIC in documentos.RIC:

                    s2300_ric_dados = {}
                    s2300_ric_dados['s2300_documentos_id'] = s2300_documentos.id

                    try:
                        s2300_ric_dados['nrric'] = RIC.nrRic.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_ric_dados['orgaoemissor'] = RIC.orgaoEmissor.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_ric_dados['dtexped'] = RIC.dtExped.cdata
                    except AttributeError:
                        pass

                    s2300_ric = s2300RIC.objects.create(**s2300_ric_dados)

            if 'RG' in dir(documentos):

                for RG in documentos.RG:

                    s2300_rg_dados = {}
                    s2300_rg_dados['s2300_documentos_id'] = s2300_documentos.id

                    try:
                        s2300_rg_dados['nrrg'] = RG.nrRg.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_rg_dados['orgaoemissor'] = RG.orgaoEmissor.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_rg_dados['dtexped'] = RG.dtExped.cdata
                    except AttributeError:
                        pass

                    s2300_rg = s2300RG.objects.create(**s2300_rg_dados)

            if 'RNE' in dir(documentos):

                for RNE in documentos.RNE:

                    s2300_rne_dados = {}
                    s2300_rne_dados['s2300_documentos_id'] = s2300_documentos.id

                    try:
                        s2300_rne_dados['nrrne'] = RNE.nrRne.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_rne_dados['orgaoemissor'] = RNE.orgaoEmissor.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_rne_dados['dtexped'] = RNE.dtExped.cdata
                    except AttributeError:
                        pass

                    s2300_rne = s2300RNE.objects.create(**s2300_rne_dados)

            if 'OC' in dir(documentos):

                for OC in documentos.OC:

                    s2300_oc_dados = {}
                    s2300_oc_dados['s2300_documentos_id'] = s2300_documentos.id

                    try:
                        s2300_oc_dados['nroc'] = OC.nrOc.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_oc_dados['orgaoemissor'] = OC.orgaoEmissor.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_oc_dados['dtexped'] = OC.dtExped.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_oc_dados['dtvalid'] = OC.dtValid.cdata
                    except AttributeError:
                        pass

                    s2300_oc = s2300OC.objects.create(**s2300_oc_dados)

            if 'CNH' in dir(documentos):

                for CNH in documentos.CNH:

                    s2300_cnh_dados = {}
                    s2300_cnh_dados['s2300_documentos_id'] = s2300_documentos.id

                    try:
                        s2300_cnh_dados['nrregcnh'] = CNH.nrRegCnh.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_cnh_dados['dtexped'] = CNH.dtExped.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_cnh_dados['ufcnh'] = CNH.ufCnh.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_cnh_dados['dtvalid'] = CNH.dtValid.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_cnh_dados['dtprihab'] = CNH.dtPriHab.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_cnh_dados['categoriacnh'] = CNH.categoriaCnh.cdata
                    except AttributeError:
                        pass

                    s2300_cnh = s2300CNH.objects.create(**s2300_cnh_dados)

    if 'trabalhador' in dir(evtTSVInicio) and 'endereco' in dir(evtTSVInicio.trabalhador) and 'brasil' in dir(evtTSVInicio.trabalhador.endereco):

        for brasil in evtTSVInicio.trabalhador.endereco.brasil:

            s2300_brasil_dados = {}
            s2300_brasil_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_brasil_dados['tplograd'] = brasil.tpLograd.cdata
            except AttributeError:
                pass

            try:
                s2300_brasil_dados['dsclograd'] = brasil.dscLograd.cdata
            except AttributeError:
                pass

            try:
                s2300_brasil_dados['nrlograd'] = brasil.nrLograd.cdata
            except AttributeError:
                pass

            try:
                s2300_brasil_dados['complemento'] = brasil.complemento.cdata
            except AttributeError:
                pass

            try:
                s2300_brasil_dados['bairro'] = brasil.bairro.cdata
            except AttributeError:
                pass

            try:
                s2300_brasil_dados['cep'] = brasil.cep.cdata
            except AttributeError:
                pass

            try:
                s2300_brasil_dados['codmunic'] = brasil.codMunic.cdata
            except AttributeError:
                pass

            try:
                s2300_brasil_dados['uf'] = brasil.uf.cdata
            except AttributeError:
                pass

            s2300_brasil = s2300brasil.objects.create(**s2300_brasil_dados)

    if 'trabalhador' in dir(evtTSVInicio) and 'endereco' in dir(evtTSVInicio.trabalhador) and 'exterior' in dir(evtTSVInicio.trabalhador.endereco):

        for exterior in evtTSVInicio.trabalhador.endereco.exterior:

            s2300_exterior_dados = {}
            s2300_exterior_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_exterior_dados['paisresid'] = exterior.paisResid.cdata
            except AttributeError:
                pass

            try:
                s2300_exterior_dados['dsclograd'] = exterior.dscLograd.cdata
            except AttributeError:
                pass

            try:
                s2300_exterior_dados['nrlograd'] = exterior.nrLograd.cdata
            except AttributeError:
                pass

            try:
                s2300_exterior_dados['complemento'] = exterior.complemento.cdata
            except AttributeError:
                pass

            try:
                s2300_exterior_dados['bairro'] = exterior.bairro.cdata
            except AttributeError:
                pass

            try:
                s2300_exterior_dados['nmcid'] = exterior.nmCid.cdata
            except AttributeError:
                pass

            try:
                s2300_exterior_dados['codpostal'] = exterior.codPostal.cdata
            except AttributeError:
                pass

            s2300_exterior = s2300exterior.objects.create(**s2300_exterior_dados)

    if 'trabalhador' in dir(evtTSVInicio) and 'trabEstrangeiro' in dir(evtTSVInicio.trabalhador):

        for trabEstrangeiro in evtTSVInicio.trabalhador.trabEstrangeiro:

            s2300_trabestrangeiro_dados = {}
            s2300_trabestrangeiro_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_trabestrangeiro_dados['dtchegada'] = trabEstrangeiro.dtChegada.cdata
            except AttributeError:
                pass

            try:
                s2300_trabestrangeiro_dados['classtrabestrang'] = trabEstrangeiro.classTrabEstrang.cdata
            except AttributeError:
                pass

            try:
                s2300_trabestrangeiro_dados['casadobr'] = trabEstrangeiro.casadoBr.cdata
            except AttributeError:
                pass

            try:
                s2300_trabestrangeiro_dados['filhosbr'] = trabEstrangeiro.filhosBr.cdata
            except AttributeError:
                pass

            s2300_trabestrangeiro = s2300trabEstrangeiro.objects.create(**s2300_trabestrangeiro_dados)

    if 'trabalhador' in dir(evtTSVInicio) and 'infoDeficiencia' in dir(evtTSVInicio.trabalhador):

        for infoDeficiencia in evtTSVInicio.trabalhador.infoDeficiencia:

            s2300_infodeficiencia_dados = {}
            s2300_infodeficiencia_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_infodeficiencia_dados['deffisica'] = infoDeficiencia.defFisica.cdata
            except AttributeError:
                pass

            try:
                s2300_infodeficiencia_dados['defvisual'] = infoDeficiencia.defVisual.cdata
            except AttributeError:
                pass

            try:
                s2300_infodeficiencia_dados['defauditiva'] = infoDeficiencia.defAuditiva.cdata
            except AttributeError:
                pass

            try:
                s2300_infodeficiencia_dados['defmental'] = infoDeficiencia.defMental.cdata
            except AttributeError:
                pass

            try:
                s2300_infodeficiencia_dados['defintelectual'] = infoDeficiencia.defIntelectual.cdata
            except AttributeError:
                pass

            try:
                s2300_infodeficiencia_dados['reabreadap'] = infoDeficiencia.reabReadap.cdata
            except AttributeError:
                pass

            try:
                s2300_infodeficiencia_dados['observacao'] = infoDeficiencia.observacao.cdata
            except AttributeError:
                pass

            s2300_infodeficiencia = s2300infoDeficiencia.objects.create(**s2300_infodeficiencia_dados)

    if 'trabalhador' in dir(evtTSVInicio) and 'dependente' in dir(evtTSVInicio.trabalhador):

        for dependente in evtTSVInicio.trabalhador.dependente:

            s2300_dependente_dados = {}
            s2300_dependente_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_dependente_dados['tpdep'] = dependente.tpDep.cdata
            except AttributeError:
                pass

            try:
                s2300_dependente_dados['nmdep'] = dependente.nmDep.cdata
            except AttributeError:
                pass

            try:
                s2300_dependente_dados['dtnascto'] = dependente.dtNascto.cdata
            except AttributeError:
                pass

            try:
                s2300_dependente_dados['cpfdep'] = dependente.cpfDep.cdata
            except AttributeError:
                pass

            try:
                s2300_dependente_dados['sexodep'] = dependente.sexoDep.cdata
            except AttributeError:
                pass

            try:
                s2300_dependente_dados['depirrf'] = dependente.depIRRF.cdata
            except AttributeError:
                pass

            try:
                s2300_dependente_dados['depsf'] = dependente.depSF.cdata
            except AttributeError:
                pass

            try:
                s2300_dependente_dados['inctrab'] = dependente.incTrab.cdata
            except AttributeError:
                pass

            try:
                s2300_dependente_dados['depfinsprev'] = dependente.depFinsPrev.cdata
            except AttributeError:
                pass

            s2300_dependente = s2300dependente.objects.create(**s2300_dependente_dados)

    if 'trabalhador' in dir(evtTSVInicio) and 'contato' in dir(evtTSVInicio.trabalhador):

        for contato in evtTSVInicio.trabalhador.contato:

            s2300_contato_dados = {}
            s2300_contato_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_contato_dados['foneprinc'] = contato.fonePrinc.cdata
            except AttributeError:
                pass

            try:
                s2300_contato_dados['fonealternat'] = contato.foneAlternat.cdata
            except AttributeError:
                pass

            try:
                s2300_contato_dados['emailprinc'] = contato.emailPrinc.cdata
            except AttributeError:
                pass

            try:
                s2300_contato_dados['emailalternat'] = contato.emailAlternat.cdata
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
                        s2300_cargofuncao_dados['codcargo'] = cargoFuncao.codCargo.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_cargofuncao_dados['codfuncao'] = cargoFuncao.codFuncao.cdata
                    except AttributeError:
                        pass

                    s2300_cargofuncao = s2300cargoFuncao.objects.create(**s2300_cargofuncao_dados)

            if 'remuneracao' in dir(infoComplementares):

                for remuneracao in infoComplementares.remuneracao:

                    s2300_remuneracao_dados = {}
                    s2300_remuneracao_dados['s2300_infocomplementares_id'] = s2300_infocomplementares.id

                    try:
                        s2300_remuneracao_dados['vrsalfx'] = remuneracao.vrSalFx.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_remuneracao_dados['undsalfixo'] = remuneracao.undSalFixo.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_remuneracao_dados['dscsalvar'] = remuneracao.dscSalVar.cdata
                    except AttributeError:
                        pass

                    s2300_remuneracao = s2300remuneracao.objects.create(**s2300_remuneracao_dados)

            if 'fgts' in dir(infoComplementares):

                for fgts in infoComplementares.fgts:

                    s2300_fgts_dados = {}
                    s2300_fgts_dados['s2300_infocomplementares_id'] = s2300_infocomplementares.id

                    try:
                        s2300_fgts_dados['opcfgts'] = fgts.opcFGTS.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_fgts_dados['dtopcfgts'] = fgts.dtOpcFGTS.cdata
                    except AttributeError:
                        pass

                    s2300_fgts = s2300fgts.objects.create(**s2300_fgts_dados)

            if 'infoDirigenteSindical' in dir(infoComplementares):

                for infoDirigenteSindical in infoComplementares.infoDirigenteSindical:

                    s2300_infodirigentesindical_dados = {}
                    s2300_infodirigentesindical_dados['s2300_infocomplementares_id'] = s2300_infocomplementares.id

                    try:
                        s2300_infodirigentesindical_dados['categorig'] = infoDirigenteSindical.categOrig.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infodirigentesindical_dados['cnpjorigem'] = infoDirigenteSindical.cnpjOrigem.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infodirigentesindical_dados['dtadmorig'] = infoDirigenteSindical.dtAdmOrig.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infodirigentesindical_dados['matricorig'] = infoDirigenteSindical.matricOrig.cdata
                    except AttributeError:
                        pass

                    s2300_infodirigentesindical = s2300infoDirigenteSindical.objects.create(**s2300_infodirigentesindical_dados)

            if 'infoTrabCedido' in dir(infoComplementares):

                for infoTrabCedido in infoComplementares.infoTrabCedido:

                    s2300_infotrabcedido_dados = {}
                    s2300_infotrabcedido_dados['s2300_infocomplementares_id'] = s2300_infocomplementares.id

                    try:
                        s2300_infotrabcedido_dados['categorig'] = infoTrabCedido.categOrig.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infotrabcedido_dados['cnpjcednt'] = infoTrabCedido.cnpjCednt.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infotrabcedido_dados['matricced'] = infoTrabCedido.matricCed.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infotrabcedido_dados['dtadmced'] = infoTrabCedido.dtAdmCed.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infotrabcedido_dados['tpregtrab'] = infoTrabCedido.tpRegTrab.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infotrabcedido_dados['tpregprev'] = infoTrabCedido.tpRegPrev.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infotrabcedido_dados['infonus'] = infoTrabCedido.infOnus.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infotrabcedido_dados['indremuncargo'] = infoTrabCedido.indRemunCargo.cdata
                    except AttributeError:
                        pass

                    s2300_infotrabcedido = s2300infoTrabCedido.objects.create(**s2300_infotrabcedido_dados)

            if 'infoEstagiario' in dir(infoComplementares):

                for infoEstagiario in infoComplementares.infoEstagiario:

                    s2300_infoestagiario_dados = {}
                    s2300_infoestagiario_dados['s2300_infocomplementares_id'] = s2300_infocomplementares.id

                    try:
                        s2300_infoestagiario_dados['natestagio'] = infoEstagiario.natEstagio.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['nivestagio'] = infoEstagiario.nivEstagio.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['areaatuacao'] = infoEstagiario.areaAtuacao.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['nrapol'] = infoEstagiario.nrApol.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['vlrbolsa'] = infoEstagiario.vlrBolsa.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['dtprevterm'] = infoEstagiario.dtPrevTerm.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['cnpjinstensino'] = infoEstagiario.instEnsino.cnpjInstEnsino.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['nmrazao'] = infoEstagiario.instEnsino.nmRazao.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['dsclograd'] = infoEstagiario.instEnsino.dscLograd.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['nrlograd'] = infoEstagiario.instEnsino.nrLograd.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['bairro'] = infoEstagiario.instEnsino.bairro.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['cep'] = infoEstagiario.instEnsino.cep.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['codmunic'] = infoEstagiario.instEnsino.codMunic.cdata
                    except AttributeError:
                        pass

                    try:
                        s2300_infoestagiario_dados['uf'] = infoEstagiario.instEnsino.uf.cdata
                    except AttributeError:
                        pass

                    s2300_infoestagiario = s2300infoEstagiario.objects.create(**s2300_infoestagiario_dados)

                    if 'ageIntegracao' in dir(infoEstagiario):

                        for ageIntegracao in infoEstagiario.ageIntegracao:

                            s2300_ageintegracao_dados = {}
                            s2300_ageintegracao_dados['s2300_infoestagiario_id'] = s2300_infoestagiario.id
        
                            try:
                                s2300_ageintegracao_dados['cnpjagntinteg'] = ageIntegracao.cnpjAgntInteg.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2300_ageintegracao_dados['nmrazao'] = ageIntegracao.nmRazao.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2300_ageintegracao_dados['dsclograd'] = ageIntegracao.dscLograd.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2300_ageintegracao_dados['nrlograd'] = ageIntegracao.nrLograd.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2300_ageintegracao_dados['bairro'] = ageIntegracao.bairro.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2300_ageintegracao_dados['cep'] = ageIntegracao.cep.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2300_ageintegracao_dados['codmunic'] = ageIntegracao.codMunic.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2300_ageintegracao_dados['uf'] = ageIntegracao.uf.cdata
                            except AttributeError:
                                pass

                            s2300_ageintegracao = s2300ageIntegracao.objects.create(**s2300_ageintegracao_dados)

                    if 'supervisorEstagio' in dir(infoEstagiario):

                        for supervisorEstagio in infoEstagiario.supervisorEstagio:

                            s2300_supervisorestagio_dados = {}
                            s2300_supervisorestagio_dados['s2300_infoestagiario_id'] = s2300_infoestagiario.id
        
                            try:
                                s2300_supervisorestagio_dados['cpfsupervisor'] = supervisorEstagio.cpfSupervisor.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2300_supervisorestagio_dados['nmsuperv'] = supervisorEstagio.nmSuperv.cdata
                            except AttributeError:
                                pass

                            s2300_supervisorestagio = s2300supervisorEstagio.objects.create(**s2300_supervisorestagio_dados)

    if 'infoTSVInicio' in dir(evtTSVInicio) and 'mudancaCPF' in dir(evtTSVInicio.infoTSVInicio):

        for mudancaCPF in evtTSVInicio.infoTSVInicio.mudancaCPF:

            s2300_mudancacpf_dados = {}
            s2300_mudancacpf_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_mudancacpf_dados['cpfant'] = mudancaCPF.cpfAnt.cdata
            except AttributeError:
                pass

            try:
                s2300_mudancacpf_dados['dtaltcpf'] = mudancaCPF.dtAltCPF.cdata
            except AttributeError:
                pass

            try:
                s2300_mudancacpf_dados['observacao'] = mudancaCPF.observacao.cdata
            except AttributeError:
                pass

            s2300_mudancacpf = s2300mudancaCPF.objects.create(**s2300_mudancacpf_dados)

    if 'infoTSVInicio' in dir(evtTSVInicio) and 'afastamento' in dir(evtTSVInicio.infoTSVInicio):

        for afastamento in evtTSVInicio.infoTSVInicio.afastamento:

            s2300_afastamento_dados = {}
            s2300_afastamento_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_afastamento_dados['dtiniafast'] = afastamento.dtIniAfast.cdata
            except AttributeError:
                pass

            try:
                s2300_afastamento_dados['codmotafast'] = afastamento.codMotAfast.cdata
            except AttributeError:
                pass

            s2300_afastamento = s2300afastamento.objects.create(**s2300_afastamento_dados)

    if 'infoTSVInicio' in dir(evtTSVInicio) and 'termino' in dir(evtTSVInicio.infoTSVInicio):

        for termino in evtTSVInicio.infoTSVInicio.termino:

            s2300_termino_dados = {}
            s2300_termino_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio.id

            try:
                s2300_termino_dados['dtterm'] = termino.dtTerm.cdata
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