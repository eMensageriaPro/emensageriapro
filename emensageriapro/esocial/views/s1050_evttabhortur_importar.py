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


def read_s1050_evttabhortur_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s1050_evttabhortur_obj(doc, status, validar)
    return dados

def read_s1050_evttabhortur(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s1050_evttabhortur_obj(doc, status, validar)
    return dados



def read_s1050_evttabhortur_obj(doc, status, validar=False):
    s1050_evttabhortur_dados = {}
    s1050_evttabhortur_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1050_evttabhortur_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1050_evttabhortur_dados['identidade'] = doc.eSocial.evtTabHorTur['Id']
    s1050_evttabhortur_dados['processamento_codigo_resposta'] = 1
    evtTabHorTur = doc.eSocial.evtTabHorTur

    if 'tpAmb' in dir(evtTabHorTur.ideEvento): s1050_evttabhortur_dados['tpamb'] = evtTabHorTur.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTabHorTur.ideEvento): s1050_evttabhortur_dados['procemi'] = evtTabHorTur.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTabHorTur.ideEvento): s1050_evttabhortur_dados['verproc'] = evtTabHorTur.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTabHorTur.ideEmpregador): s1050_evttabhortur_dados['tpinsc'] = evtTabHorTur.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTabHorTur.ideEmpregador): s1050_evttabhortur_dados['nrinsc'] = evtTabHorTur.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtTabHorTur.infoHorContratual): s1050_evttabhortur_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabHorTur.infoHorContratual): s1050_evttabhortur_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabHorTur.infoHorContratual): s1050_evttabhortur_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1050_evttabhortur', s1050_evttabhortur_dados)
    resp = executar_sql(insert, True)
    s1050_evttabhortur_id = resp[0][0]
    dados = s1050_evttabhortur_dados
    dados['evento'] = 's1050'
    dados['id'] = s1050_evttabhortur_id
    dados['identidade_evento'] = doc.eSocial.evtTabHorTur['Id']
    dados['status'] = 1

    if 'inclusao' in dir(evtTabHorTur.infoHorContratual):
        for inclusao in evtTabHorTur.infoHorContratual.inclusao:
            s1050_inclusao_dados = {}
            s1050_inclusao_dados['s1050_evttabhortur_id'] = s1050_evttabhortur_id

            if 'codHorContrat' in dir(inclusao.ideHorContratual): s1050_inclusao_dados['codhorcontrat'] = inclusao.ideHorContratual.codHorContrat.cdata
            if 'iniValid' in dir(inclusao.ideHorContratual): s1050_inclusao_dados['inivalid'] = inclusao.ideHorContratual.iniValid.cdata
            if 'fimValid' in dir(inclusao.ideHorContratual): s1050_inclusao_dados['fimvalid'] = inclusao.ideHorContratual.fimValid.cdata
            if 'hrEntr' in dir(inclusao.dadosHorContratual): s1050_inclusao_dados['hrentr'] = inclusao.dadosHorContratual.hrEntr.cdata
            if 'hrSaida' in dir(inclusao.dadosHorContratual): s1050_inclusao_dados['hrsaida'] = inclusao.dadosHorContratual.hrSaida.cdata
            if 'durJornada' in dir(inclusao.dadosHorContratual): s1050_inclusao_dados['durjornada'] = inclusao.dadosHorContratual.durJornada.cdata
            if 'perHorFlexivel' in dir(inclusao.dadosHorContratual): s1050_inclusao_dados['perhorflexivel'] = inclusao.dadosHorContratual.perHorFlexivel.cdata
            insert = create_insert('s1050_inclusao', s1050_inclusao_dados)
            resp = executar_sql(insert, True)
            s1050_inclusao_id = resp[0][0]
            #print s1050_inclusao_id

            if 'horarioIntervalo' in dir(inclusao.dadosHorContratual):
                for horarioIntervalo in inclusao.dadosHorContratual.horarioIntervalo:
                    s1050_inclusao_horariointervalo_dados = {}
                    s1050_inclusao_horariointervalo_dados['s1050_inclusao_id'] = s1050_inclusao_id

                    if 'tpInterv' in dir(horarioIntervalo): s1050_inclusao_horariointervalo_dados['tpinterv'] = horarioIntervalo.tpInterv.cdata
                    if 'durInterv' in dir(horarioIntervalo): s1050_inclusao_horariointervalo_dados['durinterv'] = horarioIntervalo.durInterv.cdata
                    if 'iniInterv' in dir(horarioIntervalo): s1050_inclusao_horariointervalo_dados['iniinterv'] = horarioIntervalo.iniInterv.cdata
                    if 'termInterv' in dir(horarioIntervalo): s1050_inclusao_horariointervalo_dados['terminterv'] = horarioIntervalo.termInterv.cdata
                    insert = create_insert('s1050_inclusao_horariointervalo', s1050_inclusao_horariointervalo_dados)
                    resp = executar_sql(insert, True)
                    s1050_inclusao_horariointervalo_id = resp[0][0]
                    #print s1050_inclusao_horariointervalo_id

    if 'alteracao' in dir(evtTabHorTur.infoHorContratual):
        for alteracao in evtTabHorTur.infoHorContratual.alteracao:
            s1050_alteracao_dados = {}
            s1050_alteracao_dados['s1050_evttabhortur_id'] = s1050_evttabhortur_id

            if 'codHorContrat' in dir(alteracao.ideHorContratual): s1050_alteracao_dados['codhorcontrat'] = alteracao.ideHorContratual.codHorContrat.cdata
            if 'iniValid' in dir(alteracao.ideHorContratual): s1050_alteracao_dados['inivalid'] = alteracao.ideHorContratual.iniValid.cdata
            if 'fimValid' in dir(alteracao.ideHorContratual): s1050_alteracao_dados['fimvalid'] = alteracao.ideHorContratual.fimValid.cdata
            if 'hrEntr' in dir(alteracao.dadosHorContratual): s1050_alteracao_dados['hrentr'] = alteracao.dadosHorContratual.hrEntr.cdata
            if 'hrSaida' in dir(alteracao.dadosHorContratual): s1050_alteracao_dados['hrsaida'] = alteracao.dadosHorContratual.hrSaida.cdata
            if 'durJornada' in dir(alteracao.dadosHorContratual): s1050_alteracao_dados['durjornada'] = alteracao.dadosHorContratual.durJornada.cdata
            if 'perHorFlexivel' in dir(alteracao.dadosHorContratual): s1050_alteracao_dados['perhorflexivel'] = alteracao.dadosHorContratual.perHorFlexivel.cdata
            insert = create_insert('s1050_alteracao', s1050_alteracao_dados)
            resp = executar_sql(insert, True)
            s1050_alteracao_id = resp[0][0]
            #print s1050_alteracao_id

            if 'horarioIntervalo' in dir(alteracao.dadosHorContratual):
                for horarioIntervalo in alteracao.dadosHorContratual.horarioIntervalo:
                    s1050_alteracao_horariointervalo_dados = {}
                    s1050_alteracao_horariointervalo_dados['s1050_alteracao_id'] = s1050_alteracao_id

                    if 'tpInterv' in dir(horarioIntervalo): s1050_alteracao_horariointervalo_dados['tpinterv'] = horarioIntervalo.tpInterv.cdata
                    if 'durInterv' in dir(horarioIntervalo): s1050_alteracao_horariointervalo_dados['durinterv'] = horarioIntervalo.durInterv.cdata
                    if 'iniInterv' in dir(horarioIntervalo): s1050_alteracao_horariointervalo_dados['iniinterv'] = horarioIntervalo.iniInterv.cdata
                    if 'termInterv' in dir(horarioIntervalo): s1050_alteracao_horariointervalo_dados['terminterv'] = horarioIntervalo.termInterv.cdata
                    insert = create_insert('s1050_alteracao_horariointervalo', s1050_alteracao_horariointervalo_dados)
                    resp = executar_sql(insert, True)
                    s1050_alteracao_horariointervalo_id = resp[0][0]
                    #print s1050_alteracao_horariointervalo_id

            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    s1050_alteracao_novavalidade_dados = {}
                    s1050_alteracao_novavalidade_dados['s1050_alteracao_id'] = s1050_alteracao_id

                    if 'iniValid' in dir(novaValidade): s1050_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    if 'fimValid' in dir(novaValidade): s1050_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    insert = create_insert('s1050_alteracao_novavalidade', s1050_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1050_alteracao_novavalidade_id = resp[0][0]
                    #print s1050_alteracao_novavalidade_id

    if 'exclusao' in dir(evtTabHorTur.infoHorContratual):
        for exclusao in evtTabHorTur.infoHorContratual.exclusao:
            s1050_exclusao_dados = {}
            s1050_exclusao_dados['s1050_evttabhortur_id'] = s1050_evttabhortur_id

            if 'codHorContrat' in dir(exclusao.ideHorContratual): s1050_exclusao_dados['codhorcontrat'] = exclusao.ideHorContratual.codHorContrat.cdata
            if 'iniValid' in dir(exclusao.ideHorContratual): s1050_exclusao_dados['inivalid'] = exclusao.ideHorContratual.iniValid.cdata
            if 'fimValid' in dir(exclusao.ideHorContratual): s1050_exclusao_dados['fimvalid'] = exclusao.ideHorContratual.fimValid.cdata
            insert = create_insert('s1050_exclusao', s1050_exclusao_dados)
            resp = executar_sql(insert, True)
            s1050_exclusao_id = resp[0][0]
            #print s1050_exclusao_id

    from emensageriapro.esocial.views.s1050_evttabhortur_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1050_evttabhortur_id, 'default')
    return dados