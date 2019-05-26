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


def validacoes_s2206_evtaltcontratual(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtAltContratual = doc.eSocial.evtAltContratual
    #variaveis
    
    if 'ideEvento' in dir(evtAltContratual.ideEvento):
        for ideEvento in evtAltContratual.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtAltContratual.ideEmpregador):
        for ideEmpregador in evtAltContratual.ideEmpregador:
            
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
    
    if 'ideVinculo' in dir(evtAltContratual.ideVinculo):
        for ideVinculo in evtAltContratual.ideVinculo:
            
            if 'cpfTrab' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.cpfTrab', 
                                                  ideVinculo.cpfTrab.cdata, 
                                                  1, u'None')
            
            if 'nisTrab' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.nisTrab', 
                                                  ideVinculo.nisTrab.cdata, 
                                                  1, u'None')
            
            if 'matricula' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.matricula', 
                                                  ideVinculo.matricula.cdata, 
                                                  1, u'None')
    
    if 'altContratual' in dir(evtAltContratual.altContratual):
        for altContratual in evtAltContratual.altContratual:
            
            if 'dtAlteracao' in dir(altContratual):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'altContratual.dtAlteracao', 
                                                  altContratual.dtAlteracao.cdata, 
                                                  1, u'None')
            
            if 'dtEf' in dir(altContratual):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'altContratual.dtEf', 
                                                  altContratual.dtEf.cdata, 
                                                  0, u'None')
            
            if 'dscAlt' in dir(altContratual):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'altContratual.dscAlt', 
                                                  altContratual.dscAlt.cdata, 
                                                  0, u'None')
            
            if 'vinculo' in dir(altContratual.vinculo):
                for vinculo in altContratual.vinculo:
                    
                    if 'tpRegPrev' in dir(vinculo):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'vinculo.tpRegPrev', 
                                                          vinculo.tpRegPrev.cdata, 
                                                          1, u'1, 2, 3')
            
            if 'infoRegimeTrab' in dir(altContratual.infoRegimeTrab):
                for infoRegimeTrab in altContratual.infoRegimeTrab:
                    
                    if 'infoCeletista' in dir(infoRegimeTrab.infoCeletista):
                        for infoCeletista in infoRegimeTrab.infoCeletista:
                            
                            if 'tpRegJor' in dir(infoCeletista):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCeletista.tpRegJor', 
                                                                  infoCeletista.tpRegJor.cdata, 
                                                                  1, u'1, 2, 3, 4')
                            
                            if 'natAtividade' in dir(infoCeletista):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCeletista.natAtividade', 
                                                                  infoCeletista.natAtividade.cdata, 
                                                                  1, u'1, 2')
                            
                            if 'dtBase' in dir(infoCeletista):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCeletista.dtBase', 
                                                                  infoCeletista.dtBase.cdata, 
                                                                  0, u'None')
                            
                            if 'cnpjSindCategProf' in dir(infoCeletista):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCeletista.cnpjSindCategProf', 
                                                                  infoCeletista.cnpjSindCategProf.cdata, 
                                                                  1, u'None')
                            
                            if 'trabTemp' in dir(infoCeletista.trabTemp):
                                for trabTemp in infoCeletista.trabTemp:
                                    
                                    if 'justProrr' in dir(trabTemp):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'trabTemp.justProrr', 
                                                                          trabTemp.justProrr.cdata, 
                                                                          1, u'None')
                            
                            if 'aprend' in dir(infoCeletista.aprend):
                                for aprend in infoCeletista.aprend:
                                    
                                    if 'tpInsc' in dir(aprend):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'aprend.tpInsc', 
                                                                          aprend.tpInsc.cdata, 
                                                                          1, u'1, 2, 3, 4, 5')
                                    
                                    if 'nrInsc' in dir(aprend):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'aprend.nrInsc', 
                                                                          aprend.nrInsc.cdata, 
                                                                          1, u'None')
                    
                    if 'infoEstatutario' in dir(infoRegimeTrab.infoEstatutario):
                        for infoEstatutario in infoRegimeTrab.infoEstatutario:
                            
                            if 'tpPlanRP' in dir(infoEstatutario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstatutario.tpPlanRP', 
                                                                  infoEstatutario.tpPlanRP.cdata, 
                                                                  1, u'1, 2')
                            
                            if 'indTetoRGPS' in dir(infoEstatutario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstatutario.indTetoRGPS', 
                                                                  infoEstatutario.indTetoRGPS.cdata, 
                                                                  0, u'S, N')
                            
                            if 'indAbonoPerm' in dir(infoEstatutario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstatutario.indAbonoPerm', 
                                                                  infoEstatutario.indAbonoPerm.cdata, 
                                                                  0, u'S, N')
                            
                            if 'indParcRemun' in dir(infoEstatutario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstatutario.indParcRemun', 
                                                                  infoEstatutario.indParcRemun.cdata, 
                                                                  0, u'S, N')
            
            if 'infoContrato' in dir(altContratual.infoContrato):
                for infoContrato in altContratual.infoContrato:
                    
                    if 'codCargo' in dir(infoContrato):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoContrato.codCargo', 
                                                          infoContrato.codCargo.cdata, 
                                                          0, u'None')
                    
                    if 'codFuncao' in dir(infoContrato):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoContrato.codFuncao', 
                                                          infoContrato.codFuncao.cdata, 
                                                          0, u'None')
                    
                    if 'codCateg' in dir(infoContrato):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoContrato.codCateg', 
                                                          infoContrato.codCateg.cdata, 
                                                          1, u'None')
                    
                    if 'codCarreira' in dir(infoContrato):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoContrato.codCarreira', 
                                                          infoContrato.codCarreira.cdata, 
                                                          0, u'None')
                    
                    if 'dtIngrCarr' in dir(infoContrato):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoContrato.dtIngrCarr', 
                                                          infoContrato.dtIngrCarr.cdata, 
                                                          0, u'None')
                    
                    if 'remuneracao' in dir(infoContrato.remuneracao):
                        for remuneracao in infoContrato.remuneracao:
                            
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
                    
                    if 'duracao' in dir(infoContrato.duracao):
                        for duracao in infoContrato.duracao:
                            
                            if 'tpContr' in dir(duracao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'duracao.tpContr', 
                                                                  duracao.tpContr.cdata, 
                                                                  1, u'1, 2, 3')
                            
                            if 'dtTerm' in dir(duracao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'duracao.dtTerm', 
                                                                  duracao.dtTerm.cdata, 
                                                                  0, u'None')
                            
                            if 'objDet' in dir(duracao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'duracao.objDet', 
                                                                  duracao.objDet.cdata, 
                                                                  0, u'None')
                    
                    if 'localTrabalho' in dir(infoContrato.localTrabalho):
                        for localTrabalho in infoContrato.localTrabalho:
                            
                            if 'localTrabGeral' in dir(localTrabalho.localTrabGeral):
                                for localTrabGeral in localTrabalho.localTrabGeral:
                                    
                                    if 'tpInsc' in dir(localTrabGeral):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabGeral.tpInsc', 
                                                                          localTrabGeral.tpInsc.cdata, 
                                                                          1, u'1, 2, 3, 4, 5')
                                    
                                    if 'nrInsc' in dir(localTrabGeral):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabGeral.nrInsc', 
                                                                          localTrabGeral.nrInsc.cdata, 
                                                                          1, u'None')
                                    
                                    if 'descComp' in dir(localTrabGeral):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabGeral.descComp', 
                                                                          localTrabGeral.descComp.cdata, 
                                                                          0, u'None')
                            
                            if 'localTrabDom' in dir(localTrabalho.localTrabDom):
                                for localTrabDom in localTrabalho.localTrabDom:
                                    
                                    if 'tpLograd' in dir(localTrabDom):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabDom.tpLograd', 
                                                                          localTrabDom.tpLograd.cdata, 
                                                                          1, u'None')
                                    
                                    if 'dscLograd' in dir(localTrabDom):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabDom.dscLograd', 
                                                                          localTrabDom.dscLograd.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nrLograd' in dir(localTrabDom):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabDom.nrLograd', 
                                                                          localTrabDom.nrLograd.cdata, 
                                                                          1, u'None')
                                    
                                    if 'complemento' in dir(localTrabDom):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabDom.complemento', 
                                                                          localTrabDom.complemento.cdata, 
                                                                          0, u'None')
                                    
                                    if 'bairro' in dir(localTrabDom):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabDom.bairro', 
                                                                          localTrabDom.bairro.cdata, 
                                                                          0, u'None')
                                    
                                    if 'cep' in dir(localTrabDom):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabDom.cep', 
                                                                          localTrabDom.cep.cdata, 
                                                                          1, u'None')
                                    
                                    if 'codMunic' in dir(localTrabDom):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabDom.codMunic', 
                                                                          localTrabDom.codMunic.cdata, 
                                                                          1, u'None')
                                    
                                    if 'uf' in dir(localTrabDom):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabDom.uf', 
                                                                          localTrabDom.uf.cdata, 
                                                                          1, u'None')
                    
                    if 'horContratual' in dir(infoContrato.horContratual):
                        for horContratual in infoContrato.horContratual:
                            
                            if 'qtdHrsSem' in dir(horContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'horContratual.qtdHrsSem', 
                                                                  horContratual.qtdHrsSem.cdata, 
                                                                  0, u'None')
                            
                            if 'tpJornada' in dir(horContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'horContratual.tpJornada', 
                                                                  horContratual.tpJornada.cdata, 
                                                                  1, u'1, 2, 3, 9')
                            
                            if 'dscTpJorn' in dir(horContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'horContratual.dscTpJorn', 
                                                                  horContratual.dscTpJorn.cdata, 
                                                                  0, u'None')
                            
                            if 'tmpParc' in dir(horContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'horContratual.tmpParc', 
                                                                  horContratual.tmpParc.cdata, 
                                                                  1, u'0, 1, 2, 3')
                            
                            if 'horario' in dir(horContratual.horario):
                                for horario in horContratual.horario:
                                    
                                    if 'dia' in dir(horario):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'horario.dia', 
                                                                          horario.dia.cdata, 
                                                                          1, u'1, 2, 3, 4, 5, 6, 7, 8')
                                    
                                    if 'codHorContrat' in dir(horario):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'horario.codHorContrat', 
                                                                          horario.codHorContrat.cdata, 
                                                                          1, u'None')
                    
                    if 'filiacaoSindical' in dir(infoContrato.filiacaoSindical):
                        for filiacaoSindical in infoContrato.filiacaoSindical:
                            
                            if 'cnpjSindTrab' in dir(filiacaoSindical):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'filiacaoSindical.cnpjSindTrab', 
                                                                  filiacaoSindical.cnpjSindTrab.cdata, 
                                                                  1, u'None')
                    
                    if 'alvaraJudicial' in dir(infoContrato.alvaraJudicial):
                        for alvaraJudicial in infoContrato.alvaraJudicial:
                            
                            if 'nrProcJud' in dir(alvaraJudicial):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'alvaraJudicial.nrProcJud', 
                                                                  alvaraJudicial.nrProcJud.cdata, 
                                                                  1, u'None')
                    
                    if 'observacoes' in dir(infoContrato.observacoes):
                        for observacoes in infoContrato.observacoes:
                            
                            if 'observacao' in dir(observacoes):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'observacoes.observacao', 
                                                                  observacoes.observacao.cdata, 
                                                                  1, u'None')
                    
                    if 'servPubl' in dir(infoContrato.servPubl):
                        for servPubl in infoContrato.servPubl:
                            
                            if 'mtvAlter' in dir(servPubl):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'servPubl.mtvAlter', 
                                                                  servPubl.mtvAlter.cdata, 
                                                                  1, u'1, 2, 3, 8, 9')
    return validacoes_lista