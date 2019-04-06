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


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO



def read_s2200_evtadmissao_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2200_evtadmissao_obj(doc, status, validar)
    return dados

def read_s2200_evtadmissao(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2200_evtadmissao_obj(doc, status, validar)
    return dados



def read_s2200_evtadmissao_obj(doc, status, validar=False):
    s2200_evtadmissao_dados = {}
    s2200_evtadmissao_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2200_evtadmissao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2200_evtadmissao_dados['identidade'] = doc.eSocial.evtAdmissao['Id']
    evtAdmissao = doc.eSocial.evtAdmissao

    try: s2200_evtadmissao_dados['indretif'] = evtAdmissao.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['nrrecibo'] = evtAdmissao.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['tpamb'] = evtAdmissao.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['procemi'] = evtAdmissao.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['verproc'] = evtAdmissao.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['tpinsc'] = evtAdmissao.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['nrinsc'] = evtAdmissao.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['cpftrab'] = evtAdmissao.trabalhador.cpfTrab.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['nistrab'] = evtAdmissao.trabalhador.nisTrab.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['nmtrab'] = evtAdmissao.trabalhador.nmTrab.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['sexo'] = evtAdmissao.trabalhador.sexo.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['racacor'] = evtAdmissao.trabalhador.racaCor.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['estciv'] = evtAdmissao.trabalhador.estCiv.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['grauinstr'] = evtAdmissao.trabalhador.grauInstr.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['indpriempr'] = evtAdmissao.trabalhador.indPriEmpr.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['nmsoc'] = evtAdmissao.trabalhador.nmSoc.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['dtnascto'] = evtAdmissao.trabalhador.nascimento.dtNascto.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['codmunic'] = evtAdmissao.trabalhador.nascimento.codMunic.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['uf'] = evtAdmissao.trabalhador.nascimento.uf.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['paisnascto'] = evtAdmissao.trabalhador.nascimento.paisNascto.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['paisnac'] = evtAdmissao.trabalhador.nascimento.paisNac.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['nmmae'] = evtAdmissao.trabalhador.nascimento.nmMae.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['nmpai'] = evtAdmissao.trabalhador.nascimento.nmPai.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['matricula'] = evtAdmissao.vinculo.matricula.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['tpregtrab'] = evtAdmissao.vinculo.tpRegTrab.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['tpregprev'] = evtAdmissao.vinculo.tpRegPrev.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['nrrecinfprelim'] = evtAdmissao.vinculo.nrRecInfPrelim.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['cadini'] = evtAdmissao.vinculo.cadIni.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['codcargo'] = evtAdmissao.vinculo.infoContrato.codCargo.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['dtingrcargo'] = evtAdmissao.vinculo.infoContrato.dtIngrCargo.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['codfuncao'] = evtAdmissao.vinculo.infoContrato.codFuncao.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['codcateg'] = evtAdmissao.vinculo.infoContrato.codCateg.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['codcarreira'] = evtAdmissao.vinculo.infoContrato.codCarreira.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['dtingrcarr'] = evtAdmissao.vinculo.infoContrato.dtIngrCarr.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['vrsalfx'] = evtAdmissao.vinculo.infoContrato.remuneracao.vrSalFx.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['undsalfixo'] = evtAdmissao.vinculo.infoContrato.remuneracao.undSalFixo.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['dscsalvar'] = evtAdmissao.vinculo.infoContrato.remuneracao.dscSalVar.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['tpcontr'] = evtAdmissao.vinculo.infoContrato.duracao.tpContr.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['dtterm'] = evtAdmissao.vinculo.infoContrato.duracao.dtTerm.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['clauassec'] = evtAdmissao.vinculo.infoContrato.duracao.clauAssec.cdata
    except AttributeError: pass
    try: s2200_evtadmissao_dados['objdet'] = evtAdmissao.vinculo.infoContrato.duracao.objDet.cdata
    except AttributeError: pass
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
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'CTPS' in dir(evtAdmissao.trabalhador.documentos) and evtAdmissao.trabalhador.documentos.CTPS.cdata != '':
        for CTPS in evtAdmissao.trabalhador.documentos.CTPS:
            s2200_ctps_dados = {}
            s2200_ctps_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_ctps_dados['nrctps'] = CTPS.nrCtps.cdata
            except AttributeError: pass
            try: s2200_ctps_dados['seriectps'] = CTPS.serieCtps.cdata
            except AttributeError: pass
            try: s2200_ctps_dados['ufctps'] = CTPS.ufCtps.cdata
            except AttributeError: pass
            insert = create_insert('s2200_ctps', s2200_ctps_dados)
            resp = executar_sql(insert, True)
            s2200_ctps_id = resp[0][0]
            #print s2200_ctps_id

    if 'RIC' in dir(evtAdmissao.trabalhador.documentos) and evtAdmissao.trabalhador.documentos.RIC.cdata != '':
        for RIC in evtAdmissao.trabalhador.documentos.RIC:
            s2200_ric_dados = {}
            s2200_ric_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_ric_dados['nrric'] = RIC.nrRic.cdata
            except AttributeError: pass
            try: s2200_ric_dados['orgaoemissor'] = RIC.orgaoEmissor.cdata
            except AttributeError: pass
            try: s2200_ric_dados['dtexped'] = RIC.dtExped.cdata
            except AttributeError: pass
            insert = create_insert('s2200_ric', s2200_ric_dados)
            resp = executar_sql(insert, True)
            s2200_ric_id = resp[0][0]
            #print s2200_ric_id

    if 'RG' in dir(evtAdmissao.trabalhador.documentos) and evtAdmissao.trabalhador.documentos.RG.cdata != '':
        for RG in evtAdmissao.trabalhador.documentos.RG:
            s2200_rg_dados = {}
            s2200_rg_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_rg_dados['nrrg'] = RG.nrRg.cdata
            except AttributeError: pass
            try: s2200_rg_dados['orgaoemissor'] = RG.orgaoEmissor.cdata
            except AttributeError: pass
            try: s2200_rg_dados['dtexped'] = RG.dtExped.cdata
            except AttributeError: pass
            insert = create_insert('s2200_rg', s2200_rg_dados)
            resp = executar_sql(insert, True)
            s2200_rg_id = resp[0][0]
            #print s2200_rg_id

    if 'RNE' in dir(evtAdmissao.trabalhador.documentos) and evtAdmissao.trabalhador.documentos.RNE.cdata != '':
        for RNE in evtAdmissao.trabalhador.documentos.RNE:
            s2200_rne_dados = {}
            s2200_rne_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_rne_dados['nrrne'] = RNE.nrRne.cdata
            except AttributeError: pass
            try: s2200_rne_dados['orgaoemissor'] = RNE.orgaoEmissor.cdata
            except AttributeError: pass
            try: s2200_rne_dados['dtexped'] = RNE.dtExped.cdata
            except AttributeError: pass
            insert = create_insert('s2200_rne', s2200_rne_dados)
            resp = executar_sql(insert, True)
            s2200_rne_id = resp[0][0]
            #print s2200_rne_id

    if 'OC' in dir(evtAdmissao.trabalhador.documentos) and evtAdmissao.trabalhador.documentos.OC.cdata != '':
        for OC in evtAdmissao.trabalhador.documentos.OC:
            s2200_oc_dados = {}
            s2200_oc_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_oc_dados['nroc'] = OC.nrOc.cdata
            except AttributeError: pass
            try: s2200_oc_dados['orgaoemissor'] = OC.orgaoEmissor.cdata
            except AttributeError: pass
            try: s2200_oc_dados['dtexped'] = OC.dtExped.cdata
            except AttributeError: pass
            try: s2200_oc_dados['dtvalid'] = OC.dtValid.cdata
            except AttributeError: pass
            insert = create_insert('s2200_oc', s2200_oc_dados)
            resp = executar_sql(insert, True)
            s2200_oc_id = resp[0][0]
            #print s2200_oc_id

    if 'CNH' in dir(evtAdmissao.trabalhador.documentos) and evtAdmissao.trabalhador.documentos.CNH.cdata != '':
        for CNH in evtAdmissao.trabalhador.documentos.CNH:
            s2200_cnh_dados = {}
            s2200_cnh_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_cnh_dados['nrregcnh'] = CNH.nrRegCnh.cdata
            except AttributeError: pass
            try: s2200_cnh_dados['dtexped'] = CNH.dtExped.cdata
            except AttributeError: pass
            try: s2200_cnh_dados['ufcnh'] = CNH.ufCnh.cdata
            except AttributeError: pass
            try: s2200_cnh_dados['dtvalid'] = CNH.dtValid.cdata
            except AttributeError: pass
            try: s2200_cnh_dados['dtprihab'] = CNH.dtPriHab.cdata
            except AttributeError: pass
            try: s2200_cnh_dados['categoriacnh'] = CNH.categoriaCnh.cdata
            except AttributeError: pass
            insert = create_insert('s2200_cnh', s2200_cnh_dados)
            resp = executar_sql(insert, True)
            s2200_cnh_id = resp[0][0]
            #print s2200_cnh_id

    if 'brasil' in dir(evtAdmissao.trabalhador.endereco) and evtAdmissao.trabalhador.endereco.brasil.cdata != '':
        for brasil in evtAdmissao.trabalhador.endereco.brasil:
            s2200_brasil_dados = {}
            s2200_brasil_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_brasil_dados['tplograd'] = brasil.tpLograd.cdata
            except AttributeError: pass
            try: s2200_brasil_dados['dsclograd'] = brasil.dscLograd.cdata
            except AttributeError: pass
            try: s2200_brasil_dados['nrlograd'] = brasil.nrLograd.cdata
            except AttributeError: pass
            try: s2200_brasil_dados['complemento'] = brasil.complemento.cdata
            except AttributeError: pass
            try: s2200_brasil_dados['bairro'] = brasil.bairro.cdata
            except AttributeError: pass
            try: s2200_brasil_dados['cep'] = brasil.cep.cdata
            except AttributeError: pass
            try: s2200_brasil_dados['codmunic'] = brasil.codMunic.cdata
            except AttributeError: pass
            try: s2200_brasil_dados['uf'] = brasil.uf.cdata
            except AttributeError: pass
            insert = create_insert('s2200_brasil', s2200_brasil_dados)
            resp = executar_sql(insert, True)
            s2200_brasil_id = resp[0][0]
            #print s2200_brasil_id

    if 'exterior' in dir(evtAdmissao.trabalhador.endereco) and evtAdmissao.trabalhador.endereco.exterior.cdata != '':
        for exterior in evtAdmissao.trabalhador.endereco.exterior:
            s2200_exterior_dados = {}
            s2200_exterior_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_exterior_dados['paisresid'] = exterior.paisResid.cdata
            except AttributeError: pass
            try: s2200_exterior_dados['dsclograd'] = exterior.dscLograd.cdata
            except AttributeError: pass
            try: s2200_exterior_dados['nrlograd'] = exterior.nrLograd.cdata
            except AttributeError: pass
            try: s2200_exterior_dados['complemento'] = exterior.complemento.cdata
            except AttributeError: pass
            try: s2200_exterior_dados['bairro'] = exterior.bairro.cdata
            except AttributeError: pass
            try: s2200_exterior_dados['nmcid'] = exterior.nmCid.cdata
            except AttributeError: pass
            try: s2200_exterior_dados['codpostal'] = exterior.codPostal.cdata
            except AttributeError: pass
            insert = create_insert('s2200_exterior', s2200_exterior_dados)
            resp = executar_sql(insert, True)
            s2200_exterior_id = resp[0][0]
            #print s2200_exterior_id

    if 'trabEstrangeiro' in dir(evtAdmissao.trabalhador) and evtAdmissao.trabalhador.trabEstrangeiro.cdata != '':
        for trabEstrangeiro in evtAdmissao.trabalhador.trabEstrangeiro:
            s2200_trabestrangeiro_dados = {}
            s2200_trabestrangeiro_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_trabestrangeiro_dados['dtchegada'] = trabEstrangeiro.dtChegada.cdata
            except AttributeError: pass
            try: s2200_trabestrangeiro_dados['classtrabestrang'] = trabEstrangeiro.classTrabEstrang.cdata
            except AttributeError: pass
            try: s2200_trabestrangeiro_dados['casadobr'] = trabEstrangeiro.casadoBr.cdata
            except AttributeError: pass
            try: s2200_trabestrangeiro_dados['filhosbr'] = trabEstrangeiro.filhosBr.cdata
            except AttributeError: pass
            insert = create_insert('s2200_trabestrangeiro', s2200_trabestrangeiro_dados)
            resp = executar_sql(insert, True)
            s2200_trabestrangeiro_id = resp[0][0]
            #print s2200_trabestrangeiro_id

    if 'infoDeficiencia' in dir(evtAdmissao.trabalhador) and evtAdmissao.trabalhador.infoDeficiencia.cdata != '':
        for infoDeficiencia in evtAdmissao.trabalhador.infoDeficiencia:
            s2200_infodeficiencia_dados = {}
            s2200_infodeficiencia_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_infodeficiencia_dados['deffisica'] = infoDeficiencia.defFisica.cdata
            except AttributeError: pass
            try: s2200_infodeficiencia_dados['defvisual'] = infoDeficiencia.defVisual.cdata
            except AttributeError: pass
            try: s2200_infodeficiencia_dados['defauditiva'] = infoDeficiencia.defAuditiva.cdata
            except AttributeError: pass
            try: s2200_infodeficiencia_dados['defmental'] = infoDeficiencia.defMental.cdata
            except AttributeError: pass
            try: s2200_infodeficiencia_dados['defintelectual'] = infoDeficiencia.defIntelectual.cdata
            except AttributeError: pass
            try: s2200_infodeficiencia_dados['reabreadap'] = infoDeficiencia.reabReadap.cdata
            except AttributeError: pass
            try: s2200_infodeficiencia_dados['infocota'] = infoDeficiencia.infoCota.cdata
            except AttributeError: pass
            try: s2200_infodeficiencia_dados['observacao'] = infoDeficiencia.observacao.cdata
            except AttributeError: pass
            insert = create_insert('s2200_infodeficiencia', s2200_infodeficiencia_dados)
            resp = executar_sql(insert, True)
            s2200_infodeficiencia_id = resp[0][0]
            #print s2200_infodeficiencia_id

    if 'dependente' in dir(evtAdmissao.trabalhador) and evtAdmissao.trabalhador.dependente.cdata != '':
        for dependente in evtAdmissao.trabalhador.dependente:
            s2200_dependente_dados = {}
            s2200_dependente_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_dependente_dados['tpdep'] = dependente.tpDep.cdata
            except AttributeError: pass
            try: s2200_dependente_dados['nmdep'] = dependente.nmDep.cdata
            except AttributeError: pass
            try: s2200_dependente_dados['dtnascto'] = dependente.dtNascto.cdata
            except AttributeError: pass
            try: s2200_dependente_dados['cpfdep'] = dependente.cpfDep.cdata
            except AttributeError: pass
            try: s2200_dependente_dados['sexodep'] = dependente.sexoDep.cdata
            except AttributeError: pass
            try: s2200_dependente_dados['depirrf'] = dependente.depIRRF.cdata
            except AttributeError: pass
            try: s2200_dependente_dados['depsf'] = dependente.depSF.cdata
            except AttributeError: pass
            try: s2200_dependente_dados['inctrab'] = dependente.incTrab.cdata
            except AttributeError: pass
            try: s2200_dependente_dados['depfinsprev'] = dependente.depFinsPrev.cdata
            except AttributeError: pass
            insert = create_insert('s2200_dependente', s2200_dependente_dados)
            resp = executar_sql(insert, True)
            s2200_dependente_id = resp[0][0]
            #print s2200_dependente_id

    if 'aposentadoria' in dir(evtAdmissao.trabalhador) and evtAdmissao.trabalhador.aposentadoria.cdata != '':
        for aposentadoria in evtAdmissao.trabalhador.aposentadoria:
            s2200_aposentadoria_dados = {}
            s2200_aposentadoria_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_aposentadoria_dados['trabaposent'] = aposentadoria.trabAposent.cdata
            except AttributeError: pass
            insert = create_insert('s2200_aposentadoria', s2200_aposentadoria_dados)
            resp = executar_sql(insert, True)
            s2200_aposentadoria_id = resp[0][0]
            #print s2200_aposentadoria_id

    if 'contato' in dir(evtAdmissao.trabalhador) and evtAdmissao.trabalhador.contato.cdata != '':
        for contato in evtAdmissao.trabalhador.contato:
            s2200_contato_dados = {}
            s2200_contato_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_contato_dados['foneprinc'] = contato.fonePrinc.cdata
            except AttributeError: pass
            try: s2200_contato_dados['fonealternat'] = contato.foneAlternat.cdata
            except AttributeError: pass
            try: s2200_contato_dados['emailprinc'] = contato.emailPrinc.cdata
            except AttributeError: pass
            try: s2200_contato_dados['emailalternat'] = contato.emailAlternat.cdata
            except AttributeError: pass
            insert = create_insert('s2200_contato', s2200_contato_dados)
            resp = executar_sql(insert, True)
            s2200_contato_id = resp[0][0]
            #print s2200_contato_id

    if 'infoCeletista' in dir(evtAdmissao.vinculo.infoRegimeTrab) and evtAdmissao.vinculo.infoRegimeTrab.infoCeletista.cdata != '':
        for infoCeletista in evtAdmissao.vinculo.infoRegimeTrab.infoCeletista:
            s2200_infoceletista_dados = {}
            s2200_infoceletista_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_infoceletista_dados['dtadm'] = infoCeletista.dtAdm.cdata
            except AttributeError: pass
            try: s2200_infoceletista_dados['tpadmissao'] = infoCeletista.tpAdmissao.cdata
            except AttributeError: pass
            try: s2200_infoceletista_dados['indadmissao'] = infoCeletista.indAdmissao.cdata
            except AttributeError: pass
            try: s2200_infoceletista_dados['tpregjor'] = infoCeletista.tpRegJor.cdata
            except AttributeError: pass
            try: s2200_infoceletista_dados['natatividade'] = infoCeletista.natAtividade.cdata
            except AttributeError: pass
            try: s2200_infoceletista_dados['dtbase'] = infoCeletista.dtBase.cdata
            except AttributeError: pass
            try: s2200_infoceletista_dados['cnpjsindcategprof'] = infoCeletista.cnpjSindCategProf.cdata
            except AttributeError: pass
            try: s2200_infoceletista_dados['opcfgts'] = infoCeletista.FGTS.opcFGTS.cdata
            except AttributeError: pass
            try: s2200_infoceletista_dados['dtopcfgts'] = infoCeletista.FGTS.dtOpcFGTS.cdata
            except AttributeError: pass
            insert = create_insert('s2200_infoceletista', s2200_infoceletista_dados)
            resp = executar_sql(insert, True)
            s2200_infoceletista_id = resp[0][0]
            #print s2200_infoceletista_id

            if 'trabTemporario' in dir(infoCeletista) and infoCeletista.trabTemporario.cdata != '':
                for trabTemporario in infoCeletista.trabTemporario:
                    s2200_trabtemporario_dados = {}
                    s2200_trabtemporario_dados['s2200_infoceletista_id'] = s2200_infoceletista_id

                    try: s2200_trabtemporario_dados['hipleg'] = trabTemporario.hipLeg.cdata
                    except AttributeError: pass
                    try: s2200_trabtemporario_dados['justcontr'] = trabTemporario.justContr.cdata
                    except AttributeError: pass
                    try: s2200_trabtemporario_dados['tpinclcontr'] = trabTemporario.tpInclContr.cdata
                    except AttributeError: pass
                    try: s2200_trabtemporario_dados['tpinsc'] = trabTemporario.ideTomadorServ.tpInsc.cdata
                    except AttributeError: pass
                    try: s2200_trabtemporario_dados['nrinsc'] = trabTemporario.ideTomadorServ.nrInsc.cdata
                    except AttributeError: pass
                    insert = create_insert('s2200_trabtemporario', s2200_trabtemporario_dados)
                    resp = executar_sql(insert, True)
                    s2200_trabtemporario_id = resp[0][0]
                    #print s2200_trabtemporario_id

            if 'aprend' in dir(infoCeletista) and infoCeletista.aprend.cdata != '':
                for aprend in infoCeletista.aprend:
                    s2200_aprend_dados = {}
                    s2200_aprend_dados['s2200_infoceletista_id'] = s2200_infoceletista_id

                    try: s2200_aprend_dados['tpinsc'] = aprend.tpInsc.cdata
                    except AttributeError: pass
                    try: s2200_aprend_dados['nrinsc'] = aprend.nrInsc.cdata
                    except AttributeError: pass
                    insert = create_insert('s2200_aprend', s2200_aprend_dados)
                    resp = executar_sql(insert, True)
                    s2200_aprend_id = resp[0][0]
                    #print s2200_aprend_id

    if 'infoEstatutario' in dir(evtAdmissao.vinculo.infoRegimeTrab) and evtAdmissao.vinculo.infoRegimeTrab.infoEstatutario.cdata != '':
        for infoEstatutario in evtAdmissao.vinculo.infoRegimeTrab.infoEstatutario:
            s2200_infoestatutario_dados = {}
            s2200_infoestatutario_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_infoestatutario_dados['indprovim'] = infoEstatutario.indProvim.cdata
            except AttributeError: pass
            try: s2200_infoestatutario_dados['tpprov'] = infoEstatutario.tpProv.cdata
            except AttributeError: pass
            try: s2200_infoestatutario_dados['dtnomeacao'] = infoEstatutario.dtNomeacao.cdata
            except AttributeError: pass
            try: s2200_infoestatutario_dados['dtposse'] = infoEstatutario.dtPosse.cdata
            except AttributeError: pass
            try: s2200_infoestatutario_dados['dtexercicio'] = infoEstatutario.dtExercicio.cdata
            except AttributeError: pass
            try: s2200_infoestatutario_dados['dtingsvpub'] = infoEstatutario.dtIngSvPub.cdata
            except AttributeError: pass
            try: s2200_infoestatutario_dados['tpplanrp'] = infoEstatutario.tpPlanRP.cdata
            except AttributeError: pass
            try: s2200_infoestatutario_dados['indtetorgps'] = infoEstatutario.indTetoRGPS.cdata
            except AttributeError: pass
            try: s2200_infoestatutario_dados['indabonoperm'] = infoEstatutario.indAbonoPerm.cdata
            except AttributeError: pass
            try: s2200_infoestatutario_dados['dtiniabono'] = infoEstatutario.dtIniAbono.cdata
            except AttributeError: pass
            try: s2200_infoestatutario_dados['indparcremun'] = infoEstatutario.indParcRemun.cdata
            except AttributeError: pass
            try: s2200_infoestatutario_dados['dtiniparc'] = infoEstatutario.dtIniParc.cdata
            except AttributeError: pass
            insert = create_insert('s2200_infoestatutario', s2200_infoestatutario_dados)
            resp = executar_sql(insert, True)
            s2200_infoestatutario_id = resp[0][0]
            #print s2200_infoestatutario_id

            if 'infoDecJud' in dir(infoEstatutario) and infoEstatutario.infoDecJud.cdata != '':
                for infoDecJud in infoEstatutario.infoDecJud:
                    s2200_infodecjud_dados = {}
                    s2200_infodecjud_dados['s2200_infoestatutario_id'] = s2200_infoestatutario_id

                    try: s2200_infodecjud_dados['nrprocjud'] = infoDecJud.nrProcJud.cdata
                    except AttributeError: pass
                    insert = create_insert('s2200_infodecjud', s2200_infodecjud_dados)
                    resp = executar_sql(insert, True)
                    s2200_infodecjud_id = resp[0][0]
                    #print s2200_infodecjud_id

    if 'localTrabGeral' in dir(evtAdmissao.vinculo.infoContrato.localTrabalho) and evtAdmissao.vinculo.infoContrato.localTrabalho.localTrabGeral.cdata != '':
        for localTrabGeral in evtAdmissao.vinculo.infoContrato.localTrabalho.localTrabGeral:
            s2200_localtrabgeral_dados = {}
            s2200_localtrabgeral_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_localtrabgeral_dados['tpinsc'] = localTrabGeral.tpInsc.cdata
            except AttributeError: pass
            try: s2200_localtrabgeral_dados['nrinsc'] = localTrabGeral.nrInsc.cdata
            except AttributeError: pass
            try: s2200_localtrabgeral_dados['desccomp'] = localTrabGeral.descComp.cdata
            except AttributeError: pass
            insert = create_insert('s2200_localtrabgeral', s2200_localtrabgeral_dados)
            resp = executar_sql(insert, True)
            s2200_localtrabgeral_id = resp[0][0]
            #print s2200_localtrabgeral_id

    if 'localTrabDom' in dir(evtAdmissao.vinculo.infoContrato.localTrabalho) and evtAdmissao.vinculo.infoContrato.localTrabalho.localTrabDom.cdata != '':
        for localTrabDom in evtAdmissao.vinculo.infoContrato.localTrabalho.localTrabDom:
            s2200_localtrabdom_dados = {}
            s2200_localtrabdom_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_localtrabdom_dados['tplograd'] = localTrabDom.tpLograd.cdata
            except AttributeError: pass
            try: s2200_localtrabdom_dados['dsclograd'] = localTrabDom.dscLograd.cdata
            except AttributeError: pass
            try: s2200_localtrabdom_dados['nrlograd'] = localTrabDom.nrLograd.cdata
            except AttributeError: pass
            try: s2200_localtrabdom_dados['complemento'] = localTrabDom.complemento.cdata
            except AttributeError: pass
            try: s2200_localtrabdom_dados['bairro'] = localTrabDom.bairro.cdata
            except AttributeError: pass
            try: s2200_localtrabdom_dados['cep'] = localTrabDom.cep.cdata
            except AttributeError: pass
            try: s2200_localtrabdom_dados['codmunic'] = localTrabDom.codMunic.cdata
            except AttributeError: pass
            try: s2200_localtrabdom_dados['uf'] = localTrabDom.uf.cdata
            except AttributeError: pass
            insert = create_insert('s2200_localtrabdom', s2200_localtrabdom_dados)
            resp = executar_sql(insert, True)
            s2200_localtrabdom_id = resp[0][0]
            #print s2200_localtrabdom_id

    if 'horContratual' in dir(evtAdmissao.vinculo.infoContrato) and evtAdmissao.vinculo.infoContrato.horContratual.cdata != '':
        for horContratual in evtAdmissao.vinculo.infoContrato.horContratual:
            s2200_horcontratual_dados = {}
            s2200_horcontratual_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_horcontratual_dados['qtdhrssem'] = horContratual.qtdHrsSem.cdata
            except AttributeError: pass
            try: s2200_horcontratual_dados['tpjornada'] = horContratual.tpJornada.cdata
            except AttributeError: pass
            try: s2200_horcontratual_dados['dsctpjorn'] = horContratual.dscTpJorn.cdata
            except AttributeError: pass
            try: s2200_horcontratual_dados['tmpparc'] = horContratual.tmpParc.cdata
            except AttributeError: pass
            insert = create_insert('s2200_horcontratual', s2200_horcontratual_dados)
            resp = executar_sql(insert, True)
            s2200_horcontratual_id = resp[0][0]
            #print s2200_horcontratual_id

            if 'horario' in dir(horContratual) and horContratual.horario.cdata != '':
                for horario in horContratual.horario:
                    s2200_horario_dados = {}
                    s2200_horario_dados['s2200_horcontratual_id'] = s2200_horcontratual_id

                    try: s2200_horario_dados['dia'] = horario.dia.cdata
                    except AttributeError: pass
                    try: s2200_horario_dados['codhorcontrat'] = horario.codHorContrat.cdata
                    except AttributeError: pass
                    insert = create_insert('s2200_horario', s2200_horario_dados)
                    resp = executar_sql(insert, True)
                    s2200_horario_id = resp[0][0]
                    #print s2200_horario_id

    if 'filiacaoSindical' in dir(evtAdmissao.vinculo.infoContrato) and evtAdmissao.vinculo.infoContrato.filiacaoSindical.cdata != '':
        for filiacaoSindical in evtAdmissao.vinculo.infoContrato.filiacaoSindical:
            s2200_filiacaosindical_dados = {}
            s2200_filiacaosindical_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_filiacaosindical_dados['cnpjsindtrab'] = filiacaoSindical.cnpjSindTrab.cdata
            except AttributeError: pass
            insert = create_insert('s2200_filiacaosindical', s2200_filiacaosindical_dados)
            resp = executar_sql(insert, True)
            s2200_filiacaosindical_id = resp[0][0]
            #print s2200_filiacaosindical_id

    if 'alvaraJudicial' in dir(evtAdmissao.vinculo.infoContrato) and evtAdmissao.vinculo.infoContrato.alvaraJudicial.cdata != '':
        for alvaraJudicial in evtAdmissao.vinculo.infoContrato.alvaraJudicial:
            s2200_alvarajudicial_dados = {}
            s2200_alvarajudicial_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_alvarajudicial_dados['nrprocjud'] = alvaraJudicial.nrProcJud.cdata
            except AttributeError: pass
            insert = create_insert('s2200_alvarajudicial', s2200_alvarajudicial_dados)
            resp = executar_sql(insert, True)
            s2200_alvarajudicial_id = resp[0][0]
            #print s2200_alvarajudicial_id

    if 'observacoes' in dir(evtAdmissao.vinculo.infoContrato) and evtAdmissao.vinculo.infoContrato.observacoes.cdata != '':
        for observacoes in evtAdmissao.vinculo.infoContrato.observacoes:
            s2200_observacoes_dados = {}
            s2200_observacoes_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_observacoes_dados['observacao'] = observacoes.observacao.cdata
            except AttributeError: pass
            insert = create_insert('s2200_observacoes', s2200_observacoes_dados)
            resp = executar_sql(insert, True)
            s2200_observacoes_id = resp[0][0]
            #print s2200_observacoes_id

    if 'sucessaoVinc' in dir(evtAdmissao.vinculo) and evtAdmissao.vinculo.sucessaoVinc.cdata != '':
        for sucessaoVinc in evtAdmissao.vinculo.sucessaoVinc:
            s2200_sucessaovinc_dados = {}
            s2200_sucessaovinc_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_sucessaovinc_dados['tpinscant'] = sucessaoVinc.tpInscAnt.cdata
            except AttributeError: pass
            try: s2200_sucessaovinc_dados['cnpjempregant'] = sucessaoVinc.cnpjEmpregAnt.cdata
            except AttributeError: pass
            try: s2200_sucessaovinc_dados['matricant'] = sucessaoVinc.matricAnt.cdata
            except AttributeError: pass
            try: s2200_sucessaovinc_dados['dttransf'] = sucessaoVinc.dtTransf.cdata
            except AttributeError: pass
            try: s2200_sucessaovinc_dados['observacao'] = sucessaoVinc.observacao.cdata
            except AttributeError: pass
            insert = create_insert('s2200_sucessaovinc', s2200_sucessaovinc_dados)
            resp = executar_sql(insert, True)
            s2200_sucessaovinc_id = resp[0][0]
            #print s2200_sucessaovinc_id

    if 'transfDom' in dir(evtAdmissao.vinculo) and evtAdmissao.vinculo.transfDom.cdata != '':
        for transfDom in evtAdmissao.vinculo.transfDom:
            s2200_transfdom_dados = {}
            s2200_transfdom_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_transfdom_dados['cpfsubstituido'] = transfDom.cpfSubstituido.cdata
            except AttributeError: pass
            try: s2200_transfdom_dados['matricant'] = transfDom.matricAnt.cdata
            except AttributeError: pass
            try: s2200_transfdom_dados['dttransf'] = transfDom.dtTransf.cdata
            except AttributeError: pass
            insert = create_insert('s2200_transfdom', s2200_transfdom_dados)
            resp = executar_sql(insert, True)
            s2200_transfdom_id = resp[0][0]
            #print s2200_transfdom_id

    if 'mudancaCPF' in dir(evtAdmissao.vinculo) and evtAdmissao.vinculo.mudancaCPF.cdata != '':
        for mudancaCPF in evtAdmissao.vinculo.mudancaCPF:
            s2200_mudancacpf_dados = {}
            s2200_mudancacpf_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_mudancacpf_dados['cpfant'] = mudancaCPF.cpfAnt.cdata
            except AttributeError: pass
            try: s2200_mudancacpf_dados['matricant'] = mudancaCPF.matricAnt.cdata
            except AttributeError: pass
            try: s2200_mudancacpf_dados['dtaltcpf'] = mudancaCPF.dtAltCPF.cdata
            except AttributeError: pass
            try: s2200_mudancacpf_dados['observacao'] = mudancaCPF.observacao.cdata
            except AttributeError: pass
            insert = create_insert('s2200_mudancacpf', s2200_mudancacpf_dados)
            resp = executar_sql(insert, True)
            s2200_mudancacpf_id = resp[0][0]
            #print s2200_mudancacpf_id

    if 'afastamento' in dir(evtAdmissao.vinculo) and evtAdmissao.vinculo.afastamento.cdata != '':
        for afastamento in evtAdmissao.vinculo.afastamento:
            s2200_afastamento_dados = {}
            s2200_afastamento_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_afastamento_dados['dtiniafast'] = afastamento.dtIniAfast.cdata
            except AttributeError: pass
            try: s2200_afastamento_dados['codmotafast'] = afastamento.codMotAfast.cdata
            except AttributeError: pass
            insert = create_insert('s2200_afastamento', s2200_afastamento_dados)
            resp = executar_sql(insert, True)
            s2200_afastamento_id = resp[0][0]
            #print s2200_afastamento_id

    if 'desligamento' in dir(evtAdmissao.vinculo) and evtAdmissao.vinculo.desligamento.cdata != '':
        for desligamento in evtAdmissao.vinculo.desligamento:
            s2200_desligamento_dados = {}
            s2200_desligamento_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_desligamento_dados['dtdeslig'] = desligamento.dtDeslig.cdata
            except AttributeError: pass
            insert = create_insert('s2200_desligamento', s2200_desligamento_dados)
            resp = executar_sql(insert, True)
            s2200_desligamento_id = resp[0][0]
            #print s2200_desligamento_id

    if 'cessao' in dir(evtAdmissao.vinculo) and evtAdmissao.vinculo.cessao.cdata != '':
        for cessao in evtAdmissao.vinculo.cessao:
            s2200_cessao_dados = {}
            s2200_cessao_dados['s2200_evtadmissao_id'] = s2200_evtadmissao_id

            try: s2200_cessao_dados['dtinicessao'] = cessao.dtIniCessao.cdata
            except AttributeError: pass
            insert = create_insert('s2200_cessao', s2200_cessao_dados)
            resp = executar_sql(insert, True)
            s2200_cessao_id = resp[0][0]
            #print s2200_cessao_id

    from emensageriapro.esocial.views.s2200_evtadmissao_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2200_evtadmissao_id, 'default')
    return dados