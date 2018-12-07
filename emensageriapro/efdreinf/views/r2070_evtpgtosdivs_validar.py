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


def validacoes_r2070_evtpgtosdivs(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtPgtosDivs = doc.Reinf.evtPgtosDivs

    if 'indRetif' in dir(evtPgtosDivs.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtPgtosDivs.ideEvento.indRetif', evtPgtosDivs.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtPgtosDivs.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtPgtosDivs.ideEvento.nrRecibo', evtPgtosDivs.ideEvento.nrRecibo.cdata, 0, '')
    if 'perApur' in dir(evtPgtosDivs.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtPgtosDivs.ideEvento.perApur', evtPgtosDivs.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtPgtosDivs.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtPgtosDivs.ideEvento.tpAmb', evtPgtosDivs.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtPgtosDivs.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtPgtosDivs.ideEvento.procEmi', evtPgtosDivs.ideEvento.procEmi.cdata, 1, '1;2')
    if 'verProc' in dir(evtPgtosDivs.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtPgtosDivs.ideEvento.verProc', evtPgtosDivs.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtPgtosDivs.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtPgtosDivs.ideContri.tpInsc', evtPgtosDivs.ideContri.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtPgtosDivs.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtPgtosDivs.ideContri.nrInsc', evtPgtosDivs.ideContri.nrInsc.cdata, 1, '')
    if 'codPgto' in dir(evtPgtosDivs.ideBenef): validacoes_lista = validar_campo(validacoes_lista,'evtPgtosDivs.ideBenef.codPgto', evtPgtosDivs.ideBenef.codPgto.cdata, 1, '')
    if 'tpInscBenef' in dir(evtPgtosDivs.ideBenef): validacoes_lista = validar_campo(validacoes_lista,'evtPgtosDivs.ideBenef.tpInscBenef', evtPgtosDivs.ideBenef.tpInscBenef.cdata, 0, '1;2')
    if 'nrInscBenef' in dir(evtPgtosDivs.ideBenef): validacoes_lista = validar_campo(validacoes_lista,'evtPgtosDivs.ideBenef.nrInscBenef', evtPgtosDivs.ideBenef.nrInscBenef.cdata, 0, '')
    if 'nmRazaoBenef' in dir(evtPgtosDivs.ideBenef): validacoes_lista = validar_campo(validacoes_lista,'evtPgtosDivs.ideBenef.nmRazaoBenef', evtPgtosDivs.ideBenef.nmRazaoBenef.cdata, 1, '')
    if 'infoResidExt' in dir(evtPgtosDivs.ideBenef):
        for infoResidExt in evtPgtosDivs.ideBenef.infoResidExt:
       
            if 'paisResid' in dir(infoResidExt.infoEnder): validacoes_lista = validar_campo(validacoes_lista,'infoResidExt.infoEnder.paisResid', infoResidExt.infoEnder.paisResid.cdata, 1, '008;040;329;331;334;337;341;345;351;355;357;358;041;359;361;365;367;369;372;375;379;383;386;043;388;391;395;396;399;403;411;420;423;426;047;427;431;434;438;440;442;445;447;449;450;053;452;455;458;461;464;467;472;474;476;477;059;485;488;490;493;494;495;497;499;501;505;063;507;508;511;517;521;525;528;531;535;538;064;542;545;548;551;556;563;566;569;573;575;065;576;578;580;583;586;589;593;599;603;607;069;611;623;625;628;640;647;660;665;670;675;009;072;676;677;678;685;687;690;691;695;697;700;073;705;710;715;720;728;731;735;738;741;744;077;748;750;754;756;759;764;767;770;772;776;080;780;782;783;785;788;790;791;795;800;805;081;810;815;820;823;824;827;828;831;833;840;083;845;847;848;850;855;858;863;866;870;873;085;875;888;890;087;088;090;013;093;097;098;100;101;105;106;108;111;115;017;119;127;131;137;141;145;149;150;151;152;020;153;154;158;160;161;163;165;169;173;177;023;183;187;190;193;195;196;198;199;229;232;025;235;237;239;240;243;244;245;246;247;249;031;251;253;255;259;263;267;271;275;281;285;037;289;291;293;297;301;305;309;313;317;325')
            if 'dscLograd' in dir(infoResidExt.infoEnder): validacoes_lista = validar_campo(validacoes_lista,'infoResidExt.infoEnder.dscLograd', infoResidExt.infoEnder.dscLograd.cdata, 1, '')
            if 'nrLograd' in dir(infoResidExt.infoEnder): validacoes_lista = validar_campo(validacoes_lista,'infoResidExt.infoEnder.nrLograd', infoResidExt.infoEnder.nrLograd.cdata, 0, '')
            if 'complem' in dir(infoResidExt.infoEnder): validacoes_lista = validar_campo(validacoes_lista,'infoResidExt.infoEnder.complem', infoResidExt.infoEnder.complem.cdata, 0, '')
            if 'bairro' in dir(infoResidExt.infoEnder): validacoes_lista = validar_campo(validacoes_lista,'infoResidExt.infoEnder.bairro', infoResidExt.infoEnder.bairro.cdata, 0, '')
            if 'cidade' in dir(infoResidExt.infoEnder): validacoes_lista = validar_campo(validacoes_lista,'infoResidExt.infoEnder.cidade', infoResidExt.infoEnder.cidade.cdata, 0, '')
            if 'codPostal' in dir(infoResidExt.infoEnder): validacoes_lista = validar_campo(validacoes_lista,'infoResidExt.infoEnder.codPostal', infoResidExt.infoEnder.codPostal.cdata, 0, '')
            if 'indNIF' in dir(infoResidExt.infoFiscal): validacoes_lista = validar_campo(validacoes_lista,'infoResidExt.infoFiscal.indNIF', infoResidExt.infoFiscal.indNIF.cdata, 1, '1;2;3')
            if 'nifBenef' in dir(infoResidExt.infoFiscal): validacoes_lista = validar_campo(validacoes_lista,'infoResidExt.infoFiscal.nifBenef', infoResidExt.infoFiscal.nifBenef.cdata, 0, '')
            if 'relFontePagad' in dir(infoResidExt.infoFiscal): validacoes_lista = validar_campo(validacoes_lista,'infoResidExt.infoFiscal.relFontePagad', infoResidExt.infoFiscal.relFontePagad.cdata, 0, '')

    if 'infoMolestia' in dir(evtPgtosDivs.ideBenef):
        for infoMolestia in evtPgtosDivs.ideBenef.infoMolestia:
       
            if 'dtLaudo' in dir(infoMolestia): validacoes_lista = validar_campo(validacoes_lista,'infoMolestia.dtLaudo', infoMolestia.dtLaudo.cdata, 1, '')

    if 'ideEstab' in dir(evtPgtosDivs.ideBenef.infoPgto):
        for ideEstab in evtPgtosDivs.ideBenef.infoPgto.ideEstab:
       
            if 'tpInsc' in dir(ideEstab): validacoes_lista = validar_campo(validacoes_lista,'ideEstab.tpInsc', ideEstab.tpInsc.cdata, 1, '1;2')
            if 'nrInsc' in dir(ideEstab): validacoes_lista = validar_campo(validacoes_lista,'ideEstab.nrInsc', ideEstab.nrInsc.cdata, 1, '')

            if 'pgtoPF' in dir(ideEstab.pgtoResidBR):
                for pgtoPF in ideEstab.pgtoResidBR.pgtoPF:
               
                    if 'dtPgto' in dir(pgtoPF): validacoes_lista = validar_campo(validacoes_lista,'pgtoPF.dtPgto', pgtoPF.dtPgto.cdata, 1, '')
                    if 'indSuspExig' in dir(pgtoPF): validacoes_lista = validar_campo(validacoes_lista,'pgtoPF.indSuspExig', pgtoPF.indSuspExig.cdata, 1, 'S;N')
                    if 'indDecTerceiro' in dir(pgtoPF): validacoes_lista = validar_campo(validacoes_lista,'pgtoPF.indDecTerceiro', pgtoPF.indDecTerceiro.cdata, 1, 'S;N')
                    if 'vlrRendTributavel' in dir(pgtoPF): validacoes_lista = validar_campo(validacoes_lista,'pgtoPF.vlrRendTributavel', pgtoPF.vlrRendTributavel.cdata, 1, '')
                    if 'vlrIRRF' in dir(pgtoPF): validacoes_lista = validar_campo(validacoes_lista,'pgtoPF.vlrIRRF', pgtoPF.vlrIRRF.cdata, 1, '')
   
            if 'pgtoPJ' in dir(ideEstab.pgtoResidBR):
                for pgtoPJ in ideEstab.pgtoResidBR.pgtoPJ:
               
                    if 'dtPagto' in dir(pgtoPJ): validacoes_lista = validar_campo(validacoes_lista,'pgtoPJ.dtPagto', pgtoPJ.dtPagto.cdata, 1, '')
                    if 'vlrRendTributavel' in dir(pgtoPJ): validacoes_lista = validar_campo(validacoes_lista,'pgtoPJ.vlrRendTributavel', pgtoPJ.vlrRendTributavel.cdata, 1, '')
                    if 'vlrRet' in dir(pgtoPJ): validacoes_lista = validar_campo(validacoes_lista,'pgtoPJ.vlrRet', pgtoPJ.vlrRet.cdata, 1, '')
   
            if 'pgtoResidExt' in dir(ideEstab):
                for pgtoResidExt in ideEstab.pgtoResidExt:
               
                    if 'dtPagto' in dir(pgtoResidExt): validacoes_lista = validar_campo(validacoes_lista,'pgtoResidExt.dtPagto', pgtoResidExt.dtPagto.cdata, 1, '')
                    if 'tpRendimento' in dir(pgtoResidExt): validacoes_lista = validar_campo(validacoes_lista,'pgtoResidExt.tpRendimento', pgtoResidExt.tpRendimento.cdata, 1, '')
                    if 'formaTributacao' in dir(pgtoResidExt): validacoes_lista = validar_campo(validacoes_lista,'pgtoResidExt.formaTributacao', pgtoResidExt.formaTributacao.cdata, 1, '')
                    if 'vlrPgto' in dir(pgtoResidExt): validacoes_lista = validar_campo(validacoes_lista,'pgtoResidExt.vlrPgto', pgtoResidExt.vlrPgto.cdata, 1, '')
                    if 'vlrRet' in dir(pgtoResidExt): validacoes_lista = validar_campo(validacoes_lista,'pgtoResidExt.vlrRet', pgtoResidExt.vlrRet.cdata, 1, '')
   
    return validacoes_lista