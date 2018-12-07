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


def validacoes_s2306_evttsvaltcontr(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTSVAltContr = doc.eSocial.evtTSVAltContr

    if 'indRetif' in dir(evtTSVAltContr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideEvento.indRetif', evtTSVAltContr.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtTSVAltContr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideEvento.nrRecibo', evtTSVAltContr.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtTSVAltContr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideEvento.tpAmb', evtTSVAltContr.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtTSVAltContr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideEvento.procEmi', evtTSVAltContr.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtTSVAltContr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideEvento.verProc', evtTSVAltContr.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtTSVAltContr.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideEmpregador.tpInsc', evtTSVAltContr.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtTSVAltContr.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideEmpregador.nrInsc', evtTSVAltContr.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtTSVAltContr.ideTrabSemVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideTrabSemVinculo.cpfTrab', evtTSVAltContr.ideTrabSemVinculo.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtTSVAltContr.ideTrabSemVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideTrabSemVinculo.nisTrab', evtTSVAltContr.ideTrabSemVinculo.nisTrab.cdata, 0, '')
    if 'codCateg' in dir(evtTSVAltContr.ideTrabSemVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideTrabSemVinculo.codCateg', evtTSVAltContr.ideTrabSemVinculo.codCateg.cdata, 1, '101;102;103;104;105;106;111;201;202;301;302;303;305;306;307;308;309;401;410;701;711;712;721;722;723;731;734;738;741;751;761;771;781;901;902;903;904;905')
    if 'dtAlteracao' in dir(evtTSVAltContr.infoTSVAlteracao): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.infoTSVAlteracao.dtAlteracao', evtTSVAltContr.infoTSVAlteracao.dtAlteracao.cdata, 1, '')
    if 'natAtividade' in dir(evtTSVAltContr.infoTSVAlteracao): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.infoTSVAlteracao.natAtividade', evtTSVAltContr.infoTSVAlteracao.natAtividade.cdata, 0, '1;2')
    if 'cargoFuncao' in dir(evtTSVAltContr.infoTSVAlteracao.infoComplementares):
        for cargoFuncao in evtTSVAltContr.infoTSVAlteracao.infoComplementares.cargoFuncao:
       
            if 'codCargo' in dir(cargoFuncao): validacoes_lista = validar_campo(validacoes_lista,'cargoFuncao.codCargo', cargoFuncao.codCargo.cdata, 1, '')
            if 'codFuncao' in dir(cargoFuncao): validacoes_lista = validar_campo(validacoes_lista,'cargoFuncao.codFuncao', cargoFuncao.codFuncao.cdata, 0, '')

    if 'remuneracao' in dir(evtTSVAltContr.infoTSVAlteracao.infoComplementares):
        for remuneracao in evtTSVAltContr.infoTSVAlteracao.infoComplementares.remuneracao:
       
            if 'vrSalFx' in dir(remuneracao): validacoes_lista = validar_campo(validacoes_lista,'remuneracao.vrSalFx', remuneracao.vrSalFx.cdata, 1, '')
            if 'undSalFixo' in dir(remuneracao): validacoes_lista = validar_campo(validacoes_lista,'remuneracao.undSalFixo', remuneracao.undSalFixo.cdata, 1, '1;2;3;4;5;6;7')
            if 'dscSalVar' in dir(remuneracao): validacoes_lista = validar_campo(validacoes_lista,'remuneracao.dscSalVar', remuneracao.dscSalVar.cdata, 0, '')

    if 'infoTrabCedido' in dir(evtTSVAltContr.infoTSVAlteracao.infoComplementares):
        for infoTrabCedido in evtTSVAltContr.infoTSVAlteracao.infoComplementares.infoTrabCedido:
       
            if 'indRemunCargo' in dir(infoTrabCedido): validacoes_lista = validar_campo(validacoes_lista,'infoTrabCedido.indRemunCargo', infoTrabCedido.indRemunCargo.cdata, 1, 'S;N')

    if 'infoEstagiario' in dir(evtTSVAltContr.infoTSVAlteracao.infoComplementares):
        for infoEstagiario in evtTSVAltContr.infoTSVAlteracao.infoComplementares.infoEstagiario:
       
            if 'natEstagio' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.natEstagio', infoEstagiario.natEstagio.cdata, 1, 'O;N')
            if 'nivEstagio' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.nivEstagio', infoEstagiario.nivEstagio.cdata, 1, '1;2;3;4;8;9')
            if 'areaAtuacao' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.areaAtuacao', infoEstagiario.areaAtuacao.cdata, 0, '')
            if 'nrApol' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.nrApol', infoEstagiario.nrApol.cdata, 0, '')
            if 'vlrBolsa' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.vlrBolsa', infoEstagiario.vlrBolsa.cdata, 0, '')
            if 'dtPrevTerm' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.dtPrevTerm', infoEstagiario.dtPrevTerm.cdata, 1, '')
            if 'cnpjInstEnsino' in dir(infoEstagiario.instEnsino): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.instEnsino.cnpjInstEnsino', infoEstagiario.instEnsino.cnpjInstEnsino.cdata, 0, '')
            if 'nmRazao' in dir(infoEstagiario.instEnsino): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.instEnsino.nmRazao', infoEstagiario.instEnsino.nmRazao.cdata, 1, '')
            if 'dscLograd' in dir(infoEstagiario.instEnsino): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.instEnsino.dscLograd', infoEstagiario.instEnsino.dscLograd.cdata, 0, '')
            if 'nrLograd' in dir(infoEstagiario.instEnsino): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.instEnsino.nrLograd', infoEstagiario.instEnsino.nrLograd.cdata, 0, '')
            if 'bairro' in dir(infoEstagiario.instEnsino): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.instEnsino.bairro', infoEstagiario.instEnsino.bairro.cdata, 0, '')
            if 'cep' in dir(infoEstagiario.instEnsino): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.instEnsino.cep', infoEstagiario.instEnsino.cep.cdata, 0, '')
            if 'codMunic' in dir(infoEstagiario.instEnsino): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.instEnsino.codMunic', infoEstagiario.instEnsino.codMunic.cdata, 0, '')
            if 'uf' in dir(infoEstagiario.instEnsino): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.instEnsino.uf', infoEstagiario.instEnsino.uf.cdata, 0, '')

            if 'ageIntegracao' in dir(infoEstagiario):
                for ageIntegracao in infoEstagiario.ageIntegracao:
               
                    if 'cnpjAgntInteg' in dir(ageIntegracao): validacoes_lista = validar_campo(validacoes_lista,'ageIntegracao.cnpjAgntInteg', ageIntegracao.cnpjAgntInteg.cdata, 1, '')
                    if 'nmRazao' in dir(ageIntegracao): validacoes_lista = validar_campo(validacoes_lista,'ageIntegracao.nmRazao', ageIntegracao.nmRazao.cdata, 1, '')
                    if 'dscLograd' in dir(ageIntegracao): validacoes_lista = validar_campo(validacoes_lista,'ageIntegracao.dscLograd', ageIntegracao.dscLograd.cdata, 1, '')
                    if 'nrLograd' in dir(ageIntegracao): validacoes_lista = validar_campo(validacoes_lista,'ageIntegracao.nrLograd', ageIntegracao.nrLograd.cdata, 1, '')
                    if 'bairro' in dir(ageIntegracao): validacoes_lista = validar_campo(validacoes_lista,'ageIntegracao.bairro', ageIntegracao.bairro.cdata, 0, '')
                    if 'cep' in dir(ageIntegracao): validacoes_lista = validar_campo(validacoes_lista,'ageIntegracao.cep', ageIntegracao.cep.cdata, 1, '')
                    if 'codMunic' in dir(ageIntegracao): validacoes_lista = validar_campo(validacoes_lista,'ageIntegracao.codMunic', ageIntegracao.codMunic.cdata, 0, '')
                    if 'uf' in dir(ageIntegracao): validacoes_lista = validar_campo(validacoes_lista,'ageIntegracao.uf', ageIntegracao.uf.cdata, 1, '')
   
            if 'supervisorEstagio' in dir(infoEstagiario):
                for supervisorEstagio in infoEstagiario.supervisorEstagio:
               
                    if 'cpfSupervisor' in dir(supervisorEstagio): validacoes_lista = validar_campo(validacoes_lista,'supervisorEstagio.cpfSupervisor', supervisorEstagio.cpfSupervisor.cdata, 1, '')
                    if 'nmSuperv' in dir(supervisorEstagio): validacoes_lista = validar_campo(validacoes_lista,'supervisorEstagio.nmSuperv', supervisorEstagio.nmSuperv.cdata, 1, '')
   
    return validacoes_lista