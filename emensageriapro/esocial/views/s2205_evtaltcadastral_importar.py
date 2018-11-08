#coding:utf-8
"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql


def read_s2205_evtaltcadastral_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2205_evtaltcadastral_obj(doc, status, validar)
    return dados

def read_s2205_evtaltcadastral(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2205_evtaltcadastral_obj(doc, status, validar)
    return dados



def read_s2205_evtaltcadastral_obj(doc, status, validar=False):
    s2205_evtaltcadastral_dados = {}
    s2205_evtaltcadastral_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2205_evtaltcadastral_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2205_evtaltcadastral_dados['identidade'] = doc.eSocial.evtAltCadastral['Id']
    s2205_evtaltcadastral_dados['processamento_codigo_resposta'] = 1
    evtAltCadastral = doc.eSocial.evtAltCadastral

    if 'indRetif' in dir(evtAltCadastral.ideEvento): s2205_evtaltcadastral_dados['indretif'] = evtAltCadastral.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtAltCadastral.ideEvento): s2205_evtaltcadastral_dados['nrrecibo'] = evtAltCadastral.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtAltCadastral.ideEvento): s2205_evtaltcadastral_dados['tpamb'] = evtAltCadastral.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtAltCadastral.ideEvento): s2205_evtaltcadastral_dados['procemi'] = evtAltCadastral.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtAltCadastral.ideEvento): s2205_evtaltcadastral_dados['verproc'] = evtAltCadastral.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtAltCadastral.ideEmpregador): s2205_evtaltcadastral_dados['tpinsc'] = evtAltCadastral.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtAltCadastral.ideEmpregador): s2205_evtaltcadastral_dados['nrinsc'] = evtAltCadastral.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtAltCadastral.ideTrabalhador): s2205_evtaltcadastral_dados['cpftrab'] = evtAltCadastral.ideTrabalhador.cpfTrab.cdata
    if 'dtAlteracao' in dir(evtAltCadastral.alteracao): s2205_evtaltcadastral_dados['dtalteracao'] = evtAltCadastral.alteracao.dtAlteracao.cdata
    if 'nisTrab' in dir(evtAltCadastral.alteracao.dadosTrabalhador): s2205_evtaltcadastral_dados['nistrab'] = evtAltCadastral.alteracao.dadosTrabalhador.nisTrab.cdata
    if 'nmTrab' in dir(evtAltCadastral.alteracao.dadosTrabalhador): s2205_evtaltcadastral_dados['nmtrab'] = evtAltCadastral.alteracao.dadosTrabalhador.nmTrab.cdata
    if 'sexo' in dir(evtAltCadastral.alteracao.dadosTrabalhador): s2205_evtaltcadastral_dados['sexo'] = evtAltCadastral.alteracao.dadosTrabalhador.sexo.cdata
    if 'racaCor' in dir(evtAltCadastral.alteracao.dadosTrabalhador): s2205_evtaltcadastral_dados['racacor'] = evtAltCadastral.alteracao.dadosTrabalhador.racaCor.cdata
    if 'estCiv' in dir(evtAltCadastral.alteracao.dadosTrabalhador): s2205_evtaltcadastral_dados['estciv'] = evtAltCadastral.alteracao.dadosTrabalhador.estCiv.cdata
    if 'grauInstr' in dir(evtAltCadastral.alteracao.dadosTrabalhador): s2205_evtaltcadastral_dados['grauinstr'] = evtAltCadastral.alteracao.dadosTrabalhador.grauInstr.cdata
    if 'nmSoc' in dir(evtAltCadastral.alteracao.dadosTrabalhador): s2205_evtaltcadastral_dados['nmsoc'] = evtAltCadastral.alteracao.dadosTrabalhador.nmSoc.cdata
    if 'dtNascto' in dir(evtAltCadastral.alteracao.dadosTrabalhador.nascimento): s2205_evtaltcadastral_dados['dtnascto'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.dtNascto.cdata
    if 'codMunic' in dir(evtAltCadastral.alteracao.dadosTrabalhador.nascimento): s2205_evtaltcadastral_dados['codmunic'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.codMunic.cdata
    if 'uf' in dir(evtAltCadastral.alteracao.dadosTrabalhador.nascimento): s2205_evtaltcadastral_dados['uf'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.uf.cdata
    if 'paisNascto' in dir(evtAltCadastral.alteracao.dadosTrabalhador.nascimento): s2205_evtaltcadastral_dados['paisnascto'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.paisNascto.cdata
    if 'paisNac' in dir(evtAltCadastral.alteracao.dadosTrabalhador.nascimento): s2205_evtaltcadastral_dados['paisnac'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.paisNac.cdata
    if 'nmMae' in dir(evtAltCadastral.alteracao.dadosTrabalhador.nascimento): s2205_evtaltcadastral_dados['nmmae'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.nmMae.cdata
    if 'nmPai' in dir(evtAltCadastral.alteracao.dadosTrabalhador.nascimento): s2205_evtaltcadastral_dados['nmpai'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.nmPai.cdata
    if 'inclusao' in dir(evtAltCadastral.alteracao): s2205_evtaltcadastral_dados['operacao'] = 1
    elif 'alteracao' in dir(evtAltCadastral.alteracao): s2205_evtaltcadastral_dados['operacao'] = 2
    elif 'exclusao' in dir(evtAltCadastral.alteracao): s2205_evtaltcadastral_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2205_evtaltcadastral', s2205_evtaltcadastral_dados)
    resp = executar_sql(insert, True)
    s2205_evtaltcadastral_id = resp[0][0]
    dados = s2205_evtaltcadastral_dados
    dados['evento'] = 's2205'
    dados['id'] = s2205_evtaltcadastral_id
    dados['identidade_evento'] = doc.eSocial.evtAltCadastral['Id']
    dados['status'] = 1

    if 'documentos' in dir(evtAltCadastral.alteracao.dadosTrabalhador):
        for documentos in evtAltCadastral.alteracao.dadosTrabalhador.documentos:
            s2205_documentos_dados = {}
            s2205_documentos_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id
       
            insert = create_insert('s2205_documentos', s2205_documentos_dados)
            resp = executar_sql(insert, True)
            s2205_documentos_id = resp[0][0]
            #print s2205_documentos_id

            if 'CTPS' in dir(documentos):
                for CTPS in documentos.CTPS:
                    s2205_ctps_dados = {}
                    s2205_ctps_dados['s2205_documentos_id'] = s2205_documentos_id
               
                    if 'nrCtps' in dir(CTPS): s2205_ctps_dados['nrctps'] = CTPS.nrCtps.cdata
                    if 'serieCtps' in dir(CTPS): s2205_ctps_dados['seriectps'] = CTPS.serieCtps.cdata
                    if 'ufCtps' in dir(CTPS): s2205_ctps_dados['ufctps'] = CTPS.ufCtps.cdata
                    insert = create_insert('s2205_ctps', s2205_ctps_dados)
                    resp = executar_sql(insert, True)
                    s2205_ctps_id = resp[0][0]
                    #print s2205_ctps_id
   
            if 'RIC' in dir(documentos):
                for RIC in documentos.RIC:
                    s2205_ric_dados = {}
                    s2205_ric_dados['s2205_documentos_id'] = s2205_documentos_id
               
                    if 'nrRic' in dir(RIC): s2205_ric_dados['nrric'] = RIC.nrRic.cdata
                    if 'orgaoEmissor' in dir(RIC): s2205_ric_dados['orgaoemissor'] = RIC.orgaoEmissor.cdata
                    if 'dtExped' in dir(RIC): s2205_ric_dados['dtexped'] = RIC.dtExped.cdata
                    insert = create_insert('s2205_ric', s2205_ric_dados)
                    resp = executar_sql(insert, True)
                    s2205_ric_id = resp[0][0]
                    #print s2205_ric_id
   
            if 'RG' in dir(documentos):
                for RG in documentos.RG:
                    s2205_rg_dados = {}
                    s2205_rg_dados['s2205_documentos_id'] = s2205_documentos_id
               
                    if 'nrRg' in dir(RG): s2205_rg_dados['nrrg'] = RG.nrRg.cdata
                    if 'orgaoEmissor' in dir(RG): s2205_rg_dados['orgaoemissor'] = RG.orgaoEmissor.cdata
                    if 'dtExped' in dir(RG): s2205_rg_dados['dtexped'] = RG.dtExped.cdata
                    insert = create_insert('s2205_rg', s2205_rg_dados)
                    resp = executar_sql(insert, True)
                    s2205_rg_id = resp[0][0]
                    #print s2205_rg_id
   
            if 'RNE' in dir(documentos):
                for RNE in documentos.RNE:
                    s2205_rne_dados = {}
                    s2205_rne_dados['s2205_documentos_id'] = s2205_documentos_id
               
                    if 'nrRne' in dir(RNE): s2205_rne_dados['nrrne'] = RNE.nrRne.cdata
                    if 'orgaoEmissor' in dir(RNE): s2205_rne_dados['orgaoemissor'] = RNE.orgaoEmissor.cdata
                    if 'dtExped' in dir(RNE): s2205_rne_dados['dtexped'] = RNE.dtExped.cdata
                    insert = create_insert('s2205_rne', s2205_rne_dados)
                    resp = executar_sql(insert, True)
                    s2205_rne_id = resp[0][0]
                    #print s2205_rne_id
   
            if 'OC' in dir(documentos):
                for OC in documentos.OC:
                    s2205_oc_dados = {}
                    s2205_oc_dados['s2205_documentos_id'] = s2205_documentos_id
               
                    if 'nrOc' in dir(OC): s2205_oc_dados['nroc'] = OC.nrOc.cdata
                    if 'orgaoEmissor' in dir(OC): s2205_oc_dados['orgaoemissor'] = OC.orgaoEmissor.cdata
                    if 'dtExped' in dir(OC): s2205_oc_dados['dtexped'] = OC.dtExped.cdata
                    if 'dtValid' in dir(OC): s2205_oc_dados['dtvalid'] = OC.dtValid.cdata
                    insert = create_insert('s2205_oc', s2205_oc_dados)
                    resp = executar_sql(insert, True)
                    s2205_oc_id = resp[0][0]
                    #print s2205_oc_id
   
            if 'CNH' in dir(documentos):
                for CNH in documentos.CNH:
                    s2205_cnh_dados = {}
                    s2205_cnh_dados['s2205_documentos_id'] = s2205_documentos_id
               
                    if 'nrRegCnh' in dir(CNH): s2205_cnh_dados['nrregcnh'] = CNH.nrRegCnh.cdata
                    if 'dtExped' in dir(CNH): s2205_cnh_dados['dtexped'] = CNH.dtExped.cdata
                    if 'ufCnh' in dir(CNH): s2205_cnh_dados['ufcnh'] = CNH.ufCnh.cdata
                    if 'dtValid' in dir(CNH): s2205_cnh_dados['dtvalid'] = CNH.dtValid.cdata
                    if 'dtPriHab' in dir(CNH): s2205_cnh_dados['dtprihab'] = CNH.dtPriHab.cdata
                    if 'categoriaCnh' in dir(CNH): s2205_cnh_dados['categoriacnh'] = CNH.categoriaCnh.cdata
                    insert = create_insert('s2205_cnh', s2205_cnh_dados)
                    resp = executar_sql(insert, True)
                    s2205_cnh_id = resp[0][0]
                    #print s2205_cnh_id
   
    if 'brasil' in dir(evtAltCadastral.alteracao.dadosTrabalhador.endereco):
        for brasil in evtAltCadastral.alteracao.dadosTrabalhador.endereco.brasil:
            s2205_brasil_dados = {}
            s2205_brasil_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id
       
            if 'tpLograd' in dir(brasil): s2205_brasil_dados['tplograd'] = brasil.tpLograd.cdata
            if 'dscLograd' in dir(brasil): s2205_brasil_dados['dsclograd'] = brasil.dscLograd.cdata
            if 'nrLograd' in dir(brasil): s2205_brasil_dados['nrlograd'] = brasil.nrLograd.cdata
            if 'complemento' in dir(brasil): s2205_brasil_dados['complemento'] = brasil.complemento.cdata
            if 'bairro' in dir(brasil): s2205_brasil_dados['bairro'] = brasil.bairro.cdata
            if 'cep' in dir(brasil): s2205_brasil_dados['cep'] = brasil.cep.cdata
            if 'codMunic' in dir(brasil): s2205_brasil_dados['codmunic'] = brasil.codMunic.cdata
            if 'uf' in dir(brasil): s2205_brasil_dados['uf'] = brasil.uf.cdata
            insert = create_insert('s2205_brasil', s2205_brasil_dados)
            resp = executar_sql(insert, True)
            s2205_brasil_id = resp[0][0]
            #print s2205_brasil_id

    if 'exterior' in dir(evtAltCadastral.alteracao.dadosTrabalhador.endereco):
        for exterior in evtAltCadastral.alteracao.dadosTrabalhador.endereco.exterior:
            s2205_exterior_dados = {}
            s2205_exterior_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id
       
            if 'paisResid' in dir(exterior): s2205_exterior_dados['paisresid'] = exterior.paisResid.cdata
            if 'dscLograd' in dir(exterior): s2205_exterior_dados['dsclograd'] = exterior.dscLograd.cdata
            if 'nrLograd' in dir(exterior): s2205_exterior_dados['nrlograd'] = exterior.nrLograd.cdata
            if 'complemento' in dir(exterior): s2205_exterior_dados['complemento'] = exterior.complemento.cdata
            if 'bairro' in dir(exterior): s2205_exterior_dados['bairro'] = exterior.bairro.cdata
            if 'nmCid' in dir(exterior): s2205_exterior_dados['nmcid'] = exterior.nmCid.cdata
            if 'codPostal' in dir(exterior): s2205_exterior_dados['codpostal'] = exterior.codPostal.cdata
            insert = create_insert('s2205_exterior', s2205_exterior_dados)
            resp = executar_sql(insert, True)
            s2205_exterior_id = resp[0][0]
            #print s2205_exterior_id

    if 'trabEstrangeiro' in dir(evtAltCadastral.alteracao.dadosTrabalhador):
        for trabEstrangeiro in evtAltCadastral.alteracao.dadosTrabalhador.trabEstrangeiro:
            s2205_trabestrangeiro_dados = {}
            s2205_trabestrangeiro_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id
       
            if 'dtChegada' in dir(trabEstrangeiro): s2205_trabestrangeiro_dados['dtchegada'] = trabEstrangeiro.dtChegada.cdata
            if 'classTrabEstrang' in dir(trabEstrangeiro): s2205_trabestrangeiro_dados['classtrabestrang'] = trabEstrangeiro.classTrabEstrang.cdata
            if 'casadoBr' in dir(trabEstrangeiro): s2205_trabestrangeiro_dados['casadobr'] = trabEstrangeiro.casadoBr.cdata
            if 'filhosBr' in dir(trabEstrangeiro): s2205_trabestrangeiro_dados['filhosbr'] = trabEstrangeiro.filhosBr.cdata
            insert = create_insert('s2205_trabestrangeiro', s2205_trabestrangeiro_dados)
            resp = executar_sql(insert, True)
            s2205_trabestrangeiro_id = resp[0][0]
            #print s2205_trabestrangeiro_id

    if 'infoDeficiencia' in dir(evtAltCadastral.alteracao.dadosTrabalhador):
        for infoDeficiencia in evtAltCadastral.alteracao.dadosTrabalhador.infoDeficiencia:
            s2205_infodeficiencia_dados = {}
            s2205_infodeficiencia_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id
       
            if 'defFisica' in dir(infoDeficiencia): s2205_infodeficiencia_dados['deffisica'] = infoDeficiencia.defFisica.cdata
            if 'defVisual' in dir(infoDeficiencia): s2205_infodeficiencia_dados['defvisual'] = infoDeficiencia.defVisual.cdata
            if 'defAuditiva' in dir(infoDeficiencia): s2205_infodeficiencia_dados['defauditiva'] = infoDeficiencia.defAuditiva.cdata
            if 'defMental' in dir(infoDeficiencia): s2205_infodeficiencia_dados['defmental'] = infoDeficiencia.defMental.cdata
            if 'defIntelectual' in dir(infoDeficiencia): s2205_infodeficiencia_dados['defintelectual'] = infoDeficiencia.defIntelectual.cdata
            if 'reabReadap' in dir(infoDeficiencia): s2205_infodeficiencia_dados['reabreadap'] = infoDeficiencia.reabReadap.cdata
            if 'infoCota' in dir(infoDeficiencia): s2205_infodeficiencia_dados['infocota'] = infoDeficiencia.infoCota.cdata
            if 'observacao' in dir(infoDeficiencia): s2205_infodeficiencia_dados['observacao'] = infoDeficiencia.observacao.cdata
            insert = create_insert('s2205_infodeficiencia', s2205_infodeficiencia_dados)
            resp = executar_sql(insert, True)
            s2205_infodeficiencia_id = resp[0][0]
            #print s2205_infodeficiencia_id

    if 'dependente' in dir(evtAltCadastral.alteracao.dadosTrabalhador):
        for dependente in evtAltCadastral.alteracao.dadosTrabalhador.dependente:
            s2205_dependente_dados = {}
            s2205_dependente_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id
       
            if 'tpDep' in dir(dependente): s2205_dependente_dados['tpdep'] = dependente.tpDep.cdata
            if 'nmDep' in dir(dependente): s2205_dependente_dados['nmdep'] = dependente.nmDep.cdata
            if 'dtNascto' in dir(dependente): s2205_dependente_dados['dtnascto'] = dependente.dtNascto.cdata
            if 'cpfDep' in dir(dependente): s2205_dependente_dados['cpfdep'] = dependente.cpfDep.cdata
            if 'sexoDep' in dir(dependente): s2205_dependente_dados['sexodep'] = dependente.sexoDep.cdata
            if 'depIRRF' in dir(dependente): s2205_dependente_dados['depirrf'] = dependente.depIRRF.cdata
            if 'depSF' in dir(dependente): s2205_dependente_dados['depsf'] = dependente.depSF.cdata
            if 'incTrab' in dir(dependente): s2205_dependente_dados['inctrab'] = dependente.incTrab.cdata
            if 'depFinsPrev' in dir(dependente): s2205_dependente_dados['depfinsprev'] = dependente.depFinsPrev.cdata
            insert = create_insert('s2205_dependente', s2205_dependente_dados)
            resp = executar_sql(insert, True)
            s2205_dependente_id = resp[0][0]
            #print s2205_dependente_id

    if 'aposentadoria' in dir(evtAltCadastral.alteracao.dadosTrabalhador):
        for aposentadoria in evtAltCadastral.alteracao.dadosTrabalhador.aposentadoria:
            s2205_aposentadoria_dados = {}
            s2205_aposentadoria_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id
       
            if 'trabAposent' in dir(aposentadoria): s2205_aposentadoria_dados['trabaposent'] = aposentadoria.trabAposent.cdata
            insert = create_insert('s2205_aposentadoria', s2205_aposentadoria_dados)
            resp = executar_sql(insert, True)
            s2205_aposentadoria_id = resp[0][0]
            #print s2205_aposentadoria_id

    if 'contato' in dir(evtAltCadastral.alteracao.dadosTrabalhador):
        for contato in evtAltCadastral.alteracao.dadosTrabalhador.contato:
            s2205_contato_dados = {}
            s2205_contato_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id
       
            if 'fonePrinc' in dir(contato): s2205_contato_dados['foneprinc'] = contato.fonePrinc.cdata
            if 'foneAlternat' in dir(contato): s2205_contato_dados['fonealternat'] = contato.foneAlternat.cdata
            if 'emailPrinc' in dir(contato): s2205_contato_dados['emailprinc'] = contato.emailPrinc.cdata
            if 'emailAlternat' in dir(contato): s2205_contato_dados['emailalternat'] = contato.emailAlternat.cdata
            insert = create_insert('s2205_contato', s2205_contato_dados)
            resp = executar_sql(insert, True)
            s2205_contato_id = resp[0][0]
            #print s2205_contato_id

    from emensageriapro.esocial.views.s2205_evtaltcadastral_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2205_evtaltcadastral_id, 'default')
    return dados