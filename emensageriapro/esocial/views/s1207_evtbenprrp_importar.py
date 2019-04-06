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



def read_s1207_evtbenprrp_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1207_evtbenprrp_obj(doc, status, validar)
    return dados

def read_s1207_evtbenprrp(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1207_evtbenprrp_obj(doc, status, validar)
    return dados



def read_s1207_evtbenprrp_obj(doc, status, validar=False):
    s1207_evtbenprrp_dados = {}
    s1207_evtbenprrp_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1207_evtbenprrp_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1207_evtbenprrp_dados['identidade'] = doc.eSocial.evtBenPrRP['Id']
    evtBenPrRP = doc.eSocial.evtBenPrRP

    try: s1207_evtbenprrp_dados['indretif'] = evtBenPrRP.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s1207_evtbenprrp_dados['nrrecibo'] = evtBenPrRP.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s1207_evtbenprrp_dados['indapuracao'] = evtBenPrRP.ideEvento.indApuracao.cdata
    except AttributeError: pass
    try: s1207_evtbenprrp_dados['perapur'] = evtBenPrRP.ideEvento.perApur.cdata
    except AttributeError: pass
    try: s1207_evtbenprrp_dados['tpamb'] = evtBenPrRP.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s1207_evtbenprrp_dados['procemi'] = evtBenPrRP.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s1207_evtbenprrp_dados['verproc'] = evtBenPrRP.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s1207_evtbenprrp_dados['tpinsc'] = evtBenPrRP.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s1207_evtbenprrp_dados['nrinsc'] = evtBenPrRP.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s1207_evtbenprrp_dados['cpfbenef'] = evtBenPrRP.ideBenef.cpfBenef.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtBenPrRP.dmDev): s1207_evtbenprrp_dados['operacao'] = 1
    elif 'alteracao' in dir(evtBenPrRP.dmDev): s1207_evtbenprrp_dados['operacao'] = 2
    elif 'exclusao' in dir(evtBenPrRP.dmDev): s1207_evtbenprrp_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1207_evtbenprrp', s1207_evtbenprrp_dados)
    resp = executar_sql(insert, True)
    s1207_evtbenprrp_id = resp[0][0]
    dados = s1207_evtbenprrp_dados
    dados['evento'] = 's1207'
    dados['id'] = s1207_evtbenprrp_id
    dados['identidade_evento'] = doc.eSocial.evtBenPrRP['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'procJudTrab' in dir(evtBenPrRP.ideBenef) and evtBenPrRP.ideBenef.procJudTrab.cdata != '':
        for procJudTrab in evtBenPrRP.ideBenef.procJudTrab:
            s1207_procjudtrab_dados = {}
            s1207_procjudtrab_dados['s1207_evtbenprrp_id'] = s1207_evtbenprrp_id

            try: s1207_procjudtrab_dados['tptrib'] = procJudTrab.tpTrib.cdata
            except AttributeError: pass
            try: s1207_procjudtrab_dados['nrprocjud'] = procJudTrab.nrProcJud.cdata
            except AttributeError: pass
            try: s1207_procjudtrab_dados['codsusp'] = procJudTrab.codSusp.cdata
            except AttributeError: pass
            insert = create_insert('s1207_procjudtrab', s1207_procjudtrab_dados)
            resp = executar_sql(insert, True)
            s1207_procjudtrab_id = resp[0][0]
            #print s1207_procjudtrab_id

    if 'dmDev' in dir(evtBenPrRP) and evtBenPrRP.dmDev.cdata != '':
        for dmDev in evtBenPrRP.dmDev:
            s1207_dmdev_dados = {}
            s1207_dmdev_dados['s1207_evtbenprrp_id'] = s1207_evtbenprrp_id

            try: s1207_dmdev_dados['tpbenef'] = dmDev.tpBenef.cdata
            except AttributeError: pass
            try: s1207_dmdev_dados['nrbenefic'] = dmDev.nrBenefic.cdata
            except AttributeError: pass
            try: s1207_dmdev_dados['idedmdev'] = dmDev.ideDmDev.cdata
            except AttributeError: pass
            insert = create_insert('s1207_dmdev', s1207_dmdev_dados)
            resp = executar_sql(insert, True)
            s1207_dmdev_id = resp[0][0]
            #print s1207_dmdev_id

            if 'itens' in dir(dmDev) and dmDev.itens.cdata != '':
                for itens in dmDev.itens:
                    s1207_itens_dados = {}
                    s1207_itens_dados['s1207_dmdev_id'] = s1207_dmdev_id

                    try: s1207_itens_dados['codrubr'] = itens.codRubr.cdata
                    except AttributeError: pass
                    try: s1207_itens_dados['idetabrubr'] = itens.ideTabRubr.cdata
                    except AttributeError: pass
                    try: s1207_itens_dados['vrrubr'] = itens.vrRubr.cdata
                    except AttributeError: pass
                    insert = create_insert('s1207_itens', s1207_itens_dados)
                    resp = executar_sql(insert, True)
                    s1207_itens_id = resp[0][0]
                    #print s1207_itens_id

            if 'ideEstab' in dir(dmDev.infoPerApur) and dmDev.infoPerApur.ideEstab.cdata != '':
                for ideEstab in dmDev.infoPerApur.ideEstab:
                    s1207_infoperapur_ideestab_dados = {}
                    s1207_infoperapur_ideestab_dados['s1207_dmdev_id'] = s1207_dmdev_id

                    try: s1207_infoperapur_ideestab_dados['tpinsc'] = ideEstab.tpInsc.cdata
                    except AttributeError: pass
                    try: s1207_infoperapur_ideestab_dados['nrinsc'] = ideEstab.nrInsc.cdata
                    except AttributeError: pass
                    insert = create_insert('s1207_infoperapur_ideestab', s1207_infoperapur_ideestab_dados)
                    resp = executar_sql(insert, True)
                    s1207_infoperapur_ideestab_id = resp[0][0]
                    #print s1207_infoperapur_ideestab_id

            if 'ideADC' in dir(dmDev.infoPerAnt) and dmDev.infoPerAnt.ideADC.cdata != '':
                for ideADC in dmDev.infoPerAnt.ideADC:
                    s1207_infoperant_ideadc_dados = {}
                    s1207_infoperant_ideadc_dados['s1207_dmdev_id'] = s1207_dmdev_id

                    try: s1207_infoperant_ideadc_dados['dtacconv'] = ideADC.dtAcConv.cdata
                    except AttributeError: pass
                    try: s1207_infoperant_ideadc_dados['tpacconv'] = ideADC.tpAcConv.cdata
                    except AttributeError: pass
                    try: s1207_infoperant_ideadc_dados['compacconv'] = ideADC.compAcConv.cdata
                    except AttributeError: pass
                    try: s1207_infoperant_ideadc_dados['dtefacconv'] = ideADC.dtEfAcConv.cdata
                    except AttributeError: pass
                    try: s1207_infoperant_ideadc_dados['dsc'] = ideADC.dsc.cdata
                    except AttributeError: pass
                    insert = create_insert('s1207_infoperant_ideadc', s1207_infoperant_ideadc_dados)
                    resp = executar_sql(insert, True)
                    s1207_infoperant_ideadc_id = resp[0][0]
                    #print s1207_infoperant_ideadc_id

    from emensageriapro.esocial.views.s1207_evtbenprrp_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1207_evtbenprrp_id, 'default')
    return dados