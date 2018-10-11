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


def validacoes_s2205_evtaltcadastral(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtAltCadastral = doc.eSocial.evtAltCadastral
    
    if 'indRetif' in dir(evtAltCadastral.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.ideEvento.indRetif', evtAltCadastral.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtAltCadastral.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.ideEvento.nrRecibo', evtAltCadastral.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtAltCadastral.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.ideEvento.tpAmb', evtAltCadastral.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtAltCadastral.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.ideEvento.procEmi', evtAltCadastral.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtAltCadastral.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.ideEvento.verProc', evtAltCadastral.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtAltCadastral.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.ideEmpregador.tpInsc', evtAltCadastral.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtAltCadastral.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.ideEmpregador.nrInsc', evtAltCadastral.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtAltCadastral.ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.ideTrabalhador.cpfTrab', evtAltCadastral.ideTrabalhador.cpfTrab.cdata, 1, '')
    if 'dtAlteracao' in dir(evtAltCadastral.alteracao): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.alteracao.dtAlteracao', evtAltCadastral.alteracao.dtAlteracao.cdata, 1, '')
    if 'nisTrab' in dir(evtAltCadastral.alteracao.dadosTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.alteracao.dadosTrabalhador.nisTrab', evtAltCadastral.alteracao.dadosTrabalhador.nisTrab.cdata, 0, '')
    if 'nmTrab' in dir(evtAltCadastral.alteracao.dadosTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.alteracao.dadosTrabalhador.nmTrab', evtAltCadastral.alteracao.dadosTrabalhador.nmTrab.cdata, 1, '')
    if 'sexo' in dir(evtAltCadastral.alteracao.dadosTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.alteracao.dadosTrabalhador.sexo', evtAltCadastral.alteracao.dadosTrabalhador.sexo.cdata, 1, 'M;F')
    if 'racaCor' in dir(evtAltCadastral.alteracao.dadosTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.alteracao.dadosTrabalhador.racaCor', evtAltCadastral.alteracao.dadosTrabalhador.racaCor.cdata, 1, '1;2;3;4;5;6')
    if 'estCiv' in dir(evtAltCadastral.alteracao.dadosTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.alteracao.dadosTrabalhador.estCiv', evtAltCadastral.alteracao.dadosTrabalhador.estCiv.cdata, 0, '1;2;3;4;5')
    if 'grauInstr' in dir(evtAltCadastral.alteracao.dadosTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.alteracao.dadosTrabalhador.grauInstr', evtAltCadastral.alteracao.dadosTrabalhador.grauInstr.cdata, 1, '01;02;03;04;05;06;07;08;09;10;11;12')
    if 'nmSoc' in dir(evtAltCadastral.alteracao.dadosTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.alteracao.dadosTrabalhador.nmSoc', evtAltCadastral.alteracao.dadosTrabalhador.nmSoc.cdata, 0, '')
    if 'dtNascto' in dir(evtAltCadastral.alteracao.dadosTrabalhador.nascimento): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.alteracao.dadosTrabalhador.nascimento.dtNascto', evtAltCadastral.alteracao.dadosTrabalhador.nascimento.dtNascto.cdata, 1, '')
    if 'codMunic' in dir(evtAltCadastral.alteracao.dadosTrabalhador.nascimento): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.alteracao.dadosTrabalhador.nascimento.codMunic', evtAltCadastral.alteracao.dadosTrabalhador.nascimento.codMunic.cdata, 0, '')
    if 'uf' in dir(evtAltCadastral.alteracao.dadosTrabalhador.nascimento): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.alteracao.dadosTrabalhador.nascimento.uf', evtAltCadastral.alteracao.dadosTrabalhador.nascimento.uf.cdata, 0, '')
    if 'paisNascto' in dir(evtAltCadastral.alteracao.dadosTrabalhador.nascimento): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.alteracao.dadosTrabalhador.nascimento.paisNascto', evtAltCadastral.alteracao.dadosTrabalhador.nascimento.paisNascto.cdata, 1, '008;040;329;331;334;337;341;345;351;355;357;358;041;359;361;365;367;369;372;375;379;383;386;043;388;391;395;396;399;403;411;420;423;426;047;427;431;434;438;440;442;445;447;449;450;053;452;455;458;461;464;467;472;474;476;477;059;485;488;490;493;494;495;497;499;501;505;063;507;508;511;517;521;525;528;531;535;538;064;542;545;548;551;556;563;566;569;573;575;065;576;578;580;583;586;589;593;599;603;607;069;611;623;625;628;640;647;660;665;670;675;009;072;676;677;678;685;687;690;691;695;697;700;073;705;710;715;720;728;731;735;738;741;744;077;748;750;754;756;759;764;767;770;772;776;080;780;782;783;785;788;790;791;795;800;805;081;810;815;820;823;824;827;828;831;833;840;083;845;847;848;850;855;858;863;866;870;873;085;875;888;890;087;088;090;013;093;097;098;100;101;105;106;108;111;115;017;119;127;131;137;141;145;149;150;151;152;020;153;154;158;160;161;163;165;169;173;177;023;183;187;190;193;195;196;198;199;229;232;025;235;237;239;240;243;244;245;246;247;249;031;251;253;255;259;263;267;271;275;281;285;037;289;291;293;297;301;305;309;313;317;325')
    if 'paisNac' in dir(evtAltCadastral.alteracao.dadosTrabalhador.nascimento): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.alteracao.dadosTrabalhador.nascimento.paisNac', evtAltCadastral.alteracao.dadosTrabalhador.nascimento.paisNac.cdata, 1, '008;040;329;331;334;337;341;345;351;355;357;358;041;359;361;365;367;369;372;375;379;383;386;043;388;391;395;396;399;403;411;420;423;426;047;427;431;434;438;440;442;445;447;449;450;053;452;455;458;461;464;467;472;474;476;477;059;485;488;490;493;494;495;497;499;501;505;063;507;508;511;517;521;525;528;531;535;538;064;542;545;548;551;556;563;566;569;573;575;065;576;578;580;583;586;589;593;599;603;607;069;611;623;625;628;640;647;660;665;670;675;009;072;676;677;678;685;687;690;691;695;697;700;073;705;710;715;720;728;731;735;738;741;744;077;748;750;754;756;759;764;767;770;772;776;080;780;782;783;785;788;790;791;795;800;805;081;810;815;820;823;824;827;828;831;833;840;083;845;847;848;850;855;858;863;866;870;873;085;875;888;890;087;088;090;013;093;097;098;100;101;105;106;108;111;115;017;119;127;131;137;141;145;149;150;151;152;020;153;154;158;160;161;163;165;169;173;177;023;183;187;190;193;195;196;198;199;229;232;025;235;237;239;240;243;244;245;246;247;249;031;251;253;255;259;263;267;271;275;281;285;037;289;291;293;297;301;305;309;313;317;325')
    if 'nmMae' in dir(evtAltCadastral.alteracao.dadosTrabalhador.nascimento): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.alteracao.dadosTrabalhador.nascimento.nmMae', evtAltCadastral.alteracao.dadosTrabalhador.nascimento.nmMae.cdata, 0, '')
    if 'nmPai' in dir(evtAltCadastral.alteracao.dadosTrabalhador.nascimento): validacoes_lista = validar_campo(validacoes_lista,'evtAltCadastral.alteracao.dadosTrabalhador.nascimento.nmPai', evtAltCadastral.alteracao.dadosTrabalhador.nascimento.nmPai.cdata, 0, '')
    if 'documentos' in dir(evtAltCadastral.alteracao.dadosTrabalhador):
        for documentos in evtAltCadastral.alteracao.dadosTrabalhador.documentos:
            

            if 'CTPS' in dir(documentos):
                for CTPS in documentos.CTPS:
                    
                    if 'nrCtps' in dir(CTPS): validacoes_lista = validar_campo(validacoes_lista,'CTPS.nrCtps', CTPS.nrCtps.cdata, 1, '')
                    if 'serieCtps' in dir(CTPS): validacoes_lista = validar_campo(validacoes_lista,'CTPS.serieCtps', CTPS.serieCtps.cdata, 1, '')
                    if 'ufCtps' in dir(CTPS): validacoes_lista = validar_campo(validacoes_lista,'CTPS.ufCtps', CTPS.ufCtps.cdata, 1, '')
        
            if 'RIC' in dir(documentos):
                for RIC in documentos.RIC:
                    
                    if 'nrRic' in dir(RIC): validacoes_lista = validar_campo(validacoes_lista,'RIC.nrRic', RIC.nrRic.cdata, 1, '')
                    if 'orgaoEmissor' in dir(RIC): validacoes_lista = validar_campo(validacoes_lista,'RIC.orgaoEmissor', RIC.orgaoEmissor.cdata, 1, '')
                    if 'dtExped' in dir(RIC): validacoes_lista = validar_campo(validacoes_lista,'RIC.dtExped', RIC.dtExped.cdata, 0, '')
        
            if 'RG' in dir(documentos):
                for RG in documentos.RG:
                    
                    if 'nrRg' in dir(RG): validacoes_lista = validar_campo(validacoes_lista,'RG.nrRg', RG.nrRg.cdata, 1, '')
                    if 'orgaoEmissor' in dir(RG): validacoes_lista = validar_campo(validacoes_lista,'RG.orgaoEmissor', RG.orgaoEmissor.cdata, 1, '')
                    if 'dtExped' in dir(RG): validacoes_lista = validar_campo(validacoes_lista,'RG.dtExped', RG.dtExped.cdata, 0, '')
        
            if 'RNE' in dir(documentos):
                for RNE in documentos.RNE:
                    
                    if 'nrRne' in dir(RNE): validacoes_lista = validar_campo(validacoes_lista,'RNE.nrRne', RNE.nrRne.cdata, 1, '')
                    if 'orgaoEmissor' in dir(RNE): validacoes_lista = validar_campo(validacoes_lista,'RNE.orgaoEmissor', RNE.orgaoEmissor.cdata, 1, '')
                    if 'dtExped' in dir(RNE): validacoes_lista = validar_campo(validacoes_lista,'RNE.dtExped', RNE.dtExped.cdata, 0, '')
        
            if 'OC' in dir(documentos):
                for OC in documentos.OC:
                    
                    if 'nrOc' in dir(OC): validacoes_lista = validar_campo(validacoes_lista,'OC.nrOc', OC.nrOc.cdata, 1, '')
                    if 'orgaoEmissor' in dir(OC): validacoes_lista = validar_campo(validacoes_lista,'OC.orgaoEmissor', OC.orgaoEmissor.cdata, 1, '')
                    if 'dtExped' in dir(OC): validacoes_lista = validar_campo(validacoes_lista,'OC.dtExped', OC.dtExped.cdata, 0, '')
                    if 'dtValid' in dir(OC): validacoes_lista = validar_campo(validacoes_lista,'OC.dtValid', OC.dtValid.cdata, 0, '')
        
            if 'CNH' in dir(documentos):
                for CNH in documentos.CNH:
                    
                    if 'nrRegCnh' in dir(CNH): validacoes_lista = validar_campo(validacoes_lista,'CNH.nrRegCnh', CNH.nrRegCnh.cdata, 1, '')
                    if 'dtExped' in dir(CNH): validacoes_lista = validar_campo(validacoes_lista,'CNH.dtExped', CNH.dtExped.cdata, 0, '')
                    if 'ufCnh' in dir(CNH): validacoes_lista = validar_campo(validacoes_lista,'CNH.ufCnh', CNH.ufCnh.cdata, 1, '')
                    if 'dtValid' in dir(CNH): validacoes_lista = validar_campo(validacoes_lista,'CNH.dtValid', CNH.dtValid.cdata, 1, '')
                    if 'dtPriHab' in dir(CNH): validacoes_lista = validar_campo(validacoes_lista,'CNH.dtPriHab', CNH.dtPriHab.cdata, 0, '')
                    if 'categoriaCnh' in dir(CNH): validacoes_lista = validar_campo(validacoes_lista,'CNH.categoriaCnh', CNH.categoriaCnh.cdata, 1, 'A;B;C;D;E;AB;AC;AD;AE')
        
    if 'brasil' in dir(evtAltCadastral.alteracao.dadosTrabalhador.endereco):
        for brasil in evtAltCadastral.alteracao.dadosTrabalhador.endereco.brasil:
            
            if 'tpLograd' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.tpLograd', brasil.tpLograd.cdata, 1, 'A;AC;ACA;ACL;AD;AE;AER;AL;AMD;AME;AN;ANT;ART;AT;ATL;A V;AV;AVC;AVM;AVV;BAL;BC;BCO;BEL;BL;BLO;BLS;BLV;BSQ;BVD;BX;C;CAL;CAM;CAN;CH;CHA;CIC;CIR;CJ;CJM;CMP;COL;COM;CON;COR;CPO;CRG;CTN;DSC;DSV;DT;EB;EIM;ENS;ENT;EQ;ESC;ESD;ESE;ESI;ESL;ESM;ESP;ESS;EST;ESV;ETA;ETC;ETD;ETN;ETP;ETT;EVA;EVD;EX;FAV;FAZ;FER;FNT;FRA;FTE;GAL;GJA;HAB;IA;IND;IOA;JD;JDE;LD;LGA;LGO;LOT;LRG;LT;MER;MNA;MOD;MRG;MRO;MTE;NUC;NUR;OUT;PAR;PAS;PAT;PC;PCE;PDA;PDO;PNT;PR;PRL;PRM;PRQ;PRR;PSA;PSG;PSP;PSS;PTE;PTO;Q;QTA;QTS;R;R I;R L;R P;R V;RAM;RCR;REC;RER;RES;RET;RLA;RMP;ROA;ROD;ROT;RPE;RPR;RTN;RTT;SEG;SIT;SRV;ST;SUB;TCH;TER;TR;TRV;TUN;TV;TVP;TVV;UNI;V;V C;V L;VAC;VAL;VCO;VD;V-E;VER;VEV;VL;VLA;VLE;VLT;VPE;VRT;ZIG')
            if 'dscLograd' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.dscLograd', brasil.dscLograd.cdata, 1, '')
            if 'nrLograd' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.nrLograd', brasil.nrLograd.cdata, 1, '')
            if 'complemento' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.complemento', brasil.complemento.cdata, 0, '')
            if 'bairro' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.bairro', brasil.bairro.cdata, 0, '')
            if 'cep' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.cep', brasil.cep.cdata, 1, '')
            if 'codMunic' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.codMunic', brasil.codMunic.cdata, 1, '')
            if 'uf' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.uf', brasil.uf.cdata, 1, '')

    if 'exterior' in dir(evtAltCadastral.alteracao.dadosTrabalhador.endereco):
        for exterior in evtAltCadastral.alteracao.dadosTrabalhador.endereco.exterior:
            
            if 'paisResid' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.paisResid', exterior.paisResid.cdata, 1, '008;040;329;331;334;337;341;345;351;355;357;358;041;359;361;365;367;369;372;375;379;383;386;043;388;391;395;396;399;403;411;420;423;426;047;427;431;434;438;440;442;445;447;449;450;053;452;455;458;461;464;467;472;474;476;477;059;485;488;490;493;494;495;497;499;501;505;063;507;508;511;517;521;525;528;531;535;538;064;542;545;548;551;556;563;566;569;573;575;065;576;578;580;583;586;589;593;599;603;607;069;611;623;625;628;640;647;660;665;670;675;009;072;676;677;678;685;687;690;691;695;697;700;073;705;710;715;720;728;731;735;738;741;744;077;748;750;754;756;759;764;767;770;772;776;080;780;782;783;785;788;790;791;795;800;805;081;810;815;820;823;824;827;828;831;833;840;083;845;847;848;850;855;858;863;866;870;873;085;875;888;890;087;088;090;013;093;097;098;100;101;105;106;108;111;115;017;119;127;131;137;141;145;149;150;151;152;020;153;154;158;160;161;163;165;169;173;177;023;183;187;190;193;195;196;198;199;229;232;025;235;237;239;240;243;244;245;246;247;249;031;251;253;255;259;263;267;271;275;281;285;037;289;291;293;297;301;305;309;313;317;325')
            if 'dscLograd' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.dscLograd', exterior.dscLograd.cdata, 1, '')
            if 'nrLograd' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.nrLograd', exterior.nrLograd.cdata, 1, '')
            if 'complemento' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.complemento', exterior.complemento.cdata, 0, '')
            if 'bairro' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.bairro', exterior.bairro.cdata, 0, '')
            if 'nmCid' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.nmCid', exterior.nmCid.cdata, 1, '')
            if 'codPostal' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.codPostal', exterior.codPostal.cdata, 0, '')

    if 'trabEstrangeiro' in dir(evtAltCadastral.alteracao.dadosTrabalhador):
        for trabEstrangeiro in evtAltCadastral.alteracao.dadosTrabalhador.trabEstrangeiro:
            
            if 'dtChegada' in dir(trabEstrangeiro): validacoes_lista = validar_campo(validacoes_lista,'trabEstrangeiro.dtChegada', trabEstrangeiro.dtChegada.cdata, 0, '')
            if 'classTrabEstrang' in dir(trabEstrangeiro): validacoes_lista = validar_campo(validacoes_lista,'trabEstrangeiro.classTrabEstrang', trabEstrangeiro.classTrabEstrang.cdata, 1, '1;2;3;4;5;6;7;8;9;10;11;12')
            if 'casadoBr' in dir(trabEstrangeiro): validacoes_lista = validar_campo(validacoes_lista,'trabEstrangeiro.casadoBr', trabEstrangeiro.casadoBr.cdata, 1, 'S;N')
            if 'filhosBr' in dir(trabEstrangeiro): validacoes_lista = validar_campo(validacoes_lista,'trabEstrangeiro.filhosBr', trabEstrangeiro.filhosBr.cdata, 1, 'S;N')

    if 'infoDeficiencia' in dir(evtAltCadastral.alteracao.dadosTrabalhador):
        for infoDeficiencia in evtAltCadastral.alteracao.dadosTrabalhador.infoDeficiencia:
            
            if 'defFisica' in dir(infoDeficiencia): validacoes_lista = validar_campo(validacoes_lista,'infoDeficiencia.defFisica', infoDeficiencia.defFisica.cdata, 1, 'S;N')
            if 'defVisual' in dir(infoDeficiencia): validacoes_lista = validar_campo(validacoes_lista,'infoDeficiencia.defVisual', infoDeficiencia.defVisual.cdata, 1, 'S;N')
            if 'defAuditiva' in dir(infoDeficiencia): validacoes_lista = validar_campo(validacoes_lista,'infoDeficiencia.defAuditiva', infoDeficiencia.defAuditiva.cdata, 1, 'S;N')
            if 'defMental' in dir(infoDeficiencia): validacoes_lista = validar_campo(validacoes_lista,'infoDeficiencia.defMental', infoDeficiencia.defMental.cdata, 1, 'S;N')
            if 'defIntelectual' in dir(infoDeficiencia): validacoes_lista = validar_campo(validacoes_lista,'infoDeficiencia.defIntelectual', infoDeficiencia.defIntelectual.cdata, 1, 'S;N')
            if 'reabReadap' in dir(infoDeficiencia): validacoes_lista = validar_campo(validacoes_lista,'infoDeficiencia.reabReadap', infoDeficiencia.reabReadap.cdata, 1, 'S;N')
            if 'infoCota' in dir(infoDeficiencia): validacoes_lista = validar_campo(validacoes_lista,'infoDeficiencia.infoCota', infoDeficiencia.infoCota.cdata, 0, 'S;N')
            if 'observacao' in dir(infoDeficiencia): validacoes_lista = validar_campo(validacoes_lista,'infoDeficiencia.observacao', infoDeficiencia.observacao.cdata, 0, '')

    if 'dependente' in dir(evtAltCadastral.alteracao.dadosTrabalhador):
        for dependente in evtAltCadastral.alteracao.dadosTrabalhador.dependente:
            
            if 'tpDep' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.tpDep', dependente.tpDep.cdata, 1, '01;02;03;04;06;07;09;10;11;12;99')
            if 'nmDep' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.nmDep', dependente.nmDep.cdata, 1, '')
            if 'dtNascto' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.dtNascto', dependente.dtNascto.cdata, 1, '')
            if 'cpfDep' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.cpfDep', dependente.cpfDep.cdata, 0, '')
            if 'sexoDep' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.sexoDep', dependente.sexoDep.cdata, 0, 'M;F')
            if 'depIRRF' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.depIRRF', dependente.depIRRF.cdata, 1, 'S;N')
            if 'depSF' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.depSF', dependente.depSF.cdata, 1, 'S;N')
            if 'incTrab' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.incTrab', dependente.incTrab.cdata, 1, 'S;N')
            if 'depFinsPrev' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.depFinsPrev', dependente.depFinsPrev.cdata, 0, 'S;N')

    if 'aposentadoria' in dir(evtAltCadastral.alteracao.dadosTrabalhador):
        for aposentadoria in evtAltCadastral.alteracao.dadosTrabalhador.aposentadoria:
            
            if 'trabAposent' in dir(aposentadoria): validacoes_lista = validar_campo(validacoes_lista,'aposentadoria.trabAposent', aposentadoria.trabAposent.cdata, 1, 'S;N')

    if 'contato' in dir(evtAltCadastral.alteracao.dadosTrabalhador):
        for contato in evtAltCadastral.alteracao.dadosTrabalhador.contato:
            
            if 'fonePrinc' in dir(contato): validacoes_lista = validar_campo(validacoes_lista,'contato.fonePrinc', contato.fonePrinc.cdata, 0, '')
            if 'foneAlternat' in dir(contato): validacoes_lista = validar_campo(validacoes_lista,'contato.foneAlternat', contato.foneAlternat.cdata, 0, '')
            if 'emailPrinc' in dir(contato): validacoes_lista = validar_campo(validacoes_lista,'contato.emailPrinc', contato.emailPrinc.cdata, 0, '')
            if 'emailAlternat' in dir(contato): validacoes_lista = validar_campo(validacoes_lista,'contato.emailAlternat', contato.emailAlternat.cdata, 0, '')

    return validacoes_lista