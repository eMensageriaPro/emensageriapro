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



def read_s2399_evttsvtermino_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2399_evttsvtermino_obj(doc, status, validar)
    return dados

def read_s2399_evttsvtermino(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2399_evttsvtermino_obj(doc, status, validar)
    return dados



def read_s2399_evttsvtermino_obj(doc, status, validar=False):
    s2399_evttsvtermino_dados = {}
    s2399_evttsvtermino_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2399_evttsvtermino_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2399_evttsvtermino_dados['identidade'] = doc.eSocial.evtTSVTermino['Id']
    s2399_evttsvtermino_dados['processamento_codigo_resposta'] = 1
    evtTSVTermino = doc.eSocial.evtTSVTermino

    if 'indRetif' in dir(evtTSVTermino.ideEvento): s2399_evttsvtermino_dados['indretif'] = evtTSVTermino.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtTSVTermino.ideEvento): s2399_evttsvtermino_dados['nrrecibo'] = evtTSVTermino.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtTSVTermino.ideEvento): s2399_evttsvtermino_dados['tpamb'] = evtTSVTermino.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTSVTermino.ideEvento): s2399_evttsvtermino_dados['procemi'] = evtTSVTermino.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTSVTermino.ideEvento): s2399_evttsvtermino_dados['verproc'] = evtTSVTermino.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTSVTermino.ideEmpregador): s2399_evttsvtermino_dados['tpinsc'] = evtTSVTermino.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTSVTermino.ideEmpregador): s2399_evttsvtermino_dados['nrinsc'] = evtTSVTermino.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtTSVTermino.ideTrabSemVinculo): s2399_evttsvtermino_dados['cpftrab'] = evtTSVTermino.ideTrabSemVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtTSVTermino.ideTrabSemVinculo): s2399_evttsvtermino_dados['nistrab'] = evtTSVTermino.ideTrabSemVinculo.nisTrab.cdata
    if 'codCateg' in dir(evtTSVTermino.ideTrabSemVinculo): s2399_evttsvtermino_dados['codcateg'] = evtTSVTermino.ideTrabSemVinculo.codCateg.cdata
    if 'dtTerm' in dir(evtTSVTermino.infoTSVTermino): s2399_evttsvtermino_dados['dtterm'] = evtTSVTermino.infoTSVTermino.dtTerm.cdata
    if 'mtvDesligTSV' in dir(evtTSVTermino.infoTSVTermino): s2399_evttsvtermino_dados['mtvdesligtsv'] = evtTSVTermino.infoTSVTermino.mtvDesligTSV.cdata
    if 'pensAlim' in dir(evtTSVTermino.infoTSVTermino): s2399_evttsvtermino_dados['pensalim'] = evtTSVTermino.infoTSVTermino.pensAlim.cdata
    if 'percAliment' in dir(evtTSVTermino.infoTSVTermino): s2399_evttsvtermino_dados['percaliment'] = evtTSVTermino.infoTSVTermino.percAliment.cdata
    if 'vrAlim' in dir(evtTSVTermino.infoTSVTermino): s2399_evttsvtermino_dados['vralim'] = evtTSVTermino.infoTSVTermino.vrAlim.cdata
    if 'inclusao' in dir(evtTSVTermino.infoTSVTermino): s2399_evttsvtermino_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTSVTermino.infoTSVTermino): s2399_evttsvtermino_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTSVTermino.infoTSVTermino): s2399_evttsvtermino_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2399_evttsvtermino', s2399_evttsvtermino_dados)
    resp = executar_sql(insert, True)
    s2399_evttsvtermino_id = resp[0][0]
    dados = s2399_evttsvtermino_dados
    dados['evento'] = 's2399'
    dados['id'] = s2399_evttsvtermino_id
    dados['identidade_evento'] = doc.eSocial.evtTSVTermino['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'mudancaCPF' in dir(evtTSVTermino.infoTSVTermino):
        for mudancaCPF in evtTSVTermino.infoTSVTermino.mudancaCPF:
            s2399_mudancacpf_dados = {}
            s2399_mudancacpf_dados['s2399_evttsvtermino_id'] = s2399_evttsvtermino_id

            if 'novoCPF' in dir(mudancaCPF): s2399_mudancacpf_dados['novocpf'] = mudancaCPF.novoCPF.cdata
            insert = create_insert('s2399_mudancacpf', s2399_mudancacpf_dados)
            resp = executar_sql(insert, True)
            s2399_mudancacpf_id = resp[0][0]
            #print s2399_mudancacpf_id

    if 'dmDev' in dir(evtTSVTermino.infoTSVTermino.verbasResc):
        for dmDev in evtTSVTermino.infoTSVTermino.verbasResc.dmDev:
            s2399_dmdev_dados = {}
            s2399_dmdev_dados['s2399_evttsvtermino_id'] = s2399_evttsvtermino_id

            if 'ideDmDev' in dir(dmDev): s2399_dmdev_dados['idedmdev'] = dmDev.ideDmDev.cdata
            insert = create_insert('s2399_dmdev', s2399_dmdev_dados)
            resp = executar_sql(insert, True)
            s2399_dmdev_id = resp[0][0]
            #print s2399_dmdev_id

            if 'ideEstabLot' in dir(dmDev):
                for ideEstabLot in dmDev.ideEstabLot:
                    s2399_ideestablot_dados = {}
                    s2399_ideestablot_dados['s2399_dmdev_id'] = s2399_dmdev_id

                    if 'tpInsc' in dir(ideEstabLot): s2399_ideestablot_dados['tpinsc'] = ideEstabLot.tpInsc.cdata
                    if 'nrInsc' in dir(ideEstabLot): s2399_ideestablot_dados['nrinsc'] = ideEstabLot.nrInsc.cdata
                    if 'codLotacao' in dir(ideEstabLot): s2399_ideestablot_dados['codlotacao'] = ideEstabLot.codLotacao.cdata
                    insert = create_insert('s2399_ideestablot', s2399_ideestablot_dados)
                    resp = executar_sql(insert, True)
                    s2399_ideestablot_id = resp[0][0]
                    #print s2399_ideestablot_id

    if 'procJudTrab' in dir(evtTSVTermino.infoTSVTermino.verbasResc):
        for procJudTrab in evtTSVTermino.infoTSVTermino.verbasResc.procJudTrab:
            s2399_procjudtrab_dados = {}
            s2399_procjudtrab_dados['s2399_evttsvtermino_id'] = s2399_evttsvtermino_id

            if 'tpTrib' in dir(procJudTrab): s2399_procjudtrab_dados['tptrib'] = procJudTrab.tpTrib.cdata
            if 'nrProcJud' in dir(procJudTrab): s2399_procjudtrab_dados['nrprocjud'] = procJudTrab.nrProcJud.cdata
            if 'codSusp' in dir(procJudTrab): s2399_procjudtrab_dados['codsusp'] = procJudTrab.codSusp.cdata
            insert = create_insert('s2399_procjudtrab', s2399_procjudtrab_dados)
            resp = executar_sql(insert, True)
            s2399_procjudtrab_id = resp[0][0]
            #print s2399_procjudtrab_id

    if 'infoMV' in dir(evtTSVTermino.infoTSVTermino.verbasResc):
        for infoMV in evtTSVTermino.infoTSVTermino.verbasResc.infoMV:
            s2399_infomv_dados = {}
            s2399_infomv_dados['s2399_evttsvtermino_id'] = s2399_evttsvtermino_id

            if 'indMV' in dir(infoMV): s2399_infomv_dados['indmv'] = infoMV.indMV.cdata
            insert = create_insert('s2399_infomv', s2399_infomv_dados)
            resp = executar_sql(insert, True)
            s2399_infomv_id = resp[0][0]
            #print s2399_infomv_id

            if 'remunOutrEmpr' in dir(infoMV):
                for remunOutrEmpr in infoMV.remunOutrEmpr:
                    s2399_remunoutrempr_dados = {}
                    s2399_remunoutrempr_dados['s2399_infomv_id'] = s2399_infomv_id

                    if 'tpInsc' in dir(remunOutrEmpr): s2399_remunoutrempr_dados['tpinsc'] = remunOutrEmpr.tpInsc.cdata
                    if 'nrInsc' in dir(remunOutrEmpr): s2399_remunoutrempr_dados['nrinsc'] = remunOutrEmpr.nrInsc.cdata
                    if 'codCateg' in dir(remunOutrEmpr): s2399_remunoutrempr_dados['codcateg'] = remunOutrEmpr.codCateg.cdata
                    if 'vlrRemunOE' in dir(remunOutrEmpr): s2399_remunoutrempr_dados['vlrremunoe'] = remunOutrEmpr.vlrRemunOE.cdata
                    insert = create_insert('s2399_remunoutrempr', s2399_remunoutrempr_dados)
                    resp = executar_sql(insert, True)
                    s2399_remunoutrempr_id = resp[0][0]
                    #print s2399_remunoutrempr_id

    if 'quarentena' in dir(evtTSVTermino.infoTSVTermino):
        for quarentena in evtTSVTermino.infoTSVTermino.quarentena:
            s2399_quarentena_dados = {}
            s2399_quarentena_dados['s2399_evttsvtermino_id'] = s2399_evttsvtermino_id

            if 'dtFimQuar' in dir(quarentena): s2399_quarentena_dados['dtfimquar'] = quarentena.dtFimQuar.cdata
            insert = create_insert('s2399_quarentena', s2399_quarentena_dados)
            resp = executar_sql(insert, True)
            s2399_quarentena_id = resp[0][0]
            #print s2399_quarentena_id

    from emensageriapro.esocial.views.s2399_evttsvtermino_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2399_evttsvtermino_id, 'default')
    return dados