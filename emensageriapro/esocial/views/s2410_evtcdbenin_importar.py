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


def read_s2410_evtcdbenin_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2410_evtcdbenin_obj(doc, status, validar)
    return dados

def read_s2410_evtcdbenin(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2410_evtcdbenin_obj(doc, status, validar)
    return dados



def read_s2410_evtcdbenin_obj(doc, status, validar=False):
    s2410_evtcdbenin_dados = {}
    s2410_evtcdbenin_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2410_evtcdbenin_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2410_evtcdbenin_dados['identidade'] = doc.eSocial.evtCdBenIn['Id']
    s2410_evtcdbenin_dados['processamento_codigo_resposta'] = 1
    evtCdBenIn = doc.eSocial.evtCdBenIn

    if 'indRetif' in dir(evtCdBenIn.ideEvento): s2410_evtcdbenin_dados['indretif'] = evtCdBenIn.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtCdBenIn.ideEvento): s2410_evtcdbenin_dados['nrrecibo'] = evtCdBenIn.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtCdBenIn.ideEvento): s2410_evtcdbenin_dados['tpamb'] = evtCdBenIn.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtCdBenIn.ideEvento): s2410_evtcdbenin_dados['procemi'] = evtCdBenIn.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtCdBenIn.ideEvento): s2410_evtcdbenin_dados['verproc'] = evtCdBenIn.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtCdBenIn.ideEmpregador): s2410_evtcdbenin_dados['tpinsc'] = evtCdBenIn.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtCdBenIn.ideEmpregador): s2410_evtcdbenin_dados['nrinsc'] = evtCdBenIn.ideEmpregador.nrInsc.cdata
    if 'cpfBenef' in dir(evtCdBenIn.beneficiario): s2410_evtcdbenin_dados['cpfbenef'] = evtCdBenIn.beneficiario.cpfBenef.cdata
    if 'matricula' in dir(evtCdBenIn.beneficiario): s2410_evtcdbenin_dados['matricula'] = evtCdBenIn.beneficiario.matricula.cdata
    if 'cnpjOrigem' in dir(evtCdBenIn.beneficiario): s2410_evtcdbenin_dados['cnpjorigem'] = evtCdBenIn.beneficiario.cnpjOrigem.cdata
    if 'cadIni' in dir(evtCdBenIn.infoBenInicio): s2410_evtcdbenin_dados['cadini'] = evtCdBenIn.infoBenInicio.cadIni.cdata
    if 'nrBeneficio' in dir(evtCdBenIn.infoBenInicio): s2410_evtcdbenin_dados['nrbeneficio'] = evtCdBenIn.infoBenInicio.nrBeneficio.cdata
    if 'dtIniBeneficio' in dir(evtCdBenIn.infoBenInicio): s2410_evtcdbenin_dados['dtinibeneficio'] = evtCdBenIn.infoBenInicio.dtIniBeneficio.cdata
    if 'tpBeneficio' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio): s2410_evtcdbenin_dados['tpbeneficio'] = evtCdBenIn.infoBenInicio.dadosBeneficio.tpBeneficio.cdata
    if 'vrBeneficio' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio): s2410_evtcdbenin_dados['vrbeneficio'] = evtCdBenIn.infoBenInicio.dadosBeneficio.vrBeneficio.cdata
    if 'tpPlanRP' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio): s2410_evtcdbenin_dados['tpplanrp'] = evtCdBenIn.infoBenInicio.dadosBeneficio.tpPlanRP.cdata
    if 'dsc' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio): s2410_evtcdbenin_dados['dsc'] = evtCdBenIn.infoBenInicio.dadosBeneficio.dsc.cdata
    if 'indDecJud' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio): s2410_evtcdbenin_dados['inddecjud'] = evtCdBenIn.infoBenInicio.dadosBeneficio.indDecJud.cdata
    if 'indHomologTC' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio): s2410_evtcdbenin_dados['indhomologtc'] = evtCdBenIn.infoBenInicio.dadosBeneficio.indHomologTC.cdata
    if 'inclusao' in dir(evtCdBenIn.infoBenInicio): s2410_evtcdbenin_dados['operacao'] = 1
    elif 'alteracao' in dir(evtCdBenIn.infoBenInicio): s2410_evtcdbenin_dados['operacao'] = 2
    elif 'exclusao' in dir(evtCdBenIn.infoBenInicio): s2410_evtcdbenin_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2410_evtcdbenin', s2410_evtcdbenin_dados)
    resp = executar_sql(insert, True)
    s2410_evtcdbenin_id = resp[0][0]
    dados = s2410_evtcdbenin_dados
    dados['evento'] = 's2410'
    dados['id'] = s2410_evtcdbenin_id
    dados['identidade_evento'] = doc.eSocial.evtCdBenIn['Id']
    dados['status'] = 1

    if 'infoPenMorte' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio):
        for infoPenMorte in evtCdBenIn.infoBenInicio.dadosBeneficio.infoPenMorte:
            s2410_infopenmorte_dados = {}
            s2410_infopenmorte_dados['s2410_evtcdbenin_id'] = s2410_evtcdbenin_id

            if 'tpPenMorte' in dir(infoPenMorte): s2410_infopenmorte_dados['tppenmorte'] = infoPenMorte.tpPenMorte.cdata
            insert = create_insert('s2410_infopenmorte', s2410_infopenmorte_dados)
            resp = executar_sql(insert, True)
            s2410_infopenmorte_id = resp[0][0]
            #print s2410_infopenmorte_id

            if 'instPenMorte' in dir(infoPenMorte):
                for instPenMorte in infoPenMorte.instPenMorte:
                    s2410_instpenmorte_dados = {}
                    s2410_instpenmorte_dados['s2410_infopenmorte_id'] = s2410_infopenmorte_id

                    if 'cpfInst' in dir(instPenMorte): s2410_instpenmorte_dados['cpfinst'] = instPenMorte.cpfInst.cdata
                    if 'dtInst' in dir(instPenMorte): s2410_instpenmorte_dados['dtinst'] = instPenMorte.dtInst.cdata
                    if 'intAposentado' in dir(instPenMorte): s2410_instpenmorte_dados['intaposentado'] = instPenMorte.intAposentado.cdata
                    insert = create_insert('s2410_instpenmorte', s2410_instpenmorte_dados)
                    resp = executar_sql(insert, True)
                    s2410_instpenmorte_id = resp[0][0]
                    #print s2410_instpenmorte_id

    if 'homologTC' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio):
        for homologTC in evtCdBenIn.infoBenInicio.dadosBeneficio.homologTC:
            s2410_homologtc_dados = {}
            s2410_homologtc_dados['s2410_evtcdbenin_id'] = s2410_evtcdbenin_id

            if 'dtHomol' in dir(homologTC): s2410_homologtc_dados['dthomol'] = homologTC.dtHomol.cdata
            if 'nrAtoLegal' in dir(homologTC): s2410_homologtc_dados['nratolegal'] = homologTC.nrAtoLegal.cdata
            insert = create_insert('s2410_homologtc', s2410_homologtc_dados)
            resp = executar_sql(insert, True)
            s2410_homologtc_id = resp[0][0]
            #print s2410_homologtc_id

    from emensageriapro.esocial.views.s2410_evtcdbenin_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2410_evtcdbenin_id, 'default')
    return dados