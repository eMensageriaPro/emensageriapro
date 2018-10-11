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


def validacoes_r1070_evttabprocesso(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtTabProcesso = doc.Reinf.evtTabProcesso
    
    if 'tpAmb' in dir(evtTabProcesso.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabProcesso.ideEvento.tpAmb', evtTabProcesso.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtTabProcesso.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabProcesso.ideEvento.procEmi', evtTabProcesso.ideEvento.procEmi.cdata, 1, '1;2')
    if 'verProc' in dir(evtTabProcesso.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabProcesso.ideEvento.verProc', evtTabProcesso.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtTabProcesso.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtTabProcesso.ideContri.tpInsc', evtTabProcesso.ideContri.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtTabProcesso.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtTabProcesso.ideContri.nrInsc', evtTabProcesso.ideContri.nrInsc.cdata, 1, '')
    if 'inclusao' in dir(evtTabProcesso.infoProcesso):
        for inclusao in evtTabProcesso.infoProcesso.inclusao:
            
            if 'tpProc' in dir(inclusao.ideProcesso): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideProcesso.tpProc', inclusao.ideProcesso.tpProc.cdata, 1, '1;2')
            if 'nrProc' in dir(inclusao.ideProcesso): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideProcesso.nrProc', inclusao.ideProcesso.nrProc.cdata, 1, '')
            if 'iniValid' in dir(inclusao.ideProcesso): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideProcesso.iniValid', inclusao.ideProcesso.iniValid.cdata, 1, '')
            if 'fimValid' in dir(inclusao.ideProcesso): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideProcesso.fimValid', inclusao.ideProcesso.fimValid.cdata, 0, '')
            if 'indAutoria' in dir(inclusao.ideProcesso): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideProcesso.indAutoria', inclusao.ideProcesso.indAutoria.cdata, 1, '1;2')


            if 'infoSusp' in dir(inclusao.ideProcesso):
                for infoSusp in inclusao.ideProcesso.infoSusp:
                    
                    if 'codSusp' in dir(infoSusp): validacoes_lista = validar_campo(validacoes_lista,'infoSusp.codSusp', infoSusp.codSusp.cdata, 0, '')
                    if 'indSusp' in dir(infoSusp): validacoes_lista = validar_campo(validacoes_lista,'infoSusp.indSusp', infoSusp.indSusp.cdata, 1, '01;02;03;04;05;08;09;10;11;12;13;90;92')
                    if 'dtDecisao' in dir(infoSusp): validacoes_lista = validar_campo(validacoes_lista,'infoSusp.dtDecisao', infoSusp.dtDecisao.cdata, 1, '')
                    if 'indDeposito' in dir(infoSusp): validacoes_lista = validar_campo(validacoes_lista,'infoSusp.indDeposito', infoSusp.indDeposito.cdata, 1, 'S;N')
        
        
            if 'dadosProcJud' in dir(inclusao.ideProcesso):
                for dadosProcJud in inclusao.ideProcesso.dadosProcJud:
                    
                    if 'ufVara' in dir(dadosProcJud): validacoes_lista = validar_campo(validacoes_lista,'dadosProcJud.ufVara', dadosProcJud.ufVara.cdata, 1, '')
                    if 'codMunic' in dir(dadosProcJud): validacoes_lista = validar_campo(validacoes_lista,'dadosProcJud.codMunic', dadosProcJud.codMunic.cdata, 1, '')
                    if 'idVara' in dir(dadosProcJud): validacoes_lista = validar_campo(validacoes_lista,'dadosProcJud.idVara', dadosProcJud.idVara.cdata, 1, '')
        
        
    if 'alteracao' in dir(evtTabProcesso.infoProcesso):
        for alteracao in evtTabProcesso.infoProcesso.alteracao:
            
            if 'tpProc' in dir(alteracao.ideProcesso): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideProcesso.tpProc', alteracao.ideProcesso.tpProc.cdata, 1, '1;2')
            if 'nrProc' in dir(alteracao.ideProcesso): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideProcesso.nrProc', alteracao.ideProcesso.nrProc.cdata, 1, '')
            if 'iniValid' in dir(alteracao.ideProcesso): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideProcesso.iniValid', alteracao.ideProcesso.iniValid.cdata, 1, '')
            if 'fimValid' in dir(alteracao.ideProcesso): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideProcesso.fimValid', alteracao.ideProcesso.fimValid.cdata, 0, '')
            if 'indAutoria' in dir(alteracao.ideProcesso): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideProcesso.indAutoria', alteracao.ideProcesso.indAutoria.cdata, 1, '1;2')


            if 'infoSusp' in dir(alteracao.ideProcesso):
                for infoSusp in alteracao.ideProcesso.infoSusp:
                    
                    if 'codSusp' in dir(infoSusp): validacoes_lista = validar_campo(validacoes_lista,'infoSusp.codSusp', infoSusp.codSusp.cdata, 0, '')
                    if 'indSusp' in dir(infoSusp): validacoes_lista = validar_campo(validacoes_lista,'infoSusp.indSusp', infoSusp.indSusp.cdata, 1, '01;02;03;04;05;08;09;10;11;12;13;90;92')
                    if 'dtDecisao' in dir(infoSusp): validacoes_lista = validar_campo(validacoes_lista,'infoSusp.dtDecisao', infoSusp.dtDecisao.cdata, 1, '')
                    if 'indDeposito' in dir(infoSusp): validacoes_lista = validar_campo(validacoes_lista,'infoSusp.indDeposito', infoSusp.indDeposito.cdata, 1, 'S;N')
        
        
            if 'dadosProcJud' in dir(alteracao.ideProcesso):
                for dadosProcJud in alteracao.ideProcesso.dadosProcJud:
                    
                    if 'ufVara' in dir(dadosProcJud): validacoes_lista = validar_campo(validacoes_lista,'dadosProcJud.ufVara', dadosProcJud.ufVara.cdata, 1, '')
                    if 'codMunic' in dir(dadosProcJud): validacoes_lista = validar_campo(validacoes_lista,'dadosProcJud.codMunic', dadosProcJud.codMunic.cdata, 1, '')
                    if 'idVara' in dir(dadosProcJud): validacoes_lista = validar_campo(validacoes_lista,'dadosProcJud.idVara', dadosProcJud.idVara.cdata, 1, '')
        
        
            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    
                    if 'iniValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.iniValid', novaValidade.iniValid.cdata, 1, '')
                    if 'fimValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.fimValid', novaValidade.fimValid.cdata, 0, '')
        
        
    if 'exclusao' in dir(evtTabProcesso.infoProcesso):
        for exclusao in evtTabProcesso.infoProcesso.exclusao:
            
            if 'tpProc' in dir(exclusao.ideProcesso): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideProcesso.tpProc', exclusao.ideProcesso.tpProc.cdata, 1, '1;2')
            if 'nrProc' in dir(exclusao.ideProcesso): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideProcesso.nrProc', exclusao.ideProcesso.nrProc.cdata, 1, '')
            if 'iniValid' in dir(exclusao.ideProcesso): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideProcesso.iniValid', exclusao.ideProcesso.iniValid.cdata, 1, '')
            if 'fimValid' in dir(exclusao.ideProcesso): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideProcesso.fimValid', exclusao.ideProcesso.fimValid.cdata, 0, '')


    return validacoes_lista