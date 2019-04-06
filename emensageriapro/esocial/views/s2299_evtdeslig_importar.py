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



def read_s2299_evtdeslig_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2299_evtdeslig_obj(doc, status, validar)
    return dados

def read_s2299_evtdeslig(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2299_evtdeslig_obj(doc, status, validar)
    return dados



def read_s2299_evtdeslig_obj(doc, status, validar=False):
    s2299_evtdeslig_dados = {}
    s2299_evtdeslig_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2299_evtdeslig_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2299_evtdeslig_dados['identidade'] = doc.eSocial.evtDeslig['Id']
    evtDeslig = doc.eSocial.evtDeslig

    try: s2299_evtdeslig_dados['indretif'] = evtDeslig.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['nrrecibo'] = evtDeslig.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['tpamb'] = evtDeslig.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['procemi'] = evtDeslig.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['verproc'] = evtDeslig.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['tpinsc'] = evtDeslig.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['nrinsc'] = evtDeslig.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['cpftrab'] = evtDeslig.ideVinculo.cpfTrab.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['nistrab'] = evtDeslig.ideVinculo.nisTrab.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['matricula'] = evtDeslig.ideVinculo.matricula.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['mtvdeslig'] = evtDeslig.infoDeslig.mtvDeslig.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['dtdeslig'] = evtDeslig.infoDeslig.dtDeslig.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['indpagtoapi'] = evtDeslig.infoDeslig.indPagtoAPI.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['dtprojfimapi'] = evtDeslig.infoDeslig.dtProjFimAPI.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['pensalim'] = evtDeslig.infoDeslig.pensAlim.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['percaliment'] = evtDeslig.infoDeslig.percAliment.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['vralim'] = evtDeslig.infoDeslig.vrAlim.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['nrcertobito'] = evtDeslig.infoDeslig.nrCertObito.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['nrproctrab'] = evtDeslig.infoDeslig.nrProcTrab.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['indcumprparc'] = evtDeslig.infoDeslig.indCumprParc.cdata
    except AttributeError: pass
    try: s2299_evtdeslig_dados['qtddiasinterm'] = evtDeslig.infoDeslig.qtdDiasInterm.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtDeslig.infoDeslig): s2299_evtdeslig_dados['operacao'] = 1
    elif 'alteracao' in dir(evtDeslig.infoDeslig): s2299_evtdeslig_dados['operacao'] = 2
    elif 'exclusao' in dir(evtDeslig.infoDeslig): s2299_evtdeslig_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2299_evtdeslig', s2299_evtdeslig_dados)
    resp = executar_sql(insert, True)
    s2299_evtdeslig_id = resp[0][0]
    dados = s2299_evtdeslig_dados
    dados['evento'] = 's2299'
    dados['id'] = s2299_evtdeslig_id
    dados['identidade_evento'] = doc.eSocial.evtDeslig['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'observacoes' in dir(evtDeslig.infoDeslig) and evtDeslig.infoDeslig.observacoes.cdata != '':
        for observacoes in evtDeslig.infoDeslig.observacoes:
            s2299_observacoes_dados = {}
            s2299_observacoes_dados['s2299_evtdeslig_id'] = s2299_evtdeslig_id

            try: s2299_observacoes_dados['observacao'] = observacoes.observacao.cdata
            except AttributeError: pass
            insert = create_insert('s2299_observacoes', s2299_observacoes_dados)
            resp = executar_sql(insert, True)
            s2299_observacoes_id = resp[0][0]
            #print s2299_observacoes_id

    if 'sucessaoVinc' in dir(evtDeslig.infoDeslig) and evtDeslig.infoDeslig.sucessaoVinc.cdata != '':
        for sucessaoVinc in evtDeslig.infoDeslig.sucessaoVinc:
            s2299_sucessaovinc_dados = {}
            s2299_sucessaovinc_dados['s2299_evtdeslig_id'] = s2299_evtdeslig_id

            try: s2299_sucessaovinc_dados['tpinscsuc'] = sucessaoVinc.tpInscSuc.cdata
            except AttributeError: pass
            try: s2299_sucessaovinc_dados['cnpjsucessora'] = sucessaoVinc.cnpjSucessora.cdata
            except AttributeError: pass
            insert = create_insert('s2299_sucessaovinc', s2299_sucessaovinc_dados)
            resp = executar_sql(insert, True)
            s2299_sucessaovinc_id = resp[0][0]
            #print s2299_sucessaovinc_id

    if 'transfTit' in dir(evtDeslig.infoDeslig) and evtDeslig.infoDeslig.transfTit.cdata != '':
        for transfTit in evtDeslig.infoDeslig.transfTit:
            s2299_transftit_dados = {}
            s2299_transftit_dados['s2299_evtdeslig_id'] = s2299_evtdeslig_id

            try: s2299_transftit_dados['cpfsubstituto'] = transfTit.cpfSubstituto.cdata
            except AttributeError: pass
            try: s2299_transftit_dados['dtnascto'] = transfTit.dtNascto.cdata
            except AttributeError: pass
            insert = create_insert('s2299_transftit', s2299_transftit_dados)
            resp = executar_sql(insert, True)
            s2299_transftit_id = resp[0][0]
            #print s2299_transftit_id

    if 'mudancaCPF' in dir(evtDeslig.infoDeslig) and evtDeslig.infoDeslig.mudancaCPF.cdata != '':
        for mudancaCPF in evtDeslig.infoDeslig.mudancaCPF:
            s2299_mudancacpf_dados = {}
            s2299_mudancacpf_dados['s2299_evtdeslig_id'] = s2299_evtdeslig_id

            try: s2299_mudancacpf_dados['novocpf'] = mudancaCPF.novoCPF.cdata
            except AttributeError: pass
            insert = create_insert('s2299_mudancacpf', s2299_mudancacpf_dados)
            resp = executar_sql(insert, True)
            s2299_mudancacpf_id = resp[0][0]
            #print s2299_mudancacpf_id

    if 'dmDev' in dir(evtDeslig.infoDeslig.verbasResc) and evtDeslig.infoDeslig.verbasResc.dmDev.cdata != '':
        for dmDev in evtDeslig.infoDeslig.verbasResc.dmDev:
            s2299_dmdev_dados = {}
            s2299_dmdev_dados['s2299_evtdeslig_id'] = s2299_evtdeslig_id

            try: s2299_dmdev_dados['idedmdev'] = dmDev.ideDmDev.cdata
            except AttributeError: pass
            insert = create_insert('s2299_dmdev', s2299_dmdev_dados)
            resp = executar_sql(insert, True)
            s2299_dmdev_id = resp[0][0]
            #print s2299_dmdev_id

            if 'ideEstabLot' in dir(dmDev.infoPerApur) and dmDev.infoPerApur.ideEstabLot.cdata != '':
                for ideEstabLot in dmDev.infoPerApur.ideEstabLot:
                    s2299_infoperapur_ideestablot_dados = {}
                    s2299_infoperapur_ideestablot_dados['s2299_dmdev_id'] = s2299_dmdev_id

                    try: s2299_infoperapur_ideestablot_dados['tpinsc'] = ideEstabLot.tpInsc.cdata
                    except AttributeError: pass
                    try: s2299_infoperapur_ideestablot_dados['nrinsc'] = ideEstabLot.nrInsc.cdata
                    except AttributeError: pass
                    try: s2299_infoperapur_ideestablot_dados['codlotacao'] = ideEstabLot.codLotacao.cdata
                    except AttributeError: pass
                    insert = create_insert('s2299_infoperapur_ideestablot', s2299_infoperapur_ideestablot_dados)
                    resp = executar_sql(insert, True)
                    s2299_infoperapur_ideestablot_id = resp[0][0]
                    #print s2299_infoperapur_ideestablot_id

            if 'ideADC' in dir(dmDev.infoPerAnt) and dmDev.infoPerAnt.ideADC.cdata != '':
                for ideADC in dmDev.infoPerAnt.ideADC:
                    s2299_infoperant_ideadc_dados = {}
                    s2299_infoperant_ideadc_dados['s2299_dmdev_id'] = s2299_dmdev_id

                    try: s2299_infoperant_ideadc_dados['dtacconv'] = ideADC.dtAcConv.cdata
                    except AttributeError: pass
                    try: s2299_infoperant_ideadc_dados['tpacconv'] = ideADC.tpAcConv.cdata
                    except AttributeError: pass
                    try: s2299_infoperant_ideadc_dados['compacconv'] = ideADC.compAcConv.cdata
                    except AttributeError: pass
                    try: s2299_infoperant_ideadc_dados['dtefacconv'] = ideADC.dtEfAcConv.cdata
                    except AttributeError: pass
                    try: s2299_infoperant_ideadc_dados['dsc'] = ideADC.dsc.cdata
                    except AttributeError: pass
                    insert = create_insert('s2299_infoperant_ideadc', s2299_infoperant_ideadc_dados)
                    resp = executar_sql(insert, True)
                    s2299_infoperant_ideadc_id = resp[0][0]
                    #print s2299_infoperant_ideadc_id

            if 'infoTrabInterm' in dir(dmDev) and dmDev.infoTrabInterm.cdata != '':
                for infoTrabInterm in dmDev.infoTrabInterm:
                    s2299_infotrabinterm_dados = {}
                    s2299_infotrabinterm_dados['s2299_dmdev_id'] = s2299_dmdev_id

                    try: s2299_infotrabinterm_dados['codconv'] = infoTrabInterm.codConv.cdata
                    except AttributeError: pass
                    insert = create_insert('s2299_infotrabinterm', s2299_infotrabinterm_dados)
                    resp = executar_sql(insert, True)
                    s2299_infotrabinterm_id = resp[0][0]
                    #print s2299_infotrabinterm_id

    if 'procJudTrab' in dir(evtDeslig.infoDeslig.verbasResc) and evtDeslig.infoDeslig.verbasResc.procJudTrab.cdata != '':
        for procJudTrab in evtDeslig.infoDeslig.verbasResc.procJudTrab:
            s2299_infotrabinterm_procjudtrab_dados = {}
            s2299_infotrabinterm_procjudtrab_dados['s2299_evtdeslig_id'] = s2299_evtdeslig_id

            try: s2299_infotrabinterm_procjudtrab_dados['tptrib'] = procJudTrab.tpTrib.cdata
            except AttributeError: pass
            try: s2299_infotrabinterm_procjudtrab_dados['nrprocjud'] = procJudTrab.nrProcJud.cdata
            except AttributeError: pass
            try: s2299_infotrabinterm_procjudtrab_dados['codsusp'] = procJudTrab.codSusp.cdata
            except AttributeError: pass
            insert = create_insert('s2299_infotrabinterm_procjudtrab', s2299_infotrabinterm_procjudtrab_dados)
            resp = executar_sql(insert, True)
            s2299_infotrabinterm_procjudtrab_id = resp[0][0]
            #print s2299_infotrabinterm_procjudtrab_id

    if 'infoMV' in dir(evtDeslig.infoDeslig.verbasResc) and evtDeslig.infoDeslig.verbasResc.infoMV.cdata != '':
        for infoMV in evtDeslig.infoDeslig.verbasResc.infoMV:
            s2299_infotrabinterm_infomv_dados = {}
            s2299_infotrabinterm_infomv_dados['s2299_evtdeslig_id'] = s2299_evtdeslig_id

            try: s2299_infotrabinterm_infomv_dados['indmv'] = infoMV.indMV.cdata
            except AttributeError: pass
            insert = create_insert('s2299_infotrabinterm_infomv', s2299_infotrabinterm_infomv_dados)
            resp = executar_sql(insert, True)
            s2299_infotrabinterm_infomv_id = resp[0][0]
            #print s2299_infotrabinterm_infomv_id

            if 'remunOutrEmpr' in dir(infoMV) and infoMV.remunOutrEmpr.cdata != '':
                for remunOutrEmpr in infoMV.remunOutrEmpr:
                    s2299_infotrabinterm_remunoutrempr_dados = {}
                    s2299_infotrabinterm_remunoutrempr_dados['s2299_infotrabinterm_infomv_id'] = s2299_infotrabinterm_infomv_id

                    try: s2299_infotrabinterm_remunoutrempr_dados['tpinsc'] = remunOutrEmpr.tpInsc.cdata
                    except AttributeError: pass
                    try: s2299_infotrabinterm_remunoutrempr_dados['nrinsc'] = remunOutrEmpr.nrInsc.cdata
                    except AttributeError: pass
                    try: s2299_infotrabinterm_remunoutrempr_dados['codcateg'] = remunOutrEmpr.codCateg.cdata
                    except AttributeError: pass
                    try: s2299_infotrabinterm_remunoutrempr_dados['vlrremunoe'] = remunOutrEmpr.vlrRemunOE.cdata
                    except AttributeError: pass
                    insert = create_insert('s2299_infotrabinterm_remunoutrempr', s2299_infotrabinterm_remunoutrempr_dados)
                    resp = executar_sql(insert, True)
                    s2299_infotrabinterm_remunoutrempr_id = resp[0][0]
                    #print s2299_infotrabinterm_remunoutrempr_id

    if 'procCS' in dir(evtDeslig.infoDeslig.verbasResc) and evtDeslig.infoDeslig.verbasResc.procCS.cdata != '':
        for procCS in evtDeslig.infoDeslig.verbasResc.procCS:
            s2299_infotrabinterm_proccs_dados = {}
            s2299_infotrabinterm_proccs_dados['s2299_evtdeslig_id'] = s2299_evtdeslig_id

            try: s2299_infotrabinterm_proccs_dados['nrprocjud'] = procCS.nrProcJud.cdata
            except AttributeError: pass
            insert = create_insert('s2299_infotrabinterm_proccs', s2299_infotrabinterm_proccs_dados)
            resp = executar_sql(insert, True)
            s2299_infotrabinterm_proccs_id = resp[0][0]
            #print s2299_infotrabinterm_proccs_id

    if 'quarentena' in dir(evtDeslig.infoDeslig) and evtDeslig.infoDeslig.quarentena.cdata != '':
        for quarentena in evtDeslig.infoDeslig.quarentena:
            s2299_infotrabinterm_quarentena_dados = {}
            s2299_infotrabinterm_quarentena_dados['s2299_evtdeslig_id'] = s2299_evtdeslig_id

            try: s2299_infotrabinterm_quarentena_dados['dtfimquar'] = quarentena.dtFimQuar.cdata
            except AttributeError: pass
            insert = create_insert('s2299_infotrabinterm_quarentena', s2299_infotrabinterm_quarentena_dados)
            resp = executar_sql(insert, True)
            s2299_infotrabinterm_quarentena_id = resp[0][0]
            #print s2299_infotrabinterm_quarentena_id

    if 'consigFGTS' in dir(evtDeslig.infoDeslig) and evtDeslig.infoDeslig.consigFGTS.cdata != '':
        for consigFGTS in evtDeslig.infoDeslig.consigFGTS:
            s2299_infotrabinterm_consigfgts_dados = {}
            s2299_infotrabinterm_consigfgts_dados['s2299_evtdeslig_id'] = s2299_evtdeslig_id

            try: s2299_infotrabinterm_consigfgts_dados['insconsig'] = consigFGTS.insConsig.cdata
            except AttributeError: pass
            try: s2299_infotrabinterm_consigfgts_dados['nrcontr'] = consigFGTS.nrContr.cdata
            except AttributeError: pass
            insert = create_insert('s2299_infotrabinterm_consigfgts', s2299_infotrabinterm_consigfgts_dados)
            resp = executar_sql(insert, True)
            s2299_infotrabinterm_consigfgts_id = resp[0][0]
            #print s2299_infotrabinterm_consigfgts_id

    from emensageriapro.esocial.views.s2299_evtdeslig_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2299_evtdeslig_id, 'default')
    return dados