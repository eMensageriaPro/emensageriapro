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


def validacoes_r3010_evtespdesportivo(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtEspDesportivo = doc.Reinf.evtEspDesportivo

    if 'indRetif' in dir(evtEspDesportivo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideEvento.indRetif', evtEspDesportivo.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtEspDesportivo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideEvento.nrRecibo', evtEspDesportivo.ideEvento.nrRecibo.cdata, 0, '')
    if 'dtApuracao' in dir(evtEspDesportivo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideEvento.dtApuracao', evtEspDesportivo.ideEvento.dtApuracao.cdata, 1, '')
    if 'tpAmb' in dir(evtEspDesportivo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideEvento.tpAmb', evtEspDesportivo.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtEspDesportivo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideEvento.procEmi', evtEspDesportivo.ideEvento.procEmi.cdata, 1, '1;2')
    if 'verProc' in dir(evtEspDesportivo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideEvento.verProc', evtEspDesportivo.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtEspDesportivo.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideContri.tpInsc', evtEspDesportivo.ideContri.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtEspDesportivo.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideContri.nrInsc', evtEspDesportivo.ideContri.nrInsc.cdata, 1, '')
    if 'tpInscEstab' in dir(evtEspDesportivo.ideContri.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideContri.ideEstab.tpInscEstab', evtEspDesportivo.ideContri.ideEstab.tpInscEstab.cdata, 1, '1')
    if 'nrInscEstab' in dir(evtEspDesportivo.ideContri.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideContri.ideEstab.nrInscEstab', evtEspDesportivo.ideContri.ideEstab.nrInscEstab.cdata, 1, '')
    if 'vlrReceitaTotal' in dir(evtEspDesportivo.ideContri.ideEstab.receitaTotal): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrReceitaTotal', evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrReceitaTotal.cdata, 1, '')
    if 'vlrCP' in dir(evtEspDesportivo.ideContri.ideEstab.receitaTotal): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrCP', evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrCP.cdata, 1, '')
    if 'vlrCPSuspTotal' in dir(evtEspDesportivo.ideContri.ideEstab.receitaTotal): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrCPSuspTotal', evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrCPSuspTotal.cdata, 0, '')
    if 'vlrReceitaClubes' in dir(evtEspDesportivo.ideContri.ideEstab.receitaTotal): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrReceitaClubes', evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrReceitaClubes.cdata, 1, '')
    if 'vlrRetParc' in dir(evtEspDesportivo.ideContri.ideEstab.receitaTotal): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrRetParc', evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrRetParc.cdata, 1, '')
    if 'boletim' in dir(evtEspDesportivo.ideContri.ideEstab):
        for boletim in evtEspDesportivo.ideContri.ideEstab.boletim:
       
            if 'nrBoletim' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.nrBoletim', boletim.nrBoletim.cdata, 1, '')
            if 'tpCompeticao' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.tpCompeticao', boletim.tpCompeticao.cdata, 1, '1;2')
            if 'categEvento' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.categEvento', boletim.categEvento.cdata, 1, '1;2;3;4')
            if 'modDesportiva' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.modDesportiva', boletim.modDesportiva.cdata, 1, '')
            if 'nomeCompeticao' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.nomeCompeticao', boletim.nomeCompeticao.cdata, 1, '')
            if 'cnpjMandante' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.cnpjMandante', boletim.cnpjMandante.cdata, 1, '')
            if 'cnpjVisitante' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.cnpjVisitante', boletim.cnpjVisitante.cdata, 0, '')
            if 'nomeVisitante' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.nomeVisitante', boletim.nomeVisitante.cdata, 0, '')
            if 'pracaDesportiva' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.pracaDesportiva', boletim.pracaDesportiva.cdata, 1, '')
            if 'codMunic' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.codMunic', boletim.codMunic.cdata, 0, '')
            if 'uf' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.uf', boletim.uf.cdata, 1, '')
            if 'qtdePagantes' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.qtdePagantes', boletim.qtdePagantes.cdata, 1, '')
            if 'qtdeNaoPagantes' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.qtdeNaoPagantes', boletim.qtdeNaoPagantes.cdata, 1, '')

            if 'receitaIngressos' in dir(boletim):
                for receitaIngressos in boletim.receitaIngressos:
               
                    if 'tpIngresso' in dir(receitaIngressos): validacoes_lista = validar_campo(validacoes_lista,'receitaIngressos.tpIngresso', receitaIngressos.tpIngresso.cdata, 1, '1;2;3;4')
                    if 'descIngr' in dir(receitaIngressos): validacoes_lista = validar_campo(validacoes_lista,'receitaIngressos.descIngr', receitaIngressos.descIngr.cdata, 1, '')
                    if 'qtdeIngrVenda' in dir(receitaIngressos): validacoes_lista = validar_campo(validacoes_lista,'receitaIngressos.qtdeIngrVenda', receitaIngressos.qtdeIngrVenda.cdata, 1, '')
                    if 'qtdeIngrVendidos' in dir(receitaIngressos): validacoes_lista = validar_campo(validacoes_lista,'receitaIngressos.qtdeIngrVendidos', receitaIngressos.qtdeIngrVendidos.cdata, 1, '')
                    if 'qtdeIngrDev' in dir(receitaIngressos): validacoes_lista = validar_campo(validacoes_lista,'receitaIngressos.qtdeIngrDev', receitaIngressos.qtdeIngrDev.cdata, 1, '')
                    if 'precoIndiv' in dir(receitaIngressos): validacoes_lista = validar_campo(validacoes_lista,'receitaIngressos.precoIndiv', receitaIngressos.precoIndiv.cdata, 1, '')
                    if 'vlrTotal' in dir(receitaIngressos): validacoes_lista = validar_campo(validacoes_lista,'receitaIngressos.vlrTotal', receitaIngressos.vlrTotal.cdata, 1, '')
   
            if 'outrasReceitas' in dir(boletim):
                for outrasReceitas in boletim.outrasReceitas:
               
                    if 'tpReceita' in dir(outrasReceitas): validacoes_lista = validar_campo(validacoes_lista,'outrasReceitas.tpReceita', outrasReceitas.tpReceita.cdata, 1, '1;2;3;4;5')
                    if 'vlrReceita' in dir(outrasReceitas): validacoes_lista = validar_campo(validacoes_lista,'outrasReceitas.vlrReceita', outrasReceitas.vlrReceita.cdata, 1, '')
                    if 'descReceita' in dir(outrasReceitas): validacoes_lista = validar_campo(validacoes_lista,'outrasReceitas.descReceita', outrasReceitas.descReceita.cdata, 1, '')
   
    if 'infoProc' in dir(evtEspDesportivo.ideContri.ideEstab.receitaTotal):
        for infoProc in evtEspDesportivo.ideContri.ideEstab.receitaTotal.infoProc:
       
            if 'tpProc' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.tpProc', infoProc.tpProc.cdata, 1, '1;2')
            if 'nrProc' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.nrProc', infoProc.nrProc.cdata, 1, '')
            if 'codSusp' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.codSusp', infoProc.codSusp.cdata, 0, '')
            if 'vlrCPSusp' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.vlrCPSusp', infoProc.vlrCPSusp.cdata, 1, '')

    return validacoes_lista