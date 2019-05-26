#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2206.models import *



def read_s2206_evtaltcontratual_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2206_evtaltcontratual_obj(doc, status, validar)
    return dados



def read_s2206_evtaltcontratual(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2206_evtaltcontratual_obj(doc, status, validar)
    return dados



def read_s2206_evtaltcontratual_obj(doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2206_evtaltcontratual_dados = {}
    s2206_evtaltcontratual_dados['status'] = status
    s2206_evtaltcontratual_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2206_evtaltcontratual_dados['identidade'] = doc.eSocial.evtAltContratual['Id']
    evtAltContratual = doc.eSocial.evtAltContratual
    
    try:
        s2206_evtaltcontratual_dados['indretif'] = evtAltContratual.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['nrrecibo'] = evtAltContratual.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['tpamb'] = evtAltContratual.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['procemi'] = evtAltContratual.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['verproc'] = evtAltContratual.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['tpinsc'] = evtAltContratual.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['nrinsc'] = evtAltContratual.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['cpftrab'] = evtAltContratual.ideVinculo.cpfTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['nistrab'] = evtAltContratual.ideVinculo.nisTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['matricula'] = evtAltContratual.ideVinculo.matricula.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['dtalteracao'] = evtAltContratual.altContratual.dtAlteracao.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['dtef'] = evtAltContratual.altContratual.dtEf.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['dscalt'] = evtAltContratual.altContratual.dscAlt.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['tpregprev'] = evtAltContratual.altContratual.vinculo.tpRegPrev.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['codcargo'] = evtAltContratual.altContratual.infoContrato.codCargo.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['codfuncao'] = evtAltContratual.altContratual.infoContrato.codFuncao.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['codcateg'] = evtAltContratual.altContratual.infoContrato.codCateg.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['codcarreira'] = evtAltContratual.altContratual.infoContrato.codCarreira.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['dtingrcarr'] = evtAltContratual.altContratual.infoContrato.dtIngrCarr.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['vrsalfx'] = evtAltContratual.altContratual.infoContrato.remuneracao.vrSalFx.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['undsalfixo'] = evtAltContratual.altContratual.infoContrato.remuneracao.undSalFixo.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['dscsalvar'] = evtAltContratual.altContratual.infoContrato.remuneracao.dscSalVar.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['tpcontr'] = evtAltContratual.altContratual.infoContrato.duracao.tpContr.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['dtterm'] = evtAltContratual.altContratual.infoContrato.duracao.dtTerm.cdata
    except AttributeError: 
        pass
    
    try:
        s2206_evtaltcontratual_dados['objdet'] = evtAltContratual.altContratual.infoContrato.duracao.objDet.cdata
    except AttributeError: 
        pass
        
    s2206_evtaltcontratual = s2206evtAltContratual.objects.create(**s2206_evtaltcontratual_dados)
    
    if 'infoCeletista' in dir(evtAltContratual.altContratual.infoRegimeTrab):
    
        for infoCeletista in evtAltContratual.altContratual.infoRegimeTrab.infoCeletista:
    
            s2206_infoceletista_dados = {}
            s2206_infoceletista_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id
            
            try:
                s2206_infoceletista_dados['tpregjor'] = infoCeletista.tpRegJor.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_infoceletista_dados['natatividade'] = infoCeletista.natAtividade.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_infoceletista_dados['dtbase'] = infoCeletista.dtBase.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_infoceletista_dados['cnpjsindcategprof'] = infoCeletista.cnpjSindCategProf.cdata
            except AttributeError: 
                pass
    
            s2206_infoceletista = s2206infoCeletista.objects.create(**s2206_infoceletista_dados)
            
            if 'trabTemp' in dir(infoCeletista):
            
                for trabTemp in infoCeletista.trabTemp:
            
                    s2206_trabtemp_dados = {}
                    s2206_trabtemp_dados['s2206_infoceletista_id'] = s2206_infoceletista.id
                    
                    try:
                        s2206_trabtemp_dados['justprorr'] = trabTemp.justProrr.cdata
                    except AttributeError: 
                        pass
            
                    s2206_trabtemp = s2206trabTemp.objects.create(**s2206_trabtemp_dados)
            
            if 'aprend' in dir(infoCeletista):
            
                for aprend in infoCeletista.aprend:
            
                    s2206_aprend_dados = {}
                    s2206_aprend_dados['s2206_infoceletista_id'] = s2206_infoceletista.id
                    
                    try:
                        s2206_aprend_dados['tpinsc'] = aprend.tpInsc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2206_aprend_dados['nrinsc'] = aprend.nrInsc.cdata
                    except AttributeError: 
                        pass
            
                    s2206_aprend = s2206aprend.objects.create(**s2206_aprend_dados)
    
    if 'infoEstatutario' in dir(evtAltContratual.altContratual.infoRegimeTrab):
    
        for infoEstatutario in evtAltContratual.altContratual.infoRegimeTrab.infoEstatutario:
    
            s2206_infoestatutario_dados = {}
            s2206_infoestatutario_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id
            
            try:
                s2206_infoestatutario_dados['tpplanrp'] = infoEstatutario.tpPlanRP.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_infoestatutario_dados['indtetorgps'] = infoEstatutario.indTetoRGPS.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_infoestatutario_dados['indabonoperm'] = infoEstatutario.indAbonoPerm.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_infoestatutario_dados['indparcremun'] = infoEstatutario.indParcRemun.cdata
            except AttributeError: 
                pass
    
            s2206_infoestatutario = s2206infoEstatutario.objects.create(**s2206_infoestatutario_dados)
    
    if 'localTrabGeral' in dir(evtAltContratual.altContratual.infoContrato.localTrabalho):
    
        for localTrabGeral in evtAltContratual.altContratual.infoContrato.localTrabalho.localTrabGeral:
    
            s2206_localtrabgeral_dados = {}
            s2206_localtrabgeral_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id
            
            try:
                s2206_localtrabgeral_dados['tpinsc'] = localTrabGeral.tpInsc.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_localtrabgeral_dados['nrinsc'] = localTrabGeral.nrInsc.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_localtrabgeral_dados['desccomp'] = localTrabGeral.descComp.cdata
            except AttributeError: 
                pass
    
            s2206_localtrabgeral = s2206localTrabGeral.objects.create(**s2206_localtrabgeral_dados)
    
    if 'localTrabDom' in dir(evtAltContratual.altContratual.infoContrato.localTrabalho):
    
        for localTrabDom in evtAltContratual.altContratual.infoContrato.localTrabalho.localTrabDom:
    
            s2206_localtrabdom_dados = {}
            s2206_localtrabdom_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id
            
            try:
                s2206_localtrabdom_dados['tplograd'] = localTrabDom.tpLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_localtrabdom_dados['dsclograd'] = localTrabDom.dscLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_localtrabdom_dados['nrlograd'] = localTrabDom.nrLograd.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_localtrabdom_dados['complemento'] = localTrabDom.complemento.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_localtrabdom_dados['bairro'] = localTrabDom.bairro.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_localtrabdom_dados['cep'] = localTrabDom.cep.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_localtrabdom_dados['codmunic'] = localTrabDom.codMunic.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_localtrabdom_dados['uf'] = localTrabDom.uf.cdata
            except AttributeError: 
                pass
    
            s2206_localtrabdom = s2206localTrabDom.objects.create(**s2206_localtrabdom_dados)
    
    if 'horContratual' in dir(evtAltContratual.altContratual.infoContrato):
    
        for horContratual in evtAltContratual.altContratual.infoContrato.horContratual:
    
            s2206_horcontratual_dados = {}
            s2206_horcontratual_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id
            
            try:
                s2206_horcontratual_dados['qtdhrssem'] = horContratual.qtdHrsSem.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_horcontratual_dados['tpjornada'] = horContratual.tpJornada.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_horcontratual_dados['dsctpjorn'] = horContratual.dscTpJorn.cdata
            except AttributeError: 
                pass
            
            try:
                s2206_horcontratual_dados['tmpparc'] = horContratual.tmpParc.cdata
            except AttributeError: 
                pass
    
            s2206_horcontratual = s2206horContratual.objects.create(**s2206_horcontratual_dados)
            
            if 'horario' in dir(horContratual):
            
                for horario in horContratual.horario:
            
                    s2206_horario_dados = {}
                    s2206_horario_dados['s2206_horcontratual_id'] = s2206_horcontratual.id
                    
                    try:
                        s2206_horario_dados['dia'] = horario.dia.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s2206_horario_dados['codhorcontrat'] = horario.codHorContrat.cdata
                    except AttributeError: 
                        pass
            
                    s2206_horario = s2206horario.objects.create(**s2206_horario_dados)
    
    if 'filiacaoSindical' in dir(evtAltContratual.altContratual.infoContrato):
    
        for filiacaoSindical in evtAltContratual.altContratual.infoContrato.filiacaoSindical:
    
            s2206_filiacaosindical_dados = {}
            s2206_filiacaosindical_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id
            
            try:
                s2206_filiacaosindical_dados['cnpjsindtrab'] = filiacaoSindical.cnpjSindTrab.cdata
            except AttributeError: 
                pass
    
            s2206_filiacaosindical = s2206filiacaoSindical.objects.create(**s2206_filiacaosindical_dados)
    
    if 'alvaraJudicial' in dir(evtAltContratual.altContratual.infoContrato):
    
        for alvaraJudicial in evtAltContratual.altContratual.infoContrato.alvaraJudicial:
    
            s2206_alvarajudicial_dados = {}
            s2206_alvarajudicial_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id
            
            try:
                s2206_alvarajudicial_dados['nrprocjud'] = alvaraJudicial.nrProcJud.cdata
            except AttributeError: 
                pass
    
            s2206_alvarajudicial = s2206alvaraJudicial.objects.create(**s2206_alvarajudicial_dados)
    
    if 'observacoes' in dir(evtAltContratual.altContratual.infoContrato):
    
        for observacoes in evtAltContratual.altContratual.infoContrato.observacoes:
    
            s2206_observacoes_dados = {}
            s2206_observacoes_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id
            
            try:
                s2206_observacoes_dados['observacao'] = observacoes.observacao.cdata
            except AttributeError: 
                pass
    
            s2206_observacoes = s2206observacoes.objects.create(**s2206_observacoes_dados)
    
    if 'servPubl' in dir(evtAltContratual.altContratual.infoContrato):
    
        for servPubl in evtAltContratual.altContratual.infoContrato.servPubl:
    
            s2206_servpubl_dados = {}
            s2206_servpubl_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id
            
            try:
                s2206_servpubl_dados['mtvalter'] = servPubl.mtvAlter.cdata
            except AttributeError: 
                pass
    
            s2206_servpubl = s2206servPubl.objects.create(**s2206_servpubl_dados)    
    s2206_evtaltcontratual_dados['evento'] = 's2206'
    s2206_evtaltcontratual_dados['id'] = s2206_evtaltcontratual.id
    s2206_evtaltcontratual_dados['identidade_evento'] = doc.eSocial.evtAltContratual['Id']
    s2206_evtaltcontratual_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s2206_evtaltcontratual_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(s2206_evtaltcontratual.id)
    return s2206_evtaltcontratual_dados