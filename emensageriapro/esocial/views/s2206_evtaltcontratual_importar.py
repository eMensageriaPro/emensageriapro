# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2206.models import *
from emensageriapro.functions import read_from_xml



def read_s2206_evtaltcontratual_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2206_evtaltcontratual_obj(request, doc, status, validar)
    return dados



def read_s2206_evtaltcontratual(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2206_evtaltcontratual_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2206evtAltContratual.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2206_evtaltcontratual_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2206_evtaltcontratual_dados = {}
    s2206_evtaltcontratual_dados['status'] = status
    s2206_evtaltcontratual_dados['arquivo_original'] = 1
    if arquivo:
        s2206_evtaltcontratual_dados['arquivo'] = arquivo.arquivo
    s2206_evtaltcontratual_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2206_evtaltcontratual_dados['identidade'] = doc.eSocial.evtAltContratual['Id']
    evtAltContratual = doc.eSocial.evtAltContratual

    try:
        s2206_evtaltcontratual_dados['indretif'] = read_from_xml(evtAltContratual.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['nrrecibo'] = read_from_xml(evtAltContratual.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['tpamb'] = read_from_xml(evtAltContratual.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['procemi'] = read_from_xml(evtAltContratual.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['verproc'] = read_from_xml(evtAltContratual.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['tpinsc'] = read_from_xml(evtAltContratual.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['nrinsc'] = read_from_xml(evtAltContratual.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['cpftrab'] = read_from_xml(evtAltContratual.ideVinculo.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['nistrab'] = read_from_xml(evtAltContratual.ideVinculo.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['matricula'] = read_from_xml(evtAltContratual.ideVinculo.matricula.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['dtalteracao'] = read_from_xml(evtAltContratual.altContratual.dtAlteracao.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['dtef'] = read_from_xml(evtAltContratual.altContratual.dtEf.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['dscalt'] = read_from_xml(evtAltContratual.altContratual.dscAlt.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['tpregprev'] = read_from_xml(evtAltContratual.altContratual.vinculo.tpRegPrev.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['codcargo'] = read_from_xml(evtAltContratual.altContratual.infoContrato.codCargo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['codfuncao'] = read_from_xml(evtAltContratual.altContratual.infoContrato.codFuncao.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['codcateg'] = read_from_xml(evtAltContratual.altContratual.infoContrato.codCateg.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['codcarreira'] = read_from_xml(evtAltContratual.altContratual.infoContrato.codCarreira.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['dtingrcarr'] = read_from_xml(evtAltContratual.altContratual.infoContrato.dtIngrCarr.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['vrsalfx'] = read_from_xml(evtAltContratual.altContratual.infoContrato.remuneracao.vrSalFx.cdata, 'esocial', 'N', 2)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['undsalfixo'] = read_from_xml(evtAltContratual.altContratual.infoContrato.remuneracao.undSalFixo.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['dscsalvar'] = read_from_xml(evtAltContratual.altContratual.infoContrato.remuneracao.dscSalVar.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['tpcontr'] = read_from_xml(evtAltContratual.altContratual.infoContrato.duracao.tpContr.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['dtterm'] = read_from_xml(evtAltContratual.altContratual.infoContrato.duracao.dtTerm.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2206_evtaltcontratual_dados['objdet'] = read_from_xml(evtAltContratual.altContratual.infoContrato.duracao.objDet.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s2206_evtaltcontratual = s2206evtAltContratual.objects.create(**s2206_evtaltcontratual_dados)

    if 'altContratual' in dir(evtAltContratual) and 'infoRegimeTrab' in dir(evtAltContratual.altContratual) and 'infoCeletista' in dir(evtAltContratual.altContratual.infoRegimeTrab):

        for infoCeletista in evtAltContratual.altContratual.infoRegimeTrab.infoCeletista:

            s2206_infoceletista_dados = {}
            s2206_infoceletista_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id

            try:
                s2206_infoceletista_dados['tpregjor'] = read_from_xml(infoCeletista.tpRegJor.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2206_infoceletista_dados['natatividade'] = read_from_xml(infoCeletista.natAtividade.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2206_infoceletista_dados['dtbase'] = read_from_xml(infoCeletista.dtBase.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2206_infoceletista_dados['cnpjsindcategprof'] = read_from_xml(infoCeletista.cnpjSindCategProf.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2206_infoceletista = s2206infoCeletista.objects.create(**s2206_infoceletista_dados)

            if 'trabTemp' in dir(infoCeletista):

                for trabTemp in infoCeletista.trabTemp:

                    s2206_trabtemp_dados = {}
                    s2206_trabtemp_dados['s2206_infoceletista_id'] = s2206_infoceletista.id

                    try:
                        s2206_trabtemp_dados['justprorr'] = read_from_xml(trabTemp.justProrr.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2206_trabtemp = s2206trabTemp.objects.create(**s2206_trabtemp_dados)

            if 'aprend' in dir(infoCeletista):

                for aprend in infoCeletista.aprend:

                    s2206_aprend_dados = {}
                    s2206_aprend_dados['s2206_infoceletista_id'] = s2206_infoceletista.id

                    try:
                        s2206_aprend_dados['tpinsc'] = read_from_xml(aprend.tpInsc.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2206_aprend_dados['nrinsc'] = read_from_xml(aprend.nrInsc.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2206_aprend = s2206aprend.objects.create(**s2206_aprend_dados)

    if 'altContratual' in dir(evtAltContratual) and 'infoRegimeTrab' in dir(evtAltContratual.altContratual) and 'infoEstatutario' in dir(evtAltContratual.altContratual.infoRegimeTrab):

        for infoEstatutario in evtAltContratual.altContratual.infoRegimeTrab.infoEstatutario:

            s2206_infoestatutario_dados = {}
            s2206_infoestatutario_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id

            try:
                s2206_infoestatutario_dados['tpplanrp'] = read_from_xml(infoEstatutario.tpPlanRP.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2206_infoestatutario_dados['indtetorgps'] = read_from_xml(infoEstatutario.indTetoRGPS.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2206_infoestatutario_dados['indabonoperm'] = read_from_xml(infoEstatutario.indAbonoPerm.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2206_infoestatutario_dados['indparcremun'] = read_from_xml(infoEstatutario.indParcRemun.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2206_infoestatutario = s2206infoEstatutario.objects.create(**s2206_infoestatutario_dados)

    if 'altContratual' in dir(evtAltContratual) and 'infoContrato' in dir(evtAltContratual.altContratual) and 'localTrabalho' in dir(evtAltContratual.altContratual.infoContrato) and 'localTrabGeral' in dir(evtAltContratual.altContratual.infoContrato.localTrabalho):

        for localTrabGeral in evtAltContratual.altContratual.infoContrato.localTrabalho.localTrabGeral:

            s2206_localtrabgeral_dados = {}
            s2206_localtrabgeral_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id

            try:
                s2206_localtrabgeral_dados['tpinsc'] = read_from_xml(localTrabGeral.tpInsc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2206_localtrabgeral_dados['nrinsc'] = read_from_xml(localTrabGeral.nrInsc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2206_localtrabgeral_dados['desccomp'] = read_from_xml(localTrabGeral.descComp.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2206_localtrabgeral = s2206localTrabGeral.objects.create(**s2206_localtrabgeral_dados)

    if 'altContratual' in dir(evtAltContratual) and 'infoContrato' in dir(evtAltContratual.altContratual) and 'localTrabalho' in dir(evtAltContratual.altContratual.infoContrato) and 'localTrabDom' in dir(evtAltContratual.altContratual.infoContrato.localTrabalho):

        for localTrabDom in evtAltContratual.altContratual.infoContrato.localTrabalho.localTrabDom:

            s2206_localtrabdom_dados = {}
            s2206_localtrabdom_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id

            try:
                s2206_localtrabdom_dados['tplograd'] = read_from_xml(localTrabDom.tpLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2206_localtrabdom_dados['dsclograd'] = read_from_xml(localTrabDom.dscLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2206_localtrabdom_dados['nrlograd'] = read_from_xml(localTrabDom.nrLograd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2206_localtrabdom_dados['complemento'] = read_from_xml(localTrabDom.complemento.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2206_localtrabdom_dados['bairro'] = read_from_xml(localTrabDom.bairro.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2206_localtrabdom_dados['cep'] = read_from_xml(localTrabDom.cep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2206_localtrabdom_dados['codmunic'] = read_from_xml(localTrabDom.codMunic.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2206_localtrabdom_dados['uf'] = read_from_xml(localTrabDom.uf.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2206_localtrabdom = s2206localTrabDom.objects.create(**s2206_localtrabdom_dados)

    if 'altContratual' in dir(evtAltContratual) and 'infoContrato' in dir(evtAltContratual.altContratual) and 'horContratual' in dir(evtAltContratual.altContratual.infoContrato):

        for horContratual in evtAltContratual.altContratual.infoContrato.horContratual:

            s2206_horcontratual_dados = {}
            s2206_horcontratual_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id

            try:
                s2206_horcontratual_dados['qtdhrssem'] = read_from_xml(horContratual.qtdHrsSem.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            try:
                s2206_horcontratual_dados['tpjornada'] = read_from_xml(horContratual.tpJornada.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2206_horcontratual_dados['dsctpjorn'] = read_from_xml(horContratual.dscTpJorn.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2206_horcontratual_dados['tmpparc'] = read_from_xml(horContratual.tmpParc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s2206_horcontratual = s2206horContratual.objects.create(**s2206_horcontratual_dados)

            if 'horario' in dir(horContratual):

                for horario in horContratual.horario:

                    s2206_horario_dados = {}
                    s2206_horario_dados['s2206_horcontratual_id'] = s2206_horcontratual.id

                    try:
                        s2206_horario_dados['dia'] = read_from_xml(horario.dia.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2206_horario_dados['codhorcontrat'] = read_from_xml(horario.codHorContrat.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2206_horario = s2206horario.objects.create(**s2206_horario_dados)

    if 'altContratual' in dir(evtAltContratual) and 'infoContrato' in dir(evtAltContratual.altContratual) and 'filiacaoSindical' in dir(evtAltContratual.altContratual.infoContrato):

        for filiacaoSindical in evtAltContratual.altContratual.infoContrato.filiacaoSindical:

            s2206_filiacaosindical_dados = {}
            s2206_filiacaosindical_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id

            try:
                s2206_filiacaosindical_dados['cnpjsindtrab'] = read_from_xml(filiacaoSindical.cnpjSindTrab.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2206_filiacaosindical = s2206filiacaoSindical.objects.create(**s2206_filiacaosindical_dados)

    if 'altContratual' in dir(evtAltContratual) and 'infoContrato' in dir(evtAltContratual.altContratual) and 'alvaraJudicial' in dir(evtAltContratual.altContratual.infoContrato):

        for alvaraJudicial in evtAltContratual.altContratual.infoContrato.alvaraJudicial:

            s2206_alvarajudicial_dados = {}
            s2206_alvarajudicial_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id

            try:
                s2206_alvarajudicial_dados['nrprocjud'] = read_from_xml(alvaraJudicial.nrProcJud.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2206_alvarajudicial = s2206alvaraJudicial.objects.create(**s2206_alvarajudicial_dados)

    if 'altContratual' in dir(evtAltContratual) and 'infoContrato' in dir(evtAltContratual.altContratual) and 'observacoes' in dir(evtAltContratual.altContratual.infoContrato):

        for observacoes in evtAltContratual.altContratual.infoContrato.observacoes:

            s2206_observacoes_dados = {}
            s2206_observacoes_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id

            try:
                s2206_observacoes_dados['observacao'] = read_from_xml(observacoes.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2206_observacoes = s2206observacoes.objects.create(**s2206_observacoes_dados)

    if 'altContratual' in dir(evtAltContratual) and 'infoContrato' in dir(evtAltContratual.altContratual) and 'servPubl' in dir(evtAltContratual.altContratual.infoContrato):

        for servPubl in evtAltContratual.altContratual.infoContrato.servPubl:

            s2206_servpubl_dados = {}
            s2206_servpubl_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual.id

            try:
                s2206_servpubl_dados['mtvalter'] = read_from_xml(servPubl.mtvAlter.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s2206_servpubl = s2206servPubl.objects.create(**s2206_servpubl_dados)
    s2206_evtaltcontratual_dados['evento'] = 's2206'
    s2206_evtaltcontratual_dados['id'] = s2206_evtaltcontratual.id
    s2206_evtaltcontratual_dados['identidade_evento'] = doc.eSocial.evtAltContratual['Id']

    from emensageriapro.esocial.views.s2206_evtaltcontratual_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2206_evtaltcontratual.id)

    return s2206_evtaltcontratual_dados