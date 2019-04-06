#coding:utf-8
"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos <www.emensageria.com.br>
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
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO



def read_s2306_evttsvaltcontr_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2306_evttsvaltcontr_obj(doc, status, validar)
    return dados

def read_s2306_evttsvaltcontr(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2306_evttsvaltcontr_obj(doc, status, validar)
    return dados



def read_s2306_evttsvaltcontr_obj(doc, status, validar=False):
    s2306_evttsvaltcontr_dados = {}
    s2306_evttsvaltcontr_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2306_evttsvaltcontr_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2306_evttsvaltcontr_dados['identidade'] = doc.eSocial.evtTSVAltContr['Id']
    evtTSVAltContr = doc.eSocial.evtTSVAltContr

    try: s2306_evttsvaltcontr_dados['indretif'] = evtTSVAltContr.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s2306_evttsvaltcontr_dados['nrrecibo'] = evtTSVAltContr.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s2306_evttsvaltcontr_dados['tpamb'] = evtTSVAltContr.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s2306_evttsvaltcontr_dados['procemi'] = evtTSVAltContr.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s2306_evttsvaltcontr_dados['verproc'] = evtTSVAltContr.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s2306_evttsvaltcontr_dados['tpinsc'] = evtTSVAltContr.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s2306_evttsvaltcontr_dados['nrinsc'] = evtTSVAltContr.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s2306_evttsvaltcontr_dados['cpftrab'] = evtTSVAltContr.ideTrabSemVinculo.cpfTrab.cdata
    except AttributeError: pass
    try: s2306_evttsvaltcontr_dados['nistrab'] = evtTSVAltContr.ideTrabSemVinculo.nisTrab.cdata
    except AttributeError: pass
    try: s2306_evttsvaltcontr_dados['codcateg'] = evtTSVAltContr.ideTrabSemVinculo.codCateg.cdata
    except AttributeError: pass
    try: s2306_evttsvaltcontr_dados['dtalteracao'] = evtTSVAltContr.infoTSVAlteracao.dtAlteracao.cdata
    except AttributeError: pass
    try: s2306_evttsvaltcontr_dados['natatividade'] = evtTSVAltContr.infoTSVAlteracao.natAtividade.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtTSVAltContr.infoTSVAlteracao): s2306_evttsvaltcontr_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTSVAltContr.infoTSVAlteracao): s2306_evttsvaltcontr_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTSVAltContr.infoTSVAlteracao): s2306_evttsvaltcontr_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2306_evttsvaltcontr', s2306_evttsvaltcontr_dados)
    resp = executar_sql(insert, True)
    s2306_evttsvaltcontr_id = resp[0][0]
    dados = s2306_evttsvaltcontr_dados
    dados['evento'] = 's2306'
    dados['id'] = s2306_evttsvaltcontr_id
    dados['identidade_evento'] = doc.eSocial.evtTSVAltContr['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'cargoFuncao' in dir(evtTSVAltContr.infoTSVAlteracao.infoComplementares) and evtTSVAltContr.infoTSVAlteracao.infoComplementares.cargoFuncao.cdata != '':
        for cargoFuncao in evtTSVAltContr.infoTSVAlteracao.infoComplementares.cargoFuncao:
            s2306_cargofuncao_dados = {}
            s2306_cargofuncao_dados['s2306_evttsvaltcontr_id'] = s2306_evttsvaltcontr_id

            try: s2306_cargofuncao_dados['codcargo'] = cargoFuncao.codCargo.cdata
            except AttributeError: pass
            try: s2306_cargofuncao_dados['codfuncao'] = cargoFuncao.codFuncao.cdata
            except AttributeError: pass
            insert = create_insert('s2306_cargofuncao', s2306_cargofuncao_dados)
            resp = executar_sql(insert, True)
            s2306_cargofuncao_id = resp[0][0]
            #print s2306_cargofuncao_id

    if 'remuneracao' in dir(evtTSVAltContr.infoTSVAlteracao.infoComplementares) and evtTSVAltContr.infoTSVAlteracao.infoComplementares.remuneracao.cdata != '':
        for remuneracao in evtTSVAltContr.infoTSVAlteracao.infoComplementares.remuneracao:
            s2306_remuneracao_dados = {}
            s2306_remuneracao_dados['s2306_evttsvaltcontr_id'] = s2306_evttsvaltcontr_id

            try: s2306_remuneracao_dados['vrsalfx'] = remuneracao.vrSalFx.cdata
            except AttributeError: pass
            try: s2306_remuneracao_dados['undsalfixo'] = remuneracao.undSalFixo.cdata
            except AttributeError: pass
            try: s2306_remuneracao_dados['dscsalvar'] = remuneracao.dscSalVar.cdata
            except AttributeError: pass
            insert = create_insert('s2306_remuneracao', s2306_remuneracao_dados)
            resp = executar_sql(insert, True)
            s2306_remuneracao_id = resp[0][0]
            #print s2306_remuneracao_id

    if 'infoTrabCedido' in dir(evtTSVAltContr.infoTSVAlteracao.infoComplementares) and evtTSVAltContr.infoTSVAlteracao.infoComplementares.infoTrabCedido.cdata != '':
        for infoTrabCedido in evtTSVAltContr.infoTSVAlteracao.infoComplementares.infoTrabCedido:
            s2306_infotrabcedido_dados = {}
            s2306_infotrabcedido_dados['s2306_evttsvaltcontr_id'] = s2306_evttsvaltcontr_id

            try: s2306_infotrabcedido_dados['indremuncargo'] = infoTrabCedido.indRemunCargo.cdata
            except AttributeError: pass
            insert = create_insert('s2306_infotrabcedido', s2306_infotrabcedido_dados)
            resp = executar_sql(insert, True)
            s2306_infotrabcedido_id = resp[0][0]
            #print s2306_infotrabcedido_id

    if 'infoEstagiario' in dir(evtTSVAltContr.infoTSVAlteracao.infoComplementares) and evtTSVAltContr.infoTSVAlteracao.infoComplementares.infoEstagiario.cdata != '':
        for infoEstagiario in evtTSVAltContr.infoTSVAlteracao.infoComplementares.infoEstagiario:
            s2306_infoestagiario_dados = {}
            s2306_infoestagiario_dados['s2306_evttsvaltcontr_id'] = s2306_evttsvaltcontr_id

            try: s2306_infoestagiario_dados['natestagio'] = infoEstagiario.natEstagio.cdata
            except AttributeError: pass
            try: s2306_infoestagiario_dados['nivestagio'] = infoEstagiario.nivEstagio.cdata
            except AttributeError: pass
            try: s2306_infoestagiario_dados['areaatuacao'] = infoEstagiario.areaAtuacao.cdata
            except AttributeError: pass
            try: s2306_infoestagiario_dados['nrapol'] = infoEstagiario.nrApol.cdata
            except AttributeError: pass
            try: s2306_infoestagiario_dados['vlrbolsa'] = infoEstagiario.vlrBolsa.cdata
            except AttributeError: pass
            try: s2306_infoestagiario_dados['dtprevterm'] = infoEstagiario.dtPrevTerm.cdata
            except AttributeError: pass
            try: s2306_infoestagiario_dados['cnpjinstensino'] = infoEstagiario.instEnsino.cnpjInstEnsino.cdata
            except AttributeError: pass
            try: s2306_infoestagiario_dados['nmrazao'] = infoEstagiario.instEnsino.nmRazao.cdata
            except AttributeError: pass
            try: s2306_infoestagiario_dados['dsclograd'] = infoEstagiario.instEnsino.dscLograd.cdata
            except AttributeError: pass
            try: s2306_infoestagiario_dados['nrlograd'] = infoEstagiario.instEnsino.nrLograd.cdata
            except AttributeError: pass
            try: s2306_infoestagiario_dados['bairro'] = infoEstagiario.instEnsino.bairro.cdata
            except AttributeError: pass
            try: s2306_infoestagiario_dados['cep'] = infoEstagiario.instEnsino.cep.cdata
            except AttributeError: pass
            try: s2306_infoestagiario_dados['codmunic'] = infoEstagiario.instEnsino.codMunic.cdata
            except AttributeError: pass
            try: s2306_infoestagiario_dados['uf'] = infoEstagiario.instEnsino.uf.cdata
            except AttributeError: pass
            insert = create_insert('s2306_infoestagiario', s2306_infoestagiario_dados)
            resp = executar_sql(insert, True)
            s2306_infoestagiario_id = resp[0][0]
            #print s2306_infoestagiario_id

            if 'ageIntegracao' in dir(infoEstagiario) and infoEstagiario.ageIntegracao.cdata != '':
                for ageIntegracao in infoEstagiario.ageIntegracao:
                    s2306_ageintegracao_dados = {}
                    s2306_ageintegracao_dados['s2306_infoestagiario_id'] = s2306_infoestagiario_id

                    try: s2306_ageintegracao_dados['cnpjagntinteg'] = ageIntegracao.cnpjAgntInteg.cdata
                    except AttributeError: pass
                    try: s2306_ageintegracao_dados['nmrazao'] = ageIntegracao.nmRazao.cdata
                    except AttributeError: pass
                    try: s2306_ageintegracao_dados['dsclograd'] = ageIntegracao.dscLograd.cdata
                    except AttributeError: pass
                    try: s2306_ageintegracao_dados['nrlograd'] = ageIntegracao.nrLograd.cdata
                    except AttributeError: pass
                    try: s2306_ageintegracao_dados['bairro'] = ageIntegracao.bairro.cdata
                    except AttributeError: pass
                    try: s2306_ageintegracao_dados['cep'] = ageIntegracao.cep.cdata
                    except AttributeError: pass
                    try: s2306_ageintegracao_dados['codmunic'] = ageIntegracao.codMunic.cdata
                    except AttributeError: pass
                    try: s2306_ageintegracao_dados['uf'] = ageIntegracao.uf.cdata
                    except AttributeError: pass
                    insert = create_insert('s2306_ageintegracao', s2306_ageintegracao_dados)
                    resp = executar_sql(insert, True)
                    s2306_ageintegracao_id = resp[0][0]
                    #print s2306_ageintegracao_id

            if 'supervisorEstagio' in dir(infoEstagiario) and infoEstagiario.supervisorEstagio.cdata != '':
                for supervisorEstagio in infoEstagiario.supervisorEstagio:
                    s2306_supervisorestagio_dados = {}
                    s2306_supervisorestagio_dados['s2306_infoestagiario_id'] = s2306_infoestagiario_id

                    try: s2306_supervisorestagio_dados['cpfsupervisor'] = supervisorEstagio.cpfSupervisor.cdata
                    except AttributeError: pass
                    try: s2306_supervisorestagio_dados['nmsuperv'] = supervisorEstagio.nmSuperv.cdata
                    except AttributeError: pass
                    insert = create_insert('s2306_supervisorestagio', s2306_supervisorestagio_dados)
                    resp = executar_sql(insert, True)
                    s2306_supervisorestagio_id = resp[0][0]
                    #print s2306_supervisorestagio_id

    from emensageriapro.esocial.views.s2306_evttsvaltcontr_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2306_evttsvaltcontr_id, 'default')
    return dados