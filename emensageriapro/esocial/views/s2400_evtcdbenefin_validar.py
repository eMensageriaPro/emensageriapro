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


def validacoes_s2400_evtcdbenefin(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtCdBenefIn = doc.eSocial.evtCdBenefIn
    #variaveis
    
    if 'ideEvento' in dir(evtCdBenefIn.ideEvento):
        for ideEvento in evtCdBenefIn.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtCdBenefIn.ideEmpregador):
        for ideEmpregador in evtCdBenefIn.ideEmpregador:
            
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
    
    if 'beneficiario' in dir(evtCdBenefIn.beneficiario):
        for beneficiario in evtCdBenefIn.beneficiario:
            
            if 'cpfBenef' in dir(beneficiario):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'beneficiario.cpfBenef', 
                                                  beneficiario.cpfBenef.cdata, 
                                                  1, u'None')
            
            if 'nisBenef' in dir(beneficiario):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'beneficiario.nisBenef', 
                                                  beneficiario.nisBenef.cdata, 
                                                  0, u'None')
            
            if 'nmBenefic' in dir(beneficiario):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'beneficiario.nmBenefic', 
                                                  beneficiario.nmBenefic.cdata, 
                                                  1, u'None')
            
            if 'dtInicio' in dir(beneficiario):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'beneficiario.dtInicio', 
                                                  beneficiario.dtInicio.cdata, 
                                                  1, u'None')
            
            if 'sexo' in dir(beneficiario):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'beneficiario.sexo', 
                                                  beneficiario.sexo.cdata, 
                                                  1, u'M, F')
            
            if 'racaCor' in dir(beneficiario):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'beneficiario.racaCor', 
                                                  beneficiario.racaCor.cdata, 
                                                  1, u'1, 2, 3, 4, 5, 6')
            
            if 'estCiv' in dir(beneficiario):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'beneficiario.estCiv', 
                                                  beneficiario.estCiv.cdata, 
                                                  0, u'1, 2, 3, 4, 5')
            
            if 'incFisMen' in dir(beneficiario):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'beneficiario.incFisMen', 
                                                  beneficiario.incFisMen.cdata, 
                                                  1, u'S, N')
            
            if 'dtIncFisMen' in dir(beneficiario):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'beneficiario.dtIncFisMen', 
                                                  beneficiario.dtIncFisMen.cdata, 
                                                  0, u'None')
            
            if 'dadosNasc' in dir(beneficiario.dadosNasc):
                for dadosNasc in beneficiario.dadosNasc:
                    
                    if 'dtNascto' in dir(dadosNasc):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosNasc.dtNascto', 
                                                          dadosNasc.dtNascto.cdata, 
                                                          1, u'None')
                    
                    if 'codMunic' in dir(dadosNasc):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosNasc.codMunic', 
                                                          dadosNasc.codMunic.cdata, 
                                                          0, u'None')
                    
                    if 'uf' in dir(dadosNasc):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosNasc.uf', 
                                                          dadosNasc.uf.cdata, 
                                                          0, u'None')
                    
                    if 'paisNascto' in dir(dadosNasc):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosNasc.paisNascto', 
                                                          dadosNasc.paisNascto.cdata, 
                                                          0, u'None')
                    
                    if 'paisNac' in dir(dadosNasc):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosNasc.paisNac', 
                                                          dadosNasc.paisNac.cdata, 
                                                          1, u'None')
                    
                    if 'nmMae' in dir(dadosNasc):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosNasc.nmMae', 
                                                          dadosNasc.nmMae.cdata, 
                                                          0, u'None')
                    
                    if 'nmPai' in dir(dadosNasc):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dadosNasc.nmPai', 
                                                          dadosNasc.nmPai.cdata, 
                                                          0, u'None')
            
            if 'endereco' in dir(beneficiario.endereco):
                for endereco in beneficiario.endereco:
                    
                    if 'brasil' in dir(endereco.brasil):
                        for brasil in endereco.brasil:
                            
                            if 'tpLograd' in dir(brasil):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'brasil.tpLograd', 
                                                                  brasil.tpLograd.cdata, 
                                                                  1, u'None')
                            
                            if 'dscLograd' in dir(brasil):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'brasil.dscLograd', 
                                                                  brasil.dscLograd.cdata, 
                                                                  1, u'None')
                            
                            if 'nrLograd' in dir(brasil):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'brasil.nrLograd', 
                                                                  brasil.nrLograd.cdata, 
                                                                  1, u'None')
                            
                            if 'complemento' in dir(brasil):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'brasil.complemento', 
                                                                  brasil.complemento.cdata, 
                                                                  0, u'None')
                            
                            if 'bairro' in dir(brasil):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'brasil.bairro', 
                                                                  brasil.bairro.cdata, 
                                                                  0, u'None')
                            
                            if 'cep' in dir(brasil):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'brasil.cep', 
                                                                  brasil.cep.cdata, 
                                                                  1, u'None')
                            
                            if 'codMunic' in dir(brasil):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'brasil.codMunic', 
                                                                  brasil.codMunic.cdata, 
                                                                  1, u'None')
                            
                            if 'uf' in dir(brasil):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'brasil.uf', 
                                                                  brasil.uf.cdata, 
                                                                  1, u'None')
                    
                    if 'exterior' in dir(endereco.exterior):
                        for exterior in endereco.exterior:
                            
                            if 'paisResid' in dir(exterior):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'exterior.paisResid', 
                                                                  exterior.paisResid.cdata, 
                                                                  1, u'None')
                            
                            if 'dscLograd' in dir(exterior):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'exterior.dscLograd', 
                                                                  exterior.dscLograd.cdata, 
                                                                  1, u'None')
                            
                            if 'nrLograd' in dir(exterior):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'exterior.nrLograd', 
                                                                  exterior.nrLograd.cdata, 
                                                                  1, u'None')
                            
                            if 'complemento' in dir(exterior):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'exterior.complemento', 
                                                                  exterior.complemento.cdata, 
                                                                  0, u'None')
                            
                            if 'bairro' in dir(exterior):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'exterior.bairro', 
                                                                  exterior.bairro.cdata, 
                                                                  0, u'None')
                            
                            if 'nmCid' in dir(exterior):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'exterior.nmCid', 
                                                                  exterior.nmCid.cdata, 
                                                                  1, u'None')
                            
                            if 'codPostal' in dir(exterior):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'exterior.codPostal', 
                                                                  exterior.codPostal.cdata, 
                                                                  0, u'None')
            
            if 'dependente' in dir(beneficiario.dependente):
                for dependente in beneficiario.dependente:
                    
                    if 'tpDep' in dir(dependente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dependente.tpDep', 
                                                          dependente.tpDep.cdata, 
                                                          1, u'01, 02, 03, 04, 06, 07, 09, 10, 11, 12, 99')
                    
                    if 'nmDep' in dir(dependente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dependente.nmDep', 
                                                          dependente.nmDep.cdata, 
                                                          1, u'None')
                    
                    if 'dtNascto' in dir(dependente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dependente.dtNascto', 
                                                          dependente.dtNascto.cdata, 
                                                          1, u'None')
                    
                    if 'cpfDep' in dir(dependente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dependente.cpfDep', 
                                                          dependente.cpfDep.cdata, 
                                                          0, u'None')
                    
                    if 'sexoDep' in dir(dependente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dependente.sexoDep', 
                                                          dependente.sexoDep.cdata, 
                                                          1, u'M, F')
                    
                    if 'depIRRF' in dir(dependente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dependente.depIRRF', 
                                                          dependente.depIRRF.cdata, 
                                                          1, u'S, N')
                    
                    if 'incFisMen' in dir(dependente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dependente.incFisMen', 
                                                          dependente.incFisMen.cdata, 
                                                          1, u'S, N')
                    
                    if 'depFinsPrev' in dir(dependente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'dependente.depFinsPrev', 
                                                          dependente.depFinsPrev.cdata, 
                                                          1, u'S, N')
    return validacoes_lista