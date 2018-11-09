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


def validacoes_s2260_evtconvinterm(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtConvInterm = doc.eSocial.evtConvInterm

    if 'indRetif' in dir(evtConvInterm.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtConvInterm.ideEvento.indRetif', evtConvInterm.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtConvInterm.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtConvInterm.ideEvento.nrRecibo', evtConvInterm.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtConvInterm.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtConvInterm.ideEvento.tpAmb', evtConvInterm.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtConvInterm.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtConvInterm.ideEvento.procEmi', evtConvInterm.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtConvInterm.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtConvInterm.ideEvento.verProc', evtConvInterm.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtConvInterm.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtConvInterm.ideEmpregador.tpInsc', evtConvInterm.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtConvInterm.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtConvInterm.ideEmpregador.nrInsc', evtConvInterm.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtConvInterm.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtConvInterm.ideVinculo.cpfTrab', evtConvInterm.ideVinculo.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtConvInterm.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtConvInterm.ideVinculo.nisTrab', evtConvInterm.ideVinculo.nisTrab.cdata, 1, '')
    if 'matricula' in dir(evtConvInterm.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtConvInterm.ideVinculo.matricula', evtConvInterm.ideVinculo.matricula.cdata, 1, '')
    if 'codConv' in dir(evtConvInterm.infoConvInterm): validacoes_lista = validar_campo(validacoes_lista,'evtConvInterm.infoConvInterm.codConv', evtConvInterm.infoConvInterm.codConv.cdata, 1, '')
    if 'dtInicio' in dir(evtConvInterm.infoConvInterm): validacoes_lista = validar_campo(validacoes_lista,'evtConvInterm.infoConvInterm.dtInicio', evtConvInterm.infoConvInterm.dtInicio.cdata, 1, '')
    if 'dtFim' in dir(evtConvInterm.infoConvInterm): validacoes_lista = validar_campo(validacoes_lista,'evtConvInterm.infoConvInterm.dtFim', evtConvInterm.infoConvInterm.dtFim.cdata, 1, '')
    if 'dtPrevPgto' in dir(evtConvInterm.infoConvInterm): validacoes_lista = validar_campo(validacoes_lista,'evtConvInterm.infoConvInterm.dtPrevPgto', evtConvInterm.infoConvInterm.dtPrevPgto.cdata, 1, '')
    if 'codHorContrat' in dir(evtConvInterm.infoConvInterm.jornada): validacoes_lista = validar_campo(validacoes_lista,'evtConvInterm.infoConvInterm.jornada.codHorContrat', evtConvInterm.infoConvInterm.jornada.codHorContrat.cdata, 0, '')
    if 'dscJornada' in dir(evtConvInterm.infoConvInterm.jornada): validacoes_lista = validar_campo(validacoes_lista,'evtConvInterm.infoConvInterm.jornada.dscJornada', evtConvInterm.infoConvInterm.jornada.dscJornada.cdata, 0, '')
    if 'indLocal' in dir(evtConvInterm.infoConvInterm.localTrab): validacoes_lista = validar_campo(validacoes_lista,'evtConvInterm.infoConvInterm.localTrab.indLocal', evtConvInterm.infoConvInterm.localTrab.indLocal.cdata, 1, '0;1;2')
    if 'localTrabInterm' in dir(evtConvInterm.infoConvInterm.localTrab):
        for localTrabInterm in evtConvInterm.infoConvInterm.localTrab.localTrabInterm:
       
            if 'tpLograd' in dir(localTrabInterm): validacoes_lista = validar_campo(validacoes_lista,'localTrabInterm.tpLograd', localTrabInterm.tpLograd.cdata, 1, 'A;AC;ACA;ACL;AD;AE;AER;AL;AMD;AME;AN;ANT;ART;AT;ATL;A V;AV;AVC;AVM;AVV;BAL;BC;BCO;BEL;BL;BLO;BLS;BLV;BSQ;BVD;BX;C;CAL;CAM;CAN;CH;CHA;CIC;CIR;CJ;CJM;CMP;COL;COM;CON;COR;CPO;CRG;CTN;DSC;DSV;DT;EB;EIM;ENS;ENT;EQ;ESC;ESD;ESE;ESI;ESL;ESM;ESP;ESS;EST;ESV;ETA;ETC;ETD;ETN;ETP;ETT;EVA;EVD;EX;FAV;FAZ;FER;FNT;FRA;FTE;GAL;GJA;HAB;IA;IND;IOA;JD;JDE;LD;LGA;LGO;LOT;LRG;LT;MER;MNA;MOD;MRG;MRO;MTE;NUC;NUR;OUT;PAR;PAS;PAT;PC;PCE;PDA;PDO;PNT;PR;PRL;PRM;PRQ;PRR;PSA;PSG;PSP;PSS;PTE;PTO;Q;QTA;QTS;R;R I;R L;R P;R V;RAM;RCR;REC;RER;RES;RET;RLA;RMP;ROA;ROD;ROT;RPE;RPR;RTN;RTT;SEG;SIT;SRV;ST;SUB;TCH;TER;TR;TRV;TUN;TV;TVP;TVV;UNI;V;V C;V L;VAC;VAL;VCO;VD;V-E;VER;VEV;VL;VLA;VLE;VLT;VPE;VRT;ZIG')
            if 'dscLograd' in dir(localTrabInterm): validacoes_lista = validar_campo(validacoes_lista,'localTrabInterm.dscLograd', localTrabInterm.dscLograd.cdata, 1, '')
            if 'nrLograd' in dir(localTrabInterm): validacoes_lista = validar_campo(validacoes_lista,'localTrabInterm.nrLograd', localTrabInterm.nrLograd.cdata, 1, '')
            if 'complem' in dir(localTrabInterm): validacoes_lista = validar_campo(validacoes_lista,'localTrabInterm.complem', localTrabInterm.complem.cdata, 0, '')
            if 'bairro' in dir(localTrabInterm): validacoes_lista = validar_campo(validacoes_lista,'localTrabInterm.bairro', localTrabInterm.bairro.cdata, 0, '')
            if 'cep' in dir(localTrabInterm): validacoes_lista = validar_campo(validacoes_lista,'localTrabInterm.cep', localTrabInterm.cep.cdata, 1, '')
            if 'codMunic' in dir(localTrabInterm): validacoes_lista = validar_campo(validacoes_lista,'localTrabInterm.codMunic', localTrabInterm.codMunic.cdata, 1, '')
            if 'uf' in dir(localTrabInterm): validacoes_lista = validar_campo(validacoes_lista,'localTrabInterm.uf', localTrabInterm.uf.cdata, 1, '')

    return validacoes_lista