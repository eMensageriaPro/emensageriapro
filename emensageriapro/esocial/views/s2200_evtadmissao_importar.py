#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2200.models import *



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
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2200_evtadmissao_obj(request, doc, status, validar)

    s2200evtAdmissao.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s2200_evtadmissao_obj(request, doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2200_evtadmissao_dados = {}
    s2200_evtadmissao_dados['status'] = status
    s2200_evtadmissao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2200_evtadmissao_dados['identidade'] = doc.eSocial.evtAdmissao['Id']
    evtAdmissao = doc.eSocial.evtAdmissao
    
    try:
        s2200_evtadmissao_dados['indretif'] = evtAdmissao.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['nrrecibo'] = evtAdmissao.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['tpamb'] = evtAdmissao.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['procemi'] = evtAdmissao.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['verproc'] = evtAdmissao.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['tpinsc'] = evtAdmissao.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['nrinsc'] = evtAdmissao.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['cpftrab'] = evtAdmissao.trabalhador.cpfTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['nistrab'] = evtAdmissao.trabalhador.nisTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['nmtrab'] = evtAdmissao.trabalhador.nmTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['sexo'] = evtAdmissao.trabalhador.sexo.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['racacor'] = evtAdmissao.trabalhador.racaCor.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['estciv'] = evtAdmissao.trabalhador.estCiv.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['grauinstr'] = evtAdmissao.trabalhador.grauInstr.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['indpriempr'] = evtAdmissao.trabalhador.indPriEmpr.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['nmsoc'] = evtAdmissao.trabalhador.nmSoc.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['dtnascto'] = evtAdmissao.trabalhador.nascimento.dtNascto.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['codmunic'] = evtAdmissao.trabalhador.nascimento.codMunic.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['uf'] = evtAdmissao.trabalhador.nascimento.uf.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['paisnascto'] = evtAdmissao.trabalhador.nascimento.paisNascto.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['paisnac'] = evtAdmissao.trabalhador.nascimento.paisNac.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['nmmae'] = evtAdmissao.trabalhador.nascimento.nmMae.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['nmpai'] = evtAdmissao.trabalhador.nascimento.nmPai.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['matricula'] = evtAdmissao.vinculo.matricula.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['tpregtrab'] = evtAdmissao.vinculo.tpRegTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['tpregprev'] = evtAdmissao.vinculo.tpRegPrev.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['nrrecinfprelim'] = evtAdmissao.vinculo.nrRecInfPrelim.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['cadini'] = evtAdmissao.vinculo.cadIni.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['codcargo'] = evtAdmissao.vinculo.infoContrato.codCargo.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['dtingrcargo'] = evtAdmissao.vinculo.infoContrato.dtIngrCargo.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['codfuncao'] = evtAdmissao.vinculo.infoContrato.codFuncao.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['codcateg'] = evtAdmissao.vinculo.infoContrato.codCateg.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['codcarreira'] = evtAdmissao.vinculo.infoContrato.codCarreira.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['dtingrcarr'] = evtAdmissao.vinculo.infoContrato.dtIngrCarr.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['vrsalfx'] = evtAdmissao.vinculo.infoContrato.remuneracao.vrSalFx.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['undsalfixo'] = evtAdmissao.vinculo.infoContrato.remuneracao.undSalFixo.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['dscsalvar'] = evtAdmissao.vinculo.infoContrato.remuneracao.dscSalVar.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['tpcontr'] = evtAdmissao.vinculo.infoContrato.duracao.tpContr.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['dtterm'] = evtAdmissao.vinculo.infoContrato.duracao.dtTerm.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['clauassec'] = evtAdmissao.vinculo.infoContrato.duracao.clauAssec.cdata
    except AttributeError: 
        pass
    
    try:
        s2200_evtadmissao_dados['objdet'] = evtAdmissao.vinculo.infoContrato.duracao.objDet.cdata
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
                        s2200_ctps_dados['nrctps'] = CTPS.nrCtps.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_ctps_dados['seriectps'] = CTPS.serieCtps.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_ctps_dados['ufctps'] = CTPS.ufCtps.cdata
                    except AttributeError: 
                        pass
            
                    s2200_ctps = s2200CTPS.objects.create(**s2200_ctps_dados)
            
            if 'RIC' in dir(documentos):
            
                for RIC in documentos.RIC:
            
                    s2200_ric_dados = {}
                    s2200_ric_dados['s2200_documentos_id'] = s2200_documentos.id
                    
                    try:
                        s2200_ric_dados['nrric'] = RIC.nrRic.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_ric_dados['orgaoemissor'] = RIC.orgaoEmissor.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_ric_dados['dtexped'] = RIC.dtExped.cdata
                    except AttributeError: 
                        pass
            
                    s2200_ric = s2200RIC.objects.create(**s2200_ric_dados)
            
            if 'RG' in dir(documentos):
            
                for RG in documentos.RG:
            
                    s2200_rg_dados = {}
                    s2200_rg_dados['s2200_documentos_id'] = s2200_documentos.id
                    
                    try:
                        s2200_rg_dados['nrrg'] = RG.nrRg.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_rg_dados['orgaoemissor'] = RG.orgaoEmissor.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_rg_dados['dtexped'] = RG.dtExped.cdata
                    except AttributeError: 
                        pass
            
                    s2200_rg = s2200RG.objects.create(**s2200_rg_dados)
            
            if 'RNE' in dir(documentos):
            
                for RNE in documentos.RNE:
            
                    s2200_rne_dados = {}
                    s2200_rne_dados['s2200_documentos_id'] = s2200_documentos.id
                    
                    try:
                        s2200_rne_dados['nrrne'] = RNE.nrRne.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_rne_dados['orgaoemissor'] = RNE.orgaoEmissor.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_rne_dados['dtexped'] = RNE.dtExped.cdata
                    except AttributeError: 
                        pass
            
                    s2200_rne = s2200RNE.objects.create(**s2200_rne_dados)
            
            if 'OC' in dir(documentos):
            
                for OC in documentos.OC:
            
                    s2200_oc_dados = {}
                    s2200_oc_dados['s2200_documentos_id'] = s2200_documentos.id
                    
                    try:
                        s2200_oc_dados['nroc'] = OC.nrOc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_oc_dados['orgaoemissor'] = OC.orgaoEmissor.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_oc_dados['dtexped'] = OC.dtExped.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_oc_dados['dtvalid'] = OC.dtValid.cdata
                    except AttributeError: 
                        pass
            
                    s2200_oc = s2200OC.objects.create(**s2200_oc_dados)
            
            if 'CNH' in dir(documentos):
            
                for CNH in documentos.CNH:
            
                    s2200_cnh_dados = {}
                    s2200_cnh_dados['s2200_documentos_id'] = s2200_documentos.id
                    
                    try:
                        s2200_cnh_dados['nrregcnh'] = CNH.nrRegCnh.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_cnh_dados['dtexped'] = CNH.dtExped.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_cnh_dados['ufcnh'] = CNH.ufCnh.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_cnh_dados['dtvalid'] = CNH.dtValid.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_cnh_dados['dtprihab'] = CNH.dtPriHab.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_cnh_dados['categoriacnh'] = CNH.categoriaCnh.cdata
                    except AttributeError: 
                        pass
            
                    s2200_cnh = s2200CNH.objects.create(**s2200_cnh_dados)
    
    if 'trabalhador' in dir(evtAdmissao) and 'endereco' in dir(evtAdmissao.trabalhador) and 'brasil' in dir(evtAdmissao.trabalhador.endereco):
    
        for brasil in evtAdmissao.trabalhador.endereco.brasil:
    
            s2200_brasil_dados = {}
            s2200_brasil_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_brasil_dados['tplograd'] = brasil.tpLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_brasil_dados['dsclograd'] = brasil.dscLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_brasil_dados['nrlograd'] = brasil.nrLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_brasil_dados['complemento'] = brasil.complemento.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_brasil_dados['bairro'] = brasil.bairro.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_brasil_dados['cep'] = brasil.cep.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_brasil_dados['codmunic'] = brasil.codMunic.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_brasil_dados['uf'] = brasil.uf.cdata
            except AttributeError: 
                pass
    
            s2200_brasil = s2200brasil.objects.create(**s2200_brasil_dados)
    
    if 'trabalhador' in dir(evtAdmissao) and 'endereco' in dir(evtAdmissao.trabalhador) and 'exterior' in dir(evtAdmissao.trabalhador.endereco):
    
        for exterior in evtAdmissao.trabalhador.endereco.exterior:
    
            s2200_exterior_dados = {}
            s2200_exterior_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_exterior_dados['paisresid'] = exterior.paisResid.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_exterior_dados['dsclograd'] = exterior.dscLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_exterior_dados['nrlograd'] = exterior.nrLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_exterior_dados['complemento'] = exterior.complemento.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_exterior_dados['bairro'] = exterior.bairro.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_exterior_dados['nmcid'] = exterior.nmCid.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_exterior_dados['codpostal'] = exterior.codPostal.cdata
            except AttributeError: 
                pass
    
            s2200_exterior = s2200exterior.objects.create(**s2200_exterior_dados)
    
    if 'trabalhador' in dir(evtAdmissao) and 'trabEstrangeiro' in dir(evtAdmissao.trabalhador):
    
        for trabEstrangeiro in evtAdmissao.trabalhador.trabEstrangeiro:
    
            s2200_trabestrangeiro_dados = {}
            s2200_trabestrangeiro_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_trabestrangeiro_dados['dtchegada'] = trabEstrangeiro.dtChegada.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_trabestrangeiro_dados['classtrabestrang'] = trabEstrangeiro.classTrabEstrang.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_trabestrangeiro_dados['casadobr'] = trabEstrangeiro.casadoBr.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_trabestrangeiro_dados['filhosbr'] = trabEstrangeiro.filhosBr.cdata
            except AttributeError: 
                pass
    
            s2200_trabestrangeiro = s2200trabEstrangeiro.objects.create(**s2200_trabestrangeiro_dados)
    
    if 'trabalhador' in dir(evtAdmissao) and 'infoDeficiencia' in dir(evtAdmissao.trabalhador):
    
        for infoDeficiencia in evtAdmissao.trabalhador.infoDeficiencia:
    
            s2200_infodeficiencia_dados = {}
            s2200_infodeficiencia_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_infodeficiencia_dados['deffisica'] = infoDeficiencia.defFisica.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infodeficiencia_dados['defvisual'] = infoDeficiencia.defVisual.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infodeficiencia_dados['defauditiva'] = infoDeficiencia.defAuditiva.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infodeficiencia_dados['defmental'] = infoDeficiencia.defMental.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infodeficiencia_dados['defintelectual'] = infoDeficiencia.defIntelectual.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infodeficiencia_dados['reabreadap'] = infoDeficiencia.reabReadap.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infodeficiencia_dados['infocota'] = infoDeficiencia.infoCota.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infodeficiencia_dados['observacao'] = infoDeficiencia.observacao.cdata
            except AttributeError: 
                pass
    
            s2200_infodeficiencia = s2200infoDeficiencia.objects.create(**s2200_infodeficiencia_dados)
    
    if 'trabalhador' in dir(evtAdmissao) and 'dependente' in dir(evtAdmissao.trabalhador):
    
        for dependente in evtAdmissao.trabalhador.dependente:
    
            s2200_dependente_dados = {}
            s2200_dependente_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_dependente_dados['tpdep'] = dependente.tpDep.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_dependente_dados['nmdep'] = dependente.nmDep.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_dependente_dados['dtnascto'] = dependente.dtNascto.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_dependente_dados['cpfdep'] = dependente.cpfDep.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_dependente_dados['sexodep'] = dependente.sexoDep.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_dependente_dados['depirrf'] = dependente.depIRRF.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_dependente_dados['depsf'] = dependente.depSF.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_dependente_dados['inctrab'] = dependente.incTrab.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_dependente_dados['depfinsprev'] = dependente.depFinsPrev.cdata
            except AttributeError: 
                pass
    
            s2200_dependente = s2200dependente.objects.create(**s2200_dependente_dados)
    
    if 'trabalhador' in dir(evtAdmissao) and 'aposentadoria' in dir(evtAdmissao.trabalhador):
    
        for aposentadoria in evtAdmissao.trabalhador.aposentadoria:
    
            s2200_aposentadoria_dados = {}
            s2200_aposentadoria_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_aposentadoria_dados['trabaposent'] = aposentadoria.trabAposent.cdata
            except AttributeError: 
                pass
    
            s2200_aposentadoria = s2200aposentadoria.objects.create(**s2200_aposentadoria_dados)
    
    if 'trabalhador' in dir(evtAdmissao) and 'contato' in dir(evtAdmissao.trabalhador):
    
        for contato in evtAdmissao.trabalhador.contato:
    
            s2200_contato_dados = {}
            s2200_contato_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_contato_dados['foneprinc'] = contato.fonePrinc.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_contato_dados['fonealternat'] = contato.foneAlternat.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_contato_dados['emailprinc'] = contato.emailPrinc.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_contato_dados['emailalternat'] = contato.emailAlternat.cdata
            except AttributeError: 
                pass
    
            s2200_contato = s2200contato.objects.create(**s2200_contato_dados)
    
    if 'vinculo' in dir(evtAdmissao) and 'infoRegimeTrab' in dir(evtAdmissao.vinculo) and 'infoCeletista' in dir(evtAdmissao.vinculo.infoRegimeTrab):
    
        for infoCeletista in evtAdmissao.vinculo.infoRegimeTrab.infoCeletista:
    
            s2200_infoceletista_dados = {}
            s2200_infoceletista_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_infoceletista_dados['dtadm'] = infoCeletista.dtAdm.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoceletista_dados['tpadmissao'] = infoCeletista.tpAdmissao.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoceletista_dados['indadmissao'] = infoCeletista.indAdmissao.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoceletista_dados['tpregjor'] = infoCeletista.tpRegJor.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoceletista_dados['natatividade'] = infoCeletista.natAtividade.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoceletista_dados['dtbase'] = infoCeletista.dtBase.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoceletista_dados['cnpjsindcategprof'] = infoCeletista.cnpjSindCategProf.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoceletista_dados['opcfgts'] = infoCeletista.FGTS.opcFGTS.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoceletista_dados['dtopcfgts'] = infoCeletista.FGTS.dtOpcFGTS.cdata
            except AttributeError: 
                pass
    
            s2200_infoceletista = s2200infoCeletista.objects.create(**s2200_infoceletista_dados)
            
            if 'trabTemporario' in dir(infoCeletista):
            
                for trabTemporario in infoCeletista.trabTemporario:
            
                    s2200_trabtemporario_dados = {}
                    s2200_trabtemporario_dados['s2200_infoceletista_id'] = s2200_infoceletista.id
                    
                    try:
                        s2200_trabtemporario_dados['hipleg'] = trabTemporario.hipLeg.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_trabtemporario_dados['justcontr'] = trabTemporario.justContr.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_trabtemporario_dados['tpinclcontr'] = trabTemporario.tpInclContr.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_trabtemporario_dados['tpinsc'] = trabTemporario.ideTomadorServ.tpInsc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_trabtemporario_dados['nrinsc'] = trabTemporario.ideTomadorServ.nrInsc.cdata
                    except AttributeError: 
                        pass
            
                    s2200_trabtemporario = s2200trabTemporario.objects.create(**s2200_trabtemporario_dados)
                    
                    if 'ideTomadorServ' in dir(trabTemporario) and 'ideEstabVinc' in dir(trabTemporario.ideTomadorServ):
                    
                        for ideEstabVinc in trabTemporario.ideTomadorServ.ideEstabVinc:
                    
                            s2200_ideestabvinc_dados = {}
                            s2200_ideestabvinc_dados['s2200_trabtemporario_id'] = s2200_trabtemporario.id
                            
                            try:
                                s2200_ideestabvinc_dados['tpinsc'] = ideEstabVinc.tpInsc.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s2200_ideestabvinc_dados['nrinsc'] = ideEstabVinc.nrInsc.cdata
                            except AttributeError: 
                                pass
                    
                            s2200_ideestabvinc = s2200ideEstabVinc.objects.create(**s2200_ideestabvinc_dados)
                    
                    if 'ideTrabSubstituido' in dir(trabTemporario):
                    
                        for ideTrabSubstituido in trabTemporario.ideTrabSubstituido:
                    
                            s2200_idetrabsubstituido_dados = {}
                            s2200_idetrabsubstituido_dados['s2200_trabtemporario_id'] = s2200_trabtemporario.id
                            
                            try:
                                s2200_idetrabsubstituido_dados['cpftrabsubst'] = ideTrabSubstituido.cpfTrabSubst.cdata
                            except AttributeError: 
                                pass
                    
                            s2200_idetrabsubstituido = s2200ideTrabSubstituido.objects.create(**s2200_idetrabsubstituido_dados)
            
            if 'aprend' in dir(infoCeletista):
            
                for aprend in infoCeletista.aprend:
            
                    s2200_aprend_dados = {}
                    s2200_aprend_dados['s2200_infoceletista_id'] = s2200_infoceletista.id
                    
                    try:
                        s2200_aprend_dados['tpinsc'] = aprend.tpInsc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_aprend_dados['nrinsc'] = aprend.nrInsc.cdata
                    except AttributeError: 
                        pass
            
                    s2200_aprend = s2200aprend.objects.create(**s2200_aprend_dados)
    
    if 'vinculo' in dir(evtAdmissao) and 'infoRegimeTrab' in dir(evtAdmissao.vinculo) and 'infoEstatutario' in dir(evtAdmissao.vinculo.infoRegimeTrab):
    
        for infoEstatutario in evtAdmissao.vinculo.infoRegimeTrab.infoEstatutario:
    
            s2200_infoestatutario_dados = {}
            s2200_infoestatutario_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_infoestatutario_dados['indprovim'] = infoEstatutario.indProvim.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoestatutario_dados['tpprov'] = infoEstatutario.tpProv.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoestatutario_dados['dtnomeacao'] = infoEstatutario.dtNomeacao.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoestatutario_dados['dtposse'] = infoEstatutario.dtPosse.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoestatutario_dados['dtexercicio'] = infoEstatutario.dtExercicio.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoestatutario_dados['dtingsvpub'] = infoEstatutario.dtIngSvPub.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoestatutario_dados['tpplanrp'] = infoEstatutario.tpPlanRP.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoestatutario_dados['indtetorgps'] = infoEstatutario.indTetoRGPS.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoestatutario_dados['indabonoperm'] = infoEstatutario.indAbonoPerm.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoestatutario_dados['dtiniabono'] = infoEstatutario.dtIniAbono.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoestatutario_dados['indparcremun'] = infoEstatutario.indParcRemun.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_infoestatutario_dados['dtiniparc'] = infoEstatutario.dtIniParc.cdata
            except AttributeError: 
                pass
    
            s2200_infoestatutario = s2200infoEstatutario.objects.create(**s2200_infoestatutario_dados)
            
            if 'infoDecJud' in dir(infoEstatutario):
            
                for infoDecJud in infoEstatutario.infoDecJud:
            
                    s2200_infodecjud_dados = {}
                    s2200_infodecjud_dados['s2200_infoestatutario_id'] = s2200_infoestatutario.id
                    
                    try:
                        s2200_infodecjud_dados['nrprocjud'] = infoDecJud.nrProcJud.cdata
                    except AttributeError: 
                        pass
            
                    s2200_infodecjud = s2200infoDecJud.objects.create(**s2200_infodecjud_dados)
    
    if 'vinculo' in dir(evtAdmissao) and 'infoContrato' in dir(evtAdmissao.vinculo) and 'localTrabalho' in dir(evtAdmissao.vinculo.infoContrato) and 'localTrabGeral' in dir(evtAdmissao.vinculo.infoContrato.localTrabalho):
    
        for localTrabGeral in evtAdmissao.vinculo.infoContrato.localTrabalho.localTrabGeral:
    
            s2200_localtrabgeral_dados = {}
            s2200_localtrabgeral_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_localtrabgeral_dados['tpinsc'] = localTrabGeral.tpInsc.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_localtrabgeral_dados['nrinsc'] = localTrabGeral.nrInsc.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_localtrabgeral_dados['desccomp'] = localTrabGeral.descComp.cdata
            except AttributeError: 
                pass
    
            s2200_localtrabgeral = s2200localTrabGeral.objects.create(**s2200_localtrabgeral_dados)
    
    if 'vinculo' in dir(evtAdmissao) and 'infoContrato' in dir(evtAdmissao.vinculo) and 'localTrabalho' in dir(evtAdmissao.vinculo.infoContrato) and 'localTrabDom' in dir(evtAdmissao.vinculo.infoContrato.localTrabalho):
    
        for localTrabDom in evtAdmissao.vinculo.infoContrato.localTrabalho.localTrabDom:
    
            s2200_localtrabdom_dados = {}
            s2200_localtrabdom_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_localtrabdom_dados['tplograd'] = localTrabDom.tpLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_localtrabdom_dados['dsclograd'] = localTrabDom.dscLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_localtrabdom_dados['nrlograd'] = localTrabDom.nrLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_localtrabdom_dados['complemento'] = localTrabDom.complemento.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_localtrabdom_dados['bairro'] = localTrabDom.bairro.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_localtrabdom_dados['cep'] = localTrabDom.cep.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_localtrabdom_dados['codmunic'] = localTrabDom.codMunic.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_localtrabdom_dados['uf'] = localTrabDom.uf.cdata
            except AttributeError: 
                pass
    
            s2200_localtrabdom = s2200localTrabDom.objects.create(**s2200_localtrabdom_dados)
    
    if 'vinculo' in dir(evtAdmissao) and 'infoContrato' in dir(evtAdmissao.vinculo) and 'horContratual' in dir(evtAdmissao.vinculo.infoContrato):
    
        for horContratual in evtAdmissao.vinculo.infoContrato.horContratual:
    
            s2200_horcontratual_dados = {}
            s2200_horcontratual_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_horcontratual_dados['qtdhrssem'] = horContratual.qtdHrsSem.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_horcontratual_dados['tpjornada'] = horContratual.tpJornada.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_horcontratual_dados['dsctpjorn'] = horContratual.dscTpJorn.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_horcontratual_dados['tmpparc'] = horContratual.tmpParc.cdata
            except AttributeError: 
                pass
    
            s2200_horcontratual = s2200horContratual.objects.create(**s2200_horcontratual_dados)
            
            if 'horario' in dir(horContratual):
            
                for horario in horContratual.horario:
            
                    s2200_horario_dados = {}
                    s2200_horario_dados['s2200_horcontratual_id'] = s2200_horcontratual.id
                    
                    try:
                        s2200_horario_dados['dia'] = horario.dia.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2200_horario_dados['codhorcontrat'] = horario.codHorContrat.cdata
                    except AttributeError: 
                        pass
            
                    s2200_horario = s2200horario.objects.create(**s2200_horario_dados)
    
    if 'vinculo' in dir(evtAdmissao) and 'infoContrato' in dir(evtAdmissao.vinculo) and 'filiacaoSindical' in dir(evtAdmissao.vinculo.infoContrato):
    
        for filiacaoSindical in evtAdmissao.vinculo.infoContrato.filiacaoSindical:
    
            s2200_filiacaosindical_dados = {}
            s2200_filiacaosindical_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_filiacaosindical_dados['cnpjsindtrab'] = filiacaoSindical.cnpjSindTrab.cdata
            except AttributeError: 
                pass
    
            s2200_filiacaosindical = s2200filiacaoSindical.objects.create(**s2200_filiacaosindical_dados)
    
    if 'vinculo' in dir(evtAdmissao) and 'infoContrato' in dir(evtAdmissao.vinculo) and 'alvaraJudicial' in dir(evtAdmissao.vinculo.infoContrato):
    
        for alvaraJudicial in evtAdmissao.vinculo.infoContrato.alvaraJudicial:
    
            s2200_alvarajudicial_dados = {}
            s2200_alvarajudicial_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_alvarajudicial_dados['nrprocjud'] = alvaraJudicial.nrProcJud.cdata
            except AttributeError: 
                pass
    
            s2200_alvarajudicial = s2200alvaraJudicial.objects.create(**s2200_alvarajudicial_dados)
    
    if 'vinculo' in dir(evtAdmissao) and 'infoContrato' in dir(evtAdmissao.vinculo) and 'observacoes' in dir(evtAdmissao.vinculo.infoContrato):
    
        for observacoes in evtAdmissao.vinculo.infoContrato.observacoes:
    
            s2200_observacoes_dados = {}
            s2200_observacoes_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_observacoes_dados['observacao'] = observacoes.observacao.cdata
            except AttributeError: 
                pass
    
            s2200_observacoes = s2200observacoes.objects.create(**s2200_observacoes_dados)
    
    if 'vinculo' in dir(evtAdmissao) and 'sucessaoVinc' in dir(evtAdmissao.vinculo):
    
        for sucessaoVinc in evtAdmissao.vinculo.sucessaoVinc:
    
            s2200_sucessaovinc_dados = {}
            s2200_sucessaovinc_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_sucessaovinc_dados['tpinscant'] = sucessaoVinc.tpInscAnt.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_sucessaovinc_dados['cnpjempregant'] = sucessaoVinc.cnpjEmpregAnt.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_sucessaovinc_dados['matricant'] = sucessaoVinc.matricAnt.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_sucessaovinc_dados['dttransf'] = sucessaoVinc.dtTransf.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_sucessaovinc_dados['observacao'] = sucessaoVinc.observacao.cdata
            except AttributeError: 
                pass
    
            s2200_sucessaovinc = s2200sucessaoVinc.objects.create(**s2200_sucessaovinc_dados)
    
    if 'vinculo' in dir(evtAdmissao) and 'transfDom' in dir(evtAdmissao.vinculo):
    
        for transfDom in evtAdmissao.vinculo.transfDom:
    
            s2200_transfdom_dados = {}
            s2200_transfdom_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_transfdom_dados['cpfsubstituido'] = transfDom.cpfSubstituido.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_transfdom_dados['matricant'] = transfDom.matricAnt.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_transfdom_dados['dttransf'] = transfDom.dtTransf.cdata
            except AttributeError: 
                pass
    
            s2200_transfdom = s2200transfDom.objects.create(**s2200_transfdom_dados)
    
    if 'vinculo' in dir(evtAdmissao) and 'mudancaCPF' in dir(evtAdmissao.vinculo):
    
        for mudancaCPF in evtAdmissao.vinculo.mudancaCPF:
    
            s2200_mudancacpf_dados = {}
            s2200_mudancacpf_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_mudancacpf_dados['cpfant'] = mudancaCPF.cpfAnt.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_mudancacpf_dados['matricant'] = mudancaCPF.matricAnt.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_mudancacpf_dados['dtaltcpf'] = mudancaCPF.dtAltCPF.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_mudancacpf_dados['observacao'] = mudancaCPF.observacao.cdata
            except AttributeError: 
                pass
    
            s2200_mudancacpf = s2200mudancaCPF.objects.create(**s2200_mudancacpf_dados)
    
    if 'vinculo' in dir(evtAdmissao) and 'afastamento' in dir(evtAdmissao.vinculo):
    
        for afastamento in evtAdmissao.vinculo.afastamento:
    
            s2200_afastamento_dados = {}
            s2200_afastamento_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_afastamento_dados['dtiniafast'] = afastamento.dtIniAfast.cdata
            except AttributeError: 
                pass
            
            try:
                s2200_afastamento_dados['codmotafast'] = afastamento.codMotAfast.cdata
            except AttributeError: 
                pass
    
            s2200_afastamento = s2200afastamento.objects.create(**s2200_afastamento_dados)
    
    if 'vinculo' in dir(evtAdmissao) and 'desligamento' in dir(evtAdmissao.vinculo):
    
        for desligamento in evtAdmissao.vinculo.desligamento:
    
            s2200_desligamento_dados = {}
            s2200_desligamento_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_desligamento_dados['dtdeslig'] = desligamento.dtDeslig.cdata
            except AttributeError: 
                pass
    
            s2200_desligamento = s2200desligamento.objects.create(**s2200_desligamento_dados)
    
    if 'vinculo' in dir(evtAdmissao) and 'cessao' in dir(evtAdmissao.vinculo):
    
        for cessao in evtAdmissao.vinculo.cessao:
    
            s2200_cessao_dados = {}
            s2200_cessao_dados['s2200_evtadmissao_id'] = s2200_evtadmissao.id
            
            try:
                s2200_cessao_dados['dtinicessao'] = cessao.dtIniCessao.cdata
            except AttributeError: 
                pass
    
            s2200_cessao = s2200cessao.objects.create(**s2200_cessao_dados)    
    s2200_evtadmissao_dados['evento'] = 's2200'
    s2200_evtadmissao_dados['id'] = s2200_evtadmissao.id
    s2200_evtadmissao_dados['identidade_evento'] = doc.eSocial.evtAdmissao['Id']
    s2200_evtadmissao_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s2200_evtadmissao_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, s2200_evtadmissao.id)
    
    return s2200_evtadmissao_dados