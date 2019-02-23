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



def read_s1010_evttabrubrica_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1010_evttabrubrica_obj(doc, status, validar)
    return dados

def read_s1010_evttabrubrica(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1010_evttabrubrica_obj(doc, status, validar)
    return dados



def read_s1010_evttabrubrica_obj(doc, status, validar=False):
    s1010_evttabrubrica_dados = {}
    s1010_evttabrubrica_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1010_evttabrubrica_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1010_evttabrubrica_dados['identidade'] = doc.eSocial.evtTabRubrica['Id']
    s1010_evttabrubrica_dados['processamento_codigo_resposta'] = 1
    evtTabRubrica = doc.eSocial.evtTabRubrica

    if 'tpAmb' in dir(evtTabRubrica.ideEvento): s1010_evttabrubrica_dados['tpamb'] = evtTabRubrica.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTabRubrica.ideEvento): s1010_evttabrubrica_dados['procemi'] = evtTabRubrica.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTabRubrica.ideEvento): s1010_evttabrubrica_dados['verproc'] = evtTabRubrica.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTabRubrica.ideEmpregador): s1010_evttabrubrica_dados['tpinsc'] = evtTabRubrica.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTabRubrica.ideEmpregador): s1010_evttabrubrica_dados['nrinsc'] = evtTabRubrica.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtTabRubrica.infoRubrica): s1010_evttabrubrica_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabRubrica.infoRubrica): s1010_evttabrubrica_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabRubrica.infoRubrica): s1010_evttabrubrica_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1010_evttabrubrica', s1010_evttabrubrica_dados)
    resp = executar_sql(insert, True)
    s1010_evttabrubrica_id = resp[0][0]
    dados = s1010_evttabrubrica_dados
    dados['evento'] = 's1010'
    dados['id'] = s1010_evttabrubrica_id
    dados['identidade_evento'] = doc.eSocial.evtTabRubrica['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'inclusao' in dir(evtTabRubrica.infoRubrica):
        for inclusao in evtTabRubrica.infoRubrica.inclusao:
            s1010_inclusao_dados = {}
            s1010_inclusao_dados['s1010_evttabrubrica_id'] = s1010_evttabrubrica_id

            if 'codRubr' in dir(inclusao.ideRubrica): s1010_inclusao_dados['codrubr'] = inclusao.ideRubrica.codRubr.cdata
            if 'ideTabRubr' in dir(inclusao.ideRubrica): s1010_inclusao_dados['idetabrubr'] = inclusao.ideRubrica.ideTabRubr.cdata
            if 'iniValid' in dir(inclusao.ideRubrica): s1010_inclusao_dados['inivalid'] = inclusao.ideRubrica.iniValid.cdata
            if 'fimValid' in dir(inclusao.ideRubrica): s1010_inclusao_dados['fimvalid'] = inclusao.ideRubrica.fimValid.cdata
            if 'dscRubr' in dir(inclusao.dadosRubrica): s1010_inclusao_dados['dscrubr'] = inclusao.dadosRubrica.dscRubr.cdata
            if 'natRubr' in dir(inclusao.dadosRubrica): s1010_inclusao_dados['natrubr'] = inclusao.dadosRubrica.natRubr.cdata
            if 'tpRubr' in dir(inclusao.dadosRubrica): s1010_inclusao_dados['tprubr'] = inclusao.dadosRubrica.tpRubr.cdata
            if 'codIncCP' in dir(inclusao.dadosRubrica): s1010_inclusao_dados['codinccp'] = inclusao.dadosRubrica.codIncCP.cdata
            if 'codIncIRRF' in dir(inclusao.dadosRubrica): s1010_inclusao_dados['codincirrf'] = inclusao.dadosRubrica.codIncIRRF.cdata
            if 'codIncFGTS' in dir(inclusao.dadosRubrica): s1010_inclusao_dados['codincfgts'] = inclusao.dadosRubrica.codIncFGTS.cdata
            if 'codIncSIND' in dir(inclusao.dadosRubrica): s1010_inclusao_dados['codincsind'] = inclusao.dadosRubrica.codIncSIND.cdata
            if 'codIncCPRP' in dir(inclusao.dadosRubrica): s1010_inclusao_dados['codinccprp'] = inclusao.dadosRubrica.codIncCPRP.cdata
            if 'tetoRemun' in dir(inclusao.dadosRubrica): s1010_inclusao_dados['tetoremun'] = inclusao.dadosRubrica.tetoRemun.cdata
            if 'observacao' in dir(inclusao.dadosRubrica): s1010_inclusao_dados['observacao'] = inclusao.dadosRubrica.observacao.cdata
            insert = create_insert('s1010_inclusao', s1010_inclusao_dados)
            resp = executar_sql(insert, True)
            s1010_inclusao_id = resp[0][0]
            #print s1010_inclusao_id

            if 'ideProcessoCP' in dir(inclusao.dadosRubrica):
                for ideProcessoCP in inclusao.dadosRubrica.ideProcessoCP:
                    s1010_inclusao_ideprocessocp_dados = {}
                    s1010_inclusao_ideprocessocp_dados['s1010_inclusao_id'] = s1010_inclusao_id

                    if 'tpProc' in dir(ideProcessoCP): s1010_inclusao_ideprocessocp_dados['tpproc'] = ideProcessoCP.tpProc.cdata
                    if 'nrProc' in dir(ideProcessoCP): s1010_inclusao_ideprocessocp_dados['nrproc'] = ideProcessoCP.nrProc.cdata
                    if 'extDecisao' in dir(ideProcessoCP): s1010_inclusao_ideprocessocp_dados['extdecisao'] = ideProcessoCP.extDecisao.cdata
                    if 'codSusp' in dir(ideProcessoCP): s1010_inclusao_ideprocessocp_dados['codsusp'] = ideProcessoCP.codSusp.cdata
                    insert = create_insert('s1010_inclusao_ideprocessocp', s1010_inclusao_ideprocessocp_dados)
                    resp = executar_sql(insert, True)
                    s1010_inclusao_ideprocessocp_id = resp[0][0]
                    #print s1010_inclusao_ideprocessocp_id

            if 'ideProcessoIRRF' in dir(inclusao.dadosRubrica):
                for ideProcessoIRRF in inclusao.dadosRubrica.ideProcessoIRRF:
                    s1010_inclusao_ideprocessoirrf_dados = {}
                    s1010_inclusao_ideprocessoirrf_dados['s1010_inclusao_id'] = s1010_inclusao_id

                    if 'nrProc' in dir(ideProcessoIRRF): s1010_inclusao_ideprocessoirrf_dados['nrproc'] = ideProcessoIRRF.nrProc.cdata
                    if 'codSusp' in dir(ideProcessoIRRF): s1010_inclusao_ideprocessoirrf_dados['codsusp'] = ideProcessoIRRF.codSusp.cdata
                    insert = create_insert('s1010_inclusao_ideprocessoirrf', s1010_inclusao_ideprocessoirrf_dados)
                    resp = executar_sql(insert, True)
                    s1010_inclusao_ideprocessoirrf_id = resp[0][0]
                    #print s1010_inclusao_ideprocessoirrf_id

            if 'ideProcessoFGTS' in dir(inclusao.dadosRubrica):
                for ideProcessoFGTS in inclusao.dadosRubrica.ideProcessoFGTS:
                    s1010_inclusao_ideprocessofgts_dados = {}
                    s1010_inclusao_ideprocessofgts_dados['s1010_inclusao_id'] = s1010_inclusao_id

                    if 'nrProc' in dir(ideProcessoFGTS): s1010_inclusao_ideprocessofgts_dados['nrproc'] = ideProcessoFGTS.nrProc.cdata
                    insert = create_insert('s1010_inclusao_ideprocessofgts', s1010_inclusao_ideprocessofgts_dados)
                    resp = executar_sql(insert, True)
                    s1010_inclusao_ideprocessofgts_id = resp[0][0]
                    #print s1010_inclusao_ideprocessofgts_id

            if 'ideProcessoSIND' in dir(inclusao.dadosRubrica):
                for ideProcessoSIND in inclusao.dadosRubrica.ideProcessoSIND:
                    s1010_inclusao_ideprocessosind_dados = {}
                    s1010_inclusao_ideprocessosind_dados['s1010_inclusao_id'] = s1010_inclusao_id

                    if 'nrProc' in dir(ideProcessoSIND): s1010_inclusao_ideprocessosind_dados['nrproc'] = ideProcessoSIND.nrProc.cdata
                    insert = create_insert('s1010_inclusao_ideprocessosind', s1010_inclusao_ideprocessosind_dados)
                    resp = executar_sql(insert, True)
                    s1010_inclusao_ideprocessosind_id = resp[0][0]
                    #print s1010_inclusao_ideprocessosind_id

            if 'ideProcessoCPRP' in dir(inclusao.dadosRubrica):
                for ideProcessoCPRP in inclusao.dadosRubrica.ideProcessoCPRP:
                    s1010_inclusao_ideprocessocprp_dados = {}
                    s1010_inclusao_ideprocessocprp_dados['s1010_inclusao_id'] = s1010_inclusao_id

                    if 'tpProc' in dir(ideProcessoCPRP): s1010_inclusao_ideprocessocprp_dados['tpproc'] = ideProcessoCPRP.tpProc.cdata
                    if 'nrProc' in dir(ideProcessoCPRP): s1010_inclusao_ideprocessocprp_dados['nrproc'] = ideProcessoCPRP.nrProc.cdata
                    if 'extDecisao' in dir(ideProcessoCPRP): s1010_inclusao_ideprocessocprp_dados['extdecisao'] = ideProcessoCPRP.extDecisao.cdata
                    insert = create_insert('s1010_inclusao_ideprocessocprp', s1010_inclusao_ideprocessocprp_dados)
                    resp = executar_sql(insert, True)
                    s1010_inclusao_ideprocessocprp_id = resp[0][0]
                    #print s1010_inclusao_ideprocessocprp_id

    if 'alteracao' in dir(evtTabRubrica.infoRubrica):
        for alteracao in evtTabRubrica.infoRubrica.alteracao:
            s1010_alteracao_dados = {}
            s1010_alteracao_dados['s1010_evttabrubrica_id'] = s1010_evttabrubrica_id

            if 'codRubr' in dir(alteracao.ideRubrica): s1010_alteracao_dados['codrubr'] = alteracao.ideRubrica.codRubr.cdata
            if 'ideTabRubr' in dir(alteracao.ideRubrica): s1010_alteracao_dados['idetabrubr'] = alteracao.ideRubrica.ideTabRubr.cdata
            if 'iniValid' in dir(alteracao.ideRubrica): s1010_alteracao_dados['inivalid'] = alteracao.ideRubrica.iniValid.cdata
            if 'fimValid' in dir(alteracao.ideRubrica): s1010_alteracao_dados['fimvalid'] = alteracao.ideRubrica.fimValid.cdata
            if 'dscRubr' in dir(alteracao.dadosRubrica): s1010_alteracao_dados['dscrubr'] = alteracao.dadosRubrica.dscRubr.cdata
            if 'natRubr' in dir(alteracao.dadosRubrica): s1010_alteracao_dados['natrubr'] = alteracao.dadosRubrica.natRubr.cdata
            if 'tpRubr' in dir(alteracao.dadosRubrica): s1010_alteracao_dados['tprubr'] = alteracao.dadosRubrica.tpRubr.cdata
            if 'codIncCP' in dir(alteracao.dadosRubrica): s1010_alteracao_dados['codinccp'] = alteracao.dadosRubrica.codIncCP.cdata
            if 'codIncIRRF' in dir(alteracao.dadosRubrica): s1010_alteracao_dados['codincirrf'] = alteracao.dadosRubrica.codIncIRRF.cdata
            if 'codIncFGTS' in dir(alteracao.dadosRubrica): s1010_alteracao_dados['codincfgts'] = alteracao.dadosRubrica.codIncFGTS.cdata
            if 'codIncSIND' in dir(alteracao.dadosRubrica): s1010_alteracao_dados['codincsind'] = alteracao.dadosRubrica.codIncSIND.cdata
            if 'codIncCPRP' in dir(alteracao.dadosRubrica): s1010_alteracao_dados['codinccprp'] = alteracao.dadosRubrica.codIncCPRP.cdata
            if 'tetoRemun' in dir(alteracao.dadosRubrica): s1010_alteracao_dados['tetoremun'] = alteracao.dadosRubrica.tetoRemun.cdata
            if 'observacao' in dir(alteracao.dadosRubrica): s1010_alteracao_dados['observacao'] = alteracao.dadosRubrica.observacao.cdata
            insert = create_insert('s1010_alteracao', s1010_alteracao_dados)
            resp = executar_sql(insert, True)
            s1010_alteracao_id = resp[0][0]
            #print s1010_alteracao_id

            if 'ideProcessoCP' in dir(alteracao.dadosRubrica):
                for ideProcessoCP in alteracao.dadosRubrica.ideProcessoCP:
                    s1010_alteracao_ideprocessocp_dados = {}
                    s1010_alteracao_ideprocessocp_dados['s1010_alteracao_id'] = s1010_alteracao_id

                    if 'tpProc' in dir(ideProcessoCP): s1010_alteracao_ideprocessocp_dados['tpproc'] = ideProcessoCP.tpProc.cdata
                    if 'nrProc' in dir(ideProcessoCP): s1010_alteracao_ideprocessocp_dados['nrproc'] = ideProcessoCP.nrProc.cdata
                    if 'extDecisao' in dir(ideProcessoCP): s1010_alteracao_ideprocessocp_dados['extdecisao'] = ideProcessoCP.extDecisao.cdata
                    if 'codSusp' in dir(ideProcessoCP): s1010_alteracao_ideprocessocp_dados['codsusp'] = ideProcessoCP.codSusp.cdata
                    insert = create_insert('s1010_alteracao_ideprocessocp', s1010_alteracao_ideprocessocp_dados)
                    resp = executar_sql(insert, True)
                    s1010_alteracao_ideprocessocp_id = resp[0][0]
                    #print s1010_alteracao_ideprocessocp_id

            if 'ideProcessoIRRF' in dir(alteracao.dadosRubrica):
                for ideProcessoIRRF in alteracao.dadosRubrica.ideProcessoIRRF:
                    s1010_alteracao_ideprocessoirrf_dados = {}
                    s1010_alteracao_ideprocessoirrf_dados['s1010_alteracao_id'] = s1010_alteracao_id

                    if 'nrProc' in dir(ideProcessoIRRF): s1010_alteracao_ideprocessoirrf_dados['nrproc'] = ideProcessoIRRF.nrProc.cdata
                    if 'codSusp' in dir(ideProcessoIRRF): s1010_alteracao_ideprocessoirrf_dados['codsusp'] = ideProcessoIRRF.codSusp.cdata
                    insert = create_insert('s1010_alteracao_ideprocessoirrf', s1010_alteracao_ideprocessoirrf_dados)
                    resp = executar_sql(insert, True)
                    s1010_alteracao_ideprocessoirrf_id = resp[0][0]
                    #print s1010_alteracao_ideprocessoirrf_id

            if 'ideProcessoFGTS' in dir(alteracao.dadosRubrica):
                for ideProcessoFGTS in alteracao.dadosRubrica.ideProcessoFGTS:
                    s1010_alteracao_ideprocessofgts_dados = {}
                    s1010_alteracao_ideprocessofgts_dados['s1010_alteracao_id'] = s1010_alteracao_id

                    if 'nrProc' in dir(ideProcessoFGTS): s1010_alteracao_ideprocessofgts_dados['nrproc'] = ideProcessoFGTS.nrProc.cdata
                    insert = create_insert('s1010_alteracao_ideprocessofgts', s1010_alteracao_ideprocessofgts_dados)
                    resp = executar_sql(insert, True)
                    s1010_alteracao_ideprocessofgts_id = resp[0][0]
                    #print s1010_alteracao_ideprocessofgts_id

            if 'ideProcessoSIND' in dir(alteracao.dadosRubrica):
                for ideProcessoSIND in alteracao.dadosRubrica.ideProcessoSIND:
                    s1010_alteracao_ideprocessosind_dados = {}
                    s1010_alteracao_ideprocessosind_dados['s1010_alteracao_id'] = s1010_alteracao_id

                    if 'nrProc' in dir(ideProcessoSIND): s1010_alteracao_ideprocessosind_dados['nrproc'] = ideProcessoSIND.nrProc.cdata
                    insert = create_insert('s1010_alteracao_ideprocessosind', s1010_alteracao_ideprocessosind_dados)
                    resp = executar_sql(insert, True)
                    s1010_alteracao_ideprocessosind_id = resp[0][0]
                    #print s1010_alteracao_ideprocessosind_id

            if 'ideProcessoCPRP' in dir(alteracao.dadosRubrica):
                for ideProcessoCPRP in alteracao.dadosRubrica.ideProcessoCPRP:
                    s1010_alteracao_ideprocessocprp_dados = {}
                    s1010_alteracao_ideprocessocprp_dados['s1010_alteracao_id'] = s1010_alteracao_id

                    if 'tpProc' in dir(ideProcessoCPRP): s1010_alteracao_ideprocessocprp_dados['tpproc'] = ideProcessoCPRP.tpProc.cdata
                    if 'nrProc' in dir(ideProcessoCPRP): s1010_alteracao_ideprocessocprp_dados['nrproc'] = ideProcessoCPRP.nrProc.cdata
                    if 'extDecisao' in dir(ideProcessoCPRP): s1010_alteracao_ideprocessocprp_dados['extdecisao'] = ideProcessoCPRP.extDecisao.cdata
                    insert = create_insert('s1010_alteracao_ideprocessocprp', s1010_alteracao_ideprocessocprp_dados)
                    resp = executar_sql(insert, True)
                    s1010_alteracao_ideprocessocprp_id = resp[0][0]
                    #print s1010_alteracao_ideprocessocprp_id

            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    s1010_alteracao_novavalidade_dados = {}
                    s1010_alteracao_novavalidade_dados['s1010_alteracao_id'] = s1010_alteracao_id

                    if 'iniValid' in dir(novaValidade): s1010_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    if 'fimValid' in dir(novaValidade): s1010_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    insert = create_insert('s1010_alteracao_novavalidade', s1010_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1010_alteracao_novavalidade_id = resp[0][0]
                    #print s1010_alteracao_novavalidade_id

    if 'exclusao' in dir(evtTabRubrica.infoRubrica):
        for exclusao in evtTabRubrica.infoRubrica.exclusao:
            s1010_exclusao_dados = {}
            s1010_exclusao_dados['s1010_evttabrubrica_id'] = s1010_evttabrubrica_id

            if 'codRubr' in dir(exclusao.ideRubrica): s1010_exclusao_dados['codrubr'] = exclusao.ideRubrica.codRubr.cdata
            if 'ideTabRubr' in dir(exclusao.ideRubrica): s1010_exclusao_dados['idetabrubr'] = exclusao.ideRubrica.ideTabRubr.cdata
            if 'iniValid' in dir(exclusao.ideRubrica): s1010_exclusao_dados['inivalid'] = exclusao.ideRubrica.iniValid.cdata
            if 'fimValid' in dir(exclusao.ideRubrica): s1010_exclusao_dados['fimvalid'] = exclusao.ideRubrica.fimValid.cdata
            insert = create_insert('s1010_exclusao', s1010_exclusao_dados)
            resp = executar_sql(insert, True)
            s1010_exclusao_id = resp[0][0]
            #print s1010_exclusao_id

    from emensageriapro.esocial.views.s1010_evttabrubrica_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1010_evttabrubrica_id, 'default')
    return dados