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


def validacoes_s1210_evtpgtos(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtPgtos = doc.eSocial.evtPgtos

    if 'indRetif' in dir(evtPgtos.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtPgtos.ideEvento.indRetif', evtPgtos.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtPgtos.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtPgtos.ideEvento.nrRecibo', evtPgtos.ideEvento.nrRecibo.cdata, 0, '')
    if 'indApuracao' in dir(evtPgtos.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtPgtos.ideEvento.indApuracao', evtPgtos.ideEvento.indApuracao.cdata, 1, '1')
    if 'perApur' in dir(evtPgtos.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtPgtos.ideEvento.perApur', evtPgtos.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtPgtos.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtPgtos.ideEvento.tpAmb', evtPgtos.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtPgtos.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtPgtos.ideEvento.procEmi', evtPgtos.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtPgtos.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtPgtos.ideEvento.verProc', evtPgtos.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtPgtos.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtPgtos.ideEmpregador.tpInsc', evtPgtos.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtPgtos.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtPgtos.ideEmpregador.nrInsc', evtPgtos.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfBenef' in dir(evtPgtos.ideBenef): validacoes_lista = validar_campo(validacoes_lista,'evtPgtos.ideBenef.cpfBenef', evtPgtos.ideBenef.cpfBenef.cdata, 1, '')
    if 'deps' in dir(evtPgtos.ideBenef):
        for deps in evtPgtos.ideBenef.deps:
       
            if 'vrDedDep' in dir(deps): validacoes_lista = validar_campo(validacoes_lista,'deps.vrDedDep', deps.vrDedDep.cdata, 1, '')

    if 'infoPgto' in dir(evtPgtos.ideBenef):
        for infoPgto in evtPgtos.ideBenef.infoPgto:
       
            if 'dtPgto' in dir(infoPgto): validacoes_lista = validar_campo(validacoes_lista,'infoPgto.dtPgto', infoPgto.dtPgto.cdata, 1, '')
            if 'tpPgto' in dir(infoPgto): validacoes_lista = validar_campo(validacoes_lista,'infoPgto.tpPgto', infoPgto.tpPgto.cdata, 1, '1;2;3;5;6;7;9')
            if 'indResBr' in dir(infoPgto): validacoes_lista = validar_campo(validacoes_lista,'infoPgto.indResBr', infoPgto.indResBr.cdata, 1, 'S;N')

            if 'detPgtoFl' in dir(infoPgto):
                for detPgtoFl in infoPgto.detPgtoFl:
               
                    if 'perRef' in dir(detPgtoFl): validacoes_lista = validar_campo(validacoes_lista,'detPgtoFl.perRef', detPgtoFl.perRef.cdata, 0, '')
                    if 'ideDmDev' in dir(detPgtoFl): validacoes_lista = validar_campo(validacoes_lista,'detPgtoFl.ideDmDev', detPgtoFl.ideDmDev.cdata, 1, '')
                    if 'indPgtoTt' in dir(detPgtoFl): validacoes_lista = validar_campo(validacoes_lista,'detPgtoFl.indPgtoTt', detPgtoFl.indPgtoTt.cdata, 1, 'S;N')
                    if 'vrLiq' in dir(detPgtoFl): validacoes_lista = validar_campo(validacoes_lista,'detPgtoFl.vrLiq', detPgtoFl.vrLiq.cdata, 1, '')
                    if 'nrRecArq' in dir(detPgtoFl): validacoes_lista = validar_campo(validacoes_lista,'detPgtoFl.nrRecArq', detPgtoFl.nrRecArq.cdata, 0, '')
   
            if 'detPgtoBenPr' in dir(infoPgto):
                for detPgtoBenPr in infoPgto.detPgtoBenPr:
               
                    if 'perRef' in dir(detPgtoBenPr): validacoes_lista = validar_campo(validacoes_lista,'detPgtoBenPr.perRef', detPgtoBenPr.perRef.cdata, 1, '')
                    if 'ideDmDev' in dir(detPgtoBenPr): validacoes_lista = validar_campo(validacoes_lista,'detPgtoBenPr.ideDmDev', detPgtoBenPr.ideDmDev.cdata, 1, '')
                    if 'indPgtoTt' in dir(detPgtoBenPr): validacoes_lista = validar_campo(validacoes_lista,'detPgtoBenPr.indPgtoTt', detPgtoBenPr.indPgtoTt.cdata, 1, 'S;N')
                    if 'vrLiq' in dir(detPgtoBenPr): validacoes_lista = validar_campo(validacoes_lista,'detPgtoBenPr.vrLiq', detPgtoBenPr.vrLiq.cdata, 1, '')
   
            if 'detPgtoFer' in dir(infoPgto):
                for detPgtoFer in infoPgto.detPgtoFer:
               
                    if 'codCateg' in dir(detPgtoFer): validacoes_lista = validar_campo(validacoes_lista,'detPgtoFer.codCateg', detPgtoFer.codCateg.cdata, 1, '101;102;103;104;105;106;111;201;202;301;302;303;305;306;307;308;309;401;410;701;711;712;721;722;723;731;734;738;741;751;761;771;781;901;902;903;904;905')
                    if 'matricula' in dir(detPgtoFer): validacoes_lista = validar_campo(validacoes_lista,'detPgtoFer.matricula', detPgtoFer.matricula.cdata, 0, '')
                    if 'dtIniGoz' in dir(detPgtoFer): validacoes_lista = validar_campo(validacoes_lista,'detPgtoFer.dtIniGoz', detPgtoFer.dtIniGoz.cdata, 1, '')
                    if 'qtDias' in dir(detPgtoFer): validacoes_lista = validar_campo(validacoes_lista,'detPgtoFer.qtDias', detPgtoFer.qtDias.cdata, 1, '')
                    if 'vrLiq' in dir(detPgtoFer): validacoes_lista = validar_campo(validacoes_lista,'detPgtoFer.vrLiq', detPgtoFer.vrLiq.cdata, 1, '')
   
            if 'detPgtoAnt' in dir(infoPgto):
                for detPgtoAnt in infoPgto.detPgtoAnt:
               
                    if 'codCateg' in dir(detPgtoAnt): validacoes_lista = validar_campo(validacoes_lista,'detPgtoAnt.codCateg', detPgtoAnt.codCateg.cdata, 1, '101;102;103;104;105;106;111;201;202;301;302;303;305;306;307;308;309;401;410;701;711;712;721;722;723;731;734;738;741;751;761;771;781;901;902;903;904;905')
   
            if 'idePgtoExt' in dir(infoPgto):
                for idePgtoExt in infoPgto.idePgtoExt:
               
                    if 'codPais' in dir(idePgtoExt): validacoes_lista = validar_campo(validacoes_lista,'idePgtoExt.codPais', idePgtoExt.codPais.cdata, 1, '008;040;329;331;334;337;341;345;351;355;357;358;041;359;361;365;367;369;372;375;379;383;386;043;388;391;395;396;399;403;411;420;423;426;047;427;431;434;438;440;442;445;447;449;450;053;452;455;458;461;464;467;472;474;476;477;059;485;488;490;493;494;495;497;499;501;505;063;507;508;511;517;521;525;528;531;535;538;064;542;545;548;551;556;563;566;569;573;575;065;576;578;580;583;586;589;593;599;603;607;069;611;623;625;628;640;647;660;665;670;675;009;072;676;677;678;685;687;690;691;695;697;700;073;705;710;715;720;728;731;735;738;741;744;077;748;750;754;756;759;764;767;770;772;776;080;780;782;783;785;788;790;791;795;800;805;081;810;815;820;823;824;827;828;831;833;840;083;845;847;848;850;855;858;863;866;870;873;085;875;888;890;087;088;090;013;093;097;098;100;101;105;106;108;111;115;017;119;127;131;137;141;145;149;150;151;152;020;153;154;158;160;161;163;165;169;173;177;023;183;187;190;193;195;196;198;199;229;232;025;235;237;239;240;243;244;245;246;247;249;031;251;253;255;259;263;267;271;275;281;285;037;289;291;293;297;301;305;309;313;317;325')
                    if 'indNIF' in dir(idePgtoExt): validacoes_lista = validar_campo(validacoes_lista,'idePgtoExt.indNIF', idePgtoExt.indNIF.cdata, 1, '1;2;3')
                    if 'nifBenef' in dir(idePgtoExt): validacoes_lista = validar_campo(validacoes_lista,'idePgtoExt.nifBenef', idePgtoExt.nifBenef.cdata, 0, '')
                    if 'dscLograd' in dir(idePgtoExt): validacoes_lista = validar_campo(validacoes_lista,'idePgtoExt.dscLograd', idePgtoExt.dscLograd.cdata, 1, '')
                    if 'nrLograd' in dir(idePgtoExt): validacoes_lista = validar_campo(validacoes_lista,'idePgtoExt.nrLograd', idePgtoExt.nrLograd.cdata, 0, '')
                    if 'complem' in dir(idePgtoExt): validacoes_lista = validar_campo(validacoes_lista,'idePgtoExt.complem', idePgtoExt.complem.cdata, 0, '')
                    if 'bairro' in dir(idePgtoExt): validacoes_lista = validar_campo(validacoes_lista,'idePgtoExt.bairro', idePgtoExt.bairro.cdata, 0, '')
                    if 'nmCid' in dir(idePgtoExt): validacoes_lista = validar_campo(validacoes_lista,'idePgtoExt.nmCid', idePgtoExt.nmCid.cdata, 1, '')
                    if 'codPostal' in dir(idePgtoExt): validacoes_lista = validar_campo(validacoes_lista,'idePgtoExt.codPostal', idePgtoExt.codPostal.cdata, 0, '')
   
    return validacoes_lista