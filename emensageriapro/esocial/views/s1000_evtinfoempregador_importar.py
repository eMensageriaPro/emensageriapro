#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1000.models import *



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

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_s1000_evtinfoempregador_obj(request, doc, status, validar, arquivo)
    novo_arquivo = arquivo.replace('/aguardando/', '/processado/')
    s1000evtInfoEmpregador.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s1000_evtinfoempregador_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1000_evtinfoempregador_dados = {}
    s1000_evtinfoempregador_dados['status'] = status
    s1000_evtinfoempregador_dados['arquivo_original'] = 1
    if arquivo:
        s1000_evtinfoempregador_dados['arquivo'] = arquivo
    s1000_evtinfoempregador_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1000_evtinfoempregador_dados['identidade'] = doc.eSocial.evtInfoEmpregador['Id']
    evtInfoEmpregador = doc.eSocial.evtInfoEmpregador

    if 'inclusao' in dir(evtInfoEmpregador.infoEmpregador): s1000_evtinfoempregador_dados['operacao'] = 1
    elif 'alteracao' in dir(evtInfoEmpregador.infoEmpregador): s1000_evtinfoempregador_dados['operacao'] = 2
    elif 'exclusao' in dir(evtInfoEmpregador.infoEmpregador): s1000_evtinfoempregador_dados['operacao'] = 3

    try:
        s1000_evtinfoempregador_dados['tpamb'] = evtInfoEmpregador.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s1000_evtinfoempregador_dados['procemi'] = evtInfoEmpregador.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s1000_evtinfoempregador_dados['verproc'] = evtInfoEmpregador.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s1000_evtinfoempregador_dados['tpinsc'] = evtInfoEmpregador.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s1000_evtinfoempregador_dados['nrinsc'] = evtInfoEmpregador.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    s1000_evtinfoempregador = s1000evtInfoEmpregador.objects.create(**s1000_evtinfoempregador_dados)

    if 'infoEmpregador' in dir(evtInfoEmpregador) and 'inclusao' in dir(evtInfoEmpregador.infoEmpregador):

        for inclusao in evtInfoEmpregador.infoEmpregador.inclusao:

            s1000_inclusao_dados = {}
            s1000_inclusao_dados['s1000_evtinfoempregador_id'] = s1000_evtinfoempregador.id

            try:
                s1000_inclusao_dados['inivalid'] = inclusao.idePeriodo.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['fimvalid'] = inclusao.idePeriodo.fimValid.cdata
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['nmrazao'] = inclusao.infoCadastro.nmRazao.cdata
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['classtrib'] = inclusao.infoCadastro.classTrib.cdata
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['natjurid'] = inclusao.infoCadastro.natJurid.cdata
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['indcoop'] = inclusao.infoCadastro.indCoop.cdata
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['indconstr'] = inclusao.infoCadastro.indConstr.cdata
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['inddesfolha'] = inclusao.infoCadastro.indDesFolha.cdata
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['indopccp'] = inclusao.infoCadastro.indOpcCP.cdata
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['indoptregeletron'] = inclusao.infoCadastro.indOptRegEletron.cdata
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['indented'] = inclusao.infoCadastro.indEntEd.cdata
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['indett'] = inclusao.infoCadastro.indEtt.cdata
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['nrregett'] = inclusao.infoCadastro.nrRegEtt.cdata
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['nmctt'] = inclusao.infoCadastro.contato.nmCtt.cdata
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['cpfctt'] = inclusao.infoCadastro.contato.cpfCtt.cdata
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['fonefixo'] = inclusao.infoCadastro.contato.foneFixo.cdata
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['fonecel'] = inclusao.infoCadastro.contato.foneCel.cdata
            except AttributeError:
                pass

            try:
                s1000_inclusao_dados['email'] = inclusao.infoCadastro.contato.email.cdata
            except AttributeError:
                pass

            s1000_inclusao = s1000inclusao.objects.create(**s1000_inclusao_dados)

            if 'infoCadastro' in dir(inclusao) and 'dadosIsencao' in dir(inclusao.infoCadastro):

                for dadosIsencao in inclusao.infoCadastro.dadosIsencao:

                    s1000_inclusao_dadosisencao_dados = {}
                    s1000_inclusao_dadosisencao_dados['s1000_inclusao_id'] = s1000_inclusao.id

                    try:
                        s1000_inclusao_dadosisencao_dados['ideminlei'] = dadosIsencao.ideMinLei.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_dadosisencao_dados['nrcertif'] = dadosIsencao.nrCertif.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_dadosisencao_dados['dtemiscertif'] = dadosIsencao.dtEmisCertif.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_dadosisencao_dados['dtvenccertif'] = dadosIsencao.dtVencCertif.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_dadosisencao_dados['nrprotrenov'] = dadosIsencao.nrProtRenov.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_dadosisencao_dados['dtprotrenov'] = dadosIsencao.dtProtRenov.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_dadosisencao_dados['dtdou'] = dadosIsencao.dtDou.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_dadosisencao_dados['pagdou'] = dadosIsencao.pagDou.cdata
                    except AttributeError:
                        pass

                    s1000_inclusao_dadosisencao = s1000inclusaodadosIsencao.objects.create(**s1000_inclusao_dadosisencao_dados)

            if 'infoCadastro' in dir(inclusao) and 'infoOP' in dir(inclusao.infoCadastro):

                for infoOP in inclusao.infoCadastro.infoOP:

                    s1000_inclusao_infoop_dados = {}
                    s1000_inclusao_infoop_dados['s1000_inclusao_id'] = s1000_inclusao.id

                    try:
                        s1000_inclusao_infoop_dados['nrsiafi'] = infoOP.nrSiafi.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_infoop_dados['indugrpps'] = infoOP.indUGRPPS.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_infoop_dados['esferaop'] = infoOP.esferaOP.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_infoop_dados['poderop'] = infoOP.poderOP.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_infoop_dados['vrtetorem'] = infoOP.vrTetoRem.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_infoop_dados['ideefr'] = infoOP.ideEFR.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_infoop_dados['cnpjefr'] = infoOP.cnpjEFR.cdata
                    except AttributeError:
                        pass

                    s1000_inclusao_infoop = s1000inclusaoinfoOP.objects.create(**s1000_inclusao_infoop_dados)

                    if 'infoEFR' in dir(infoOP):

                        for infoEFR in infoOP.infoEFR:

                            s1000_inclusao_infoefr_dados = {}
                            s1000_inclusao_infoefr_dados['s1000_inclusao_infoop_id'] = s1000_inclusao_infoop.id
        
                            try:
                                s1000_inclusao_infoefr_dados['ideefr'] = infoEFR.ideEFR.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1000_inclusao_infoefr_dados['cnpjefr'] = infoEFR.cnpjEFR.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1000_inclusao_infoefr_dados['indrpps'] = infoEFR.indRPPS.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1000_inclusao_infoefr_dados['prevcomp'] = infoEFR.prevComp.cdata
                            except AttributeError:
                                pass

                            s1000_inclusao_infoefr = s1000inclusaoinfoEFR.objects.create(**s1000_inclusao_infoefr_dados)

                    if 'infoEnte' in dir(infoOP):

                        for infoEnte in infoOP.infoEnte:

                            s1000_inclusao_infoente_dados = {}
                            s1000_inclusao_infoente_dados['s1000_inclusao_infoop_id'] = s1000_inclusao_infoop.id
        
                            try:
                                s1000_inclusao_infoente_dados['nmente'] = infoEnte.nmEnte.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1000_inclusao_infoente_dados['uf'] = infoEnte.uf.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1000_inclusao_infoente_dados['codmunic'] = infoEnte.codMunic.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1000_inclusao_infoente_dados['indrpps'] = infoEnte.indRPPS.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1000_inclusao_infoente_dados['subteto'] = infoEnte.subteto.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1000_inclusao_infoente_dados['vrsubteto'] = infoEnte.vrSubteto.cdata
                            except AttributeError:
                                pass

                            s1000_inclusao_infoente = s1000inclusaoinfoEnte.objects.create(**s1000_inclusao_infoente_dados)

            if 'infoCadastro' in dir(inclusao) and 'infoOrgInternacional' in dir(inclusao.infoCadastro):

                for infoOrgInternacional in inclusao.infoCadastro.infoOrgInternacional:

                    s1000_inclusao_infoorginternacional_dados = {}
                    s1000_inclusao_infoorginternacional_dados['s1000_inclusao_id'] = s1000_inclusao.id

                    try:
                        s1000_inclusao_infoorginternacional_dados['indacordoisenmulta'] = infoOrgInternacional.indAcordoIsenMulta.cdata
                    except AttributeError:
                        pass

                    s1000_inclusao_infoorginternacional = s1000inclusaoinfoOrgInternacional.objects.create(**s1000_inclusao_infoorginternacional_dados)

            if 'infoCadastro' in dir(inclusao) and 'softwareHouse' in dir(inclusao.infoCadastro):

                for softwareHouse in inclusao.infoCadastro.softwareHouse:

                    s1000_inclusao_softwarehouse_dados = {}
                    s1000_inclusao_softwarehouse_dados['s1000_inclusao_id'] = s1000_inclusao.id

                    try:
                        s1000_inclusao_softwarehouse_dados['cnpjsofthouse'] = softwareHouse.cnpjSoftHouse.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_softwarehouse_dados['nmrazao'] = softwareHouse.nmRazao.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_softwarehouse_dados['nmcont'] = softwareHouse.nmCont.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_softwarehouse_dados['telefone'] = softwareHouse.telefone.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_inclusao_softwarehouse_dados['email'] = softwareHouse.email.cdata
                    except AttributeError:
                        pass

                    s1000_inclusao_softwarehouse = s1000inclusaosoftwareHouse.objects.create(**s1000_inclusao_softwarehouse_dados)

            if 'infoCadastro' in dir(inclusao) and 'infoComplementares' in dir(inclusao.infoCadastro) and 'situacaoPJ' in dir(inclusao.infoCadastro.infoComplementares):

                for situacaoPJ in inclusao.infoCadastro.infoComplementares.situacaoPJ:

                    s1000_inclusao_situacaopj_dados = {}
                    s1000_inclusao_situacaopj_dados['s1000_inclusao_id'] = s1000_inclusao.id

                    try:
                        s1000_inclusao_situacaopj_dados['indsitpj'] = situacaoPJ.indSitPJ.cdata
                    except AttributeError:
                        pass

                    s1000_inclusao_situacaopj = s1000inclusaosituacaoPJ.objects.create(**s1000_inclusao_situacaopj_dados)

            if 'infoCadastro' in dir(inclusao) and 'infoComplementares' in dir(inclusao.infoCadastro) and 'situacaoPF' in dir(inclusao.infoCadastro.infoComplementares):

                for situacaoPF in inclusao.infoCadastro.infoComplementares.situacaoPF:

                    s1000_inclusao_situacaopf_dados = {}
                    s1000_inclusao_situacaopf_dados['s1000_inclusao_id'] = s1000_inclusao.id

                    try:
                        s1000_inclusao_situacaopf_dados['indsitpf'] = situacaoPF.indSitPF.cdata
                    except AttributeError:
                        pass

                    s1000_inclusao_situacaopf = s1000inclusaosituacaoPF.objects.create(**s1000_inclusao_situacaopf_dados)

    if 'infoEmpregador' in dir(evtInfoEmpregador) and 'alteracao' in dir(evtInfoEmpregador.infoEmpregador):

        for alteracao in evtInfoEmpregador.infoEmpregador.alteracao:

            s1000_alteracao_dados = {}
            s1000_alteracao_dados['s1000_evtinfoempregador_id'] = s1000_evtinfoempregador.id

            try:
                s1000_alteracao_dados['inivalid'] = alteracao.idePeriodo.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['fimvalid'] = alteracao.idePeriodo.fimValid.cdata
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['nmrazao'] = alteracao.infoCadastro.nmRazao.cdata
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['classtrib'] = alteracao.infoCadastro.classTrib.cdata
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['natjurid'] = alteracao.infoCadastro.natJurid.cdata
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['indcoop'] = alteracao.infoCadastro.indCoop.cdata
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['indconstr'] = alteracao.infoCadastro.indConstr.cdata
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['inddesfolha'] = alteracao.infoCadastro.indDesFolha.cdata
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['indopccp'] = alteracao.infoCadastro.indOpcCP.cdata
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['indoptregeletron'] = alteracao.infoCadastro.indOptRegEletron.cdata
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['indented'] = alteracao.infoCadastro.indEntEd.cdata
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['indett'] = alteracao.infoCadastro.indEtt.cdata
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['nrregett'] = alteracao.infoCadastro.nrRegEtt.cdata
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['nmctt'] = alteracao.infoCadastro.contato.nmCtt.cdata
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['cpfctt'] = alteracao.infoCadastro.contato.cpfCtt.cdata
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['fonefixo'] = alteracao.infoCadastro.contato.foneFixo.cdata
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['fonecel'] = alteracao.infoCadastro.contato.foneCel.cdata
            except AttributeError:
                pass

            try:
                s1000_alteracao_dados['email'] = alteracao.infoCadastro.contato.email.cdata
            except AttributeError:
                pass

            s1000_alteracao = s1000alteracao.objects.create(**s1000_alteracao_dados)

            if 'infoCadastro' in dir(alteracao) and 'dadosIsencao' in dir(alteracao.infoCadastro):

                for dadosIsencao in alteracao.infoCadastro.dadosIsencao:

                    s1000_alteracao_dadosisencao_dados = {}
                    s1000_alteracao_dadosisencao_dados['s1000_alteracao_id'] = s1000_alteracao.id

                    try:
                        s1000_alteracao_dadosisencao_dados['ideminlei'] = dadosIsencao.ideMinLei.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_dadosisencao_dados['nrcertif'] = dadosIsencao.nrCertif.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_dadosisencao_dados['dtemiscertif'] = dadosIsencao.dtEmisCertif.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_dadosisencao_dados['dtvenccertif'] = dadosIsencao.dtVencCertif.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_dadosisencao_dados['nrprotrenov'] = dadosIsencao.nrProtRenov.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_dadosisencao_dados['dtprotrenov'] = dadosIsencao.dtProtRenov.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_dadosisencao_dados['dtdou'] = dadosIsencao.dtDou.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_dadosisencao_dados['pagdou'] = dadosIsencao.pagDou.cdata
                    except AttributeError:
                        pass

                    s1000_alteracao_dadosisencao = s1000alteracaodadosIsencao.objects.create(**s1000_alteracao_dadosisencao_dados)

            if 'infoCadastro' in dir(alteracao) and 'infoOP' in dir(alteracao.infoCadastro):

                for infoOP in alteracao.infoCadastro.infoOP:

                    s1000_alteracao_infoop_dados = {}
                    s1000_alteracao_infoop_dados['s1000_alteracao_id'] = s1000_alteracao.id

                    try:
                        s1000_alteracao_infoop_dados['nrsiafi'] = infoOP.nrSiafi.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_infoop_dados['indugrpps'] = infoOP.indUGRPPS.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_infoop_dados['esferaop'] = infoOP.esferaOP.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_infoop_dados['poderop'] = infoOP.poderOP.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_infoop_dados['vrtetorem'] = infoOP.vrTetoRem.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_infoop_dados['ideefr'] = infoOP.ideEFR.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_infoop_dados['cnpjefr'] = infoOP.cnpjEFR.cdata
                    except AttributeError:
                        pass

                    s1000_alteracao_infoop = s1000alteracaoinfoOP.objects.create(**s1000_alteracao_infoop_dados)

                    if 'infoEFR' in dir(infoOP):

                        for infoEFR in infoOP.infoEFR:

                            s1000_alteracao_infoefr_dados = {}
                            s1000_alteracao_infoefr_dados['s1000_alteracao_infoop_id'] = s1000_alteracao_infoop.id
        
                            try:
                                s1000_alteracao_infoefr_dados['ideefr'] = infoEFR.ideEFR.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1000_alteracao_infoefr_dados['cnpjefr'] = infoEFR.cnpjEFR.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1000_alteracao_infoefr_dados['indrpps'] = infoEFR.indRPPS.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1000_alteracao_infoefr_dados['prevcomp'] = infoEFR.prevComp.cdata
                            except AttributeError:
                                pass

                            s1000_alteracao_infoefr = s1000alteracaoinfoEFR.objects.create(**s1000_alteracao_infoefr_dados)

                    if 'infoEnte' in dir(infoOP):

                        for infoEnte in infoOP.infoEnte:

                            s1000_alteracao_infoente_dados = {}
                            s1000_alteracao_infoente_dados['s1000_alteracao_infoop_id'] = s1000_alteracao_infoop.id
        
                            try:
                                s1000_alteracao_infoente_dados['nmente'] = infoEnte.nmEnte.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1000_alteracao_infoente_dados['uf'] = infoEnte.uf.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1000_alteracao_infoente_dados['codmunic'] = infoEnte.codMunic.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1000_alteracao_infoente_dados['indrpps'] = infoEnte.indRPPS.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1000_alteracao_infoente_dados['subteto'] = infoEnte.subteto.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s1000_alteracao_infoente_dados['vrsubteto'] = infoEnte.vrSubteto.cdata
                            except AttributeError:
                                pass

                            s1000_alteracao_infoente = s1000alteracaoinfoEnte.objects.create(**s1000_alteracao_infoente_dados)

            if 'infoCadastro' in dir(alteracao) and 'infoOrgInternacional' in dir(alteracao.infoCadastro):

                for infoOrgInternacional in alteracao.infoCadastro.infoOrgInternacional:

                    s1000_alteracao_infoorginternacional_dados = {}
                    s1000_alteracao_infoorginternacional_dados['s1000_alteracao_id'] = s1000_alteracao.id

                    try:
                        s1000_alteracao_infoorginternacional_dados['indacordoisenmulta'] = infoOrgInternacional.indAcordoIsenMulta.cdata
                    except AttributeError:
                        pass

                    s1000_alteracao_infoorginternacional = s1000alteracaoinfoOrgInternacional.objects.create(**s1000_alteracao_infoorginternacional_dados)

            if 'infoCadastro' in dir(alteracao) and 'softwareHouse' in dir(alteracao.infoCadastro):

                for softwareHouse in alteracao.infoCadastro.softwareHouse:

                    s1000_alteracao_softwarehouse_dados = {}
                    s1000_alteracao_softwarehouse_dados['s1000_alteracao_id'] = s1000_alteracao.id

                    try:
                        s1000_alteracao_softwarehouse_dados['cnpjsofthouse'] = softwareHouse.cnpjSoftHouse.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_softwarehouse_dados['nmrazao'] = softwareHouse.nmRazao.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_softwarehouse_dados['nmcont'] = softwareHouse.nmCont.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_softwarehouse_dados['telefone'] = softwareHouse.telefone.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_softwarehouse_dados['email'] = softwareHouse.email.cdata
                    except AttributeError:
                        pass

                    s1000_alteracao_softwarehouse = s1000alteracaosoftwareHouse.objects.create(**s1000_alteracao_softwarehouse_dados)

            if 'infoCadastro' in dir(alteracao) and 'infoComplementares' in dir(alteracao.infoCadastro) and 'situacaoPJ' in dir(alteracao.infoCadastro.infoComplementares):

                for situacaoPJ in alteracao.infoCadastro.infoComplementares.situacaoPJ:

                    s1000_alteracao_situacaopj_dados = {}
                    s1000_alteracao_situacaopj_dados['s1000_alteracao_id'] = s1000_alteracao.id

                    try:
                        s1000_alteracao_situacaopj_dados['indsitpj'] = situacaoPJ.indSitPJ.cdata
                    except AttributeError:
                        pass

                    s1000_alteracao_situacaopj = s1000alteracaosituacaoPJ.objects.create(**s1000_alteracao_situacaopj_dados)

            if 'infoCadastro' in dir(alteracao) and 'infoComplementares' in dir(alteracao.infoCadastro) and 'situacaoPF' in dir(alteracao.infoCadastro.infoComplementares):

                for situacaoPF in alteracao.infoCadastro.infoComplementares.situacaoPF:

                    s1000_alteracao_situacaopf_dados = {}
                    s1000_alteracao_situacaopf_dados['s1000_alteracao_id'] = s1000_alteracao.id

                    try:
                        s1000_alteracao_situacaopf_dados['indsitpf'] = situacaoPF.indSitPF.cdata
                    except AttributeError:
                        pass

                    s1000_alteracao_situacaopf = s1000alteracaosituacaoPF.objects.create(**s1000_alteracao_situacaopf_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    s1000_alteracao_novavalidade_dados = {}
                    s1000_alteracao_novavalidade_dados['s1000_alteracao_id'] = s1000_alteracao.id

                    try:
                        s1000_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError:
                        pass

                    try:
                        s1000_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError:
                        pass

                    s1000_alteracao_novavalidade = s1000alteracaonovaValidade.objects.create(**s1000_alteracao_novavalidade_dados)

    if 'infoEmpregador' in dir(evtInfoEmpregador) and 'exclusao' in dir(evtInfoEmpregador.infoEmpregador):

        for exclusao in evtInfoEmpregador.infoEmpregador.exclusao:

            s1000_exclusao_dados = {}
            s1000_exclusao_dados['s1000_evtinfoempregador_id'] = s1000_evtinfoempregador.id

            try:
                s1000_exclusao_dados['inivalid'] = exclusao.idePeriodo.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1000_exclusao_dados['fimvalid'] = exclusao.idePeriodo.fimValid.cdata
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