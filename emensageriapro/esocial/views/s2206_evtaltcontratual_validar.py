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


def validacoes_s2206_evtaltcontratual(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtAltContratual = doc.eSocial.evtAltContratual

    if 'indRetif' in dir(evtAltContratual.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideEvento.indRetif', evtAltContratual.ideEvento.indRetif.cdata, 1, u'1;2')
    if 'nrRecibo' in dir(evtAltContratual.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideEvento.nrRecibo', evtAltContratual.ideEvento.nrRecibo.cdata, 0, u'')
    if 'tpAmb' in dir(evtAltContratual.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideEvento.tpAmb', evtAltContratual.ideEvento.tpAmb.cdata, 1, u'1;2')
    if 'procEmi' in dir(evtAltContratual.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideEvento.procEmi', evtAltContratual.ideEvento.procEmi.cdata, 1, u'1;2;3;4;5')
    if 'verProc' in dir(evtAltContratual.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideEvento.verProc', evtAltContratual.ideEvento.verProc.cdata, 1, u'')
    if 'tpInsc' in dir(evtAltContratual.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideEmpregador.tpInsc', evtAltContratual.ideEmpregador.tpInsc.cdata, 1, u'1;2;3;4')
    if 'nrInsc' in dir(evtAltContratual.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideEmpregador.nrInsc', evtAltContratual.ideEmpregador.nrInsc.cdata, 1, u'')
    if 'cpfTrab' in dir(evtAltContratual.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideVinculo.cpfTrab', evtAltContratual.ideVinculo.cpfTrab.cdata, 1, u'')
    if 'nisTrab' in dir(evtAltContratual.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideVinculo.nisTrab', evtAltContratual.ideVinculo.nisTrab.cdata, 1, u'')
    if 'matricula' in dir(evtAltContratual.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideVinculo.matricula', evtAltContratual.ideVinculo.matricula.cdata, 1, u'')
    if 'dtAlteracao' in dir(evtAltContratual.altContratual): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.dtAlteracao', evtAltContratual.altContratual.dtAlteracao.cdata, 1, u'')
    if 'dtEf' in dir(evtAltContratual.altContratual): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.dtEf', evtAltContratual.altContratual.dtEf.cdata, 0, u'')
    if 'dscAlt' in dir(evtAltContratual.altContratual): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.dscAlt', evtAltContratual.altContratual.dscAlt.cdata, 0, u'')
    if 'tpRegPrev' in dir(evtAltContratual.altContratual.vinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.vinculo.tpRegPrev', evtAltContratual.altContratual.vinculo.tpRegPrev.cdata, 1, u'1;2;3')
    if 'codCargo' in dir(evtAltContratual.altContratual.infoContrato): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.codCargo', evtAltContratual.altContratual.infoContrato.codCargo.cdata, 0, u'')
    if 'codFuncao' in dir(evtAltContratual.altContratual.infoContrato): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.codFuncao', evtAltContratual.altContratual.infoContrato.codFuncao.cdata, 0, u'')
    if 'codCateg' in dir(evtAltContratual.altContratual.infoContrato): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.codCateg', evtAltContratual.altContratual.infoContrato.codCateg.cdata, 1, u'101;102;103;104;105;106;111;201;202;301;302;303;305;306;307;308;309;401;410;701;711;712;721;722;723;731;734;738;741;751;761;771;781;901;902;903;904;905')
    if 'codCarreira' in dir(evtAltContratual.altContratual.infoContrato): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.codCarreira', evtAltContratual.altContratual.infoContrato.codCarreira.cdata, 0, u'')
    if 'dtIngrCarr' in dir(evtAltContratual.altContratual.infoContrato): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.dtIngrCarr', evtAltContratual.altContratual.infoContrato.dtIngrCarr.cdata, 0, u'')
    if 'vrSalFx' in dir(evtAltContratual.altContratual.infoContrato.remuneracao): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.remuneracao.vrSalFx', evtAltContratual.altContratual.infoContrato.remuneracao.vrSalFx.cdata, 1, u'')
    if 'undSalFixo' in dir(evtAltContratual.altContratual.infoContrato.remuneracao): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.remuneracao.undSalFixo', evtAltContratual.altContratual.infoContrato.remuneracao.undSalFixo.cdata, 1, u'1;2;3;4;5;6;7')
    if 'dscSalVar' in dir(evtAltContratual.altContratual.infoContrato.remuneracao): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.remuneracao.dscSalVar', evtAltContratual.altContratual.infoContrato.remuneracao.dscSalVar.cdata, 0, u'')
    if 'tpContr' in dir(evtAltContratual.altContratual.infoContrato.duracao): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.duracao.tpContr', evtAltContratual.altContratual.infoContrato.duracao.tpContr.cdata, 1, u'1;2')
    if 'dtTerm' in dir(evtAltContratual.altContratual.infoContrato.duracao): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.duracao.dtTerm', evtAltContratual.altContratual.infoContrato.duracao.dtTerm.cdata, 0, u'')
    if 'objDet' in dir(evtAltContratual.altContratual.infoContrato.duracao): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.duracao.objDet', evtAltContratual.altContratual.infoContrato.duracao.objDet.cdata, 0, u'')
    if 'infoCeletista' in dir(evtAltContratual.altContratual.infoRegimeTrab):
        for infoCeletista in evtAltContratual.altContratual.infoRegimeTrab.infoCeletista:

            if 'tpRegJor' in dir(infoCeletista): validacoes_lista = validar_campo(validacoes_lista,'infoCeletista.tpRegJor', infoCeletista.tpRegJor.cdata, 1, u'1;2;3;4')
            if 'natAtividade' in dir(infoCeletista): validacoes_lista = validar_campo(validacoes_lista,'infoCeletista.natAtividade', infoCeletista.natAtividade.cdata, 1, u'1;2')
            if 'dtBase' in dir(infoCeletista): validacoes_lista = validar_campo(validacoes_lista,'infoCeletista.dtBase', infoCeletista.dtBase.cdata, 0, u'')
            if 'cnpjSindCategProf' in dir(infoCeletista): validacoes_lista = validar_campo(validacoes_lista,'infoCeletista.cnpjSindCategProf', infoCeletista.cnpjSindCategProf.cdata, 1, u'')

            if 'trabTemp' in dir(infoCeletista):
                for trabTemp in infoCeletista.trabTemp:

                    if 'justProrr' in dir(trabTemp): validacoes_lista = validar_campo(validacoes_lista,'trabTemp.justProrr', trabTemp.justProrr.cdata, 1, u'')

            if 'aprend' in dir(infoCeletista):
                for aprend in infoCeletista.aprend:

                    if 'tpInsc' in dir(aprend): validacoes_lista = validar_campo(validacoes_lista,'aprend.tpInsc', aprend.tpInsc.cdata, 1, u'1;2;3;4')
                    if 'nrInsc' in dir(aprend): validacoes_lista = validar_campo(validacoes_lista,'aprend.nrInsc', aprend.nrInsc.cdata, 1, u'')

    if 'infoEstatutario' in dir(evtAltContratual.altContratual.infoRegimeTrab):
        for infoEstatutario in evtAltContratual.altContratual.infoRegimeTrab.infoEstatutario:

            if 'tpPlanRP' in dir(infoEstatutario): validacoes_lista = validar_campo(validacoes_lista,'infoEstatutario.tpPlanRP', infoEstatutario.tpPlanRP.cdata, 1, u'1;2')
            if 'indTetoRGPS' in dir(infoEstatutario): validacoes_lista = validar_campo(validacoes_lista,'infoEstatutario.indTetoRGPS', infoEstatutario.indTetoRGPS.cdata, 0, u'S;N')
            if 'indAbonoPerm' in dir(infoEstatutario): validacoes_lista = validar_campo(validacoes_lista,'infoEstatutario.indAbonoPerm', infoEstatutario.indAbonoPerm.cdata, 0, u'S;N')
            if 'indParcRemun' in dir(infoEstatutario): validacoes_lista = validar_campo(validacoes_lista,'infoEstatutario.indParcRemun', infoEstatutario.indParcRemun.cdata, 0, u'S;N')

    if 'localTrabGeral' in dir(evtAltContratual.altContratual.infoContrato.localTrabalho):
        for localTrabGeral in evtAltContratual.altContratual.infoContrato.localTrabalho.localTrabGeral:

            if 'tpInsc' in dir(localTrabGeral): validacoes_lista = validar_campo(validacoes_lista,'localTrabGeral.tpInsc', localTrabGeral.tpInsc.cdata, 1, u'1;2;3;4')
            if 'nrInsc' in dir(localTrabGeral): validacoes_lista = validar_campo(validacoes_lista,'localTrabGeral.nrInsc', localTrabGeral.nrInsc.cdata, 1, u'')
            if 'descComp' in dir(localTrabGeral): validacoes_lista = validar_campo(validacoes_lista,'localTrabGeral.descComp', localTrabGeral.descComp.cdata, 0, u'')

    if 'localTrabDom' in dir(evtAltContratual.altContratual.infoContrato.localTrabalho):
        for localTrabDom in evtAltContratual.altContratual.infoContrato.localTrabalho.localTrabDom:

            if 'tpLograd' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.tpLograd', localTrabDom.tpLograd.cdata, 1, u'A;AC;ACA;ACL;AD;AE;AER;AL;AMD;AME;AN;ANT;ART;AT;ATL;A V;AV;AVC;AVM;AVV;BAL;BC;BCO;BEL;BL;BLO;BLS;BLV;BSQ;BVD;BX;C;CAL;CAM;CAN;CH;CHA;CIC;CIR;CJ;CJM;CMP;COL;COM;CON;COR;CPO;CRG;CTN;DSC;DSV;DT;EB;EIM;ENS;ENT;EQ;ESC;ESD;ESE;ESI;ESL;ESM;ESP;ESS;EST;ESV;ETA;ETC;ETD;ETN;ETP;ETT;EVA;EVD;EX;FAV;FAZ;FER;FNT;FRA;FTE;GAL;GJA;HAB;IA;IND;IOA;JD;JDE;LD;LGA;LGO;LOT;LRG;LT;MER;MNA;MOD;MRG;MRO;MTE;NUC;NUR;OUT;PAR;PAS;PAT;PC;PCE;PDA;PDO;PNT;PR;PRL;PRM;PRQ;PRR;PSA;PSG;PSP;PSS;PTE;PTO;Q;QTA;QTS;R;R I;R L;R P;R V;RAM;RCR;REC;RER;RES;RET;RLA;RMP;ROA;ROD;ROT;RPE;RPR;RTN;RTT;SEG;SIT;SRV;ST;SUB;TCH;TER;TR;TRV;TUN;TV;TVP;TVV;UNI;V;V C;V L;VAC;VAL;VCO;VD;V-E;VER;VEV;VL;VLA;VLE;VLT;VPE;VRT;ZIG')
            if 'dscLograd' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.dscLograd', localTrabDom.dscLograd.cdata, 1, u'')
            if 'nrLograd' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.nrLograd', localTrabDom.nrLograd.cdata, 1, u'')
            if 'complemento' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.complemento', localTrabDom.complemento.cdata, 0, u'')
            if 'bairro' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.bairro', localTrabDom.bairro.cdata, 0, u'')
            if 'cep' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.cep', localTrabDom.cep.cdata, 1, u'')
            if 'codMunic' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.codMunic', localTrabDom.codMunic.cdata, 1, u'')
            if 'uf' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.uf', localTrabDom.uf.cdata, 1, u'')

    if 'horContratual' in dir(evtAltContratual.altContratual.infoContrato):
        for horContratual in evtAltContratual.altContratual.infoContrato.horContratual:

            if 'qtdHrsSem' in dir(horContratual): validacoes_lista = validar_campo(validacoes_lista,'horContratual.qtdHrsSem', horContratual.qtdHrsSem.cdata, 0, u'')
            if 'tpJornada' in dir(horContratual): validacoes_lista = validar_campo(validacoes_lista,'horContratual.tpJornada', horContratual.tpJornada.cdata, 1, u'1;2;3;9')
            if 'dscTpJorn' in dir(horContratual): validacoes_lista = validar_campo(validacoes_lista,'horContratual.dscTpJorn', horContratual.dscTpJorn.cdata, 0, u'')
            if 'tmpParc' in dir(horContratual): validacoes_lista = validar_campo(validacoes_lista,'horContratual.tmpParc', horContratual.tmpParc.cdata, 1, u'0;1;2;3')

            if 'horario' in dir(horContratual):
                for horario in horContratual.horario:

                    if 'dia' in dir(horario): validacoes_lista = validar_campo(validacoes_lista,'horario.dia', horario.dia.cdata, 1, u'1;2;3;4;5;6;7;8')
                    if 'codHorContrat' in dir(horario): validacoes_lista = validar_campo(validacoes_lista,'horario.codHorContrat', horario.codHorContrat.cdata, 1, u'')

    if 'filiacaoSindical' in dir(evtAltContratual.altContratual.infoContrato):
        for filiacaoSindical in evtAltContratual.altContratual.infoContrato.filiacaoSindical:

            if 'cnpjSindTrab' in dir(filiacaoSindical): validacoes_lista = validar_campo(validacoes_lista,'filiacaoSindical.cnpjSindTrab', filiacaoSindical.cnpjSindTrab.cdata, 1, u'')

    if 'alvaraJudicial' in dir(evtAltContratual.altContratual.infoContrato):
        for alvaraJudicial in evtAltContratual.altContratual.infoContrato.alvaraJudicial:

            if 'nrProcJud' in dir(alvaraJudicial): validacoes_lista = validar_campo(validacoes_lista,'alvaraJudicial.nrProcJud', alvaraJudicial.nrProcJud.cdata, 1, u'')

    if 'observacoes' in dir(evtAltContratual.altContratual.infoContrato):
        for observacoes in evtAltContratual.altContratual.infoContrato.observacoes:

            if 'observacao' in dir(observacoes): validacoes_lista = validar_campo(validacoes_lista,'observacoes.observacao', observacoes.observacao.cdata, 1, u'')

    if 'servPubl' in dir(evtAltContratual.altContratual.infoContrato):
        for servPubl in evtAltContratual.altContratual.infoContrato.servPubl:

            if 'mtvAlter' in dir(servPubl): validacoes_lista = validar_campo(validacoes_lista,'servPubl.mtvAlter', servPubl.mtvAlter.cdata, 1, u'1;2;3;8;9')

    return validacoes_lista