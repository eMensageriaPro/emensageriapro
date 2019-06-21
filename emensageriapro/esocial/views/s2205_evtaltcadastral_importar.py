#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2205.models import *



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
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2205_evtaltcadastral_obj(request, doc, status, validar)

    s2205evtAltCadastral.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s2205_evtaltcadastral_obj(request, doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2205_evtaltcadastral_dados = {}
    s2205_evtaltcadastral_dados['status'] = status
    s2205_evtaltcadastral_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2205_evtaltcadastral_dados['identidade'] = doc.eSocial.evtAltCadastral['Id']
    evtAltCadastral = doc.eSocial.evtAltCadastral
    
    try:
        s2205_evtaltcadastral_dados['indretif'] = evtAltCadastral.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['nrrecibo'] = evtAltCadastral.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['tpamb'] = evtAltCadastral.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['procemi'] = evtAltCadastral.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['verproc'] = evtAltCadastral.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['tpinsc'] = evtAltCadastral.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['nrinsc'] = evtAltCadastral.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['cpftrab'] = evtAltCadastral.ideTrabalhador.cpfTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['dtalteracao'] = evtAltCadastral.alteracao.dtAlteracao.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['nistrab'] = evtAltCadastral.alteracao.dadosTrabalhador.nisTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['nmtrab'] = evtAltCadastral.alteracao.dadosTrabalhador.nmTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['sexo'] = evtAltCadastral.alteracao.dadosTrabalhador.sexo.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['racacor'] = evtAltCadastral.alteracao.dadosTrabalhador.racaCor.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['estciv'] = evtAltCadastral.alteracao.dadosTrabalhador.estCiv.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['grauinstr'] = evtAltCadastral.alteracao.dadosTrabalhador.grauInstr.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['nmsoc'] = evtAltCadastral.alteracao.dadosTrabalhador.nmSoc.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['dtnascto'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.dtNascto.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['codmunic'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.codMunic.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['uf'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.uf.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['paisnascto'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.paisNascto.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['paisnac'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.paisNac.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['nmmae'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.nmMae.cdata
    except AttributeError: 
        pass
    
    try:
        s2205_evtaltcadastral_dados['nmpai'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.nmPai.cdata
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
                        s2205_ctps_dados['nrctps'] = CTPS.nrCtps.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2205_ctps_dados['seriectps'] = CTPS.serieCtps.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2205_ctps_dados['ufctps'] = CTPS.ufCtps.cdata
                    except AttributeError: 
                        pass
            
                    s2205_ctps = s2205CTPS.objects.create(**s2205_ctps_dados)
            
            if 'RIC' in dir(documentos):
            
                for RIC in documentos.RIC:
            
                    s2205_ric_dados = {}
                    s2205_ric_dados['s2205_documentos_id'] = s2205_documentos.id
                    
                    try:
                        s2205_ric_dados['nrric'] = RIC.nrRic.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2205_ric_dados['orgaoemissor'] = RIC.orgaoEmissor.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2205_ric_dados['dtexped'] = RIC.dtExped.cdata
                    except AttributeError: 
                        pass
            
                    s2205_ric = s2205RIC.objects.create(**s2205_ric_dados)
            
            if 'RG' in dir(documentos):
            
                for RG in documentos.RG:
            
                    s2205_rg_dados = {}
                    s2205_rg_dados['s2205_documentos_id'] = s2205_documentos.id
                    
                    try:
                        s2205_rg_dados['nrrg'] = RG.nrRg.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2205_rg_dados['orgaoemissor'] = RG.orgaoEmissor.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2205_rg_dados['dtexped'] = RG.dtExped.cdata
                    except AttributeError: 
                        pass
            
                    s2205_rg = s2205RG.objects.create(**s2205_rg_dados)
            
            if 'RNE' in dir(documentos):
            
                for RNE in documentos.RNE:
            
                    s2205_rne_dados = {}
                    s2205_rne_dados['s2205_documentos_id'] = s2205_documentos.id
                    
                    try:
                        s2205_rne_dados['nrrne'] = RNE.nrRne.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2205_rne_dados['orgaoemissor'] = RNE.orgaoEmissor.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2205_rne_dados['dtexped'] = RNE.dtExped.cdata
                    except AttributeError: 
                        pass
            
                    s2205_rne = s2205RNE.objects.create(**s2205_rne_dados)
            
            if 'OC' in dir(documentos):
            
                for OC in documentos.OC:
            
                    s2205_oc_dados = {}
                    s2205_oc_dados['s2205_documentos_id'] = s2205_documentos.id
                    
                    try:
                        s2205_oc_dados['nroc'] = OC.nrOc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2205_oc_dados['orgaoemissor'] = OC.orgaoEmissor.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2205_oc_dados['dtexped'] = OC.dtExped.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2205_oc_dados['dtvalid'] = OC.dtValid.cdata
                    except AttributeError: 
                        pass
            
                    s2205_oc = s2205OC.objects.create(**s2205_oc_dados)
            
            if 'CNH' in dir(documentos):
            
                for CNH in documentos.CNH:
            
                    s2205_cnh_dados = {}
                    s2205_cnh_dados['s2205_documentos_id'] = s2205_documentos.id
                    
                    try:
                        s2205_cnh_dados['nrregcnh'] = CNH.nrRegCnh.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2205_cnh_dados['dtexped'] = CNH.dtExped.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2205_cnh_dados['ufcnh'] = CNH.ufCnh.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2205_cnh_dados['dtvalid'] = CNH.dtValid.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2205_cnh_dados['dtprihab'] = CNH.dtPriHab.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2205_cnh_dados['categoriacnh'] = CNH.categoriaCnh.cdata
                    except AttributeError: 
                        pass
            
                    s2205_cnh = s2205CNH.objects.create(**s2205_cnh_dados)
    
    if 'alteracao' in dir(evtAltCadastral) and 'dadosTrabalhador' in dir(evtAltCadastral.alteracao) and 'endereco' in dir(evtAltCadastral.alteracao.dadosTrabalhador) and 'brasil' in dir(evtAltCadastral.alteracao.dadosTrabalhador.endereco):
    
        for brasil in evtAltCadastral.alteracao.dadosTrabalhador.endereco.brasil:
    
            s2205_brasil_dados = {}
            s2205_brasil_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral.id
            
            try:
                s2205_brasil_dados['tplograd'] = brasil.tpLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_brasil_dados['dsclograd'] = brasil.dscLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_brasil_dados['nrlograd'] = brasil.nrLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_brasil_dados['complemento'] = brasil.complemento.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_brasil_dados['bairro'] = brasil.bairro.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_brasil_dados['cep'] = brasil.cep.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_brasil_dados['codmunic'] = brasil.codMunic.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_brasil_dados['uf'] = brasil.uf.cdata
            except AttributeError: 
                pass
    
            s2205_brasil = s2205brasil.objects.create(**s2205_brasil_dados)
    
    if 'alteracao' in dir(evtAltCadastral) and 'dadosTrabalhador' in dir(evtAltCadastral.alteracao) and 'endereco' in dir(evtAltCadastral.alteracao.dadosTrabalhador) and 'exterior' in dir(evtAltCadastral.alteracao.dadosTrabalhador.endereco):
    
        for exterior in evtAltCadastral.alteracao.dadosTrabalhador.endereco.exterior:
    
            s2205_exterior_dados = {}
            s2205_exterior_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral.id
            
            try:
                s2205_exterior_dados['paisresid'] = exterior.paisResid.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_exterior_dados['dsclograd'] = exterior.dscLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_exterior_dados['nrlograd'] = exterior.nrLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_exterior_dados['complemento'] = exterior.complemento.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_exterior_dados['bairro'] = exterior.bairro.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_exterior_dados['nmcid'] = exterior.nmCid.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_exterior_dados['codpostal'] = exterior.codPostal.cdata
            except AttributeError: 
                pass
    
            s2205_exterior = s2205exterior.objects.create(**s2205_exterior_dados)
    
    if 'alteracao' in dir(evtAltCadastral) and 'dadosTrabalhador' in dir(evtAltCadastral.alteracao) and 'trabEstrangeiro' in dir(evtAltCadastral.alteracao.dadosTrabalhador):
    
        for trabEstrangeiro in evtAltCadastral.alteracao.dadosTrabalhador.trabEstrangeiro:
    
            s2205_trabestrangeiro_dados = {}
            s2205_trabestrangeiro_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral.id
            
            try:
                s2205_trabestrangeiro_dados['dtchegada'] = trabEstrangeiro.dtChegada.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_trabestrangeiro_dados['classtrabestrang'] = trabEstrangeiro.classTrabEstrang.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_trabestrangeiro_dados['casadobr'] = trabEstrangeiro.casadoBr.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_trabestrangeiro_dados['filhosbr'] = trabEstrangeiro.filhosBr.cdata
            except AttributeError: 
                pass
    
            s2205_trabestrangeiro = s2205trabEstrangeiro.objects.create(**s2205_trabestrangeiro_dados)
    
    if 'alteracao' in dir(evtAltCadastral) and 'dadosTrabalhador' in dir(evtAltCadastral.alteracao) and 'infoDeficiencia' in dir(evtAltCadastral.alteracao.dadosTrabalhador):
    
        for infoDeficiencia in evtAltCadastral.alteracao.dadosTrabalhador.infoDeficiencia:
    
            s2205_infodeficiencia_dados = {}
            s2205_infodeficiencia_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral.id
            
            try:
                s2205_infodeficiencia_dados['deffisica'] = infoDeficiencia.defFisica.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_infodeficiencia_dados['defvisual'] = infoDeficiencia.defVisual.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_infodeficiencia_dados['defauditiva'] = infoDeficiencia.defAuditiva.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_infodeficiencia_dados['defmental'] = infoDeficiencia.defMental.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_infodeficiencia_dados['defintelectual'] = infoDeficiencia.defIntelectual.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_infodeficiencia_dados['reabreadap'] = infoDeficiencia.reabReadap.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_infodeficiencia_dados['infocota'] = infoDeficiencia.infoCota.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_infodeficiencia_dados['observacao'] = infoDeficiencia.observacao.cdata
            except AttributeError: 
                pass
    
            s2205_infodeficiencia = s2205infoDeficiencia.objects.create(**s2205_infodeficiencia_dados)
    
    if 'alteracao' in dir(evtAltCadastral) and 'dadosTrabalhador' in dir(evtAltCadastral.alteracao) and 'dependente' in dir(evtAltCadastral.alteracao.dadosTrabalhador):
    
        for dependente in evtAltCadastral.alteracao.dadosTrabalhador.dependente:
    
            s2205_dependente_dados = {}
            s2205_dependente_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral.id
            
            try:
                s2205_dependente_dados['tpdep'] = dependente.tpDep.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_dependente_dados['nmdep'] = dependente.nmDep.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_dependente_dados['dtnascto'] = dependente.dtNascto.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_dependente_dados['cpfdep'] = dependente.cpfDep.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_dependente_dados['sexodep'] = dependente.sexoDep.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_dependente_dados['depirrf'] = dependente.depIRRF.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_dependente_dados['depsf'] = dependente.depSF.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_dependente_dados['inctrab'] = dependente.incTrab.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_dependente_dados['depfinsprev'] = dependente.depFinsPrev.cdata
            except AttributeError: 
                pass
    
            s2205_dependente = s2205dependente.objects.create(**s2205_dependente_dados)
    
    if 'alteracao' in dir(evtAltCadastral) and 'dadosTrabalhador' in dir(evtAltCadastral.alteracao) and 'aposentadoria' in dir(evtAltCadastral.alteracao.dadosTrabalhador):
    
        for aposentadoria in evtAltCadastral.alteracao.dadosTrabalhador.aposentadoria:
    
            s2205_aposentadoria_dados = {}
            s2205_aposentadoria_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral.id
            
            try:
                s2205_aposentadoria_dados['trabaposent'] = aposentadoria.trabAposent.cdata
            except AttributeError: 
                pass
    
            s2205_aposentadoria = s2205aposentadoria.objects.create(**s2205_aposentadoria_dados)
    
    if 'alteracao' in dir(evtAltCadastral) and 'dadosTrabalhador' in dir(evtAltCadastral.alteracao) and 'contato' in dir(evtAltCadastral.alteracao.dadosTrabalhador):
    
        for contato in evtAltCadastral.alteracao.dadosTrabalhador.contato:
    
            s2205_contato_dados = {}
            s2205_contato_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral.id
            
            try:
                s2205_contato_dados['foneprinc'] = contato.fonePrinc.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_contato_dados['fonealternat'] = contato.foneAlternat.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_contato_dados['emailprinc'] = contato.emailPrinc.cdata
            except AttributeError: 
                pass
            
            try:
                s2205_contato_dados['emailalternat'] = contato.emailAlternat.cdata
            except AttributeError: 
                pass
    
            s2205_contato = s2205contato.objects.create(**s2205_contato_dados)    
    s2205_evtaltcadastral_dados['evento'] = 's2205'
    s2205_evtaltcadastral_dados['id'] = s2205_evtaltcadastral.id
    s2205_evtaltcadastral_dados['identidade_evento'] = doc.eSocial.evtAltCadastral['Id']
    s2205_evtaltcadastral_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s2205_evtaltcadastral_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, s2205_evtaltcadastral.id)
    
    return s2205_evtaltcadastral_dados