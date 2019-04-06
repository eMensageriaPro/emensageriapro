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



def read_s2205_evtaltcadastral_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2205_evtaltcadastral_obj(doc, status, validar)
    return dados

def read_s2205_evtaltcadastral(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2205_evtaltcadastral_obj(doc, status, validar)
    return dados



def read_s2205_evtaltcadastral_obj(doc, status, validar=False):
    s2205_evtaltcadastral_dados = {}
    s2205_evtaltcadastral_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2205_evtaltcadastral_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2205_evtaltcadastral_dados['identidade'] = doc.eSocial.evtAltCadastral['Id']
    evtAltCadastral = doc.eSocial.evtAltCadastral

    try: s2205_evtaltcadastral_dados['indretif'] = evtAltCadastral.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['nrrecibo'] = evtAltCadastral.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['tpamb'] = evtAltCadastral.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['procemi'] = evtAltCadastral.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['verproc'] = evtAltCadastral.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['tpinsc'] = evtAltCadastral.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['nrinsc'] = evtAltCadastral.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['cpftrab'] = evtAltCadastral.ideTrabalhador.cpfTrab.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['dtalteracao'] = evtAltCadastral.alteracao.dtAlteracao.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['nistrab'] = evtAltCadastral.alteracao.dadosTrabalhador.nisTrab.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['nmtrab'] = evtAltCadastral.alteracao.dadosTrabalhador.nmTrab.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['sexo'] = evtAltCadastral.alteracao.dadosTrabalhador.sexo.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['racacor'] = evtAltCadastral.alteracao.dadosTrabalhador.racaCor.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['estciv'] = evtAltCadastral.alteracao.dadosTrabalhador.estCiv.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['grauinstr'] = evtAltCadastral.alteracao.dadosTrabalhador.grauInstr.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['nmsoc'] = evtAltCadastral.alteracao.dadosTrabalhador.nmSoc.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['dtnascto'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.dtNascto.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['codmunic'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.codMunic.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['uf'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.uf.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['paisnascto'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.paisNascto.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['paisnac'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.paisNac.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['nmmae'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.nmMae.cdata
    except AttributeError: pass
    try: s2205_evtaltcadastral_dados['nmpai'] = evtAltCadastral.alteracao.dadosTrabalhador.nascimento.nmPai.cdata
    except AttributeError: pass
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
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'CTPS' in dir(evtAltCadastral.alteracao.dadosTrabalhador.documentos) and evtAltCadastral.alteracao.dadosTrabalhador.documentos.CTPS.cdata != '':
        for CTPS in evtAltCadastral.alteracao.dadosTrabalhador.documentos.CTPS:
            s2205_ctps_dados = {}
            s2205_ctps_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id

            try: s2205_ctps_dados['nrctps'] = CTPS.nrCtps.cdata
            except AttributeError: pass
            try: s2205_ctps_dados['seriectps'] = CTPS.serieCtps.cdata
            except AttributeError: pass
            try: s2205_ctps_dados['ufctps'] = CTPS.ufCtps.cdata
            except AttributeError: pass
            insert = create_insert('s2205_ctps', s2205_ctps_dados)
            resp = executar_sql(insert, True)
            s2205_ctps_id = resp[0][0]
            #print s2205_ctps_id

    if 'RIC' in dir(evtAltCadastral.alteracao.dadosTrabalhador.documentos) and evtAltCadastral.alteracao.dadosTrabalhador.documentos.RIC.cdata != '':
        for RIC in evtAltCadastral.alteracao.dadosTrabalhador.documentos.RIC:
            s2205_ric_dados = {}
            s2205_ric_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id

            try: s2205_ric_dados['nrric'] = RIC.nrRic.cdata
            except AttributeError: pass
            try: s2205_ric_dados['orgaoemissor'] = RIC.orgaoEmissor.cdata
            except AttributeError: pass
            try: s2205_ric_dados['dtexped'] = RIC.dtExped.cdata
            except AttributeError: pass
            insert = create_insert('s2205_ric', s2205_ric_dados)
            resp = executar_sql(insert, True)
            s2205_ric_id = resp[0][0]
            #print s2205_ric_id

    if 'RG' in dir(evtAltCadastral.alteracao.dadosTrabalhador.documentos) and evtAltCadastral.alteracao.dadosTrabalhador.documentos.RG.cdata != '':
        for RG in evtAltCadastral.alteracao.dadosTrabalhador.documentos.RG:
            s2205_rg_dados = {}
            s2205_rg_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id

            try: s2205_rg_dados['nrrg'] = RG.nrRg.cdata
            except AttributeError: pass
            try: s2205_rg_dados['orgaoemissor'] = RG.orgaoEmissor.cdata
            except AttributeError: pass
            try: s2205_rg_dados['dtexped'] = RG.dtExped.cdata
            except AttributeError: pass
            insert = create_insert('s2205_rg', s2205_rg_dados)
            resp = executar_sql(insert, True)
            s2205_rg_id = resp[0][0]
            #print s2205_rg_id

    if 'RNE' in dir(evtAltCadastral.alteracao.dadosTrabalhador.documentos) and evtAltCadastral.alteracao.dadosTrabalhador.documentos.RNE.cdata != '':
        for RNE in evtAltCadastral.alteracao.dadosTrabalhador.documentos.RNE:
            s2205_rne_dados = {}
            s2205_rne_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id

            try: s2205_rne_dados['nrrne'] = RNE.nrRne.cdata
            except AttributeError: pass
            try: s2205_rne_dados['orgaoemissor'] = RNE.orgaoEmissor.cdata
            except AttributeError: pass
            try: s2205_rne_dados['dtexped'] = RNE.dtExped.cdata
            except AttributeError: pass
            insert = create_insert('s2205_rne', s2205_rne_dados)
            resp = executar_sql(insert, True)
            s2205_rne_id = resp[0][0]
            #print s2205_rne_id

    if 'OC' in dir(evtAltCadastral.alteracao.dadosTrabalhador.documentos) and evtAltCadastral.alteracao.dadosTrabalhador.documentos.OC.cdata != '':
        for OC in evtAltCadastral.alteracao.dadosTrabalhador.documentos.OC:
            s2205_oc_dados = {}
            s2205_oc_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id

            try: s2205_oc_dados['nroc'] = OC.nrOc.cdata
            except AttributeError: pass
            try: s2205_oc_dados['orgaoemissor'] = OC.orgaoEmissor.cdata
            except AttributeError: pass
            try: s2205_oc_dados['dtexped'] = OC.dtExped.cdata
            except AttributeError: pass
            try: s2205_oc_dados['dtvalid'] = OC.dtValid.cdata
            except AttributeError: pass
            insert = create_insert('s2205_oc', s2205_oc_dados)
            resp = executar_sql(insert, True)
            s2205_oc_id = resp[0][0]
            #print s2205_oc_id

    if 'CNH' in dir(evtAltCadastral.alteracao.dadosTrabalhador.documentos) and evtAltCadastral.alteracao.dadosTrabalhador.documentos.CNH.cdata != '':
        for CNH in evtAltCadastral.alteracao.dadosTrabalhador.documentos.CNH:
            s2205_cnh_dados = {}
            s2205_cnh_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id

            try: s2205_cnh_dados['nrregcnh'] = CNH.nrRegCnh.cdata
            except AttributeError: pass
            try: s2205_cnh_dados['dtexped'] = CNH.dtExped.cdata
            except AttributeError: pass
            try: s2205_cnh_dados['ufcnh'] = CNH.ufCnh.cdata
            except AttributeError: pass
            try: s2205_cnh_dados['dtvalid'] = CNH.dtValid.cdata
            except AttributeError: pass
            try: s2205_cnh_dados['dtprihab'] = CNH.dtPriHab.cdata
            except AttributeError: pass
            try: s2205_cnh_dados['categoriacnh'] = CNH.categoriaCnh.cdata
            except AttributeError: pass
            insert = create_insert('s2205_cnh', s2205_cnh_dados)
            resp = executar_sql(insert, True)
            s2205_cnh_id = resp[0][0]
            #print s2205_cnh_id

    if 'brasil' in dir(evtAltCadastral.alteracao.dadosTrabalhador.endereco) and evtAltCadastral.alteracao.dadosTrabalhador.endereco.brasil.cdata != '':
        for brasil in evtAltCadastral.alteracao.dadosTrabalhador.endereco.brasil:
            s2205_brasil_dados = {}
            s2205_brasil_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id

            try: s2205_brasil_dados['tplograd'] = brasil.tpLograd.cdata
            except AttributeError: pass
            try: s2205_brasil_dados['dsclograd'] = brasil.dscLograd.cdata
            except AttributeError: pass
            try: s2205_brasil_dados['nrlograd'] = brasil.nrLograd.cdata
            except AttributeError: pass
            try: s2205_brasil_dados['complemento'] = brasil.complemento.cdata
            except AttributeError: pass
            try: s2205_brasil_dados['bairro'] = brasil.bairro.cdata
            except AttributeError: pass
            try: s2205_brasil_dados['cep'] = brasil.cep.cdata
            except AttributeError: pass
            try: s2205_brasil_dados['codmunic'] = brasil.codMunic.cdata
            except AttributeError: pass
            try: s2205_brasil_dados['uf'] = brasil.uf.cdata
            except AttributeError: pass
            insert = create_insert('s2205_brasil', s2205_brasil_dados)
            resp = executar_sql(insert, True)
            s2205_brasil_id = resp[0][0]
            #print s2205_brasil_id

    if 'exterior' in dir(evtAltCadastral.alteracao.dadosTrabalhador.endereco) and evtAltCadastral.alteracao.dadosTrabalhador.endereco.exterior.cdata != '':
        for exterior in evtAltCadastral.alteracao.dadosTrabalhador.endereco.exterior:
            s2205_exterior_dados = {}
            s2205_exterior_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id

            try: s2205_exterior_dados['paisresid'] = exterior.paisResid.cdata
            except AttributeError: pass
            try: s2205_exterior_dados['dsclograd'] = exterior.dscLograd.cdata
            except AttributeError: pass
            try: s2205_exterior_dados['nrlograd'] = exterior.nrLograd.cdata
            except AttributeError: pass
            try: s2205_exterior_dados['complemento'] = exterior.complemento.cdata
            except AttributeError: pass
            try: s2205_exterior_dados['bairro'] = exterior.bairro.cdata
            except AttributeError: pass
            try: s2205_exterior_dados['nmcid'] = exterior.nmCid.cdata
            except AttributeError: pass
            try: s2205_exterior_dados['codpostal'] = exterior.codPostal.cdata
            except AttributeError: pass
            insert = create_insert('s2205_exterior', s2205_exterior_dados)
            resp = executar_sql(insert, True)
            s2205_exterior_id = resp[0][0]
            #print s2205_exterior_id

    if 'trabEstrangeiro' in dir(evtAltCadastral.alteracao.dadosTrabalhador) and evtAltCadastral.alteracao.dadosTrabalhador.trabEstrangeiro.cdata != '':
        for trabEstrangeiro in evtAltCadastral.alteracao.dadosTrabalhador.trabEstrangeiro:
            s2205_trabestrangeiro_dados = {}
            s2205_trabestrangeiro_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id

            try: s2205_trabestrangeiro_dados['dtchegada'] = trabEstrangeiro.dtChegada.cdata
            except AttributeError: pass
            try: s2205_trabestrangeiro_dados['classtrabestrang'] = trabEstrangeiro.classTrabEstrang.cdata
            except AttributeError: pass
            try: s2205_trabestrangeiro_dados['casadobr'] = trabEstrangeiro.casadoBr.cdata
            except AttributeError: pass
            try: s2205_trabestrangeiro_dados['filhosbr'] = trabEstrangeiro.filhosBr.cdata
            except AttributeError: pass
            insert = create_insert('s2205_trabestrangeiro', s2205_trabestrangeiro_dados)
            resp = executar_sql(insert, True)
            s2205_trabestrangeiro_id = resp[0][0]
            #print s2205_trabestrangeiro_id

    if 'infoDeficiencia' in dir(evtAltCadastral.alteracao.dadosTrabalhador) and evtAltCadastral.alteracao.dadosTrabalhador.infoDeficiencia.cdata != '':
        for infoDeficiencia in evtAltCadastral.alteracao.dadosTrabalhador.infoDeficiencia:
            s2205_infodeficiencia_dados = {}
            s2205_infodeficiencia_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id

            try: s2205_infodeficiencia_dados['deffisica'] = infoDeficiencia.defFisica.cdata
            except AttributeError: pass
            try: s2205_infodeficiencia_dados['defvisual'] = infoDeficiencia.defVisual.cdata
            except AttributeError: pass
            try: s2205_infodeficiencia_dados['defauditiva'] = infoDeficiencia.defAuditiva.cdata
            except AttributeError: pass
            try: s2205_infodeficiencia_dados['defmental'] = infoDeficiencia.defMental.cdata
            except AttributeError: pass
            try: s2205_infodeficiencia_dados['defintelectual'] = infoDeficiencia.defIntelectual.cdata
            except AttributeError: pass
            try: s2205_infodeficiencia_dados['reabreadap'] = infoDeficiencia.reabReadap.cdata
            except AttributeError: pass
            try: s2205_infodeficiencia_dados['infocota'] = infoDeficiencia.infoCota.cdata
            except AttributeError: pass
            try: s2205_infodeficiencia_dados['observacao'] = infoDeficiencia.observacao.cdata
            except AttributeError: pass
            insert = create_insert('s2205_infodeficiencia', s2205_infodeficiencia_dados)
            resp = executar_sql(insert, True)
            s2205_infodeficiencia_id = resp[0][0]
            #print s2205_infodeficiencia_id

    if 'dependente' in dir(evtAltCadastral.alteracao.dadosTrabalhador) and evtAltCadastral.alteracao.dadosTrabalhador.dependente.cdata != '':
        for dependente in evtAltCadastral.alteracao.dadosTrabalhador.dependente:
            s2205_dependente_dados = {}
            s2205_dependente_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id

            try: s2205_dependente_dados['tpdep'] = dependente.tpDep.cdata
            except AttributeError: pass
            try: s2205_dependente_dados['nmdep'] = dependente.nmDep.cdata
            except AttributeError: pass
            try: s2205_dependente_dados['dtnascto'] = dependente.dtNascto.cdata
            except AttributeError: pass
            try: s2205_dependente_dados['cpfdep'] = dependente.cpfDep.cdata
            except AttributeError: pass
            try: s2205_dependente_dados['sexodep'] = dependente.sexoDep.cdata
            except AttributeError: pass
            try: s2205_dependente_dados['depirrf'] = dependente.depIRRF.cdata
            except AttributeError: pass
            try: s2205_dependente_dados['depsf'] = dependente.depSF.cdata
            except AttributeError: pass
            try: s2205_dependente_dados['inctrab'] = dependente.incTrab.cdata
            except AttributeError: pass
            try: s2205_dependente_dados['depfinsprev'] = dependente.depFinsPrev.cdata
            except AttributeError: pass
            insert = create_insert('s2205_dependente', s2205_dependente_dados)
            resp = executar_sql(insert, True)
            s2205_dependente_id = resp[0][0]
            #print s2205_dependente_id

    if 'aposentadoria' in dir(evtAltCadastral.alteracao.dadosTrabalhador) and evtAltCadastral.alteracao.dadosTrabalhador.aposentadoria.cdata != '':
        for aposentadoria in evtAltCadastral.alteracao.dadosTrabalhador.aposentadoria:
            s2205_aposentadoria_dados = {}
            s2205_aposentadoria_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id

            try: s2205_aposentadoria_dados['trabaposent'] = aposentadoria.trabAposent.cdata
            except AttributeError: pass
            insert = create_insert('s2205_aposentadoria', s2205_aposentadoria_dados)
            resp = executar_sql(insert, True)
            s2205_aposentadoria_id = resp[0][0]
            #print s2205_aposentadoria_id

    if 'contato' in dir(evtAltCadastral.alteracao.dadosTrabalhador) and evtAltCadastral.alteracao.dadosTrabalhador.contato.cdata != '':
        for contato in evtAltCadastral.alteracao.dadosTrabalhador.contato:
            s2205_contato_dados = {}
            s2205_contato_dados['s2205_evtaltcadastral_id'] = s2205_evtaltcadastral_id

            try: s2205_contato_dados['foneprinc'] = contato.fonePrinc.cdata
            except AttributeError: pass
            try: s2205_contato_dados['fonealternat'] = contato.foneAlternat.cdata
            except AttributeError: pass
            try: s2205_contato_dados['emailprinc'] = contato.emailPrinc.cdata
            except AttributeError: pass
            try: s2205_contato_dados['emailalternat'] = contato.emailAlternat.cdata
            except AttributeError: pass
            insert = create_insert('s2205_contato', s2205_contato_dados)
            resp = executar_sql(insert, True)
            s2205_contato_id = resp[0][0]
            #print s2205_contato_id

    from emensageriapro.esocial.views.s2205_evtaltcadastral_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2205_evtaltcadastral_id, 'default')
    return dados