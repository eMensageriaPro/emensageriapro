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



def read_s1200_evtremun_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1200_evtremun_obj(doc, status, validar)
    return dados

def read_s1200_evtremun(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1200_evtremun_obj(doc, status, validar)
    return dados



def read_s1200_evtremun_obj(doc, status, validar=False):
    s1200_evtremun_dados = {}
    s1200_evtremun_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1200_evtremun_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1200_evtremun_dados['identidade'] = doc.eSocial.evtRemun['Id']
    evtRemun = doc.eSocial.evtRemun

    try: s1200_evtremun_dados['indretif'] = evtRemun.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s1200_evtremun_dados['nrrecibo'] = evtRemun.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s1200_evtremun_dados['indapuracao'] = evtRemun.ideEvento.indApuracao.cdata
    except AttributeError: pass
    try: s1200_evtremun_dados['perapur'] = evtRemun.ideEvento.perApur.cdata
    except AttributeError: pass
    try: s1200_evtremun_dados['tpamb'] = evtRemun.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s1200_evtremun_dados['procemi'] = evtRemun.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s1200_evtremun_dados['verproc'] = evtRemun.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s1200_evtremun_dados['tpinsc'] = evtRemun.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s1200_evtremun_dados['nrinsc'] = evtRemun.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s1200_evtremun_dados['cpftrab'] = evtRemun.ideTrabalhador.cpfTrab.cdata
    except AttributeError: pass
    try: s1200_evtremun_dados['nistrab'] = evtRemun.ideTrabalhador.nisTrab.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtRemun.dmDev): s1200_evtremun_dados['operacao'] = 1
    elif 'alteracao' in dir(evtRemun.dmDev): s1200_evtremun_dados['operacao'] = 2
    elif 'exclusao' in dir(evtRemun.dmDev): s1200_evtremun_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1200_evtremun', s1200_evtremun_dados)
    resp = executar_sql(insert, True)
    s1200_evtremun_id = resp[0][0]
    dados = s1200_evtremun_dados
    dados['evento'] = 's1200'
    dados['id'] = s1200_evtremun_id
    dados['identidade_evento'] = doc.eSocial.evtRemun['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'infoMV' in dir(evtRemun.ideTrabalhador) and evtRemun.ideTrabalhador.infoMV.cdata != '':
        for infoMV in evtRemun.ideTrabalhador.infoMV:
            s1200_infomv_dados = {}
            s1200_infomv_dados['s1200_evtremun_id'] = s1200_evtremun_id

            try: s1200_infomv_dados['indmv'] = infoMV.indMV.cdata
            except AttributeError: pass
            insert = create_insert('s1200_infomv', s1200_infomv_dados)
            resp = executar_sql(insert, True)
            s1200_infomv_id = resp[0][0]
            #print s1200_infomv_id

            if 'remunOutrEmpr' in dir(infoMV) and infoMV.remunOutrEmpr.cdata != '':
                for remunOutrEmpr in infoMV.remunOutrEmpr:
                    s1200_remunoutrempr_dados = {}
                    s1200_remunoutrempr_dados['s1200_infomv_id'] = s1200_infomv_id

                    try: s1200_remunoutrempr_dados['tpinsc'] = remunOutrEmpr.tpInsc.cdata
                    except AttributeError: pass
                    try: s1200_remunoutrempr_dados['nrinsc'] = remunOutrEmpr.nrInsc.cdata
                    except AttributeError: pass
                    try: s1200_remunoutrempr_dados['codcateg'] = remunOutrEmpr.codCateg.cdata
                    except AttributeError: pass
                    try: s1200_remunoutrempr_dados['vlrremunoe'] = remunOutrEmpr.vlrRemunOE.cdata
                    except AttributeError: pass
                    insert = create_insert('s1200_remunoutrempr', s1200_remunoutrempr_dados)
                    resp = executar_sql(insert, True)
                    s1200_remunoutrempr_id = resp[0][0]
                    #print s1200_remunoutrempr_id

    if 'infoComplem' in dir(evtRemun.ideTrabalhador) and evtRemun.ideTrabalhador.infoComplem.cdata != '':
        for infoComplem in evtRemun.ideTrabalhador.infoComplem:
            s1200_infocomplem_dados = {}
            s1200_infocomplem_dados['s1200_evtremun_id'] = s1200_evtremun_id

            try: s1200_infocomplem_dados['nmtrab'] = infoComplem.nmTrab.cdata
            except AttributeError: pass
            try: s1200_infocomplem_dados['dtnascto'] = infoComplem.dtNascto.cdata
            except AttributeError: pass
            insert = create_insert('s1200_infocomplem', s1200_infocomplem_dados)
            resp = executar_sql(insert, True)
            s1200_infocomplem_id = resp[0][0]
            #print s1200_infocomplem_id

            if 'sucessaoVinc' in dir(infoComplem) and infoComplem.sucessaoVinc.cdata != '':
                for sucessaoVinc in infoComplem.sucessaoVinc:
                    s1200_sucessaovinc_dados = {}
                    s1200_sucessaovinc_dados['s1200_infocomplem_id'] = s1200_infocomplem_id

                    try: s1200_sucessaovinc_dados['tpinscant'] = sucessaoVinc.tpInscAnt.cdata
                    except AttributeError: pass
                    try: s1200_sucessaovinc_dados['cnpjempregant'] = sucessaoVinc.cnpjEmpregAnt.cdata
                    except AttributeError: pass
                    try: s1200_sucessaovinc_dados['matricant'] = sucessaoVinc.matricAnt.cdata
                    except AttributeError: pass
                    try: s1200_sucessaovinc_dados['dtadm'] = sucessaoVinc.dtAdm.cdata
                    except AttributeError: pass
                    try: s1200_sucessaovinc_dados['observacao'] = sucessaoVinc.observacao.cdata
                    except AttributeError: pass
                    insert = create_insert('s1200_sucessaovinc', s1200_sucessaovinc_dados)
                    resp = executar_sql(insert, True)
                    s1200_sucessaovinc_id = resp[0][0]
                    #print s1200_sucessaovinc_id

    if 'procJudTrab' in dir(evtRemun.ideTrabalhador) and evtRemun.ideTrabalhador.procJudTrab.cdata != '':
        for procJudTrab in evtRemun.ideTrabalhador.procJudTrab:
            s1200_procjudtrab_dados = {}
            s1200_procjudtrab_dados['s1200_evtremun_id'] = s1200_evtremun_id

            try: s1200_procjudtrab_dados['tptrib'] = procJudTrab.tpTrib.cdata
            except AttributeError: pass
            try: s1200_procjudtrab_dados['nrprocjud'] = procJudTrab.nrProcJud.cdata
            except AttributeError: pass
            try: s1200_procjudtrab_dados['codsusp'] = procJudTrab.codSusp.cdata
            except AttributeError: pass
            insert = create_insert('s1200_procjudtrab', s1200_procjudtrab_dados)
            resp = executar_sql(insert, True)
            s1200_procjudtrab_id = resp[0][0]
            #print s1200_procjudtrab_id

    if 'infoInterm' in dir(evtRemun.ideTrabalhador) and evtRemun.ideTrabalhador.infoInterm.cdata != '':
        for infoInterm in evtRemun.ideTrabalhador.infoInterm:
            s1200_infointerm_dados = {}
            s1200_infointerm_dados['s1200_evtremun_id'] = s1200_evtremun_id

            try: s1200_infointerm_dados['qtddiasinterm'] = infoInterm.qtdDiasInterm.cdata
            except AttributeError: pass
            insert = create_insert('s1200_infointerm', s1200_infointerm_dados)
            resp = executar_sql(insert, True)
            s1200_infointerm_id = resp[0][0]
            #print s1200_infointerm_id

    if 'dmDev' in dir(evtRemun) and evtRemun.dmDev.cdata != '':
        for dmDev in evtRemun.dmDev:
            s1200_dmdev_dados = {}
            s1200_dmdev_dados['s1200_evtremun_id'] = s1200_evtremun_id

            try: s1200_dmdev_dados['idedmdev'] = dmDev.ideDmDev.cdata
            except AttributeError: pass
            try: s1200_dmdev_dados['codcateg'] = dmDev.codCateg.cdata
            except AttributeError: pass
            insert = create_insert('s1200_dmdev', s1200_dmdev_dados)
            resp = executar_sql(insert, True)
            s1200_dmdev_id = resp[0][0]
            #print s1200_dmdev_id

            if 'ideEstabLot' in dir(dmDev.infoPerApur) and dmDev.infoPerApur.ideEstabLot.cdata != '':
                for ideEstabLot in dmDev.infoPerApur.ideEstabLot:
                    s1200_infoperapur_ideestablot_dados = {}
                    s1200_infoperapur_ideestablot_dados['s1200_dmdev_id'] = s1200_dmdev_id

                    try: s1200_infoperapur_ideestablot_dados['tpinsc'] = ideEstabLot.tpInsc.cdata
                    except AttributeError: pass
                    try: s1200_infoperapur_ideestablot_dados['nrinsc'] = ideEstabLot.nrInsc.cdata
                    except AttributeError: pass
                    try: s1200_infoperapur_ideestablot_dados['codlotacao'] = ideEstabLot.codLotacao.cdata
                    except AttributeError: pass
                    try: s1200_infoperapur_ideestablot_dados['qtddiasav'] = ideEstabLot.qtdDiasAv.cdata
                    except AttributeError: pass
                    insert = create_insert('s1200_infoperapur_ideestablot', s1200_infoperapur_ideestablot_dados)
                    resp = executar_sql(insert, True)
                    s1200_infoperapur_ideestablot_id = resp[0][0]
                    #print s1200_infoperapur_ideestablot_id

            if 'ideADC' in dir(dmDev.infoPerAnt) and dmDev.infoPerAnt.ideADC.cdata != '':
                for ideADC in dmDev.infoPerAnt.ideADC:
                    s1200_infoperant_ideadc_dados = {}
                    s1200_infoperant_ideadc_dados['s1200_dmdev_id'] = s1200_dmdev_id

                    try: s1200_infoperant_ideadc_dados['dtacconv'] = ideADC.dtAcConv.cdata
                    except AttributeError: pass
                    try: s1200_infoperant_ideadc_dados['tpacconv'] = ideADC.tpAcConv.cdata
                    except AttributeError: pass
                    try: s1200_infoperant_ideadc_dados['compacconv'] = ideADC.compAcConv.cdata
                    except AttributeError: pass
                    try: s1200_infoperant_ideadc_dados['dtefacconv'] = ideADC.dtEfAcConv.cdata
                    except AttributeError: pass
                    try: s1200_infoperant_ideadc_dados['dsc'] = ideADC.dsc.cdata
                    except AttributeError: pass
                    try: s1200_infoperant_ideadc_dados['remunsuc'] = ideADC.remunSuc.cdata
                    except AttributeError: pass
                    insert = create_insert('s1200_infoperant_ideadc', s1200_infoperant_ideadc_dados)
                    resp = executar_sql(insert, True)
                    s1200_infoperant_ideadc_id = resp[0][0]
                    #print s1200_infoperant_ideadc_id

            if 'infoComplCont' in dir(dmDev) and dmDev.infoComplCont.cdata != '':
                for infoComplCont in dmDev.infoComplCont:
                    s1200_infoperant_infocomplcont_dados = {}
                    s1200_infoperant_infocomplcont_dados['s1200_dmdev_id'] = s1200_dmdev_id

                    try: s1200_infoperant_infocomplcont_dados['codcbo'] = infoComplCont.codCBO.cdata
                    except AttributeError: pass
                    try: s1200_infoperant_infocomplcont_dados['natatividade'] = infoComplCont.natAtividade.cdata
                    except AttributeError: pass
                    try: s1200_infoperant_infocomplcont_dados['qtddiastrab'] = infoComplCont.qtdDiasTrab.cdata
                    except AttributeError: pass
                    insert = create_insert('s1200_infoperant_infocomplcont', s1200_infoperant_infocomplcont_dados)
                    resp = executar_sql(insert, True)
                    s1200_infoperant_infocomplcont_id = resp[0][0]
                    #print s1200_infoperant_infocomplcont_id

    from emensageriapro.esocial.views.s1200_evtremun_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1200_evtremun_id, 'default')
    return dados