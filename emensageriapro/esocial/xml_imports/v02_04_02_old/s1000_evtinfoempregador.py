#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql




def read_s1000_evtinfoempregador(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    s1000_evtinfoempregador_dados = {}
    xmlns = doc.eSocial['xmlns'].split('/')
    if validar:
        s1000_evtinfoempregador_dados['status'] = 1
    else:
        s1000_evtinfoempregador_dados['status'] = 0
    s1000_evtinfoempregador_dados['versao'] = xmlns[len(xmlns)-1]
    s1000_evtinfoempregador_dados['identidade'] = doc.eSocial.evtInfoEmpregador['Id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_esocial WHERE identidade = '%s';
    #     """ % s1000_evtinfoempregador_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    s1000_evtinfoempregador_dados['processamento_codigo_resposta'] = 1
    evtInfoEmpregador = doc.eSocial.evtInfoEmpregador
    
    if 'tpAmb' in dir(evtInfoEmpregador.ideEvento): s1000_evtinfoempregador_dados['tpamb'] = evtInfoEmpregador.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtInfoEmpregador.ideEvento): s1000_evtinfoempregador_dados['procemi'] = evtInfoEmpregador.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtInfoEmpregador.ideEvento): s1000_evtinfoempregador_dados['verproc'] = evtInfoEmpregador.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtInfoEmpregador.ideEmpregador): s1000_evtinfoempregador_dados['tpinsc'] = evtInfoEmpregador.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtInfoEmpregador.ideEmpregador): s1000_evtinfoempregador_dados['nrinsc'] = evtInfoEmpregador.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtInfoEmpregador.infoEmpregador): s1000_evtinfoempregador_dados['operacao'] = 1
    elif 'alteracao' in dir(evtInfoEmpregador.infoEmpregador): s1000_evtinfoempregador_dados['operacao'] = 2
    elif 'exclusao' in dir(evtInfoEmpregador.infoEmpregador): s1000_evtinfoempregador_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1000_evtinfoempregador', s1000_evtinfoempregador_dados)
    resp = executar_sql(insert, True)
    s1000_evtinfoempregador_id = resp[0][0]
    dados['evento'] = 's1000'
    dados['identidade'] = s1000_evtinfoempregador_id
    dados['identidade_evento'] = doc.eSocial.evtInfoEmpregador['Id']
    dados['status'] = 1

    if 'inclusao' in dir(evtInfoEmpregador.infoEmpregador):
        for inclusao in evtInfoEmpregador.infoEmpregador.inclusao:
            s1000_inclusao_dados = {}
            s1000_inclusao_dados['s1000_evtinfoempregador_id'] = s1000_evtinfoempregador_id
            
            if 'iniValid' in dir(inclusao.idePeriodo): s1000_inclusao_dados['inivalid'] = inclusao.idePeriodo.iniValid.cdata
            if 'fimValid' in dir(inclusao.idePeriodo): s1000_inclusao_dados['fimvalid'] = inclusao.idePeriodo.fimValid.cdata
            if 'nmRazao' in dir(inclusao.infoCadastro): s1000_inclusao_dados['nmrazao'] = inclusao.infoCadastro.nmRazao.cdata
            if 'classTrib' in dir(inclusao.infoCadastro): s1000_inclusao_dados['classtrib'] = inclusao.infoCadastro.classTrib.cdata
            if 'natJurid' in dir(inclusao.infoCadastro): s1000_inclusao_dados['natjurid'] = inclusao.infoCadastro.natJurid.cdata
            if 'indCoop' in dir(inclusao.infoCadastro): s1000_inclusao_dados['indcoop'] = inclusao.infoCadastro.indCoop.cdata
            if 'indConstr' in dir(inclusao.infoCadastro): s1000_inclusao_dados['indconstr'] = inclusao.infoCadastro.indConstr.cdata
            if 'indDesFolha' in dir(inclusao.infoCadastro): s1000_inclusao_dados['inddesfolha'] = inclusao.infoCadastro.indDesFolha.cdata
            if 'indOptRegEletron' in dir(inclusao.infoCadastro): s1000_inclusao_dados['indoptregeletron'] = inclusao.infoCadastro.indOptRegEletron.cdata
            if 'indEntEd' in dir(inclusao.infoCadastro): s1000_inclusao_dados['indented'] = inclusao.infoCadastro.indEntEd.cdata
            if 'indEtt' in dir(inclusao.infoCadastro): s1000_inclusao_dados['indett'] = inclusao.infoCadastro.indEtt.cdata
            if 'nrRegEtt' in dir(inclusao.infoCadastro): s1000_inclusao_dados['nrregett'] = inclusao.infoCadastro.nrRegEtt.cdata
            if 'nmCtt' in dir(inclusao.infoCadastro.contato): s1000_inclusao_dados['nmctt'] = inclusao.infoCadastro.contato.nmCtt.cdata
            if 'cpfCtt' in dir(inclusao.infoCadastro.contato): s1000_inclusao_dados['cpfctt'] = inclusao.infoCadastro.contato.cpfCtt.cdata
            if 'foneFixo' in dir(inclusao.infoCadastro.contato): s1000_inclusao_dados['fonefixo'] = inclusao.infoCadastro.contato.foneFixo.cdata
            if 'foneCel' in dir(inclusao.infoCadastro.contato): s1000_inclusao_dados['fonecel'] = inclusao.infoCadastro.contato.foneCel.cdata
            if 'email' in dir(inclusao.infoCadastro.contato): s1000_inclusao_dados['email'] = inclusao.infoCadastro.contato.email.cdata
            insert = create_insert('s1000_inclusao', s1000_inclusao_dados)
            resp = executar_sql(insert, True)
            s1000_inclusao_id = resp[0][0]
            #print s1000_inclusao_id

            if 'dadosIsencao' in dir(inclusao.infoCadastro):
                for dadosIsencao in inclusao.infoCadastro.dadosIsencao:
                    s1000_inclusao_dadosisencao_dados = {}
                    s1000_inclusao_dadosisencao_dados['s1000_inclusao_id'] = s1000_inclusao_id
                    
                    if 'ideMinLei' in dir(dadosIsencao): s1000_inclusao_dadosisencao_dados['ideminlei'] = dadosIsencao.ideMinLei.cdata
                    if 'nrCertif' in dir(dadosIsencao): s1000_inclusao_dadosisencao_dados['nrcertif'] = dadosIsencao.nrCertif.cdata
                    if 'dtEmisCertif' in dir(dadosIsencao): s1000_inclusao_dadosisencao_dados['dtemiscertif'] = dadosIsencao.dtEmisCertif.cdata
                    if 'dtVencCertif' in dir(dadosIsencao): s1000_inclusao_dadosisencao_dados['dtvenccertif'] = dadosIsencao.dtVencCertif.cdata
                    if 'nrProtRenov' in dir(dadosIsencao): s1000_inclusao_dadosisencao_dados['nrprotrenov'] = dadosIsencao.nrProtRenov.cdata
                    if 'dtProtRenov' in dir(dadosIsencao): s1000_inclusao_dadosisencao_dados['dtprotrenov'] = dadosIsencao.dtProtRenov.cdata
                    if 'dtDou' in dir(dadosIsencao): s1000_inclusao_dadosisencao_dados['dtdou'] = dadosIsencao.dtDou.cdata
                    if 'pagDou' in dir(dadosIsencao): s1000_inclusao_dadosisencao_dados['pagdou'] = dadosIsencao.pagDou.cdata
                    insert = create_insert('s1000_inclusao_dadosisencao', s1000_inclusao_dadosisencao_dados)
                    resp = executar_sql(insert, True)
                    s1000_inclusao_dadosisencao_id = resp[0][0]
                    #print s1000_inclusao_dadosisencao_id
        
            if 'infoOP' in dir(inclusao.infoCadastro):
                for infoOP in inclusao.infoCadastro.infoOP:
                    s1000_inclusao_infoop_dados = {}
                    s1000_inclusao_infoop_dados['s1000_inclusao_id'] = s1000_inclusao_id
                    
                    if 'nrSiafi' in dir(infoOP): s1000_inclusao_infoop_dados['nrsiafi'] = infoOP.nrSiafi.cdata
                    insert = create_insert('s1000_inclusao_infoop', s1000_inclusao_infoop_dados)
                    resp = executar_sql(insert, True)
                    s1000_inclusao_infoop_id = resp[0][0]
                    #print s1000_inclusao_infoop_id
        
            if 'infoOrgInternacional' in dir(inclusao.infoCadastro):
                for infoOrgInternacional in inclusao.infoCadastro.infoOrgInternacional:
                    s1000_inclusao_infoorginternacional_dados = {}
                    s1000_inclusao_infoorginternacional_dados['s1000_inclusao_id'] = s1000_inclusao_id
                    
                    if 'indAcordoIsenMulta' in dir(infoOrgInternacional): s1000_inclusao_infoorginternacional_dados['indacordoisenmulta'] = infoOrgInternacional.indAcordoIsenMulta.cdata
                    insert = create_insert('s1000_inclusao_infoorginternacional', s1000_inclusao_infoorginternacional_dados)
                    resp = executar_sql(insert, True)
                    s1000_inclusao_infoorginternacional_id = resp[0][0]
                    #print s1000_inclusao_infoorginternacional_id
        
            if 'softwareHouse' in dir(inclusao.infoCadastro):
                for softwareHouse in inclusao.infoCadastro.softwareHouse:
                    s1000_inclusao_softwarehouse_dados = {}
                    s1000_inclusao_softwarehouse_dados['s1000_inclusao_id'] = s1000_inclusao_id
                    
                    if 'cnpjSoftHouse' in dir(softwareHouse): s1000_inclusao_softwarehouse_dados['cnpjsofthouse'] = softwareHouse.cnpjSoftHouse.cdata
                    if 'nmRazao' in dir(softwareHouse): s1000_inclusao_softwarehouse_dados['nmrazao'] = softwareHouse.nmRazao.cdata
                    if 'nmCont' in dir(softwareHouse): s1000_inclusao_softwarehouse_dados['nmcont'] = softwareHouse.nmCont.cdata
                    if 'telefone' in dir(softwareHouse): s1000_inclusao_softwarehouse_dados['telefone'] = softwareHouse.telefone.cdata
                    if 'email' in dir(softwareHouse): s1000_inclusao_softwarehouse_dados['email'] = softwareHouse.email.cdata
                    insert = create_insert('s1000_inclusao_softwarehouse', s1000_inclusao_softwarehouse_dados)
                    resp = executar_sql(insert, True)
                    s1000_inclusao_softwarehouse_id = resp[0][0]
                    #print s1000_inclusao_softwarehouse_id
        
            if 'situacaoPJ' in dir(inclusao.infoCadastro.infoComplementares):
                for situacaoPJ in inclusao.infoCadastro.infoComplementares.situacaoPJ:
                    s1000_inclusao_situacaopj_dados = {}
                    s1000_inclusao_situacaopj_dados['s1000_inclusao_id'] = s1000_inclusao_id
                    
                    if 'indSitPJ' in dir(situacaoPJ): s1000_inclusao_situacaopj_dados['indsitpj'] = situacaoPJ.indSitPJ.cdata
                    insert = create_insert('s1000_inclusao_situacaopj', s1000_inclusao_situacaopj_dados)
                    resp = executar_sql(insert, True)
                    s1000_inclusao_situacaopj_id = resp[0][0]
                    #print s1000_inclusao_situacaopj_id
        
            if 'situacaoPF' in dir(inclusao.infoCadastro.infoComplementares):
                for situacaoPF in inclusao.infoCadastro.infoComplementares.situacaoPF:
                    s1000_inclusao_situacaopf_dados = {}
                    s1000_inclusao_situacaopf_dados['s1000_inclusao_id'] = s1000_inclusao_id
                    
                    if 'indSitPF' in dir(situacaoPF): s1000_inclusao_situacaopf_dados['indsitpf'] = situacaoPF.indSitPF.cdata
                    insert = create_insert('s1000_inclusao_situacaopf', s1000_inclusao_situacaopf_dados)
                    resp = executar_sql(insert, True)
                    s1000_inclusao_situacaopf_id = resp[0][0]
                    #print s1000_inclusao_situacaopf_id
        
    if 'alteracao' in dir(evtInfoEmpregador.infoEmpregador):
        for alteracao in evtInfoEmpregador.infoEmpregador.alteracao:
            s1000_alteracao_dados = {}
            s1000_alteracao_dados['s1000_evtinfoempregador_id'] = s1000_evtinfoempregador_id
            
            if 'iniValid' in dir(alteracao.idePeriodo): s1000_alteracao_dados['inivalid'] = alteracao.idePeriodo.iniValid.cdata
            if 'fimValid' in dir(alteracao.idePeriodo): s1000_alteracao_dados['fimvalid'] = alteracao.idePeriodo.fimValid.cdata
            if 'nmRazao' in dir(alteracao.infoCadastro): s1000_alteracao_dados['nmrazao'] = alteracao.infoCadastro.nmRazao.cdata
            if 'classTrib' in dir(alteracao.infoCadastro): s1000_alteracao_dados['classtrib'] = alteracao.infoCadastro.classTrib.cdata
            if 'natJurid' in dir(alteracao.infoCadastro): s1000_alteracao_dados['natjurid'] = alteracao.infoCadastro.natJurid.cdata
            if 'indCoop' in dir(alteracao.infoCadastro): s1000_alteracao_dados['indcoop'] = alteracao.infoCadastro.indCoop.cdata
            if 'indConstr' in dir(alteracao.infoCadastro): s1000_alteracao_dados['indconstr'] = alteracao.infoCadastro.indConstr.cdata
            if 'indDesFolha' in dir(alteracao.infoCadastro): s1000_alteracao_dados['inddesfolha'] = alteracao.infoCadastro.indDesFolha.cdata
            if 'indOptRegEletron' in dir(alteracao.infoCadastro): s1000_alteracao_dados['indoptregeletron'] = alteracao.infoCadastro.indOptRegEletron.cdata
            if 'indEntEd' in dir(alteracao.infoCadastro): s1000_alteracao_dados['indented'] = alteracao.infoCadastro.indEntEd.cdata
            if 'indEtt' in dir(alteracao.infoCadastro): s1000_alteracao_dados['indett'] = alteracao.infoCadastro.indEtt.cdata
            if 'nrRegEtt' in dir(alteracao.infoCadastro): s1000_alteracao_dados['nrregett'] = alteracao.infoCadastro.nrRegEtt.cdata
            if 'nmCtt' in dir(alteracao.infoCadastro.contato): s1000_alteracao_dados['nmctt'] = alteracao.infoCadastro.contato.nmCtt.cdata
            if 'cpfCtt' in dir(alteracao.infoCadastro.contato): s1000_alteracao_dados['cpfctt'] = alteracao.infoCadastro.contato.cpfCtt.cdata
            if 'foneFixo' in dir(alteracao.infoCadastro.contato): s1000_alteracao_dados['fonefixo'] = alteracao.infoCadastro.contato.foneFixo.cdata
            if 'foneCel' in dir(alteracao.infoCadastro.contato): s1000_alteracao_dados['fonecel'] = alteracao.infoCadastro.contato.foneCel.cdata
            if 'email' in dir(alteracao.infoCadastro.contato): s1000_alteracao_dados['email'] = alteracao.infoCadastro.contato.email.cdata
            insert = create_insert('s1000_alteracao', s1000_alteracao_dados)
            resp = executar_sql(insert, True)
            s1000_alteracao_id = resp[0][0]
            #print s1000_alteracao_id

            if 'dadosIsencao' in dir(alteracao.infoCadastro):
                for dadosIsencao in alteracao.infoCadastro.dadosIsencao:
                    s1000_alteracao_dadosisencao_dados = {}
                    s1000_alteracao_dadosisencao_dados['s1000_alteracao_id'] = s1000_alteracao_id
                    
                    if 'ideMinLei' in dir(dadosIsencao): s1000_alteracao_dadosisencao_dados['ideminlei'] = dadosIsencao.ideMinLei.cdata
                    if 'nrCertif' in dir(dadosIsencao): s1000_alteracao_dadosisencao_dados['nrcertif'] = dadosIsencao.nrCertif.cdata
                    if 'dtEmisCertif' in dir(dadosIsencao): s1000_alteracao_dadosisencao_dados['dtemiscertif'] = dadosIsencao.dtEmisCertif.cdata
                    if 'dtVencCertif' in dir(dadosIsencao): s1000_alteracao_dadosisencao_dados['dtvenccertif'] = dadosIsencao.dtVencCertif.cdata
                    if 'nrProtRenov' in dir(dadosIsencao): s1000_alteracao_dadosisencao_dados['nrprotrenov'] = dadosIsencao.nrProtRenov.cdata
                    if 'dtProtRenov' in dir(dadosIsencao): s1000_alteracao_dadosisencao_dados['dtprotrenov'] = dadosIsencao.dtProtRenov.cdata
                    if 'dtDou' in dir(dadosIsencao): s1000_alteracao_dadosisencao_dados['dtdou'] = dadosIsencao.dtDou.cdata
                    if 'pagDou' in dir(dadosIsencao): s1000_alteracao_dadosisencao_dados['pagdou'] = dadosIsencao.pagDou.cdata
                    insert = create_insert('s1000_alteracao_dadosisencao', s1000_alteracao_dadosisencao_dados)
                    resp = executar_sql(insert, True)
                    s1000_alteracao_dadosisencao_id = resp[0][0]
                    #print s1000_alteracao_dadosisencao_id
        
            if 'infoOP' in dir(alteracao.infoCadastro):
                for infoOP in alteracao.infoCadastro.infoOP:
                    s1000_alteracao_infoop_dados = {}
                    s1000_alteracao_infoop_dados['s1000_alteracao_id'] = s1000_alteracao_id
                    
                    if 'nrSiafi' in dir(infoOP): s1000_alteracao_infoop_dados['nrsiafi'] = infoOP.nrSiafi.cdata
                    insert = create_insert('s1000_alteracao_infoop', s1000_alteracao_infoop_dados)
                    resp = executar_sql(insert, True)
                    s1000_alteracao_infoop_id = resp[0][0]
                    #print s1000_alteracao_infoop_id
        
            if 'infoOrgInternacional' in dir(alteracao.infoCadastro):
                for infoOrgInternacional in alteracao.infoCadastro.infoOrgInternacional:
                    s1000_alteracao_infoorginternacional_dados = {}
                    s1000_alteracao_infoorginternacional_dados['s1000_alteracao_id'] = s1000_alteracao_id
                    
                    if 'indAcordoIsenMulta' in dir(infoOrgInternacional): s1000_alteracao_infoorginternacional_dados['indacordoisenmulta'] = infoOrgInternacional.indAcordoIsenMulta.cdata
                    insert = create_insert('s1000_alteracao_infoorginternacional', s1000_alteracao_infoorginternacional_dados)
                    resp = executar_sql(insert, True)
                    s1000_alteracao_infoorginternacional_id = resp[0][0]
                    #print s1000_alteracao_infoorginternacional_id
        
            if 'softwareHouse' in dir(alteracao.infoCadastro):
                for softwareHouse in alteracao.infoCadastro.softwareHouse:
                    s1000_alteracao_softwarehouse_dados = {}
                    s1000_alteracao_softwarehouse_dados['s1000_alteracao_id'] = s1000_alteracao_id
                    
                    if 'cnpjSoftHouse' in dir(softwareHouse): s1000_alteracao_softwarehouse_dados['cnpjsofthouse'] = softwareHouse.cnpjSoftHouse.cdata
                    if 'nmRazao' in dir(softwareHouse): s1000_alteracao_softwarehouse_dados['nmrazao'] = softwareHouse.nmRazao.cdata
                    if 'nmCont' in dir(softwareHouse): s1000_alteracao_softwarehouse_dados['nmcont'] = softwareHouse.nmCont.cdata
                    if 'telefone' in dir(softwareHouse): s1000_alteracao_softwarehouse_dados['telefone'] = softwareHouse.telefone.cdata
                    if 'email' in dir(softwareHouse): s1000_alteracao_softwarehouse_dados['email'] = softwareHouse.email.cdata
                    insert = create_insert('s1000_alteracao_softwarehouse', s1000_alteracao_softwarehouse_dados)
                    resp = executar_sql(insert, True)
                    s1000_alteracao_softwarehouse_id = resp[0][0]
                    #print s1000_alteracao_softwarehouse_id
        
            if 'situacaoPJ' in dir(alteracao.infoCadastro.infoComplementares):
                for situacaoPJ in alteracao.infoCadastro.infoComplementares.situacaoPJ:
                    s1000_alteracao_situacaopj_dados = {}
                    s1000_alteracao_situacaopj_dados['s1000_alteracao_id'] = s1000_alteracao_id
                    
                    if 'indSitPJ' in dir(situacaoPJ): s1000_alteracao_situacaopj_dados['indsitpj'] = situacaoPJ.indSitPJ.cdata
                    insert = create_insert('s1000_alteracao_situacaopj', s1000_alteracao_situacaopj_dados)
                    resp = executar_sql(insert, True)
                    s1000_alteracao_situacaopj_id = resp[0][0]
                    #print s1000_alteracao_situacaopj_id
        
            if 'situacaoPF' in dir(alteracao.infoCadastro.infoComplementares):
                for situacaoPF in alteracao.infoCadastro.infoComplementares.situacaoPF:
                    s1000_alteracao_situacaopf_dados = {}
                    s1000_alteracao_situacaopf_dados['s1000_alteracao_id'] = s1000_alteracao_id
                    
                    if 'indSitPF' in dir(situacaoPF): s1000_alteracao_situacaopf_dados['indsitpf'] = situacaoPF.indSitPF.cdata
                    insert = create_insert('s1000_alteracao_situacaopf', s1000_alteracao_situacaopf_dados)
                    resp = executar_sql(insert, True)
                    s1000_alteracao_situacaopf_id = resp[0][0]
                    #print s1000_alteracao_situacaopf_id
        
            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    s1000_alteracao_novavalidade_dados = {}
                    s1000_alteracao_novavalidade_dados['s1000_alteracao_id'] = s1000_alteracao_id
                    
                    if 'iniValid' in dir(novaValidade): s1000_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    if 'fimValid' in dir(novaValidade): s1000_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    insert = create_insert('s1000_alteracao_novavalidade', s1000_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1000_alteracao_novavalidade_id = resp[0][0]
                    #print s1000_alteracao_novavalidade_id
        
    if 'exclusao' in dir(evtInfoEmpregador.infoEmpregador):
        for exclusao in evtInfoEmpregador.infoEmpregador.exclusao:
            s1000_exclusao_dados = {}
            s1000_exclusao_dados['s1000_evtinfoempregador_id'] = s1000_evtinfoempregador_id
            
            if 'iniValid' in dir(exclusao.idePeriodo): s1000_exclusao_dados['inivalid'] = exclusao.idePeriodo.iniValid.cdata
            if 'fimValid' in dir(exclusao.idePeriodo): s1000_exclusao_dados['fimvalid'] = exclusao.idePeriodo.fimValid.cdata
            insert = create_insert('s1000_exclusao', s1000_exclusao_dados)
            resp = executar_sql(insert, True)
            s1000_exclusao_id = resp[0][0]
            #print s1000_exclusao_id

    from emensageriapro.esocial.views.s1000_evtinfoempregador_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1000_evtinfoempregador_id, 'default')
    return dados