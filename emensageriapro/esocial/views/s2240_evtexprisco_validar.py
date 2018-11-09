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


def validacoes_s2240_evtexprisco(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtExpRisco = doc.eSocial.evtExpRisco

    if 'indRetif' in dir(evtExpRisco.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideEvento.indRetif', evtExpRisco.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtExpRisco.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideEvento.nrRecibo', evtExpRisco.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtExpRisco.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideEvento.tpAmb', evtExpRisco.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtExpRisco.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideEvento.procEmi', evtExpRisco.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtExpRisco.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideEvento.verProc', evtExpRisco.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtExpRisco.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideEmpregador.tpInsc', evtExpRisco.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtExpRisco.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideEmpregador.nrInsc', evtExpRisco.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtExpRisco.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideVinculo.cpfTrab', evtExpRisco.ideVinculo.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtExpRisco.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideVinculo.nisTrab', evtExpRisco.ideVinculo.nisTrab.cdata, 0, '')
    if 'matricula' in dir(evtExpRisco.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideVinculo.matricula', evtExpRisco.ideVinculo.matricula.cdata, 0, '')
    if 'codCateg' in dir(evtExpRisco.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideVinculo.codCateg', evtExpRisco.ideVinculo.codCateg.cdata, 0, '')
    if 'dtIniCondicao' in dir(evtExpRisco.infoExpRisco): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.infoExpRisco.dtIniCondicao', evtExpRisco.infoExpRisco.dtIniCondicao.cdata, 1, '')
    if 'dscAtivDes' in dir(evtExpRisco.infoExpRisco.infoAtiv): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.infoExpRisco.infoAtiv.dscAtivDes', evtExpRisco.infoExpRisco.infoAtiv.dscAtivDes.cdata, 1, '')
    if 'iniExpRisco' in dir(evtExpRisco.infoExpRisco):
        for iniExpRisco in evtExpRisco.infoExpRisco.iniExpRisco:
       

    if 'infoAmb' in dir(evtExpRisco.infoExpRisco):
        for infoAmb in evtExpRisco.infoExpRisco.infoAmb:
       
            if 'codAmb' in dir(infoAmb): validacoes_lista = validar_campo(validacoes_lista,'infoAmb.codAmb', infoAmb.codAmb.cdata, 1, '')

    if 'ativPericInsal' in dir(evtExpRisco.infoExpRisco.infoAtiv):
        for ativPericInsal in evtExpRisco.infoExpRisco.infoAtiv.ativPericInsal:
       
            if 'codAtiv' in dir(ativPericInsal): validacoes_lista = validar_campo(validacoes_lista,'ativPericInsal.codAtiv', ativPericInsal.codAtiv.cdata, 1, '')

    if 'fatRisco' in dir(evtExpRisco.infoExpRisco):
        for fatRisco in evtExpRisco.infoExpRisco.fatRisco:
       
            if 'codFatRis' in dir(fatRisco): validacoes_lista = validar_campo(validacoes_lista,'fatRisco.codFatRis', fatRisco.codFatRis.cdata, 1, '01.01.001;01.01.002;01.01.003;01.01.004;01.01.005;01.01.006;01.01.007;01.01.008;01.01.009;01.01.010;01.01.011;01.01.012;01.01.013;01.01.014;01.01.015;01.01.016;01.01.017;01.01.018;01.01.019;01.01.999;02.01.001;02.01.002;02.01.003;02.01.004;02.01.005;02.01.006;02.01.007;02.01.008;02.01.009;02.01.010;02.01.011;02.01.012;02.01.013;02.01.014;02.01.015;02.01.016;02.01.017;02.01.018;02.01.019;02.01.020;02.01.021;02.01.022;02.01.023;02.01.024;02.01.025;02.01.026;02.01.027;02.01.028;02.01.029;02.01.030;02.01.031;02.01.032;02.01.033;02.01.034;02.01.035;02.01.036;02.01.037;02.01.038;02.01.039;02.01.040;02.01.041;02.01.042;02.01.043;02.01.044;02.01.045;02.01.046;02.01.047;02.01.048;02.01.049;02.01.050;02.01.051;02.01.052;02.01.053;02.01.054;02.01.055;02.01.056;02.01.057;02.01.058;02.01.059;02.01.060;02.01.061;02.01.062;02.01.063;02.01.064;02.01.065;02.01.066;02.01.067;02.01.068;02.01.069;02.01.070;02.01.071;02.01.072;02.01.073;02.01.074;02.01.075;02.01.076;02.01.077;02.01.078;02.01.079;02.01.080;02.01.081;02.01.082;02.01.083;02.01.084;02.01.085;02.01.086;02.01.087;02.01.088;02.01.089;02.01.090;02.01.091;02.01.092;02.01.093;02.01.094;02.01.095;02.01.096;02.01.097;02.01.098;02.01.099;02.01.100;02.01.101;02.01.102;02.01.103;02.01.104;02.01.105;02.01.106;02.01.107;02.01.108;02.01.109;02.01.110;02.01.111;02.01.112;02.01.113;02.01.114;02.01.115;02.01.116;02.01.117;02.01.118;02.01.119;02.01.120;02.01.121;02.01.122;02.01.123;02.01.124;02.01.125;02.01.126;02.01.127;02.01.128;02.01.129;02.01.130;02.01.131;02.01.132;02.01.133;02.01.134;02.01.135;02.01.136;02.01.137;02.01.138;02.01.139;02.01.140;02.01.141;02.01.142;02.01.143;02.01.144;02.01.145;02.01.146;02.01.147;02.01.148;02.01.149;02.01.150;02.01.151;02.01.152;02.01.153;02.01.154;02.01.155;02.01.156;02.01.157;02.01.158;02.01.159;02.01.160;02.01.161;02.01.162;02.01.163;02.01.164;02.01.165;02.01.166;02.01.167;02.01.168;02.01.169;02.01.170;02.01.171;02.01.172;02.01.173;02.01.174;02.01.175;02.01.176;02.01.177;02.01.178;02.01.179;02.01.180;02.01.181;02.01.182;02.01.183;02.01.184;02.01.185;02.01.186;02.01.187;02.01.188;02.01.189;02.01.190;02.01.191;02.01.192;02.01.193;02.01.194;02.01.195;02.01.196;02.01.197;02.01.198;02.01.199;02.01.200;02.01.201;02.01.202;02.01.203;02.01.204;02.01.205;02.01.206;02.01.207;02.01.208;02.01.209;02.01.210;02.01.211;02.01.212;02.01.213;02.01.214;02.01.215;02.01.216;02.01.217;02.01.218;02.01.219;02.01.220;02.01.221;02.01.222;02.01.223;02.01.224;02.01.225;02.01.226;02.01.227;02.01.228;02.01.229;02.01.230;02.01.231;02.01.232;02.01.233;02.01.234;02.01.235;02.01.236;02.01.237;02.01.238;02.01.239;02.01.240;02.01.241;02.01.242;02.01.243;02.01.244;02.01.245;02.01.246;02.01.247;02.01.248;02.01.249;02.01.250;02.01.251;02.01.252;02.01.253;02.01.254;02.01.255;02.01.256;02.01.257;02.01.258;02.01.259;02.01.260;02.01.261;02.01.262;02.01.263;02.01.264;02.01.265;02.01.266;02.01.267;02.01.268;02.01.269;02.01.270;02.01.271;02.01.272;02.01.273;02.01.274;02.01.275;02.01.276;02.01.277;02.01.278;02.01.279;02.01.280;02.01.281;02.01.282;02.01.283;02.01.284;02.01.285;02.01.286;02.01.287;02.01.288;02.01.289;02.01.290;02.01.291;02.01.292;02.01.293;02.01.294;02.01.295;02.01.296;02.01.297;02.01.298;02.01.299;02.01.300;02.01.301;02.01.302;02.01.303;02.01.304;02.01.305;02.01.306;02.01.307;02.01.308;02.01.309;02.01.310;02.01.311;02.01.312;02.01.313;02.01.314;02.01.315;02.01.316;02.01.317;02.01.318;02.01.319;02.01.320;02.01.321;02.01.322;02.01.323;02.01.324;02.01.325;02.01.326;02.01.327;02.01.328;02.01.329;02.01.330;02.01.331;02.01.332;02.01.333;02.01.334;02.01.335;02.01.336;02.01.337;02.01.338;02.01.339;02.01.340;02.01.341;02.01.342;02.01.343;02.01.344;02.01.345;02.01.346;02.01.347;02.01.348;02.01.349;02.01.350;02.01.351;02.01.352;02.01.353;02.01.354;02.01.355;02.01.356;02.01.357;02.01.358;02.01.359;02.01.360;02.01.361;02.01.362;02.01.363;02.01.364;02.01.365;02.01.366;02.01.367;02.01.368;02.01.369;02.01.370;02.01.371;02.01.372;02.01.373;02.01.374;02.01.375;02.01.376;02.01.377;02.01.378;02.01.379;02.01.380;02.01.381;02.01.382;02.01.383;02.01.384;02.01.385;02.01.386;02.01.387;02.01.388;02.01.389;02.01.390;02.01.391;02.01.392;02.01.393;02.01.394;02.01.395;02.01.396;02.01.397;02.01.398;02.01.399;02.01.400;02.01.401;02.01.402;02.01.403;02.01.404;02.01.405;02.01.406;02.01.407;02.01.408;02.01.409;02.01.410;02.01.411;02.01.412;02.01.413;02.01.414;02.01.415;02.01.416;02.01.417;02.01.418;02.01.419;02.01.420;02.01.421;02.01.422;02.01.423;02.01.424;02.01.425;02.01.426;02.01.427;02.01.428;02.01.429;02.01.430;02.01.431;02.01.432;02.01.433;02.01.434;02.01.435;02.01.436;02.01.437;02.01.438;02.01.439;02.01.440;02.01.441;02.01.442;02.01.443;02.01.444;02.01.445;02.01.446;02.01.447;02.01.448;02.01.449;02.01.450;02.01.451;02.01.452;02.01.453;02.01.454;02.01.455;02.01.456;02.01.457;02.01.458;02.01.459;02.01.460;02.01.461;02.01.462;02.01.463;02.01.464;02.01.465;02.01.466;02.01.467;02.01.468;02.01.469;02.01.470;02.01.471;02.01.472;02.01.473;02.01.474;02.01.475;02.01.476;02.01.477;02.01.478;02.01.479;02.01.480;02.01.481;02.01.482;02.01.483;02.01.484;02.01.485;02.01.486;02.01.487;02.01.488;02.01.489;02.01.490;02.01.491;02.01.492;02.01.493;02.01.494;02.01.495;02.01.496;02.01.497;02.01.498;02.01.499;02.01.500;02.01.501;02.01.502;02.01.503;02.01.504;02.01.505;02.01.506;02.01.507;02.01.508;02.01.509;02.01.510;02.01.511;02.01.512;02.01.513;02.01.514;02.01.515;02.01.516;02.01.517;02.01.518;02.01.519;02.01.520;02.01.521;02.01.522;02.01.523;02.01.524;02.01.525;02.01.526;02.01.527;02.01.528;02.01.529;02.01.530;02.01.531;02.01.532;02.01.533;02.01.534;02.01.535;02.01.536;02.01.537;02.01.538;02.01.539;02.01.540;02.01.541;02.01.542;02.01.543;02.01.544;02.01.545;02.01.546;02.01.547;02.01.548;02.01.549;02.01.550;02.01.551;02.01.552;02.01.553;02.01.554;02.01.555;02.01.556;02.01.557;02.01.558;02.01.559;02.01.560;02.01.561;02.01.562;02.01.563;02.01.564;02.01.565;02.01.566;02.01.567;02.01.568;02.01.569;02.01.570;02.01.571;02.01.572;02.01.573;02.01.574;02.01.575;02.01.576;02.01.577;02.01.578;02.01.579;02.01.580;02.01.581;02.01.582;02.01.583;02.01.584;02.01.585;02.01.586;02.01.587;02.01.588;02.01.589;02.01.590;02.01.591;02.01.592;02.01.593;02.01.594;02.01.595;02.01.596;02.01.597;02.01.598;02.01.599;02.01.600;02.01.601;02.01.602;02.01.603;02.01.604;02.01.605;02.01.606;02.01.607;02.01.608;02.01.609;02.01.610;02.01.611;02.01.612;02.01.613;02.01.614;02.01.615;02.01.616;02.01.617;02.01.618;02.01.619;02.01.620;02.01.621;02.01.622;02.01.623;02.01.624;02.01.625;02.01.626;02.01.627;02.01.628;02.01.629;02.01.630;02.01.631;02.01.632;02.01.633;02.01.634;02.01.635;02.01.636;02.01.637;02.01.638;02.01.639;02.01.640;02.01.641;02.01.642;02.01.643;02.01.644;02.01.645;02.01.646;02.01.647;02.01.648;02.01.649;02.01.650;02.01.651;02.01.652;02.01.653;02.01.654;02.01.655;02.01.656;02.01.657;02.01.658;02.01.659;02.01.660;02.01.661;02.01.662;02.01.663;02.01.664;02.01.665;02.01.666;02.01.667;02.01.668;02.01.669;02.01.670;02.01.671;02.01.672;02.01.673;02.01.674;02.01.675;02.01.676;02.01.677;02.01.678;02.01.679;02.01.680;02.01.681;02.01.682;02.01.683;02.01.684;02.01.685;02.01.686;02.01.687;02.01.688;02.01.689;02.01.690;02.01.691;02.01.692;02.01.693;02.01.694;02.01.695;02.01.696;02.01.697;02.01.698;02.01.699;02.01.700;02.01.701;02.01.702;02.01.703;02.01.704;02.01.705;02.01.706;02.01.707;02.01.708;02.01.709;02.01.710;02.01.711;02.01.712;02.01.713;02.01.714;02.01.715;02.01.716;02.01.717;02.01.718;02.01.719;02.01.720;02.01.721;02.01.722;02.01.723;02.01.724;02.01.725;02.01.726;02.01.727;02.01.728;02.01.729;02.01.730;02.01.731;02.01.732;02.01.733;02.01.734;02.01.735;02.01.736;02.01.737;02.01.738;02.01.739;02.01.740;02.01.741;02.01.742;02.01.743;02.01.744;02.01.745;02.01.746;02.01.747;02.01.748;02.01.749;02.01.750;02.01.751;02.01.752;02.01.753;02.01.754;02.01.755;02.01.756;02.01.757;02.01.758;02.01.759;02.01.760;02.01.761;02.01.762;02.01.763;02.01.764;02.01.765;02.01.766;02.01.767;02.01.768;02.01.769;02.01.770;02.01.771;02.01.772;02.01.773;02.01.774;02.01.775;02.01.776;02.01.777;02.01.778;02.01.779;02.01.780;02.01.781;02.01.782;02.01.783;02.01.784;02.01.785;02.01.786;02.01.787;02.01.788;02.01.789;02.01.790;02.01.791;02.01.792;02.01.793;02.01.794;02.01.795;02.01.796;02.01.797;02.01.798;02.01.799;02.01.800;02.01.801;02.01.802;02.01.803;02.01.804;02.01.805;02.01.806;02.01.807;02.01.808;02.01.809;02.01.810;02.01.811;02.01.812;02.01.813;02.01.814;02.01.815;02.01.816;02.01.817;02.01.818;02.01.819;02.01.820;02.01.821;02.01.822;02.01.823;02.01.824;02.01.825;02.01.826;02.01.827;02.01.828;02.01.829;02.01.830;02.01.831;02.01.832;02.01.833;02.01.834;02.01.835;02.01.836;02.01.837;02.01.838;02.01.839;02.01.840;02.01.841;02.01.999;03.01.001;03.01.002;03.01.003;03.01.004;03.01.005;03.01.006;03.01.007;03.01.008;03.01.009;03.01.010;03.01.011;03.01.012;03.01.013;03.01.014;03.01.999;04.01.001;04.01.002;04.01.003;04.01.004;04.01.005;04.01.006;04.01.007;04.01.008;04.01.009;04.01.999;04.02.001;04.02.002;04.02.999;04.03.001;04.03.002;04.03.003;04.03.004;04.03.005;04.03.006;04.03.999;04.04.001;04.04.002;04.04.003;04.04.004;04.04.999;05.01.001;05.01.002;05.01.003;05.01.004;05.01.005;05.01.006;05.01.007;05.01.008;05.01.009;05.01.010;05.01.011;05.01.012;05.01.013;05.01.014;05.01.015;05.01.016;05.01.017;05.01.999;06.01.001;06.01.002;06.01.003;06.01.004;06.01.005;06.01.006;06.01.999;07.01.001;07.01.002;07.01.003;07.01.999;08.01.001;08.01.002;08.01.999;09.01.001')
            if 'tpAval' in dir(fatRisco): validacoes_lista = validar_campo(validacoes_lista,'fatRisco.tpAval', fatRisco.tpAval.cdata, 1, '1;2')
            if 'intConc' in dir(fatRisco): validacoes_lista = validar_campo(validacoes_lista,'fatRisco.intConc', fatRisco.intConc.cdata, 0, '')
            if 'limTol' in dir(fatRisco): validacoes_lista = validar_campo(validacoes_lista,'fatRisco.limTol', fatRisco.limTol.cdata, 0, '')
            if 'unMed' in dir(fatRisco): validacoes_lista = validar_campo(validacoes_lista,'fatRisco.unMed', fatRisco.unMed.cdata, 0, '01;02;03;04;05;06;07;08;09;10;11;12;13;14;15;16;17;18')
            if 'tecMedicao' in dir(fatRisco): validacoes_lista = validar_campo(validacoes_lista,'fatRisco.tecMedicao', fatRisco.tecMedicao.cdata, 0, '')
            if 'insalubridade' in dir(fatRisco): validacoes_lista = validar_campo(validacoes_lista,'fatRisco.insalubridade', fatRisco.insalubridade.cdata, 0, 'S;N')
            if 'periculosidade' in dir(fatRisco): validacoes_lista = validar_campo(validacoes_lista,'fatRisco.periculosidade', fatRisco.periculosidade.cdata, 0, 'S;N')
            if 'aposentEsp' in dir(fatRisco): validacoes_lista = validar_campo(validacoes_lista,'fatRisco.aposentEsp', fatRisco.aposentEsp.cdata, 0, 'S;N')
            if 'utilizEPC' in dir(fatRisco.epcEpi): validacoes_lista = validar_campo(validacoes_lista,'fatRisco.epcEpi.utilizEPC', fatRisco.epcEpi.utilizEPC.cdata, 1, '0;1;2')
            if 'eficEpc' in dir(fatRisco.epcEpi): validacoes_lista = validar_campo(validacoes_lista,'fatRisco.epcEpi.eficEpc', fatRisco.epcEpi.eficEpc.cdata, 1, 'S;N')
            if 'utilizEPI' in dir(fatRisco.epcEpi): validacoes_lista = validar_campo(validacoes_lista,'fatRisco.epcEpi.utilizEPI', fatRisco.epcEpi.utilizEPI.cdata, 1, '0;1;2')

            if 'epc' in dir(fatRisco.epcEpi):
                for epc in fatRisco.epcEpi.epc:
               
                    if 'codEP' in dir(epc): validacoes_lista = validar_campo(validacoes_lista,'epc.codEP', epc.codEP.cdata, 1, '')
                    if 'dscEpc' in dir(epc): validacoes_lista = validar_campo(validacoes_lista,'epc.dscEpc', epc.dscEpc.cdata, 1, '')
                    if 'eficEpc' in dir(epc): validacoes_lista = validar_campo(validacoes_lista,'epc.eficEpc', epc.eficEpc.cdata, 0, 'S;N')
   
            if 'epi' in dir(fatRisco.epcEpi):
                for epi in fatRisco.epcEpi.epi:
               
                    if 'caEPI' in dir(epi): validacoes_lista = validar_campo(validacoes_lista,'epi.caEPI', epi.caEPI.cdata, 0, '')
                    if 'dscEPI' in dir(epi): validacoes_lista = validar_campo(validacoes_lista,'epi.dscEPI', epi.dscEPI.cdata, 0, '')
                    if 'eficEpi' in dir(epi): validacoes_lista = validar_campo(validacoes_lista,'epi.eficEpi', epi.eficEpi.cdata, 1, 'S;N')
                    if 'medProtecao' in dir(epi): validacoes_lista = validar_campo(validacoes_lista,'epi.medProtecao', epi.medProtecao.cdata, 1, 'S;N')
                    if 'condFuncto' in dir(epi): validacoes_lista = validar_campo(validacoes_lista,'epi.condFuncto', epi.condFuncto.cdata, 1, 'S;N')
                    if 'usoInint' in dir(epi): validacoes_lista = validar_campo(validacoes_lista,'epi.usoInint', epi.usoInint.cdata, 1, 'S;N')
                    if 'przValid' in dir(epi): validacoes_lista = validar_campo(validacoes_lista,'epi.przValid', epi.przValid.cdata, 1, 'S;N')
                    if 'periodicTroca' in dir(epi): validacoes_lista = validar_campo(validacoes_lista,'epi.periodicTroca', epi.periodicTroca.cdata, 1, 'S;N')
                    if 'higienizacao' in dir(epi): validacoes_lista = validar_campo(validacoes_lista,'epi.higienizacao', epi.higienizacao.cdata, 1, 'S;N')
   
    if 'respReg' in dir(evtExpRisco.infoExpRisco):
        for respReg in evtExpRisco.infoExpRisco.respReg:
       
            if 'cpfResp' in dir(respReg): validacoes_lista = validar_campo(validacoes_lista,'respReg.cpfResp', respReg.cpfResp.cdata, 1, '')
            if 'nisResp' in dir(respReg): validacoes_lista = validar_campo(validacoes_lista,'respReg.nisResp', respReg.nisResp.cdata, 1, '')
            if 'nmResp' in dir(respReg): validacoes_lista = validar_campo(validacoes_lista,'respReg.nmResp', respReg.nmResp.cdata, 1, '')
            if 'ideOC' in dir(respReg): validacoes_lista = validar_campo(validacoes_lista,'respReg.ideOC', respReg.ideOC.cdata, 1, '1;2;9')
            if 'dscOC' in dir(respReg): validacoes_lista = validar_campo(validacoes_lista,'respReg.dscOC', respReg.dscOC.cdata, 0, '')
            if 'nrOC' in dir(respReg): validacoes_lista = validar_campo(validacoes_lista,'respReg.nrOC', respReg.nrOC.cdata, 1, '')
            if 'ufOC' in dir(respReg): validacoes_lista = validar_campo(validacoes_lista,'respReg.ufOC', respReg.ufOC.cdata, 1, '')

    if 'obs' in dir(evtExpRisco.infoExpRisco):
        for obs in evtExpRisco.infoExpRisco.obs:
       
            if 'metErg' in dir(obs): validacoes_lista = validar_campo(validacoes_lista,'obs.metErg', obs.metErg.cdata, 0, '')
            if 'observacao' in dir(obs): validacoes_lista = validar_campo(validacoes_lista,'obs.observacao', obs.observacao.cdata, 0, '')

    if 'altExpRisco' in dir(evtExpRisco.infoExpRisco):
        for altExpRisco in evtExpRisco.infoExpRisco.altExpRisco:
       
            if 'dtAltCondicao' in dir(altExpRisco): validacoes_lista = validar_campo(validacoes_lista,'altExpRisco.dtAltCondicao', altExpRisco.dtAltCondicao.cdata, 1, '')

            if 'infoAmb' in dir(altExpRisco):
                for infoAmb in altExpRisco.infoAmb:
               
                    if 'codAmb' in dir(infoAmb): validacoes_lista = validar_campo(validacoes_lista,'infoAmb.codAmb', infoAmb.codAmb.cdata, 1, '')
                    if 'dscAtivDes' in dir(infoAmb): validacoes_lista = validar_campo(validacoes_lista,'infoAmb.dscAtivDes', infoAmb.dscAtivDes.cdata, 1, '')
   
    if 'fimExpRisco' in dir(evtExpRisco.infoExpRisco):
        for fimExpRisco in evtExpRisco.infoExpRisco.fimExpRisco:
       
            if 'dtFimCondicao' in dir(fimExpRisco): validacoes_lista = validar_campo(validacoes_lista,'fimExpRisco.dtFimCondicao', fimExpRisco.dtFimCondicao.cdata, 1, '')

            if 'infoAmb' in dir(fimExpRisco):
                for infoAmb in fimExpRisco.infoAmb:
               
                    if 'codAmb' in dir(infoAmb): validacoes_lista = validar_campo(validacoes_lista,'infoAmb.codAmb', infoAmb.codAmb.cdata, 1, '')
   
    if 'respReg' in dir(evtExpRisco.infoExpRisco):
        for respReg in evtExpRisco.infoExpRisco.respReg:
       
            if 'dtIni' in dir(respReg): validacoes_lista = validar_campo(validacoes_lista,'respReg.dtIni', respReg.dtIni.cdata, 1, '')
            if 'dtFim' in dir(respReg): validacoes_lista = validar_campo(validacoes_lista,'respReg.dtFim', respReg.dtFim.cdata, 0, '')
            if 'nisResp' in dir(respReg): validacoes_lista = validar_campo(validacoes_lista,'respReg.nisResp', respReg.nisResp.cdata, 1, '')
            if 'nrOc' in dir(respReg): validacoes_lista = validar_campo(validacoes_lista,'respReg.nrOc', respReg.nrOc.cdata, 1, '')
            if 'ufOC' in dir(respReg): validacoes_lista = validar_campo(validacoes_lista,'respReg.ufOC', respReg.ufOC.cdata, 0, '')

    return validacoes_lista