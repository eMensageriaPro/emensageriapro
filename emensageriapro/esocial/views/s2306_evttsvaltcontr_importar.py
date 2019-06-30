#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2306.models import *



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
        s2306_evttsvaltcontr_dados['indretif'] = evtTSVAltContr.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['nrrecibo'] = evtTSVAltContr.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['tpamb'] = evtTSVAltContr.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['procemi'] = evtTSVAltContr.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['verproc'] = evtTSVAltContr.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['tpinsc'] = evtTSVAltContr.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['nrinsc'] = evtTSVAltContr.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['cpftrab'] = evtTSVAltContr.ideTrabSemVinculo.cpfTrab.cdata
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['nistrab'] = evtTSVAltContr.ideTrabSemVinculo.nisTrab.cdata
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['codcateg'] = evtTSVAltContr.ideTrabSemVinculo.codCateg.cdata
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['dtalteracao'] = evtTSVAltContr.infoTSVAlteracao.dtAlteracao.cdata
    except AttributeError:
        pass

    try:
        s2306_evttsvaltcontr_dados['natatividade'] = evtTSVAltContr.infoTSVAlteracao.natAtividade.cdata
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
                        s2306_cargofuncao_dados['codcargo'] = cargoFuncao.codCargo.cdata
                    except AttributeError:
                        pass

                    try:
                        s2306_cargofuncao_dados['codfuncao'] = cargoFuncao.codFuncao.cdata
                    except AttributeError:
                        pass

                    s2306_cargofuncao = s2306cargoFuncao.objects.create(**s2306_cargofuncao_dados)

            if 'remuneracao' in dir(infoComplementares):

                for remuneracao in infoComplementares.remuneracao:

                    s2306_remuneracao_dados = {}
                    s2306_remuneracao_dados['s2306_infocomplementares_id'] = s2306_infocomplementares.id

                    try:
                        s2306_remuneracao_dados['vrsalfx'] = remuneracao.vrSalFx.cdata
                    except AttributeError:
                        pass

                    try:
                        s2306_remuneracao_dados['undsalfixo'] = remuneracao.undSalFixo.cdata
                    except AttributeError:
                        pass

                    try:
                        s2306_remuneracao_dados['dscsalvar'] = remuneracao.dscSalVar.cdata
                    except AttributeError:
                        pass

                    s2306_remuneracao = s2306remuneracao.objects.create(**s2306_remuneracao_dados)

            if 'infoTrabCedido' in dir(infoComplementares):

                for infoTrabCedido in infoComplementares.infoTrabCedido:

                    s2306_infotrabcedido_dados = {}
                    s2306_infotrabcedido_dados['s2306_infocomplementares_id'] = s2306_infocomplementares.id

                    try:
                        s2306_infotrabcedido_dados['indremuncargo'] = infoTrabCedido.indRemunCargo.cdata
                    except AttributeError:
                        pass

                    s2306_infotrabcedido = s2306infoTrabCedido.objects.create(**s2306_infotrabcedido_dados)

            if 'infoEstagiario' in dir(infoComplementares):

                for infoEstagiario in infoComplementares.infoEstagiario:

                    s2306_infoestagiario_dados = {}
                    s2306_infoestagiario_dados['s2306_infocomplementares_id'] = s2306_infocomplementares.id

                    try:
                        s2306_infoestagiario_dados['natestagio'] = infoEstagiario.natEstagio.cdata
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['nivestagio'] = infoEstagiario.nivEstagio.cdata
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['areaatuacao'] = infoEstagiario.areaAtuacao.cdata
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['nrapol'] = infoEstagiario.nrApol.cdata
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['vlrbolsa'] = infoEstagiario.vlrBolsa.cdata
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['dtprevterm'] = infoEstagiario.dtPrevTerm.cdata
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['cnpjinstensino'] = infoEstagiario.instEnsino.cnpjInstEnsino.cdata
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['nmrazao'] = infoEstagiario.instEnsino.nmRazao.cdata
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['dsclograd'] = infoEstagiario.instEnsino.dscLograd.cdata
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['nrlograd'] = infoEstagiario.instEnsino.nrLograd.cdata
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['bairro'] = infoEstagiario.instEnsino.bairro.cdata
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['cep'] = infoEstagiario.instEnsino.cep.cdata
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['codmunic'] = infoEstagiario.instEnsino.codMunic.cdata
                    except AttributeError:
                        pass

                    try:
                        s2306_infoestagiario_dados['uf'] = infoEstagiario.instEnsino.uf.cdata
                    except AttributeError:
                        pass

                    s2306_infoestagiario = s2306infoEstagiario.objects.create(**s2306_infoestagiario_dados)

                    if 'ageIntegracao' in dir(infoEstagiario):

                        for ageIntegracao in infoEstagiario.ageIntegracao:

                            s2306_ageintegracao_dados = {}
                            s2306_ageintegracao_dados['s2306_infoestagiario_id'] = s2306_infoestagiario.id
        
                            try:
                                s2306_ageintegracao_dados['cnpjagntinteg'] = ageIntegracao.cnpjAgntInteg.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2306_ageintegracao_dados['nmrazao'] = ageIntegracao.nmRazao.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2306_ageintegracao_dados['dsclograd'] = ageIntegracao.dscLograd.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2306_ageintegracao_dados['nrlograd'] = ageIntegracao.nrLograd.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2306_ageintegracao_dados['bairro'] = ageIntegracao.bairro.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2306_ageintegracao_dados['cep'] = ageIntegracao.cep.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2306_ageintegracao_dados['codmunic'] = ageIntegracao.codMunic.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2306_ageintegracao_dados['uf'] = ageIntegracao.uf.cdata
                            except AttributeError:
                                pass

                            s2306_ageintegracao = s2306ageIntegracao.objects.create(**s2306_ageintegracao_dados)

                    if 'supervisorEstagio' in dir(infoEstagiario):

                        for supervisorEstagio in infoEstagiario.supervisorEstagio:

                            s2306_supervisorestagio_dados = {}
                            s2306_supervisorestagio_dados['s2306_infoestagiario_id'] = s2306_infoestagiario.id
        
                            try:
                                s2306_supervisorestagio_dados['cpfsupervisor'] = supervisorEstagio.cpfSupervisor.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2306_supervisorestagio_dados['nmsuperv'] = supervisorEstagio.nmSuperv.cdata
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