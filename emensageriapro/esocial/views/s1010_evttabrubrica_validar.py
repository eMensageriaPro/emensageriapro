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


def validacoes_s1010_evttabrubrica(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabRubrica = doc.eSocial.evtTabRubrica

    if 'tpAmb' in dir(evtTabRubrica.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabRubrica.ideEvento.tpAmb', evtTabRubrica.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtTabRubrica.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabRubrica.ideEvento.procEmi', evtTabRubrica.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtTabRubrica.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabRubrica.ideEvento.verProc', evtTabRubrica.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtTabRubrica.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabRubrica.ideEmpregador.tpInsc', evtTabRubrica.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtTabRubrica.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabRubrica.ideEmpregador.nrInsc', evtTabRubrica.ideEmpregador.nrInsc.cdata, 1, '')
    if 'inclusao' in dir(evtTabRubrica.infoRubrica):
        for inclusao in evtTabRubrica.infoRubrica.inclusao:
       
            if 'codRubr' in dir(inclusao.ideRubrica): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideRubrica.codRubr', inclusao.ideRubrica.codRubr.cdata, 1, '')
            if 'ideTabRubr' in dir(inclusao.ideRubrica): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideRubrica.ideTabRubr', inclusao.ideRubrica.ideTabRubr.cdata, 1, '')
            if 'iniValid' in dir(inclusao.ideRubrica): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideRubrica.iniValid', inclusao.ideRubrica.iniValid.cdata, 1, '')
            if 'fimValid' in dir(inclusao.ideRubrica): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideRubrica.fimValid', inclusao.ideRubrica.fimValid.cdata, 0, '')
            if 'dscRubr' in dir(inclusao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosRubrica.dscRubr', inclusao.dadosRubrica.dscRubr.cdata, 1, '')
            if 'natRubr' in dir(inclusao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosRubrica.natRubr', inclusao.dadosRubrica.natRubr.cdata, 1, '1000;1002;1003;1004;1005;1006;1007;1009;1010;1011;1020;1021;1022;1023;1024;1040;1041;1050;1080;1099;1201;1202;1203;1204;1205;1206;1207;1208;1209;1210;1211;1212;1213;1214;1215;1225;1230;1299;1300;1350;1351;1352;1401;1402;1403;1404;1405;1406;1407;1409;1410;1601;1602;1620;1621;1623;1629;1651;1652;1801;1802;1805;1810;2501;2510;2801;2901;2902;2920;2930;2999;3501;3505;3506;3508;3509;3520;4010;4050;4051;5001;5005;5501;5504;5510;6000;6001;6002;6003;6004;6006;6007;6101;6102;6103;6104;6105;6106;6107;6129;6901;6904;7001;7002;7003;7004;7005;9200;9201;9203;9205;9209;9210;9213;9214;9216;9217;9218;9219;9220;9221;9222;9223;9224;9225;9226;9230;9231;9232;9233;9250;9254;9255;9258;9270;9290;9299;9901;9902;9903;9904;9905;9906;9908;9910;9911;9930;9931;9932;9933;9938;9939;9950;9951;9989')
            if 'tpRubr' in dir(inclusao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosRubrica.tpRubr', inclusao.dadosRubrica.tpRubr.cdata, 1, '1;2;3;4')
            if 'codIncCP' in dir(inclusao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosRubrica.codIncCP', inclusao.dadosRubrica.codIncCP.cdata, 1, '00;01;11;12;13;14;15;16;21;22;23;24;25;26;31;32;34;35;51;61;91;92;93;94;95;96;97;98')
            if 'codIncIRRF' in dir(inclusao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosRubrica.codIncIRRF', inclusao.dadosRubrica.codIncIRRF.cdata, 1, '00;01;09;11;12;13;14;15;31;32;33;34;35;41;42;43;44;46;47;51;52;53;54;55;61;62;63;64;70;71;72;73;74;75;76;77;78;79;81;82;83;91;92;93;94;95')
            if 'codIncFGTS' in dir(inclusao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosRubrica.codIncFGTS', inclusao.dadosRubrica.codIncFGTS.cdata, 1, '00;11;12;21;91')
            if 'codIncSIND' in dir(inclusao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosRubrica.codIncSIND', inclusao.dadosRubrica.codIncSIND.cdata, 1, '00;11;31;91')
            if 'codIncCPRP' in dir(inclusao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosRubrica.codIncCPRP', inclusao.dadosRubrica.codIncCPRP.cdata, 0, '00;01;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;31;32;33;34;35;36;41;42;51;52;91;92;93;94;95;96')
            if 'tetoRemun' in dir(inclusao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosRubrica.tetoRemun', inclusao.dadosRubrica.tetoRemun.cdata, 0, 'S;N')
            if 'observacao' in dir(inclusao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosRubrica.observacao', inclusao.dadosRubrica.observacao.cdata, 0, '')

            if 'ideProcessoCP' in dir(inclusao.dadosRubrica):
                for ideProcessoCP in inclusao.dadosRubrica.ideProcessoCP:
               
                    if 'tpProc' in dir(ideProcessoCP): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoCP.tpProc', ideProcessoCP.tpProc.cdata, 1, '1;2')
                    if 'nrProc' in dir(ideProcessoCP): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoCP.nrProc', ideProcessoCP.nrProc.cdata, 1, '')
                    if 'extDecisao' in dir(ideProcessoCP): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoCP.extDecisao', ideProcessoCP.extDecisao.cdata, 1, '1;2')
                    if 'codSusp' in dir(ideProcessoCP): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoCP.codSusp', ideProcessoCP.codSusp.cdata, 1, '')
                    if 'tpProc' in dir(ideProcessoCP): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoCP.tpProc', ideProcessoCP.tpProc.cdata, 1, '1;2')
                    if 'nrProc' in dir(ideProcessoCP): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoCP.nrProc', ideProcessoCP.nrProc.cdata, 1, '')
                    if 'extDecisao' in dir(ideProcessoCP): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoCP.extDecisao', ideProcessoCP.extDecisao.cdata, 1, '1;2;3')
   
            if 'ideProcessoIRRF' in dir(inclusao.dadosRubrica):
                for ideProcessoIRRF in inclusao.dadosRubrica.ideProcessoIRRF:
               
                    if 'nrProc' in dir(ideProcessoIRRF): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoIRRF.nrProc', ideProcessoIRRF.nrProc.cdata, 1, '')
                    if 'codSusp' in dir(ideProcessoIRRF): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoIRRF.codSusp', ideProcessoIRRF.codSusp.cdata, 1, '')
   
            if 'ideProcessoFGTS' in dir(inclusao.dadosRubrica):
                for ideProcessoFGTS in inclusao.dadosRubrica.ideProcessoFGTS:
               
                    if 'nrProc' in dir(ideProcessoFGTS): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoFGTS.nrProc', ideProcessoFGTS.nrProc.cdata, 1, '')
   
            if 'ideProcessoSIND' in dir(inclusao.dadosRubrica):
                for ideProcessoSIND in inclusao.dadosRubrica.ideProcessoSIND:
               
                    if 'nrProc' in dir(ideProcessoSIND): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoSIND.nrProc', ideProcessoSIND.nrProc.cdata, 1, '')
   
            if 'ideProcessoCPRP' in dir(inclusao.dadosRubrica):
                for ideProcessoCPRP in inclusao.dadosRubrica.ideProcessoCPRP:
               
   
    if 'alteracao' in dir(evtTabRubrica.infoRubrica):
        for alteracao in evtTabRubrica.infoRubrica.alteracao:
       
            if 'codRubr' in dir(alteracao.ideRubrica): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideRubrica.codRubr', alteracao.ideRubrica.codRubr.cdata, 1, '')
            if 'ideTabRubr' in dir(alteracao.ideRubrica): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideRubrica.ideTabRubr', alteracao.ideRubrica.ideTabRubr.cdata, 1, '')
            if 'iniValid' in dir(alteracao.ideRubrica): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideRubrica.iniValid', alteracao.ideRubrica.iniValid.cdata, 1, '')
            if 'fimValid' in dir(alteracao.ideRubrica): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideRubrica.fimValid', alteracao.ideRubrica.fimValid.cdata, 0, '')
            if 'dscRubr' in dir(alteracao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosRubrica.dscRubr', alteracao.dadosRubrica.dscRubr.cdata, 1, '')
            if 'natRubr' in dir(alteracao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosRubrica.natRubr', alteracao.dadosRubrica.natRubr.cdata, 1, '1000;1002;1003;1004;1005;1006;1007;1009;1010;1011;1020;1021;1022;1023;1024;1040;1041;1050;1080;1099;1201;1202;1203;1204;1205;1206;1207;1208;1209;1210;1211;1212;1213;1214;1215;1225;1230;1299;1300;1350;1351;1352;1401;1402;1403;1404;1405;1406;1407;1409;1410;1601;1602;1620;1621;1623;1629;1651;1652;1801;1802;1805;1810;2501;2510;2801;2901;2902;2920;2930;2999;3501;3505;3506;3508;3509;3520;4010;4050;4051;5001;5005;5501;5504;5510;6000;6001;6002;6003;6004;6006;6007;6101;6102;6103;6104;6105;6106;6107;6129;6901;6904;7001;7002;7003;7004;7005;9200;9201;9203;9205;9209;9210;9213;9214;9216;9217;9218;9219;9220;9221;9222;9223;9224;9225;9226;9230;9231;9232;9233;9250;9254;9255;9258;9270;9290;9299;9901;9902;9903;9904;9905;9906;9908;9910;9911;9930;9931;9932;9933;9938;9939;9950;9951;9989')
            if 'tpRubr' in dir(alteracao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosRubrica.tpRubr', alteracao.dadosRubrica.tpRubr.cdata, 1, '1;2;3;4')
            if 'codIncCP' in dir(alteracao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosRubrica.codIncCP', alteracao.dadosRubrica.codIncCP.cdata, 1, '00;01;11;12;13;14;15;16;21;22;23;24;25;26;31;32;34;35;51;61;91;92;93;94;95;96;97;98')
            if 'codIncIRRF' in dir(alteracao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosRubrica.codIncIRRF', alteracao.dadosRubrica.codIncIRRF.cdata, 1, '00;01;09;11;12;13;14;15;31;32;33;34;35;41;42;43;44;46;47;51;52;53;54;55;61;62;63;64;70;71;72;73;74;75;76;77;78;79;81;82;83;91;92;93;94;95')
            if 'codIncFGTS' in dir(alteracao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosRubrica.codIncFGTS', alteracao.dadosRubrica.codIncFGTS.cdata, 1, '00;11;12;21;91')
            if 'codIncSIND' in dir(alteracao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosRubrica.codIncSIND', alteracao.dadosRubrica.codIncSIND.cdata, 1, '00;11;31;91')
            if 'codIncCPRP' in dir(alteracao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosRubrica.codIncCPRP', alteracao.dadosRubrica.codIncCPRP.cdata, 0, '00;01;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;31;32;33;34;35;36;41;42;51;52;91;92;93;94;95;96')
            if 'tetoRemun' in dir(alteracao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosRubrica.tetoRemun', alteracao.dadosRubrica.tetoRemun.cdata, 0, 'S;N')
            if 'observacao' in dir(alteracao.dadosRubrica): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosRubrica.observacao', alteracao.dadosRubrica.observacao.cdata, 0, '')

            if 'ideProcessoCP' in dir(alteracao.dadosRubrica):
                for ideProcessoCP in alteracao.dadosRubrica.ideProcessoCP:
               
                    if 'tpProc' in dir(ideProcessoCP): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoCP.tpProc', ideProcessoCP.tpProc.cdata, 1, '1;2')
                    if 'nrProc' in dir(ideProcessoCP): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoCP.nrProc', ideProcessoCP.nrProc.cdata, 1, '')
                    if 'extDecisao' in dir(ideProcessoCP): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoCP.extDecisao', ideProcessoCP.extDecisao.cdata, 1, '1;2')
                    if 'codSusp' in dir(ideProcessoCP): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoCP.codSusp', ideProcessoCP.codSusp.cdata, 1, '')
                    if 'tpProc' in dir(ideProcessoCP): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoCP.tpProc', ideProcessoCP.tpProc.cdata, 1, '1;2')
                    if 'nrProc' in dir(ideProcessoCP): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoCP.nrProc', ideProcessoCP.nrProc.cdata, 1, '')
                    if 'extDecisao' in dir(ideProcessoCP): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoCP.extDecisao', ideProcessoCP.extDecisao.cdata, 1, '1;2;3')
   
            if 'ideProcessoIRRF' in dir(alteracao.dadosRubrica):
                for ideProcessoIRRF in alteracao.dadosRubrica.ideProcessoIRRF:
               
                    if 'nrProc' in dir(ideProcessoIRRF): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoIRRF.nrProc', ideProcessoIRRF.nrProc.cdata, 1, '')
                    if 'codSusp' in dir(ideProcessoIRRF): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoIRRF.codSusp', ideProcessoIRRF.codSusp.cdata, 1, '')
   
            if 'ideProcessoFGTS' in dir(alteracao.dadosRubrica):
                for ideProcessoFGTS in alteracao.dadosRubrica.ideProcessoFGTS:
               
                    if 'nrProc' in dir(ideProcessoFGTS): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoFGTS.nrProc', ideProcessoFGTS.nrProc.cdata, 1, '')
   
            if 'ideProcessoSIND' in dir(alteracao.dadosRubrica):
                for ideProcessoSIND in alteracao.dadosRubrica.ideProcessoSIND:
               
                    if 'nrProc' in dir(ideProcessoSIND): validacoes_lista = validar_campo(validacoes_lista,'ideProcessoSIND.nrProc', ideProcessoSIND.nrProc.cdata, 1, '')
   
            if 'ideProcessoCPRP' in dir(alteracao.dadosRubrica):
                for ideProcessoCPRP in alteracao.dadosRubrica.ideProcessoCPRP:
               
   
            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
               
                    if 'iniValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.iniValid', novaValidade.iniValid.cdata, 1, '')
                    if 'fimValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.fimValid', novaValidade.fimValid.cdata, 0, '')
   
    if 'exclusao' in dir(evtTabRubrica.infoRubrica):
        for exclusao in evtTabRubrica.infoRubrica.exclusao:
       
            if 'codRubr' in dir(exclusao.ideRubrica): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideRubrica.codRubr', exclusao.ideRubrica.codRubr.cdata, 1, '')
            if 'ideTabRubr' in dir(exclusao.ideRubrica): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideRubrica.ideTabRubr', exclusao.ideRubrica.ideTabRubr.cdata, 1, '')
            if 'iniValid' in dir(exclusao.ideRubrica): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideRubrica.iniValid', exclusao.ideRubrica.iniValid.cdata, 1, '')
            if 'fimValid' in dir(exclusao.ideRubrica): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideRubrica.fimValid', exclusao.ideRubrica.fimValid.cdata, 0, '')

    return validacoes_lista