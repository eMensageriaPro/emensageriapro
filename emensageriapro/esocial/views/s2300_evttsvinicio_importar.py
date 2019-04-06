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



def read_s2300_evttsvinicio_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2300_evttsvinicio_obj(doc, status, validar)
    return dados

def read_s2300_evttsvinicio(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2300_evttsvinicio_obj(doc, status, validar)
    return dados



def read_s2300_evttsvinicio_obj(doc, status, validar=False):
    s2300_evttsvinicio_dados = {}
    s2300_evttsvinicio_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2300_evttsvinicio_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2300_evttsvinicio_dados['identidade'] = doc.eSocial.evtTSVInicio['Id']
    evtTSVInicio = doc.eSocial.evtTSVInicio

    try: s2300_evttsvinicio_dados['indretif'] = evtTSVInicio.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['nrrecibo'] = evtTSVInicio.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['tpamb'] = evtTSVInicio.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['procemi'] = evtTSVInicio.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['verproc'] = evtTSVInicio.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['tpinsc'] = evtTSVInicio.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['nrinsc'] = evtTSVInicio.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['cpftrab'] = evtTSVInicio.trabalhador.cpfTrab.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['nistrab'] = evtTSVInicio.trabalhador.nisTrab.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['nmtrab'] = evtTSVInicio.trabalhador.nmTrab.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['sexo'] = evtTSVInicio.trabalhador.sexo.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['racacor'] = evtTSVInicio.trabalhador.racaCor.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['estciv'] = evtTSVInicio.trabalhador.estCiv.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['grauinstr'] = evtTSVInicio.trabalhador.grauInstr.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['nmsoc'] = evtTSVInicio.trabalhador.nmSoc.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['dtnascto'] = evtTSVInicio.trabalhador.nascimento.dtNascto.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['codmunic'] = evtTSVInicio.trabalhador.nascimento.codMunic.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['uf'] = evtTSVInicio.trabalhador.nascimento.uf.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['paisnascto'] = evtTSVInicio.trabalhador.nascimento.paisNascto.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['paisnac'] = evtTSVInicio.trabalhador.nascimento.paisNac.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['nmmae'] = evtTSVInicio.trabalhador.nascimento.nmMae.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['nmpai'] = evtTSVInicio.trabalhador.nascimento.nmPai.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['cadini'] = evtTSVInicio.infoTSVInicio.cadIni.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['codcateg'] = evtTSVInicio.infoTSVInicio.codCateg.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['dtinicio'] = evtTSVInicio.infoTSVInicio.dtInicio.cdata
    except AttributeError: pass
    try: s2300_evttsvinicio_dados['natatividade'] = evtTSVInicio.infoTSVInicio.natAtividade.cdata
    except AttributeError: pass
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
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'CTPS' in dir(evtTSVInicio.trabalhador.documentos) and evtTSVInicio.trabalhador.documentos.CTPS.cdata != '':
        for CTPS in evtTSVInicio.trabalhador.documentos.CTPS:
            s2300_ctps_dados = {}
            s2300_ctps_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_ctps_dados['nrctps'] = CTPS.nrCtps.cdata
            except AttributeError: pass
            try: s2300_ctps_dados['seriectps'] = CTPS.serieCtps.cdata
            except AttributeError: pass
            try: s2300_ctps_dados['ufctps'] = CTPS.ufCtps.cdata
            except AttributeError: pass
            insert = create_insert('s2300_ctps', s2300_ctps_dados)
            resp = executar_sql(insert, True)
            s2300_ctps_id = resp[0][0]
            #print s2300_ctps_id

    if 'RIC' in dir(evtTSVInicio.trabalhador.documentos) and evtTSVInicio.trabalhador.documentos.RIC.cdata != '':
        for RIC in evtTSVInicio.trabalhador.documentos.RIC:
            s2300_ric_dados = {}
            s2300_ric_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_ric_dados['nrric'] = RIC.nrRic.cdata
            except AttributeError: pass
            try: s2300_ric_dados['orgaoemissor'] = RIC.orgaoEmissor.cdata
            except AttributeError: pass
            try: s2300_ric_dados['dtexped'] = RIC.dtExped.cdata
            except AttributeError: pass
            insert = create_insert('s2300_ric', s2300_ric_dados)
            resp = executar_sql(insert, True)
            s2300_ric_id = resp[0][0]
            #print s2300_ric_id

    if 'RG' in dir(evtTSVInicio.trabalhador.documentos) and evtTSVInicio.trabalhador.documentos.RG.cdata != '':
        for RG in evtTSVInicio.trabalhador.documentos.RG:
            s2300_rg_dados = {}
            s2300_rg_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_rg_dados['nrrg'] = RG.nrRg.cdata
            except AttributeError: pass
            try: s2300_rg_dados['orgaoemissor'] = RG.orgaoEmissor.cdata
            except AttributeError: pass
            try: s2300_rg_dados['dtexped'] = RG.dtExped.cdata
            except AttributeError: pass
            insert = create_insert('s2300_rg', s2300_rg_dados)
            resp = executar_sql(insert, True)
            s2300_rg_id = resp[0][0]
            #print s2300_rg_id

    if 'RNE' in dir(evtTSVInicio.trabalhador.documentos) and evtTSVInicio.trabalhador.documentos.RNE.cdata != '':
        for RNE in evtTSVInicio.trabalhador.documentos.RNE:
            s2300_rne_dados = {}
            s2300_rne_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_rne_dados['nrrne'] = RNE.nrRne.cdata
            except AttributeError: pass
            try: s2300_rne_dados['orgaoemissor'] = RNE.orgaoEmissor.cdata
            except AttributeError: pass
            try: s2300_rne_dados['dtexped'] = RNE.dtExped.cdata
            except AttributeError: pass
            insert = create_insert('s2300_rne', s2300_rne_dados)
            resp = executar_sql(insert, True)
            s2300_rne_id = resp[0][0]
            #print s2300_rne_id

    if 'OC' in dir(evtTSVInicio.trabalhador.documentos) and evtTSVInicio.trabalhador.documentos.OC.cdata != '':
        for OC in evtTSVInicio.trabalhador.documentos.OC:
            s2300_oc_dados = {}
            s2300_oc_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_oc_dados['nroc'] = OC.nrOc.cdata
            except AttributeError: pass
            try: s2300_oc_dados['orgaoemissor'] = OC.orgaoEmissor.cdata
            except AttributeError: pass
            try: s2300_oc_dados['dtexped'] = OC.dtExped.cdata
            except AttributeError: pass
            try: s2300_oc_dados['dtvalid'] = OC.dtValid.cdata
            except AttributeError: pass
            insert = create_insert('s2300_oc', s2300_oc_dados)
            resp = executar_sql(insert, True)
            s2300_oc_id = resp[0][0]
            #print s2300_oc_id

    if 'CNH' in dir(evtTSVInicio.trabalhador.documentos) and evtTSVInicio.trabalhador.documentos.CNH.cdata != '':
        for CNH in evtTSVInicio.trabalhador.documentos.CNH:
            s2300_cnh_dados = {}
            s2300_cnh_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_cnh_dados['nrregcnh'] = CNH.nrRegCnh.cdata
            except AttributeError: pass
            try: s2300_cnh_dados['dtexped'] = CNH.dtExped.cdata
            except AttributeError: pass
            try: s2300_cnh_dados['ufcnh'] = CNH.ufCnh.cdata
            except AttributeError: pass
            try: s2300_cnh_dados['dtvalid'] = CNH.dtValid.cdata
            except AttributeError: pass
            try: s2300_cnh_dados['dtprihab'] = CNH.dtPriHab.cdata
            except AttributeError: pass
            try: s2300_cnh_dados['categoriacnh'] = CNH.categoriaCnh.cdata
            except AttributeError: pass
            insert = create_insert('s2300_cnh', s2300_cnh_dados)
            resp = executar_sql(insert, True)
            s2300_cnh_id = resp[0][0]
            #print s2300_cnh_id

    if 'brasil' in dir(evtTSVInicio.trabalhador.endereco) and evtTSVInicio.trabalhador.endereco.brasil.cdata != '':
        for brasil in evtTSVInicio.trabalhador.endereco.brasil:
            s2300_brasil_dados = {}
            s2300_brasil_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_brasil_dados['tplograd'] = brasil.tpLograd.cdata
            except AttributeError: pass
            try: s2300_brasil_dados['dsclograd'] = brasil.dscLograd.cdata
            except AttributeError: pass
            try: s2300_brasil_dados['nrlograd'] = brasil.nrLograd.cdata
            except AttributeError: pass
            try: s2300_brasil_dados['complemento'] = brasil.complemento.cdata
            except AttributeError: pass
            try: s2300_brasil_dados['bairro'] = brasil.bairro.cdata
            except AttributeError: pass
            try: s2300_brasil_dados['cep'] = brasil.cep.cdata
            except AttributeError: pass
            try: s2300_brasil_dados['codmunic'] = brasil.codMunic.cdata
            except AttributeError: pass
            try: s2300_brasil_dados['uf'] = brasil.uf.cdata
            except AttributeError: pass
            insert = create_insert('s2300_brasil', s2300_brasil_dados)
            resp = executar_sql(insert, True)
            s2300_brasil_id = resp[0][0]
            #print s2300_brasil_id

    if 'exterior' in dir(evtTSVInicio.trabalhador.endereco) and evtTSVInicio.trabalhador.endereco.exterior.cdata != '':
        for exterior in evtTSVInicio.trabalhador.endereco.exterior:
            s2300_exterior_dados = {}
            s2300_exterior_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_exterior_dados['paisresid'] = exterior.paisResid.cdata
            except AttributeError: pass
            try: s2300_exterior_dados['dsclograd'] = exterior.dscLograd.cdata
            except AttributeError: pass
            try: s2300_exterior_dados['nrlograd'] = exterior.nrLograd.cdata
            except AttributeError: pass
            try: s2300_exterior_dados['complemento'] = exterior.complemento.cdata
            except AttributeError: pass
            try: s2300_exterior_dados['bairro'] = exterior.bairro.cdata
            except AttributeError: pass
            try: s2300_exterior_dados['nmcid'] = exterior.nmCid.cdata
            except AttributeError: pass
            try: s2300_exterior_dados['codpostal'] = exterior.codPostal.cdata
            except AttributeError: pass
            insert = create_insert('s2300_exterior', s2300_exterior_dados)
            resp = executar_sql(insert, True)
            s2300_exterior_id = resp[0][0]
            #print s2300_exterior_id

    if 'trabEstrangeiro' in dir(evtTSVInicio.trabalhador) and evtTSVInicio.trabalhador.trabEstrangeiro.cdata != '':
        for trabEstrangeiro in evtTSVInicio.trabalhador.trabEstrangeiro:
            s2300_trabestrangeiro_dados = {}
            s2300_trabestrangeiro_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_trabestrangeiro_dados['dtchegada'] = trabEstrangeiro.dtChegada.cdata
            except AttributeError: pass
            try: s2300_trabestrangeiro_dados['classtrabestrang'] = trabEstrangeiro.classTrabEstrang.cdata
            except AttributeError: pass
            try: s2300_trabestrangeiro_dados['casadobr'] = trabEstrangeiro.casadoBr.cdata
            except AttributeError: pass
            try: s2300_trabestrangeiro_dados['filhosbr'] = trabEstrangeiro.filhosBr.cdata
            except AttributeError: pass
            insert = create_insert('s2300_trabestrangeiro', s2300_trabestrangeiro_dados)
            resp = executar_sql(insert, True)
            s2300_trabestrangeiro_id = resp[0][0]
            #print s2300_trabestrangeiro_id

    if 'infoDeficiencia' in dir(evtTSVInicio.trabalhador) and evtTSVInicio.trabalhador.infoDeficiencia.cdata != '':
        for infoDeficiencia in evtTSVInicio.trabalhador.infoDeficiencia:
            s2300_infodeficiencia_dados = {}
            s2300_infodeficiencia_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_infodeficiencia_dados['deffisica'] = infoDeficiencia.defFisica.cdata
            except AttributeError: pass
            try: s2300_infodeficiencia_dados['defvisual'] = infoDeficiencia.defVisual.cdata
            except AttributeError: pass
            try: s2300_infodeficiencia_dados['defauditiva'] = infoDeficiencia.defAuditiva.cdata
            except AttributeError: pass
            try: s2300_infodeficiencia_dados['defmental'] = infoDeficiencia.defMental.cdata
            except AttributeError: pass
            try: s2300_infodeficiencia_dados['defintelectual'] = infoDeficiencia.defIntelectual.cdata
            except AttributeError: pass
            try: s2300_infodeficiencia_dados['reabreadap'] = infoDeficiencia.reabReadap.cdata
            except AttributeError: pass
            try: s2300_infodeficiencia_dados['observacao'] = infoDeficiencia.observacao.cdata
            except AttributeError: pass
            insert = create_insert('s2300_infodeficiencia', s2300_infodeficiencia_dados)
            resp = executar_sql(insert, True)
            s2300_infodeficiencia_id = resp[0][0]
            #print s2300_infodeficiencia_id

    if 'dependente' in dir(evtTSVInicio.trabalhador) and evtTSVInicio.trabalhador.dependente.cdata != '':
        for dependente in evtTSVInicio.trabalhador.dependente:
            s2300_dependente_dados = {}
            s2300_dependente_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_dependente_dados['tpdep'] = dependente.tpDep.cdata
            except AttributeError: pass
            try: s2300_dependente_dados['nmdep'] = dependente.nmDep.cdata
            except AttributeError: pass
            try: s2300_dependente_dados['dtnascto'] = dependente.dtNascto.cdata
            except AttributeError: pass
            try: s2300_dependente_dados['cpfdep'] = dependente.cpfDep.cdata
            except AttributeError: pass
            try: s2300_dependente_dados['sexodep'] = dependente.sexoDep.cdata
            except AttributeError: pass
            try: s2300_dependente_dados['depirrf'] = dependente.depIRRF.cdata
            except AttributeError: pass
            try: s2300_dependente_dados['depsf'] = dependente.depSF.cdata
            except AttributeError: pass
            try: s2300_dependente_dados['inctrab'] = dependente.incTrab.cdata
            except AttributeError: pass
            try: s2300_dependente_dados['depfinsprev'] = dependente.depFinsPrev.cdata
            except AttributeError: pass
            insert = create_insert('s2300_dependente', s2300_dependente_dados)
            resp = executar_sql(insert, True)
            s2300_dependente_id = resp[0][0]
            #print s2300_dependente_id

    if 'contato' in dir(evtTSVInicio.trabalhador) and evtTSVInicio.trabalhador.contato.cdata != '':
        for contato in evtTSVInicio.trabalhador.contato:
            s2300_contato_dados = {}
            s2300_contato_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_contato_dados['foneprinc'] = contato.fonePrinc.cdata
            except AttributeError: pass
            try: s2300_contato_dados['fonealternat'] = contato.foneAlternat.cdata
            except AttributeError: pass
            try: s2300_contato_dados['emailprinc'] = contato.emailPrinc.cdata
            except AttributeError: pass
            try: s2300_contato_dados['emailalternat'] = contato.emailAlternat.cdata
            except AttributeError: pass
            insert = create_insert('s2300_contato', s2300_contato_dados)
            resp = executar_sql(insert, True)
            s2300_contato_id = resp[0][0]
            #print s2300_contato_id

    if 'cargoFuncao' in dir(evtTSVInicio.infoTSVInicio.infoComplementares) and evtTSVInicio.infoTSVInicio.infoComplementares.cargoFuncao.cdata != '':
        for cargoFuncao in evtTSVInicio.infoTSVInicio.infoComplementares.cargoFuncao:
            s2300_cargofuncao_dados = {}
            s2300_cargofuncao_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_cargofuncao_dados['codcargo'] = cargoFuncao.codCargo.cdata
            except AttributeError: pass
            try: s2300_cargofuncao_dados['codfuncao'] = cargoFuncao.codFuncao.cdata
            except AttributeError: pass
            insert = create_insert('s2300_cargofuncao', s2300_cargofuncao_dados)
            resp = executar_sql(insert, True)
            s2300_cargofuncao_id = resp[0][0]
            #print s2300_cargofuncao_id

    if 'remuneracao' in dir(evtTSVInicio.infoTSVInicio.infoComplementares) and evtTSVInicio.infoTSVInicio.infoComplementares.remuneracao.cdata != '':
        for remuneracao in evtTSVInicio.infoTSVInicio.infoComplementares.remuneracao:
            s2300_remuneracao_dados = {}
            s2300_remuneracao_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_remuneracao_dados['vrsalfx'] = remuneracao.vrSalFx.cdata
            except AttributeError: pass
            try: s2300_remuneracao_dados['undsalfixo'] = remuneracao.undSalFixo.cdata
            except AttributeError: pass
            try: s2300_remuneracao_dados['dscsalvar'] = remuneracao.dscSalVar.cdata
            except AttributeError: pass
            insert = create_insert('s2300_remuneracao', s2300_remuneracao_dados)
            resp = executar_sql(insert, True)
            s2300_remuneracao_id = resp[0][0]
            #print s2300_remuneracao_id

    if 'fgts' in dir(evtTSVInicio.infoTSVInicio.infoComplementares) and evtTSVInicio.infoTSVInicio.infoComplementares.fgts.cdata != '':
        for fgts in evtTSVInicio.infoTSVInicio.infoComplementares.fgts:
            s2300_fgts_dados = {}
            s2300_fgts_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_fgts_dados['opcfgts'] = fgts.opcFGTS.cdata
            except AttributeError: pass
            try: s2300_fgts_dados['dtopcfgts'] = fgts.dtOpcFGTS.cdata
            except AttributeError: pass
            insert = create_insert('s2300_fgts', s2300_fgts_dados)
            resp = executar_sql(insert, True)
            s2300_fgts_id = resp[0][0]
            #print s2300_fgts_id

    if 'infoDirigenteSindical' in dir(evtTSVInicio.infoTSVInicio.infoComplementares) and evtTSVInicio.infoTSVInicio.infoComplementares.infoDirigenteSindical.cdata != '':
        for infoDirigenteSindical in evtTSVInicio.infoTSVInicio.infoComplementares.infoDirigenteSindical:
            s2300_infodirigentesindical_dados = {}
            s2300_infodirigentesindical_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_infodirigentesindical_dados['categorig'] = infoDirigenteSindical.categOrig.cdata
            except AttributeError: pass
            try: s2300_infodirigentesindical_dados['cnpjorigem'] = infoDirigenteSindical.cnpjOrigem.cdata
            except AttributeError: pass
            try: s2300_infodirigentesindical_dados['dtadmorig'] = infoDirigenteSindical.dtAdmOrig.cdata
            except AttributeError: pass
            try: s2300_infodirigentesindical_dados['matricorig'] = infoDirigenteSindical.matricOrig.cdata
            except AttributeError: pass
            insert = create_insert('s2300_infodirigentesindical', s2300_infodirigentesindical_dados)
            resp = executar_sql(insert, True)
            s2300_infodirigentesindical_id = resp[0][0]
            #print s2300_infodirigentesindical_id

    if 'infoTrabCedido' in dir(evtTSVInicio.infoTSVInicio.infoComplementares) and evtTSVInicio.infoTSVInicio.infoComplementares.infoTrabCedido.cdata != '':
        for infoTrabCedido in evtTSVInicio.infoTSVInicio.infoComplementares.infoTrabCedido:
            s2300_infotrabcedido_dados = {}
            s2300_infotrabcedido_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_infotrabcedido_dados['categorig'] = infoTrabCedido.categOrig.cdata
            except AttributeError: pass
            try: s2300_infotrabcedido_dados['cnpjcednt'] = infoTrabCedido.cnpjCednt.cdata
            except AttributeError: pass
            try: s2300_infotrabcedido_dados['matricced'] = infoTrabCedido.matricCed.cdata
            except AttributeError: pass
            try: s2300_infotrabcedido_dados['dtadmced'] = infoTrabCedido.dtAdmCed.cdata
            except AttributeError: pass
            try: s2300_infotrabcedido_dados['tpregtrab'] = infoTrabCedido.tpRegTrab.cdata
            except AttributeError: pass
            try: s2300_infotrabcedido_dados['tpregprev'] = infoTrabCedido.tpRegPrev.cdata
            except AttributeError: pass
            try: s2300_infotrabcedido_dados['infonus'] = infoTrabCedido.infOnus.cdata
            except AttributeError: pass
            try: s2300_infotrabcedido_dados['indremuncargo'] = infoTrabCedido.indRemunCargo.cdata
            except AttributeError: pass
            insert = create_insert('s2300_infotrabcedido', s2300_infotrabcedido_dados)
            resp = executar_sql(insert, True)
            s2300_infotrabcedido_id = resp[0][0]
            #print s2300_infotrabcedido_id

    if 'infoEstagiario' in dir(evtTSVInicio.infoTSVInicio.infoComplementares) and evtTSVInicio.infoTSVInicio.infoComplementares.infoEstagiario.cdata != '':
        for infoEstagiario in evtTSVInicio.infoTSVInicio.infoComplementares.infoEstagiario:
            s2300_infoestagiario_dados = {}
            s2300_infoestagiario_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_infoestagiario_dados['natestagio'] = infoEstagiario.natEstagio.cdata
            except AttributeError: pass
            try: s2300_infoestagiario_dados['nivestagio'] = infoEstagiario.nivEstagio.cdata
            except AttributeError: pass
            try: s2300_infoestagiario_dados['areaatuacao'] = infoEstagiario.areaAtuacao.cdata
            except AttributeError: pass
            try: s2300_infoestagiario_dados['nrapol'] = infoEstagiario.nrApol.cdata
            except AttributeError: pass
            try: s2300_infoestagiario_dados['vlrbolsa'] = infoEstagiario.vlrBolsa.cdata
            except AttributeError: pass
            try: s2300_infoestagiario_dados['dtprevterm'] = infoEstagiario.dtPrevTerm.cdata
            except AttributeError: pass
            try: s2300_infoestagiario_dados['cnpjinstensino'] = infoEstagiario.instEnsino.cnpjInstEnsino.cdata
            except AttributeError: pass
            try: s2300_infoestagiario_dados['nmrazao'] = infoEstagiario.instEnsino.nmRazao.cdata
            except AttributeError: pass
            try: s2300_infoestagiario_dados['dsclograd'] = infoEstagiario.instEnsino.dscLograd.cdata
            except AttributeError: pass
            try: s2300_infoestagiario_dados['nrlograd'] = infoEstagiario.instEnsino.nrLograd.cdata
            except AttributeError: pass
            try: s2300_infoestagiario_dados['bairro'] = infoEstagiario.instEnsino.bairro.cdata
            except AttributeError: pass
            try: s2300_infoestagiario_dados['cep'] = infoEstagiario.instEnsino.cep.cdata
            except AttributeError: pass
            try: s2300_infoestagiario_dados['codmunic'] = infoEstagiario.instEnsino.codMunic.cdata
            except AttributeError: pass
            try: s2300_infoestagiario_dados['uf'] = infoEstagiario.instEnsino.uf.cdata
            except AttributeError: pass
            insert = create_insert('s2300_infoestagiario', s2300_infoestagiario_dados)
            resp = executar_sql(insert, True)
            s2300_infoestagiario_id = resp[0][0]
            #print s2300_infoestagiario_id

            if 'ageIntegracao' in dir(infoEstagiario) and infoEstagiario.ageIntegracao.cdata != '':
                for ageIntegracao in infoEstagiario.ageIntegracao:
                    s2300_ageintegracao_dados = {}
                    s2300_ageintegracao_dados['s2300_infoestagiario_id'] = s2300_infoestagiario_id

                    try: s2300_ageintegracao_dados['cnpjagntinteg'] = ageIntegracao.cnpjAgntInteg.cdata
                    except AttributeError: pass
                    try: s2300_ageintegracao_dados['nmrazao'] = ageIntegracao.nmRazao.cdata
                    except AttributeError: pass
                    try: s2300_ageintegracao_dados['dsclograd'] = ageIntegracao.dscLograd.cdata
                    except AttributeError: pass
                    try: s2300_ageintegracao_dados['nrlograd'] = ageIntegracao.nrLograd.cdata
                    except AttributeError: pass
                    try: s2300_ageintegracao_dados['bairro'] = ageIntegracao.bairro.cdata
                    except AttributeError: pass
                    try: s2300_ageintegracao_dados['cep'] = ageIntegracao.cep.cdata
                    except AttributeError: pass
                    try: s2300_ageintegracao_dados['codmunic'] = ageIntegracao.codMunic.cdata
                    except AttributeError: pass
                    try: s2300_ageintegracao_dados['uf'] = ageIntegracao.uf.cdata
                    except AttributeError: pass
                    insert = create_insert('s2300_ageintegracao', s2300_ageintegracao_dados)
                    resp = executar_sql(insert, True)
                    s2300_ageintegracao_id = resp[0][0]
                    #print s2300_ageintegracao_id

            if 'supervisorEstagio' in dir(infoEstagiario) and infoEstagiario.supervisorEstagio.cdata != '':
                for supervisorEstagio in infoEstagiario.supervisorEstagio:
                    s2300_supervisorestagio_dados = {}
                    s2300_supervisorestagio_dados['s2300_infoestagiario_id'] = s2300_infoestagiario_id

                    try: s2300_supervisorestagio_dados['cpfsupervisor'] = supervisorEstagio.cpfSupervisor.cdata
                    except AttributeError: pass
                    try: s2300_supervisorestagio_dados['nmsuperv'] = supervisorEstagio.nmSuperv.cdata
                    except AttributeError: pass
                    insert = create_insert('s2300_supervisorestagio', s2300_supervisorestagio_dados)
                    resp = executar_sql(insert, True)
                    s2300_supervisorestagio_id = resp[0][0]
                    #print s2300_supervisorestagio_id

    if 'mudancaCPF' in dir(evtTSVInicio.infoTSVInicio) and evtTSVInicio.infoTSVInicio.mudancaCPF.cdata != '':
        for mudancaCPF in evtTSVInicio.infoTSVInicio.mudancaCPF:
            s2300_mudancacpf_dados = {}
            s2300_mudancacpf_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_mudancacpf_dados['cpfant'] = mudancaCPF.cpfAnt.cdata
            except AttributeError: pass
            try: s2300_mudancacpf_dados['dtaltcpf'] = mudancaCPF.dtAltCPF.cdata
            except AttributeError: pass
            try: s2300_mudancacpf_dados['observacao'] = mudancaCPF.observacao.cdata
            except AttributeError: pass
            insert = create_insert('s2300_mudancacpf', s2300_mudancacpf_dados)
            resp = executar_sql(insert, True)
            s2300_mudancacpf_id = resp[0][0]
            #print s2300_mudancacpf_id

    if 'afastamento' in dir(evtTSVInicio.infoTSVInicio) and evtTSVInicio.infoTSVInicio.afastamento.cdata != '':
        for afastamento in evtTSVInicio.infoTSVInicio.afastamento:
            s2300_afastamento_dados = {}
            s2300_afastamento_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_afastamento_dados['dtiniafast'] = afastamento.dtIniAfast.cdata
            except AttributeError: pass
            try: s2300_afastamento_dados['codmotafast'] = afastamento.codMotAfast.cdata
            except AttributeError: pass
            insert = create_insert('s2300_afastamento', s2300_afastamento_dados)
            resp = executar_sql(insert, True)
            s2300_afastamento_id = resp[0][0]
            #print s2300_afastamento_id

    if 'termino' in dir(evtTSVInicio.infoTSVInicio) and evtTSVInicio.infoTSVInicio.termino.cdata != '':
        for termino in evtTSVInicio.infoTSVInicio.termino:
            s2300_termino_dados = {}
            s2300_termino_dados['s2300_evttsvinicio_id'] = s2300_evttsvinicio_id

            try: s2300_termino_dados['dtterm'] = termino.dtTerm.cdata
            except AttributeError: pass
            insert = create_insert('s2300_termino', s2300_termino_dados)
            resp = executar_sql(insert, True)
            s2300_termino_id = resp[0][0]
            #print s2300_termino_id

    from emensageriapro.esocial.views.s2300_evttsvinicio_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2300_evttsvinicio_id, 'default')
    return dados