#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql




def read_s2306_evttsvaltcontr(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    s2306_evttsvaltcontr_dados = {}
    xmlns = doc.eSocial['xmlns'].split('/')
    if validar:
        s2306_evttsvaltcontr_dados['status'] = 1
    else:
        s2306_evttsvaltcontr_dados['status'] = 0
    s2306_evttsvaltcontr_dados['versao'] = xmlns[len(xmlns)-1]
    s2306_evttsvaltcontr_dados['identidade'] = doc.eSocial.evtTSVAltContr['Id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_esocial WHERE identidade = '%s';
    #     """ % s2306_evttsvaltcontr_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    s2306_evttsvaltcontr_dados['processamento_codigo_resposta'] = 1
    evtTSVAltContr = doc.eSocial.evtTSVAltContr
    
    if 'indRetif' in dir(evtTSVAltContr.ideEvento): s2306_evttsvaltcontr_dados['indretif'] = evtTSVAltContr.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtTSVAltContr.ideEvento): s2306_evttsvaltcontr_dados['nrrecibo'] = evtTSVAltContr.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtTSVAltContr.ideEvento): s2306_evttsvaltcontr_dados['tpamb'] = evtTSVAltContr.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTSVAltContr.ideEvento): s2306_evttsvaltcontr_dados['procemi'] = evtTSVAltContr.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTSVAltContr.ideEvento): s2306_evttsvaltcontr_dados['verproc'] = evtTSVAltContr.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTSVAltContr.ideEmpregador): s2306_evttsvaltcontr_dados['tpinsc'] = evtTSVAltContr.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTSVAltContr.ideEmpregador): s2306_evttsvaltcontr_dados['nrinsc'] = evtTSVAltContr.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtTSVAltContr.ideTrabSemVinculo): s2306_evttsvaltcontr_dados['cpftrab'] = evtTSVAltContr.ideTrabSemVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtTSVAltContr.ideTrabSemVinculo): s2306_evttsvaltcontr_dados['nistrab'] = evtTSVAltContr.ideTrabSemVinculo.nisTrab.cdata
    if 'codCateg' in dir(evtTSVAltContr.ideTrabSemVinculo): s2306_evttsvaltcontr_dados['codcateg'] = evtTSVAltContr.ideTrabSemVinculo.codCateg.cdata
    if 'dtAlteracao' in dir(evtTSVAltContr.infoTSVAlteracao): s2306_evttsvaltcontr_dados['dtalteracao'] = evtTSVAltContr.infoTSVAlteracao.dtAlteracao.cdata
    if 'natAtividade' in dir(evtTSVAltContr.infoTSVAlteracao): s2306_evttsvaltcontr_dados['natatividade'] = evtTSVAltContr.infoTSVAlteracao.natAtividade.cdata
    if 'inclusao' in dir(evtTSVAltContr.infoTSVAlteracao): s2306_evttsvaltcontr_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTSVAltContr.infoTSVAlteracao): s2306_evttsvaltcontr_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTSVAltContr.infoTSVAlteracao): s2306_evttsvaltcontr_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2306_evttsvaltcontr', s2306_evttsvaltcontr_dados)
    resp = executar_sql(insert, True)
    s2306_evttsvaltcontr_id = resp[0][0]
    dados['evento'] = 's2306'
    dados['identidade'] = s2306_evttsvaltcontr_id
    dados['identidade_evento'] = doc.eSocial.evtTSVAltContr['Id']
    dados['status'] = 1

    if 'infoComplementares' in dir(evtTSVAltContr.infoTSVAlteracao):
        for infoComplementares in evtTSVAltContr.infoTSVAlteracao.infoComplementares:
            s2306_infocomplementares_dados = {}
            s2306_infocomplementares_dados['s2306_evttsvaltcontr_id'] = s2306_evttsvaltcontr_id
            
            insert = create_insert('s2306_infocomplementares', s2306_infocomplementares_dados)
            resp = executar_sql(insert, True)
            s2306_infocomplementares_id = resp[0][0]
            #print s2306_infocomplementares_id

            if 'cargoFuncao' in dir(infoComplementares):
                for cargoFuncao in infoComplementares.cargoFuncao:
                    s2306_cargofuncao_dados = {}
                    s2306_cargofuncao_dados['s2306_infocomplementares_id'] = s2306_infocomplementares_id
                    
                    if 'codCargo' in dir(cargoFuncao): s2306_cargofuncao_dados['codcargo'] = cargoFuncao.codCargo.cdata
                    if 'codFuncao' in dir(cargoFuncao): s2306_cargofuncao_dados['codfuncao'] = cargoFuncao.codFuncao.cdata
                    insert = create_insert('s2306_cargofuncao', s2306_cargofuncao_dados)
                    resp = executar_sql(insert, True)
                    s2306_cargofuncao_id = resp[0][0]
                    #print s2306_cargofuncao_id
        
            if 'remuneracao' in dir(infoComplementares):
                for remuneracao in infoComplementares.remuneracao:
                    s2306_remuneracao_dados = {}
                    s2306_remuneracao_dados['s2306_infocomplementares_id'] = s2306_infocomplementares_id
                    
                    if 'vrSalFx' in dir(remuneracao): s2306_remuneracao_dados['vrsalfx'] = remuneracao.vrSalFx.cdata
                    if 'undSalFixo' in dir(remuneracao): s2306_remuneracao_dados['undsalfixo'] = remuneracao.undSalFixo.cdata
                    if 'dscSalVar' in dir(remuneracao): s2306_remuneracao_dados['dscsalvar'] = remuneracao.dscSalVar.cdata
                    insert = create_insert('s2306_remuneracao', s2306_remuneracao_dados)
                    resp = executar_sql(insert, True)
                    s2306_remuneracao_id = resp[0][0]
                    #print s2306_remuneracao_id
        
            if 'infoEstagiario' in dir(infoComplementares):
                for infoEstagiario in infoComplementares.infoEstagiario:
                    s2306_infoestagiario_dados = {}
                    s2306_infoestagiario_dados['s2306_infocomplementares_id'] = s2306_infocomplementares_id
                    
                    if 'natEstagio' in dir(infoEstagiario): s2306_infoestagiario_dados['natestagio'] = infoEstagiario.natEstagio.cdata
                    if 'nivEstagio' in dir(infoEstagiario): s2306_infoestagiario_dados['nivestagio'] = infoEstagiario.nivEstagio.cdata
                    if 'areaAtuacao' in dir(infoEstagiario): s2306_infoestagiario_dados['areaatuacao'] = infoEstagiario.areaAtuacao.cdata
                    if 'nrApol' in dir(infoEstagiario): s2306_infoestagiario_dados['nrapol'] = infoEstagiario.nrApol.cdata
                    if 'vlrBolsa' in dir(infoEstagiario): s2306_infoestagiario_dados['vlrbolsa'] = infoEstagiario.vlrBolsa.cdata
                    if 'dtPrevTerm' in dir(infoEstagiario): s2306_infoestagiario_dados['dtprevterm'] = infoEstagiario.dtPrevTerm.cdata
                    if 'cnpjInstEnsino' in dir(infoEstagiario): s2306_infoestagiario_dados['cnpjinstensino'] = infoEstagiario.instEnsino.cnpjInstEnsino.cdata
                    if 'nmRazao' in dir(infoEstagiario): s2306_infoestagiario_dados['nmrazao'] = infoEstagiario.instEnsino.nmRazao.cdata
                    if 'dscLograd' in dir(infoEstagiario): s2306_infoestagiario_dados['dsclograd'] = infoEstagiario.instEnsino.dscLograd.cdata
                    if 'nrLograd' in dir(infoEstagiario): s2306_infoestagiario_dados['nrlograd'] = infoEstagiario.instEnsino.nrLograd.cdata
                    if 'bairro' in dir(infoEstagiario): s2306_infoestagiario_dados['bairro'] = infoEstagiario.instEnsino.bairro.cdata
                    if 'cep' in dir(infoEstagiario): s2306_infoestagiario_dados['cep'] = infoEstagiario.instEnsino.cep.cdata
                    if 'codMunic' in dir(infoEstagiario): s2306_infoestagiario_dados['codmunic'] = infoEstagiario.instEnsino.codMunic.cdata
                    if 'uf' in dir(infoEstagiario): s2306_infoestagiario_dados['uf'] = infoEstagiario.instEnsino.uf.cdata
                    insert = create_insert('s2306_infoestagiario', s2306_infoestagiario_dados)
                    resp = executar_sql(insert, True)
                    s2306_infoestagiario_id = resp[0][0]
                    #print s2306_infoestagiario_id
        
    from emensageriapro.esocial.views.s2306_evttsvaltcontr_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2306_evttsvaltcontr_id, 'default')
    return dados