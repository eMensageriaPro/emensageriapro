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


def validacoes_s1000_evtinfoempregador(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtInfoEmpregador = doc.eSocial.evtInfoEmpregador
    #variaveis
    
    if 'ideEvento' in dir(evtInfoEmpregador.ideEvento):
        for ideEvento in evtInfoEmpregador.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtInfoEmpregador.ideEmpregador):
        for ideEmpregador in evtInfoEmpregador.ideEmpregador:
            
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
    
    if 'infoEmpregador' in dir(evtInfoEmpregador.infoEmpregador):
        for infoEmpregador in evtInfoEmpregador.infoEmpregador:
            
            if 'inclusao' in dir(infoEmpregador.inclusao):
                for inclusao in infoEmpregador.inclusao:
                    
                    if 'idePeriodo' in dir(inclusao.idePeriodo):
                        for idePeriodo in inclusao.idePeriodo:
                            
                            if 'iniValid' in dir(idePeriodo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePeriodo.iniValid', 
                                                                  idePeriodo.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(idePeriodo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePeriodo.fimValid', 
                                                                  idePeriodo.fimValid.cdata, 
                                                                  0, u'None')
                    
                    if 'infoCadastro' in dir(inclusao.infoCadastro):
                        for infoCadastro in inclusao.infoCadastro:
                            
                            if 'nmRazao' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.nmRazao', 
                                                                  infoCadastro.nmRazao.cdata, 
                                                                  1, u'None')
                            
                            if 'classTrib' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.classTrib', 
                                                                  infoCadastro.classTrib.cdata, 
                                                                  1, u'01, 02, 03, 04, 06, 07, 08, 09, 10, 11, 13, 14, 21, 22, 60, 70, 80, 85, 99')
                            
                            if 'natJurid' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.natJurid', 
                                                                  infoCadastro.natJurid.cdata, 
                                                                  0, u'101-5, 102-3, 103-1, 104-0, 105-8, 106-6, 107-4, 108-2, 110-4, 111-2, 112-0, 113-9, 114-7, 115-5, 116-3, 117-1, 118-0, 119-8, 120-1, 121-0, 122-8, 123-6, 124-4, 125-2, 126-0, 127-9, 201-1, 203-8, 204-6, 205-4, 206-2, 207-0, 208-9, 209-7, 212-7, 213-5, 214-3, 215-1, 216-0, 217-8, 219-4, 221-6, 222-4, 223-2, 224-0, 225-9, 226-7, 227-5, 228-3, 229-1, 230-5, 231-3, 232-1, 233-0, 303-4, 306-9, 307-7, 308-5, 310-7, 311-5, 313-1, 320-4, 321-2, 322-0, 323-9, 324-7, 325-5, 326-3, 327-1, 328-0, 329-8, 330-1, 331-0, 399-9, 401-4, 402-2, 408-1, 409-0, 411-1, 412-0, 501-0, 502-9, 503-7')
                            
                            if 'indCoop' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indCoop', 
                                                                  infoCadastro.indCoop.cdata, 
                                                                  0, u'0, 1, 2, 3')
                            
                            if 'indConstr' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indConstr', 
                                                                  infoCadastro.indConstr.cdata, 
                                                                  0, u'0, 1')
                            
                            if 'indDesFolha' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indDesFolha', 
                                                                  infoCadastro.indDesFolha.cdata, 
                                                                  1, u'0, 1')
                            
                            if 'indOpcCP' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indOpcCP', 
                                                                  infoCadastro.indOpcCP.cdata, 
                                                                  0, u'1, 2')
                            
                            if 'indOptRegEletron' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indOptRegEletron', 
                                                                  infoCadastro.indOptRegEletron.cdata, 
                                                                  1, u'0, 1')
                            
                            if 'indEntEd' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indEntEd', 
                                                                  infoCadastro.indEntEd.cdata, 
                                                                  0, u'S, N')
                            
                            if 'indEtt' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indEtt', 
                                                                  infoCadastro.indEtt.cdata, 
                                                                  1, u'S, N')
                            
                            if 'nrRegEtt' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.nrRegEtt', 
                                                                  infoCadastro.nrRegEtt.cdata, 
                                                                  0, u'None')
                            
                            if 'dadosIsencao' in dir(infoCadastro.dadosIsencao):
                                for dadosIsencao in infoCadastro.dadosIsencao:
                                    
                                    if 'ideMinLei' in dir(dadosIsencao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosIsencao.ideMinLei', 
                                                                          dadosIsencao.ideMinLei.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nrCertif' in dir(dadosIsencao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosIsencao.nrCertif', 
                                                                          dadosIsencao.nrCertif.cdata, 
                                                                          1, u'None')
                                    
                                    if 'dtEmisCertif' in dir(dadosIsencao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosIsencao.dtEmisCertif', 
                                                                          dadosIsencao.dtEmisCertif.cdata, 
                                                                          1, u'None')
                                    
                                    if 'dtVencCertif' in dir(dadosIsencao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosIsencao.dtVencCertif', 
                                                                          dadosIsencao.dtVencCertif.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nrProtRenov' in dir(dadosIsencao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosIsencao.nrProtRenov', 
                                                                          dadosIsencao.nrProtRenov.cdata, 
                                                                          0, u'None')
                                    
                                    if 'dtProtRenov' in dir(dadosIsencao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosIsencao.dtProtRenov', 
                                                                          dadosIsencao.dtProtRenov.cdata, 
                                                                          0, u'None')
                                    
                                    if 'dtDou' in dir(dadosIsencao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosIsencao.dtDou', 
                                                                          dadosIsencao.dtDou.cdata, 
                                                                          0, u'None')
                                    
                                    if 'pagDou' in dir(dadosIsencao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosIsencao.pagDou', 
                                                                          dadosIsencao.pagDou.cdata, 
                                                                          0, u'None')
                            
                            if 'contato' in dir(infoCadastro.contato):
                                for contato in infoCadastro.contato:
                                    
                                    if 'nmCtt' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.nmCtt', 
                                                                          contato.nmCtt.cdata, 
                                                                          1, u'None')
                                    
                                    if 'cpfCtt' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.cpfCtt', 
                                                                          contato.cpfCtt.cdata, 
                                                                          1, u'None')
                                    
                                    if 'foneFixo' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.foneFixo', 
                                                                          contato.foneFixo.cdata, 
                                                                          0, u'None')
                                    
                                    if 'foneCel' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.foneCel', 
                                                                          contato.foneCel.cdata, 
                                                                          0, u'None')
                                    
                                    if 'email' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.email', 
                                                                          contato.email.cdata, 
                                                                          0, u'None')
                            
                            if 'infoOP' in dir(infoCadastro.infoOP):
                                for infoOP in infoCadastro.infoOP:
                                    
                                    if 'nrSiafi' in dir(infoOP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoOP.nrSiafi', 
                                                                          infoOP.nrSiafi.cdata, 
                                                                          1, u'None')
                                    
                                    if 'indUGRPPS' in dir(infoOP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoOP.indUGRPPS', 
                                                                          infoOP.indUGRPPS.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'esferaOP' in dir(infoOP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoOP.esferaOP', 
                                                                          infoOP.esferaOP.cdata, 
                                                                          0, u'1, 2, 3')
                                    
                                    if 'poderOP' in dir(infoOP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoOP.poderOP', 
                                                                          infoOP.poderOP.cdata, 
                                                                          1, u'1, 2, 3, 4, 5, 6')
                                    
                                    if 'vrTetoRem' in dir(infoOP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoOP.vrTetoRem', 
                                                                          infoOP.vrTetoRem.cdata, 
                                                                          1, u'None')
                                    
                                    if 'ideEFR' in dir(infoOP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoOP.ideEFR', 
                                                                          infoOP.ideEFR.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'cnpjEFR' in dir(infoOP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoOP.cnpjEFR', 
                                                                          infoOP.cnpjEFR.cdata, 
                                                                          0, u'None')
                                    
                                    if 'infoEFR' in dir(infoOP.infoEFR):
                                        for infoEFR in infoOP.infoEFR:
                                            
                                            if 'ideEFR' in dir(infoEFR):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEFR.ideEFR', 
                                                                                  infoEFR.ideEFR.cdata, 
                                                                                  1, u'S, N')
                                            
                                            if 'cnpjEFR' in dir(infoEFR):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEFR.cnpjEFR', 
                                                                                  infoEFR.cnpjEFR.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'indRPPS' in dir(infoEFR):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEFR.indRPPS', 
                                                                                  infoEFR.indRPPS.cdata, 
                                                                                  1, u'S, N')
                                            
                                            if 'prevComp' in dir(infoEFR):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEFR.prevComp', 
                                                                                  infoEFR.prevComp.cdata, 
                                                                                  1, u'S, N')
                                    
                                    if 'infoEnte' in dir(infoOP.infoEnte):
                                        for infoEnte in infoOP.infoEnte:
                                            
                                            if 'nmEnte' in dir(infoEnte):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEnte.nmEnte', 
                                                                                  infoEnte.nmEnte.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'uf' in dir(infoEnte):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEnte.uf', 
                                                                                  infoEnte.uf.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'codMunic' in dir(infoEnte):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEnte.codMunic', 
                                                                                  infoEnte.codMunic.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'indRPPS' in dir(infoEnte):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEnte.indRPPS', 
                                                                                  infoEnte.indRPPS.cdata, 
                                                                                  1, u'S, N')
                                            
                                            if 'subteto' in dir(infoEnte):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEnte.subteto', 
                                                                                  infoEnte.subteto.cdata, 
                                                                                  1, u'1, 2, 3, 9')
                                            
                                            if 'vrSubteto' in dir(infoEnte):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEnte.vrSubteto', 
                                                                                  infoEnte.vrSubteto.cdata, 
                                                                                  1, u'None')
                            
                            if 'infoOrgInternacional' in dir(infoCadastro.infoOrgInternacional):
                                for infoOrgInternacional in infoCadastro.infoOrgInternacional:
                                    
                                    if 'indAcordoIsenMulta' in dir(infoOrgInternacional):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoOrgInternacional.indAcordoIsenMulta', 
                                                                          infoOrgInternacional.indAcordoIsenMulta.cdata, 
                                                                          1, u'0, 1')
                            
                            if 'softwareHouse' in dir(infoCadastro.softwareHouse):
                                for softwareHouse in infoCadastro.softwareHouse:
                                    
                                    if 'cnpjSoftHouse' in dir(softwareHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softwareHouse.cnpjSoftHouse', 
                                                                          softwareHouse.cnpjSoftHouse.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nmRazao' in dir(softwareHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softwareHouse.nmRazao', 
                                                                          softwareHouse.nmRazao.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nmCont' in dir(softwareHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softwareHouse.nmCont', 
                                                                          softwareHouse.nmCont.cdata, 
                                                                          1, u'None')
                                    
                                    if 'telefone' in dir(softwareHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softwareHouse.telefone', 
                                                                          softwareHouse.telefone.cdata, 
                                                                          1, u'None')
                                    
                                    if 'email' in dir(softwareHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softwareHouse.email', 
                                                                          softwareHouse.email.cdata, 
                                                                          0, u'None')
                            
                            if 'infoComplementares' in dir(infoCadastro.infoComplementares):
                                for infoComplementares in infoCadastro.infoComplementares:
                                    
                                    if 'situacaoPJ' in dir(infoComplementares.situacaoPJ):
                                        for situacaoPJ in infoComplementares.situacaoPJ:
                                            
                                            if 'indSitPJ' in dir(situacaoPJ):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'situacaoPJ.indSitPJ', 
                                                                                  situacaoPJ.indSitPJ.cdata, 
                                                                                  1, u'0, 1, 2, 3, 4')
                                    
                                    if 'situacaoPF' in dir(infoComplementares.situacaoPF):
                                        for situacaoPF in infoComplementares.situacaoPF:
                                            
                                            if 'indSitPF' in dir(situacaoPF):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'situacaoPF.indSitPF', 
                                                                                  situacaoPF.indSitPF.cdata, 
                                                                                  1, u'0, 1, 2')
            
            if 'alteracao' in dir(infoEmpregador.alteracao):
                for alteracao in infoEmpregador.alteracao:
                    
                    if 'idePeriodo' in dir(alteracao.idePeriodo):
                        for idePeriodo in alteracao.idePeriodo:
                            
                            if 'iniValid' in dir(idePeriodo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePeriodo.iniValid', 
                                                                  idePeriodo.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(idePeriodo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePeriodo.fimValid', 
                                                                  idePeriodo.fimValid.cdata, 
                                                                  0, u'None')
                    
                    if 'infoCadastro' in dir(alteracao.infoCadastro):
                        for infoCadastro in alteracao.infoCadastro:
                            
                            if 'nmRazao' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.nmRazao', 
                                                                  infoCadastro.nmRazao.cdata, 
                                                                  1, u'None')
                            
                            if 'classTrib' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.classTrib', 
                                                                  infoCadastro.classTrib.cdata, 
                                                                  1, u'01, 02, 03, 04, 06, 07, 08, 09, 10, 11, 13, 14, 21, 22, 60, 70, 80, 85, 99')
                            
                            if 'natJurid' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.natJurid', 
                                                                  infoCadastro.natJurid.cdata, 
                                                                  0, u'101-5, 102-3, 103-1, 104-0, 105-8, 106-6, 107-4, 108-2, 110-4, 111-2, 112-0, 113-9, 114-7, 115-5, 116-3, 117-1, 118-0, 119-8, 120-1, 121-0, 122-8, 123-6, 124-4, 125-2, 126-0, 127-9, 201-1, 203-8, 204-6, 205-4, 206-2, 207-0, 208-9, 209-7, 212-7, 213-5, 214-3, 215-1, 216-0, 217-8, 219-4, 221-6, 222-4, 223-2, 224-0, 225-9, 226-7, 227-5, 228-3, 229-1, 230-5, 231-3, 232-1, 233-0, 303-4, 306-9, 307-7, 308-5, 310-7, 311-5, 313-1, 320-4, 321-2, 322-0, 323-9, 324-7, 325-5, 326-3, 327-1, 328-0, 329-8, 330-1, 331-0, 399-9, 401-4, 402-2, 408-1, 409-0, 411-1, 412-0, 501-0, 502-9, 503-7')
                            
                            if 'indCoop' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indCoop', 
                                                                  infoCadastro.indCoop.cdata, 
                                                                  0, u'0, 1, 2, 3')
                            
                            if 'indConstr' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indConstr', 
                                                                  infoCadastro.indConstr.cdata, 
                                                                  0, u'0, 1')
                            
                            if 'indDesFolha' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indDesFolha', 
                                                                  infoCadastro.indDesFolha.cdata, 
                                                                  1, u'0, 1')
                            
                            if 'indOpcCP' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indOpcCP', 
                                                                  infoCadastro.indOpcCP.cdata, 
                                                                  0, u'1, 2')
                            
                            if 'indOptRegEletron' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indOptRegEletron', 
                                                                  infoCadastro.indOptRegEletron.cdata, 
                                                                  1, u'0, 1')
                            
                            if 'indEntEd' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indEntEd', 
                                                                  infoCadastro.indEntEd.cdata, 
                                                                  0, u'S, N')
                            
                            if 'indEtt' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indEtt', 
                                                                  infoCadastro.indEtt.cdata, 
                                                                  1, u'S, N')
                            
                            if 'nrRegEtt' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.nrRegEtt', 
                                                                  infoCadastro.nrRegEtt.cdata, 
                                                                  0, u'None')
                            
                            if 'dadosIsencao' in dir(infoCadastro.dadosIsencao):
                                for dadosIsencao in infoCadastro.dadosIsencao:
                                    
                                    if 'ideMinLei' in dir(dadosIsencao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosIsencao.ideMinLei', 
                                                                          dadosIsencao.ideMinLei.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nrCertif' in dir(dadosIsencao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosIsencao.nrCertif', 
                                                                          dadosIsencao.nrCertif.cdata, 
                                                                          1, u'None')
                                    
                                    if 'dtEmisCertif' in dir(dadosIsencao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosIsencao.dtEmisCertif', 
                                                                          dadosIsencao.dtEmisCertif.cdata, 
                                                                          1, u'None')
                                    
                                    if 'dtVencCertif' in dir(dadosIsencao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosIsencao.dtVencCertif', 
                                                                          dadosIsencao.dtVencCertif.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nrProtRenov' in dir(dadosIsencao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosIsencao.nrProtRenov', 
                                                                          dadosIsencao.nrProtRenov.cdata, 
                                                                          0, u'None')
                                    
                                    if 'dtProtRenov' in dir(dadosIsencao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosIsencao.dtProtRenov', 
                                                                          dadosIsencao.dtProtRenov.cdata, 
                                                                          0, u'None')
                                    
                                    if 'dtDou' in dir(dadosIsencao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosIsencao.dtDou', 
                                                                          dadosIsencao.dtDou.cdata, 
                                                                          0, u'None')
                                    
                                    if 'pagDou' in dir(dadosIsencao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosIsencao.pagDou', 
                                                                          dadosIsencao.pagDou.cdata, 
                                                                          0, u'None')
                            
                            if 'contato' in dir(infoCadastro.contato):
                                for contato in infoCadastro.contato:
                                    
                                    if 'nmCtt' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.nmCtt', 
                                                                          contato.nmCtt.cdata, 
                                                                          1, u'None')
                                    
                                    if 'cpfCtt' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.cpfCtt', 
                                                                          contato.cpfCtt.cdata, 
                                                                          1, u'None')
                                    
                                    if 'foneFixo' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.foneFixo', 
                                                                          contato.foneFixo.cdata, 
                                                                          0, u'None')
                                    
                                    if 'foneCel' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.foneCel', 
                                                                          contato.foneCel.cdata, 
                                                                          0, u'None')
                                    
                                    if 'email' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.email', 
                                                                          contato.email.cdata, 
                                                                          0, u'None')
                            
                            if 'infoOP' in dir(infoCadastro.infoOP):
                                for infoOP in infoCadastro.infoOP:
                                    
                                    if 'nrSiafi' in dir(infoOP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoOP.nrSiafi', 
                                                                          infoOP.nrSiafi.cdata, 
                                                                          1, u'None')
                                    
                                    if 'indUGRPPS' in dir(infoOP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoOP.indUGRPPS', 
                                                                          infoOP.indUGRPPS.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'esferaOP' in dir(infoOP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoOP.esferaOP', 
                                                                          infoOP.esferaOP.cdata, 
                                                                          0, u'1, 2, 3')
                                    
                                    if 'poderOP' in dir(infoOP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoOP.poderOP', 
                                                                          infoOP.poderOP.cdata, 
                                                                          1, u'1, 2, 3, 4, 5, 6')
                                    
                                    if 'vrTetoRem' in dir(infoOP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoOP.vrTetoRem', 
                                                                          infoOP.vrTetoRem.cdata, 
                                                                          1, u'None')
                                    
                                    if 'ideEFR' in dir(infoOP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoOP.ideEFR', 
                                                                          infoOP.ideEFR.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'cnpjEFR' in dir(infoOP):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoOP.cnpjEFR', 
                                                                          infoOP.cnpjEFR.cdata, 
                                                                          0, u'None')
                                    
                                    if 'infoEFR' in dir(infoOP.infoEFR):
                                        for infoEFR in infoOP.infoEFR:
                                            
                                            if 'ideEFR' in dir(infoEFR):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEFR.ideEFR', 
                                                                                  infoEFR.ideEFR.cdata, 
                                                                                  1, u'S, N')
                                            
                                            if 'cnpjEFR' in dir(infoEFR):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEFR.cnpjEFR', 
                                                                                  infoEFR.cnpjEFR.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'indRPPS' in dir(infoEFR):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEFR.indRPPS', 
                                                                                  infoEFR.indRPPS.cdata, 
                                                                                  1, u'S, N')
                                            
                                            if 'prevComp' in dir(infoEFR):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEFR.prevComp', 
                                                                                  infoEFR.prevComp.cdata, 
                                                                                  1, u'S, N')
                                    
                                    if 'infoEnte' in dir(infoOP.infoEnte):
                                        for infoEnte in infoOP.infoEnte:
                                            
                                            if 'nmEnte' in dir(infoEnte):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEnte.nmEnte', 
                                                                                  infoEnte.nmEnte.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'uf' in dir(infoEnte):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEnte.uf', 
                                                                                  infoEnte.uf.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'codMunic' in dir(infoEnte):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEnte.codMunic', 
                                                                                  infoEnte.codMunic.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'indRPPS' in dir(infoEnte):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEnte.indRPPS', 
                                                                                  infoEnte.indRPPS.cdata, 
                                                                                  1, u'S, N')
                                            
                                            if 'subteto' in dir(infoEnte):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEnte.subteto', 
                                                                                  infoEnte.subteto.cdata, 
                                                                                  1, u'1, 2, 3, 9')
                                            
                                            if 'vrSubteto' in dir(infoEnte):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoEnte.vrSubteto', 
                                                                                  infoEnte.vrSubteto.cdata, 
                                                                                  1, u'None')
                            
                            if 'infoOrgInternacional' in dir(infoCadastro.infoOrgInternacional):
                                for infoOrgInternacional in infoCadastro.infoOrgInternacional:
                                    
                                    if 'indAcordoIsenMulta' in dir(infoOrgInternacional):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoOrgInternacional.indAcordoIsenMulta', 
                                                                          infoOrgInternacional.indAcordoIsenMulta.cdata, 
                                                                          1, u'0, 1')
                            
                            if 'softwareHouse' in dir(infoCadastro.softwareHouse):
                                for softwareHouse in infoCadastro.softwareHouse:
                                    
                                    if 'cnpjSoftHouse' in dir(softwareHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softwareHouse.cnpjSoftHouse', 
                                                                          softwareHouse.cnpjSoftHouse.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nmRazao' in dir(softwareHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softwareHouse.nmRazao', 
                                                                          softwareHouse.nmRazao.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nmCont' in dir(softwareHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softwareHouse.nmCont', 
                                                                          softwareHouse.nmCont.cdata, 
                                                                          1, u'None')
                                    
                                    if 'telefone' in dir(softwareHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softwareHouse.telefone', 
                                                                          softwareHouse.telefone.cdata, 
                                                                          1, u'None')
                                    
                                    if 'email' in dir(softwareHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softwareHouse.email', 
                                                                          softwareHouse.email.cdata, 
                                                                          0, u'None')
                            
                            if 'infoComplementares' in dir(infoCadastro.infoComplementares):
                                for infoComplementares in infoCadastro.infoComplementares:
                                    
                                    if 'situacaoPJ' in dir(infoComplementares.situacaoPJ):
                                        for situacaoPJ in infoComplementares.situacaoPJ:
                                            
                                            if 'indSitPJ' in dir(situacaoPJ):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'situacaoPJ.indSitPJ', 
                                                                                  situacaoPJ.indSitPJ.cdata, 
                                                                                  1, u'0, 1, 2, 3, 4')
                                    
                                    if 'situacaoPF' in dir(infoComplementares.situacaoPF):
                                        for situacaoPF in infoComplementares.situacaoPF:
                                            
                                            if 'indSitPF' in dir(situacaoPF):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'situacaoPF.indSitPF', 
                                                                                  situacaoPF.indSitPF.cdata, 
                                                                                  1, u'0, 1, 2')
                    
                    if 'novaValidade' in dir(alteracao.novaValidade):
                        for novaValidade in alteracao.novaValidade:
                            
                            if 'iniValid' in dir(novaValidade):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'novaValidade.iniValid', 
                                                                  novaValidade.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(novaValidade):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'novaValidade.fimValid', 
                                                                  novaValidade.fimValid.cdata, 
                                                                  0, u'None')
            
            if 'exclusao' in dir(infoEmpregador.exclusao):
                for exclusao in infoEmpregador.exclusao:
                    
                    if 'idePeriodo' in dir(exclusao.idePeriodo):
                        for idePeriodo in exclusao.idePeriodo:
                            
                            if 'iniValid' in dir(idePeriodo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePeriodo.iniValid', 
                                                                  idePeriodo.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(idePeriodo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePeriodo.fimValid', 
                                                                  idePeriodo.fimValid.cdata, 
                                                                  0, u'None')
    return validacoes_lista