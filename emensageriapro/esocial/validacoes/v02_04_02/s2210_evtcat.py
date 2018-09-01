#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s2210_evtcat(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtCAT = doc.eSocial.evtCAT
    
    if 'indRetif' in dir(evtCAT.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.ideEvento.indRetif', evtCAT.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtCAT.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.ideEvento.nrRecibo', evtCAT.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtCAT.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.ideEvento.tpAmb', evtCAT.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtCAT.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.ideEvento.procEmi', evtCAT.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtCAT.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.ideEvento.verProc', evtCAT.ideEvento.verProc.cdata, 1, '')
    if 'tpRegistrador' in dir(evtCAT.ideRegistrador): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.ideRegistrador.tpRegistrador', evtCAT.ideRegistrador.tpRegistrador.cdata, 1, '1;2;3;4;5;6;7;8;9')
    if 'tpInsc' in dir(evtCAT.ideRegistrador): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.ideRegistrador.tpInsc', evtCAT.ideRegistrador.tpInsc.cdata, 0, '1;2;3;4')
    if 'nrInsc' in dir(evtCAT.ideRegistrador): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.ideRegistrador.nrInsc', evtCAT.ideRegistrador.nrInsc.cdata, 0, '')
    if 'tpInsc' in dir(evtCAT.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.ideEmpregador.tpInsc', evtCAT.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtCAT.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.ideEmpregador.nrInsc', evtCAT.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtCAT.ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.ideTrabalhador.cpfTrab', evtCAT.ideTrabalhador.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtCAT.ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.ideTrabalhador.nisTrab', evtCAT.ideTrabalhador.nisTrab.cdata, 0, '')
    if 'dtAcid' in dir(evtCAT.cat): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.dtAcid', evtCAT.cat.dtAcid.cdata, 1, '')
    if 'tpAcid' in dir(evtCAT.cat): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.tpAcid', evtCAT.cat.tpAcid.cdata, 1, '1.0.01;1.0.02;2.0.01;2.0.02;2.0.03;2.0.04;2.0.05;2.0.06;3.0.01;3.0.02;3.0.03;3.0.04;3.0.05;3.0.06;3.0.07;3.0.08;3.0.09;3.0.10;3.0.11;4.0.01;4.0.02;5.0.01')
    if 'hrAcid' in dir(evtCAT.cat): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.hrAcid', evtCAT.cat.hrAcid.cdata, 1, '')
    if 'hrsTrabAntesAcid' in dir(evtCAT.cat): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.hrsTrabAntesAcid', evtCAT.cat.hrsTrabAntesAcid.cdata, 1, '')
    if 'tpCat' in dir(evtCAT.cat): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.tpCat', evtCAT.cat.tpCat.cdata, 1, '1;2;3')
    if 'indCatObito' in dir(evtCAT.cat): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.indCatObito', evtCAT.cat.indCatObito.cdata, 1, 'S;N')
    if 'dtObito' in dir(evtCAT.cat): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.dtObito', evtCAT.cat.dtObito.cdata, 0, '')
    if 'indComunPolicia' in dir(evtCAT.cat): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.indComunPolicia', evtCAT.cat.indComunPolicia.cdata, 1, 'S;N')
    if 'codSitGeradora' in dir(evtCAT.cat): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.codSitGeradora', evtCAT.cat.codSitGeradora.cdata, 0, '200004300;200004600;200008300;200008600;200008900;200012200;200012300;200012400;200012500;200012600;200012700;200012900;200016300;200016600;200016900;200020100;200020300;200020500;200020700;200020900;200024300;200024400;200024500;200024600;200024700;200024900;200028300;200028600;200032200;200032400;200032600;200032900;200036000;200040300;200040600;200044300;200044600;200048200;200048400;200048600;200048900;200052000;200056000;200060000;200064000;200068000;200072000;200072300;200072600;200076200;200076400;200076600;200076900;200080200;200080400;200080600;200080900;209000000;209500000')
    if 'iniciatCAT' in dir(evtCAT.cat): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.iniciatCAT', evtCAT.cat.iniciatCAT.cdata, 1, '1;2;3')
    if 'observacao' in dir(evtCAT.cat): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.observacao', evtCAT.cat.observacao.cdata, 0, '')
    if 'tpLocal' in dir(evtCAT.cat.localAcidente): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.localAcidente.tpLocal', evtCAT.cat.localAcidente.tpLocal.cdata, 1, '1;2;3;4;5;6;9')
    if 'dscLocal' in dir(evtCAT.cat.localAcidente): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.localAcidente.dscLocal', evtCAT.cat.localAcidente.dscLocal.cdata, 0, '')
    if 'dscLograd' in dir(evtCAT.cat.localAcidente): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.localAcidente.dscLograd', evtCAT.cat.localAcidente.dscLograd.cdata, 0, '')
    if 'nrLograd' in dir(evtCAT.cat.localAcidente): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.localAcidente.nrLograd', evtCAT.cat.localAcidente.nrLograd.cdata, 0, '')
    if 'codMunic' in dir(evtCAT.cat.localAcidente): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.localAcidente.codMunic', evtCAT.cat.localAcidente.codMunic.cdata, 0, '')
    if 'uf' in dir(evtCAT.cat.localAcidente): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.localAcidente.uf', evtCAT.cat.localAcidente.uf.cdata, 0, '')
    if 'cnpjLocalAcid' in dir(evtCAT.cat.localAcidente): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.localAcidente.cnpjLocalAcid', evtCAT.cat.localAcidente.cnpjLocalAcid.cdata, 0, '')
    if 'pais' in dir(evtCAT.cat.localAcidente): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.localAcidente.pais', evtCAT.cat.localAcidente.pais.cdata, 0, '008;040;329;331;334;337;341;345;351;355;357;358;041;359;361;365;367;369;372;375;379;383;386;043;388;391;395;396;399;403;411;420;423;426;047;427;431;434;438;440;442;445;447;449;450;053;452;455;458;461;464;467;472;474;476;477;059;485;488;490;493;494;495;497;499;501;505;063;507;508;511;517;521;525;528;531;535;538;064;542;545;548;551;556;563;566;569;573;575;065;576;578;580;583;586;589;593;599;603;607;069;611;623;625;628;640;647;660;665;670;675;009;072;676;677;678;685;687;690;691;695;697;700;073;705;710;715;720;728;731;735;738;741;744;077;748;750;754;756;759;764;767;770;772;776;080;780;782;783;785;788;790;791;795;800;805;081;810;815;820;823;824;827;828;831;833;840;083;845;847;848;850;855;858;863;866;870;873;085;875;888;890;087;088;090;013;093;097;098;100;101;105;106;108;111;115;017;119;127;131;137;141;145;149;150;151;152;020;153;154;158;160;161;163;165;169;173;177;023;183;187;190;193;195;196;198;199;229;232;025;235;237;239;240;243;244;245;246;247;249;031;251;253;255;259;263;267;271;275;281;285;037;289;291;293;297;301;305;309;313;317;325')
    if 'codPostal' in dir(evtCAT.cat.localAcidente): validacoes_lista = validar_campo(validacoes_lista,'evtCAT.cat.localAcidente.codPostal', evtCAT.cat.localAcidente.codPostal.cdata, 0, '')
    if 'parteAtingida' in dir(evtCAT.cat):
        for parteAtingida in evtCAT.cat.parteAtingida:
            
            if 'codParteAting' in dir(parteAtingida): validacoes_lista = validar_campo(validacoes_lista,'parteAtingida.codParteAting', parteAtingida.codParteAting.cdata, 1, '753030000;753050000;753070100;753070300;753070500;753070700;753070800;753080000;753090000;753510000;753510200;754000000;755010400;755010600;755030000;755050000;755070000;755080000;755090000;756020000;756030000;756040000;756050000;756060000;756070000;756090000;757010000;757010200;757010400;757010600;757030000;757050000;757070000;757080000;757090000;758000000;758500000;758520000;758530000;758540000;758550000;758560000;758570000;758590000;759000000')
            if 'lateralidade' in dir(parteAtingida): validacoes_lista = validar_campo(validacoes_lista,'parteAtingida.lateralidade', parteAtingida.lateralidade.cdata, 1, '0;1;2;3')

    if 'agenteCausador' in dir(evtCAT.cat):
        for agenteCausador in evtCAT.cat.agenteCausador:
            
            if 'codAgntCausador' in dir(agenteCausador): validacoes_lista = validar_campo(validacoes_lista,'agenteCausador.codAgntCausador', agenteCausador.codAgntCausador.cdata, 1, '302010200;302010250;302010300;302010350;302010400;302010450;302010500;302010550;302010600;302010650;302010700;302010900;302030900;302050100;302050200;302050300;302050400;302050500;302050600;302050700;302050800;302050900;302070100;302070300;302070500;302070700;302070900;302090000;303010040;303010080;303010120;303010160;303010200;303010240;303010280;303010320;303010360;303010400;303010440;303010480;303010520;303010560;303010600;303010640;303010680;303010720;303010760;303010800;303010900;303015050;303015100;303015150;303015200;303015250;303015300;303015350;303015400;303015450;303015500;303015550;303015600;303015650;303015700;303015750;303015900;303020040;303020080;303020120;303020160;303020200;303020240;303020280;303020320;303020360;303020400;303020440;303020480;303020520;303020560;303020600;303020640;303020680;303020720;303020760;303020900;303025300;303025600;303025900;303030050;303030100;303030150;303030200;303030250;303030300;303030350;303030400;303030450;303030500;303030900;303035300;303035400;303035500;303035600;303035700;303035900;303040100;303040200;303040300;303040400;303040500;303040600;303040700;303040750;303040800;303040900;303045200;303045400;303045600;303045900;303050200;303050400;303050600;303050900;303055200;303055400;303055600;303055900;303060000;303065000;303065300;303065600;303065900;303066300;303066600;303070200;303070400;303070600;303070900;303075100;303075150;303075200;303075250;303075300;303075350;303075400;303075450;303075500;303075550;303075600;303075650;303075700;303075750;303075800;303075900;303090000;305004100;305004150;305004200;305004250;305004300;305004350;305004400;305004450;305004500;305004550;305004600;305004650;305004700;305004750;305004900;305008500;305008900;305020000;305024100;305024300;305024500;305024700;305024900;305028000 - Madeira (toro, madeira serrada, pranchão, poste, barrote, ripa e produto de madeira);305032000;305032500;305036000;305040100;305040150;305040200;305040250;305040300;305040350;305040400;305040450;305040500;305040600;305040650;305040700;305040900;305044000;305048000;305048300;305048400;305048500;305048600;305048700;305048900;305052000;305056000;305060000;305064000;305064300;305064400;305064500;305064600;305064700;305064900;305068300;305068600;305072000;305076000;305090000;306020000;306040000;306060000;306090000;307030100;307030200;307030250;307030300;307030400;307030500;307030600;307030900;307040100;307040300;307040500;307040700;307040900;307050900;307070000;309000000;309500000;354000000;354010300;354010600;354020000;354040000;354050300;355016000;355016600;355016800')

    if 'atestado' in dir(evtCAT.cat):
        for atestado in evtCAT.cat.atestado:
            
            if 'codCNES' in dir(atestado): validacoes_lista = validar_campo(validacoes_lista,'atestado.codCNES', atestado.codCNES.cdata, 0, '')
            if 'dtAtendimento' in dir(atestado): validacoes_lista = validar_campo(validacoes_lista,'atestado.dtAtendimento', atestado.dtAtendimento.cdata, 1, '')
            if 'hrAtendimento' in dir(atestado): validacoes_lista = validar_campo(validacoes_lista,'atestado.hrAtendimento', atestado.hrAtendimento.cdata, 1, '')
            if 'indInternacao' in dir(atestado): validacoes_lista = validar_campo(validacoes_lista,'atestado.indInternacao', atestado.indInternacao.cdata, 1, 'S;N')
            if 'durTrat' in dir(atestado): validacoes_lista = validar_campo(validacoes_lista,'atestado.durTrat', atestado.durTrat.cdata, 1, '')
            if 'indAfast' in dir(atestado): validacoes_lista = validar_campo(validacoes_lista,'atestado.indAfast', atestado.indAfast.cdata, 1, 'S;N')
            if 'dscLesao' in dir(atestado): validacoes_lista = validar_campo(validacoes_lista,'atestado.dscLesao', atestado.dscLesao.cdata, 0, '702000000;702005000;702010000;702015000;702020000;702025000;702030000;702035000;702040000;702042000;702045000;702048000;702050000;702055000;702060000;702065000;702070000;702075000;702080000;702090000;704020000;704030000;704040000;704050000;704060000;704070000;704090000;706050000;706090000')
            if 'dscCompLesao' in dir(atestado): validacoes_lista = validar_campo(validacoes_lista,'atestado.dscCompLesao', atestado.dscCompLesao.cdata, 0, '')
            if 'diagProvavel' in dir(atestado): validacoes_lista = validar_campo(validacoes_lista,'atestado.diagProvavel', atestado.diagProvavel.cdata, 0, '')
            if 'codCID' in dir(atestado): validacoes_lista = validar_campo(validacoes_lista,'atestado.codCID', atestado.codCID.cdata, 1, '')
            if 'observacao' in dir(atestado): validacoes_lista = validar_campo(validacoes_lista,'atestado.observacao', atestado.observacao.cdata, 0, '')
            if 'nmEmit' in dir(atestado.emitente): validacoes_lista = validar_campo(validacoes_lista,'atestado.emitente.nmEmit', atestado.emitente.nmEmit.cdata, 1, '')
            if 'ideOC' in dir(atestado.emitente): validacoes_lista = validar_campo(validacoes_lista,'atestado.emitente.ideOC', atestado.emitente.ideOC.cdata, 1, '1;2;3')
            if 'nrOc' in dir(atestado.emitente): validacoes_lista = validar_campo(validacoes_lista,'atestado.emitente.nrOc', atestado.emitente.nrOc.cdata, 1, '')
            if 'ufOC' in dir(atestado.emitente): validacoes_lista = validar_campo(validacoes_lista,'atestado.emitente.ufOC', atestado.emitente.ufOC.cdata, 0, '')

    if 'catOrigem' in dir(evtCAT.cat):
        for catOrigem in evtCAT.cat.catOrigem:
            
            if 'dtCatOrig' in dir(catOrigem): validacoes_lista = validar_campo(validacoes_lista,'catOrigem.dtCatOrig', catOrigem.dtCatOrig.cdata, 1, '')
            if 'nrCatOrig' in dir(catOrigem): validacoes_lista = validar_campo(validacoes_lista,'catOrigem.nrCatOrig', catOrigem.nrCatOrig.cdata, 0, '')

    return validacoes_lista