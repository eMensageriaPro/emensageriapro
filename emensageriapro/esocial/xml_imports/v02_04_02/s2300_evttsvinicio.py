#coding:utf-8
"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos<www.emensageria.com.br>
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


def read_s2300_evttsvinicio(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    read_s2300_evttsvinicio_obj(doc, status)



def read_s2300_evttsvinicio_obj(doc):
    s2300_evttsvinicio_dados = {}
    s2300_evttsvinicio_dados['versao'] = 'v02_04_02'
    s2300_evttsvinicio_dados['status'] = status
    s2300_evttsvinicio_dados['identidade'] = doc.eSocial.evtTSVInicio['Id']
    s2300_evttsvinicio_dados['processamento_codigo_resposta'] = 1
    evtTSVInicio = doc.eSocial.evtTSVInicio
    
    if 'indRetif' in dir(evtTSVInicio.ideEvento): s2300_evttsvinicio_dados['indretif'] = evtTSVInicio.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtTSVInicio.ideEvento): s2300_evttsvinicio_dados['nrrecibo'] = evtTSVInicio.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtTSVInicio.ideEvento): s2300_evttsvinicio_dados['tpamb'] = evtTSVInicio.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTSVInicio.ideEvento): s2300_evttsvinicio_dados['procemi'] = evtTSVInicio.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTSVInicio.ideEvento): s2300_evttsvinicio_dados['verproc'] = evtTSVInicio.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTSVInicio.ideEmpregador): s2300_evttsvinicio_dados['tpinsc'] = evtTSVInicio.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTSVInicio.ideEmpregador): s2300_evttsvinicio_dados['nrinsc'] = evtTSVInicio.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtTSVInicio.trabalhador): s2300_evttsvinicio_dados['cpftrab'] = evtTSVInicio.trabalhador.cpfTrab.cdata
    if 'nisTrab' in dir(evtTSVInicio.trabalhador): s2300_evttsvinicio_dados['nistrab'] = evtTSVInicio.trabalhador.nisTrab.cdata
    if 'nmTrab' in dir(evtTSVInicio.trabalhador): s2300_evttsvinicio_dados['nmtrab'] = evtTSVInicio.trabalhador.nmTrab.cdata
    if 'sexo' in dir(evtTSVInicio.trabalhador): s2300_evttsvinicio_dados['sexo'] = evtTSVInicio.trabalhador.sexo.cdata
    if 'racaCor' in dir(evtTSVInicio.trabalhador): s2300_evttsvinicio_dados['racacor'] = evtTSVInicio.trabalhador.racaCor.cdata
    if 'estCiv' in dir(evtTSVInicio.trabalhador): s2300_evttsvinicio_dados['estciv'] = evtTSVInicio.trabalhador.estCiv.cdata
    if 'grauInstr' in dir(evtTSVInicio.trabalhador): s2300_evttsvinicio_dados['grauinstr'] = evtTSVInicio.trabalhador.grauInstr.cdata
    if 'nmSoc' in dir(evtTSVInicio.trabalhador): s2300_evttsvinicio_dados['nmsoc'] = evtTSVInicio.trabalhador.nmSoc.cdata
    if 'dtNascto' in dir(evtTSVInicio.trabalhador.nascimento): s2300_evttsvinicio_dados['dtnascto'] = evtTSVInicio.trabalhador.nascimento.dtNascto.cdata
    if 'codMunic' in dir(evtTSVInicio.trabalhador.nascimento): s2300_evttsvinicio_dados['codmunic'] = evtTSVInicio.trabalhador.nascimento.codMunic.cdata
    if 'uf' in dir(evtTSVInicio.trabalhador.nascimento): s2300_evttsvinicio_dados['uf'] = evtTSVInicio.trabalhador.nascimento.uf.cdata
    if 'paisNascto' in dir(evtTSVInicio.trabalhador.nascimento): s2300_evttsvinicio_dados['paisnascto'] = evtTSVInicio.trabalhador.nascimento.paisNascto.cdata
    if 'paisNac' in dir(evtTSVInicio.trabalhador.nascimento): s2300_evttsvinicio_dados['paisnac'] = evtTSVInicio.trabalhador.nascimento.paisNac.cdata
    if 'nmMae' in dir(evtTSVInicio.trabalhador.nascimento): s2300_evttsvinicio_dados['nmmae'] = evtTSVInicio.trabalhador.nascimento.nmMae.cdata
    if 'nmPai' in dir(evtTSVInicio.trabalhador.nascimento): s2300_evttsvinicio_dados['nmpai'] = evtTSVInicio.trabalhador.nascimento.nmPai.cdata
    if 'cadIni' in dir(evtTSVInicio.infoTSVInicio): s2300_evttsvinicio_dados['cadini'] = evtTSVInicio.infoTSVInicio.cadIni.cdata
    if 'codCateg' in dir(evtTSVInicio.infoTSVInicio): s2300_evttsvinicio_dados['codcateg'] = evtTSVInicio.infoTSVInicio.codCateg.cdata
    if 'dtInicio' in dir(evtTSVInicio.infoTSVInicio): s2300_evttsvinicio_dados['dtinicio'] = evtTSVInicio.infoTSVInicio.dtInicio.cdata
    if 'natAtividade' in dir(evtTSVInicio.infoTSVInicio): s2300_evttsvinicio_dados['natatividade'] = evtTSVInicio.infoTSVInicio.natAtividade.cdata
    if 'inclusao' in dir(evtTSVInicio.infoTSVInicio): s2300_evttsvinicio_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTSVInicio.infoTSVInicio): s2300_evttsvinicio_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTSVInicio.infoTSVInicio): s2300_evttsvinicio_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2300_evttsvinicio', s2300_evttsvinicio_dados)
    resp = executar_sql(insert, True)
    s2300_evttsvinicio_id = resp[0][0]
    dados = s2300_evttsvinicio_dados
    dados['evento'] = 's2300'
    dados['id'] = s2300_evttsvinicio_id
    dados['identidade_evento'] = doc.eSocial.evtTSVInicio['Id']
    dados['status'] = 1

    if 'documentos' in dir(evtTSVInicio.trabalhador):
        for documentos in evtTSVInicio.trabalhador.documentos:
            s2300_documentos_dados = {}
            s2300_documentos_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id
            
            insert = create_insert('s2300_documentos', s2300_documentos_dados)
            resp = executar_sql(insert, True)
            s2300_documentos_id = resp[0][0]
            #print s2300_documentos_id

            if 'CTPS' in dir(documentos):
                for CTPS in documentos.CTPS:
                    s2300_ctps_dados = {}
                    s2300_ctps_dados['s2300_documentos_id'] = s2300_documentos_id
                    
                    if 'nrCtps' in dir(CTPS): s2300_ctps_dados['nrctps'] = CTPS.nrCtps.cdata
                    if 'serieCtps' in dir(CTPS): s2300_ctps_dados['seriectps'] = CTPS.serieCtps.cdata
                    if 'ufCtps' in dir(CTPS): s2300_ctps_dados['ufctps'] = CTPS.ufCtps.cdata
                    insert = create_insert('s2300_ctps', s2300_ctps_dados)
                    resp = executar_sql(insert, True)
                    s2300_ctps_id = resp[0][0]
                    #print s2300_ctps_id
        
            if 'RIC' in dir(documentos):
                for RIC in documentos.RIC:
                    s2300_ric_dados = {}
                    s2300_ric_dados['s2300_documentos_id'] = s2300_documentos_id
                    
                    if 'nrRic' in dir(RIC): s2300_ric_dados['nrric'] = RIC.nrRic.cdata
                    if 'orgaoEmissor' in dir(RIC): s2300_ric_dados['orgaoemissor'] = RIC.orgaoEmissor.cdata
                    if 'dtExped' in dir(RIC): s2300_ric_dados['dtexped'] = RIC.dtExped.cdata
                    insert = create_insert('s2300_ric', s2300_ric_dados)
                    resp = executar_sql(insert, True)
                    s2300_ric_id = resp[0][0]
                    #print s2300_ric_id
        
            if 'RG' in dir(documentos):
                for RG in documentos.RG:
                    s2300_rg_dados = {}
                    s2300_rg_dados['s2300_documentos_id'] = s2300_documentos_id
                    
                    if 'nrRg' in dir(RG): s2300_rg_dados['nrrg'] = RG.nrRg.cdata
                    if 'orgaoEmissor' in dir(RG): s2300_rg_dados['orgaoemissor'] = RG.orgaoEmissor.cdata
                    if 'dtExped' in dir(RG): s2300_rg_dados['dtexped'] = RG.dtExped.cdata
                    insert = create_insert('s2300_rg', s2300_rg_dados)
                    resp = executar_sql(insert, True)
                    s2300_rg_id = resp[0][0]
                    #print s2300_rg_id
        
            if 'RNE' in dir(documentos):
                for RNE in documentos.RNE:
                    s2300_rne_dados = {}
                    s2300_rne_dados['s2300_documentos_id'] = s2300_documentos_id
                    
                    if 'nrRne' in dir(RNE): s2300_rne_dados['nrrne'] = RNE.nrRne.cdata
                    if 'orgaoEmissor' in dir(RNE): s2300_rne_dados['orgaoemissor'] = RNE.orgaoEmissor.cdata
                    if 'dtExped' in dir(RNE): s2300_rne_dados['dtexped'] = RNE.dtExped.cdata
                    insert = create_insert('s2300_rne', s2300_rne_dados)
                    resp = executar_sql(insert, True)
                    s2300_rne_id = resp[0][0]
                    #print s2300_rne_id
        
            if 'OC' in dir(documentos):
                for OC in documentos.OC:
                    s2300_oc_dados = {}
                    s2300_oc_dados['s2300_documentos_id'] = s2300_documentos_id
                    
                    if 'nrOc' in dir(OC): s2300_oc_dados['nroc'] = OC.nrOc.cdata
                    if 'orgaoEmissor' in dir(OC): s2300_oc_dados['orgaoemissor'] = OC.orgaoEmissor.cdata
                    if 'dtExped' in dir(OC): s2300_oc_dados['dtexped'] = OC.dtExped.cdata
                    if 'dtValid' in dir(OC): s2300_oc_dados['dtvalid'] = OC.dtValid.cdata
                    insert = create_insert('s2300_oc', s2300_oc_dados)
                    resp = executar_sql(insert, True)
                    s2300_oc_id = resp[0][0]
                    #print s2300_oc_id
        
            if 'CNH' in dir(documentos):
                for CNH in documentos.CNH:
                    s2300_cnh_dados = {}
                    s2300_cnh_dados['s2300_documentos_id'] = s2300_documentos_id
                    
                    if 'nrRegCnh' in dir(CNH): s2300_cnh_dados['nrregcnh'] = CNH.nrRegCnh.cdata
                    if 'dtExped' in dir(CNH): s2300_cnh_dados['dtexped'] = CNH.dtExped.cdata
                    if 'ufCnh' in dir(CNH): s2300_cnh_dados['ufcnh'] = CNH.ufCnh.cdata
                    if 'dtValid' in dir(CNH): s2300_cnh_dados['dtvalid'] = CNH.dtValid.cdata
                    if 'dtPriHab' in dir(CNH): s2300_cnh_dados['dtprihab'] = CNH.dtPriHab.cdata
                    if 'categoriaCnh' in dir(CNH): s2300_cnh_dados['categoriacnh'] = CNH.categoriaCnh.cdata
                    insert = create_insert('s2300_cnh', s2300_cnh_dados)
                    resp = executar_sql(insert, True)
                    s2300_cnh_id = resp[0][0]
                    #print s2300_cnh_id
        
    if 'brasil' in dir(evtTSVInicio.trabalhador.endereco):
        for brasil in evtTSVInicio.trabalhador.endereco.brasil:
            s2300_brasil_dados = {}
            s2300_brasil_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id
            
            if 'tpLograd' in dir(brasil): s2300_brasil_dados['tplograd'] = brasil.tpLograd.cdata
            if 'dscLograd' in dir(brasil): s2300_brasil_dados['dsclograd'] = brasil.dscLograd.cdata
            if 'nrLograd' in dir(brasil): s2300_brasil_dados['nrlograd'] = brasil.nrLograd.cdata
            if 'complemento' in dir(brasil): s2300_brasil_dados['complemento'] = brasil.complemento.cdata
            if 'bairro' in dir(brasil): s2300_brasil_dados['bairro'] = brasil.bairro.cdata
            if 'cep' in dir(brasil): s2300_brasil_dados['cep'] = brasil.cep.cdata
            if 'codMunic' in dir(brasil): s2300_brasil_dados['codmunic'] = brasil.codMunic.cdata
            if 'uf' in dir(brasil): s2300_brasil_dados['uf'] = brasil.uf.cdata
            insert = create_insert('s2300_brasil', s2300_brasil_dados)
            resp = executar_sql(insert, True)
            s2300_brasil_id = resp[0][0]
            #print s2300_brasil_id

    if 'exterior' in dir(evtTSVInicio.trabalhador.endereco):
        for exterior in evtTSVInicio.trabalhador.endereco.exterior:
            s2300_exterior_dados = {}
            s2300_exterior_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id
            
            if 'paisResid' in dir(exterior): s2300_exterior_dados['paisresid'] = exterior.paisResid.cdata
            if 'dscLograd' in dir(exterior): s2300_exterior_dados['dsclograd'] = exterior.dscLograd.cdata
            if 'nrLograd' in dir(exterior): s2300_exterior_dados['nrlograd'] = exterior.nrLograd.cdata
            if 'complemento' in dir(exterior): s2300_exterior_dados['complemento'] = exterior.complemento.cdata
            if 'bairro' in dir(exterior): s2300_exterior_dados['bairro'] = exterior.bairro.cdata
            if 'nmCid' in dir(exterior): s2300_exterior_dados['nmcid'] = exterior.nmCid.cdata
            if 'codPostal' in dir(exterior): s2300_exterior_dados['codpostal'] = exterior.codPostal.cdata
            insert = create_insert('s2300_exterior', s2300_exterior_dados)
            resp = executar_sql(insert, True)
            s2300_exterior_id = resp[0][0]
            #print s2300_exterior_id

    if 'trabEstrangeiro' in dir(evtTSVInicio.trabalhador):
        for trabEstrangeiro in evtTSVInicio.trabalhador.trabEstrangeiro:
            s2300_trabestrangeiro_dados = {}
            s2300_trabestrangeiro_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id
            
            if 'dtChegada' in dir(trabEstrangeiro): s2300_trabestrangeiro_dados['dtchegada'] = trabEstrangeiro.dtChegada.cdata
            if 'classTrabEstrang' in dir(trabEstrangeiro): s2300_trabestrangeiro_dados['classtrabestrang'] = trabEstrangeiro.classTrabEstrang.cdata
            if 'casadoBr' in dir(trabEstrangeiro): s2300_trabestrangeiro_dados['casadobr'] = trabEstrangeiro.casadoBr.cdata
            if 'filhosBr' in dir(trabEstrangeiro): s2300_trabestrangeiro_dados['filhosbr'] = trabEstrangeiro.filhosBr.cdata
            insert = create_insert('s2300_trabestrangeiro', s2300_trabestrangeiro_dados)
            resp = executar_sql(insert, True)
            s2300_trabestrangeiro_id = resp[0][0]
            #print s2300_trabestrangeiro_id

    if 'infoDeficiencia' in dir(evtTSVInicio.trabalhador):
        for infoDeficiencia in evtTSVInicio.trabalhador.infoDeficiencia:
            s2300_infodeficiencia_dados = {}
            s2300_infodeficiencia_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id
            
            if 'defFisica' in dir(infoDeficiencia): s2300_infodeficiencia_dados['deffisica'] = infoDeficiencia.defFisica.cdata
            if 'defVisual' in dir(infoDeficiencia): s2300_infodeficiencia_dados['defvisual'] = infoDeficiencia.defVisual.cdata
            if 'defAuditiva' in dir(infoDeficiencia): s2300_infodeficiencia_dados['defauditiva'] = infoDeficiencia.defAuditiva.cdata
            if 'defMental' in dir(infoDeficiencia): s2300_infodeficiencia_dados['defmental'] = infoDeficiencia.defMental.cdata
            if 'defIntelectual' in dir(infoDeficiencia): s2300_infodeficiencia_dados['defintelectual'] = infoDeficiencia.defIntelectual.cdata
            if 'reabReadap' in dir(infoDeficiencia): s2300_infodeficiencia_dados['reabreadap'] = infoDeficiencia.reabReadap.cdata
            if 'observacao' in dir(infoDeficiencia): s2300_infodeficiencia_dados['observacao'] = infoDeficiencia.observacao.cdata
            insert = create_insert('s2300_infodeficiencia', s2300_infodeficiencia_dados)
            resp = executar_sql(insert, True)
            s2300_infodeficiencia_id = resp[0][0]
            #print s2300_infodeficiencia_id

    if 'dependente' in dir(evtTSVInicio.trabalhador):
        for dependente in evtTSVInicio.trabalhador.dependente:
            s2300_dependente_dados = {}
            s2300_dependente_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id
            
            if 'tpDep' in dir(dependente): s2300_dependente_dados['tpdep'] = dependente.tpDep.cdata
            if 'nmDep' in dir(dependente): s2300_dependente_dados['nmdep'] = dependente.nmDep.cdata
            if 'dtNascto' in dir(dependente): s2300_dependente_dados['dtnascto'] = dependente.dtNascto.cdata
            if 'cpfDep' in dir(dependente): s2300_dependente_dados['cpfdep'] = dependente.cpfDep.cdata
            if 'sexoDep' in dir(dependente): s2300_dependente_dados['sexodep'] = dependente.sexoDep.cdata
            if 'depIRRF' in dir(dependente): s2300_dependente_dados['depirrf'] = dependente.depIRRF.cdata
            if 'depSF' in dir(dependente): s2300_dependente_dados['depsf'] = dependente.depSF.cdata
            if 'incTrab' in dir(dependente): s2300_dependente_dados['inctrab'] = dependente.incTrab.cdata
            if 'depFinsPrev' in dir(dependente): s2300_dependente_dados['depfinsprev'] = dependente.depFinsPrev.cdata
            insert = create_insert('s2300_dependente', s2300_dependente_dados)
            resp = executar_sql(insert, True)
            s2300_dependente_id = resp[0][0]
            #print s2300_dependente_id

    if 'contato' in dir(evtTSVInicio.trabalhador):
        for contato in evtTSVInicio.trabalhador.contato:
            s2300_contato_dados = {}
            s2300_contato_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id
            
            if 'fonePrinc' in dir(contato): s2300_contato_dados['foneprinc'] = contato.fonePrinc.cdata
            if 'foneAlternat' in dir(contato): s2300_contato_dados['fonealternat'] = contato.foneAlternat.cdata
            if 'emailPrinc' in dir(contato): s2300_contato_dados['emailprinc'] = contato.emailPrinc.cdata
            if 'emailAlternat' in dir(contato): s2300_contato_dados['emailalternat'] = contato.emailAlternat.cdata
            insert = create_insert('s2300_contato', s2300_contato_dados)
            resp = executar_sql(insert, True)
            s2300_contato_id = resp[0][0]
            #print s2300_contato_id

    if 'infoComplementares' in dir(evtTSVInicio.infoTSVInicio):
        for infoComplementares in evtTSVInicio.infoTSVInicio.infoComplementares:
            s2300_infocomplementares_dados = {}
            s2300_infocomplementares_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id
            
            insert = create_insert('s2300_infocomplementares', s2300_infocomplementares_dados)
            resp = executar_sql(insert, True)
            s2300_infocomplementares_id = resp[0][0]
            #print s2300_infocomplementares_id

            if 'cargoFuncao' in dir(infoComplementares):
                for cargoFuncao in infoComplementares.cargoFuncao:
                    s2300_cargofuncao_dados = {}
                    s2300_cargofuncao_dados['s2300_infocomplementares_id'] = s2300_infocomplementares_id
                    
                    if 'codCargo' in dir(cargoFuncao): s2300_cargofuncao_dados['codcargo'] = cargoFuncao.codCargo.cdata
                    if 'codFuncao' in dir(cargoFuncao): s2300_cargofuncao_dados['codfuncao'] = cargoFuncao.codFuncao.cdata
                    insert = create_insert('s2300_cargofuncao', s2300_cargofuncao_dados)
                    resp = executar_sql(insert, True)
                    s2300_cargofuncao_id = resp[0][0]
                    #print s2300_cargofuncao_id
        
            if 'remuneracao' in dir(infoComplementares):
                for remuneracao in infoComplementares.remuneracao:
                    s2300_remuneracao_dados = {}
                    s2300_remuneracao_dados['s2300_infocomplementares_id'] = s2300_infocomplementares_id
                    
                    if 'vrSalFx' in dir(remuneracao): s2300_remuneracao_dados['vrsalfx'] = remuneracao.vrSalFx.cdata
                    if 'undSalFixo' in dir(remuneracao): s2300_remuneracao_dados['undsalfixo'] = remuneracao.undSalFixo.cdata
                    if 'dscSalVar' in dir(remuneracao): s2300_remuneracao_dados['dscsalvar'] = remuneracao.dscSalVar.cdata
                    insert = create_insert('s2300_remuneracao', s2300_remuneracao_dados)
                    resp = executar_sql(insert, True)
                    s2300_remuneracao_id = resp[0][0]
                    #print s2300_remuneracao_id
        
            if 'fgts' in dir(infoComplementares):
                for fgts in infoComplementares.fgts:
                    s2300_fgts_dados = {}
                    s2300_fgts_dados['s2300_infocomplementares_id'] = s2300_infocomplementares_id
                    
                    if 'opcFGTS' in dir(fgts): s2300_fgts_dados['opcfgts'] = fgts.opcFGTS.cdata
                    if 'dtOpcFGTS' in dir(fgts): s2300_fgts_dados['dtopcfgts'] = fgts.dtOpcFGTS.cdata
                    insert = create_insert('s2300_fgts', s2300_fgts_dados)
                    resp = executar_sql(insert, True)
                    s2300_fgts_id = resp[0][0]
                    #print s2300_fgts_id
        
            if 'infoDirigenteSindical' in dir(infoComplementares):
                for infoDirigenteSindical in infoComplementares.infoDirigenteSindical:
                    s2300_infodirigentesindical_dados = {}
                    s2300_infodirigentesindical_dados['s2300_infocomplementares_id'] = s2300_infocomplementares_id
                    
                    if 'categOrig' in dir(infoDirigenteSindical): s2300_infodirigentesindical_dados['categorig'] = infoDirigenteSindical.categOrig.cdata
                    if 'cnpjOrigem' in dir(infoDirigenteSindical): s2300_infodirigentesindical_dados['cnpjorigem'] = infoDirigenteSindical.cnpjOrigem.cdata
                    if 'dtAdmOrig' in dir(infoDirigenteSindical): s2300_infodirigentesindical_dados['dtadmorig'] = infoDirigenteSindical.dtAdmOrig.cdata
                    if 'matricOrig' in dir(infoDirigenteSindical): s2300_infodirigentesindical_dados['matricorig'] = infoDirigenteSindical.matricOrig.cdata
                    insert = create_insert('s2300_infodirigentesindical', s2300_infodirigentesindical_dados)
                    resp = executar_sql(insert, True)
                    s2300_infodirigentesindical_id = resp[0][0]
                    #print s2300_infodirigentesindical_id
        
            if 'infoTrabCedido' in dir(infoComplementares):
                for infoTrabCedido in infoComplementares.infoTrabCedido:
                    s2300_infotrabcedido_dados = {}
                    s2300_infotrabcedido_dados['s2300_infocomplementares_id'] = s2300_infocomplementares_id
                    
                    if 'categOrig' in dir(infoTrabCedido): s2300_infotrabcedido_dados['categorig'] = infoTrabCedido.categOrig.cdata
                    if 'cnpjCednt' in dir(infoTrabCedido): s2300_infotrabcedido_dados['cnpjcednt'] = infoTrabCedido.cnpjCednt.cdata
                    if 'matricCed' in dir(infoTrabCedido): s2300_infotrabcedido_dados['matricced'] = infoTrabCedido.matricCed.cdata
                    if 'dtAdmCed' in dir(infoTrabCedido): s2300_infotrabcedido_dados['dtadmced'] = infoTrabCedido.dtAdmCed.cdata
                    if 'tpRegTrab' in dir(infoTrabCedido): s2300_infotrabcedido_dados['tpregtrab'] = infoTrabCedido.tpRegTrab.cdata
                    if 'tpRegPrev' in dir(infoTrabCedido): s2300_infotrabcedido_dados['tpregprev'] = infoTrabCedido.tpRegPrev.cdata
                    if 'infOnus' in dir(infoTrabCedido): s2300_infotrabcedido_dados['infonus'] = infoTrabCedido.infOnus.cdata
                    if 'indRemunCargo' in dir(infoTrabCedido): s2300_infotrabcedido_dados['indremuncargo'] = infoTrabCedido.indRemunCargo.cdata
                    insert = create_insert('s2300_infotrabcedido', s2300_infotrabcedido_dados)
                    resp = executar_sql(insert, True)
                    s2300_infotrabcedido_id = resp[0][0]
                    #print s2300_infotrabcedido_id
        
            if 'infoEstagiario' in dir(infoComplementares):
                for infoEstagiario in infoComplementares.infoEstagiario:
                    s2300_infoestagiario_dados = {}
                    s2300_infoestagiario_dados['s2300_infocomplementares_id'] = s2300_infocomplementares_id
                    
                    if 'natEstagio' in dir(infoEstagiario): s2300_infoestagiario_dados['natestagio'] = infoEstagiario.natEstagio.cdata
                    if 'nivEstagio' in dir(infoEstagiario): s2300_infoestagiario_dados['nivestagio'] = infoEstagiario.nivEstagio.cdata
                    if 'areaAtuacao' in dir(infoEstagiario): s2300_infoestagiario_dados['areaatuacao'] = infoEstagiario.areaAtuacao.cdata
                    if 'nrApol' in dir(infoEstagiario): s2300_infoestagiario_dados['nrapol'] = infoEstagiario.nrApol.cdata
                    if 'vlrBolsa' in dir(infoEstagiario): s2300_infoestagiario_dados['vlrbolsa'] = infoEstagiario.vlrBolsa.cdata
                    if 'dtPrevTerm' in dir(infoEstagiario): s2300_infoestagiario_dados['dtprevterm'] = infoEstagiario.dtPrevTerm.cdata
                    if 'cnpjInstEnsino' in dir(infoEstagiario): s2300_infoestagiario_dados['cnpjinstensino'] = infoEstagiario.instEnsino.cnpjInstEnsino.cdata
                    if 'nmRazao' in dir(infoEstagiario): s2300_infoestagiario_dados['nmrazao'] = infoEstagiario.instEnsino.nmRazao.cdata
                    if 'dscLograd' in dir(infoEstagiario): s2300_infoestagiario_dados['dsclograd'] = infoEstagiario.instEnsino.dscLograd.cdata
                    if 'nrLograd' in dir(infoEstagiario): s2300_infoestagiario_dados['nrlograd'] = infoEstagiario.instEnsino.nrLograd.cdata
                    if 'bairro' in dir(infoEstagiario): s2300_infoestagiario_dados['bairro'] = infoEstagiario.instEnsino.bairro.cdata
                    if 'cep' in dir(infoEstagiario): s2300_infoestagiario_dados['cep'] = infoEstagiario.instEnsino.cep.cdata
                    if 'codMunic' in dir(infoEstagiario): s2300_infoestagiario_dados['codmunic'] = infoEstagiario.instEnsino.codMunic.cdata
                    if 'uf' in dir(infoEstagiario): s2300_infoestagiario_dados['uf'] = infoEstagiario.instEnsino.uf.cdata
                    insert = create_insert('s2300_infoestagiario', s2300_infoestagiario_dados)
                    resp = executar_sql(insert, True)
                    s2300_infoestagiario_id = resp[0][0]
                    #print s2300_infoestagiario_id
        
    if 'afastamento' in dir(evtTSVInicio.infoTSVInicio):
        for afastamento in evtTSVInicio.infoTSVInicio.afastamento:
            s2300_afastamento_dados = {}
            s2300_afastamento_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id
            
            if 'dtIniAfast' in dir(afastamento): s2300_afastamento_dados['dtiniafast'] = afastamento.dtIniAfast.cdata
            if 'codMotAfast' in dir(afastamento): s2300_afastamento_dados['codmotafast'] = afastamento.codMotAfast.cdata
            insert = create_insert('s2300_afastamento', s2300_afastamento_dados)
            resp = executar_sql(insert, True)
            s2300_afastamento_id = resp[0][0]
            #print s2300_afastamento_id

    if 'termino' in dir(evtTSVInicio.infoTSVInicio):
        for termino in evtTSVInicio.infoTSVInicio.termino:
            s2300_termino_dados = {}
            s2300_termino_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id
            
            if 'dtTerm' in dir(termino): s2300_termino_dados['dtterm'] = termino.dtTerm.cdata
            insert = create_insert('s2300_termino', s2300_termino_dados)
            resp = executar_sql(insert, True)
            s2300_termino_id = resp[0][0]
            #print s2300_termino_id

    from emensageriapro.esocial.views.s2300_evttsvinicio_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2300_evttsvinicio_id, 'default')
    return dados