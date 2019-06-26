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


def validacoes_r2010_evtservtom(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtServTom = doc.Reinf.evtServTom
    #variaveis

    if 'ideEvento' in dir(evtServTom.ideEvento):
        for ideEvento in evtServTom.ideEvento:

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

            if 'perApur' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.perApur',
                                                  ideEvento.perApur.cdata,
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

    if 'ideContri' in dir(evtServTom.ideContri):
        for ideContri in evtServTom.ideContri:

            if 'tpInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.tpInsc',
                                                  ideContri.tpInsc.cdata,
                                                  1, u'1, 2')

            if 'nrInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.nrInsc',
                                                  ideContri.nrInsc.cdata,
                                                  1, u'None')

    if 'infoServTom' in dir(evtServTom.infoServTom):
        for infoServTom in evtServTom.infoServTom:

            if 'ideEstabObra' in dir(infoServTom.ideEstabObra):
                for ideEstabObra in infoServTom.ideEstabObra:

                    if 'tpInscEstab' in dir(ideEstabObra):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstabObra.tpInscEstab',
                                                          ideEstabObra.tpInscEstab.cdata,
                                                          1, u'None')

                    if 'nrInscEstab' in dir(ideEstabObra):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstabObra.nrInscEstab',
                                                          ideEstabObra.nrInscEstab.cdata,
                                                          1, u'None')

                    if 'indObra' in dir(ideEstabObra):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstabObra.indObra',
                                                          ideEstabObra.indObra.cdata,
                                                          1, u'0, 1, 2')

                    if 'idePrestServ' in dir(ideEstabObra.idePrestServ):
                        for idePrestServ in ideEstabObra.idePrestServ:
        
                            if 'cnpjPrestador' in dir(idePrestServ):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePrestServ.cnpjPrestador',
                                                                  idePrestServ.cnpjPrestador.cdata,
                                                                  1, u'None')
        
                            if 'vlrTotalBruto' in dir(idePrestServ):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePrestServ.vlrTotalBruto',
                                                                  idePrestServ.vlrTotalBruto.cdata,
                                                                  1, u'None')
        
                            if 'vlrTotalBaseRet' in dir(idePrestServ):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePrestServ.vlrTotalBaseRet',
                                                                  idePrestServ.vlrTotalBaseRet.cdata,
                                                                  1, u'None')
        
                            if 'vlrTotalRetPrinc' in dir(idePrestServ):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePrestServ.vlrTotalRetPrinc',
                                                                  idePrestServ.vlrTotalRetPrinc.cdata,
                                                                  1, u'None')
        
                            if 'vlrTotalRetAdic' in dir(idePrestServ):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePrestServ.vlrTotalRetAdic',
                                                                  idePrestServ.vlrTotalRetAdic.cdata,
                                                                  0, u'None')
        
                            if 'vlrTotalNRetPrinc' in dir(idePrestServ):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePrestServ.vlrTotalNRetPrinc',
                                                                  idePrestServ.vlrTotalNRetPrinc.cdata,
                                                                  0, u'None')
        
                            if 'vlrTotalNRetAdic' in dir(idePrestServ):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePrestServ.vlrTotalNRetAdic',
                                                                  idePrestServ.vlrTotalNRetAdic.cdata,
                                                                  0, u'None')
        
                            if 'indCPRB' in dir(idePrestServ):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePrestServ.indCPRB',
                                                                  idePrestServ.indCPRB.cdata,
                                                                  1, u'0, 1')
        
                            if 'nfs' in dir(idePrestServ.nfs):
                                for nfs in idePrestServ.nfs:
                
                                    if 'serie' in dir(nfs):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'nfs.serie',
                                                                          nfs.serie.cdata,
                                                                          1, u'None')
                
                                    if 'numDocto' in dir(nfs):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'nfs.numDocto',
                                                                          nfs.numDocto.cdata,
                                                                          1, u'None')
                
                                    if 'dtEmissaoNF' in dir(nfs):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'nfs.dtEmissaoNF',
                                                                          nfs.dtEmissaoNF.cdata,
                                                                          1, u'None')
                
                                    if 'vlrBruto' in dir(nfs):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'nfs.vlrBruto',
                                                                          nfs.vlrBruto.cdata,
                                                                          1, u'None')
                
                                    if 'obs' in dir(nfs):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'nfs.obs',
                                                                          nfs.obs.cdata,
                                                                          0, u'None')
                
                                    if 'infoTpServ' in dir(nfs.infoTpServ):
                                        for infoTpServ in nfs.infoTpServ:
                        
                                            if 'tpServico' in dir(infoTpServ):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoTpServ.tpServico',
                                                                                  infoTpServ.tpServico.cdata,
                                                                                  1, u'100000001, 100000002, 100000003, 100000004, 100000005, 100000006, 100000007, 100000008, 100000009, 100000010, 100000011, 100000012, 100000013, 100000014, 100000015, 100000016, 100000017, 100000018, 100000019, 100000020, 100000021, 100000022, 100000023, 100000024, 100000025, 100000026, 100000027, 100000028, 100000029, 100000030, 100000031')
                        
                                            if 'vlrBaseRet' in dir(infoTpServ):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoTpServ.vlrBaseRet',
                                                                                  infoTpServ.vlrBaseRet.cdata,
                                                                                  1, u'None')
                        
                                            if 'vlrRetencao' in dir(infoTpServ):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoTpServ.vlrRetencao',
                                                                                  infoTpServ.vlrRetencao.cdata,
                                                                                  1, u'None')
                        
                                            if 'vlrRetSub' in dir(infoTpServ):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoTpServ.vlrRetSub',
                                                                                  infoTpServ.vlrRetSub.cdata,
                                                                                  0, u'None')
                        
                                            if 'vlrNRetPrinc' in dir(infoTpServ):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoTpServ.vlrNRetPrinc',
                                                                                  infoTpServ.vlrNRetPrinc.cdata,
                                                                                  0, u'None')
                        
                                            if 'vlrServicos15' in dir(infoTpServ):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoTpServ.vlrServicos15',
                                                                                  infoTpServ.vlrServicos15.cdata,
                                                                                  0, u'None')
                        
                                            if 'vlrServicos20' in dir(infoTpServ):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoTpServ.vlrServicos20',
                                                                                  infoTpServ.vlrServicos20.cdata,
                                                                                  0, u'None')
                        
                                            if 'vlrServicos25' in dir(infoTpServ):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoTpServ.vlrServicos25',
                                                                                  infoTpServ.vlrServicos25.cdata,
                                                                                  0, u'None')
                        
                                            if 'vlrAdicional' in dir(infoTpServ):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoTpServ.vlrAdicional',
                                                                                  infoTpServ.vlrAdicional.cdata,
                                                                                  0, u'None')
                        
                                            if 'vlrNRetAdic' in dir(infoTpServ):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoTpServ.vlrNRetAdic',
                                                                                  infoTpServ.vlrNRetAdic.cdata,
                                                                                  0, u'None')
        
                            if 'infoProcRetPr' in dir(idePrestServ.infoProcRetPr):
                                for infoProcRetPr in idePrestServ.infoProcRetPr:
                
                                    if 'tpProcRetPrinc' in dir(infoProcRetPr):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcRetPr.tpProcRetPrinc',
                                                                          infoProcRetPr.tpProcRetPrinc.cdata,
                                                                          1, u'1, 2')
                
                                    if 'nrProcRetPrinc' in dir(infoProcRetPr):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcRetPr.nrProcRetPrinc',
                                                                          infoProcRetPr.nrProcRetPrinc.cdata,
                                                                          1, u'None')
                
                                    if 'codSuspPrinc' in dir(infoProcRetPr):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcRetPr.codSuspPrinc',
                                                                          infoProcRetPr.codSuspPrinc.cdata,
                                                                          0, u'None')
                
                                    if 'valorPrinc' in dir(infoProcRetPr):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcRetPr.valorPrinc',
                                                                          infoProcRetPr.valorPrinc.cdata,
                                                                          1, u'None')
        
                            if 'infoProcRetAd' in dir(idePrestServ.infoProcRetAd):
                                for infoProcRetAd in idePrestServ.infoProcRetAd:
                
                                    if 'tpProcRetAdic' in dir(infoProcRetAd):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcRetAd.tpProcRetAdic',
                                                                          infoProcRetAd.tpProcRetAdic.cdata,
                                                                          1, u'1, 2')
                
                                    if 'nrProcRetAdic' in dir(infoProcRetAd):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcRetAd.nrProcRetAdic',
                                                                          infoProcRetAd.nrProcRetAdic.cdata,
                                                                          1, u'None')
                
                                    if 'codSuspAdic' in dir(infoProcRetAd):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcRetAd.codSuspAdic',
                                                                          infoProcRetAd.codSuspAdic.cdata,
                                                                          0, u'None')
                
                                    if 'valorAdic' in dir(infoProcRetAd):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcRetAd.valorAdic',
                                                                          infoProcRetAd.valorAdic.cdata,
                                                                          1, u'None')
    return validacoes_lista