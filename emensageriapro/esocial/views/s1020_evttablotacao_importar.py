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



def read_s1020_evttablotacao_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1020_evttablotacao_obj(doc, status, validar)
    return dados

def read_s1020_evttablotacao(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1020_evttablotacao_obj(doc, status, validar)
    return dados



def read_s1020_evttablotacao_obj(doc, status, validar=False):
    s1020_evttablotacao_dados = {}
    s1020_evttablotacao_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1020_evttablotacao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1020_evttablotacao_dados['identidade'] = doc.eSocial.evtTabLotacao['Id']
    evtTabLotacao = doc.eSocial.evtTabLotacao

    try: s1020_evttablotacao_dados['tpamb'] = evtTabLotacao.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s1020_evttablotacao_dados['procemi'] = evtTabLotacao.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s1020_evttablotacao_dados['verproc'] = evtTabLotacao.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s1020_evttablotacao_dados['tpinsc'] = evtTabLotacao.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s1020_evttablotacao_dados['nrinsc'] = evtTabLotacao.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtTabLotacao.infoLotacao): s1020_evttablotacao_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabLotacao.infoLotacao): s1020_evttablotacao_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabLotacao.infoLotacao): s1020_evttablotacao_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1020_evttablotacao', s1020_evttablotacao_dados)
    resp = executar_sql(insert, True)
    s1020_evttablotacao_id = resp[0][0]
    dados = s1020_evttablotacao_dados
    dados['evento'] = 's1020'
    dados['id'] = s1020_evttablotacao_id
    dados['identidade_evento'] = doc.eSocial.evtTabLotacao['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'inclusao' in dir(evtTabLotacao.infoLotacao) and evtTabLotacao.infoLotacao.inclusao.cdata != '':
        for inclusao in evtTabLotacao.infoLotacao.inclusao:
            s1020_inclusao_dados = {}
            s1020_inclusao_dados['s1020_evttablotacao_id'] = s1020_evttablotacao_id

            try: s1020_inclusao_dados['codlotacao'] = inclusao.ideLotacao.codLotacao.cdata
            except AttributeError: pass
            try: s1020_inclusao_dados['inivalid'] = inclusao.ideLotacao.iniValid.cdata
            except AttributeError: pass
            try: s1020_inclusao_dados['fimvalid'] = inclusao.ideLotacao.fimValid.cdata
            except AttributeError: pass
            try: s1020_inclusao_dados['tplotacao'] = inclusao.dadosLotacao.tpLotacao.cdata
            except AttributeError: pass
            try: s1020_inclusao_dados['tpinsc'] = inclusao.dadosLotacao.tpInsc.cdata
            except AttributeError: pass
            try: s1020_inclusao_dados['nrinsc'] = inclusao.dadosLotacao.nrInsc.cdata
            except AttributeError: pass
            try: s1020_inclusao_dados['fpas'] = inclusao.dadosLotacao.fpasLotacao.fpas.cdata
            except AttributeError: pass
            try: s1020_inclusao_dados['codtercs'] = inclusao.dadosLotacao.fpasLotacao.codTercs.cdata
            except AttributeError: pass
            try: s1020_inclusao_dados['codtercssusp'] = inclusao.dadosLotacao.fpasLotacao.codTercsSusp.cdata
            except AttributeError: pass
            insert = create_insert('s1020_inclusao', s1020_inclusao_dados)
            resp = executar_sql(insert, True)
            s1020_inclusao_id = resp[0][0]
            #print s1020_inclusao_id

            if 'procJudTerceiro' in dir(inclusao.dadosLotacao.fpasLotacao.infoProcJudTerceiros) and inclusao.dadosLotacao.fpasLotacao.infoProcJudTerceiros.procJudTerceiro.cdata != '':
                for procJudTerceiro in inclusao.dadosLotacao.fpasLotacao.infoProcJudTerceiros.procJudTerceiro:
                    s1020_inclusao_procjudterceiro_dados = {}
                    s1020_inclusao_procjudterceiro_dados['s1020_inclusao_id'] = s1020_inclusao_id

                    try: s1020_inclusao_procjudterceiro_dados['codterc'] = procJudTerceiro.codTerc.cdata
                    except AttributeError: pass
                    try: s1020_inclusao_procjudterceiro_dados['nrprocjud'] = procJudTerceiro.nrProcJud.cdata
                    except AttributeError: pass
                    try: s1020_inclusao_procjudterceiro_dados['codsusp'] = procJudTerceiro.codSusp.cdata
                    except AttributeError: pass
                    insert = create_insert('s1020_inclusao_procjudterceiro', s1020_inclusao_procjudterceiro_dados)
                    resp = executar_sql(insert, True)
                    s1020_inclusao_procjudterceiro_id = resp[0][0]
                    #print s1020_inclusao_procjudterceiro_id

            if 'infoEmprParcial' in dir(inclusao.dadosLotacao) and inclusao.dadosLotacao.infoEmprParcial.cdata != '':
                for infoEmprParcial in inclusao.dadosLotacao.infoEmprParcial:
                    s1020_inclusao_infoemprparcial_dados = {}
                    s1020_inclusao_infoemprparcial_dados['s1020_inclusao_id'] = s1020_inclusao_id

                    try: s1020_inclusao_infoemprparcial_dados['tpinsccontrat'] = infoEmprParcial.tpInscContrat.cdata
                    except AttributeError: pass
                    try: s1020_inclusao_infoemprparcial_dados['nrinsccontrat'] = infoEmprParcial.nrInscContrat.cdata
                    except AttributeError: pass
                    try: s1020_inclusao_infoemprparcial_dados['tpinscprop'] = infoEmprParcial.tpInscProp.cdata
                    except AttributeError: pass
                    try: s1020_inclusao_infoemprparcial_dados['nrinscprop'] = infoEmprParcial.nrInscProp.cdata
                    except AttributeError: pass
                    insert = create_insert('s1020_inclusao_infoemprparcial', s1020_inclusao_infoemprparcial_dados)
                    resp = executar_sql(insert, True)
                    s1020_inclusao_infoemprparcial_id = resp[0][0]
                    #print s1020_inclusao_infoemprparcial_id

    if 'alteracao' in dir(evtTabLotacao.infoLotacao) and evtTabLotacao.infoLotacao.alteracao.cdata != '':
        for alteracao in evtTabLotacao.infoLotacao.alteracao:
            s1020_alteracao_dados = {}
            s1020_alteracao_dados['s1020_evttablotacao_id'] = s1020_evttablotacao_id

            try: s1020_alteracao_dados['codlotacao'] = alteracao.ideLotacao.codLotacao.cdata
            except AttributeError: pass
            try: s1020_alteracao_dados['inivalid'] = alteracao.ideLotacao.iniValid.cdata
            except AttributeError: pass
            try: s1020_alteracao_dados['fimvalid'] = alteracao.ideLotacao.fimValid.cdata
            except AttributeError: pass
            try: s1020_alteracao_dados['tplotacao'] = alteracao.dadosLotacao.tpLotacao.cdata
            except AttributeError: pass
            try: s1020_alteracao_dados['tpinsc'] = alteracao.dadosLotacao.tpInsc.cdata
            except AttributeError: pass
            try: s1020_alteracao_dados['nrinsc'] = alteracao.dadosLotacao.nrInsc.cdata
            except AttributeError: pass
            try: s1020_alteracao_dados['fpas'] = alteracao.dadosLotacao.fpasLotacao.fpas.cdata
            except AttributeError: pass
            try: s1020_alteracao_dados['codtercs'] = alteracao.dadosLotacao.fpasLotacao.codTercs.cdata
            except AttributeError: pass
            try: s1020_alteracao_dados['codtercssusp'] = alteracao.dadosLotacao.fpasLotacao.codTercsSusp.cdata
            except AttributeError: pass
            insert = create_insert('s1020_alteracao', s1020_alteracao_dados)
            resp = executar_sql(insert, True)
            s1020_alteracao_id = resp[0][0]
            #print s1020_alteracao_id

            if 'procJudTerceiro' in dir(alteracao.dadosLotacao.fpasLotacao.infoProcJudTerceiros) and alteracao.dadosLotacao.fpasLotacao.infoProcJudTerceiros.procJudTerceiro.cdata != '':
                for procJudTerceiro in alteracao.dadosLotacao.fpasLotacao.infoProcJudTerceiros.procJudTerceiro:
                    s1020_alteracao_procjudterceiro_dados = {}
                    s1020_alteracao_procjudterceiro_dados['s1020_alteracao_id'] = s1020_alteracao_id

                    try: s1020_alteracao_procjudterceiro_dados['codterc'] = procJudTerceiro.codTerc.cdata
                    except AttributeError: pass
                    try: s1020_alteracao_procjudterceiro_dados['nrprocjud'] = procJudTerceiro.nrProcJud.cdata
                    except AttributeError: pass
                    try: s1020_alteracao_procjudterceiro_dados['codsusp'] = procJudTerceiro.codSusp.cdata
                    except AttributeError: pass
                    insert = create_insert('s1020_alteracao_procjudterceiro', s1020_alteracao_procjudterceiro_dados)
                    resp = executar_sql(insert, True)
                    s1020_alteracao_procjudterceiro_id = resp[0][0]
                    #print s1020_alteracao_procjudterceiro_id

            if 'infoEmprParcial' in dir(alteracao.dadosLotacao) and alteracao.dadosLotacao.infoEmprParcial.cdata != '':
                for infoEmprParcial in alteracao.dadosLotacao.infoEmprParcial:
                    s1020_alteracao_infoemprparcial_dados = {}
                    s1020_alteracao_infoemprparcial_dados['s1020_alteracao_id'] = s1020_alteracao_id

                    try: s1020_alteracao_infoemprparcial_dados['tpinsccontrat'] = infoEmprParcial.tpInscContrat.cdata
                    except AttributeError: pass
                    try: s1020_alteracao_infoemprparcial_dados['nrinsccontrat'] = infoEmprParcial.nrInscContrat.cdata
                    except AttributeError: pass
                    try: s1020_alteracao_infoemprparcial_dados['tpinscprop'] = infoEmprParcial.tpInscProp.cdata
                    except AttributeError: pass
                    try: s1020_alteracao_infoemprparcial_dados['nrinscprop'] = infoEmprParcial.nrInscProp.cdata
                    except AttributeError: pass
                    insert = create_insert('s1020_alteracao_infoemprparcial', s1020_alteracao_infoemprparcial_dados)
                    resp = executar_sql(insert, True)
                    s1020_alteracao_infoemprparcial_id = resp[0][0]
                    #print s1020_alteracao_infoemprparcial_id

            if 'novaValidade' in dir(alteracao) and alteracao.novaValidade.cdata != '':
                for novaValidade in alteracao.novaValidade:
                    s1020_alteracao_novavalidade_dados = {}
                    s1020_alteracao_novavalidade_dados['s1020_alteracao_id'] = s1020_alteracao_id

                    try: s1020_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError: pass
                    try: s1020_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError: pass
                    insert = create_insert('s1020_alteracao_novavalidade', s1020_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1020_alteracao_novavalidade_id = resp[0][0]
                    #print s1020_alteracao_novavalidade_id

    if 'exclusao' in dir(evtTabLotacao.infoLotacao) and evtTabLotacao.infoLotacao.exclusao.cdata != '':
        for exclusao in evtTabLotacao.infoLotacao.exclusao:
            s1020_exclusao_dados = {}
            s1020_exclusao_dados['s1020_evttablotacao_id'] = s1020_evttablotacao_id

            try: s1020_exclusao_dados['codlotacao'] = exclusao.ideLotacao.codLotacao.cdata
            except AttributeError: pass
            try: s1020_exclusao_dados['inivalid'] = exclusao.ideLotacao.iniValid.cdata
            except AttributeError: pass
            try: s1020_exclusao_dados['fimvalid'] = exclusao.ideLotacao.fimValid.cdata
            except AttributeError: pass
            insert = create_insert('s1020_exclusao', s1020_exclusao_dados)
            resp = executar_sql(insert, True)
            s1020_exclusao_id = resp[0][0]
            #print s1020_exclusao_id

    from emensageriapro.esocial.views.s1020_evttablotacao_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1020_evttablotacao_id, 'default')
    return dados