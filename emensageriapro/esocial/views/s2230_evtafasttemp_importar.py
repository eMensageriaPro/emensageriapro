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



def read_s2230_evtafasttemp_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2230_evtafasttemp_obj(doc, status, validar)
    return dados

def read_s2230_evtafasttemp(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2230_evtafasttemp_obj(doc, status, validar)
    return dados



def read_s2230_evtafasttemp_obj(doc, status, validar=False):
    s2230_evtafasttemp_dados = {}
    s2230_evtafasttemp_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2230_evtafasttemp_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2230_evtafasttemp_dados['identidade'] = doc.eSocial.evtAfastTemp['Id']
    evtAfastTemp = doc.eSocial.evtAfastTemp

    try: s2230_evtafasttemp_dados['indretif'] = evtAfastTemp.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s2230_evtafasttemp_dados['nrrecibo'] = evtAfastTemp.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s2230_evtafasttemp_dados['tpamb'] = evtAfastTemp.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s2230_evtafasttemp_dados['procemi'] = evtAfastTemp.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s2230_evtafasttemp_dados['verproc'] = evtAfastTemp.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s2230_evtafasttemp_dados['tpinsc'] = evtAfastTemp.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s2230_evtafasttemp_dados['nrinsc'] = evtAfastTemp.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s2230_evtafasttemp_dados['cpftrab'] = evtAfastTemp.ideVinculo.cpfTrab.cdata
    except AttributeError: pass
    try: s2230_evtafasttemp_dados['nistrab'] = evtAfastTemp.ideVinculo.nisTrab.cdata
    except AttributeError: pass
    try: s2230_evtafasttemp_dados['matricula'] = evtAfastTemp.ideVinculo.matricula.cdata
    except AttributeError: pass
    try: s2230_evtafasttemp_dados['codcateg'] = evtAfastTemp.ideVinculo.codCateg.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtAfastTemp.infoAfastamento): s2230_evtafasttemp_dados['operacao'] = 1
    elif 'alteracao' in dir(evtAfastTemp.infoAfastamento): s2230_evtafasttemp_dados['operacao'] = 2
    elif 'exclusao' in dir(evtAfastTemp.infoAfastamento): s2230_evtafasttemp_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2230_evtafasttemp', s2230_evtafasttemp_dados)
    resp = executar_sql(insert, True)
    s2230_evtafasttemp_id = resp[0][0]
    dados = s2230_evtafasttemp_dados
    dados['evento'] = 's2230'
    dados['id'] = s2230_evtafasttemp_id
    dados['identidade_evento'] = doc.eSocial.evtAfastTemp['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'iniAfastamento' in dir(evtAfastTemp.infoAfastamento) and evtAfastTemp.infoAfastamento.iniAfastamento.cdata != '':
        for iniAfastamento in evtAfastTemp.infoAfastamento.iniAfastamento:
            s2230_iniafastamento_dados = {}
            s2230_iniafastamento_dados['s2230_evtafasttemp_id'] = s2230_evtafasttemp_id

            try: s2230_iniafastamento_dados['dtiniafast'] = iniAfastamento.dtIniAfast.cdata
            except AttributeError: pass
            try: s2230_iniafastamento_dados['codmotafast'] = iniAfastamento.codMotAfast.cdata
            except AttributeError: pass
            try: s2230_iniafastamento_dados['infomesmomtv'] = iniAfastamento.infoMesmoMtv.cdata
            except AttributeError: pass
            try: s2230_iniafastamento_dados['tpacidtransito'] = iniAfastamento.tpAcidTransito.cdata
            except AttributeError: pass
            try: s2230_iniafastamento_dados['observacao'] = iniAfastamento.observacao.cdata
            except AttributeError: pass
            insert = create_insert('s2230_iniafastamento', s2230_iniafastamento_dados)
            resp = executar_sql(insert, True)
            s2230_iniafastamento_id = resp[0][0]
            #print s2230_iniafastamento_id

            if 'infoAtestado' in dir(iniAfastamento) and iniAfastamento.infoAtestado.cdata != '':
                for infoAtestado in iniAfastamento.infoAtestado:
                    s2230_infoatestado_dados = {}
                    s2230_infoatestado_dados['s2230_iniafastamento_id'] = s2230_iniafastamento_id

                    try: s2230_infoatestado_dados['codcid'] = infoAtestado.codCID.cdata
                    except AttributeError: pass
                    try: s2230_infoatestado_dados['qtddiasafast'] = infoAtestado.qtdDiasAfast.cdata
                    except AttributeError: pass
                    insert = create_insert('s2230_infoatestado', s2230_infoatestado_dados)
                    resp = executar_sql(insert, True)
                    s2230_infoatestado_id = resp[0][0]
                    #print s2230_infoatestado_id

            if 'infoCessao' in dir(iniAfastamento) and iniAfastamento.infoCessao.cdata != '':
                for infoCessao in iniAfastamento.infoCessao:
                    s2230_infocessao_dados = {}
                    s2230_infocessao_dados['s2230_iniafastamento_id'] = s2230_iniafastamento_id

                    try: s2230_infocessao_dados['cnpjcess'] = infoCessao.cnpjCess.cdata
                    except AttributeError: pass
                    try: s2230_infocessao_dados['infonus'] = infoCessao.infOnus.cdata
                    except AttributeError: pass
                    insert = create_insert('s2230_infocessao', s2230_infocessao_dados)
                    resp = executar_sql(insert, True)
                    s2230_infocessao_id = resp[0][0]
                    #print s2230_infocessao_id

            if 'infoMandSind' in dir(iniAfastamento) and iniAfastamento.infoMandSind.cdata != '':
                for infoMandSind in iniAfastamento.infoMandSind:
                    s2230_infomandsind_dados = {}
                    s2230_infomandsind_dados['s2230_iniafastamento_id'] = s2230_iniafastamento_id

                    try: s2230_infomandsind_dados['cnpjsind'] = infoMandSind.cnpjSind.cdata
                    except AttributeError: pass
                    try: s2230_infomandsind_dados['infonusremun'] = infoMandSind.infOnusRemun.cdata
                    except AttributeError: pass
                    insert = create_insert('s2230_infomandsind', s2230_infomandsind_dados)
                    resp = executar_sql(insert, True)
                    s2230_infomandsind_id = resp[0][0]
                    #print s2230_infomandsind_id

    if 'infoRetif' in dir(evtAfastTemp.infoAfastamento) and evtAfastTemp.infoAfastamento.infoRetif.cdata != '':
        for infoRetif in evtAfastTemp.infoAfastamento.infoRetif:
            s2230_inforetif_dados = {}
            s2230_inforetif_dados['s2230_evtafasttemp_id'] = s2230_evtafasttemp_id

            try: s2230_inforetif_dados['origretif'] = infoRetif.origRetif.cdata
            except AttributeError: pass
            try: s2230_inforetif_dados['tpproc'] = infoRetif.tpProc.cdata
            except AttributeError: pass
            try: s2230_inforetif_dados['nrproc'] = infoRetif.nrProc.cdata
            except AttributeError: pass
            insert = create_insert('s2230_inforetif', s2230_inforetif_dados)
            resp = executar_sql(insert, True)
            s2230_inforetif_id = resp[0][0]
            #print s2230_inforetif_id

    if 'fimAfastamento' in dir(evtAfastTemp.infoAfastamento) and evtAfastTemp.infoAfastamento.fimAfastamento.cdata != '':
        for fimAfastamento in evtAfastTemp.infoAfastamento.fimAfastamento:
            s2230_fimafastamento_dados = {}
            s2230_fimafastamento_dados['s2230_evtafasttemp_id'] = s2230_evtafasttemp_id

            try: s2230_fimafastamento_dados['dttermafast'] = fimAfastamento.dtTermAfast.cdata
            except AttributeError: pass
            insert = create_insert('s2230_fimafastamento', s2230_fimafastamento_dados)
            resp = executar_sql(insert, True)
            s2230_fimafastamento_id = resp[0][0]
            #print s2230_fimafastamento_id

    from emensageriapro.esocial.views.s2230_evtafasttemp_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2230_evtafasttemp_id, 'default')
    return dados