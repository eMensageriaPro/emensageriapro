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


def read_s2200_evtadmissao_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2200_evtadmissao_obj(doc, status, validar)
    return dados

def read_s2200_evtadmissao(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2200_evtadmissao_obj(doc, status, validar)
    return dados



def read_s2200_evtadmissao_obj(doc, status, validar=False):
    s2200_evtadmissao_dados = {}
    s2200_evtadmissao_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2200_evtadmissao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2200_evtadmissao_dados['identidade'] = doc.eSocial.evtAdmissao['Id']
    s2200_evtadmissao_dados['processamento_codigo_resposta'] = 1
    evtAdmissao = doc.eSocial.evtAdmissao

    if 'indRetif' in dir(evtAdmissao.ideEvento): s2200_evtadmissao_dados['indretif'] = evtAdmissao.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtAdmissao.ideEvento): s2200_evtadmissao_dados['nrrecibo'] = evtAdmissao.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtAdmissao.ideEvento): s2200_evtadmissao_dados['tpamb'] = evtAdmissao.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtAdmissao.ideEvento): s2200_evtadmissao_dados['procemi'] = evtAdmissao.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtAdmissao.ideEvento): s2200_evtadmissao_dados['verproc'] = evtAdmissao.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtAdmissao.ideEmpregador): s2200_evtadmissao_dados['tpinsc'] = evtAdmissao.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtAdmissao.ideEmpregador): s2200_evtadmissao_dados['nrinsc'] = evtAdmissao.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtAdmissao.trabalhador): s2200_evtadmissao_dados['cpftrab'] = evtAdmissao.trabalhador.cpfTrab.cdata
    if 'nisTrab' in dir(evtAdmissao.trabalhador): s2200_evtadmissao_dados['nistrab'] = evtAdmissao.trabalhador.nisTrab.cdata
    if 'nmTrab' in dir(evtAdmissao.trabalhador): s2200_evtadmissao_dados['nmtrab'] = evtAdmissao.trabalhador.nmTrab.cdata
    if 'sexo' in dir(evtAdmissao.trabalhador): s2200_evtadmissao_dados['sexo'] = evtAdmissao.trabalhador.sexo.cdata
    if 'racaCor' in dir(evtAdmissao.trabalhador): s2200_evtadmissao_dados['racacor'] = evtAdmissao.trabalhador.racaCor.cdata
    if 'estCiv' in dir(evtAdmissao.trabalhador): s2200_evtadmissao_dados['estciv'] = evtAdmissao.trabalhador.estCiv.cdata
    if 'grauInstr' in dir(evtAdmissao.trabalhador): s2200_evtadmissao_dados['grauinstr'] = evtAdmissao.trabalhador.grauInstr.cdata
    if 'indPriEmpr' in dir(evtAdmissao.trabalhador): s2200_evtadmissao_dados['indpriempr'] = evtAdmissao.trabalhador.indPriEmpr.cdata
    if 'nmSoc' in dir(evtAdmissao.trabalhador): s2200_evtadmissao_dados['nmsoc'] = evtAdmissao.trabalhador.nmSoc.cdata
    if 'dtNascto' in dir(evtAdmissao.trabalhador.nascimento): s2200_evtadmissao_dados['dtnascto'] = evtAdmissao.trabalhador.nascimento.dtNascto.cdata
    if 'codMunic' in dir(evtAdmissao.trabalhador.nascimento): s2200_evtadmissao_dados['codmunic'] = evtAdmissao.trabalhador.nascimento.codMunic.cdata
    if 'uf' in dir(evtAdmissao.trabalhador.nascimento): s2200_evtadmissao_dados['uf'] = evtAdmissao.trabalhador.nascimento.uf.cdata
    if 'paisNascto' in dir(evtAdmissao.trabalhador.nascimento): s2200_evtadmissao_dados['paisnascto'] = evtAdmissao.trabalhador.nascimento.paisNascto.cdata
    if 'paisNac' in dir(evtAdmissao.trabalhador.nascimento): s2200_evtadmissao_dados['paisnac'] = evtAdmissao.trabalhador.nascimento.paisNac.cdata
    if 'nmMae' in dir(evtAdmissao.trabalhador.nascimento): s2200_evtadmissao_dados['nmmae'] = evtAdmissao.trabalhador.nascimento.nmMae.cdata
    if 'nmPai' in dir(evtAdmissao.trabalhador.nascimento): s2200_evtadmissao_dados['nmpai'] = evtAdmissao.trabalhador.nascimento.nmPai.cdata
    if 'matricula' in dir(evtAdmissao.vinculo): s2200_evtadmissao_dados['matricula'] = evtAdmissao.vinculo.matricula.cdata
    if 'tpRegTrab' in dir(evtAdmissao.vinculo): s2200_evtadmissao_dados['tpregtrab'] = evtAdmissao.vinculo.tpRegTrab.cdata
    if 'tpRegPrev' in dir(evtAdmissao.vinculo): s2200_evtadmissao_dados['tpregprev'] = evtAdmissao.vinculo.tpRegPrev.cdata
    if 'nrRecInfPrelim' in dir(evtAdmissao.vinculo): s2200_evtadmissao_dados['nrrecinfprelim'] = evtAdmissao.vinculo.nrRecInfPrelim.cdata
    if 'cadIni' in dir(evtAdmissao.vinculo): s2200_evtadmissao_dados['cadini'] = evtAdmissao.vinculo.cadIni.cdata
    if 'codCargo' in dir(evtAdmissao.vinculo.infoContrato): s2200_evtadmissao_dados['codcargo'] = evtAdmissao.vinculo.infoContrato.codCargo.cdata
    if 'dtIngrCargo' in dir(evtAdmissao.vinculo.infoContrato): s2200_evtadmissao_dados['dtingrcargo'] = evtAdmissao.vinculo.infoContrato.dtIngrCargo.cdata
    if 'codFuncao' in dir(evtAdmissao.vinculo.infoContrato): s2200_evtadmissao_dados['codfuncao'] = evtAdmissao.vinculo.infoContrato.codFuncao.cdata
    if 'codCateg' in dir(evtAdmissao.vinculo.infoContrato): s2200_evtadmissao_dados['codcateg'] = evtAdmissao.vinculo.infoContrato.codCateg.cdata
    if 'codCarreira' in dir(evtAdmissao.vinculo.infoContrato): s2200_evtadmissao_dados['codcarreira'] = evtAdmissao.vinculo.infoContrato.codCarreira.cdata
    if 'dtIngrCarr' in dir(evtAdmissao.vinculo.infoContrato): s2200_evtadmissao_dados['dtingrcarr'] = evtAdmissao.vinculo.infoContrato.dtIngrCarr.cdata
    if 'vrSalFx' in dir(evtAdmissao.vinculo.infoContrato.remuneracao): s2200_evtadmissao_dados['vrsalfx'] = evtAdmissao.vinculo.infoContrato.remuneracao.vrSalFx.cdata
    if 'undSalFixo' in dir(evtAdmissao.vinculo.infoContrato.remuneracao): s2200_evtadmissao_dados['undsalfixo'] = evtAdmissao.vinculo.infoContrato.remuneracao.undSalFixo.cdata
    if 'dscSalVar' in dir(evtAdmissao.vinculo.infoContrato.remuneracao): s2200_evtadmissao_dados['dscsalvar'] = evtAdmissao.vinculo.infoContrato.remuneracao.dscSalVar.cdata
    if 'tpContr' in dir(evtAdmissao.vinculo.infoContrato.duracao): s2200_evtadmissao_dados['tpcontr'] = evtAdmissao.vinculo.infoContrato.duracao.tpContr.cdata
    if 'dtTerm' in dir(evtAdmissao.vinculo.infoContrato.duracao): s2200_evtadmissao_dados['dtterm'] = evtAdmissao.vinculo.infoContrato.duracao.dtTerm.cdata
    if 'clauAssec' in dir(evtAdmissao.vinculo.infoContrato.duracao): s2200_evtadmissao_dados['clauassec'] = evtAdmissao.vinculo.infoContrato.duracao.clauAssec.cdata
    if 'inclusao' in dir(evtAdmissao.vinculo): s2200_evtadmissao_dados['operacao'] = 1
    elif 'alteracao' in dir(evtAdmissao.vinculo): s2200_evtadmissao_dados['operacao'] = 2
    elif 'exclusao' in dir(evtAdmissao.vinculo): s2200_evtadmissao_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2200_evtadmissao', s2200_evtadmissao_dados)
    resp = executar_sql(insert, True)
    s2200_evtadmissao_id = resp[0][0]
    dados = s2200_evtadmissao_dados
    dados['evento'] = 's2200'
    dados['id'] = s2200_evtadmissao_id
    dados['identidade_evento'] = doc.eSocial.evtAdmissao['Id']
    dados['status'] = 1

    if 'documentos' in dir(evtAdmissao.trabalhador):
        for documentos in evtAdmissao.trabalhador.documentos:
            s2200_documentos_dados = {}
            s2200_documentos_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            insert = create_insert('s2200_documentos', s2200_documentos_dados)
            resp = executar_sql(insert, True)
            s2200_documentos_id = resp[0][0]
            #print s2200_documentos_id

            if 'CTPS' in dir(documentos):
                for CTPS in documentos.CTPS:
                    s2200_ctps_dados = {}
                    s2200_ctps_dados['s2200_documentos_id'] = s2200_documentos_id
               
                    if 'nrCtps' in dir(CTPS): s2200_ctps_dados['nrctps'] = CTPS.nrCtps.cdata
                    if 'serieCtps' in dir(CTPS): s2200_ctps_dados['seriectps'] = CTPS.serieCtps.cdata
                    if 'ufCtps' in dir(CTPS): s2200_ctps_dados['ufctps'] = CTPS.ufCtps.cdata
                    insert = create_insert('s2200_ctps', s2200_ctps_dados)
                    resp = executar_sql(insert, True)
                    s2200_ctps_id = resp[0][0]
                    #print s2200_ctps_id
   
            if 'RIC' in dir(documentos):
                for RIC in documentos.RIC:
                    s2200_ric_dados = {}
                    s2200_ric_dados['s2200_documentos_id'] = s2200_documentos_id
               
                    if 'nrRic' in dir(RIC): s2200_ric_dados['nrric'] = RIC.nrRic.cdata
                    if 'orgaoEmissor' in dir(RIC): s2200_ric_dados['orgaoemissor'] = RIC.orgaoEmissor.cdata
                    if 'dtExped' in dir(RIC): s2200_ric_dados['dtexped'] = RIC.dtExped.cdata
                    insert = create_insert('s2200_ric', s2200_ric_dados)
                    resp = executar_sql(insert, True)
                    s2200_ric_id = resp[0][0]
                    #print s2200_ric_id
   
            if 'RG' in dir(documentos):
                for RG in documentos.RG:
                    s2200_rg_dados = {}
                    s2200_rg_dados['s2200_documentos_id'] = s2200_documentos_id
               
                    if 'nrRg' in dir(RG): s2200_rg_dados['nrrg'] = RG.nrRg.cdata
                    if 'orgaoEmissor' in dir(RG): s2200_rg_dados['orgaoemissor'] = RG.orgaoEmissor.cdata
                    if 'dtExped' in dir(RG): s2200_rg_dados['dtexped'] = RG.dtExped.cdata
                    insert = create_insert('s2200_rg', s2200_rg_dados)
                    resp = executar_sql(insert, True)
                    s2200_rg_id = resp[0][0]
                    #print s2200_rg_id
   
            if 'RNE' in dir(documentos):
                for RNE in documentos.RNE:
                    s2200_rne_dados = {}
                    s2200_rne_dados['s2200_documentos_id'] = s2200_documentos_id
               
                    if 'nrRne' in dir(RNE): s2200_rne_dados['nrrne'] = RNE.nrRne.cdata
                    if 'orgaoEmissor' in dir(RNE): s2200_rne_dados['orgaoemissor'] = RNE.orgaoEmissor.cdata
                    if 'dtExped' in dir(RNE): s2200_rne_dados['dtexped'] = RNE.dtExped.cdata
                    insert = create_insert('s2200_rne', s2200_rne_dados)
                    resp = executar_sql(insert, True)
                    s2200_rne_id = resp[0][0]
                    #print s2200_rne_id
   
            if 'OC' in dir(documentos):
                for OC in documentos.OC:
                    s2200_oc_dados = {}
                    s2200_oc_dados['s2200_documentos_id'] = s2200_documentos_id
               
                    if 'nrOc' in dir(OC): s2200_oc_dados['nroc'] = OC.nrOc.cdata
                    if 'orgaoEmissor' in dir(OC): s2200_oc_dados['orgaoemissor'] = OC.orgaoEmissor.cdata
                    if 'dtExped' in dir(OC): s2200_oc_dados['dtexped'] = OC.dtExped.cdata
                    if 'dtValid' in dir(OC): s2200_oc_dados['dtvalid'] = OC.dtValid.cdata
                    insert = create_insert('s2200_oc', s2200_oc_dados)
                    resp = executar_sql(insert, True)
                    s2200_oc_id = resp[0][0]
                    #print s2200_oc_id
   
            if 'CNH' in dir(documentos):
                for CNH in documentos.CNH:
                    s2200_cnh_dados = {}
                    s2200_cnh_dados['s2200_documentos_id'] = s2200_documentos_id
               
                    if 'nrRegCnh' in dir(CNH): s2200_cnh_dados['nrregcnh'] = CNH.nrRegCnh.cdata
                    if 'dtExped' in dir(CNH): s2200_cnh_dados['dtexped'] = CNH.dtExped.cdata
                    if 'ufCnh' in dir(CNH): s2200_cnh_dados['ufcnh'] = CNH.ufCnh.cdata
                    if 'dtValid' in dir(CNH): s2200_cnh_dados['dtvalid'] = CNH.dtValid.cdata
                    if 'dtPriHab' in dir(CNH): s2200_cnh_dados['dtprihab'] = CNH.dtPriHab.cdata
                    if 'categoriaCnh' in dir(CNH): s2200_cnh_dados['categoriacnh'] = CNH.categoriaCnh.cdata
                    insert = create_insert('s2200_cnh', s2200_cnh_dados)
                    resp = executar_sql(insert, True)
                    s2200_cnh_id = resp[0][0]
                    #print s2200_cnh_id
   
    if 'brasil' in dir(evtAdmissao.trabalhador.endereco):
        for brasil in evtAdmissao.trabalhador.endereco.brasil:
            s2200_brasil_dados = {}
            s2200_brasil_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'tpLograd' in dir(brasil): s2200_brasil_dados['tplograd'] = brasil.tpLograd.cdata
            if 'dscLograd' in dir(brasil): s2200_brasil_dados['dsclograd'] = brasil.dscLograd.cdata
            if 'nrLograd' in dir(brasil): s2200_brasil_dados['nrlograd'] = brasil.nrLograd.cdata
            if 'complemento' in dir(brasil): s2200_brasil_dados['complemento'] = brasil.complemento.cdata
            if 'bairro' in dir(brasil): s2200_brasil_dados['bairro'] = brasil.bairro.cdata
            if 'cep' in dir(brasil): s2200_brasil_dados['cep'] = brasil.cep.cdata
            if 'codMunic' in dir(brasil): s2200_brasil_dados['codmunic'] = brasil.codMunic.cdata
            if 'uf' in dir(brasil): s2200_brasil_dados['uf'] = brasil.uf.cdata
            insert = create_insert('s2200_brasil', s2200_brasil_dados)
            resp = executar_sql(insert, True)
            s2200_brasil_id = resp[0][0]
            #print s2200_brasil_id

    if 'exterior' in dir(evtAdmissao.trabalhador.endereco):
        for exterior in evtAdmissao.trabalhador.endereco.exterior:
            s2200_exterior_dados = {}
            s2200_exterior_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'paisResid' in dir(exterior): s2200_exterior_dados['paisresid'] = exterior.paisResid.cdata
            if 'dscLograd' in dir(exterior): s2200_exterior_dados['dsclograd'] = exterior.dscLograd.cdata
            if 'nrLograd' in dir(exterior): s2200_exterior_dados['nrlograd'] = exterior.nrLograd.cdata
            if 'complemento' in dir(exterior): s2200_exterior_dados['complemento'] = exterior.complemento.cdata
            if 'bairro' in dir(exterior): s2200_exterior_dados['bairro'] = exterior.bairro.cdata
            if 'nmCid' in dir(exterior): s2200_exterior_dados['nmcid'] = exterior.nmCid.cdata
            if 'codPostal' in dir(exterior): s2200_exterior_dados['codpostal'] = exterior.codPostal.cdata
            insert = create_insert('s2200_exterior', s2200_exterior_dados)
            resp = executar_sql(insert, True)
            s2200_exterior_id = resp[0][0]
            #print s2200_exterior_id

    if 'trabEstrangeiro' in dir(evtAdmissao.trabalhador):
        for trabEstrangeiro in evtAdmissao.trabalhador.trabEstrangeiro:
            s2200_trabestrangeiro_dados = {}
            s2200_trabestrangeiro_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'dtChegada' in dir(trabEstrangeiro): s2200_trabestrangeiro_dados['dtchegada'] = trabEstrangeiro.dtChegada.cdata
            if 'classTrabEstrang' in dir(trabEstrangeiro): s2200_trabestrangeiro_dados['classtrabestrang'] = trabEstrangeiro.classTrabEstrang.cdata
            if 'casadoBr' in dir(trabEstrangeiro): s2200_trabestrangeiro_dados['casadobr'] = trabEstrangeiro.casadoBr.cdata
            if 'filhosBr' in dir(trabEstrangeiro): s2200_trabestrangeiro_dados['filhosbr'] = trabEstrangeiro.filhosBr.cdata
            insert = create_insert('s2200_trabestrangeiro', s2200_trabestrangeiro_dados)
            resp = executar_sql(insert, True)
            s2200_trabestrangeiro_id = resp[0][0]
            #print s2200_trabestrangeiro_id

    if 'infoDeficiencia' in dir(evtAdmissao.trabalhador):
        for infoDeficiencia in evtAdmissao.trabalhador.infoDeficiencia:
            s2200_infodeficiencia_dados = {}
            s2200_infodeficiencia_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'defFisica' in dir(infoDeficiencia): s2200_infodeficiencia_dados['deffisica'] = infoDeficiencia.defFisica.cdata
            if 'defVisual' in dir(infoDeficiencia): s2200_infodeficiencia_dados['defvisual'] = infoDeficiencia.defVisual.cdata
            if 'defAuditiva' in dir(infoDeficiencia): s2200_infodeficiencia_dados['defauditiva'] = infoDeficiencia.defAuditiva.cdata
            if 'defMental' in dir(infoDeficiencia): s2200_infodeficiencia_dados['defmental'] = infoDeficiencia.defMental.cdata
            if 'defIntelectual' in dir(infoDeficiencia): s2200_infodeficiencia_dados['defintelectual'] = infoDeficiencia.defIntelectual.cdata
            if 'reabReadap' in dir(infoDeficiencia): s2200_infodeficiencia_dados['reabreadap'] = infoDeficiencia.reabReadap.cdata
            if 'infoCota' in dir(infoDeficiencia): s2200_infodeficiencia_dados['infocota'] = infoDeficiencia.infoCota.cdata
            if 'observacao' in dir(infoDeficiencia): s2200_infodeficiencia_dados['observacao'] = infoDeficiencia.observacao.cdata
            insert = create_insert('s2200_infodeficiencia', s2200_infodeficiencia_dados)
            resp = executar_sql(insert, True)
            s2200_infodeficiencia_id = resp[0][0]
            #print s2200_infodeficiencia_id

    if 'dependente' in dir(evtAdmissao.trabalhador):
        for dependente in evtAdmissao.trabalhador.dependente:
            s2200_dependente_dados = {}
            s2200_dependente_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'tpDep' in dir(dependente): s2200_dependente_dados['tpdep'] = dependente.tpDep.cdata
            if 'nmDep' in dir(dependente): s2200_dependente_dados['nmdep'] = dependente.nmDep.cdata
            if 'dtNascto' in dir(dependente): s2200_dependente_dados['dtnascto'] = dependente.dtNascto.cdata
            if 'cpfDep' in dir(dependente): s2200_dependente_dados['cpfdep'] = dependente.cpfDep.cdata
            if 'sexoDep' in dir(dependente): s2200_dependente_dados['sexodep'] = dependente.sexoDep.cdata
            if 'depIRRF' in dir(dependente): s2200_dependente_dados['depirrf'] = dependente.depIRRF.cdata
            if 'depSF' in dir(dependente): s2200_dependente_dados['depsf'] = dependente.depSF.cdata
            if 'incTrab' in dir(dependente): s2200_dependente_dados['inctrab'] = dependente.incTrab.cdata
            if 'depFinsPrev' in dir(dependente): s2200_dependente_dados['depfinsprev'] = dependente.depFinsPrev.cdata
            insert = create_insert('s2200_dependente', s2200_dependente_dados)
            resp = executar_sql(insert, True)
            s2200_dependente_id = resp[0][0]
            #print s2200_dependente_id

    if 'aposentadoria' in dir(evtAdmissao.trabalhador):
        for aposentadoria in evtAdmissao.trabalhador.aposentadoria:
            s2200_aposentadoria_dados = {}
            s2200_aposentadoria_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'trabAposent' in dir(aposentadoria): s2200_aposentadoria_dados['trabaposent'] = aposentadoria.trabAposent.cdata
            insert = create_insert('s2200_aposentadoria', s2200_aposentadoria_dados)
            resp = executar_sql(insert, True)
            s2200_aposentadoria_id = resp[0][0]
            #print s2200_aposentadoria_id

    if 'contato' in dir(evtAdmissao.trabalhador):
        for contato in evtAdmissao.trabalhador.contato:
            s2200_contato_dados = {}
            s2200_contato_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'fonePrinc' in dir(contato): s2200_contato_dados['foneprinc'] = contato.fonePrinc.cdata
            if 'foneAlternat' in dir(contato): s2200_contato_dados['fonealternat'] = contato.foneAlternat.cdata
            if 'emailPrinc' in dir(contato): s2200_contato_dados['emailprinc'] = contato.emailPrinc.cdata
            if 'emailAlternat' in dir(contato): s2200_contato_dados['emailalternat'] = contato.emailAlternat.cdata
            insert = create_insert('s2200_contato', s2200_contato_dados)
            resp = executar_sql(insert, True)
            s2200_contato_id = resp[0][0]
            #print s2200_contato_id

    if 'infoCeletista' in dir(evtAdmissao.vinculo.infoRegimeTrab):
        for infoCeletista in evtAdmissao.vinculo.infoRegimeTrab.infoCeletista:
            s2200_infoceletista_dados = {}
            s2200_infoceletista_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'dtAdm' in dir(infoCeletista): s2200_infoceletista_dados['dtadm'] = infoCeletista.dtAdm.cdata
            if 'tpAdmissao' in dir(infoCeletista): s2200_infoceletista_dados['tpadmissao'] = infoCeletista.tpAdmissao.cdata
            if 'indAdmissao' in dir(infoCeletista): s2200_infoceletista_dados['indadmissao'] = infoCeletista.indAdmissao.cdata
            if 'tpRegJor' in dir(infoCeletista): s2200_infoceletista_dados['tpregjor'] = infoCeletista.tpRegJor.cdata
            if 'natAtividade' in dir(infoCeletista): s2200_infoceletista_dados['natatividade'] = infoCeletista.natAtividade.cdata
            if 'dtBase' in dir(infoCeletista): s2200_infoceletista_dados['dtbase'] = infoCeletista.dtBase.cdata
            if 'cnpjSindCategProf' in dir(infoCeletista): s2200_infoceletista_dados['cnpjsindcategprof'] = infoCeletista.cnpjSindCategProf.cdata
            if 'opcFGTS' in dir(infoCeletista.FGTS): s2200_infoceletista_dados['opcfgts'] = infoCeletista.FGTS.opcFGTS.cdata
            if 'dtOpcFGTS' in dir(infoCeletista.FGTS): s2200_infoceletista_dados['dtopcfgts'] = infoCeletista.FGTS.dtOpcFGTS.cdata
            insert = create_insert('s2200_infoceletista', s2200_infoceletista_dados)
            resp = executar_sql(insert, True)
            s2200_infoceletista_id = resp[0][0]
            #print s2200_infoceletista_id

            if 'trabTemporario' in dir(infoCeletista):
                for trabTemporario in infoCeletista.trabTemporario:
                    s2200_trabtemporario_dados = {}
                    s2200_trabtemporario_dados['s2200_infoceletista_id'] = s2200_infoceletista_id
               
                    if 'hipLeg' in dir(trabTemporario): s2200_trabtemporario_dados['hipleg'] = trabTemporario.hipLeg.cdata
                    if 'justContr' in dir(trabTemporario): s2200_trabtemporario_dados['justcontr'] = trabTemporario.justContr.cdata
                    if 'tpInclContr' in dir(trabTemporario): s2200_trabtemporario_dados['tpinclcontr'] = trabTemporario.tpInclContr.cdata
                    if 'tpInsc' in dir(trabTemporario): s2200_trabtemporario_dados['tpinsc'] = trabTemporario.ideTomadorServ.tpInsc.cdata
                    if 'nrInsc' in dir(trabTemporario): s2200_trabtemporario_dados['nrinsc'] = trabTemporario.ideTomadorServ.nrInsc.cdata
                    insert = create_insert('s2200_trabtemporario', s2200_trabtemporario_dados)
                    resp = executar_sql(insert, True)
                    s2200_trabtemporario_id = resp[0][0]
                    #print s2200_trabtemporario_id
   
            if 'aprend' in dir(infoCeletista):
                for aprend in infoCeletista.aprend:
                    s2200_aprend_dados = {}
                    s2200_aprend_dados['s2200_infoceletista_id'] = s2200_infoceletista_id
               
                    if 'tpInsc' in dir(aprend): s2200_aprend_dados['tpinsc'] = aprend.tpInsc.cdata
                    if 'nrInsc' in dir(aprend): s2200_aprend_dados['nrinsc'] = aprend.nrInsc.cdata
                    insert = create_insert('s2200_aprend', s2200_aprend_dados)
                    resp = executar_sql(insert, True)
                    s2200_aprend_id = resp[0][0]
                    #print s2200_aprend_id
   
    if 'infoEstatutario' in dir(evtAdmissao.vinculo.infoRegimeTrab):
        for infoEstatutario in evtAdmissao.vinculo.infoRegimeTrab.infoEstatutario:
            s2200_infoestatutario_dados = {}
            s2200_infoestatutario_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'indProvim' in dir(infoEstatutario): s2200_infoestatutario_dados['indprovim'] = infoEstatutario.indProvim.cdata
            if 'tpProv' in dir(infoEstatutario): s2200_infoestatutario_dados['tpprov'] = infoEstatutario.tpProv.cdata
            if 'dtNomeacao' in dir(infoEstatutario): s2200_infoestatutario_dados['dtnomeacao'] = infoEstatutario.dtNomeacao.cdata
            if 'dtPosse' in dir(infoEstatutario): s2200_infoestatutario_dados['dtposse'] = infoEstatutario.dtPosse.cdata
            if 'dtExercicio' in dir(infoEstatutario): s2200_infoestatutario_dados['dtexercicio'] = infoEstatutario.dtExercicio.cdata
            if 'dtIngSvPub' in dir(infoEstatutario): s2200_infoestatutario_dados['dtingsvpub'] = infoEstatutario.dtIngSvPub.cdata
            if 'tpPlanRP' in dir(infoEstatutario): s2200_infoestatutario_dados['tpplanrp'] = infoEstatutario.tpPlanRP.cdata
            if 'indTetoRGPS' in dir(infoEstatutario): s2200_infoestatutario_dados['indtetorgps'] = infoEstatutario.indTetoRGPS.cdata
            if 'indAbonoPerm' in dir(infoEstatutario): s2200_infoestatutario_dados['indabonoperm'] = infoEstatutario.indAbonoPerm.cdata
            if 'dtIniAbono' in dir(infoEstatutario): s2200_infoestatutario_dados['dtiniabono'] = infoEstatutario.dtIniAbono.cdata
            if 'indParcRemun' in dir(infoEstatutario): s2200_infoestatutario_dados['indparcremun'] = infoEstatutario.indParcRemun.cdata
            if 'dtIniParc' in dir(infoEstatutario): s2200_infoestatutario_dados['dtiniparc'] = infoEstatutario.dtIniParc.cdata
            insert = create_insert('s2200_infoestatutario', s2200_infoestatutario_dados)
            resp = executar_sql(insert, True)
            s2200_infoestatutario_id = resp[0][0]
            #print s2200_infoestatutario_id

            if 'infoDecJud' in dir(infoEstatutario):
                for infoDecJud in infoEstatutario.infoDecJud:
                    s2200_infodecjud_dados = {}
                    s2200_infodecjud_dados['s2200_infoestatutario_id'] = s2200_infoestatutario_id
               
                    if 'nrProcJud' in dir(infoDecJud): s2200_infodecjud_dados['nrprocjud'] = infoDecJud.nrProcJud.cdata
                    insert = create_insert('s2200_infodecjud', s2200_infodecjud_dados)
                    resp = executar_sql(insert, True)
                    s2200_infodecjud_id = resp[0][0]
                    #print s2200_infodecjud_id
   
    if 'localTrabGeral' in dir(evtAdmissao.vinculo.infoContrato.localTrabalho):
        for localTrabGeral in evtAdmissao.vinculo.infoContrato.localTrabalho.localTrabGeral:
            s2200_localtrabgeral_dados = {}
            s2200_localtrabgeral_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'tpInsc' in dir(localTrabGeral): s2200_localtrabgeral_dados['tpinsc'] = localTrabGeral.tpInsc.cdata
            if 'nrInsc' in dir(localTrabGeral): s2200_localtrabgeral_dados['nrinsc'] = localTrabGeral.nrInsc.cdata
            if 'descComp' in dir(localTrabGeral): s2200_localtrabgeral_dados['desccomp'] = localTrabGeral.descComp.cdata
            insert = create_insert('s2200_localtrabgeral', s2200_localtrabgeral_dados)
            resp = executar_sql(insert, True)
            s2200_localtrabgeral_id = resp[0][0]
            #print s2200_localtrabgeral_id

    if 'localTrabDom' in dir(evtAdmissao.vinculo.infoContrato.localTrabalho):
        for localTrabDom in evtAdmissao.vinculo.infoContrato.localTrabalho.localTrabDom:
            s2200_localtrabdom_dados = {}
            s2200_localtrabdom_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'tpLograd' in dir(localTrabDom): s2200_localtrabdom_dados['tplograd'] = localTrabDom.tpLograd.cdata
            if 'dscLograd' in dir(localTrabDom): s2200_localtrabdom_dados['dsclograd'] = localTrabDom.dscLograd.cdata
            if 'nrLograd' in dir(localTrabDom): s2200_localtrabdom_dados['nrlograd'] = localTrabDom.nrLograd.cdata
            if 'complemento' in dir(localTrabDom): s2200_localtrabdom_dados['complemento'] = localTrabDom.complemento.cdata
            if 'bairro' in dir(localTrabDom): s2200_localtrabdom_dados['bairro'] = localTrabDom.bairro.cdata
            if 'cep' in dir(localTrabDom): s2200_localtrabdom_dados['cep'] = localTrabDom.cep.cdata
            if 'codMunic' in dir(localTrabDom): s2200_localtrabdom_dados['codmunic'] = localTrabDom.codMunic.cdata
            if 'uf' in dir(localTrabDom): s2200_localtrabdom_dados['uf'] = localTrabDom.uf.cdata
            insert = create_insert('s2200_localtrabdom', s2200_localtrabdom_dados)
            resp = executar_sql(insert, True)
            s2200_localtrabdom_id = resp[0][0]
            #print s2200_localtrabdom_id

    if 'horContratual' in dir(evtAdmissao.vinculo.infoContrato):
        for horContratual in evtAdmissao.vinculo.infoContrato.horContratual:
            s2200_horcontratual_dados = {}
            s2200_horcontratual_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'qtdHrsSem' in dir(horContratual): s2200_horcontratual_dados['qtdhrssem'] = horContratual.qtdHrsSem.cdata
            if 'tpJornada' in dir(horContratual): s2200_horcontratual_dados['tpjornada'] = horContratual.tpJornada.cdata
            if 'dscTpJorn' in dir(horContratual): s2200_horcontratual_dados['dsctpjorn'] = horContratual.dscTpJorn.cdata
            if 'tmpParc' in dir(horContratual): s2200_horcontratual_dados['tmpparc'] = horContratual.tmpParc.cdata
            insert = create_insert('s2200_horcontratual', s2200_horcontratual_dados)
            resp = executar_sql(insert, True)
            s2200_horcontratual_id = resp[0][0]
            #print s2200_horcontratual_id

            if 'horario' in dir(horContratual):
                for horario in horContratual.horario:
                    s2200_horario_dados = {}
                    s2200_horario_dados['s2200_horcontratual_id'] = s2200_horcontratual_id
               
                    if 'dia' in dir(horario): s2200_horario_dados['dia'] = horario.dia.cdata
                    if 'codHorContrat' in dir(horario): s2200_horario_dados['codhorcontrat'] = horario.codHorContrat.cdata
                    insert = create_insert('s2200_horario', s2200_horario_dados)
                    resp = executar_sql(insert, True)
                    s2200_horario_id = resp[0][0]
                    #print s2200_horario_id
   
    if 'filiacaoSindical' in dir(evtAdmissao.vinculo.infoContrato):
        for filiacaoSindical in evtAdmissao.vinculo.infoContrato.filiacaoSindical:
            s2200_filiacaosindical_dados = {}
            s2200_filiacaosindical_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'cnpjSindTrab' in dir(filiacaoSindical): s2200_filiacaosindical_dados['cnpjsindtrab'] = filiacaoSindical.cnpjSindTrab.cdata
            insert = create_insert('s2200_filiacaosindical', s2200_filiacaosindical_dados)
            resp = executar_sql(insert, True)
            s2200_filiacaosindical_id = resp[0][0]
            #print s2200_filiacaosindical_id

    if 'alvaraJudicial' in dir(evtAdmissao.vinculo.infoContrato):
        for alvaraJudicial in evtAdmissao.vinculo.infoContrato.alvaraJudicial:
            s2200_alvarajudicial_dados = {}
            s2200_alvarajudicial_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'nrProcJud' in dir(alvaraJudicial): s2200_alvarajudicial_dados['nrprocjud'] = alvaraJudicial.nrProcJud.cdata
            insert = create_insert('s2200_alvarajudicial', s2200_alvarajudicial_dados)
            resp = executar_sql(insert, True)
            s2200_alvarajudicial_id = resp[0][0]
            #print s2200_alvarajudicial_id

    if 'observacoes' in dir(evtAdmissao.vinculo.infoContrato):
        for observacoes in evtAdmissao.vinculo.infoContrato.observacoes:
            s2200_observacoes_dados = {}
            s2200_observacoes_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'observacao' in dir(observacoes): s2200_observacoes_dados['observacao'] = observacoes.observacao.cdata
            insert = create_insert('s2200_observacoes', s2200_observacoes_dados)
            resp = executar_sql(insert, True)
            s2200_observacoes_id = resp[0][0]
            #print s2200_observacoes_id

    if 'sucessaoVinc' in dir(evtAdmissao.vinculo):
        for sucessaoVinc in evtAdmissao.vinculo.sucessaoVinc:
            s2200_sucessaovinc_dados = {}
            s2200_sucessaovinc_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'cnpjEmpregAnt' in dir(sucessaoVinc): s2200_sucessaovinc_dados['cnpjempregant'] = sucessaoVinc.cnpjEmpregAnt.cdata
            if 'matricAnt' in dir(sucessaoVinc): s2200_sucessaovinc_dados['matricant'] = sucessaoVinc.matricAnt.cdata
            if 'dtTransf' in dir(sucessaoVinc): s2200_sucessaovinc_dados['dttransf'] = sucessaoVinc.dtTransf.cdata
            if 'observacao' in dir(sucessaoVinc): s2200_sucessaovinc_dados['observacao'] = sucessaoVinc.observacao.cdata
            insert = create_insert('s2200_sucessaovinc', s2200_sucessaovinc_dados)
            resp = executar_sql(insert, True)
            s2200_sucessaovinc_id = resp[0][0]
            #print s2200_sucessaovinc_id

    if 'transfDom' in dir(evtAdmissao.vinculo):
        for transfDom in evtAdmissao.vinculo.transfDom:
            s2200_transfdom_dados = {}
            s2200_transfdom_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'cpfSubstituido' in dir(transfDom): s2200_transfdom_dados['cpfsubstituido'] = transfDom.cpfSubstituido.cdata
            if 'matricAnt' in dir(transfDom): s2200_transfdom_dados['matricant'] = transfDom.matricAnt.cdata
            if 'dtTransf' in dir(transfDom): s2200_transfdom_dados['dttransf'] = transfDom.dtTransf.cdata
            insert = create_insert('s2200_transfdom', s2200_transfdom_dados)
            resp = executar_sql(insert, True)
            s2200_transfdom_id = resp[0][0]
            #print s2200_transfdom_id

    if 'afastamento' in dir(evtAdmissao.vinculo):
        for afastamento in evtAdmissao.vinculo.afastamento:
            s2200_afastamento_dados = {}
            s2200_afastamento_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'dtIniAfast' in dir(afastamento): s2200_afastamento_dados['dtiniafast'] = afastamento.dtIniAfast.cdata
            if 'codMotAfast' in dir(afastamento): s2200_afastamento_dados['codmotafast'] = afastamento.codMotAfast.cdata
            insert = create_insert('s2200_afastamento', s2200_afastamento_dados)
            resp = executar_sql(insert, True)
            s2200_afastamento_id = resp[0][0]
            #print s2200_afastamento_id

    if 'desligamento' in dir(evtAdmissao.vinculo):
        for desligamento in evtAdmissao.vinculo.desligamento:
            s2200_desligamento_dados = {}
            s2200_desligamento_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'dtDeslig' in dir(desligamento): s2200_desligamento_dados['dtdeslig'] = desligamento.dtDeslig.cdata
            insert = create_insert('s2200_desligamento', s2200_desligamento_dados)
            resp = executar_sql(insert, True)
            s2200_desligamento_id = resp[0][0]
            #print s2200_desligamento_id

    if 'cessao' in dir(evtAdmissao.vinculo):
        for cessao in evtAdmissao.vinculo.cessao:
            s2200_cessao_dados = {}
            s2200_cessao_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id
       
            if 'dtIniCessao' in dir(cessao): s2200_cessao_dados['dtinicessao'] = cessao.dtIniCessao.cdata
            insert = create_insert('s2200_cessao', s2200_cessao_dados)
            resp = executar_sql(insert, True)
            s2200_cessao_id = resp[0][0]
            #print s2200_cessao_id

    from emensageriapro.esocial.views.s2200_evtadmissao_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2200_evtadmissao_id, 'default')
    return dados