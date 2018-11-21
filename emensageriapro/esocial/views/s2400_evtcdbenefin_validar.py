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


def validacoes_s2400_evtcdbenefin(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtCdBenefIn = doc.eSocial.evtCdBenefIn

    if 'indRetif' in dir(evtCdBenefIn.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.ideEvento.indRetif', evtCdBenefIn.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtCdBenefIn.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.ideEvento.nrRecibo', evtCdBenefIn.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtCdBenefIn.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.ideEvento.tpAmb', evtCdBenefIn.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtCdBenefIn.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.ideEvento.procEmi', evtCdBenefIn.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtCdBenefIn.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.ideEvento.verProc', evtCdBenefIn.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtCdBenefIn.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.ideEmpregador.tpInsc', evtCdBenefIn.ideEmpregador.tpInsc.cdata, 1, '1')
    if 'nrInsc' in dir(evtCdBenefIn.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.ideEmpregador.nrInsc', evtCdBenefIn.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfBenef' in dir(evtCdBenefIn.beneficiario): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.beneficiario.cpfBenef', evtCdBenefIn.beneficiario.cpfBenef.cdata, 1, '')
    if 'nisBenef' in dir(evtCdBenefIn.beneficiario): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.beneficiario.nisBenef', evtCdBenefIn.beneficiario.nisBenef.cdata, 0, '')
    if 'nmBenefic' in dir(evtCdBenefIn.beneficiario): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.beneficiario.nmBenefic', evtCdBenefIn.beneficiario.nmBenefic.cdata, 1, '')
    if 'dtInicio' in dir(evtCdBenefIn.beneficiario): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.beneficiario.dtInicio', evtCdBenefIn.beneficiario.dtInicio.cdata, 1, '')
    if 'sexo' in dir(evtCdBenefIn.beneficiario): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.beneficiario.sexo', evtCdBenefIn.beneficiario.sexo.cdata, 1, 'M;F')
    if 'racaCor' in dir(evtCdBenefIn.beneficiario): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.beneficiario.racaCor', evtCdBenefIn.beneficiario.racaCor.cdata, 1, '1;2;3;4;5;6')
    if 'estCiv' in dir(evtCdBenefIn.beneficiario): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.beneficiario.estCiv', evtCdBenefIn.beneficiario.estCiv.cdata, 0, '1;2;3;4;5')
    if 'incFisMen' in dir(evtCdBenefIn.beneficiario): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.beneficiario.incFisMen', evtCdBenefIn.beneficiario.incFisMen.cdata, 1, 'S;N')
    if 'dtIncFisMen' in dir(evtCdBenefIn.beneficiario): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.beneficiario.dtIncFisMen', evtCdBenefIn.beneficiario.dtIncFisMen.cdata, 0, '')
    if 'dtNascto' in dir(evtCdBenefIn.beneficiario.dadosNasc): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.beneficiario.dadosNasc.dtNascto', evtCdBenefIn.beneficiario.dadosNasc.dtNascto.cdata, 1, '')
    if 'codMunic' in dir(evtCdBenefIn.beneficiario.dadosNasc): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.beneficiario.dadosNasc.codMunic', evtCdBenefIn.beneficiario.dadosNasc.codMunic.cdata, 0, '')
    if 'uf' in dir(evtCdBenefIn.beneficiario.dadosNasc): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.beneficiario.dadosNasc.uf', evtCdBenefIn.beneficiario.dadosNasc.uf.cdata, 0, '')
    if 'paisNascto' in dir(evtCdBenefIn.beneficiario.dadosNasc): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.beneficiario.dadosNasc.paisNascto', evtCdBenefIn.beneficiario.dadosNasc.paisNascto.cdata, 0, '008;040;329;331;334;337;341;345;351;355;357;358;041;359;361;365;367;369;372;375;379;383;386;043;388;391;395;396;399;403;411;420;423;426;047;427;431;434;438;440;442;445;447;449;450;053;452;455;458;461;464;467;472;474;476;477;059;485;488;490;493;494;495;497;499;501;505;063;507;508;511;517;521;525;528;531;535;538;064;542;545;548;551;556;563;566;569;573;575;065;576;578;580;583;586;589;593;599;603;607;069;611;623;625;628;640;647;660;665;670;675;009;072;676;677;678;685;687;690;691;695;697;700;073;705;710;715;720;728;731;735;738;741;744;077;748;750;754;756;759;764;767;770;772;776;080;780;782;783;785;788;790;791;795;800;805;081;810;815;820;823;824;827;828;831;833;840;083;845;847;848;850;855;858;863;866;870;873;085;875;888;890;087;088;090;013;093;097;098;100;101;105;106;108;111;115;017;119;127;131;137;141;145;149;150;151;152;020;153;154;158;160;161;163;165;169;173;177;023;183;187;190;193;195;196;198;199;229;232;025;235;237;239;240;243;244;245;246;247;249;031;251;253;255;259;263;267;271;275;281;285;037;289;291;293;297;301;305;309;313;317;325')
    if 'paisNac' in dir(evtCdBenefIn.beneficiario.dadosNasc): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.beneficiario.dadosNasc.paisNac', evtCdBenefIn.beneficiario.dadosNasc.paisNac.cdata, 1, '008;040;329;331;334;337;341;345;351;355;357;358;041;359;361;365;367;369;372;375;379;383;386;043;388;391;395;396;399;403;411;420;423;426;047;427;431;434;438;440;442;445;447;449;450;053;452;455;458;461;464;467;472;474;476;477;059;485;488;490;493;494;495;497;499;501;505;063;507;508;511;517;521;525;528;531;535;538;064;542;545;548;551;556;563;566;569;573;575;065;576;578;580;583;586;589;593;599;603;607;069;611;623;625;628;640;647;660;665;670;675;009;072;676;677;678;685;687;690;691;695;697;700;073;705;710;715;720;728;731;735;738;741;744;077;748;750;754;756;759;764;767;770;772;776;080;780;782;783;785;788;790;791;795;800;805;081;810;815;820;823;824;827;828;831;833;840;083;845;847;848;850;855;858;863;866;870;873;085;875;888;890;087;088;090;013;093;097;098;100;101;105;106;108;111;115;017;119;127;131;137;141;145;149;150;151;152;020;153;154;158;160;161;163;165;169;173;177;023;183;187;190;193;195;196;198;199;229;232;025;235;237;239;240;243;244;245;246;247;249;031;251;253;255;259;263;267;271;275;281;285;037;289;291;293;297;301;305;309;313;317;325')
    if 'nmMae' in dir(evtCdBenefIn.beneficiario.dadosNasc): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.beneficiario.dadosNasc.nmMae', evtCdBenefIn.beneficiario.dadosNasc.nmMae.cdata, 0, '')
    if 'nmPai' in dir(evtCdBenefIn.beneficiario.dadosNasc): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefIn.beneficiario.dadosNasc.nmPai', evtCdBenefIn.beneficiario.dadosNasc.nmPai.cdata, 0, '')
    if 'brasil' in dir(evtCdBenefIn.beneficiario.endereco):
        for brasil in evtCdBenefIn.beneficiario.endereco.brasil:
       
            if 'tpLograd' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.tpLograd', brasil.tpLograd.cdata, 1, 'A - Área;AC - Acesso;ACA - Acampamento;ACL - Acesso Local;AD - Adro;AE - Área Especial;AER - Aeroporto;AL - Alameda;AMD - Avenida Marginal Direita;AME - Avenida Marginal Esquerda;AN - Anel Viário;ANT - Antiga Estrada;ART - Artéria;AT - Alto;ATL - Atalho;A V - Área Verde;AV - Avenida;AVC - Avenida Contorno;AVM - Avenida Marginal;AVV - Avenida Velha;BAL - Balneário;BC - Beco;BCO - Buraco;BEL - Belvedere;BL - Bloco;BLO - Balão;BLS - Blocos;BLV - Bulevar;BSQ - Bosque;BVD - Boulevard;BX - Baixa;C - Cais;CAL - Calçada;CAM - Caminho;CAN - Canal;CH - Chácara;CHA - Chapadão;CIC - Ciclovia;CIR - Circular;CJ - Conjunto;CJM - Conjunto Mutirão;CMP - Complexo Viário;COL - Colônia;COM - Comunidade;CON - Condomínio;COR - Corredor;CPO - Campo;CRG - Córrego;CTN - Contorno;DSC - Descida;DSV - Desvio;DT - Distrito;EB - Entre Bloco;EIM - Estrada Intermunicipal;ENS - Enseada;ENT - Entrada Particular;EQ - Entre Quadra;ESC - Escada;ESD - Escadaria;ESE - Estrada Estadual;ESI - Estrada Vicinal;ESL - Estrada de Ligação;ESM - Estrada Municipal;ESP - Esplanada;ESS - Estrada de Servidão;EST - Estrada;ESV - Estrada Velha;ETA - Estrada Antiga;ETC - Estação;ETD - Estádio;ETN - Estância;ETP - Estrada Particular;ETT - Estacionamento;EVA - Evangélica;EVD - Elevada;EX - Eixo Industrial;FAV - Favela;FAZ - Fazenda;FER - Ferrovia;FNT - Fonte;FRA - Feira;FTE - Forte;GAL - Galeria;GJA - Granja;HAB - Núcleo Habitacional;IA - Ilha;IND - Indeterminado;IOA - Ilhota;JD - Jardim;JDE - Jardinete;LD - Ladeira;LGA - Lagoa;LGO - Lago;LOT - Loteamento;LRG - Largo;LT - Lote;MER - Mercado;MNA - Marina;MOD - Modulo;MRG - Projeção;MRO - Morro;MTE - Monte;NUC - Núcleo;NUR - Núcleo Rural;OUT - Outeiro;PAR - Paralela;PAS - Passeio;PAT - Pátio;PC - Praça;PCE - Praça de Esportes;PDA - Parada;PDO - Paradouro;PNT - Ponta;PR - Praia;PRL - Prolongamento;PRM - Parque Municipal;PRQ - Parque;PRR - Parque Residencial;PSA - Passarela;PSG - Passagem;PSP - Passagem de Pedestre;PSS - Passagem Subterrânea;PTE - Ponte;PTO - Porto;Q - Quadra;QTA - Quinta;QTS - Quintas;R - Rua;R I - Rua Integração;R L - Rua de Ligação;R P - Rua Particular;R V - Rua Velha;RAM - Ramal;RCR - Recreio;REC - Recanto;RER - Retiro;RES - Residencial;RET - Reta;RLA - Ruela;RMP - Rampa;ROA - Rodo Anel;ROD - Rodovia;ROT - Rotula;RPE - Rua de Pedestre;RPR - Margem;RTN - Retorno;RTT - Rotatória;SEG - Segunda Avenida;SIT - Sitio;SRV - Servidão;ST - Setor;SUB - Subida;TCH - Trincheira;TER - Terminal;TR - Trecho;TRV - Trevo;TUN - Túnel;TV - Travessa;TVP - Travessa Particular;TVV - Travessa Velha;UNI - Unidade;V - Via;V C - Via Coletora;V L - Via Local;VAC - Via de Acesso;VAL - Vala;VCO - Via Costeira;VD - Viaduto;V-E - Via Expressa;VER - Vereda;VEV - Via Elevado;VL - Vila;VLA - Viela;VLE - Vale;VLT - Via Litorânea;VPE - Via de Pedestre;VRT - Variante;ZIG - Zigue-Zague')
            if 'dscLograd' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.dscLograd', brasil.dscLograd.cdata, 1, '')
            if 'nrLograd' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.nrLograd', brasil.nrLograd.cdata, 1, '')
            if 'complemento' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.complemento', brasil.complemento.cdata, 0, '')
            if 'bairro' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.bairro', brasil.bairro.cdata, 0, '')
            if 'cep' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.cep', brasil.cep.cdata, 1, '')
            if 'codMunic' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.codMunic', brasil.codMunic.cdata, 1, '')
            if 'uf' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.uf', brasil.uf.cdata, 1, '')

    if 'exterior' in dir(evtCdBenefIn.beneficiario.endereco):
        for exterior in evtCdBenefIn.beneficiario.endereco.exterior:
       
            if 'paisResid' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.paisResid', exterior.paisResid.cdata, 1, '008;040;329;331;334;337;341;345;351;355;357;358;041;359;361;365;367;369;372;375;379;383;386;043;388;391;395;396;399;403;411;420;423;426;047;427;431;434;438;440;442;445;447;449;450;053;452;455;458;461;464;467;472;474;476;477;059;485;488;490;493;494;495;497;499;501;505;063;507;508;511;517;521;525;528;531;535;538;064;542;545;548;551;556;563;566;569;573;575;065;576;578;580;583;586;589;593;599;603;607;069;611;623;625;628;640;647;660;665;670;675;009;072;676;677;678;685;687;690;691;695;697;700;073;705;710;715;720;728;731;735;738;741;744;077;748;750;754;756;759;764;767;770;772;776;080;780;782;783;785;788;790;791;795;800;805;081;810;815;820;823;824;827;828;831;833;840;083;845;847;848;850;855;858;863;866;870;873;085;875;888;890;087;088;090;013;093;097;098;100;101;105;106;108;111;115;017;119;127;131;137;141;145;149;150;151;152;020;153;154;158;160;161;163;165;169;173;177;023;183;187;190;193;195;196;198;199;229;232;025;235;237;239;240;243;244;245;246;247;249;031;251;253;255;259;263;267;271;275;281;285;037;289;291;293;297;301;305;309;313;317;325')
            if 'dscLograd' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.dscLograd', exterior.dscLograd.cdata, 1, '')
            if 'nrLograd' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.nrLograd', exterior.nrLograd.cdata, 1, '')
            if 'complemento' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.complemento', exterior.complemento.cdata, 0, '')
            if 'bairro' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.bairro', exterior.bairro.cdata, 0, '')
            if 'nmCid' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.nmCid', exterior.nmCid.cdata, 1, '')
            if 'codPostal' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.codPostal', exterior.codPostal.cdata, 0, '')

    if 'dependente' in dir(evtCdBenefIn.beneficiario):
        for dependente in evtCdBenefIn.beneficiario.dependente:
       
            if 'tpDep' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.tpDep', dependente.tpDep.cdata, 1, '')
            if 'nmDep' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.nmDep', dependente.nmDep.cdata, 1, '')
            if 'dtNascto' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.dtNascto', dependente.dtNascto.cdata, 1, '')
            if 'cpfDep' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.cpfDep', dependente.cpfDep.cdata, 0, '')
            if 'sexoDep' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.sexoDep', dependente.sexoDep.cdata, 1, 'M;F')
            if 'depIRRF' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.depIRRF', dependente.depIRRF.cdata, 1, 'S;N')
            if 'incFisMen' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.incFisMen', dependente.incFisMen.cdata, 1, 'S;N')
            if 'depFinsPrev' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.depFinsPrev', dependente.depFinsPrev.cdata, 1, 'S;N')

    return validacoes_lista