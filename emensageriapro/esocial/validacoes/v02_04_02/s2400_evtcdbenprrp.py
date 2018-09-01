#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s2400_evtcdbenprrp(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtCdBenPrRP = doc.eSocial.evtCdBenPrRP
    
    if 'indRetif' in dir(evtCdBenPrRP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenPrRP.ideEvento.indRetif', evtCdBenPrRP.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtCdBenPrRP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenPrRP.ideEvento.nrRecibo', evtCdBenPrRP.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtCdBenPrRP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenPrRP.ideEvento.tpAmb', evtCdBenPrRP.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtCdBenPrRP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenPrRP.ideEvento.procEmi', evtCdBenPrRP.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtCdBenPrRP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenPrRP.ideEvento.verProc', evtCdBenPrRP.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtCdBenPrRP.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenPrRP.ideEmpregador.tpInsc', evtCdBenPrRP.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtCdBenPrRP.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenPrRP.ideEmpregador.nrInsc', evtCdBenPrRP.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfBenef' in dir(evtCdBenPrRP.ideBenef): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenPrRP.ideBenef.cpfBenef', evtCdBenPrRP.ideBenef.cpfBenef.cdata, 1, '')
    if 'nmBenefic' in dir(evtCdBenPrRP.ideBenef): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenPrRP.ideBenef.nmBenefic', evtCdBenPrRP.ideBenef.nmBenefic.cdata, 1, '')
    if 'dtNascto' in dir(evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.dtNascto', evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.dtNascto.cdata, 1, '')
    if 'codMunic' in dir(evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.codMunic', evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.codMunic.cdata, 0, '')
    if 'uf' in dir(evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.uf', evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.uf.cdata, 0, '')
    if 'paisNascto' in dir(evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.paisNascto', evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.paisNascto.cdata, 1, '008;040;329;331;334;337;341;345;351;355;357;358;041;359;361;365;367;369;372;375;379;383;386;043;388;391;395;396;399;403;411;420;423;426;047;427;431;434;438;440;442;445;447;449;450;053;452;455;458;461;464;467;472;474;476;477;059;485;488;490;493;494;495;497;499;501;505;063;507;508;511;517;521;525;528;531;535;538;064;542;545;548;551;556;563;566;569;573;575;065;576;578;580;583;586;589;593;599;603;607;069;611;623;625;628;640;647;660;665;670;675;009;072;676;677;678;685;687;690;691;695;697;700;073;705;710;715;720;728;731;735;738;741;744;077;748;750;754;756;759;764;767;770;772;776;080;780;782;783;785;788;790;791;795;800;805;081;810;815;820;823;824;827;828;831;833;840;083;845;847;848;850;855;858;863;866;870;873;085;875;888;890;087;088;090;013;093;097;098;100;101;105;106;108;111;115;017;119;127;131;137;141;145;149;150;151;152;020;153;154;158;160;161;163;165;169;173;177;023;183;187;190;193;195;196;198;199;229;232;025;235;237;239;240;243;244;245;246;247;249;031;251;253;255;259;263;267;271;275;281;285;037;289;291;293;297;301;305;309;313;317;325')
    if 'paisNac' in dir(evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.paisNac', evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.paisNac.cdata, 1, '008;040;329;331;334;337;341;345;351;355;357;358;041;359;361;365;367;369;372;375;379;383;386;043;388;391;395;396;399;403;411;420;423;426;047;427;431;434;438;440;442;445;447;449;450;053;452;455;458;461;464;467;472;474;476;477;059;485;488;490;493;494;495;497;499;501;505;063;507;508;511;517;521;525;528;531;535;538;064;542;545;548;551;556;563;566;569;573;575;065;576;578;580;583;586;589;593;599;603;607;069;611;623;625;628;640;647;660;665;670;675;009;072;676;677;678;685;687;690;691;695;697;700;073;705;710;715;720;728;731;735;738;741;744;077;748;750;754;756;759;764;767;770;772;776;080;780;782;783;785;788;790;791;795;800;805;081;810;815;820;823;824;827;828;831;833;840;083;845;847;848;850;855;858;863;866;870;873;085;875;888;890;087;088;090;013;093;097;098;100;101;105;106;108;111;115;017;119;127;131;137;141;145;149;150;151;152;020;153;154;158;160;161;163;165;169;173;177;023;183;187;190;193;195;196;198;199;229;232;025;235;237;239;240;243;244;245;246;247;249;031;251;253;255;259;263;267;271;275;281;285;037;289;291;293;297;301;305;309;313;317;325')
    if 'nmMae' in dir(evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.nmMae', evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.nmMae.cdata, 0, '')
    if 'nmPai' in dir(evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.nmPai', evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.nmPai.cdata, 0, '')
    if 'tpPlanRP' in dir(evtCdBenPrRP.infoBeneficio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenPrRP.infoBeneficio.tpPlanRP', evtCdBenPrRP.infoBeneficio.tpPlanRP.cdata, 1, '1;2')
    if 'brasil' in dir(evtCdBenPrRP.ideBenef.dadosBenef.endereco):
        for brasil in evtCdBenPrRP.ideBenef.dadosBenef.endereco.brasil:
            
            if 'tpLograd' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.tpLograd', brasil.tpLograd.cdata, 1, 'A;AC;ACA;ACL;AD;AE;AER;AL;AMD;AME;AN;ANT;ART;AT;ATL;A V;AV;AVC;AVM;AVV;BAL;BC;BCO;BEL;BL;BLO;BLS;BLV;BSQ;BVD;BX;C;CAL;CAM;CAN;CH;CHA;CIC;CIR;CJ;CJM;CMP;COL;COM;CON;COR;CPO;CRG;CTN;DSC;DSV;DT;EB;EIM;ENS;ENT;EQ;ESC;ESD;ESE;ESI;ESL;ESM;ESP;ESS;EST;ESV;ETA;ETC;ETD;ETN;ETP;ETT;EVA;EVD;EX;FAV;FAZ;FER;FNT;FRA;FTE;GAL;GJA;HAB;IA;IND;IOA;JD;JDE;LD;LGA;LGO;LOT;LRG;LT;MER;MNA;MOD;MRG;MRO;MTE;NUC;NUR;OUT;PAR;PAS;PAT;PC;PCE;PDA;PDO;PNT;PR;PRL;PRM;PRQ;PRR;PSA;PSG;PSP;PSS;PTE;PTO;Q;QTA;QTS;R;R I;R L;R P;R V;RAM;RCR;REC;RER;RES;RET;RLA;RMP;ROA;ROD;ROT;RPE;RPR;RTN;RTT;SEG;SIT;SRV;ST;SUB;TCH;TER;TR;TRV;TUN;TV;TVP;TVV;UNI;V;V C;V L;VAC;VAL;VCO;VD;V-E;VER;VEV;VL;VLA;VLE;VLT;VPE;VRT;ZIG')
            if 'dscLograd' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.dscLograd', brasil.dscLograd.cdata, 1, '')
            if 'nrLograd' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.nrLograd', brasil.nrLograd.cdata, 1, '')
            if 'complemento' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.complemento', brasil.complemento.cdata, 0, '')
            if 'bairro' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.bairro', brasil.bairro.cdata, 0, '')
            if 'cep' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.cep', brasil.cep.cdata, 1, '')
            if 'codMunic' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.codMunic', brasil.codMunic.cdata, 1, '')
            if 'uf' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.uf', brasil.uf.cdata, 1, '')

    if 'exterior' in dir(evtCdBenPrRP.ideBenef.dadosBenef.endereco):
        for exterior in evtCdBenPrRP.ideBenef.dadosBenef.endereco.exterior:
            
            if 'paisResid' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.paisResid', exterior.paisResid.cdata, 1, '008;040;329;331;334;337;341;345;351;355;357;358;041;359;361;365;367;369;372;375;379;383;386;043;388;391;395;396;399;403;411;420;423;426;047;427;431;434;438;440;442;445;447;449;450;053;452;455;458;461;464;467;472;474;476;477;059;485;488;490;493;494;495;497;499;501;505;063;507;508;511;517;521;525;528;531;535;538;064;542;545;548;551;556;563;566;569;573;575;065;576;578;580;583;586;589;593;599;603;607;069;611;623;625;628;640;647;660;665;670;675;009;072;676;677;678;685;687;690;691;695;697;700;073;705;710;715;720;728;731;735;738;741;744;077;748;750;754;756;759;764;767;770;772;776;080;780;782;783;785;788;790;791;795;800;805;081;810;815;820;823;824;827;828;831;833;840;083;845;847;848;850;855;858;863;866;870;873;085;875;888;890;087;088;090;013;093;097;098;100;101;105;106;108;111;115;017;119;127;131;137;141;145;149;150;151;152;020;153;154;158;160;161;163;165;169;173;177;023;183;187;190;193;195;196;198;199;229;232;025;235;237;239;240;243;244;245;246;247;249;031;251;253;255;259;263;267;271;275;281;285;037;289;291;293;297;301;305;309;313;317;325')
            if 'dscLograd' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.dscLograd', exterior.dscLograd.cdata, 1, '')
            if 'nrLograd' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.nrLograd', exterior.nrLograd.cdata, 1, '')
            if 'complemento' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.complemento', exterior.complemento.cdata, 0, '')
            if 'bairro' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.bairro', exterior.bairro.cdata, 0, '')
            if 'nmCid' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.nmCid', exterior.nmCid.cdata, 1, '')
            if 'codPostal' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.codPostal', exterior.codPostal.cdata, 0, '')

    if 'iniBeneficio' in dir(evtCdBenPrRP.infoBeneficio):
        for iniBeneficio in evtCdBenPrRP.infoBeneficio.iniBeneficio:
            
            if 'tpBenef' in dir(iniBeneficio): validacoes_lista = validar_campo(validacoes_lista,'iniBeneficio.tpBenef', iniBeneficio.tpBenef.cdata, 1, '1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;91;92;93;94;95;96;97;98;99')
            if 'nrBenefic' in dir(iniBeneficio): validacoes_lista = validar_campo(validacoes_lista,'iniBeneficio.nrBenefic', iniBeneficio.nrBenefic.cdata, 1, '')
            if 'dtIniBenef' in dir(iniBeneficio): validacoes_lista = validar_campo(validacoes_lista,'iniBeneficio.dtIniBenef', iniBeneficio.dtIniBenef.cdata, 1, '')
            if 'vrBenef' in dir(iniBeneficio): validacoes_lista = validar_campo(validacoes_lista,'iniBeneficio.vrBenef', iniBeneficio.vrBenef.cdata, 1, '')

            if 'infoPenMorte' in dir(iniBeneficio):
                for infoPenMorte in iniBeneficio.infoPenMorte:
                    
                    if 'idQuota' in dir(infoPenMorte): validacoes_lista = validar_campo(validacoes_lista,'infoPenMorte.idQuota', infoPenMorte.idQuota.cdata, 1, '')
                    if 'cpfInst' in dir(infoPenMorte): validacoes_lista = validar_campo(validacoes_lista,'infoPenMorte.cpfInst', infoPenMorte.cpfInst.cdata, 1, '')
        
    if 'altBeneficio' in dir(evtCdBenPrRP.infoBeneficio):
        for altBeneficio in evtCdBenPrRP.infoBeneficio.altBeneficio:
            
            if 'tpBenef' in dir(altBeneficio): validacoes_lista = validar_campo(validacoes_lista,'altBeneficio.tpBenef', altBeneficio.tpBenef.cdata, 1, '1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;91;92;93;94;95;96;97;98;99')
            if 'nrBenefic' in dir(altBeneficio): validacoes_lista = validar_campo(validacoes_lista,'altBeneficio.nrBenefic', altBeneficio.nrBenefic.cdata, 1, '')
            if 'dtIniBenef' in dir(altBeneficio): validacoes_lista = validar_campo(validacoes_lista,'altBeneficio.dtIniBenef', altBeneficio.dtIniBenef.cdata, 1, '')
            if 'vrBenef' in dir(altBeneficio): validacoes_lista = validar_campo(validacoes_lista,'altBeneficio.vrBenef', altBeneficio.vrBenef.cdata, 1, '')

            if 'infoPenMorte' in dir(altBeneficio):
                for infoPenMorte in altBeneficio.infoPenMorte:
                    
                    if 'idQuota' in dir(infoPenMorte): validacoes_lista = validar_campo(validacoes_lista,'infoPenMorte.idQuota', infoPenMorte.idQuota.cdata, 1, '')
                    if 'cpfInst' in dir(infoPenMorte): validacoes_lista = validar_campo(validacoes_lista,'infoPenMorte.cpfInst', infoPenMorte.cpfInst.cdata, 1, '')
        
    if 'fimBeneficio' in dir(evtCdBenPrRP.infoBeneficio):
        for fimBeneficio in evtCdBenPrRP.infoBeneficio.fimBeneficio:
            
            if 'tpBenef' in dir(fimBeneficio): validacoes_lista = validar_campo(validacoes_lista,'fimBeneficio.tpBenef', fimBeneficio.tpBenef.cdata, 1, '1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;91;92;93;94;95;96;97;98;99')
            if 'nrBenefic' in dir(fimBeneficio): validacoes_lista = validar_campo(validacoes_lista,'fimBeneficio.nrBenefic', fimBeneficio.nrBenefic.cdata, 1, '')
            if 'dtFimBenef' in dir(fimBeneficio): validacoes_lista = validar_campo(validacoes_lista,'fimBeneficio.dtFimBenef', fimBeneficio.dtFimBenef.cdata, 1, '')
            if 'mtvFim' in dir(fimBeneficio): validacoes_lista = validar_campo(validacoes_lista,'fimBeneficio.mtvFim', fimBeneficio.mtvFim.cdata, 1, '1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;91;92;93;94;95;96;97;98;99')

    return validacoes_lista