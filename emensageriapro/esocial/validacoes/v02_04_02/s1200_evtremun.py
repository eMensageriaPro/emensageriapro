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


def validacoes_s1200_evtremun(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtRemun = doc.eSocial.evtRemun
    
    if 'indRetif' in dir(evtRemun.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRemun.ideEvento.indRetif', evtRemun.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtRemun.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRemun.ideEvento.nrRecibo', evtRemun.ideEvento.nrRecibo.cdata, 0, '')
    if 'indApuracao' in dir(evtRemun.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRemun.ideEvento.indApuracao', evtRemun.ideEvento.indApuracao.cdata, 1, '1;2')
    if 'perApur' in dir(evtRemun.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRemun.ideEvento.perApur', evtRemun.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtRemun.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRemun.ideEvento.tpAmb', evtRemun.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtRemun.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRemun.ideEvento.procEmi', evtRemun.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtRemun.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRemun.ideEvento.verProc', evtRemun.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtRemun.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtRemun.ideEmpregador.tpInsc', evtRemun.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtRemun.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtRemun.ideEmpregador.nrInsc', evtRemun.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtRemun.ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtRemun.ideTrabalhador.cpfTrab', evtRemun.ideTrabalhador.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtRemun.ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtRemun.ideTrabalhador.nisTrab', evtRemun.ideTrabalhador.nisTrab.cdata, 0, '')
    if 'infoMV' in dir(evtRemun.ideTrabalhador):
        for infoMV in evtRemun.ideTrabalhador.infoMV:
            
            if 'indMV' in dir(infoMV): validacoes_lista = validar_campo(validacoes_lista,'infoMV.indMV', infoMV.indMV.cdata, 1, '1;2;3')

            if 'remunOutrEmpr' in dir(infoMV):
                for remunOutrEmpr in infoMV.remunOutrEmpr:
                    
                    if 'tpInsc' in dir(remunOutrEmpr): validacoes_lista = validar_campo(validacoes_lista,'remunOutrEmpr.tpInsc', remunOutrEmpr.tpInsc.cdata, 1, '1;2;3;4')
                    if 'nrInsc' in dir(remunOutrEmpr): validacoes_lista = validar_campo(validacoes_lista,'remunOutrEmpr.nrInsc', remunOutrEmpr.nrInsc.cdata, 1, '')
                    if 'codCateg' in dir(remunOutrEmpr): validacoes_lista = validar_campo(validacoes_lista,'remunOutrEmpr.codCateg', remunOutrEmpr.codCateg.cdata, 1, '101;102;103;104;105;106;111;201;202;301;302;303;305;306;307;308;309;401;410;701;711;712;721;722;723;731;734;738;741;751;761;771;781;901;902;903;904;905')
                    if 'vlrRemunOE' in dir(remunOutrEmpr): validacoes_lista = validar_campo(validacoes_lista,'remunOutrEmpr.vlrRemunOE', remunOutrEmpr.vlrRemunOE.cdata, 1, '')
        
    if 'infoComplem' in dir(evtRemun.ideTrabalhador):
        for infoComplem in evtRemun.ideTrabalhador.infoComplem:
            
            if 'nmTrab' in dir(infoComplem): validacoes_lista = validar_campo(validacoes_lista,'infoComplem.nmTrab', infoComplem.nmTrab.cdata, 1, '')
            if 'dtNascto' in dir(infoComplem): validacoes_lista = validar_campo(validacoes_lista,'infoComplem.dtNascto', infoComplem.dtNascto.cdata, 1, '')

            if 'sucessaoVinc' in dir(infoComplem):
                for sucessaoVinc in infoComplem.sucessaoVinc:
                    
                    if 'cnpjEmpregAnt' in dir(sucessaoVinc): validacoes_lista = validar_campo(validacoes_lista,'sucessaoVinc.cnpjEmpregAnt', sucessaoVinc.cnpjEmpregAnt.cdata, 1, '')
                    if 'matricAnt' in dir(sucessaoVinc): validacoes_lista = validar_campo(validacoes_lista,'sucessaoVinc.matricAnt', sucessaoVinc.matricAnt.cdata, 0, '')
                    if 'dtAdm' in dir(sucessaoVinc): validacoes_lista = validar_campo(validacoes_lista,'sucessaoVinc.dtAdm', sucessaoVinc.dtAdm.cdata, 1, '')
                    if 'observacao' in dir(sucessaoVinc): validacoes_lista = validar_campo(validacoes_lista,'sucessaoVinc.observacao', sucessaoVinc.observacao.cdata, 0, '')
        
    if 'procJudTrab' in dir(evtRemun.ideTrabalhador):
        for procJudTrab in evtRemun.ideTrabalhador.procJudTrab:
            
            if 'tpTrib' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.tpTrib', procJudTrab.tpTrib.cdata, 1, '1;2;3;4')
            if 'nrProcJud' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.nrProcJud', procJudTrab.nrProcJud.cdata, 1, '')
            if 'codSusp' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.codSusp', procJudTrab.codSusp.cdata, 0, '')

    if 'infoInterm' in dir(evtRemun.ideTrabalhador):
        for infoInterm in evtRemun.ideTrabalhador.infoInterm:
            
            if 'qtdDiasInterm' in dir(infoInterm): validacoes_lista = validar_campo(validacoes_lista,'infoInterm.qtdDiasInterm', infoInterm.qtdDiasInterm.cdata, 1, '')

    if 'dmDev' in dir(evtRemun):
        for dmDev in evtRemun.dmDev:
            
            if 'ideDmDev' in dir(dmDev): validacoes_lista = validar_campo(validacoes_lista,'dmDev.ideDmDev', dmDev.ideDmDev.cdata, 1, '')
            if 'codCateg' in dir(dmDev): validacoes_lista = validar_campo(validacoes_lista,'dmDev.codCateg', dmDev.codCateg.cdata, 1, '101;102;103;104;105;106;111;201;202;301;302;303;305;306;307;308;309;401;410;701;711;712;721;722;723;731;734;738;741;751;761;771;781;901;902;903;904;905')

            if 'infoPerApur' in dir(dmDev):
                for infoPerApur in dmDev.infoPerApur:
                    
        
            if 'infoPerAnt' in dir(dmDev):
                for infoPerAnt in dmDev.infoPerAnt:
                    
        
            if 'infoComplCont' in dir(dmDev):
                for infoComplCont in dmDev.infoComplCont:
                    
                    if 'codCBO' in dir(infoComplCont): validacoes_lista = validar_campo(validacoes_lista,'infoComplCont.codCBO', infoComplCont.codCBO.cdata, 1, '')
                    if 'natAtividade' in dir(infoComplCont): validacoes_lista = validar_campo(validacoes_lista,'infoComplCont.natAtividade', infoComplCont.natAtividade.cdata, 0, '')
                    if 'qtdDiasTrab' in dir(infoComplCont): validacoes_lista = validar_campo(validacoes_lista,'infoComplCont.qtdDiasTrab', infoComplCont.qtdDiasTrab.cdata, 0, '')
        
    return validacoes_lista