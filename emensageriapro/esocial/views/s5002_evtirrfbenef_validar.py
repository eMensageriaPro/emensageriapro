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


def validacoes_s5002_evtirrfbenef(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtIrrfBenef = doc.eSocial.evtIrrfBenef

    if 'nrRecArqBase' in dir(evtIrrfBenef.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtIrrfBenef.ideEvento.nrRecArqBase', evtIrrfBenef.ideEvento.nrRecArqBase.cdata, 1, '')
    if 'perApur' in dir(evtIrrfBenef.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtIrrfBenef.ideEvento.perApur', evtIrrfBenef.ideEvento.perApur.cdata, 1, '')
    if 'tpInsc' in dir(evtIrrfBenef.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtIrrfBenef.ideEmpregador.tpInsc', evtIrrfBenef.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtIrrfBenef.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtIrrfBenef.ideEmpregador.nrInsc', evtIrrfBenef.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtIrrfBenef.ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtIrrfBenef.ideTrabalhador.cpfTrab', evtIrrfBenef.ideTrabalhador.cpfTrab.cdata, 1, '')
    if 'infoDep' in dir(evtIrrfBenef):
        for infoDep in evtIrrfBenef.infoDep:
       
            if 'vrDedDep' in dir(infoDep): validacoes_lista = validar_campo(validacoes_lista,'infoDep.vrDedDep', infoDep.vrDedDep.cdata, 1, '')

    if 'infoIrrf' in dir(evtIrrfBenef):
        for infoIrrf in evtIrrfBenef.infoIrrf:
       
            if 'codCateg' in dir(infoIrrf): validacoes_lista = validar_campo(validacoes_lista,'infoIrrf.codCateg', infoIrrf.codCateg.cdata, 0, '101;102;103;104;105;106;111;201;202;301;302;303;305;306;307;308;309;401;410;701;711;712;721;722;723;731;734;738;741;751;761;771;781;901;902;903;904;905')
            if 'indResBr' in dir(infoIrrf): validacoes_lista = validar_campo(validacoes_lista,'infoIrrf.indResBr', infoIrrf.indResBr.cdata, 1, 'S;N')

            if 'basesIrrf' in dir(infoIrrf):
                for basesIrrf in infoIrrf.basesIrrf:
               
                    if 'tpValor' in dir(basesIrrf): validacoes_lista = validar_campo(validacoes_lista,'basesIrrf.tpValor', basesIrrf.tpValor.cdata, 1, '')
                    if 'valor' in dir(basesIrrf): validacoes_lista = validar_campo(validacoes_lista,'basesIrrf.valor', basesIrrf.valor.cdata, 1, '')
   
            if 'irrf' in dir(infoIrrf):
                for irrf in infoIrrf.irrf:
               
                    if 'tpCR' in dir(irrf): validacoes_lista = validar_campo(validacoes_lista,'irrf.tpCR', irrf.tpCR.cdata, 1, '047301;056107;056108;056109;056110;056111;056112;056113;058806;061001;3280-06;3533;356201')
                    if 'vrIrrfDesc' in dir(irrf): validacoes_lista = validar_campo(validacoes_lista,'irrf.vrIrrfDesc', irrf.vrIrrfDesc.cdata, 1, '')
   
            if 'idePgtoExt' in dir(infoIrrf):
                for idePgtoExt in infoIrrf.idePgtoExt:
               
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