#coding:utf-8
"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos<www.emensageria.com.br>
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
from emensageriapro.padrao import ler_arquivo


def validacoes_s1020_evttablotacao(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabLotacao = doc.eSocial.evtTabLotacao

    if 'tpAmb' in dir(evtTabLotacao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabLotacao.ideEvento.tpAmb', evtTabLotacao.ideEvento.tpAmb.cdata, 1, u'1;2')
    if 'procEmi' in dir(evtTabLotacao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabLotacao.ideEvento.procEmi', evtTabLotacao.ideEvento.procEmi.cdata, 1, u'1;2;3;4;5')
    if 'verProc' in dir(evtTabLotacao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabLotacao.ideEvento.verProc', evtTabLotacao.ideEvento.verProc.cdata, 1, u'')
    if 'tpInsc' in dir(evtTabLotacao.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabLotacao.ideEmpregador.tpInsc', evtTabLotacao.ideEmpregador.tpInsc.cdata, 1, u'1;2;3;4')
    if 'nrInsc' in dir(evtTabLotacao.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabLotacao.ideEmpregador.nrInsc', evtTabLotacao.ideEmpregador.nrInsc.cdata, 1, u'')
    if 'inclusao' in dir(evtTabLotacao.infoLotacao):
        for inclusao in evtTabLotacao.infoLotacao.inclusao:

            if 'codLotacao' in dir(inclusao.ideLotacao): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideLotacao.codLotacao', inclusao.ideLotacao.codLotacao.cdata, 1, u'')
            if 'iniValid' in dir(inclusao.ideLotacao): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideLotacao.iniValid', inclusao.ideLotacao.iniValid.cdata, 1, u'')
            if 'fimValid' in dir(inclusao.ideLotacao): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideLotacao.fimValid', inclusao.ideLotacao.fimValid.cdata, 0, u'')
            if 'tpLotacao' in dir(inclusao.dadosLotacao): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosLotacao.tpLotacao', inclusao.dadosLotacao.tpLotacao.cdata, 1, u'01;02;03;04;05;06;07;08;09;10;21;24;90;91')
            if 'tpInsc' in dir(inclusao.dadosLotacao): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosLotacao.tpInsc', inclusao.dadosLotacao.tpInsc.cdata, 0, u'1;2;3;4')
            if 'nrInsc' in dir(inclusao.dadosLotacao): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosLotacao.nrInsc', inclusao.dadosLotacao.nrInsc.cdata, 0, u'')
            if 'fpas' in dir(inclusao.dadosLotacao.fpasLotacao): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosLotacao.fpasLotacao.fpas', inclusao.dadosLotacao.fpasLotacao.fpas.cdata, 1, u'')
            if 'codTercs' in dir(inclusao.dadosLotacao.fpasLotacao): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosLotacao.fpasLotacao.codTercs', inclusao.dadosLotacao.fpasLotacao.codTercs.cdata, 1, u'')
            if 'codTercsSusp' in dir(inclusao.dadosLotacao.fpasLotacao): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosLotacao.fpasLotacao.codTercsSusp', inclusao.dadosLotacao.fpasLotacao.codTercsSusp.cdata, 0, u'')

            if 'procJudTerceiro' in dir(inclusao.dadosLotacao.fpasLotacao.infoProcJudTerceiros):
                for procJudTerceiro in inclusao.dadosLotacao.fpasLotacao.infoProcJudTerceiros.procJudTerceiro:

                    if 'codTerc' in dir(procJudTerceiro): validacoes_lista = validar_campo(validacoes_lista,'procJudTerceiro.codTerc', procJudTerceiro.codTerc.cdata, 1, u'')
                    if 'nrProcJud' in dir(procJudTerceiro): validacoes_lista = validar_campo(validacoes_lista,'procJudTerceiro.nrProcJud', procJudTerceiro.nrProcJud.cdata, 1, u'')
                    if 'codSusp' in dir(procJudTerceiro): validacoes_lista = validar_campo(validacoes_lista,'procJudTerceiro.codSusp', procJudTerceiro.codSusp.cdata, 1, u'')

            if 'infoEmprParcial' in dir(inclusao.dadosLotacao):
                for infoEmprParcial in inclusao.dadosLotacao.infoEmprParcial:

                    if 'tpInscContrat' in dir(infoEmprParcial): validacoes_lista = validar_campo(validacoes_lista,'infoEmprParcial.tpInscContrat', infoEmprParcial.tpInscContrat.cdata, 1, u'1;2;3;4')
                    if 'nrInscContrat' in dir(infoEmprParcial): validacoes_lista = validar_campo(validacoes_lista,'infoEmprParcial.nrInscContrat', infoEmprParcial.nrInscContrat.cdata, 1, u'')
                    if 'tpInscProp' in dir(infoEmprParcial): validacoes_lista = validar_campo(validacoes_lista,'infoEmprParcial.tpInscProp', infoEmprParcial.tpInscProp.cdata, 1, u'1;2;3;4')
                    if 'nrInscProp' in dir(infoEmprParcial): validacoes_lista = validar_campo(validacoes_lista,'infoEmprParcial.nrInscProp', infoEmprParcial.nrInscProp.cdata, 1, u'')

    if 'alteracao' in dir(evtTabLotacao.infoLotacao):
        for alteracao in evtTabLotacao.infoLotacao.alteracao:

            if 'codLotacao' in dir(alteracao.ideLotacao): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideLotacao.codLotacao', alteracao.ideLotacao.codLotacao.cdata, 1, u'')
            if 'iniValid' in dir(alteracao.ideLotacao): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideLotacao.iniValid', alteracao.ideLotacao.iniValid.cdata, 1, u'')
            if 'fimValid' in dir(alteracao.ideLotacao): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideLotacao.fimValid', alteracao.ideLotacao.fimValid.cdata, 0, u'')
            if 'tpLotacao' in dir(alteracao.dadosLotacao): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosLotacao.tpLotacao', alteracao.dadosLotacao.tpLotacao.cdata, 1, u'01;02;03;04;05;06;07;08;09;10;21;24;90;91')
            if 'tpInsc' in dir(alteracao.dadosLotacao): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosLotacao.tpInsc', alteracao.dadosLotacao.tpInsc.cdata, 0, u'1;2;3;4')
            if 'nrInsc' in dir(alteracao.dadosLotacao): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosLotacao.nrInsc', alteracao.dadosLotacao.nrInsc.cdata, 0, u'')
            if 'fpas' in dir(alteracao.dadosLotacao.fpasLotacao): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosLotacao.fpasLotacao.fpas', alteracao.dadosLotacao.fpasLotacao.fpas.cdata, 1, u'')
            if 'codTercs' in dir(alteracao.dadosLotacao.fpasLotacao): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosLotacao.fpasLotacao.codTercs', alteracao.dadosLotacao.fpasLotacao.codTercs.cdata, 1, u'')
            if 'codTercsSusp' in dir(alteracao.dadosLotacao.fpasLotacao): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosLotacao.fpasLotacao.codTercsSusp', alteracao.dadosLotacao.fpasLotacao.codTercsSusp.cdata, 0, u'')

            if 'procJudTerceiro' in dir(alteracao.dadosLotacao.fpasLotacao.infoProcJudTerceiros):
                for procJudTerceiro in alteracao.dadosLotacao.fpasLotacao.infoProcJudTerceiros.procJudTerceiro:

                    if 'codTerc' in dir(procJudTerceiro): validacoes_lista = validar_campo(validacoes_lista,'procJudTerceiro.codTerc', procJudTerceiro.codTerc.cdata, 1, u'')
                    if 'nrProcJud' in dir(procJudTerceiro): validacoes_lista = validar_campo(validacoes_lista,'procJudTerceiro.nrProcJud', procJudTerceiro.nrProcJud.cdata, 1, u'')
                    if 'codSusp' in dir(procJudTerceiro): validacoes_lista = validar_campo(validacoes_lista,'procJudTerceiro.codSusp', procJudTerceiro.codSusp.cdata, 1, u'')

            if 'infoEmprParcial' in dir(alteracao.dadosLotacao):
                for infoEmprParcial in alteracao.dadosLotacao.infoEmprParcial:

                    if 'tpInscContrat' in dir(infoEmprParcial): validacoes_lista = validar_campo(validacoes_lista,'infoEmprParcial.tpInscContrat', infoEmprParcial.tpInscContrat.cdata, 1, u'1;2;3;4')
                    if 'nrInscContrat' in dir(infoEmprParcial): validacoes_lista = validar_campo(validacoes_lista,'infoEmprParcial.nrInscContrat', infoEmprParcial.nrInscContrat.cdata, 1, u'')
                    if 'tpInscProp' in dir(infoEmprParcial): validacoes_lista = validar_campo(validacoes_lista,'infoEmprParcial.tpInscProp', infoEmprParcial.tpInscProp.cdata, 1, u'1;2;3;4')
                    if 'nrInscProp' in dir(infoEmprParcial): validacoes_lista = validar_campo(validacoes_lista,'infoEmprParcial.nrInscProp', infoEmprParcial.nrInscProp.cdata, 1, u'')

            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:

                    if 'iniValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.iniValid', novaValidade.iniValid.cdata, 1, u'')
                    if 'fimValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.fimValid', novaValidade.fimValid.cdata, 0, u'')

    if 'exclusao' in dir(evtTabLotacao.infoLotacao):
        for exclusao in evtTabLotacao.infoLotacao.exclusao:

            if 'codLotacao' in dir(exclusao.ideLotacao): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideLotacao.codLotacao', exclusao.ideLotacao.codLotacao.cdata, 1, u'')
            if 'iniValid' in dir(exclusao.ideLotacao): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideLotacao.iniValid', exclusao.ideLotacao.iniValid.cdata, 1, u'')
            if 'fimValid' in dir(exclusao.ideLotacao): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideLotacao.fimValid', exclusao.ideLotacao.fimValid.cdata, 0, u'')

    return validacoes_lista