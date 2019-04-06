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


def validacoes_s2200_evtadmissao(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtAdmissao = doc.eSocial.evtAdmissao

    if 'indRetif' in dir(evtAdmissao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.ideEvento.indRetif', evtAdmissao.ideEvento.indRetif.cdata, 1, u'1;2')
    if 'nrRecibo' in dir(evtAdmissao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.ideEvento.nrRecibo', evtAdmissao.ideEvento.nrRecibo.cdata, 0, u'')
    if 'tpAmb' in dir(evtAdmissao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.ideEvento.tpAmb', evtAdmissao.ideEvento.tpAmb.cdata, 1, u'1;2')
    if 'procEmi' in dir(evtAdmissao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.ideEvento.procEmi', evtAdmissao.ideEvento.procEmi.cdata, 1, u'1;2;3;4;5')
    if 'verProc' in dir(evtAdmissao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.ideEvento.verProc', evtAdmissao.ideEvento.verProc.cdata, 1, u'')
    if 'tpInsc' in dir(evtAdmissao.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.ideEmpregador.tpInsc', evtAdmissao.ideEmpregador.tpInsc.cdata, 1, u'1;2;3;4')
    if 'nrInsc' in dir(evtAdmissao.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.ideEmpregador.nrInsc', evtAdmissao.ideEmpregador.nrInsc.cdata, 1, u'')
    if 'cpfTrab' in dir(evtAdmissao.trabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.trabalhador.cpfTrab', evtAdmissao.trabalhador.cpfTrab.cdata, 1, u'')
    if 'nisTrab' in dir(evtAdmissao.trabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.trabalhador.nisTrab', evtAdmissao.trabalhador.nisTrab.cdata, 1, u'')
    if 'nmTrab' in dir(evtAdmissao.trabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.trabalhador.nmTrab', evtAdmissao.trabalhador.nmTrab.cdata, 1, u'')
    if 'sexo' in dir(evtAdmissao.trabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.trabalhador.sexo', evtAdmissao.trabalhador.sexo.cdata, 1, u'M;F')
    if 'racaCor' in dir(evtAdmissao.trabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.trabalhador.racaCor', evtAdmissao.trabalhador.racaCor.cdata, 1, u'1;2;3;4;5;6')
    if 'estCiv' in dir(evtAdmissao.trabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.trabalhador.estCiv', evtAdmissao.trabalhador.estCiv.cdata, 0, u'1;2;3;4;5')
    if 'grauInstr' in dir(evtAdmissao.trabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.trabalhador.grauInstr', evtAdmissao.trabalhador.grauInstr.cdata, 1, u'01;02;03;04;05;06;07;08;09;10;11;12')
    if 'indPriEmpr' in dir(evtAdmissao.trabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.trabalhador.indPriEmpr', evtAdmissao.trabalhador.indPriEmpr.cdata, 0, u'S;N')
    if 'nmSoc' in dir(evtAdmissao.trabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.trabalhador.nmSoc', evtAdmissao.trabalhador.nmSoc.cdata, 0, u'')
    if 'dtNascto' in dir(evtAdmissao.trabalhador.nascimento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.trabalhador.nascimento.dtNascto', evtAdmissao.trabalhador.nascimento.dtNascto.cdata, 1, u'')
    if 'codMunic' in dir(evtAdmissao.trabalhador.nascimento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.trabalhador.nascimento.codMunic', evtAdmissao.trabalhador.nascimento.codMunic.cdata, 0, u'')
    if 'uf' in dir(evtAdmissao.trabalhador.nascimento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.trabalhador.nascimento.uf', evtAdmissao.trabalhador.nascimento.uf.cdata, 0, u'')
    if 'paisNascto' in dir(evtAdmissao.trabalhador.nascimento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.trabalhador.nascimento.paisNascto', evtAdmissao.trabalhador.nascimento.paisNascto.cdata, 1, u'008;040;329;331;334;337;341;345;351;355;357;358;041;359;361;365;367;369;372;375;379;383;386;043;388;391;395;396;399;403;411;420;423;426;047;427;431;434;438;440;442;445;447;449;450;053;452;455;458;461;464;467;472;474;476;477;059;485;488;490;493;494;495;497;499;501;505;063;507;508;511;517;521;525;528;531;535;538;064;542;545;548;551;556;563;566;569;573;575;065;576;578;580;583;586;589;593;599;603;607;069;611;623;625;628;640;647;660;665;670;675;009;072;676;677;678;685;687;690;691;695;697;700;073;705;710;715;720;728;731;735;738;741;744;077;748;750;754;756;759;764;767;770;772;776;080;780;782;783;785;788;790;791;795;800;805;081;810;815;820;823;824;827;828;831;833;840;083;845;847;848;850;855;858;863;866;870;873;085;875;888;890;087;088;090;013;093;097;098;100;101;105;106;108;111;115;017;119;127;131;137;141;145;149;150;151;152;020;153;154;158;160;161;163;165;169;173;177;023;183;187;190;193;195;196;198;199;229;232;025;235;237;239;240;243;244;245;246;247;249;031;251;253;255;259;263;267;271;275;281;285;037;289;291;293;297;301;305;309;313;317;325')
    if 'paisNac' in dir(evtAdmissao.trabalhador.nascimento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.trabalhador.nascimento.paisNac', evtAdmissao.trabalhador.nascimento.paisNac.cdata, 1, u'008;040;329;331;334;337;341;345;351;355;357;358;041;359;361;365;367;369;372;375;379;383;386;043;388;391;395;396;399;403;411;420;423;426;047;427;431;434;438;440;442;445;447;449;450;053;452;455;458;461;464;467;472;474;476;477;059;485;488;490;493;494;495;497;499;501;505;063;507;508;511;517;521;525;528;531;535;538;064;542;545;548;551;556;563;566;569;573;575;065;576;578;580;583;586;589;593;599;603;607;069;611;623;625;628;640;647;660;665;670;675;009;072;676;677;678;685;687;690;691;695;697;700;073;705;710;715;720;728;731;735;738;741;744;077;748;750;754;756;759;764;767;770;772;776;080;780;782;783;785;788;790;791;795;800;805;081;810;815;820;823;824;827;828;831;833;840;083;845;847;848;850;855;858;863;866;870;873;085;875;888;890;087;088;090;013;093;097;098;100;101;105;106;108;111;115;017;119;127;131;137;141;145;149;150;151;152;020;153;154;158;160;161;163;165;169;173;177;023;183;187;190;193;195;196;198;199;229;232;025;235;237;239;240;243;244;245;246;247;249;031;251;253;255;259;263;267;271;275;281;285;037;289;291;293;297;301;305;309;313;317;325')
    if 'nmMae' in dir(evtAdmissao.trabalhador.nascimento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.trabalhador.nascimento.nmMae', evtAdmissao.trabalhador.nascimento.nmMae.cdata, 0, u'')
    if 'nmPai' in dir(evtAdmissao.trabalhador.nascimento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.trabalhador.nascimento.nmPai', evtAdmissao.trabalhador.nascimento.nmPai.cdata, 0, u'')
    if 'matricula' in dir(evtAdmissao.vinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.matricula', evtAdmissao.vinculo.matricula.cdata, 1, u'')
    if 'tpRegTrab' in dir(evtAdmissao.vinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.tpRegTrab', evtAdmissao.vinculo.tpRegTrab.cdata, 1, u'1;2')
    if 'tpRegPrev' in dir(evtAdmissao.vinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.tpRegPrev', evtAdmissao.vinculo.tpRegPrev.cdata, 1, u'1;2;3')
    if 'nrRecInfPrelim' in dir(evtAdmissao.vinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.nrRecInfPrelim', evtAdmissao.vinculo.nrRecInfPrelim.cdata, 0, u'')
    if 'cadIni' in dir(evtAdmissao.vinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.cadIni', evtAdmissao.vinculo.cadIni.cdata, 1, u'S;N')
    if 'codCargo' in dir(evtAdmissao.vinculo.infoContrato): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.infoContrato.codCargo', evtAdmissao.vinculo.infoContrato.codCargo.cdata, 0, u'')
    if 'dtIngrCargo' in dir(evtAdmissao.vinculo.infoContrato): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.infoContrato.dtIngrCargo', evtAdmissao.vinculo.infoContrato.dtIngrCargo.cdata, 0, u'')
    if 'codFuncao' in dir(evtAdmissao.vinculo.infoContrato): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.infoContrato.codFuncao', evtAdmissao.vinculo.infoContrato.codFuncao.cdata, 0, u'')
    if 'codCateg' in dir(evtAdmissao.vinculo.infoContrato): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.infoContrato.codCateg', evtAdmissao.vinculo.infoContrato.codCateg.cdata, 1, u'101;102;103;104;105;106;111;201;202;301;302;303;305;306;307;308;309;401;410;701;711;712;721;722;723;731;734;738;741;751;761;771;781;901;902;903;904;905')
    if 'codCarreira' in dir(evtAdmissao.vinculo.infoContrato): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.infoContrato.codCarreira', evtAdmissao.vinculo.infoContrato.codCarreira.cdata, 0, u'')
    if 'dtIngrCarr' in dir(evtAdmissao.vinculo.infoContrato): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.infoContrato.dtIngrCarr', evtAdmissao.vinculo.infoContrato.dtIngrCarr.cdata, 0, u'')
    if 'vrSalFx' in dir(evtAdmissao.vinculo.infoContrato.remuneracao): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.infoContrato.remuneracao.vrSalFx', evtAdmissao.vinculo.infoContrato.remuneracao.vrSalFx.cdata, 1, u'')
    if 'undSalFixo' in dir(evtAdmissao.vinculo.infoContrato.remuneracao): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.infoContrato.remuneracao.undSalFixo', evtAdmissao.vinculo.infoContrato.remuneracao.undSalFixo.cdata, 1, u'1;2;3;4;5;6;7')
    if 'dscSalVar' in dir(evtAdmissao.vinculo.infoContrato.remuneracao): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.infoContrato.remuneracao.dscSalVar', evtAdmissao.vinculo.infoContrato.remuneracao.dscSalVar.cdata, 0, u'')
    if 'tpContr' in dir(evtAdmissao.vinculo.infoContrato.duracao): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.infoContrato.duracao.tpContr', evtAdmissao.vinculo.infoContrato.duracao.tpContr.cdata, 1, u'1;2')
    if 'dtTerm' in dir(evtAdmissao.vinculo.infoContrato.duracao): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.infoContrato.duracao.dtTerm', evtAdmissao.vinculo.infoContrato.duracao.dtTerm.cdata, 0, u'')
    if 'clauAssec' in dir(evtAdmissao.vinculo.infoContrato.duracao): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.infoContrato.duracao.clauAssec', evtAdmissao.vinculo.infoContrato.duracao.clauAssec.cdata, 0, u'S;N')
    if 'objDet' in dir(evtAdmissao.vinculo.infoContrato.duracao): validacoes_lista = validar_campo(validacoes_lista,'evtAdmissao.vinculo.infoContrato.duracao.objDet', evtAdmissao.vinculo.infoContrato.duracao.objDet.cdata, 0, u'')
    if 'CTPS' in dir(evtAdmissao.trabalhador.documentos):
        for CTPS in evtAdmissao.trabalhador.documentos.CTPS:

            if 'nrCtps' in dir(CTPS): validacoes_lista = validar_campo(validacoes_lista,'CTPS.nrCtps', CTPS.nrCtps.cdata, 1, u'')
            if 'serieCtps' in dir(CTPS): validacoes_lista = validar_campo(validacoes_lista,'CTPS.serieCtps', CTPS.serieCtps.cdata, 1, u'')
            if 'ufCtps' in dir(CTPS): validacoes_lista = validar_campo(validacoes_lista,'CTPS.ufCtps', CTPS.ufCtps.cdata, 1, u'')

    if 'RIC' in dir(evtAdmissao.trabalhador.documentos):
        for RIC in evtAdmissao.trabalhador.documentos.RIC:

            if 'nrRic' in dir(RIC): validacoes_lista = validar_campo(validacoes_lista,'RIC.nrRic', RIC.nrRic.cdata, 1, u'')
            if 'orgaoEmissor' in dir(RIC): validacoes_lista = validar_campo(validacoes_lista,'RIC.orgaoEmissor', RIC.orgaoEmissor.cdata, 1, u'')
            if 'dtExped' in dir(RIC): validacoes_lista = validar_campo(validacoes_lista,'RIC.dtExped', RIC.dtExped.cdata, 0, u'')

    if 'RG' in dir(evtAdmissao.trabalhador.documentos):
        for RG in evtAdmissao.trabalhador.documentos.RG:

            if 'nrRg' in dir(RG): validacoes_lista = validar_campo(validacoes_lista,'RG.nrRg', RG.nrRg.cdata, 1, u'')
            if 'orgaoEmissor' in dir(RG): validacoes_lista = validar_campo(validacoes_lista,'RG.orgaoEmissor', RG.orgaoEmissor.cdata, 1, u'')
            if 'dtExped' in dir(RG): validacoes_lista = validar_campo(validacoes_lista,'RG.dtExped', RG.dtExped.cdata, 0, u'')

    if 'RNE' in dir(evtAdmissao.trabalhador.documentos):
        for RNE in evtAdmissao.trabalhador.documentos.RNE:

            if 'nrRne' in dir(RNE): validacoes_lista = validar_campo(validacoes_lista,'RNE.nrRne', RNE.nrRne.cdata, 1, u'')
            if 'orgaoEmissor' in dir(RNE): validacoes_lista = validar_campo(validacoes_lista,'RNE.orgaoEmissor', RNE.orgaoEmissor.cdata, 1, u'')
            if 'dtExped' in dir(RNE): validacoes_lista = validar_campo(validacoes_lista,'RNE.dtExped', RNE.dtExped.cdata, 0, u'')

    if 'OC' in dir(evtAdmissao.trabalhador.documentos):
        for OC in evtAdmissao.trabalhador.documentos.OC:

            if 'nrOc' in dir(OC): validacoes_lista = validar_campo(validacoes_lista,'OC.nrOc', OC.nrOc.cdata, 1, u'')
            if 'orgaoEmissor' in dir(OC): validacoes_lista = validar_campo(validacoes_lista,'OC.orgaoEmissor', OC.orgaoEmissor.cdata, 1, u'')
            if 'dtExped' in dir(OC): validacoes_lista = validar_campo(validacoes_lista,'OC.dtExped', OC.dtExped.cdata, 0, u'')
            if 'dtValid' in dir(OC): validacoes_lista = validar_campo(validacoes_lista,'OC.dtValid', OC.dtValid.cdata, 0, u'')

    if 'CNH' in dir(evtAdmissao.trabalhador.documentos):
        for CNH in evtAdmissao.trabalhador.documentos.CNH:

            if 'nrRegCnh' in dir(CNH): validacoes_lista = validar_campo(validacoes_lista,'CNH.nrRegCnh', CNH.nrRegCnh.cdata, 1, u'')
            if 'dtExped' in dir(CNH): validacoes_lista = validar_campo(validacoes_lista,'CNH.dtExped', CNH.dtExped.cdata, 0, u'')
            if 'ufCnh' in dir(CNH): validacoes_lista = validar_campo(validacoes_lista,'CNH.ufCnh', CNH.ufCnh.cdata, 1, u'')
            if 'dtValid' in dir(CNH): validacoes_lista = validar_campo(validacoes_lista,'CNH.dtValid', CNH.dtValid.cdata, 1, u'')
            if 'dtPriHab' in dir(CNH): validacoes_lista = validar_campo(validacoes_lista,'CNH.dtPriHab', CNH.dtPriHab.cdata, 0, u'')
            if 'categoriaCnh' in dir(CNH): validacoes_lista = validar_campo(validacoes_lista,'CNH.categoriaCnh', CNH.categoriaCnh.cdata, 1, u'A;B;C;D;E;AB;AC;AD;AE')

    if 'brasil' in dir(evtAdmissao.trabalhador.endereco):
        for brasil in evtAdmissao.trabalhador.endereco.brasil:

            if 'tpLograd' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.tpLograd', brasil.tpLograd.cdata, 1, u'A;AC;ACA;ACL;AD;AE;AER;AL;AMD;AME;AN;ANT;ART;AT;ATL;A V;AV;AVC;AVM;AVV;BAL;BC;BCO;BEL;BL;BLO;BLS;BLV;BSQ;BVD;BX;C;CAL;CAM;CAN;CH;CHA;CIC;CIR;CJ;CJM;CMP;COL;COM;CON;COR;CPO;CRG;CTN;DSC;DSV;DT;EB;EIM;ENS;ENT;EQ;ESC;ESD;ESE;ESI;ESL;ESM;ESP;ESS;EST;ESV;ETA;ETC;ETD;ETN;ETP;ETT;EVA;EVD;EX;FAV;FAZ;FER;FNT;FRA;FTE;GAL;GJA;HAB;IA;IND;IOA;JD;JDE;LD;LGA;LGO;LOT;LRG;LT;MER;MNA;MOD;MRG;MRO;MTE;NUC;NUR;OUT;PAR;PAS;PAT;PC;PCE;PDA;PDO;PNT;PR;PRL;PRM;PRQ;PRR;PSA;PSG;PSP;PSS;PTE;PTO;Q;QTA;QTS;R;R I;R L;R P;R V;RAM;RCR;REC;RER;RES;RET;RLA;RMP;ROA;ROD;ROT;RPE;RPR;RTN;RTT;SEG;SIT;SRV;ST;SUB;TCH;TER;TR;TRV;TUN;TV;TVP;TVV;UNI;V;V C;V L;VAC;VAL;VCO;VD;V-E;VER;VEV;VL;VLA;VLE;VLT;VPE;VRT;ZIG')
            if 'dscLograd' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.dscLograd', brasil.dscLograd.cdata, 1, u'')
            if 'nrLograd' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.nrLograd', brasil.nrLograd.cdata, 1, u'')
            if 'complemento' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.complemento', brasil.complemento.cdata, 0, u'')
            if 'bairro' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.bairro', brasil.bairro.cdata, 0, u'')
            if 'cep' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.cep', brasil.cep.cdata, 1, u'')
            if 'codMunic' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.codMunic', brasil.codMunic.cdata, 1, u'')
            if 'uf' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.uf', brasil.uf.cdata, 1, u'')

    if 'exterior' in dir(evtAdmissao.trabalhador.endereco):
        for exterior in evtAdmissao.trabalhador.endereco.exterior:

            if 'paisResid' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.paisResid', exterior.paisResid.cdata, 1, u'008;040;329;331;334;337;341;345;351;355;357;358;041;359;361;365;367;369;372;375;379;383;386;043;388;391;395;396;399;403;411;420;423;426;047;427;431;434;438;440;442;445;447;449;450;053;452;455;458;461;464;467;472;474;476;477;059;485;488;490;493;494;495;497;499;501;505;063;507;508;511;517;521;525;528;531;535;538;064;542;545;548;551;556;563;566;569;573;575;065;576;578;580;583;586;589;593;599;603;607;069;611;623;625;628;640;647;660;665;670;675;009;072;676;677;678;685;687;690;691;695;697;700;073;705;710;715;720;728;731;735;738;741;744;077;748;750;754;756;759;764;767;770;772;776;080;780;782;783;785;788;790;791;795;800;805;081;810;815;820;823;824;827;828;831;833;840;083;845;847;848;850;855;858;863;866;870;873;085;875;888;890;087;088;090;013;093;097;098;100;101;105;106;108;111;115;017;119;127;131;137;141;145;149;150;151;152;020;153;154;158;160;161;163;165;169;173;177;023;183;187;190;193;195;196;198;199;229;232;025;235;237;239;240;243;244;245;246;247;249;031;251;253;255;259;263;267;271;275;281;285;037;289;291;293;297;301;305;309;313;317;325')
            if 'dscLograd' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.dscLograd', exterior.dscLograd.cdata, 1, u'')
            if 'nrLograd' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.nrLograd', exterior.nrLograd.cdata, 1, u'')
            if 'complemento' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.complemento', exterior.complemento.cdata, 0, u'')
            if 'bairro' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.bairro', exterior.bairro.cdata, 0, u'')
            if 'nmCid' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.nmCid', exterior.nmCid.cdata, 1, u'')
            if 'codPostal' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.codPostal', exterior.codPostal.cdata, 0, u'')

    if 'trabEstrangeiro' in dir(evtAdmissao.trabalhador):
        for trabEstrangeiro in evtAdmissao.trabalhador.trabEstrangeiro:

            if 'dtChegada' in dir(trabEstrangeiro): validacoes_lista = validar_campo(validacoes_lista,'trabEstrangeiro.dtChegada', trabEstrangeiro.dtChegada.cdata, 0, u'')
            if 'classTrabEstrang' in dir(trabEstrangeiro): validacoes_lista = validar_campo(validacoes_lista,'trabEstrangeiro.classTrabEstrang', trabEstrangeiro.classTrabEstrang.cdata, 1, u'1;2;3;4;5;6;7;8;9;10;11;12')
            if 'casadoBr' in dir(trabEstrangeiro): validacoes_lista = validar_campo(validacoes_lista,'trabEstrangeiro.casadoBr', trabEstrangeiro.casadoBr.cdata, 1, u'S;N')
            if 'filhosBr' in dir(trabEstrangeiro): validacoes_lista = validar_campo(validacoes_lista,'trabEstrangeiro.filhosBr', trabEstrangeiro.filhosBr.cdata, 1, u'S;N')

    if 'infoDeficiencia' in dir(evtAdmissao.trabalhador):
        for infoDeficiencia in evtAdmissao.trabalhador.infoDeficiencia:

            if 'defFisica' in dir(infoDeficiencia): validacoes_lista = validar_campo(validacoes_lista,'infoDeficiencia.defFisica', infoDeficiencia.defFisica.cdata, 1, u'S;N')
            if 'defVisual' in dir(infoDeficiencia): validacoes_lista = validar_campo(validacoes_lista,'infoDeficiencia.defVisual', infoDeficiencia.defVisual.cdata, 1, u'S;N')
            if 'defAuditiva' in dir(infoDeficiencia): validacoes_lista = validar_campo(validacoes_lista,'infoDeficiencia.defAuditiva', infoDeficiencia.defAuditiva.cdata, 1, u'S;N')
            if 'defMental' in dir(infoDeficiencia): validacoes_lista = validar_campo(validacoes_lista,'infoDeficiencia.defMental', infoDeficiencia.defMental.cdata, 1, u'S;N')
            if 'defIntelectual' in dir(infoDeficiencia): validacoes_lista = validar_campo(validacoes_lista,'infoDeficiencia.defIntelectual', infoDeficiencia.defIntelectual.cdata, 1, u'S;N')
            if 'reabReadap' in dir(infoDeficiencia): validacoes_lista = validar_campo(validacoes_lista,'infoDeficiencia.reabReadap', infoDeficiencia.reabReadap.cdata, 1, u'S;N')
            if 'infoCota' in dir(infoDeficiencia): validacoes_lista = validar_campo(validacoes_lista,'infoDeficiencia.infoCota', infoDeficiencia.infoCota.cdata, 1, u'S;N')
            if 'observacao' in dir(infoDeficiencia): validacoes_lista = validar_campo(validacoes_lista,'infoDeficiencia.observacao', infoDeficiencia.observacao.cdata, 0, u'')

    if 'dependente' in dir(evtAdmissao.trabalhador):
        for dependente in evtAdmissao.trabalhador.dependente:

            if 'tpDep' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.tpDep', dependente.tpDep.cdata, 1, u'01;02;03;04;06;07;09;10;11;12;99')
            if 'nmDep' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.nmDep', dependente.nmDep.cdata, 1, u'')
            if 'dtNascto' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.dtNascto', dependente.dtNascto.cdata, 1, u'')
            if 'cpfDep' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.cpfDep', dependente.cpfDep.cdata, 0, u'')
            if 'sexoDep' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.sexoDep', dependente.sexoDep.cdata, 0, u'M;F')
            if 'depIRRF' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.depIRRF', dependente.depIRRF.cdata, 1, u'S;N')
            if 'depSF' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.depSF', dependente.depSF.cdata, 1, u'S;N')
            if 'incTrab' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.incTrab', dependente.incTrab.cdata, 1, u'S;N')
            if 'depFinsPrev' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.depFinsPrev', dependente.depFinsPrev.cdata, 0, u'S;N')

    if 'aposentadoria' in dir(evtAdmissao.trabalhador):
        for aposentadoria in evtAdmissao.trabalhador.aposentadoria:

            if 'trabAposent' in dir(aposentadoria): validacoes_lista = validar_campo(validacoes_lista,'aposentadoria.trabAposent', aposentadoria.trabAposent.cdata, 1, u'S;N')

    if 'contato' in dir(evtAdmissao.trabalhador):
        for contato in evtAdmissao.trabalhador.contato:

            if 'fonePrinc' in dir(contato): validacoes_lista = validar_campo(validacoes_lista,'contato.fonePrinc', contato.fonePrinc.cdata, 0, u'')
            if 'foneAlternat' in dir(contato): validacoes_lista = validar_campo(validacoes_lista,'contato.foneAlternat', contato.foneAlternat.cdata, 0, u'')
            if 'emailPrinc' in dir(contato): validacoes_lista = validar_campo(validacoes_lista,'contato.emailPrinc', contato.emailPrinc.cdata, 0, u'')
            if 'emailAlternat' in dir(contato): validacoes_lista = validar_campo(validacoes_lista,'contato.emailAlternat', contato.emailAlternat.cdata, 0, u'')

    if 'infoCeletista' in dir(evtAdmissao.vinculo.infoRegimeTrab):
        for infoCeletista in evtAdmissao.vinculo.infoRegimeTrab.infoCeletista:

            if 'dtAdm' in dir(infoCeletista): validacoes_lista = validar_campo(validacoes_lista,'infoCeletista.dtAdm', infoCeletista.dtAdm.cdata, 1, u'')
            if 'tpAdmissao' in dir(infoCeletista): validacoes_lista = validar_campo(validacoes_lista,'infoCeletista.tpAdmissao', infoCeletista.tpAdmissao.cdata, 1, u'1;2;3;4;5')
            if 'indAdmissao' in dir(infoCeletista): validacoes_lista = validar_campo(validacoes_lista,'infoCeletista.indAdmissao', infoCeletista.indAdmissao.cdata, 1, u'1;2;3')
            if 'tpRegJor' in dir(infoCeletista): validacoes_lista = validar_campo(validacoes_lista,'infoCeletista.tpRegJor', infoCeletista.tpRegJor.cdata, 1, u'1;2;3;4')
            if 'natAtividade' in dir(infoCeletista): validacoes_lista = validar_campo(validacoes_lista,'infoCeletista.natAtividade', infoCeletista.natAtividade.cdata, 1, u'1;2')
            if 'dtBase' in dir(infoCeletista): validacoes_lista = validar_campo(validacoes_lista,'infoCeletista.dtBase', infoCeletista.dtBase.cdata, 0, u'')
            if 'cnpjSindCategProf' in dir(infoCeletista): validacoes_lista = validar_campo(validacoes_lista,'infoCeletista.cnpjSindCategProf', infoCeletista.cnpjSindCategProf.cdata, 1, u'')
            if 'opcFGTS' in dir(infoCeletista.FGTS): validacoes_lista = validar_campo(validacoes_lista,'infoCeletista.FGTS.opcFGTS', infoCeletista.FGTS.opcFGTS.cdata, 1, u'1;2')
            if 'dtOpcFGTS' in dir(infoCeletista.FGTS): validacoes_lista = validar_campo(validacoes_lista,'infoCeletista.FGTS.dtOpcFGTS', infoCeletista.FGTS.dtOpcFGTS.cdata, 0, u'')

            if 'trabTemporario' in dir(infoCeletista):
                for trabTemporario in infoCeletista.trabTemporario:

                    if 'hipLeg' in dir(trabTemporario): validacoes_lista = validar_campo(validacoes_lista,'trabTemporario.hipLeg', trabTemporario.hipLeg.cdata, 1, u'1;2')
                    if 'justContr' in dir(trabTemporario): validacoes_lista = validar_campo(validacoes_lista,'trabTemporario.justContr', trabTemporario.justContr.cdata, 1, u'')
                    if 'tpInclContr' in dir(trabTemporario): validacoes_lista = validar_campo(validacoes_lista,'trabTemporario.tpInclContr', trabTemporario.tpInclContr.cdata, 1, u'1;2;3')
                    if 'tpInsc' in dir(trabTemporario): validacoes_lista = validar_campo(validacoes_lista,'trabTemporario.tpInsc', trabTemporario.tpInsc.cdata, 1, u'1;2;3;4')
                    if 'nrInsc' in dir(trabTemporario): validacoes_lista = validar_campo(validacoes_lista,'trabTemporario.nrInsc', trabTemporario.nrInsc.cdata, 1, u'')

            if 'aprend' in dir(infoCeletista):
                for aprend in infoCeletista.aprend:

                    if 'tpInsc' in dir(aprend): validacoes_lista = validar_campo(validacoes_lista,'aprend.tpInsc', aprend.tpInsc.cdata, 1, u'1;2;3;4')
                    if 'nrInsc' in dir(aprend): validacoes_lista = validar_campo(validacoes_lista,'aprend.nrInsc', aprend.nrInsc.cdata, 1, u'')

    if 'infoEstatutario' in dir(evtAdmissao.vinculo.infoRegimeTrab):
        for infoEstatutario in evtAdmissao.vinculo.infoRegimeTrab.infoEstatutario:

            if 'indProvim' in dir(infoEstatutario): validacoes_lista = validar_campo(validacoes_lista,'infoEstatutario.indProvim', infoEstatutario.indProvim.cdata, 1, u'1;2')
            if 'tpProv' in dir(infoEstatutario): validacoes_lista = validar_campo(validacoes_lista,'infoEstatutario.tpProv', infoEstatutario.tpProv.cdata, 1, u'1;2;3;4;5;6;99')
            if 'dtNomeacao' in dir(infoEstatutario): validacoes_lista = validar_campo(validacoes_lista,'infoEstatutario.dtNomeacao', infoEstatutario.dtNomeacao.cdata, 1, u'')
            if 'dtPosse' in dir(infoEstatutario): validacoes_lista = validar_campo(validacoes_lista,'infoEstatutario.dtPosse', infoEstatutario.dtPosse.cdata, 1, u'')
            if 'dtExercicio' in dir(infoEstatutario): validacoes_lista = validar_campo(validacoes_lista,'infoEstatutario.dtExercicio', infoEstatutario.dtExercicio.cdata, 1, u'')
            if 'dtIngSvPub' in dir(infoEstatutario): validacoes_lista = validar_campo(validacoes_lista,'infoEstatutario.dtIngSvPub', infoEstatutario.dtIngSvPub.cdata, 1, u'')
            if 'tpPlanRP' in dir(infoEstatutario): validacoes_lista = validar_campo(validacoes_lista,'infoEstatutario.tpPlanRP', infoEstatutario.tpPlanRP.cdata, 0, u'1;2')
            if 'indTetoRGPS' in dir(infoEstatutario): validacoes_lista = validar_campo(validacoes_lista,'infoEstatutario.indTetoRGPS', infoEstatutario.indTetoRGPS.cdata, 0, u'S;N')
            if 'indAbonoPerm' in dir(infoEstatutario): validacoes_lista = validar_campo(validacoes_lista,'infoEstatutario.indAbonoPerm', infoEstatutario.indAbonoPerm.cdata, 0, u'S;N')
            if 'dtIniAbono' in dir(infoEstatutario): validacoes_lista = validar_campo(validacoes_lista,'infoEstatutario.dtIniAbono', infoEstatutario.dtIniAbono.cdata, 0, u'')
            if 'indParcRemun' in dir(infoEstatutario): validacoes_lista = validar_campo(validacoes_lista,'infoEstatutario.indParcRemun', infoEstatutario.indParcRemun.cdata, 0, u'S;N')
            if 'dtIniParc' in dir(infoEstatutario): validacoes_lista = validar_campo(validacoes_lista,'infoEstatutario.dtIniParc', infoEstatutario.dtIniParc.cdata, 0, u'')

            if 'infoDecJud' in dir(infoEstatutario):
                for infoDecJud in infoEstatutario.infoDecJud:

                    if 'nrProcJud' in dir(infoDecJud): validacoes_lista = validar_campo(validacoes_lista,'infoDecJud.nrProcJud', infoDecJud.nrProcJud.cdata, 1, u'')

    if 'localTrabGeral' in dir(evtAdmissao.vinculo.infoContrato.localTrabalho):
        for localTrabGeral in evtAdmissao.vinculo.infoContrato.localTrabalho.localTrabGeral:

            if 'tpInsc' in dir(localTrabGeral): validacoes_lista = validar_campo(validacoes_lista,'localTrabGeral.tpInsc', localTrabGeral.tpInsc.cdata, 1, u'1;2;3;4')
            if 'nrInsc' in dir(localTrabGeral): validacoes_lista = validar_campo(validacoes_lista,'localTrabGeral.nrInsc', localTrabGeral.nrInsc.cdata, 1, u'')
            if 'descComp' in dir(localTrabGeral): validacoes_lista = validar_campo(validacoes_lista,'localTrabGeral.descComp', localTrabGeral.descComp.cdata, 0, u'')

    if 'localTrabDom' in dir(evtAdmissao.vinculo.infoContrato.localTrabalho):
        for localTrabDom in evtAdmissao.vinculo.infoContrato.localTrabalho.localTrabDom:

            if 'tpLograd' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.tpLograd', localTrabDom.tpLograd.cdata, 1, u'A;AC;ACA;ACL;AD;AE;AER;AL;AMD;AME;AN;ANT;ART;AT;ATL;A V;AV;AVC;AVM;AVV;BAL;BC;BCO;BEL;BL;BLO;BLS;BLV;BSQ;BVD;BX;C;CAL;CAM;CAN;CH;CHA;CIC;CIR;CJ;CJM;CMP;COL;COM;CON;COR;CPO;CRG;CTN;DSC;DSV;DT;EB;EIM;ENS;ENT;EQ;ESC;ESD;ESE;ESI;ESL;ESM;ESP;ESS;EST;ESV;ETA;ETC;ETD;ETN;ETP;ETT;EVA;EVD;EX;FAV;FAZ;FER;FNT;FRA;FTE;GAL;GJA;HAB;IA;IND;IOA;JD;JDE;LD;LGA;LGO;LOT;LRG;LT;MER;MNA;MOD;MRG;MRO;MTE;NUC;NUR;OUT;PAR;PAS;PAT;PC;PCE;PDA;PDO;PNT;PR;PRL;PRM;PRQ;PRR;PSA;PSG;PSP;PSS;PTE;PTO;Q;QTA;QTS;R;R I;R L;R P;R V;RAM;RCR;REC;RER;RES;RET;RLA;RMP;ROA;ROD;ROT;RPE;RPR;RTN;RTT;SEG;SIT;SRV;ST;SUB;TCH;TER;TR;TRV;TUN;TV;TVP;TVV;UNI;V;V C;V L;VAC;VAL;VCO;VD;V-E;VER;VEV;VL;VLA;VLE;VLT;VPE;VRT;ZIG')
            if 'dscLograd' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.dscLograd', localTrabDom.dscLograd.cdata, 1, u'')
            if 'nrLograd' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.nrLograd', localTrabDom.nrLograd.cdata, 1, u'')
            if 'complemento' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.complemento', localTrabDom.complemento.cdata, 0, u'')
            if 'bairro' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.bairro', localTrabDom.bairro.cdata, 0, u'')
            if 'cep' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.cep', localTrabDom.cep.cdata, 1, u'')
            if 'codMunic' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.codMunic', localTrabDom.codMunic.cdata, 1, u'')
            if 'uf' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.uf', localTrabDom.uf.cdata, 1, u'')

    if 'horContratual' in dir(evtAdmissao.vinculo.infoContrato):
        for horContratual in evtAdmissao.vinculo.infoContrato.horContratual:

            if 'qtdHrsSem' in dir(horContratual): validacoes_lista = validar_campo(validacoes_lista,'horContratual.qtdHrsSem', horContratual.qtdHrsSem.cdata, 0, u'')
            if 'tpJornada' in dir(horContratual): validacoes_lista = validar_campo(validacoes_lista,'horContratual.tpJornada', horContratual.tpJornada.cdata, 1, u'1;2;3;9')
            if 'dscTpJorn' in dir(horContratual): validacoes_lista = validar_campo(validacoes_lista,'horContratual.dscTpJorn', horContratual.dscTpJorn.cdata, 0, u'')
            if 'tmpParc' in dir(horContratual): validacoes_lista = validar_campo(validacoes_lista,'horContratual.tmpParc', horContratual.tmpParc.cdata, 1, u'0;1;2;3')

            if 'horario' in dir(horContratual):
                for horario in horContratual.horario:

                    if 'dia' in dir(horario): validacoes_lista = validar_campo(validacoes_lista,'horario.dia', horario.dia.cdata, 1, u'1;2;3;4;5;6;7;8')
                    if 'codHorContrat' in dir(horario): validacoes_lista = validar_campo(validacoes_lista,'horario.codHorContrat', horario.codHorContrat.cdata, 1, u'')

    if 'filiacaoSindical' in dir(evtAdmissao.vinculo.infoContrato):
        for filiacaoSindical in evtAdmissao.vinculo.infoContrato.filiacaoSindical:

            if 'cnpjSindTrab' in dir(filiacaoSindical): validacoes_lista = validar_campo(validacoes_lista,'filiacaoSindical.cnpjSindTrab', filiacaoSindical.cnpjSindTrab.cdata, 1, u'')

    if 'alvaraJudicial' in dir(evtAdmissao.vinculo.infoContrato):
        for alvaraJudicial in evtAdmissao.vinculo.infoContrato.alvaraJudicial:

            if 'nrProcJud' in dir(alvaraJudicial): validacoes_lista = validar_campo(validacoes_lista,'alvaraJudicial.nrProcJud', alvaraJudicial.nrProcJud.cdata, 1, u'')

    if 'observacoes' in dir(evtAdmissao.vinculo.infoContrato):
        for observacoes in evtAdmissao.vinculo.infoContrato.observacoes:

            if 'observacao' in dir(observacoes): validacoes_lista = validar_campo(validacoes_lista,'observacoes.observacao', observacoes.observacao.cdata, 1, u'')

    if 'sucessaoVinc' in dir(evtAdmissao.vinculo):
        for sucessaoVinc in evtAdmissao.vinculo.sucessaoVinc:

            if 'tpInscAnt' in dir(sucessaoVinc): validacoes_lista = validar_campo(validacoes_lista,'sucessaoVinc.tpInscAnt', sucessaoVinc.tpInscAnt.cdata, 1, u'')
            if 'cnpjEmpregAnt' in dir(sucessaoVinc): validacoes_lista = validar_campo(validacoes_lista,'sucessaoVinc.cnpjEmpregAnt', sucessaoVinc.cnpjEmpregAnt.cdata, 1, u'')
            if 'matricAnt' in dir(sucessaoVinc): validacoes_lista = validar_campo(validacoes_lista,'sucessaoVinc.matricAnt', sucessaoVinc.matricAnt.cdata, 0, u'')
            if 'dtTransf' in dir(sucessaoVinc): validacoes_lista = validar_campo(validacoes_lista,'sucessaoVinc.dtTransf', sucessaoVinc.dtTransf.cdata, 1, u'')
            if 'observacao' in dir(sucessaoVinc): validacoes_lista = validar_campo(validacoes_lista,'sucessaoVinc.observacao', sucessaoVinc.observacao.cdata, 0, u'')

    if 'transfDom' in dir(evtAdmissao.vinculo):
        for transfDom in evtAdmissao.vinculo.transfDom:

            if 'cpfSubstituido' in dir(transfDom): validacoes_lista = validar_campo(validacoes_lista,'transfDom.cpfSubstituido', transfDom.cpfSubstituido.cdata, 1, u'')
            if 'matricAnt' in dir(transfDom): validacoes_lista = validar_campo(validacoes_lista,'transfDom.matricAnt', transfDom.matricAnt.cdata, 0, u'')
            if 'dtTransf' in dir(transfDom): validacoes_lista = validar_campo(validacoes_lista,'transfDom.dtTransf', transfDom.dtTransf.cdata, 1, u'')

    if 'mudancaCPF' in dir(evtAdmissao.vinculo):
        for mudancaCPF in evtAdmissao.vinculo.mudancaCPF:

            if 'cpfAnt' in dir(mudancaCPF): validacoes_lista = validar_campo(validacoes_lista,'mudancaCPF.cpfAnt', mudancaCPF.cpfAnt.cdata, 1, u'')
            if 'matricAnt' in dir(mudancaCPF): validacoes_lista = validar_campo(validacoes_lista,'mudancaCPF.matricAnt', mudancaCPF.matricAnt.cdata, 1, u'')
            if 'dtAltCPF' in dir(mudancaCPF): validacoes_lista = validar_campo(validacoes_lista,'mudancaCPF.dtAltCPF', mudancaCPF.dtAltCPF.cdata, 1, u'')
            if 'observacao' in dir(mudancaCPF): validacoes_lista = validar_campo(validacoes_lista,'mudancaCPF.observacao', mudancaCPF.observacao.cdata, 0, u'')

    if 'afastamento' in dir(evtAdmissao.vinculo):
        for afastamento in evtAdmissao.vinculo.afastamento:

            if 'dtIniAfast' in dir(afastamento): validacoes_lista = validar_campo(validacoes_lista,'afastamento.dtIniAfast', afastamento.dtIniAfast.cdata, 1, u'')
            if 'codMotAfast' in dir(afastamento): validacoes_lista = validar_campo(validacoes_lista,'afastamento.codMotAfast', afastamento.codMotAfast.cdata, 1, u'01;03;05;06;07;08;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;33;34')

    if 'desligamento' in dir(evtAdmissao.vinculo):
        for desligamento in evtAdmissao.vinculo.desligamento:

            if 'dtDeslig' in dir(desligamento): validacoes_lista = validar_campo(validacoes_lista,'desligamento.dtDeslig', desligamento.dtDeslig.cdata, 1, u'')

    if 'cessao' in dir(evtAdmissao.vinculo):
        for cessao in evtAdmissao.vinculo.cessao:

            if 'dtIniCessao' in dir(cessao): validacoes_lista = validar_campo(validacoes_lista,'cessao.dtIniCessao', cessao.dtIniCessao.cdata, 1, u'')

    return validacoes_lista