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



def read_r2070_evtpgtosdivs_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r2070_evtpgtosdivs_obj(doc, status, validar)
    return dados

def read_r2070_evtpgtosdivs(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r2070_evtpgtosdivs_obj(doc, status, validar)
    return dados



def read_r2070_evtpgtosdivs_obj(doc, status, validar=False):
    r2070_evtpgtosdivs_dados = {}
    r2070_evtpgtosdivs_dados['status'] = status
    xmlns_lista = doc.Reinf['xmlns'].split('/')
    r2070_evtpgtosdivs_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2070_evtpgtosdivs_dados['identidade'] = doc.Reinf.evtPgtosDivs['id']
    evtPgtosDivs = doc.Reinf.evtPgtosDivs

    try: r2070_evtpgtosdivs_dados['indretif'] = evtPgtosDivs.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: r2070_evtpgtosdivs_dados['nrrecibo'] = evtPgtosDivs.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: r2070_evtpgtosdivs_dados['perapur'] = evtPgtosDivs.ideEvento.perApur.cdata
    except AttributeError: pass
    try: r2070_evtpgtosdivs_dados['tpamb'] = evtPgtosDivs.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: r2070_evtpgtosdivs_dados['procemi'] = evtPgtosDivs.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: r2070_evtpgtosdivs_dados['verproc'] = evtPgtosDivs.ideEvento.verProc.cdata
    except AttributeError: pass
    try: r2070_evtpgtosdivs_dados['tpinsc'] = evtPgtosDivs.ideContri.tpInsc.cdata
    except AttributeError: pass
    try: r2070_evtpgtosdivs_dados['nrinsc'] = evtPgtosDivs.ideContri.nrInsc.cdata
    except AttributeError: pass
    try: r2070_evtpgtosdivs_dados['codpgto'] = evtPgtosDivs.ideBenef.codPgto.cdata
    except AttributeError: pass
    try: r2070_evtpgtosdivs_dados['tpinscbenef'] = evtPgtosDivs.ideBenef.tpInscBenef.cdata
    except AttributeError: pass
    try: r2070_evtpgtosdivs_dados['nrinscbenef'] = evtPgtosDivs.ideBenef.nrInscBenef.cdata
    except AttributeError: pass
    try: r2070_evtpgtosdivs_dados['nmrazaobenef'] = evtPgtosDivs.ideBenef.nmRazaoBenef.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtPgtosDivs.ideBenef): r2070_evtpgtosdivs_dados['operacao'] = 1
    elif 'alteracao' in dir(evtPgtosDivs.ideBenef): r2070_evtpgtosdivs_dados['operacao'] = 2
    elif 'exclusao' in dir(evtPgtosDivs.ideBenef): r2070_evtpgtosdivs_dados['operacao'] = 3
    #print dados
    insert = create_insert('r2070_evtpgtosdivs', r2070_evtpgtosdivs_dados)
    resp = executar_sql(insert, True)
    r2070_evtpgtosdivs_id = resp[0][0]
    dados = r2070_evtpgtosdivs_dados
    dados['evento'] = 'r2070'
    dados['id'] = r2070_evtpgtosdivs_id
    dados['identidade_evento'] = doc.Reinf.evtPgtosDivs['id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'infoResidExt' in dir(evtPgtosDivs.ideBenef) and evtPgtosDivs.ideBenef.infoResidExt.cdata != '':
        for infoResidExt in evtPgtosDivs.ideBenef.infoResidExt:
            r2070_inforesidext_dados = {}
            r2070_inforesidext_dados['r2070_evtpgtosdivs_id'] = r2070_evtpgtosdivs_id

            try: r2070_inforesidext_dados['paisresid'] = infoResidExt.infoEnder.paisResid.cdata
            except AttributeError: pass
            try: r2070_inforesidext_dados['dsclograd'] = infoResidExt.infoEnder.dscLograd.cdata
            except AttributeError: pass
            try: r2070_inforesidext_dados['nrlograd'] = infoResidExt.infoEnder.nrLograd.cdata
            except AttributeError: pass
            try: r2070_inforesidext_dados['complem'] = infoResidExt.infoEnder.complem.cdata
            except AttributeError: pass
            try: r2070_inforesidext_dados['bairro'] = infoResidExt.infoEnder.bairro.cdata
            except AttributeError: pass
            try: r2070_inforesidext_dados['cidade'] = infoResidExt.infoEnder.cidade.cdata
            except AttributeError: pass
            try: r2070_inforesidext_dados['codpostal'] = infoResidExt.infoEnder.codPostal.cdata
            except AttributeError: pass
            try: r2070_inforesidext_dados['indnif'] = infoResidExt.infoFiscal.indNIF.cdata
            except AttributeError: pass
            try: r2070_inforesidext_dados['nifbenef'] = infoResidExt.infoFiscal.nifBenef.cdata
            except AttributeError: pass
            try: r2070_inforesidext_dados['relfontepagad'] = infoResidExt.infoFiscal.relFontePagad.cdata
            except AttributeError: pass
            insert = create_insert('r2070_inforesidext', r2070_inforesidext_dados)
            resp = executar_sql(insert, True)
            r2070_inforesidext_id = resp[0][0]
            #print r2070_inforesidext_id

    if 'infoMolestia' in dir(evtPgtosDivs.ideBenef) and evtPgtosDivs.ideBenef.infoMolestia.cdata != '':
        for infoMolestia in evtPgtosDivs.ideBenef.infoMolestia:
            r2070_infomolestia_dados = {}
            r2070_infomolestia_dados['r2070_evtpgtosdivs_id'] = r2070_evtpgtosdivs_id

            try: r2070_infomolestia_dados['dtlaudo'] = infoMolestia.dtLaudo.cdata
            except AttributeError: pass
            insert = create_insert('r2070_infomolestia', r2070_infomolestia_dados)
            resp = executar_sql(insert, True)
            r2070_infomolestia_id = resp[0][0]
            #print r2070_infomolestia_id

    if 'ideEstab' in dir(evtPgtosDivs.ideBenef.infoPgto) and evtPgtosDivs.ideBenef.infoPgto.ideEstab.cdata != '':
        for ideEstab in evtPgtosDivs.ideBenef.infoPgto.ideEstab:
            r2070_ideestab_dados = {}
            r2070_ideestab_dados['r2070_evtpgtosdivs_id'] = r2070_evtpgtosdivs_id

            try: r2070_ideestab_dados['tpinsc'] = ideEstab.tpInsc.cdata
            except AttributeError: pass
            try: r2070_ideestab_dados['nrinsc'] = ideEstab.nrInsc.cdata
            except AttributeError: pass
            insert = create_insert('r2070_ideestab', r2070_ideestab_dados)
            resp = executar_sql(insert, True)
            r2070_ideestab_id = resp[0][0]
            #print r2070_ideestab_id

            if 'pgtoPF' in dir(ideEstab.pgtoResidBR) and ideEstab.pgtoResidBR.pgtoPF.cdata != '':
                for pgtoPF in ideEstab.pgtoResidBR.pgtoPF:
                    r2070_pgtopf_dados = {}
                    r2070_pgtopf_dados['r2070_ideestab_id'] = r2070_ideestab_id

                    try: r2070_pgtopf_dados['dtpgto'] = pgtoPF.dtPgto.cdata
                    except AttributeError: pass
                    try: r2070_pgtopf_dados['indsuspexig'] = pgtoPF.indSuspExig.cdata
                    except AttributeError: pass
                    try: r2070_pgtopf_dados['inddecterceiro'] = pgtoPF.indDecTerceiro.cdata
                    except AttributeError: pass
                    try: r2070_pgtopf_dados['vlrrendtributavel'] = pgtoPF.vlrRendTributavel.cdata
                    except AttributeError: pass
                    try: r2070_pgtopf_dados['vlrirrf'] = pgtoPF.vlrIRRF.cdata
                    except AttributeError: pass
                    insert = create_insert('r2070_pgtopf', r2070_pgtopf_dados)
                    resp = executar_sql(insert, True)
                    r2070_pgtopf_id = resp[0][0]
                    #print r2070_pgtopf_id

            if 'pgtoPJ' in dir(ideEstab.pgtoResidBR) and ideEstab.pgtoResidBR.pgtoPJ.cdata != '':
                for pgtoPJ in ideEstab.pgtoResidBR.pgtoPJ:
                    r2070_pgtopj_dados = {}
                    r2070_pgtopj_dados['r2070_ideestab_id'] = r2070_ideestab_id

                    try: r2070_pgtopj_dados['dtpagto'] = pgtoPJ.dtPagto.cdata
                    except AttributeError: pass
                    try: r2070_pgtopj_dados['vlrrendtributavel'] = pgtoPJ.vlrRendTributavel.cdata
                    except AttributeError: pass
                    try: r2070_pgtopj_dados['vlrret'] = pgtoPJ.vlrRet.cdata
                    except AttributeError: pass
                    insert = create_insert('r2070_pgtopj', r2070_pgtopj_dados)
                    resp = executar_sql(insert, True)
                    r2070_pgtopj_id = resp[0][0]
                    #print r2070_pgtopj_id

            if 'pgtoResidExt' in dir(ideEstab) and ideEstab.pgtoResidExt.cdata != '':
                for pgtoResidExt in ideEstab.pgtoResidExt:
                    r2070_pgtoresidext_dados = {}
                    r2070_pgtoresidext_dados['r2070_ideestab_id'] = r2070_ideestab_id

                    try: r2070_pgtoresidext_dados['dtpagto'] = pgtoResidExt.dtPagto.cdata
                    except AttributeError: pass
                    try: r2070_pgtoresidext_dados['tprendimento'] = pgtoResidExt.tpRendimento.cdata
                    except AttributeError: pass
                    try: r2070_pgtoresidext_dados['formatributacao'] = pgtoResidExt.formaTributacao.cdata
                    except AttributeError: pass
                    try: r2070_pgtoresidext_dados['vlrpgto'] = pgtoResidExt.vlrPgto.cdata
                    except AttributeError: pass
                    try: r2070_pgtoresidext_dados['vlrret'] = pgtoResidExt.vlrRet.cdata
                    except AttributeError: pass
                    insert = create_insert('r2070_pgtoresidext', r2070_pgtoresidext_dados)
                    resp = executar_sql(insert, True)
                    r2070_pgtoresidext_id = resp[0][0]
                    #print r2070_pgtoresidext_id

    from emensageriapro.efdreinf.views.r2070_evtpgtosdivs_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r2070_evtpgtosdivs_id, 'default')
    return dados