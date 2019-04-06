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


def validacoes_s1005_evttabestab(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabEstab = doc.eSocial.evtTabEstab

    if 'tpAmb' in dir(evtTabEstab.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabEstab.ideEvento.tpAmb', evtTabEstab.ideEvento.tpAmb.cdata, 1, u'1;2')
    if 'procEmi' in dir(evtTabEstab.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabEstab.ideEvento.procEmi', evtTabEstab.ideEvento.procEmi.cdata, 1, u'1;2;3;4;5')
    if 'verProc' in dir(evtTabEstab.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabEstab.ideEvento.verProc', evtTabEstab.ideEvento.verProc.cdata, 1, u'')
    if 'tpInsc' in dir(evtTabEstab.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabEstab.ideEmpregador.tpInsc', evtTabEstab.ideEmpregador.tpInsc.cdata, 1, u'1;2;3;4')
    if 'nrInsc' in dir(evtTabEstab.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabEstab.ideEmpregador.nrInsc', evtTabEstab.ideEmpregador.nrInsc.cdata, 1, u'')
    if 'inclusao' in dir(evtTabEstab.infoEstab):
        for inclusao in evtTabEstab.infoEstab.inclusao:

            if 'tpInsc' in dir(inclusao.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideEstab.tpInsc', inclusao.ideEstab.tpInsc.cdata, 1, u'1;3;4')
            if 'nrInsc' in dir(inclusao.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideEstab.nrInsc', inclusao.ideEstab.nrInsc.cdata, 1, u'')
            if 'iniValid' in dir(inclusao.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideEstab.iniValid', inclusao.ideEstab.iniValid.cdata, 1, u'')
            if 'fimValid' in dir(inclusao.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideEstab.fimValid', inclusao.ideEstab.fimValid.cdata, 0, u'')
            if 'cnaePrep' in dir(inclusao.dadosEstab): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosEstab.cnaePrep', inclusao.dadosEstab.cnaePrep.cdata, 1, u'')
            if 'aliqRat' in dir(inclusao.dadosEstab.aliqGilrat): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosEstab.aliqGilrat.aliqRat', inclusao.dadosEstab.aliqGilrat.aliqRat.cdata, 1, u'1;2;3')
            if 'fap' in dir(inclusao.dadosEstab.aliqGilrat): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosEstab.aliqGilrat.fap', inclusao.dadosEstab.aliqGilrat.fap.cdata, 0, u'')
            if 'aliqRatAjust' in dir(inclusao.dadosEstab.aliqGilrat): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosEstab.aliqGilrat.aliqRatAjust', inclusao.dadosEstab.aliqGilrat.aliqRatAjust.cdata, 0, u'')
            if 'regPt' in dir(inclusao.dadosEstab.infoTrab): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosEstab.infoTrab.regPt', inclusao.dadosEstab.infoTrab.regPt.cdata, 1, u'0;1;2;3;4;5;6')
            if 'contApr' in dir(inclusao.dadosEstab.infoTrab.infoApr): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosEstab.infoTrab.infoApr.contApr', inclusao.dadosEstab.infoTrab.infoApr.contApr.cdata, 1, u'0;1;2')
            if 'nrProcJud' in dir(inclusao.dadosEstab.infoTrab.infoApr): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosEstab.infoTrab.infoApr.nrProcJud', inclusao.dadosEstab.infoTrab.infoApr.nrProcJud.cdata, 0, u'')
            if 'contEntEd' in dir(inclusao.dadosEstab.infoTrab.infoApr): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosEstab.infoTrab.infoApr.contEntEd', inclusao.dadosEstab.infoTrab.infoApr.contEntEd.cdata, 0, u'S;N')

            if 'procAdmJudRat' in dir(inclusao.dadosEstab.aliqGilrat):
                for procAdmJudRat in inclusao.dadosEstab.aliqGilrat.procAdmJudRat:

                    if 'tpProc' in dir(procAdmJudRat): validacoes_lista = validar_campo(validacoes_lista,'procAdmJudRat.tpProc', procAdmJudRat.tpProc.cdata, 1, u'1;2')
                    if 'nrProc' in dir(procAdmJudRat): validacoes_lista = validar_campo(validacoes_lista,'procAdmJudRat.nrProc', procAdmJudRat.nrProc.cdata, 1, u'')
                    if 'codSusp' in dir(procAdmJudRat): validacoes_lista = validar_campo(validacoes_lista,'procAdmJudRat.codSusp', procAdmJudRat.codSusp.cdata, 1, u'')

            if 'procAdmJudFap' in dir(inclusao.dadosEstab.aliqGilrat):
                for procAdmJudFap in inclusao.dadosEstab.aliqGilrat.procAdmJudFap:

                    if 'tpProc' in dir(procAdmJudFap): validacoes_lista = validar_campo(validacoes_lista,'procAdmJudFap.tpProc', procAdmJudFap.tpProc.cdata, 1, u'1;2;4')
                    if 'nrProc' in dir(procAdmJudFap): validacoes_lista = validar_campo(validacoes_lista,'procAdmJudFap.nrProc', procAdmJudFap.nrProc.cdata, 1, u'')
                    if 'codSusp' in dir(procAdmJudFap): validacoes_lista = validar_campo(validacoes_lista,'procAdmJudFap.codSusp', procAdmJudFap.codSusp.cdata, 1, u'')

            if 'infoCaepf' in dir(inclusao.dadosEstab):
                for infoCaepf in inclusao.dadosEstab.infoCaepf:

                    if 'tpCaepf' in dir(infoCaepf): validacoes_lista = validar_campo(validacoes_lista,'infoCaepf.tpCaepf', infoCaepf.tpCaepf.cdata, 1, u'1;2;3')

            if 'infoObra' in dir(inclusao.dadosEstab):
                for infoObra in inclusao.dadosEstab.infoObra:

                    if 'indSubstPatrObra' in dir(infoObra): validacoes_lista = validar_campo(validacoes_lista,'infoObra.indSubstPatrObra', infoObra.indSubstPatrObra.cdata, 1, u'1;2')

            if 'infoEntEduc' in dir(inclusao.dadosEstab.infoTrab.infoApr):
                for infoEntEduc in inclusao.dadosEstab.infoTrab.infoApr.infoEntEduc:

                    if 'nrInsc' in dir(infoEntEduc): validacoes_lista = validar_campo(validacoes_lista,'infoEntEduc.nrInsc', infoEntEduc.nrInsc.cdata, 1, u'')

            if 'infoPCD' in dir(inclusao.dadosEstab.infoTrab):
                for infoPCD in inclusao.dadosEstab.infoTrab.infoPCD:

                    if 'contPCD' in dir(infoPCD): validacoes_lista = validar_campo(validacoes_lista,'infoPCD.contPCD', infoPCD.contPCD.cdata, 1, u'0;1;2;9')
                    if 'nrProcJud' in dir(infoPCD): validacoes_lista = validar_campo(validacoes_lista,'infoPCD.nrProcJud', infoPCD.nrProcJud.cdata, 0, u'')

    if 'alteracao' in dir(evtTabEstab.infoEstab):
        for alteracao in evtTabEstab.infoEstab.alteracao:

            if 'tpInsc' in dir(alteracao.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideEstab.tpInsc', alteracao.ideEstab.tpInsc.cdata, 1, u'1;3;4')
            if 'nrInsc' in dir(alteracao.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideEstab.nrInsc', alteracao.ideEstab.nrInsc.cdata, 1, u'')
            if 'iniValid' in dir(alteracao.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideEstab.iniValid', alteracao.ideEstab.iniValid.cdata, 1, u'')
            if 'fimValid' in dir(alteracao.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideEstab.fimValid', alteracao.ideEstab.fimValid.cdata, 0, u'')
            if 'cnaePrep' in dir(alteracao.dadosEstab): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosEstab.cnaePrep', alteracao.dadosEstab.cnaePrep.cdata, 1, u'')
            if 'aliqRat' in dir(alteracao.dadosEstab.aliqGilrat): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosEstab.aliqGilrat.aliqRat', alteracao.dadosEstab.aliqGilrat.aliqRat.cdata, 1, u'1;2;3')
            if 'fap' in dir(alteracao.dadosEstab.aliqGilrat): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosEstab.aliqGilrat.fap', alteracao.dadosEstab.aliqGilrat.fap.cdata, 0, u'')
            if 'aliqRatAjust' in dir(alteracao.dadosEstab.aliqGilrat): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosEstab.aliqGilrat.aliqRatAjust', alteracao.dadosEstab.aliqGilrat.aliqRatAjust.cdata, 0, u'')
            if 'regPt' in dir(alteracao.dadosEstab.infoTrab): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosEstab.infoTrab.regPt', alteracao.dadosEstab.infoTrab.regPt.cdata, 1, u'0;1;2;3;4;5;6')
            if 'contApr' in dir(alteracao.dadosEstab.infoTrab.infoApr): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosEstab.infoTrab.infoApr.contApr', alteracao.dadosEstab.infoTrab.infoApr.contApr.cdata, 1, u'0;1;2')
            if 'nrProcJud' in dir(alteracao.dadosEstab.infoTrab.infoApr): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosEstab.infoTrab.infoApr.nrProcJud', alteracao.dadosEstab.infoTrab.infoApr.nrProcJud.cdata, 0, u'')
            if 'contEntEd' in dir(alteracao.dadosEstab.infoTrab.infoApr): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosEstab.infoTrab.infoApr.contEntEd', alteracao.dadosEstab.infoTrab.infoApr.contEntEd.cdata, 0, u'S;N')

            if 'procAdmJudRat' in dir(alteracao.dadosEstab.aliqGilrat):
                for procAdmJudRat in alteracao.dadosEstab.aliqGilrat.procAdmJudRat:

                    if 'tpProc' in dir(procAdmJudRat): validacoes_lista = validar_campo(validacoes_lista,'procAdmJudRat.tpProc', procAdmJudRat.tpProc.cdata, 1, u'1;2')
                    if 'nrProc' in dir(procAdmJudRat): validacoes_lista = validar_campo(validacoes_lista,'procAdmJudRat.nrProc', procAdmJudRat.nrProc.cdata, 1, u'')
                    if 'codSusp' in dir(procAdmJudRat): validacoes_lista = validar_campo(validacoes_lista,'procAdmJudRat.codSusp', procAdmJudRat.codSusp.cdata, 1, u'')

            if 'procAdmJudFap' in dir(alteracao.dadosEstab.aliqGilrat):
                for procAdmJudFap in alteracao.dadosEstab.aliqGilrat.procAdmJudFap:

                    if 'tpProc' in dir(procAdmJudFap): validacoes_lista = validar_campo(validacoes_lista,'procAdmJudFap.tpProc', procAdmJudFap.tpProc.cdata, 1, u'1;2;4')
                    if 'nrProc' in dir(procAdmJudFap): validacoes_lista = validar_campo(validacoes_lista,'procAdmJudFap.nrProc', procAdmJudFap.nrProc.cdata, 1, u'')
                    if 'codSusp' in dir(procAdmJudFap): validacoes_lista = validar_campo(validacoes_lista,'procAdmJudFap.codSusp', procAdmJudFap.codSusp.cdata, 1, u'')

            if 'infoCaepf' in dir(alteracao.dadosEstab):
                for infoCaepf in alteracao.dadosEstab.infoCaepf:

                    if 'tpCaepf' in dir(infoCaepf): validacoes_lista = validar_campo(validacoes_lista,'infoCaepf.tpCaepf', infoCaepf.tpCaepf.cdata, 1, u'1;2;3')

            if 'infoObra' in dir(alteracao.dadosEstab):
                for infoObra in alteracao.dadosEstab.infoObra:

                    if 'indSubstPatrObra' in dir(infoObra): validacoes_lista = validar_campo(validacoes_lista,'infoObra.indSubstPatrObra', infoObra.indSubstPatrObra.cdata, 1, u'1;2')

            if 'infoEntEduc' in dir(alteracao.dadosEstab.infoTrab.infoApr):
                for infoEntEduc in alteracao.dadosEstab.infoTrab.infoApr.infoEntEduc:

                    if 'nrInsc' in dir(infoEntEduc): validacoes_lista = validar_campo(validacoes_lista,'infoEntEduc.nrInsc', infoEntEduc.nrInsc.cdata, 1, u'')

            if 'infoPCD' in dir(alteracao.dadosEstab.infoTrab):
                for infoPCD in alteracao.dadosEstab.infoTrab.infoPCD:

                    if 'contPCD' in dir(infoPCD): validacoes_lista = validar_campo(validacoes_lista,'infoPCD.contPCD', infoPCD.contPCD.cdata, 1, u'0;1;2;9')
                    if 'nrProcJud' in dir(infoPCD): validacoes_lista = validar_campo(validacoes_lista,'infoPCD.nrProcJud', infoPCD.nrProcJud.cdata, 0, u'')

            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:

                    if 'iniValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.iniValid', novaValidade.iniValid.cdata, 1, u'')
                    if 'fimValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.fimValid', novaValidade.fimValid.cdata, 0, u'')

    if 'exclusao' in dir(evtTabEstab.infoEstab):
        for exclusao in evtTabEstab.infoEstab.exclusao:

            if 'tpInsc' in dir(exclusao.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideEstab.tpInsc', exclusao.ideEstab.tpInsc.cdata, 1, u'1;3;4')
            if 'nrInsc' in dir(exclusao.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideEstab.nrInsc', exclusao.ideEstab.nrInsc.cdata, 1, u'')
            if 'iniValid' in dir(exclusao.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideEstab.iniValid', exclusao.ideEstab.iniValid.cdata, 1, u'')
            if 'fimValid' in dir(exclusao.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideEstab.fimValid', exclusao.ideEstab.fimValid.cdata, 0, u'')

    return validacoes_lista