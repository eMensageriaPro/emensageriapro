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



def read_s1070_evttabprocesso_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1070_evttabprocesso_obj(doc, status, validar)
    return dados

def read_s1070_evttabprocesso(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1070_evttabprocesso_obj(doc, status, validar)
    return dados



def read_s1070_evttabprocesso_obj(doc, status, validar=False):
    s1070_evttabprocesso_dados = {}
    s1070_evttabprocesso_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1070_evttabprocesso_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1070_evttabprocesso_dados['identidade'] = doc.eSocial.evtTabProcesso['Id']
    evtTabProcesso = doc.eSocial.evtTabProcesso

    if 'tpAmb' in dir(evtTabProcesso.ideEvento): s1070_evttabprocesso_dados['tpamb'] = evtTabProcesso.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTabProcesso.ideEvento): s1070_evttabprocesso_dados['procemi'] = evtTabProcesso.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTabProcesso.ideEvento): s1070_evttabprocesso_dados['verproc'] = evtTabProcesso.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTabProcesso.ideEmpregador): s1070_evttabprocesso_dados['tpinsc'] = evtTabProcesso.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTabProcesso.ideEmpregador): s1070_evttabprocesso_dados['nrinsc'] = evtTabProcesso.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtTabProcesso.infoProcesso): s1070_evttabprocesso_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabProcesso.infoProcesso): s1070_evttabprocesso_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabProcesso.infoProcesso): s1070_evttabprocesso_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1070_evttabprocesso', s1070_evttabprocesso_dados)
    resp = executar_sql(insert, True)
    s1070_evttabprocesso_id = resp[0][0]
    dados = s1070_evttabprocesso_dados
    dados['evento'] = 's1070'
    dados['id'] = s1070_evttabprocesso_id
    dados['identidade_evento'] = doc.eSocial.evtTabProcesso['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'inclusao' in dir(evtTabProcesso.infoProcesso):
        for inclusao in evtTabProcesso.infoProcesso.inclusao:
            s1070_inclusao_dados = {}
            s1070_inclusao_dados['s1070_evttabprocesso_id'] = s1070_evttabprocesso_id

            if 'tpProc' in dir(inclusao.ideProcesso): s1070_inclusao_dados['tpproc'] = inclusao.ideProcesso.tpProc.cdata
            if 'nrProc' in dir(inclusao.ideProcesso): s1070_inclusao_dados['nrproc'] = inclusao.ideProcesso.nrProc.cdata
            if 'iniValid' in dir(inclusao.ideProcesso): s1070_inclusao_dados['inivalid'] = inclusao.ideProcesso.iniValid.cdata
            if 'fimValid' in dir(inclusao.ideProcesso): s1070_inclusao_dados['fimvalid'] = inclusao.ideProcesso.fimValid.cdata
            if 'indAutoria' in dir(inclusao.dadosProc): s1070_inclusao_dados['indautoria'] = inclusao.dadosProc.indAutoria.cdata
            if 'indMatProc' in dir(inclusao.dadosProc): s1070_inclusao_dados['indmatproc'] = inclusao.dadosProc.indMatProc.cdata
            if 'observacao' in dir(inclusao.dadosProc): s1070_inclusao_dados['observacao'] = inclusao.dadosProc.observacao.cdata
            insert = create_insert('s1070_inclusao', s1070_inclusao_dados)
            resp = executar_sql(insert, True)
            s1070_inclusao_id = resp[0][0]
            #print s1070_inclusao_id

            if 'dadosProcJud' in dir(inclusao.dadosProc):
                for dadosProcJud in inclusao.dadosProc.dadosProcJud:
                    s1070_inclusao_dadosprocjud_dados = {}
                    s1070_inclusao_dadosprocjud_dados['s1070_inclusao_id'] = s1070_inclusao_id

                    if 'ufVara' in dir(dadosProcJud): s1070_inclusao_dadosprocjud_dados['ufvara'] = dadosProcJud.ufVara.cdata
                    if 'codMunic' in dir(dadosProcJud): s1070_inclusao_dadosprocjud_dados['codmunic'] = dadosProcJud.codMunic.cdata
                    if 'idVara' in dir(dadosProcJud): s1070_inclusao_dadosprocjud_dados['idvara'] = dadosProcJud.idVara.cdata
                    insert = create_insert('s1070_inclusao_dadosprocjud', s1070_inclusao_dadosprocjud_dados)
                    resp = executar_sql(insert, True)
                    s1070_inclusao_dadosprocjud_id = resp[0][0]
                    #print s1070_inclusao_dadosprocjud_id

            if 'infoSusp' in dir(inclusao.dadosProc):
                for infoSusp in inclusao.dadosProc.infoSusp:
                    s1070_inclusao_infosusp_dados = {}
                    s1070_inclusao_infosusp_dados['s1070_inclusao_id'] = s1070_inclusao_id

                    if 'codSusp' in dir(infoSusp): s1070_inclusao_infosusp_dados['codsusp'] = infoSusp.codSusp.cdata
                    if 'indSusp' in dir(infoSusp): s1070_inclusao_infosusp_dados['indsusp'] = infoSusp.indSusp.cdata
                    if 'dtDecisao' in dir(infoSusp): s1070_inclusao_infosusp_dados['dtdecisao'] = infoSusp.dtDecisao.cdata
                    if 'indDeposito' in dir(infoSusp): s1070_inclusao_infosusp_dados['inddeposito'] = infoSusp.indDeposito.cdata
                    insert = create_insert('s1070_inclusao_infosusp', s1070_inclusao_infosusp_dados)
                    resp = executar_sql(insert, True)
                    s1070_inclusao_infosusp_id = resp[0][0]
                    #print s1070_inclusao_infosusp_id

    if 'alteracao' in dir(evtTabProcesso.infoProcesso):
        for alteracao in evtTabProcesso.infoProcesso.alteracao:
            s1070_alteracao_dados = {}
            s1070_alteracao_dados['s1070_evttabprocesso_id'] = s1070_evttabprocesso_id

            if 'tpProc' in dir(alteracao.ideProcesso): s1070_alteracao_dados['tpproc'] = alteracao.ideProcesso.tpProc.cdata
            if 'nrProc' in dir(alteracao.ideProcesso): s1070_alteracao_dados['nrproc'] = alteracao.ideProcesso.nrProc.cdata
            if 'iniValid' in dir(alteracao.ideProcesso): s1070_alteracao_dados['inivalid'] = alteracao.ideProcesso.iniValid.cdata
            if 'fimValid' in dir(alteracao.ideProcesso): s1070_alteracao_dados['fimvalid'] = alteracao.ideProcesso.fimValid.cdata
            if 'indAutoria' in dir(alteracao.dadosProc): s1070_alteracao_dados['indautoria'] = alteracao.dadosProc.indAutoria.cdata
            if 'indMatProc' in dir(alteracao.dadosProc): s1070_alteracao_dados['indmatproc'] = alteracao.dadosProc.indMatProc.cdata
            if 'observacao' in dir(alteracao.dadosProc): s1070_alteracao_dados['observacao'] = alteracao.dadosProc.observacao.cdata
            insert = create_insert('s1070_alteracao', s1070_alteracao_dados)
            resp = executar_sql(insert, True)
            s1070_alteracao_id = resp[0][0]
            #print s1070_alteracao_id

            if 'dadosProcJud' in dir(alteracao.dadosProc):
                for dadosProcJud in alteracao.dadosProc.dadosProcJud:
                    s1070_alteracao_dadosprocjud_dados = {}
                    s1070_alteracao_dadosprocjud_dados['s1070_alteracao_id'] = s1070_alteracao_id

                    if 'ufVara' in dir(dadosProcJud): s1070_alteracao_dadosprocjud_dados['ufvara'] = dadosProcJud.ufVara.cdata
                    if 'codMunic' in dir(dadosProcJud): s1070_alteracao_dadosprocjud_dados['codmunic'] = dadosProcJud.codMunic.cdata
                    if 'idVara' in dir(dadosProcJud): s1070_alteracao_dadosprocjud_dados['idvara'] = dadosProcJud.idVara.cdata
                    insert = create_insert('s1070_alteracao_dadosprocjud', s1070_alteracao_dadosprocjud_dados)
                    resp = executar_sql(insert, True)
                    s1070_alteracao_dadosprocjud_id = resp[0][0]
                    #print s1070_alteracao_dadosprocjud_id

            if 'infoSusp' in dir(alteracao.dadosProc):
                for infoSusp in alteracao.dadosProc.infoSusp:
                    s1070_alteracao_infosusp_dados = {}
                    s1070_alteracao_infosusp_dados['s1070_alteracao_id'] = s1070_alteracao_id

                    if 'codSusp' in dir(infoSusp): s1070_alteracao_infosusp_dados['codsusp'] = infoSusp.codSusp.cdata
                    if 'indSusp' in dir(infoSusp): s1070_alteracao_infosusp_dados['indsusp'] = infoSusp.indSusp.cdata
                    if 'dtDecisao' in dir(infoSusp): s1070_alteracao_infosusp_dados['dtdecisao'] = infoSusp.dtDecisao.cdata
                    if 'indDeposito' in dir(infoSusp): s1070_alteracao_infosusp_dados['inddeposito'] = infoSusp.indDeposito.cdata
                    insert = create_insert('s1070_alteracao_infosusp', s1070_alteracao_infosusp_dados)
                    resp = executar_sql(insert, True)
                    s1070_alteracao_infosusp_id = resp[0][0]
                    #print s1070_alteracao_infosusp_id

            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    s1070_alteracao_novavalidade_dados = {}
                    s1070_alteracao_novavalidade_dados['s1070_alteracao_id'] = s1070_alteracao_id

                    if 'iniValid' in dir(novaValidade): s1070_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    if 'fimValid' in dir(novaValidade): s1070_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    insert = create_insert('s1070_alteracao_novavalidade', s1070_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1070_alteracao_novavalidade_id = resp[0][0]
                    #print s1070_alteracao_novavalidade_id

    if 'exclusao' in dir(evtTabProcesso.infoProcesso):
        for exclusao in evtTabProcesso.infoProcesso.exclusao:
            s1070_exclusao_dados = {}
            s1070_exclusao_dados['s1070_evttabprocesso_id'] = s1070_evttabprocesso_id

            if 'tpProc' in dir(exclusao.ideProcesso): s1070_exclusao_dados['tpproc'] = exclusao.ideProcesso.tpProc.cdata
            if 'nrProc' in dir(exclusao.ideProcesso): s1070_exclusao_dados['nrproc'] = exclusao.ideProcesso.nrProc.cdata
            if 'iniValid' in dir(exclusao.ideProcesso): s1070_exclusao_dados['inivalid'] = exclusao.ideProcesso.iniValid.cdata
            if 'fimValid' in dir(exclusao.ideProcesso): s1070_exclusao_dados['fimvalid'] = exclusao.ideProcesso.fimValid.cdata
            insert = create_insert('s1070_exclusao', s1070_exclusao_dados)
            resp = executar_sql(insert, True)
            s1070_exclusao_id = resp[0][0]
            #print s1070_exclusao_id

    from emensageriapro.esocial.views.s1070_evttabprocesso_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1070_evttabprocesso_id, 'default')
    return dados