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
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtInfoEmpregador = doc.eSocial.evtInfoEmpregador

    if 'tpAmb' in dir(evtInfoEmpregador.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInfoEmpregador.ideEvento.tpAmb', evtInfoEmpregador.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtInfoEmpregador.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInfoEmpregador.ideEvento.procEmi', evtInfoEmpregador.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtInfoEmpregador.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInfoEmpregador.ideEvento.verProc', evtInfoEmpregador.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtInfoEmpregador.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtInfoEmpregador.ideEmpregador.tpInsc', evtInfoEmpregador.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtInfoEmpregador.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtInfoEmpregador.ideEmpregador.nrInsc', evtInfoEmpregador.ideEmpregador.nrInsc.cdata, 1, '')
    if 'inclusao' in dir(evtInfoEmpregador.infoEmpregador):
        for inclusao in evtInfoEmpregador.infoEmpregador.inclusao:
       
            if 'iniValid' in dir(inclusao.idePeriodo): validacoes_lista = validar_campo(validacoes_lista,'inclusao.idePeriodo.iniValid', inclusao.idePeriodo.iniValid.cdata, 1, '')
            if 'fimValid' in dir(inclusao.idePeriodo): validacoes_lista = validar_campo(validacoes_lista,'inclusao.idePeriodo.fimValid', inclusao.idePeriodo.fimValid.cdata, 0, '')
            if 'nmRazao' in dir(inclusao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.nmRazao', inclusao.infoCadastro.nmRazao.cdata, 1, '')
            if 'classTrib' in dir(inclusao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.classTrib', inclusao.infoCadastro.classTrib.cdata, 1, '01;02;03;04;06;07;08;09;10;11;13;14;21;22;60;70;80;85;99')
            if 'natJurid' in dir(inclusao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.natJurid', inclusao.infoCadastro.natJurid.cdata, 0, '1015;1023;1031;1040;1058;1066;1074;1082;1104;1112;1120;1139;1147;1155;1163;1171;1180;1198;1201;1210;1228;1236;1244;1252;1260;1279;2011;2038;2046;2054;2062;2070;2089;2097;2127;2135;2143;2151;2160;2178;2194;2216;2224;2232;2240;2259;2267;2275;2283;2291;2305;2313;2321;2330;3034;3069;3077;3085;3107;3115;3131;3204;3212;3220;3239;3247;3255;3263;3271;3280;3298;3306;3310;3999;4014;4022;4081;4090;4111;4124;5010;5029;5037')
            if 'indCoop' in dir(inclusao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.indCoop', inclusao.infoCadastro.indCoop.cdata, 0, '0;1;2;3')
            if 'indConstr' in dir(inclusao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.indConstr', inclusao.infoCadastro.indConstr.cdata, 0, '0;1')
            if 'indDesFolha' in dir(inclusao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.indDesFolha', inclusao.infoCadastro.indDesFolha.cdata, 1, '0;1')
            if 'indOptRegEletron' in dir(inclusao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.indOptRegEletron', inclusao.infoCadastro.indOptRegEletron.cdata, 1, '0;1')
            if 'indEntEd' in dir(inclusao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.indEntEd', inclusao.infoCadastro.indEntEd.cdata, 0, 'N;S')
            if 'indEtt' in dir(inclusao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.indEtt', inclusao.infoCadastro.indEtt.cdata, 1, 'N;S')
            if 'nrRegEtt' in dir(inclusao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.nrRegEtt', inclusao.infoCadastro.nrRegEtt.cdata, 0, '')
            if 'nmCtt' in dir(inclusao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.contato.nmCtt', inclusao.infoCadastro.contato.nmCtt.cdata, 1, '')
            if 'cpfCtt' in dir(inclusao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.contato.cpfCtt', inclusao.infoCadastro.contato.cpfCtt.cdata, 1, '')
            if 'foneFixo' in dir(inclusao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.contato.foneFixo', inclusao.infoCadastro.contato.foneFixo.cdata, 0, '')
            if 'foneCel' in dir(inclusao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.contato.foneCel', inclusao.infoCadastro.contato.foneCel.cdata, 0, '')
            if 'email' in dir(inclusao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.contato.email', inclusao.infoCadastro.contato.email.cdata, 0, '')

            if 'dadosIsencao' in dir(inclusao.infoCadastro):
                for dadosIsencao in inclusao.infoCadastro.dadosIsencao:
               
                    if 'ideMinLei' in dir(dadosIsencao): validacoes_lista = validar_campo(validacoes_lista,'dadosIsencao.ideMinLei', dadosIsencao.ideMinLei.cdata, 1, '')
                    if 'nrCertif' in dir(dadosIsencao): validacoes_lista = validar_campo(validacoes_lista,'dadosIsencao.nrCertif', dadosIsencao.nrCertif.cdata, 1, '')
                    if 'dtEmisCertif' in dir(dadosIsencao): validacoes_lista = validar_campo(validacoes_lista,'dadosIsencao.dtEmisCertif', dadosIsencao.dtEmisCertif.cdata, 1, '')
                    if 'dtVencCertif' in dir(dadosIsencao): validacoes_lista = validar_campo(validacoes_lista,'dadosIsencao.dtVencCertif', dadosIsencao.dtVencCertif.cdata, 1, '')
                    if 'nrProtRenov' in dir(dadosIsencao): validacoes_lista = validar_campo(validacoes_lista,'dadosIsencao.nrProtRenov', dadosIsencao.nrProtRenov.cdata, 0, '')
                    if 'dtProtRenov' in dir(dadosIsencao): validacoes_lista = validar_campo(validacoes_lista,'dadosIsencao.dtProtRenov', dadosIsencao.dtProtRenov.cdata, 0, '')
                    if 'dtDou' in dir(dadosIsencao): validacoes_lista = validar_campo(validacoes_lista,'dadosIsencao.dtDou', dadosIsencao.dtDou.cdata, 0, '')
                    if 'pagDou' in dir(dadosIsencao): validacoes_lista = validar_campo(validacoes_lista,'dadosIsencao.pagDou', dadosIsencao.pagDou.cdata, 0, '')
   
            if 'infoOP' in dir(inclusao.infoCadastro):
                for infoOP in inclusao.infoCadastro.infoOP:
               
                    if 'nrSiafi' in dir(infoOP): validacoes_lista = validar_campo(validacoes_lista,'infoOP.nrSiafi', infoOP.nrSiafi.cdata, 1, '')
                    if 'indUGRPPS' in dir(infoOP): validacoes_lista = validar_campo(validacoes_lista,'infoOP.indUGRPPS', infoOP.indUGRPPS.cdata, 1, 'S;N')
                    if 'esferaOP' in dir(infoOP): validacoes_lista = validar_campo(validacoes_lista,'infoOP.esferaOP', infoOP.esferaOP.cdata, 0, '1;2;3')
                    if 'poderOP' in dir(infoOP): validacoes_lista = validar_campo(validacoes_lista,'infoOP.poderOP', infoOP.poderOP.cdata, 1, '1;2;3;4;5;6')
                    if 'vrTetoRem' in dir(infoOP): validacoes_lista = validar_campo(validacoes_lista,'infoOP.vrTetoRem', infoOP.vrTetoRem.cdata, 1, '')
                    if 'ideEFR' in dir(infoOP): validacoes_lista = validar_campo(validacoes_lista,'infoOP.ideEFR', infoOP.ideEFR.cdata, 1, 'S;N')
                    if 'cnpjEFR' in dir(infoOP): validacoes_lista = validar_campo(validacoes_lista,'infoOP.cnpjEFR', infoOP.cnpjEFR.cdata, 0, '')
   
            if 'infoOrgInternacional' in dir(inclusao.infoCadastro):
                for infoOrgInternacional in inclusao.infoCadastro.infoOrgInternacional:
               
                    if 'indAcordoIsenMulta' in dir(infoOrgInternacional): validacoes_lista = validar_campo(validacoes_lista,'infoOrgInternacional.indAcordoIsenMulta', infoOrgInternacional.indAcordoIsenMulta.cdata, 1, '0;1')
   
            if 'softwareHouse' in dir(inclusao.infoCadastro):
                for softwareHouse in inclusao.infoCadastro.softwareHouse:
               
                    if 'cnpjSoftHouse' in dir(softwareHouse): validacoes_lista = validar_campo(validacoes_lista,'softwareHouse.cnpjSoftHouse', softwareHouse.cnpjSoftHouse.cdata, 1, '')
                    if 'nmRazao' in dir(softwareHouse): validacoes_lista = validar_campo(validacoes_lista,'softwareHouse.nmRazao', softwareHouse.nmRazao.cdata, 1, '')
                    if 'nmCont' in dir(softwareHouse): validacoes_lista = validar_campo(validacoes_lista,'softwareHouse.nmCont', softwareHouse.nmCont.cdata, 1, '')
                    if 'telefone' in dir(softwareHouse): validacoes_lista = validar_campo(validacoes_lista,'softwareHouse.telefone', softwareHouse.telefone.cdata, 1, '')
                    if 'email' in dir(softwareHouse): validacoes_lista = validar_campo(validacoes_lista,'softwareHouse.email', softwareHouse.email.cdata, 0, '')
   
            if 'situacaoPJ' in dir(inclusao.infoCadastro.infoComplementares):
                for situacaoPJ in inclusao.infoCadastro.infoComplementares.situacaoPJ:
               
                    if 'indSitPJ' in dir(situacaoPJ): validacoes_lista = validar_campo(validacoes_lista,'situacaoPJ.indSitPJ', situacaoPJ.indSitPJ.cdata, 1, '0;1;2;3;4')
   
            if 'situacaoPF' in dir(inclusao.infoCadastro.infoComplementares):
                for situacaoPF in inclusao.infoCadastro.infoComplementares.situacaoPF:
               
                    if 'indSitPF' in dir(situacaoPF): validacoes_lista = validar_campo(validacoes_lista,'situacaoPF.indSitPF', situacaoPF.indSitPF.cdata, 1, '0;1;2')
   
    if 'alteracao' in dir(evtInfoEmpregador.infoEmpregador):
        for alteracao in evtInfoEmpregador.infoEmpregador.alteracao:
       
            if 'iniValid' in dir(alteracao.idePeriodo): validacoes_lista = validar_campo(validacoes_lista,'alteracao.idePeriodo.iniValid', alteracao.idePeriodo.iniValid.cdata, 1, '')
            if 'fimValid' in dir(alteracao.idePeriodo): validacoes_lista = validar_campo(validacoes_lista,'alteracao.idePeriodo.fimValid', alteracao.idePeriodo.fimValid.cdata, 0, '')
            if 'nmRazao' in dir(alteracao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.nmRazao', alteracao.infoCadastro.nmRazao.cdata, 1, '')
            if 'classTrib' in dir(alteracao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.classTrib', alteracao.infoCadastro.classTrib.cdata, 1, '01;02;03;04;06;07;08;09;10;11;13;14;21;22;60;70;80;85;99')
            if 'natJurid' in dir(alteracao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.natJurid', alteracao.infoCadastro.natJurid.cdata, 0, '1015;1023;1031;1040;1058;1066;1074;1082;1104;1112;1120;1139;1147;1155;1163;1171;1180;1198;1201;1210;1228;1236;1244;1252;1260;1279;2011;2038;2046;2054;2062;2070;2089;2097;2127;2135;2143;2151;2160;2178;2194;2216;2224;2232;2240;2259;2267;2275;2283;2291;2305;2313;2321;2330;3034;3069;3077;3085;3107;3115;3131;3204;3212;3220;3239;3247;3255;3263;3271;3280;3298;3306;3310;3999;4014;4022;4081;4090;4111;4124;5010;5029;5037')
            if 'indCoop' in dir(alteracao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.indCoop', alteracao.infoCadastro.indCoop.cdata, 0, '0;1;2;3')
            if 'indConstr' in dir(alteracao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.indConstr', alteracao.infoCadastro.indConstr.cdata, 0, '0;1')
            if 'indDesFolha' in dir(alteracao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.indDesFolha', alteracao.infoCadastro.indDesFolha.cdata, 1, '0;1')
            if 'indOptRegEletron' in dir(alteracao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.indOptRegEletron', alteracao.infoCadastro.indOptRegEletron.cdata, 1, '0;1')
            if 'indEntEd' in dir(alteracao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.indEntEd', alteracao.infoCadastro.indEntEd.cdata, 0, 'N;S')
            if 'indEtt' in dir(alteracao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.indEtt', alteracao.infoCadastro.indEtt.cdata, 1, 'N;S')
            if 'nrRegEtt' in dir(alteracao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.nrRegEtt', alteracao.infoCadastro.nrRegEtt.cdata, 0, '')
            if 'nmCtt' in dir(alteracao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.contato.nmCtt', alteracao.infoCadastro.contato.nmCtt.cdata, 1, '')
            if 'cpfCtt' in dir(alteracao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.contato.cpfCtt', alteracao.infoCadastro.contato.cpfCtt.cdata, 1, '')
            if 'foneFixo' in dir(alteracao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.contato.foneFixo', alteracao.infoCadastro.contato.foneFixo.cdata, 0, '')
            if 'foneCel' in dir(alteracao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.contato.foneCel', alteracao.infoCadastro.contato.foneCel.cdata, 0, '')
            if 'email' in dir(alteracao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.contato.email', alteracao.infoCadastro.contato.email.cdata, 0, '')

            if 'dadosIsencao' in dir(alteracao.infoCadastro):
                for dadosIsencao in alteracao.infoCadastro.dadosIsencao:
               
                    if 'ideMinLei' in dir(dadosIsencao): validacoes_lista = validar_campo(validacoes_lista,'dadosIsencao.ideMinLei', dadosIsencao.ideMinLei.cdata, 1, '')
                    if 'nrCertif' in dir(dadosIsencao): validacoes_lista = validar_campo(validacoes_lista,'dadosIsencao.nrCertif', dadosIsencao.nrCertif.cdata, 1, '')
                    if 'dtEmisCertif' in dir(dadosIsencao): validacoes_lista = validar_campo(validacoes_lista,'dadosIsencao.dtEmisCertif', dadosIsencao.dtEmisCertif.cdata, 1, '')
                    if 'dtVencCertif' in dir(dadosIsencao): validacoes_lista = validar_campo(validacoes_lista,'dadosIsencao.dtVencCertif', dadosIsencao.dtVencCertif.cdata, 1, '')
                    if 'nrProtRenov' in dir(dadosIsencao): validacoes_lista = validar_campo(validacoes_lista,'dadosIsencao.nrProtRenov', dadosIsencao.nrProtRenov.cdata, 0, '')
                    if 'dtProtRenov' in dir(dadosIsencao): validacoes_lista = validar_campo(validacoes_lista,'dadosIsencao.dtProtRenov', dadosIsencao.dtProtRenov.cdata, 0, '')
                    if 'dtDou' in dir(dadosIsencao): validacoes_lista = validar_campo(validacoes_lista,'dadosIsencao.dtDou', dadosIsencao.dtDou.cdata, 0, '')
                    if 'pagDou' in dir(dadosIsencao): validacoes_lista = validar_campo(validacoes_lista,'dadosIsencao.pagDou', dadosIsencao.pagDou.cdata, 0, '')
   
            if 'infoOP' in dir(alteracao.infoCadastro):
                for infoOP in alteracao.infoCadastro.infoOP:
               
                    if 'nrSiafi' in dir(infoOP): validacoes_lista = validar_campo(validacoes_lista,'infoOP.nrSiafi', infoOP.nrSiafi.cdata, 1, '')
                    if 'indUGRPPS' in dir(infoOP): validacoes_lista = validar_campo(validacoes_lista,'infoOP.indUGRPPS', infoOP.indUGRPPS.cdata, 1, 'S;N')
                    if 'esferaOP' in dir(infoOP): validacoes_lista = validar_campo(validacoes_lista,'infoOP.esferaOP', infoOP.esferaOP.cdata, 0, '1;2;3')
                    if 'poderOP' in dir(infoOP): validacoes_lista = validar_campo(validacoes_lista,'infoOP.poderOP', infoOP.poderOP.cdata, 1, '1;2;3;4;5;6')
                    if 'vrTetoRem' in dir(infoOP): validacoes_lista = validar_campo(validacoes_lista,'infoOP.vrTetoRem', infoOP.vrTetoRem.cdata, 1, '')
                    if 'ideEFR' in dir(infoOP): validacoes_lista = validar_campo(validacoes_lista,'infoOP.ideEFR', infoOP.ideEFR.cdata, 1, 'S;N')
                    if 'cnpjEFR' in dir(infoOP): validacoes_lista = validar_campo(validacoes_lista,'infoOP.cnpjEFR', infoOP.cnpjEFR.cdata, 0, '')
   
            if 'infoOrgInternacional' in dir(alteracao.infoCadastro):
                for infoOrgInternacional in alteracao.infoCadastro.infoOrgInternacional:
               
                    if 'indAcordoIsenMulta' in dir(infoOrgInternacional): validacoes_lista = validar_campo(validacoes_lista,'infoOrgInternacional.indAcordoIsenMulta', infoOrgInternacional.indAcordoIsenMulta.cdata, 1, '0;1')
   
            if 'softwareHouse' in dir(alteracao.infoCadastro):
                for softwareHouse in alteracao.infoCadastro.softwareHouse:
               
                    if 'cnpjSoftHouse' in dir(softwareHouse): validacoes_lista = validar_campo(validacoes_lista,'softwareHouse.cnpjSoftHouse', softwareHouse.cnpjSoftHouse.cdata, 1, '')
                    if 'nmRazao' in dir(softwareHouse): validacoes_lista = validar_campo(validacoes_lista,'softwareHouse.nmRazao', softwareHouse.nmRazao.cdata, 1, '')
                    if 'nmCont' in dir(softwareHouse): validacoes_lista = validar_campo(validacoes_lista,'softwareHouse.nmCont', softwareHouse.nmCont.cdata, 1, '')
                    if 'telefone' in dir(softwareHouse): validacoes_lista = validar_campo(validacoes_lista,'softwareHouse.telefone', softwareHouse.telefone.cdata, 1, '')
                    if 'email' in dir(softwareHouse): validacoes_lista = validar_campo(validacoes_lista,'softwareHouse.email', softwareHouse.email.cdata, 0, '')
   
            if 'situacaoPJ' in dir(alteracao.infoCadastro.infoComplementares):
                for situacaoPJ in alteracao.infoCadastro.infoComplementares.situacaoPJ:
               
                    if 'indSitPJ' in dir(situacaoPJ): validacoes_lista = validar_campo(validacoes_lista,'situacaoPJ.indSitPJ', situacaoPJ.indSitPJ.cdata, 1, '0;1;2;3;4')
   
            if 'situacaoPF' in dir(alteracao.infoCadastro.infoComplementares):
                for situacaoPF in alteracao.infoCadastro.infoComplementares.situacaoPF:
               
                    if 'indSitPF' in dir(situacaoPF): validacoes_lista = validar_campo(validacoes_lista,'situacaoPF.indSitPF', situacaoPF.indSitPF.cdata, 1, '0;1;2')
   
            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
               
                    if 'iniValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.iniValid', novaValidade.iniValid.cdata, 1, '')
                    if 'fimValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.fimValid', novaValidade.fimValid.cdata, 0, '')
   
    if 'exclusao' in dir(evtInfoEmpregador.infoEmpregador):
        for exclusao in evtInfoEmpregador.infoEmpregador.exclusao:
       
            if 'iniValid' in dir(exclusao.idePeriodo): validacoes_lista = validar_campo(validacoes_lista,'exclusao.idePeriodo.iniValid', exclusao.idePeriodo.iniValid.cdata, 1, '')
            if 'fimValid' in dir(exclusao.idePeriodo): validacoes_lista = validar_campo(validacoes_lista,'exclusao.idePeriodo.fimValid', exclusao.idePeriodo.fimValid.cdata, 0, '')

    return validacoes_lista