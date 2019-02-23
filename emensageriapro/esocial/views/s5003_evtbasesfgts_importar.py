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



def read_s5003_evtbasesfgts_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s5003_evtbasesfgts_obj(doc, status, validar)
    return dados

def read_s5003_evtbasesfgts(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s5003_evtbasesfgts_obj(doc, status, validar)
    return dados



def read_s5003_evtbasesfgts_obj(doc, status, validar=False):
    s5003_evtbasesfgts_dados = {}
    s5003_evtbasesfgts_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s5003_evtbasesfgts_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5003_evtbasesfgts_dados['identidade'] = doc.eSocial.evtBasesFGTS['Id']
    s5003_evtbasesfgts_dados['processamento_codigo_resposta'] = 1
    evtBasesFGTS = doc.eSocial.evtBasesFGTS

    if 'nrRecArqBase' in dir(evtBasesFGTS.ideEvento): s5003_evtbasesfgts_dados['nrrecarqbase'] = evtBasesFGTS.ideEvento.nrRecArqBase.cdata
    if 'perApur' in dir(evtBasesFGTS.ideEvento): s5003_evtbasesfgts_dados['perapur'] = evtBasesFGTS.ideEvento.perApur.cdata
    if 'tpInsc' in dir(evtBasesFGTS.ideEmpregador): s5003_evtbasesfgts_dados['tpinsc'] = evtBasesFGTS.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtBasesFGTS.ideEmpregador): s5003_evtbasesfgts_dados['nrinsc'] = evtBasesFGTS.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtBasesFGTS.ideTrabalhador): s5003_evtbasesfgts_dados['cpftrab'] = evtBasesFGTS.ideTrabalhador.cpfTrab.cdata
    if 'nisTrab' in dir(evtBasesFGTS.ideTrabalhador): s5003_evtbasesfgts_dados['nistrab'] = evtBasesFGTS.ideTrabalhador.nisTrab.cdata
    if 'inclusao' in dir(evtBasesFGTS.infoFGTS): s5003_evtbasesfgts_dados['operacao'] = 1
    elif 'alteracao' in dir(evtBasesFGTS.infoFGTS): s5003_evtbasesfgts_dados['operacao'] = 2
    elif 'exclusao' in dir(evtBasesFGTS.infoFGTS): s5003_evtbasesfgts_dados['operacao'] = 3
    #print dados
    insert = create_insert('s5003_evtbasesfgts', s5003_evtbasesfgts_dados)
    resp = executar_sql(insert, True)
    s5003_evtbasesfgts_id = resp[0][0]
    dados = s5003_evtbasesfgts_dados
    dados['evento'] = 's5003'
    dados['id'] = s5003_evtbasesfgts_id
    dados['identidade_evento'] = doc.eSocial.evtBasesFGTS['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'infoFGTS' in dir(evtBasesFGTS):
        for infoFGTS in evtBasesFGTS.infoFGTS:
            s5003_infofgts_dados = {}
            s5003_infofgts_dados['s5003_evtbasesfgts_id'] = s5003_evtbasesfgts_id

            if 'dtVenc' in dir(infoFGTS): s5003_infofgts_dados['dtvenc'] = infoFGTS.dtVenc.cdata
            insert = create_insert('s5003_infofgts', s5003_infofgts_dados)
            resp = executar_sql(insert, True)
            s5003_infofgts_id = resp[0][0]
            #print s5003_infofgts_id

            if 'ideEstabLot' in dir(infoFGTS):
                for ideEstabLot in infoFGTS.ideEstabLot:
                    s5003_ideestablot_dados = {}
                    s5003_ideestablot_dados['s5003_infofgts_id'] = s5003_infofgts_id

                    if 'tpInsc' in dir(ideEstabLot): s5003_ideestablot_dados['tpinsc'] = ideEstabLot.tpInsc.cdata
                    if 'nrInsc' in dir(ideEstabLot): s5003_ideestablot_dados['nrinsc'] = ideEstabLot.nrInsc.cdata
                    if 'codLotacao' in dir(ideEstabLot): s5003_ideestablot_dados['codlotacao'] = ideEstabLot.codLotacao.cdata
                    insert = create_insert('s5003_ideestablot', s5003_ideestablot_dados)
                    resp = executar_sql(insert, True)
                    s5003_ideestablot_id = resp[0][0]
                    #print s5003_ideestablot_id

            if 'infoTrabDps' in dir(infoFGTS.infoDpsFGTS):
                for infoTrabDps in infoFGTS.infoDpsFGTS.infoTrabDps:
                    s5003_infotrabdps_dados = {}
                    s5003_infotrabdps_dados['s5003_infofgts_id'] = s5003_infofgts_id

                    if 'matricula' in dir(infoTrabDps): s5003_infotrabdps_dados['matricula'] = infoTrabDps.matricula.cdata
                    if 'codCateg' in dir(infoTrabDps): s5003_infotrabdps_dados['codcateg'] = infoTrabDps.codCateg.cdata
                    insert = create_insert('s5003_infotrabdps', s5003_infotrabdps_dados)
                    resp = executar_sql(insert, True)
                    s5003_infotrabdps_id = resp[0][0]
                    #print s5003_infotrabdps_id

    from emensageriapro.esocial.views.s5003_evtbasesfgts_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s5003_evtbasesfgts_id, 'default')
    return dados