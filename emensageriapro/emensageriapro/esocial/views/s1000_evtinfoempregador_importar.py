#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1000.models import *
from emensageriapro.functions import read_from_xml



def read_s1000_evtinfoempregador_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1000_evtinfoempregador_obj(request, doc, status, validar)
    return dados



def read_s1000_evtinfoempregador(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1000_evtinfoempregador_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1000evtInfoEmpregador.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1000_evtinfoempregador_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1000_evtinfoempregador_dados = {}
    s1000_evtinfoempregador_dados['status'] = status
    s1000_evtinfoempregador_dados['arquivo_original'] = 1
    if arquivo:
        s1000_evtinfoempregador_dados['arquivo'] = arquivo.arquivo
    s1000_evtinfoempregador_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1000_evtinfoempregador_dados['identidade'] = doc.eSocial.evtInfoEmpregador['Id']
    evtInfoEmpregador = doc.eSocial.evtInfoEmpregador

    if 'inclusao' in dir(evtInfoEmpregador.infoEmpregador): s1000_evtinfoempregador_dados['operacao'] = 1
    elif 'alteracao' in dir(evtInfoEmpregador.infoEmpregador): s1000_evtinfoempregador_dados['operacao'] = 2
    elif 'exclusao' in dir(evtInfoEmpregador.infoEmpregador): s1000_evtinfoempregador_dados['operacao'] = 3

    try:
        s1000_evtinfoempregador_dados['tpamb'] = read_from_xml(evtInfoEmpregador.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1000_evtinfoempregador_dados['procemi'] = read_from_xml(evtInfoEmpregador.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1000_evtinfoempregador_dados['verproc'] = read_from_xml(evtInfoEmpregador.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1000_evtinfoempregador_dados['tpinsc'] = read_from_xml(evtInfoEmpregador.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1000_evtinfoempregador_dados['nrinsc'] = read_from_xml(evtInfoEmpregador.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1000_evtinfoempregador = s1000evtInfoEmpregador.objects.create(**s1000_evtinfoempregador_dados)

    if 'infoEmpregador' in dir(evtInfoEmpregador) and 'inclusao' in dir(evtInfoEmpregador.infoEmpregador):

        for inclusao in evtInfoEmpregador.infoEmpregador.inclusao:

            s1000_inclusao_dados = {}
            s1000_inclusao_dados['s1000_evtinfoempregador_id'] = s1000_evtinfoempregador.id

            try:
                s1000_inclusao_dados['inivalid'] = read_from_xml(inclusao.idePeriodo.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['fimvalid'] = read_from_xml(inclusao.idePeriodo.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['nmrazao'] = read_from_xml(inclusao.infoCadastro.nmRazao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['classtrib'] = read_from_xml(inclusao.infoCadastro.classTrib.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['natjurid'] = read_from_xml(inclusao.infoCadastro.natJurid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['indcoop'] = read_from_xml(inclusao.infoCadastro.indCoop.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['indconstr'] = read_from_xml(inclusao.infoCadastro.indConstr.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['inddesfolha'] = read_from_xml(inclusao.infoCadastro.indDesFolha.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['indopccp'] = read_from_xml(inclusao.infoCadastro.indOpcCP.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['indporte'] = read_from_xml(inclusao.infoCadastro.indPorte.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['indoptregeletron'] = read_from_xml(inclusao.infoCadastro.indOptRegEletron.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['indented'] = read_from_xml(inclusao.infoCadastro.indEntEd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['indett'] = read_from_xml(inclusao.infoCadastro.indEtt.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['nrregett'] = read_from_xml(inclusao.infoCadastro.nrRegEtt.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['nmctt'] = read_from_xml(inclusao.infoCadastro.contato.nmCtt.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['cpfctt'] = read_from_xml(inclusao.infoCadastro.contato.cpfCtt.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['fonefixo'] = read_from_xml(inclusao.infoCadastro.contato.foneFixo.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['fonecel'] = read_from_xml(inclusao.infoCadastro.contato.foneCel.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['email'] = read_from_xml(inclusao.infoCadastro.contato.email.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1000_inclusao = s1000inclusao.objects.create(**s1000_inclusao_dados)

            if 'infoCadastro' in dir(inclusao) and 'dadosIsencao' in dir(inclusao.infoCadastro):

                for dadosIsencao in inclusao.infoCadastro.dadosIsencao:

                    s1000_inclusao_dadosisencao_dados = {}
                    s1000_inclusao_dadosisencao_dados['s1000_inclusao_id'] = s1000_inclusao.id

                    try:
                        s1000_inclusao_dadosisencao_dados['ideminlei'] = read_from_xml(dadosIsencao.ideMinLei.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_dadosisencao_dados['nrcertif'] = read_from_xml(dadosIsencao.nrCertif.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_dadosisencao_dados['dtemiscertif'] = read_from_xml(dadosIsencao.dtEmisCertif.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_dadosisencao_dados['dtvenccertif'] = read_from_xml(dadosIsencao.dtVencCertif.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_dadosisencao_dados['nrprotrenov'] = read_from_xml(dadosIsencao.nrProtRenov.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_dadosisencao_dados['dtprotrenov'] = read_from_xml(dadosIsencao.dtProtRenov.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_dadosisencao_dados['dtdou'] = read_from_xml(dadosIsencao.dtDou.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_dadosisencao_dados['pagdou'] = read_from_xml(dadosIsencao.pagDou.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1000_inclusao_dadosisencao = s1000inclusaodadosIsencao.objects.create(**s1000_inclusao_dadosisencao_dados)

            if 'infoCadastro' in dir(inclusao) and 'infoOP' in dir(inclusao.infoCadastro):

                for infoOP in inclusao.infoCadastro.infoOP:

                    s1000_inclusao_infoop_dados = {}
                    s1000_inclusao_infoop_dados['s1000_inclusao_id'] = s1000_inclusao.id

                    try:
                        s1000_inclusao_infoop_dados['nrsiafi'] = read_from_xml(infoOP.nrSiafi.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_infoop_dados['indugrpps'] = read_from_xml(infoOP.indUGRPPS.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_infoop_dados['esferaop'] = read_from_xml(infoOP.esferaOP.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_infoop_dados['poderop'] = read_from_xml(infoOP.poderOP.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_infoop_dados['vrtetorem'] = read_from_xml(infoOP.vrTetoRem.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_infoop_dados['ideefr'] = read_from_xml(infoOP.ideEFR.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_infoop_dados['cnpjefr'] = read_from_xml(infoOP.cnpjEFR.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1000_inclusao_infoop = s1000inclusaoinfoOP.objects.create(**s1000_inclusao_infoop_dados)

                    if 'infoEFR' in dir(infoOP):

                        for infoEFR in infoOP.infoEFR:

                            s1000_inclusao_infoefr_dados = {}
                            s1000_inclusao_infoefr_dados['s1000_inclusao_infoop_id'] = s1000_inclusao_infoop.id
        
                            try:
                                s1000_inclusao_infoefr_dados['ideefr'] = read_from_xml(infoEFR.ideEFR.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1000_inclusao_infoefr_dados['cnpjefr'] = read_from_xml(infoEFR.cnpjEFR.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1000_inclusao_infoefr_dados['indrpps'] = read_from_xml(infoEFR.indRPPS.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1000_inclusao_infoefr_dados['prevcomp'] = read_from_xml(infoEFR.prevComp.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s1000_inclusao_infoefr = s1000inclusaoinfoEFR.objects.create(**s1000_inclusao_infoefr_dados)

                    if 'infoEnte' in dir(infoOP):

                        for infoEnte in infoOP.infoEnte:

                            s1000_inclusao_infoente_dados = {}
                            s1000_inclusao_infoente_dados['s1000_inclusao_infoop_id'] = s1000_inclusao_infoop.id
        
                            try:
                                s1000_inclusao_infoente_dados['nmente'] = read_from_xml(infoEnte.nmEnte.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1000_inclusao_infoente_dados['uf'] = read_from_xml(infoEnte.uf.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1000_inclusao_infoente_dados['codmunic'] = read_from_xml(infoEnte.codMunic.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1000_inclusao_infoente_dados['indrpps'] = read_from_xml(infoEnte.indRPPS.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1000_inclusao_infoente_dados['subteto'] = read_from_xml(infoEnte.subteto.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1000_inclusao_infoente_dados['vrsubteto'] = read_from_xml(infoEnte.vrSubteto.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s1000_inclusao_infoente = s1000inclusaoinfoEnte.objects.create(**s1000_inclusao_infoente_dados)

            if 'infoCadastro' in dir(inclusao) and 'infoOrgInternacional' in dir(inclusao.infoCadastro):

                for infoOrgInternacional in inclusao.infoCadastro.infoOrgInternacional:

                    s1000_inclusao_infoorginternacional_dados = {}
                    s1000_inclusao_infoorginternacional_dados['s1000_inclusao_id'] = s1000_inclusao.id

                    try:
                        s1000_inclusao_infoorginternacional_dados['indacordoisenmulta'] = read_from_xml(infoOrgInternacional.indAcordoIsenMulta.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1000_inclusao_infoorginternacional = s1000inclusaoinfoOrgInternacional.objects.create(**s1000_inclusao_infoorginternacional_dados)

            if 'infoCadastro' in dir(inclusao) and 'softwareHouse' in dir(inclusao.infoCadastro):

                for softwareHouse in inclusao.infoCadastro.softwareHouse:

                    s1000_inclusao_softwarehouse_dados = {}
                    s1000_inclusao_softwarehouse_dados['s1000_inclusao_id'] = s1000_inclusao.id

                    try:
                        s1000_inclusao_softwarehouse_dados['cnpjsofthouse'] = read_from_xml(softwareHouse.cnpjSoftHouse.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_softwarehouse_dados['nmrazao'] = read_from_xml(softwareHouse.nmRazao.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_softwarehouse_dados['nmcont'] = read_from_xml(softwareHouse.nmCont.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_softwarehouse_dados['telefone'] = read_from_xml(softwareHouse.telefone.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_softwarehouse_dados['email'] = read_from_xml(softwareHouse.email.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1000_inclusao_softwarehouse = s1000inclusaosoftwareHouse.objects.create(**s1000_inclusao_softwarehouse_dados)

            if 'infoCadastro' in dir(inclusao) and 'infoComplementares' in dir(inclusao.infoCadastro) and 'situacaoPJ' in dir(inclusao.infoCadastro.infoComplementares):

                for situacaoPJ in inclusao.infoCadastro.infoComplementares.situacaoPJ:

                    s1000_inclusao_situacaopj_dados = {}
                    s1000_inclusao_situacaopj_dados['s1000_inclusao_id'] = s1000_inclusao.id

                    try:
                        s1000_inclusao_situacaopj_dados['indsitpj'] = read_from_xml(situacaoPJ.indSitPJ.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1000_inclusao_situacaopj = s1000inclusaosituacaoPJ.objects.create(**s1000_inclusao_situacaopj_dados)

            if 'infoCadastro' in dir(inclusao) and 'infoComplementares' in dir(inclusao.infoCadastro) and 'situacaoPF' in dir(inclusao.infoCadastro.infoComplementares):

                for situacaoPF in inclusao.infoCadastro.infoComplementares.situacaoPF:

                    s1000_inclusao_situacaopf_dados = {}
                    s1000_inclusao_situacaopf_dados['s1000_inclusao_id'] = s1000_inclusao.id

                    try:
                        s1000_inclusao_situacaopf_dados['indsitpf'] = read_from_xml(situacaoPF.indSitPF.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1000_inclusao_situacaopf = s1000inclusaosituacaoPF.objects.create(**s1000_inclusao_situacaopf_dados)

    if 'infoEmpregador' in dir(evtInfoEmpregador) and 'alteracao' in dir(evtInfoEmpregador.infoEmpregador):

        for alteracao in evtInfoEmpregador.infoEmpregador.alteracao:

            s1000_alteracao_dados = {}
            s1000_alteracao_dados['s1000_evtinfoempregador_id'] = s1000_evtinfoempregador.id

            try:
                s1000_alteracao_dados['inivalid'] = read_from_xml(alteracao.idePeriodo.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['fimvalid'] = read_from_xml(alteracao.idePeriodo.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['nmrazao'] = read_from_xml(alteracao.infoCadastro.nmRazao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['classtrib'] = read_from_xml(alteracao.infoCadastro.classTrib.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['natjurid'] = read_from_xml(alteracao.infoCadastro.natJurid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['indcoop'] = read_from_xml(alteracao.infoCadastro.indCoop.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['indconstr'] = read_from_xml(alteracao.infoCadastro.indConstr.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['inddesfolha'] = read_from_xml(alteracao.infoCadastro.indDesFolha.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['indopccp'] = read_from_xml(alteracao.infoCadastro.indOpcCP.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['indporte'] = read_from_xml(alteracao.infoCadastro.indPorte.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['indoptregeletron'] = read_from_xml(alteracao.infoCadastro.indOptRegEletron.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['indented'] = read_from_xml(alteracao.infoCadastro.indEntEd.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['indett'] = read_from_xml(alteracao.infoCadastro.indEtt.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['nrregett'] = read_from_xml(alteracao.infoCadastro.nrRegEtt.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['nmctt'] = read_from_xml(alteracao.infoCadastro.contato.nmCtt.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['cpfctt'] = read_from_xml(alteracao.infoCadastro.contato.cpfCtt.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['fonefixo'] = read_from_xml(alteracao.infoCadastro.contato.foneFixo.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['fonecel'] = read_from_xml(alteracao.infoCadastro.contato.foneCel.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['email'] = read_from_xml(alteracao.infoCadastro.contato.email.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1000_alteracao = s1000alteracao.objects.create(**s1000_alteracao_dados)

            if 'infoCadastro' in dir(alteracao) and 'dadosIsencao' in dir(alteracao.infoCadastro):

                for dadosIsencao in alteracao.infoCadastro.dadosIsencao:

                    s1000_alteracao_dadosisencao_dados = {}
                    s1000_alteracao_dadosisencao_dados['s1000_alteracao_id'] = s1000_alteracao.id

                    try:
                        s1000_alteracao_dadosisencao_dados['ideminlei'] = read_from_xml(dadosIsencao.ideMinLei.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_dadosisencao_dados['nrcertif'] = read_from_xml(dadosIsencao.nrCertif.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_dadosisencao_dados['dtemiscertif'] = read_from_xml(dadosIsencao.dtEmisCertif.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_dadosisencao_dados['dtvenccertif'] = read_from_xml(dadosIsencao.dtVencCertif.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_dadosisencao_dados['nrprotrenov'] = read_from_xml(dadosIsencao.nrProtRenov.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_dadosisencao_dados['dtprotrenov'] = read_from_xml(dadosIsencao.dtProtRenov.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_dadosisencao_dados['dtdou'] = read_from_xml(dadosIsencao.dtDou.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_dadosisencao_dados['pagdou'] = read_from_xml(dadosIsencao.pagDou.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1000_alteracao_dadosisencao = s1000alteracaodadosIsencao.objects.create(**s1000_alteracao_dadosisencao_dados)

            if 'infoCadastro' in dir(alteracao) and 'infoOP' in dir(alteracao.infoCadastro):

                for infoOP in alteracao.infoCadastro.infoOP:

                    s1000_alteracao_infoop_dados = {}
                    s1000_alteracao_infoop_dados['s1000_alteracao_id'] = s1000_alteracao.id

                    try:
                        s1000_alteracao_infoop_dados['nrsiafi'] = read_from_xml(infoOP.nrSiafi.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_infoop_dados['indugrpps'] = read_from_xml(infoOP.indUGRPPS.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_infoop_dados['esferaop'] = read_from_xml(infoOP.esferaOP.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_infoop_dados['poderop'] = read_from_xml(infoOP.poderOP.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_infoop_dados['vrtetorem'] = read_from_xml(infoOP.vrTetoRem.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_infoop_dados['ideefr'] = read_from_xml(infoOP.ideEFR.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_infoop_dados['cnpjefr'] = read_from_xml(infoOP.cnpjEFR.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1000_alteracao_infoop = s1000alteracaoinfoOP.objects.create(**s1000_alteracao_infoop_dados)

                    if 'infoEFR' in dir(infoOP):

                        for infoEFR in infoOP.infoEFR:

                            s1000_alteracao_infoefr_dados = {}
                            s1000_alteracao_infoefr_dados['s1000_alteracao_infoop_id'] = s1000_alteracao_infoop.id
        
                            try:
                                s1000_alteracao_infoefr_dados['ideefr'] = read_from_xml(infoEFR.ideEFR.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1000_alteracao_infoefr_dados['cnpjefr'] = read_from_xml(infoEFR.cnpjEFR.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1000_alteracao_infoefr_dados['indrpps'] = read_from_xml(infoEFR.indRPPS.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1000_alteracao_infoefr_dados['prevcomp'] = read_from_xml(infoEFR.prevComp.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s1000_alteracao_infoefr = s1000alteracaoinfoEFR.objects.create(**s1000_alteracao_infoefr_dados)

                    if 'infoEnte' in dir(infoOP):

                        for infoEnte in infoOP.infoEnte:

                            s1000_alteracao_infoente_dados = {}
                            s1000_alteracao_infoente_dados['s1000_alteracao_infoop_id'] = s1000_alteracao_infoop.id
        
                            try:
                                s1000_alteracao_infoente_dados['nmente'] = read_from_xml(infoEnte.nmEnte.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1000_alteracao_infoente_dados['uf'] = read_from_xml(infoEnte.uf.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1000_alteracao_infoente_dados['codmunic'] = read_from_xml(infoEnte.codMunic.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1000_alteracao_infoente_dados['indrpps'] = read_from_xml(infoEnte.indRPPS.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1000_alteracao_infoente_dados['subteto'] = read_from_xml(infoEnte.subteto.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1000_alteracao_infoente_dados['vrsubteto'] = read_from_xml(infoEnte.vrSubteto.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s1000_alteracao_infoente = s1000alteracaoinfoEnte.objects.create(**s1000_alteracao_infoente_dados)

            if 'infoCadastro' in dir(alteracao) and 'infoOrgInternacional' in dir(alteracao.infoCadastro):

                for infoOrgInternacional in alteracao.infoCadastro.infoOrgInternacional:

                    s1000_alteracao_infoorginternacional_dados = {}
                    s1000_alteracao_infoorginternacional_dados['s1000_alteracao_id'] = s1000_alteracao.id

                    try:
                        s1000_alteracao_infoorginternacional_dados['indacordoisenmulta'] = read_from_xml(infoOrgInternacional.indAcordoIsenMulta.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1000_alteracao_infoorginternacional = s1000alteracaoinfoOrgInternacional.objects.create(**s1000_alteracao_infoorginternacional_dados)

            if 'infoCadastro' in dir(alteracao) and 'softwareHouse' in dir(alteracao.infoCadastro):

                for softwareHouse in alteracao.infoCadastro.softwareHouse:

                    s1000_alteracao_softwarehouse_dados = {}
                    s1000_alteracao_softwarehouse_dados['s1000_alteracao_id'] = s1000_alteracao.id

                    try:
                        s1000_alteracao_softwarehouse_dados['cnpjsofthouse'] = read_from_xml(softwareHouse.cnpjSoftHouse.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_softwarehouse_dados['nmrazao'] = read_from_xml(softwareHouse.nmRazao.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_softwarehouse_dados['nmcont'] = read_from_xml(softwareHouse.nmCont.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_softwarehouse_dados['telefone'] = read_from_xml(softwareHouse.telefone.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_softwarehouse_dados['email'] = read_from_xml(softwareHouse.email.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1000_alteracao_softwarehouse = s1000alteracaosoftwareHouse.objects.create(**s1000_alteracao_softwarehouse_dados)

            if 'infoCadastro' in dir(alteracao) and 'infoComplementares' in dir(alteracao.infoCadastro) and 'situacaoPJ' in dir(alteracao.infoCadastro.infoComplementares):

                for situacaoPJ in alteracao.infoCadastro.infoComplementares.situacaoPJ:

                    s1000_alteracao_situacaopj_dados = {}
                    s1000_alteracao_situacaopj_dados['s1000_alteracao_id'] = s1000_alteracao.id

                    try:
                        s1000_alteracao_situacaopj_dados['indsitpj'] = read_from_xml(situacaoPJ.indSitPJ.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1000_alteracao_situacaopj = s1000alteracaosituacaoPJ.objects.create(**s1000_alteracao_situacaopj_dados)

            if 'infoCadastro' in dir(alteracao) and 'infoComplementares' in dir(alteracao.infoCadastro) and 'situacaoPF' in dir(alteracao.infoCadastro.infoComplementares):

                for situacaoPF in alteracao.infoCadastro.infoComplementares.situacaoPF:

                    s1000_alteracao_situacaopf_dados = {}
                    s1000_alteracao_situacaopf_dados['s1000_alteracao_id'] = s1000_alteracao.id

                    try:
                        s1000_alteracao_situacaopf_dados['indsitpf'] = read_from_xml(situacaoPF.indSitPF.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1000_alteracao_situacaopf = s1000alteracaosituacaoPF.objects.create(**s1000_alteracao_situacaopf_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    s1000_alteracao_novavalidade_dados = {}
                    s1000_alteracao_novavalidade_dados['s1000_alteracao_id'] = s1000_alteracao.id

                    try:
                        s1000_alteracao_novavalidade_dados['inivalid'] = read_from_xml(novaValidade.iniValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_novavalidade_dados['fimvalid'] = read_from_xml(novaValidade.fimValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1000_alteracao_novavalidade = s1000alteracaonovaValidade.objects.create(**s1000_alteracao_novavalidade_dados)

    if 'infoEmpregador' in dir(evtInfoEmpregador) and 'exclusao' in dir(evtInfoEmpregador.infoEmpregador):

        for exclusao in evtInfoEmpregador.infoEmpregador.exclusao:

            s1000_exclusao_dados = {}
            s1000_exclusao_dados['s1000_evtinfoempregador_id'] = s1000_evtinfoempregador.id

            try:
                s1000_exclusao_dados['inivalid'] = read_from_xml(exclusao.idePeriodo.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1000_exclusao_dados['fimvalid'] = read_from_xml(exclusao.idePeriodo.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1000_exclusao = s1000exclusao.objects.create(**s1000_exclusao_dados)
    s1000_evtinfoempregador_dados['evento'] = 's1000'
    s1000_evtinfoempregador_dados['id'] = s1000_evtinfoempregador.id
    s1000_evtinfoempregador_dados['identidade_evento'] = doc.eSocial.evtInfoEmpregador['Id']

    from emensageriapro.esocial.views.s1000_evtinfoempregador_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1000_evtinfoempregador.id)

    return s1000_evtinfoempregador_dados