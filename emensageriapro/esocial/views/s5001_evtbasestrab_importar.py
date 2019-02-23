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



def read_s5001_evtbasestrab_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s5001_evtbasestrab_obj(doc, status, validar)
    return dados

def read_s5001_evtbasestrab(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s5001_evtbasestrab_obj(doc, status, validar)
    return dados



def read_s5001_evtbasestrab_obj(doc, status, validar=False):
    s5001_evtbasestrab_dados = {}
    s5001_evtbasestrab_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s5001_evtbasestrab_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5001_evtbasestrab_dados['identidade'] = doc.eSocial.evtBasesTrab['Id']
    s5001_evtbasestrab_dados['processamento_codigo_resposta'] = 1
    evtBasesTrab = doc.eSocial.evtBasesTrab

    if 'nrRecArqBase' in dir(evtBasesTrab.ideEvento): s5001_evtbasestrab_dados['nrrecarqbase'] = evtBasesTrab.ideEvento.nrRecArqBase.cdata
    if 'indApuracao' in dir(evtBasesTrab.ideEvento): s5001_evtbasestrab_dados['indapuracao'] = evtBasesTrab.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtBasesTrab.ideEvento): s5001_evtbasestrab_dados['perapur'] = evtBasesTrab.ideEvento.perApur.cdata
    if 'tpInsc' in dir(evtBasesTrab.ideEmpregador): s5001_evtbasestrab_dados['tpinsc'] = evtBasesTrab.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtBasesTrab.ideEmpregador): s5001_evtbasestrab_dados['nrinsc'] = evtBasesTrab.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtBasesTrab.ideTrabalhador): s5001_evtbasestrab_dados['cpftrab'] = evtBasesTrab.ideTrabalhador.cpfTrab.cdata
    if 'inclusao' in dir(evtBasesTrab.infoCp): s5001_evtbasestrab_dados['operacao'] = 1
    elif 'alteracao' in dir(evtBasesTrab.infoCp): s5001_evtbasestrab_dados['operacao'] = 2
    elif 'exclusao' in dir(evtBasesTrab.infoCp): s5001_evtbasestrab_dados['operacao'] = 3
    #print dados
    insert = create_insert('s5001_evtbasestrab', s5001_evtbasestrab_dados)
    resp = executar_sql(insert, True)
    s5001_evtbasestrab_id = resp[0][0]
    dados = s5001_evtbasestrab_dados
    dados['evento'] = 's5001'
    dados['id'] = s5001_evtbasestrab_id
    dados['identidade_evento'] = doc.eSocial.evtBasesTrab['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'procJudTrab' in dir(evtBasesTrab.ideTrabalhador):
        for procJudTrab in evtBasesTrab.ideTrabalhador.procJudTrab:
            s5001_procjudtrab_dados = {}
            s5001_procjudtrab_dados['s5001_evtbasestrab_id'] = s5001_evtbasestrab_id

            if 'nrProcJud' in dir(procJudTrab): s5001_procjudtrab_dados['nrprocjud'] = procJudTrab.nrProcJud.cdata
            if 'codSusp' in dir(procJudTrab): s5001_procjudtrab_dados['codsusp'] = procJudTrab.codSusp.cdata
            insert = create_insert('s5001_procjudtrab', s5001_procjudtrab_dados)
            resp = executar_sql(insert, True)
            s5001_procjudtrab_id = resp[0][0]
            #print s5001_procjudtrab_id

    if 'infoCpCalc' in dir(evtBasesTrab):
        for infoCpCalc in evtBasesTrab.infoCpCalc:
            s5001_infocpcalc_dados = {}
            s5001_infocpcalc_dados['s5001_evtbasestrab_id'] = s5001_evtbasestrab_id

            if 'tpCR' in dir(infoCpCalc): s5001_infocpcalc_dados['tpcr'] = infoCpCalc.tpCR.cdata
            if 'vrCpSeg' in dir(infoCpCalc): s5001_infocpcalc_dados['vrcpseg'] = infoCpCalc.vrCpSeg.cdata
            if 'vrDescSeg' in dir(infoCpCalc): s5001_infocpcalc_dados['vrdescseg'] = infoCpCalc.vrDescSeg.cdata
            insert = create_insert('s5001_infocpcalc', s5001_infocpcalc_dados)
            resp = executar_sql(insert, True)
            s5001_infocpcalc_id = resp[0][0]
            #print s5001_infocpcalc_id

    if 'ideEstabLot' in dir(evtBasesTrab.infoCp):
        for ideEstabLot in evtBasesTrab.infoCp.ideEstabLot:
            s5001_ideestablot_dados = {}
            s5001_ideestablot_dados['s5001_evtbasestrab_id'] = s5001_evtbasestrab_id

            if 'tpInsc' in dir(ideEstabLot): s5001_ideestablot_dados['tpinsc'] = ideEstabLot.tpInsc.cdata
            if 'nrInsc' in dir(ideEstabLot): s5001_ideestablot_dados['nrinsc'] = ideEstabLot.nrInsc.cdata
            if 'codLotacao' in dir(ideEstabLot): s5001_ideestablot_dados['codlotacao'] = ideEstabLot.codLotacao.cdata
            insert = create_insert('s5001_ideestablot', s5001_ideestablot_dados)
            resp = executar_sql(insert, True)
            s5001_ideestablot_id = resp[0][0]
            #print s5001_ideestablot_id

            if 'infoCategIncid' in dir(ideEstabLot):
                for infoCategIncid in ideEstabLot.infoCategIncid:
                    s5001_infocategincid_dados = {}
                    s5001_infocategincid_dados['s5001_ideestablot_id'] = s5001_ideestablot_id

                    if 'matricula' in dir(infoCategIncid): s5001_infocategincid_dados['matricula'] = infoCategIncid.matricula.cdata
                    if 'codCateg' in dir(infoCategIncid): s5001_infocategincid_dados['codcateg'] = infoCategIncid.codCateg.cdata
                    if 'indSimples' in dir(infoCategIncid): s5001_infocategincid_dados['indsimples'] = infoCategIncid.indSimples.cdata
                    insert = create_insert('s5001_infocategincid', s5001_infocategincid_dados)
                    resp = executar_sql(insert, True)
                    s5001_infocategincid_id = resp[0][0]
                    #print s5001_infocategincid_id

    from emensageriapro.esocial.views.s5001_evtbasestrab_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s5001_evtbasestrab_id, 'default')
    return dados