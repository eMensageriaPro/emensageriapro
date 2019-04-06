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



def read_s1202_evtrmnrpps_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1202_evtrmnrpps_obj(doc, status, validar)
    return dados

def read_s1202_evtrmnrpps(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1202_evtrmnrpps_obj(doc, status, validar)
    return dados



def read_s1202_evtrmnrpps_obj(doc, status, validar=False):
    s1202_evtrmnrpps_dados = {}
    s1202_evtrmnrpps_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1202_evtrmnrpps_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1202_evtrmnrpps_dados['identidade'] = doc.eSocial.evtRmnRPPS['Id']
    evtRmnRPPS = doc.eSocial.evtRmnRPPS

    try: s1202_evtrmnrpps_dados['indretif'] = evtRmnRPPS.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s1202_evtrmnrpps_dados['nrrecibo'] = evtRmnRPPS.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s1202_evtrmnrpps_dados['indapuracao'] = evtRmnRPPS.ideEvento.indApuracao.cdata
    except AttributeError: pass
    try: s1202_evtrmnrpps_dados['perapur'] = evtRmnRPPS.ideEvento.perApur.cdata
    except AttributeError: pass
    try: s1202_evtrmnrpps_dados['tpamb'] = evtRmnRPPS.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s1202_evtrmnrpps_dados['procemi'] = evtRmnRPPS.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s1202_evtrmnrpps_dados['verproc'] = evtRmnRPPS.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s1202_evtrmnrpps_dados['tpinsc'] = evtRmnRPPS.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s1202_evtrmnrpps_dados['nrinsc'] = evtRmnRPPS.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s1202_evtrmnrpps_dados['cpftrab'] = evtRmnRPPS.ideTrabalhador.cpfTrab.cdata
    except AttributeError: pass
    try: s1202_evtrmnrpps_dados['nistrab'] = evtRmnRPPS.ideTrabalhador.nisTrab.cdata
    except AttributeError: pass
    try: s1202_evtrmnrpps_dados['qtddepfp'] = evtRmnRPPS.ideTrabalhador.qtdDepFP.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtRmnRPPS.dmDev): s1202_evtrmnrpps_dados['operacao'] = 1
    elif 'alteracao' in dir(evtRmnRPPS.dmDev): s1202_evtrmnrpps_dados['operacao'] = 2
    elif 'exclusao' in dir(evtRmnRPPS.dmDev): s1202_evtrmnrpps_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1202_evtrmnrpps', s1202_evtrmnrpps_dados)
    resp = executar_sql(insert, True)
    s1202_evtrmnrpps_id = resp[0][0]
    dados = s1202_evtrmnrpps_dados
    dados['evento'] = 's1202'
    dados['id'] = s1202_evtrmnrpps_id
    dados['identidade_evento'] = doc.eSocial.evtRmnRPPS['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'procJudTrab' in dir(evtRmnRPPS.ideTrabalhador) and evtRmnRPPS.ideTrabalhador.procJudTrab.cdata != '':
        for procJudTrab in evtRmnRPPS.ideTrabalhador.procJudTrab:
            s1202_procjudtrab_dados = {}
            s1202_procjudtrab_dados['s1202_evtrmnrpps_id'] = s1202_evtrmnrpps_id

            try: s1202_procjudtrab_dados['tptrib'] = procJudTrab.tpTrib.cdata
            except AttributeError: pass
            try: s1202_procjudtrab_dados['nrprocjud'] = procJudTrab.nrProcJud.cdata
            except AttributeError: pass
            try: s1202_procjudtrab_dados['codsusp'] = procJudTrab.codSusp.cdata
            except AttributeError: pass
            insert = create_insert('s1202_procjudtrab', s1202_procjudtrab_dados)
            resp = executar_sql(insert, True)
            s1202_procjudtrab_id = resp[0][0]
            #print s1202_procjudtrab_id

    if 'dmDev' in dir(evtRmnRPPS) and evtRmnRPPS.dmDev.cdata != '':
        for dmDev in evtRmnRPPS.dmDev:
            s1202_dmdev_dados = {}
            s1202_dmdev_dados['s1202_evtrmnrpps_id'] = s1202_evtrmnrpps_id

            try: s1202_dmdev_dados['idedmdev'] = dmDev.ideDmDev.cdata
            except AttributeError: pass
            try: s1202_dmdev_dados['codcateg'] = dmDev.codCateg.cdata
            except AttributeError: pass
            insert = create_insert('s1202_dmdev', s1202_dmdev_dados)
            resp = executar_sql(insert, True)
            s1202_dmdev_id = resp[0][0]
            #print s1202_dmdev_id

            if 'ideEstab' in dir(dmDev.infoPerApur) and dmDev.infoPerApur.ideEstab.cdata != '':
                for ideEstab in dmDev.infoPerApur.ideEstab:
                    s1202_infoperapur_ideestab_dados = {}
                    s1202_infoperapur_ideestab_dados['s1202_dmdev_id'] = s1202_dmdev_id

                    try: s1202_infoperapur_ideestab_dados['tpinsc'] = ideEstab.tpInsc.cdata
                    except AttributeError: pass
                    try: s1202_infoperapur_ideestab_dados['nrinsc'] = ideEstab.nrInsc.cdata
                    except AttributeError: pass
                    insert = create_insert('s1202_infoperapur_ideestab', s1202_infoperapur_ideestab_dados)
                    resp = executar_sql(insert, True)
                    s1202_infoperapur_ideestab_id = resp[0][0]
                    #print s1202_infoperapur_ideestab_id

            if 'ideADC' in dir(dmDev.infoPerAnt) and dmDev.infoPerAnt.ideADC.cdata != '':
                for ideADC in dmDev.infoPerAnt.ideADC:
                    s1202_infoperant_ideadc_dados = {}
                    s1202_infoperant_ideadc_dados['s1202_dmdev_id'] = s1202_dmdev_id

                    try: s1202_infoperant_ideadc_dados['dtlei'] = ideADC.dtLei.cdata
                    except AttributeError: pass
                    try: s1202_infoperant_ideadc_dados['nrlei'] = ideADC.nrLei.cdata
                    except AttributeError: pass
                    try: s1202_infoperant_ideadc_dados['dtef'] = ideADC.dtEf.cdata
                    except AttributeError: pass
                    try: s1202_infoperant_ideadc_dados['dtacconv'] = ideADC.dtAcConv.cdata
                    except AttributeError: pass
                    try: s1202_infoperant_ideadc_dados['tpacconv'] = ideADC.tpAcConv.cdata
                    except AttributeError: pass
                    try: s1202_infoperant_ideadc_dados['compacconv'] = ideADC.compAcConv.cdata
                    except AttributeError: pass
                    try: s1202_infoperant_ideadc_dados['dtefacconv'] = ideADC.dtEfAcConv.cdata
                    except AttributeError: pass
                    try: s1202_infoperant_ideadc_dados['dsc'] = ideADC.dsc.cdata
                    except AttributeError: pass
                    insert = create_insert('s1202_infoperant_ideadc', s1202_infoperant_ideadc_dados)
                    resp = executar_sql(insert, True)
                    s1202_infoperant_ideadc_id = resp[0][0]
                    #print s1202_infoperant_ideadc_id

    from emensageriapro.esocial.views.s1202_evtrmnrpps_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1202_evtrmnrpps_id, 'default')
    return dados