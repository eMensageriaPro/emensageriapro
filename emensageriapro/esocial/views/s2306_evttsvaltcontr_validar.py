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
    #variaveis
    
    if 'ideEvento' in dir(evtTSVAltContr.ideEvento):
        for ideEvento in evtTSVAltContr.ideEvento:
            
            if 'indRetif' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.indRetif', 
                                                  ideEvento.indRetif.cdata, 
                                                  1, u'1, 2')
            
            if 'nrRecibo' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.nrRecibo', 
                                                  ideEvento.nrRecibo.cdata, 
                                                  0, u'None')
            
            if 'tpAmb' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.tpAmb', 
                                                  ideEvento.tpAmb.cdata, 
                                                  1, u'1, 2')
            
            if 'procEmi' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.procEmi', 
                                                  ideEvento.procEmi.cdata, 
                                                  1, u'1, 2, 3, 4, 5')
            
            if 'verProc' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.verProc', 
                                                  ideEvento.verProc.cdata, 
                                                  1, u'None')
    
    if 'ideEmpregador' in dir(evtTSVAltContr.ideEmpregador):
        for ideEmpregador in evtTSVAltContr.ideEmpregador:
            
            if 'tpInsc' in dir(ideEmpregador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEmpregador.tpInsc', 
                                                  ideEmpregador.tpInsc.cdata, 
                                                  1, u'1, 2, 3, 4, 5')
            
            if 'nrInsc' in dir(ideEmpregador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEmpregador.nrInsc', 
                                                  ideEmpregador.nrInsc.cdata, 
                                                  1, u'None')
    
    if 'ideTrabSemVinculo' in dir(evtTSVAltContr.ideTrabSemVinculo):
        for ideTrabSemVinculo in evtTSVAltContr.ideTrabSemVinculo:
            
            if 'cpfTrab' in dir(ideTrabSemVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideTrabSemVinculo.cpfTrab', 
                                                  ideTrabSemVinculo.cpfTrab.cdata, 
                                                  1, u'None')
            
            if 'nisTrab' in dir(ideTrabSemVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideTrabSemVinculo.nisTrab', 
                                                  ideTrabSemVinculo.nisTrab.cdata, 
                                                  0, u'None')
            
            if 'codCateg' in dir(ideTrabSemVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideTrabSemVinculo.codCateg', 
                                                  ideTrabSemVinculo.codCateg.cdata, 
                                                  1, u'101, 102, 103, 104, 105, 106, 111, 201, 202, 301, 302, 303, 305, 306, 307, 308, 309, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 751, 761, 771, 781, 901, 902, 903, 904, 905')
    
    if 'infoTSVAlteracao' in dir(evtTSVAltContr.infoTSVAlteracao):
        for infoTSVAlteracao in evtTSVAltContr.infoTSVAlteracao:
            
            if 'dtAlteracao' in dir(infoTSVAlteracao):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoTSVAlteracao.dtAlteracao', 
                                                  infoTSVAlteracao.dtAlteracao.cdata, 
                                                  1, u'None')
            
            if 'natAtividade' in dir(infoTSVAlteracao):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoTSVAlteracao.natAtividade', 
                                                  infoTSVAlteracao.natAtividade.cdata, 
                                                  0, u'1, 2')
            
            if 'infoComplementares' in dir(infoTSVAlteracao.infoComplementares):
                for infoComplementares in infoTSVAlteracao.infoComplementares:
                    
                    if 'cargoFuncao' in dir(infoComplementares.cargoFuncao):
                        for cargoFuncao in infoComplementares.cargoFuncao:
                            
                            if 'codCargo' in dir(cargoFuncao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'cargoFuncao.codCargo', 
                                                                  cargoFuncao.codCargo.cdata, 
                                                                  1, u'None')
                            
                            if 'codFuncao' in dir(cargoFuncao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'cargoFuncao.codFuncao', 
                                                                  cargoFuncao.codFuncao.cdata, 
                                                                  0, u'None')
                    
                    if 'remuneracao' in dir(infoComplementares.remuneracao):
                        for remuneracao in infoComplementares.remuneracao:
                            
                            if 'vrSalFx' in dir(remuneracao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'remuneracao.vrSalFx', 
                                                                  remuneracao.vrSalFx.cdata, 
                                                                  1, u'None')
                            
                            if 'undSalFixo' in dir(remuneracao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'remuneracao.undSalFixo', 
                                                                  remuneracao.undSalFixo.cdata, 
                                                                  1, u'1, 2, 3, 4, 5, 6, 7')
                            
                            if 'dscSalVar' in dir(remuneracao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'remuneracao.dscSalVar', 
                                                                  remuneracao.dscSalVar.cdata, 
                                                                  0, u'None')
                    
                    if 'infoTrabCedido' in dir(infoComplementares.infoTrabCedido):
                        for infoTrabCedido in infoComplementares.infoTrabCedido:
                            
                            if 'indRemunCargo' in dir(infoTrabCedido):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoTrabCedido.indRemunCargo', 
                                                                  infoTrabCedido.indRemunCargo.cdata, 
                                                                  1, u'None')
                    
                    if 'infoEstagiario' in dir(infoComplementares.infoEstagiario):
                        for infoEstagiario in infoComplementares.infoEstagiario:
                            
                            if 'natEstagio' in dir(infoEstagiario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstagiario.natEstagio', 
                                                                  infoEstagiario.natEstagio.cdata, 
                                                                  1, u'O, N')
                            
                            if 'nivEstagio' in dir(infoEstagiario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstagiario.nivEstagio', 
                                                                  infoEstagiario.nivEstagio.cdata, 
                                                                  1, u'1, 2, 3, 4, 8, 9')
                            
                            if 'areaAtuacao' in dir(infoEstagiario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstagiario.areaAtuacao', 
                                                                  infoEstagiario.areaAtuacao.cdata, 
                                                                  0, u'None')
                            
                            if 'nrApol' in dir(infoEstagiario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstagiario.nrApol', 
                                                                  infoEstagiario.nrApol.cdata, 
                                                                  0, u'None')
                            
                            if 'vlrBolsa' in dir(infoEstagiario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstagiario.vlrBolsa', 
                                                                  infoEstagiario.vlrBolsa.cdata, 
                                                                  0, u'None')
                            
                            if 'dtPrevTerm' in dir(infoEstagiario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstagiario.dtPrevTerm', 
                                                                  infoEstagiario.dtPrevTerm.cdata, 
                                                                  1, u'None')
                            
                            if 'instEnsino' in dir(infoEstagiario.instEnsino):
                                for instEnsino in infoEstagiario.instEnsino:
                                    
                                    if 'cnpjInstEnsino' in dir(instEnsino):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'instEnsino.cnpjInstEnsino', 
                                                                          instEnsino.cnpjInstEnsino.cdata, 
                                                                          0, u'None')
                                    
                                    if 'nmRazao' in dir(instEnsino):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'instEnsino.nmRazao', 
                                                                          instEnsino.nmRazao.cdata, 
                                                                          1, u'None')
                                    
                                    if 'dscLograd' in dir(instEnsino):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'instEnsino.dscLograd', 
                                                                          instEnsino.dscLograd.cdata, 
                                                                          0, u'None')
                                    
                                    if 'nrLograd' in dir(instEnsino):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'instEnsino.nrLograd', 
                                                                          instEnsino.nrLograd.cdata, 
                                                                          0, u'None')
                                    
                                    if 'bairro' in dir(instEnsino):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'instEnsino.bairro', 
                                                                          instEnsino.bairro.cdata, 
                                                                          0, u'None')
                                    
                                    if 'cep' in dir(instEnsino):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'instEnsino.cep', 
                                                                          instEnsino.cep.cdata, 
                                                                          0, u'None')
                                    
                                    if 'codMunic' in dir(instEnsino):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'instEnsino.codMunic', 
                                                                          instEnsino.codMunic.cdata, 
                                                                          0, u'None')
                                    
                                    if 'uf' in dir(instEnsino):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'instEnsino.uf', 
                                                                          instEnsino.uf.cdata, 
                                                                          0, u'None')
                            
                            if 'ageIntegracao' in dir(infoEstagiario.ageIntegracao):
                                for ageIntegracao in infoEstagiario.ageIntegracao:
                                    
                                    if 'cnpjAgntInteg' in dir(ageIntegracao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ageIntegracao.cnpjAgntInteg', 
                                                                          ageIntegracao.cnpjAgntInteg.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nmRazao' in dir(ageIntegracao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ageIntegracao.nmRazao', 
                                                                          ageIntegracao.nmRazao.cdata, 
                                                                          1, u'None')
                                    
                                    if 'dscLograd' in dir(ageIntegracao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ageIntegracao.dscLograd', 
                                                                          ageIntegracao.dscLograd.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nrLograd' in dir(ageIntegracao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ageIntegracao.nrLograd', 
                                                                          ageIntegracao.nrLograd.cdata, 
                                                                          1, u'None')
                                    
                                    if 'bairro' in dir(ageIntegracao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ageIntegracao.bairro', 
                                                                          ageIntegracao.bairro.cdata, 
                                                                          0, u'None')
                                    
                                    if 'cep' in dir(ageIntegracao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ageIntegracao.cep', 
                                                                          ageIntegracao.cep.cdata, 
                                                                          1, u'None')
                                    
                                    if 'codMunic' in dir(ageIntegracao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ageIntegracao.codMunic', 
                                                                          ageIntegracao.codMunic.cdata, 
                                                                          0, u'None')
                                    
                                    if 'uf' in dir(ageIntegracao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ageIntegracao.uf', 
                                                                          ageIntegracao.uf.cdata, 
                                                                          1, u'None')
                            
                            if 'supervisorEstagio' in dir(infoEstagiario.supervisorEstagio):
                                for supervisorEstagio in infoEstagiario.supervisorEstagio:
                                    
                                    if 'cpfSupervisor' in dir(supervisorEstagio):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'supervisorEstagio.cpfSupervisor', 
                                                                          supervisorEstagio.cpfSupervisor.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nmSuperv' in dir(supervisorEstagio):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'supervisorEstagio.nmSuperv', 
                                                                          supervisorEstagio.nmSuperv.cdata, 
                                                                          1, u'None')
    return validacoes_lista