# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2306.models import *
from emensageriapro.functions import read_from_xml



def read_s2306_evttsvaltcontr_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2306_evttsvaltcontr_obj(request, doc, status, validar)
    return dados



def read_s2306_evttsvaltcontr(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2306_evttsvaltcontr_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2306evtTSVAltContr.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2306_evttsvaltcontr_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2306_evttsvaltcontr_dados = {}
    s2306_evttsvaltcontr_dados['status'] = status
    s2306_evttsvaltcontr_dados['arquivo_original'] = 1
    if arquivo:
        s2306_evttsvaltcontr_dados['arquivo'] = arquivo.arquivo
    s2306_evttsvaltcontr_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2306_evttsvaltcontr_dados['identidade'] = doc.eSocial.evtTSVAltContr['Id']
    evtTSVAltContr = doc.eSocial.evtTSVAltContr

    try:
        s2306_evttsvaltcontr_dados['indretif'] = read_from_xml(evtTSVAltContr.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['nrrecibo'] = read_from_xml(evtTSVAltContr.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['tpamb'] = read_from_xml(evtTSVAltContr.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['procemi'] = read_from_xml(evtTSVAltContr.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['verproc'] = read_from_xml(evtTSVAltContr.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['tpinsc'] = read_from_xml(evtTSVAltContr.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['nrinsc'] = read_from_xml(evtTSVAltContr.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['cpftrab'] = read_from_xml(evtTSVAltContr.ideTrabSemVinculo.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['nistrab'] = read_from_xml(evtTSVAltContr.ideTrabSemVinculo.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['codcateg'] = read_from_xml(evtTSVAltContr.ideTrabSemVinculo.codCateg.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['dtalteracao'] = read_from_xml(evtTSVAltContr.infoTSVAlteracao.dtAlteracao.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['natatividade'] = read_from_xml(evtTSVAltContr.infoTSVAlteracao.natAtividade.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    s2306_evttsvaltcontr = s2306evtTSVAltContr.objects.create(**s2306_evttsvaltcontr_dados)

    if 'infoTSVAlteracao' in dir(evtTSVAltContr) and 'infoComplementares' in dir(evtTSVAltContr.infoTSVAlteracao):

        for infoComplementares in evtTSVAltContr.infoTSVAlteracao.infoComplementares:

            s2306_infocomplementares_dados = {}
            s2306_infocomplementares_dados['s2306_evttsvaltcontr_id'] = s2306_evttsvaltcontr.id

            s2306_infocomplementares = s2306infoComplementares.objects.create(**s2306_infocomplementares_dados)

            if 'cargoFuncao' in dir(infoComplementares):

                for cargoFuncao in infoComplementares.cargoFuncao:

                    s2306_cargofuncao_dados = {}
                    s2306_cargofuncao_dados['s2306_infocomplementares_id'] = s2306_infocomplementares.id

                    try:
                        s2306_cargofuncao_dados['codcargo'] = read_from_xml(cargoFuncao.codCargo.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2306_cargofuncao_dados['codfuncao'] = read_from_xml(cargoFuncao.codFuncao.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2306_cargofuncao = s2306cargoFuncao.objects.create(**s2306_cargofuncao_dados)

            if 'remuneracao' in dir(infoComplementares):

                for remuneracao in infoComplementares.remuneracao:

                    s2306_remuneracao_dados = {}
                    s2306_remuneracao_dados['s2306_infocomplementares_id'] = s2306_infocomplementares.id

                    try:
                        s2306_remuneracao_dados['vrsalfx'] = read_from_xml(remuneracao.vrSalFx.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s2306_remuneracao_dados['undsalfixo'] = read_from_xml(remuneracao.undSalFixo.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2306_remuneracao_dados['dscsalvar'] = read_from_xml(remuneracao.dscSalVar.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2306_remuneracao = s2306remuneracao.objects.create(**s2306_remuneracao_dados)

            if 'infoTrabCedido' in dir(infoComplementares):

                for infoTrabCedido in infoComplementares.infoTrabCedido:

                    s2306_infotrabcedido_dados = {}
                    s2306_infotrabcedido_dados['s2306_infocomplementares_id'] = s2306_infocomplementares.id

                    try:
                        s2306_infotrabcedido_dados['indremuncargo'] = read_from_xml(infoTrabCedido.indRemunCargo.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2306_infotrabcedido = s2306infoTrabCedido.objects.create(**s2306_infotrabcedido_dados)

            if 'infoEstagiario' in dir(infoComplementares):

                for infoEstagiario in infoComplementares.infoEstagiario:

                    s2306_infoestagiario_dados = {}
                    s2306_infoestagiario_dados['s2306_infocomplementares_id'] = s2306_infocomplementares.id

                    try:
                        s2306_infoestagiario_dados['natestagio'] = read_from_xml(infoEstagiario.natEstagio.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['nivestagio'] = read_from_xml(infoEstagiario.nivEstagio.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['areaatuacao'] = read_from_xml(infoEstagiario.areaAtuacao.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['nrapol'] = read_from_xml(infoEstagiario.nrApol.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['vlrbolsa'] = read_from_xml(infoEstagiario.vlrBolsa.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['dtprevterm'] = read_from_xml(infoEstagiario.dtPrevTerm.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['cnpjinstensino'] = read_from_xml(infoEstagiario.instEnsino.cnpjInstEnsino.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['nmrazao'] = read_from_xml(infoEstagiario.instEnsino.nmRazao.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['dsclograd'] = read_from_xml(infoEstagiario.instEnsino.dscLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['nrlograd'] = read_from_xml(infoEstagiario.instEnsino.nrLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['bairro'] = read_from_xml(infoEstagiario.instEnsino.bairro.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['cep'] = read_from_xml(infoEstagiario.instEnsino.cep.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['codmunic'] = read_from_xml(infoEstagiario.instEnsino.codMunic.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['uf'] = read_from_xml(infoEstagiario.instEnsino.uf.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2306_infoestagiario = s2306infoEstagiario.objects.create(**s2306_infoestagiario_dados)

                    if 'ageIntegracao' in dir(infoEstagiario):

                        for ageIntegracao in infoEstagiario.ageIntegracao:

                            s2306_ageintegracao_dados = {}
                            s2306_ageintegracao_dados['s2306_infoestagiario_id'] = s2306_infoestagiario.id
        
                            try:
                                s2306_ageintegracao_dados['cnpjagntinteg'] = read_from_xml(ageIntegracao.cnpjAgntInteg.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2306_ageintegracao_dados['nmrazao'] = read_from_xml(ageIntegracao.nmRazao.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2306_ageintegracao_dados['dsclograd'] = read_from_xml(ageIntegracao.dscLograd.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2306_ageintegracao_dados['nrlograd'] = read_from_xml(ageIntegracao.nrLograd.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2306_ageintegracao_dados['bairro'] = read_from_xml(ageIntegracao.bairro.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2306_ageintegracao_dados['cep'] = read_from_xml(ageIntegracao.cep.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2306_ageintegracao_dados['codmunic'] = read_from_xml(ageIntegracao.codMunic.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2306_ageintegracao_dados['uf'] = read_from_xml(ageIntegracao.uf.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s2306_ageintegracao = s2306ageIntegracao.objects.create(**s2306_ageintegracao_dados)

                    if 'supervisorEstagio' in dir(infoEstagiario):

                        for supervisorEstagio in infoEstagiario.supervisorEstagio:

                            s2306_supervisorestagio_dados = {}
                            s2306_supervisorestagio_dados['s2306_infoestagiario_id'] = s2306_infoestagiario.id
        
                            try:
                                s2306_supervisorestagio_dados['cpfsupervisor'] = read_from_xml(supervisorEstagio.cpfSupervisor.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2306_supervisorestagio_dados['nmsuperv'] = read_from_xml(supervisorEstagio.nmSuperv.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s2306_supervisorestagio = s2306supervisorEstagio.objects.create(**s2306_supervisorestagio_dados)
    s2306_evttsvaltcontr_dados['evento'] = 's2306'
    s2306_evttsvaltcontr_dados['id'] = s2306_evttsvaltcontr.id
    s2306_evttsvaltcontr_dados['identidade_evento'] = doc.eSocial.evtTSVAltContr['Id']

    from emensageriapro.esocial.views.s2306_evttsvaltcontr_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2306_evttsvaltcontr.id)

    return s2306_evttsvaltcontr_dados