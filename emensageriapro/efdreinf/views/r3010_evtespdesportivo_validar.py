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
    #variaveis
    
    if 'ideEvento' in dir(evtEspDesportivo.ideEvento):
        for ideEvento in evtEspDesportivo.ideEvento:
            
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
            
            if 'dtApuracao' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.dtApuracao', 
                                                  ideEvento.dtApuracao.cdata, 
                                                  1, u'None')
            
            if 'tpAmb' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.tpAmb', 
                                                  ideEvento.tpAmb.cdata, 
                                                  1, u'1, 2')
            
            if 'procEmi' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.procEmi', 
                                                  ideEvento.procEmi.cdata, 
                                                  1, u'1, 2')
            
            if 'verProc' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.verProc', 
                                                  ideEvento.verProc.cdata, 
                                                  1, u'None')
    
    if 'ideContri' in dir(evtEspDesportivo.ideContri):
        for ideContri in evtEspDesportivo.ideContri:
            
            if 'tpInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.tpInsc', 
                                                  ideContri.tpInsc.cdata, 
                                                  1, u'None')
            
            if 'nrInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.nrInsc', 
                                                  ideContri.nrInsc.cdata, 
                                                  1, u'None')
            
            if 'ideEstab' in dir(ideContri.ideEstab):
                for ideEstab in ideContri.ideEstab:
                    
                    if 'tpInscEstab' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.tpInscEstab', 
                                                          ideEstab.tpInscEstab.cdata, 
                                                          1, u'1')
                    
                    if 'nrInscEstab' in dir(ideEstab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstab.nrInscEstab', 
                                                          ideEstab.nrInscEstab.cdata, 
                                                          1, u'None')
                    
                    if 'boletim' in dir(ideEstab.boletim):
                        for boletim in ideEstab.boletim:
                            
                            if 'nrBoletim' in dir(boletim):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'boletim.nrBoletim', 
                                                                  boletim.nrBoletim.cdata, 
                                                                  1, u'None')
                            
                            if 'tpCompeticao' in dir(boletim):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'boletim.tpCompeticao', 
                                                                  boletim.tpCompeticao.cdata, 
                                                                  1, u'1, 2')
                            
                            if 'categEvento' in dir(boletim):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'boletim.categEvento', 
                                                                  boletim.categEvento.cdata, 
                                                                  1, u'1, 2, 3, 4')
                            
                            if 'modDesportiva' in dir(boletim):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'boletim.modDesportiva', 
                                                                  boletim.modDesportiva.cdata, 
                                                                  1, u'None')
                            
                            if 'nomeCompeticao' in dir(boletim):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'boletim.nomeCompeticao', 
                                                                  boletim.nomeCompeticao.cdata, 
                                                                  1, u'None')
                            
                            if 'cnpjMandante' in dir(boletim):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'boletim.cnpjMandante', 
                                                                  boletim.cnpjMandante.cdata, 
                                                                  1, u'None')
                            
                            if 'cnpjVisitante' in dir(boletim):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'boletim.cnpjVisitante', 
                                                                  boletim.cnpjVisitante.cdata, 
                                                                  0, u'None')
                            
                            if 'nomeVisitante' in dir(boletim):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'boletim.nomeVisitante', 
                                                                  boletim.nomeVisitante.cdata, 
                                                                  0, u'None')
                            
                            if 'pracaDesportiva' in dir(boletim):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'boletim.pracaDesportiva', 
                                                                  boletim.pracaDesportiva.cdata, 
                                                                  1, u'None')
                            
                            if 'codMunic' in dir(boletim):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'boletim.codMunic', 
                                                                  boletim.codMunic.cdata, 
                                                                  0, u'None')
                            
                            if 'uf' in dir(boletim):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'boletim.uf', 
                                                                  boletim.uf.cdata, 
                                                                  1, u'None')
                            
                            if 'qtdePagantes' in dir(boletim):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'boletim.qtdePagantes', 
                                                                  boletim.qtdePagantes.cdata, 
                                                                  1, u'None')
                            
                            if 'qtdeNaoPagantes' in dir(boletim):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'boletim.qtdeNaoPagantes', 
                                                                  boletim.qtdeNaoPagantes.cdata, 
                                                                  1, u'None')
                            
                            if 'receitaIngressos' in dir(boletim.receitaIngressos):
                                for receitaIngressos in boletim.receitaIngressos:
                                    
                                    if 'tpIngresso' in dir(receitaIngressos):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'receitaIngressos.tpIngresso', 
                                                                          receitaIngressos.tpIngresso.cdata, 
                                                                          1, u'1, 2, 3, 4')
                                    
                                    if 'descIngr' in dir(receitaIngressos):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'receitaIngressos.descIngr', 
                                                                          receitaIngressos.descIngr.cdata, 
                                                                          1, u'None')
                                    
                                    if 'qtdeIngrVenda' in dir(receitaIngressos):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'receitaIngressos.qtdeIngrVenda', 
                                                                          receitaIngressos.qtdeIngrVenda.cdata, 
                                                                          1, u'None')
                                    
                                    if 'qtdeIngrVendidos' in dir(receitaIngressos):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'receitaIngressos.qtdeIngrVendidos', 
                                                                          receitaIngressos.qtdeIngrVendidos.cdata, 
                                                                          1, u'None')
                                    
                                    if 'qtdeIngrDev' in dir(receitaIngressos):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'receitaIngressos.qtdeIngrDev', 
                                                                          receitaIngressos.qtdeIngrDev.cdata, 
                                                                          1, u'None')
                                    
                                    if 'precoIndiv' in dir(receitaIngressos):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'receitaIngressos.precoIndiv', 
                                                                          receitaIngressos.precoIndiv.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vlrTotal' in dir(receitaIngressos):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'receitaIngressos.vlrTotal', 
                                                                          receitaIngressos.vlrTotal.cdata, 
                                                                          1, u'None')
                            
                            if 'outrasReceitas' in dir(boletim.outrasReceitas):
                                for outrasReceitas in boletim.outrasReceitas:
                                    
                                    if 'tpReceita' in dir(outrasReceitas):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'outrasReceitas.tpReceita', 
                                                                          outrasReceitas.tpReceita.cdata, 
                                                                          1, u'1, 2, 3, 4, 5')
                                    
                                    if 'vlrReceita' in dir(outrasReceitas):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'outrasReceitas.vlrReceita', 
                                                                          outrasReceitas.vlrReceita.cdata, 
                                                                          1, u'None')
                                    
                                    if 'descReceita' in dir(outrasReceitas):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'outrasReceitas.descReceita', 
                                                                          outrasReceitas.descReceita.cdata, 
                                                                          1, u'None')
                    
                    if 'receitaTotal' in dir(ideEstab.receitaTotal):
                        for receitaTotal in ideEstab.receitaTotal:
                            
                            if 'vlrReceitaTotal' in dir(receitaTotal):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'receitaTotal.vlrReceitaTotal', 
                                                                  receitaTotal.vlrReceitaTotal.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrCP' in dir(receitaTotal):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'receitaTotal.vlrCP', 
                                                                  receitaTotal.vlrCP.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrCPSuspTotal' in dir(receitaTotal):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'receitaTotal.vlrCPSuspTotal', 
                                                                  receitaTotal.vlrCPSuspTotal.cdata, 
                                                                  0, u'None')
                            
                            if 'vlrReceitaClubes' in dir(receitaTotal):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'receitaTotal.vlrReceitaClubes', 
                                                                  receitaTotal.vlrReceitaClubes.cdata, 
                                                                  1, u'None')
                            
                            if 'vlrRetParc' in dir(receitaTotal):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'receitaTotal.vlrRetParc', 
                                                                  receitaTotal.vlrRetParc.cdata, 
                                                                  1, u'None')
                            
                            if 'infoProc' in dir(receitaTotal.infoProc):
                                for infoProc in receitaTotal.infoProc:
                                    
                                    if 'tpProc' in dir(infoProc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProc.tpProc', 
                                                                          infoProc.tpProc.cdata, 
                                                                          1, u'1, 2')
                                    
                                    if 'nrProc' in dir(infoProc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProc.nrProc', 
                                                                          infoProc.nrProc.cdata, 
                                                                          1, u'None')
                                    
                                    if 'codSusp' in dir(infoProc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProc.codSusp', 
                                                                          infoProc.codSusp.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vlrCPSusp' in dir(infoProc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProc.vlrCPSusp', 
                                                                          infoProc.vlrCPSusp.cdata, 
                                                                          1, u'None')
    return validacoes_lista