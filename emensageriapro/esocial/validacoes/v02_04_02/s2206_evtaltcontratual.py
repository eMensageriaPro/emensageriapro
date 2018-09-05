#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s2206_evtaltcontratual(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtAltContratual = doc.eSocial.evtAltContratual
    
    if 'indRetif' in dir(evtAltContratual.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideEvento.indRetif', evtAltContratual.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtAltContratual.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideEvento.nrRecibo', evtAltContratual.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtAltContratual.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideEvento.tpAmb', evtAltContratual.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtAltContratual.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideEvento.procEmi', evtAltContratual.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtAltContratual.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideEvento.verProc', evtAltContratual.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtAltContratual.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideEmpregador.tpInsc', evtAltContratual.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtAltContratual.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideEmpregador.nrInsc', evtAltContratual.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtAltContratual.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideVinculo.cpfTrab', evtAltContratual.ideVinculo.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtAltContratual.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideVinculo.nisTrab', evtAltContratual.ideVinculo.nisTrab.cdata, 1, '')
    if 'matricula' in dir(evtAltContratual.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.ideVinculo.matricula', evtAltContratual.ideVinculo.matricula.cdata, 1, '')
    if 'dtAlteracao' in dir(evtAltContratual.altContratual): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.dtAlteracao', evtAltContratual.altContratual.dtAlteracao.cdata, 1, '')
    if 'dtEf' in dir(evtAltContratual.altContratual): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.dtEf', evtAltContratual.altContratual.dtEf.cdata, 0, '')
    if 'dscAlt' in dir(evtAltContratual.altContratual): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.dscAlt', evtAltContratual.altContratual.dscAlt.cdata, 0, '')
    if 'tpRegPrev' in dir(evtAltContratual.altContratual.vinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.vinculo.tpRegPrev', evtAltContratual.altContratual.vinculo.tpRegPrev.cdata, 1, '1;2;3')
    if 'codCargo' in dir(evtAltContratual.altContratual.infoContrato): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.codCargo', evtAltContratual.altContratual.infoContrato.codCargo.cdata, 0, '')
    if 'codFuncao' in dir(evtAltContratual.altContratual.infoContrato): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.codFuncao', evtAltContratual.altContratual.infoContrato.codFuncao.cdata, 0, '')
    if 'codCateg' in dir(evtAltContratual.altContratual.infoContrato): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.codCateg', evtAltContratual.altContratual.infoContrato.codCateg.cdata, 1, '')
    if 'codCarreira' in dir(evtAltContratual.altContratual.infoContrato): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.codCarreira', evtAltContratual.altContratual.infoContrato.codCarreira.cdata, 0, '')
    if 'dtIngrCarr' in dir(evtAltContratual.altContratual.infoContrato): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.dtIngrCarr', evtAltContratual.altContratual.infoContrato.dtIngrCarr.cdata, 0, '')
    if 'vrSalFx' in dir(evtAltContratual.altContratual.infoContrato.remuneracao): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.remuneracao.vrSalFx', evtAltContratual.altContratual.infoContrato.remuneracao.vrSalFx.cdata, 1, '')
    if 'undSalFixo' in dir(evtAltContratual.altContratual.infoContrato.remuneracao): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.remuneracao.undSalFixo', evtAltContratual.altContratual.infoContrato.remuneracao.undSalFixo.cdata, 1, '1;2;3;4;5;6;7')
    if 'dscSalVar' in dir(evtAltContratual.altContratual.infoContrato.remuneracao): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.remuneracao.dscSalVar', evtAltContratual.altContratual.infoContrato.remuneracao.dscSalVar.cdata, 0, '')
    if 'tpContr' in dir(evtAltContratual.altContratual.infoContrato.duracao): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.duracao.tpContr', evtAltContratual.altContratual.infoContrato.duracao.tpContr.cdata, 1, '1;2')
    if 'dtTerm' in dir(evtAltContratual.altContratual.infoContrato.duracao): validacoes_lista = validar_campo(validacoes_lista,'evtAltContratual.altContratual.infoContrato.duracao.dtTerm', evtAltContratual.altContratual.infoContrato.duracao.dtTerm.cdata, 0, '')
    if 'infoCeletista' in dir(evtAltContratual.altContratual.infoRegimeTrab):
        for infoCeletista in evtAltContratual.altContratual.infoRegimeTrab.infoCeletista:
            
            if 'tpRegJor' in dir(infoCeletista): validacoes_lista = validar_campo(validacoes_lista,'infoCeletista.tpRegJor', infoCeletista.tpRegJor.cdata, 1, '1;2;3;4')
            if 'natAtividade' in dir(infoCeletista): validacoes_lista = validar_campo(validacoes_lista,'infoCeletista.natAtividade', infoCeletista.natAtividade.cdata, 1, '1;2')
            if 'dtBase' in dir(infoCeletista): validacoes_lista = validar_campo(validacoes_lista,'infoCeletista.dtBase', infoCeletista.dtBase.cdata, 0, '')
            if 'cnpjSindCategProf' in dir(infoCeletista): validacoes_lista = validar_campo(validacoes_lista,'infoCeletista.cnpjSindCategProf', infoCeletista.cnpjSindCategProf.cdata, 1, '')

            if 'trabTemp' in dir(infoCeletista):
                for trabTemp in infoCeletista.trabTemp:
                    
                    if 'justProrr' in dir(trabTemp): validacoes_lista = validar_campo(validacoes_lista,'trabTemp.justProrr', trabTemp.justProrr.cdata, 1, '')
        
            if 'aprend' in dir(infoCeletista):
                for aprend in infoCeletista.aprend:
                    
                    if 'tpInsc' in dir(aprend): validacoes_lista = validar_campo(validacoes_lista,'aprend.tpInsc', aprend.tpInsc.cdata, 1, '1;2;3;4')
                    if 'nrInsc' in dir(aprend): validacoes_lista = validar_campo(validacoes_lista,'aprend.nrInsc', aprend.nrInsc.cdata, 1, '')
        
    if 'infoEstatutario' in dir(evtAltContratual.altContratual.infoRegimeTrab):
        for infoEstatutario in evtAltContratual.altContratual.infoRegimeTrab.infoEstatutario:
            
            if 'tpPlanRP' in dir(infoEstatutario): validacoes_lista = validar_campo(validacoes_lista,'infoEstatutario.tpPlanRP', infoEstatutario.tpPlanRP.cdata, 1, '1;2')

    if 'localTrabGeral' in dir(evtAltContratual.altContratual.infoContrato.localTrabalho):
        for localTrabGeral in evtAltContratual.altContratual.infoContrato.localTrabalho.localTrabGeral:
            
            if 'tpInsc' in dir(localTrabGeral): validacoes_lista = validar_campo(validacoes_lista,'localTrabGeral.tpInsc', localTrabGeral.tpInsc.cdata, 1, '1;2;3;4')
            if 'nrInsc' in dir(localTrabGeral): validacoes_lista = validar_campo(validacoes_lista,'localTrabGeral.nrInsc', localTrabGeral.nrInsc.cdata, 1, '')
            if 'descComp' in dir(localTrabGeral): validacoes_lista = validar_campo(validacoes_lista,'localTrabGeral.descComp', localTrabGeral.descComp.cdata, 0, '')

    if 'localTrabDom' in dir(evtAltContratual.altContratual.infoContrato.localTrabalho):
        for localTrabDom in evtAltContratual.altContratual.infoContrato.localTrabalho.localTrabDom:
            
            if 'tpLograd' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.tpLograd', localTrabDom.tpLograd.cdata, 1, 'A;AC;ACA;ACL;AD;AE;AER;AL;AMD;AME;AN;ANT;ART;AT;ATL;A V;AV;AVC;AVM;AVV;BAL;BC;BCO;BEL;BL;BLO;BLS;BLV;BSQ;BVD;BX;C;CAL;CAM;CAN;CH;CHA;CIC;CIR;CJ;CJM;CMP;COL;COM;CON;COR;CPO;CRG;CTN;DSC;DSV;DT;EB;EIM;ENS;ENT;EQ;ESC;ESD;ESE;ESI;ESL;ESM;ESP;ESS;EST;ESV;ETA;ETC;ETD;ETN;ETP;ETT;EVA;EVD;EX;FAV;FAZ;FER;FNT;FRA;FTE;GAL;GJA;HAB;IA;IND;IOA;JD;JDE;LD;LGA;LGO;LOT;LRG;LT;MER;MNA;MOD;MRG;MRO;MTE;NUC;NUR;OUT;PAR;PAS;PAT;PC;PCE;PDA;PDO;PNT;PR;PRL;PRM;PRQ;PRR;PSA;PSG;PSP;PSS;PTE;PTO;Q;QTA;QTS;R;R I;R L;R P;R V;RAM;RCR;REC;RER;RES;RET;RLA;RMP;ROA;ROD;ROT;RPE;RPR;RTN;RTT;SEG;SIT;SRV;ST;SUB;TCH;TER;TR;TRV;TUN;TV;TVP;TVV;UNI;V;V C;V L;VAC;VAL;VCO;VD;V-E;VER;VEV;VL;VLA;VLE;VLT;VPE;VRT;ZIG')
            if 'dscLograd' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.dscLograd', localTrabDom.dscLograd.cdata, 1, '')
            if 'nrLograd' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.nrLograd', localTrabDom.nrLograd.cdata, 1, '')
            if 'complemento' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.complemento', localTrabDom.complemento.cdata, 0, '')
            if 'bairro' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.bairro', localTrabDom.bairro.cdata, 0, '')
            if 'cep' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.cep', localTrabDom.cep.cdata, 1, '')
            if 'codMunic' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.codMunic', localTrabDom.codMunic.cdata, 1, '')
            if 'uf' in dir(localTrabDom): validacoes_lista = validar_campo(validacoes_lista,'localTrabDom.uf', localTrabDom.uf.cdata, 1, '')

    if 'horContratual' in dir(evtAltContratual.altContratual.infoContrato):
        for horContratual in evtAltContratual.altContratual.infoContrato.horContratual:
            
            if 'qtdHrsSem' in dir(horContratual): validacoes_lista = validar_campo(validacoes_lista,'horContratual.qtdHrsSem', horContratual.qtdHrsSem.cdata, 0, '')
            if 'tpJornada' in dir(horContratual): validacoes_lista = validar_campo(validacoes_lista,'horContratual.tpJornada', horContratual.tpJornada.cdata, 1, '1;2;3;9')
            if 'dscTpJorn' in dir(horContratual): validacoes_lista = validar_campo(validacoes_lista,'horContratual.dscTpJorn', horContratual.dscTpJorn.cdata, 0, '')
            if 'tmpParc' in dir(horContratual): validacoes_lista = validar_campo(validacoes_lista,'horContratual.tmpParc', horContratual.tmpParc.cdata, 1, '0;1;2;3')

            if 'horario' in dir(horContratual):
                for horario in horContratual.horario:
                    
                    if 'dia' in dir(horario): validacoes_lista = validar_campo(validacoes_lista,'horario.dia', horario.dia.cdata, 1, '1;2;3;4;5;6;7;8')
                    if 'codHorContrat' in dir(horario): validacoes_lista = validar_campo(validacoes_lista,'horario.codHorContrat', horario.codHorContrat.cdata, 1, '')
        
    if 'filiacaoSindical' in dir(evtAltContratual.altContratual.infoContrato):
        for filiacaoSindical in evtAltContratual.altContratual.infoContrato.filiacaoSindical:
            
            if 'cnpjSindTrab' in dir(filiacaoSindical): validacoes_lista = validar_campo(validacoes_lista,'filiacaoSindical.cnpjSindTrab', filiacaoSindical.cnpjSindTrab.cdata, 1, '')

    if 'alvaraJudicial' in dir(evtAltContratual.altContratual.infoContrato):
        for alvaraJudicial in evtAltContratual.altContratual.infoContrato.alvaraJudicial:
            
            if 'nrProcJud' in dir(alvaraJudicial): validacoes_lista = validar_campo(validacoes_lista,'alvaraJudicial.nrProcJud', alvaraJudicial.nrProcJud.cdata, 1, '')

    if 'observacoes' in dir(evtAltContratual.altContratual.infoContrato):
        for observacoes in evtAltContratual.altContratual.infoContrato.observacoes:
            
            if 'observacao' in dir(observacoes): validacoes_lista = validar_campo(validacoes_lista,'observacoes.observacao', observacoes.observacao.cdata, 1, '')

    if 'servPubl' in dir(evtAltContratual.altContratual.infoContrato):
        for servPubl in evtAltContratual.altContratual.infoContrato.servPubl:
            
            if 'mtvAlter' in dir(servPubl): validacoes_lista = validar_campo(validacoes_lista,'servPubl.mtvAlter', servPubl.mtvAlter.cdata, 1, '1;2;3;8;9')

    return validacoes_lista