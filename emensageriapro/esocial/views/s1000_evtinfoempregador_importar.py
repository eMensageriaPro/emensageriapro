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



def read_s1000_evtinfoempregador_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1000_evtinfoempregador_obj(doc, status, validar)
    return dados

def read_s1000_evtinfoempregador(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1000_evtinfoempregador_obj(doc, status, validar)
    return dados



def read_s1000_evtinfoempregador_obj(doc, status, validar=False):
    s1000_evtinfoempregador_dados = {}
    s1000_evtinfoempregador_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1000_evtinfoempregador_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1000_evtinfoempregador_dados['identidade'] = doc.eSocial.evtInfoEmpregador['Id']
    evtInfoEmpregador = doc.eSocial.evtInfoEmpregador

    try: s1000_evtinfoempregador_dados['tpamb'] = evtInfoEmpregador.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s1000_evtinfoempregador_dados['procemi'] = evtInfoEmpregador.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s1000_evtinfoempregador_dados['verproc'] = evtInfoEmpregador.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s1000_evtinfoempregador_dados['tpinsc'] = evtInfoEmpregador.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s1000_evtinfoempregador_dados['nrinsc'] = evtInfoEmpregador.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtInfoEmpregador.infoEmpregador): s1000_evtinfoempregador_dados['operacao'] = 1
    elif 'alteracao' in dir(evtInfoEmpregador.infoEmpregador): s1000_evtinfoempregador_dados['operacao'] = 2
    elif 'exclusao' in dir(evtInfoEmpregador.infoEmpregador): s1000_evtinfoempregador_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1000_evtinfoempregador', s1000_evtinfoempregador_dados)
    resp = executar_sql(insert, True)
    s1000_evtinfoempregador_id = resp[0][0]
    dados = s1000_evtinfoempregador_dados
    dados['evento'] = 's1000'
    dados['id'] = s1000_evtinfoempregador_id
    dados['identidade_evento'] = doc.eSocial.evtInfoEmpregador['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'inclusao' in dir(evtInfoEmpregador.infoEmpregador) and evtInfoEmpregador.infoEmpregador.inclusao.cdata != '':
        for inclusao in evtInfoEmpregador.infoEmpregador.inclusao:
            s1000_inclusao_dados = {}
            s1000_inclusao_dados['s1000_evtinfoempregador_id'] = s1000_evtinfoempregador_id

            try: s1000_inclusao_dados['inivalid'] = inclusao.idePeriodo.iniValid.cdata
            except AttributeError: pass
            try: s1000_inclusao_dados['fimvalid'] = inclusao.idePeriodo.fimValid.cdata
            except AttributeError: pass
            try: s1000_inclusao_dados['nmrazao'] = inclusao.infoCadastro.nmRazao.cdata
            except AttributeError: pass
            try: s1000_inclusao_dados['classtrib'] = inclusao.infoCadastro.classTrib.cdata
            except AttributeError: pass
            try: s1000_inclusao_dados['natjurid'] = inclusao.infoCadastro.natJurid.cdata
            except AttributeError: pass
            try: s1000_inclusao_dados['indcoop'] = inclusao.infoCadastro.indCoop.cdata
            except AttributeError: pass
            try: s1000_inclusao_dados['indconstr'] = inclusao.infoCadastro.indConstr.cdata
            except AttributeError: pass
            try: s1000_inclusao_dados['inddesfolha'] = inclusao.infoCadastro.indDesFolha.cdata
            except AttributeError: pass
            try: s1000_inclusao_dados['indopccp'] = inclusao.infoCadastro.indOpcCP.cdata
            except AttributeError: pass
            try: s1000_inclusao_dados['indoptregeletron'] = inclusao.infoCadastro.indOptRegEletron.cdata
            except AttributeError: pass
            try: s1000_inclusao_dados['indented'] = inclusao.infoCadastro.indEntEd.cdata
            except AttributeError: pass
            try: s1000_inclusao_dados['indett'] = inclusao.infoCadastro.indEtt.cdata
            except AttributeError: pass
            try: s1000_inclusao_dados['nrregett'] = inclusao.infoCadastro.nrRegEtt.cdata
            except AttributeError: pass
            try: s1000_inclusao_dados['nmctt'] = inclusao.infoCadastro.contato.nmCtt.cdata
            except AttributeError: pass
            try: s1000_inclusao_dados['cpfctt'] = inclusao.infoCadastro.contato.cpfCtt.cdata
            except AttributeError: pass
            try: s1000_inclusao_dados['fonefixo'] = inclusao.infoCadastro.contato.foneFixo.cdata
            except AttributeError: pass
            try: s1000_inclusao_dados['fonecel'] = inclusao.infoCadastro.contato.foneCel.cdata
            except AttributeError: pass
            try: s1000_inclusao_dados['email'] = inclusao.infoCadastro.contato.email.cdata
            except AttributeError: pass
            insert = create_insert('s1000_inclusao', s1000_inclusao_dados)
            resp = executar_sql(insert, True)
            s1000_inclusao_id = resp[0][0]
            #print s1000_inclusao_id

            if 'dadosIsencao' in dir(inclusao.infoCadastro) and inclusao.infoCadastro.dadosIsencao.cdata != '':
                for dadosIsencao in inclusao.infoCadastro.dadosIsencao:
                    s1000_inclusao_dadosisencao_dados = {}
                    s1000_inclusao_dadosisencao_dados['s1000_inclusao_id'] = s1000_inclusao_id

                    try: s1000_inclusao_dadosisencao_dados['ideminlei'] = dadosIsencao.ideMinLei.cdata
                    except AttributeError: pass
                    try: s1000_inclusao_dadosisencao_dados['nrcertif'] = dadosIsencao.nrCertif.cdata
                    except AttributeError: pass
                    try: s1000_inclusao_dadosisencao_dados['dtemiscertif'] = dadosIsencao.dtEmisCertif.cdata
                    except AttributeError: pass
                    try: s1000_inclusao_dadosisencao_dados['dtvenccertif'] = dadosIsencao.dtVencCertif.cdata
                    except AttributeError: pass
                    try: s1000_inclusao_dadosisencao_dados['nrprotrenov'] = dadosIsencao.nrProtRenov.cdata
                    except AttributeError: pass
                    try: s1000_inclusao_dadosisencao_dados['dtprotrenov'] = dadosIsencao.dtProtRenov.cdata
                    except AttributeError: pass
                    try: s1000_inclusao_dadosisencao_dados['dtdou'] = dadosIsencao.dtDou.cdata
                    except AttributeError: pass
                    try: s1000_inclusao_dadosisencao_dados['pagdou'] = dadosIsencao.pagDou.cdata
                    except AttributeError: pass
                    insert = create_insert('s1000_inclusao_dadosisencao', s1000_inclusao_dadosisencao_dados)
                    resp = executar_sql(insert, True)
                    s1000_inclusao_dadosisencao_id = resp[0][0]
                    #print s1000_inclusao_dadosisencao_id

            if 'infoOP' in dir(inclusao.infoCadastro) and inclusao.infoCadastro.infoOP.cdata != '':
                for infoOP in inclusao.infoCadastro.infoOP:
                    s1000_inclusao_infoop_dados = {}
                    s1000_inclusao_infoop_dados['s1000_inclusao_id'] = s1000_inclusao_id

                    try: s1000_inclusao_infoop_dados['nrsiafi'] = infoOP.nrSiafi.cdata
                    except AttributeError: pass
                    try: s1000_inclusao_infoop_dados['indugrpps'] = infoOP.indUGRPPS.cdata
                    except AttributeError: pass
                    try: s1000_inclusao_infoop_dados['esferaop'] = infoOP.esferaOP.cdata
                    except AttributeError: pass
                    try: s1000_inclusao_infoop_dados['poderop'] = infoOP.poderOP.cdata
                    except AttributeError: pass
                    try: s1000_inclusao_infoop_dados['vrtetorem'] = infoOP.vrTetoRem.cdata
                    except AttributeError: pass
                    try: s1000_inclusao_infoop_dados['ideefr'] = infoOP.ideEFR.cdata
                    except AttributeError: pass
                    try: s1000_inclusao_infoop_dados['cnpjefr'] = infoOP.cnpjEFR.cdata
                    except AttributeError: pass
                    insert = create_insert('s1000_inclusao_infoop', s1000_inclusao_infoop_dados)
                    resp = executar_sql(insert, True)
                    s1000_inclusao_infoop_id = resp[0][0]
                    #print s1000_inclusao_infoop_id

            if 'infoOrgInternacional' in dir(inclusao.infoCadastro) and inclusao.infoCadastro.infoOrgInternacional.cdata != '':
                for infoOrgInternacional in inclusao.infoCadastro.infoOrgInternacional:
                    s1000_inclusao_infoorginternacional_dados = {}
                    s1000_inclusao_infoorginternacional_dados['s1000_inclusao_id'] = s1000_inclusao_id

                    try: s1000_inclusao_infoorginternacional_dados['indacordoisenmulta'] = infoOrgInternacional.indAcordoIsenMulta.cdata
                    except AttributeError: pass
                    insert = create_insert('s1000_inclusao_infoorginternacional', s1000_inclusao_infoorginternacional_dados)
                    resp = executar_sql(insert, True)
                    s1000_inclusao_infoorginternacional_id = resp[0][0]
                    #print s1000_inclusao_infoorginternacional_id

            if 'softwareHouse' in dir(inclusao.infoCadastro) and inclusao.infoCadastro.softwareHouse.cdata != '':
                for softwareHouse in inclusao.infoCadastro.softwareHouse:
                    s1000_inclusao_softwarehouse_dados = {}
                    s1000_inclusao_softwarehouse_dados['s1000_inclusao_id'] = s1000_inclusao_id

                    try: s1000_inclusao_softwarehouse_dados['cnpjsofthouse'] = softwareHouse.cnpjSoftHouse.cdata
                    except AttributeError: pass
                    try: s1000_inclusao_softwarehouse_dados['nmrazao'] = softwareHouse.nmRazao.cdata
                    except AttributeError: pass
                    try: s1000_inclusao_softwarehouse_dados['nmcont'] = softwareHouse.nmCont.cdata
                    except AttributeError: pass
                    try: s1000_inclusao_softwarehouse_dados['telefone'] = softwareHouse.telefone.cdata
                    except AttributeError: pass
                    try: s1000_inclusao_softwarehouse_dados['email'] = softwareHouse.email.cdata
                    except AttributeError: pass
                    insert = create_insert('s1000_inclusao_softwarehouse', s1000_inclusao_softwarehouse_dados)
                    resp = executar_sql(insert, True)
                    s1000_inclusao_softwarehouse_id = resp[0][0]
                    #print s1000_inclusao_softwarehouse_id

            if 'situacaoPJ' in dir(inclusao.infoCadastro.infoComplementares) and inclusao.infoCadastro.infoComplementares.situacaoPJ.cdata != '':
                for situacaoPJ in inclusao.infoCadastro.infoComplementares.situacaoPJ:
                    s1000_inclusao_situacaopj_dados = {}
                    s1000_inclusao_situacaopj_dados['s1000_inclusao_id'] = s1000_inclusao_id

                    try: s1000_inclusao_situacaopj_dados['indsitpj'] = situacaoPJ.indSitPJ.cdata
                    except AttributeError: pass
                    insert = create_insert('s1000_inclusao_situacaopj', s1000_inclusao_situacaopj_dados)
                    resp = executar_sql(insert, True)
                    s1000_inclusao_situacaopj_id = resp[0][0]
                    #print s1000_inclusao_situacaopj_id

            if 'situacaoPF' in dir(inclusao.infoCadastro.infoComplementares) and inclusao.infoCadastro.infoComplementares.situacaoPF.cdata != '':
                for situacaoPF in inclusao.infoCadastro.infoComplementares.situacaoPF:
                    s1000_inclusao_situacaopf_dados = {}
                    s1000_inclusao_situacaopf_dados['s1000_inclusao_id'] = s1000_inclusao_id

                    try: s1000_inclusao_situacaopf_dados['indsitpf'] = situacaoPF.indSitPF.cdata
                    except AttributeError: pass
                    insert = create_insert('s1000_inclusao_situacaopf', s1000_inclusao_situacaopf_dados)
                    resp = executar_sql(insert, True)
                    s1000_inclusao_situacaopf_id = resp[0][0]
                    #print s1000_inclusao_situacaopf_id

    if 'alteracao' in dir(evtInfoEmpregador.infoEmpregador) and evtInfoEmpregador.infoEmpregador.alteracao.cdata != '':
        for alteracao in evtInfoEmpregador.infoEmpregador.alteracao:
            s1000_alteracao_dados = {}
            s1000_alteracao_dados['s1000_evtinfoempregador_id'] = s1000_evtinfoempregador_id

            try: s1000_alteracao_dados['inivalid'] = alteracao.idePeriodo.iniValid.cdata
            except AttributeError: pass
            try: s1000_alteracao_dados['fimvalid'] = alteracao.idePeriodo.fimValid.cdata
            except AttributeError: pass
            try: s1000_alteracao_dados['nmrazao'] = alteracao.infoCadastro.nmRazao.cdata
            except AttributeError: pass
            try: s1000_alteracao_dados['classtrib'] = alteracao.infoCadastro.classTrib.cdata
            except AttributeError: pass
            try: s1000_alteracao_dados['natjurid'] = alteracao.infoCadastro.natJurid.cdata
            except AttributeError: pass
            try: s1000_alteracao_dados['indcoop'] = alteracao.infoCadastro.indCoop.cdata
            except AttributeError: pass
            try: s1000_alteracao_dados['indconstr'] = alteracao.infoCadastro.indConstr.cdata
            except AttributeError: pass
            try: s1000_alteracao_dados['inddesfolha'] = alteracao.infoCadastro.indDesFolha.cdata
            except AttributeError: pass
            try: s1000_alteracao_dados['indopccp'] = alteracao.infoCadastro.indOpcCP.cdata
            except AttributeError: pass
            try: s1000_alteracao_dados['indoptregeletron'] = alteracao.infoCadastro.indOptRegEletron.cdata
            except AttributeError: pass
            try: s1000_alteracao_dados['indented'] = alteracao.infoCadastro.indEntEd.cdata
            except AttributeError: pass
            try: s1000_alteracao_dados['indett'] = alteracao.infoCadastro.indEtt.cdata
            except AttributeError: pass
            try: s1000_alteracao_dados['nrregett'] = alteracao.infoCadastro.nrRegEtt.cdata
            except AttributeError: pass
            try: s1000_alteracao_dados['nmctt'] = alteracao.infoCadastro.contato.nmCtt.cdata
            except AttributeError: pass
            try: s1000_alteracao_dados['cpfctt'] = alteracao.infoCadastro.contato.cpfCtt.cdata
            except AttributeError: pass
            try: s1000_alteracao_dados['fonefixo'] = alteracao.infoCadastro.contato.foneFixo.cdata
            except AttributeError: pass
            try: s1000_alteracao_dados['fonecel'] = alteracao.infoCadastro.contato.foneCel.cdata
            except AttributeError: pass
            try: s1000_alteracao_dados['email'] = alteracao.infoCadastro.contato.email.cdata
            except AttributeError: pass
            insert = create_insert('s1000_alteracao', s1000_alteracao_dados)
            resp = executar_sql(insert, True)
            s1000_alteracao_id = resp[0][0]
            #print s1000_alteracao_id

            if 'dadosIsencao' in dir(alteracao.infoCadastro) and alteracao.infoCadastro.dadosIsencao.cdata != '':
                for dadosIsencao in alteracao.infoCadastro.dadosIsencao:
                    s1000_alteracao_dadosisencao_dados = {}
                    s1000_alteracao_dadosisencao_dados['s1000_alteracao_id'] = s1000_alteracao_id

                    try: s1000_alteracao_dadosisencao_dados['ideminlei'] = dadosIsencao.ideMinLei.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_dadosisencao_dados['nrcertif'] = dadosIsencao.nrCertif.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_dadosisencao_dados['dtemiscertif'] = dadosIsencao.dtEmisCertif.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_dadosisencao_dados['dtvenccertif'] = dadosIsencao.dtVencCertif.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_dadosisencao_dados['nrprotrenov'] = dadosIsencao.nrProtRenov.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_dadosisencao_dados['dtprotrenov'] = dadosIsencao.dtProtRenov.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_dadosisencao_dados['dtdou'] = dadosIsencao.dtDou.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_dadosisencao_dados['pagdou'] = dadosIsencao.pagDou.cdata
                    except AttributeError: pass
                    insert = create_insert('s1000_alteracao_dadosisencao', s1000_alteracao_dadosisencao_dados)
                    resp = executar_sql(insert, True)
                    s1000_alteracao_dadosisencao_id = resp[0][0]
                    #print s1000_alteracao_dadosisencao_id

            if 'infoOP' in dir(alteracao.infoCadastro) and alteracao.infoCadastro.infoOP.cdata != '':
                for infoOP in alteracao.infoCadastro.infoOP:
                    s1000_alteracao_infoop_dados = {}
                    s1000_alteracao_infoop_dados['s1000_alteracao_id'] = s1000_alteracao_id

                    try: s1000_alteracao_infoop_dados['nrsiafi'] = infoOP.nrSiafi.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_infoop_dados['indugrpps'] = infoOP.indUGRPPS.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_infoop_dados['esferaop'] = infoOP.esferaOP.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_infoop_dados['poderop'] = infoOP.poderOP.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_infoop_dados['vrtetorem'] = infoOP.vrTetoRem.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_infoop_dados['ideefr'] = infoOP.ideEFR.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_infoop_dados['cnpjefr'] = infoOP.cnpjEFR.cdata
                    except AttributeError: pass
                    insert = create_insert('s1000_alteracao_infoop', s1000_alteracao_infoop_dados)
                    resp = executar_sql(insert, True)
                    s1000_alteracao_infoop_id = resp[0][0]
                    #print s1000_alteracao_infoop_id

            if 'infoOrgInternacional' in dir(alteracao.infoCadastro) and alteracao.infoCadastro.infoOrgInternacional.cdata != '':
                for infoOrgInternacional in alteracao.infoCadastro.infoOrgInternacional:
                    s1000_alteracao_infoorginternacional_dados = {}
                    s1000_alteracao_infoorginternacional_dados['s1000_alteracao_id'] = s1000_alteracao_id

                    try: s1000_alteracao_infoorginternacional_dados['indacordoisenmulta'] = infoOrgInternacional.indAcordoIsenMulta.cdata
                    except AttributeError: pass
                    insert = create_insert('s1000_alteracao_infoorginternacional', s1000_alteracao_infoorginternacional_dados)
                    resp = executar_sql(insert, True)
                    s1000_alteracao_infoorginternacional_id = resp[0][0]
                    #print s1000_alteracao_infoorginternacional_id

            if 'softwareHouse' in dir(alteracao.infoCadastro) and alteracao.infoCadastro.softwareHouse.cdata != '':
                for softwareHouse in alteracao.infoCadastro.softwareHouse:
                    s1000_alteracao_softwarehouse_dados = {}
                    s1000_alteracao_softwarehouse_dados['s1000_alteracao_id'] = s1000_alteracao_id

                    try: s1000_alteracao_softwarehouse_dados['cnpjsofthouse'] = softwareHouse.cnpjSoftHouse.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_softwarehouse_dados['nmrazao'] = softwareHouse.nmRazao.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_softwarehouse_dados['nmcont'] = softwareHouse.nmCont.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_softwarehouse_dados['telefone'] = softwareHouse.telefone.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_softwarehouse_dados['email'] = softwareHouse.email.cdata
                    except AttributeError: pass
                    insert = create_insert('s1000_alteracao_softwarehouse', s1000_alteracao_softwarehouse_dados)
                    resp = executar_sql(insert, True)
                    s1000_alteracao_softwarehouse_id = resp[0][0]
                    #print s1000_alteracao_softwarehouse_id

            if 'situacaoPJ' in dir(alteracao.infoCadastro.infoComplementares) and alteracao.infoCadastro.infoComplementares.situacaoPJ.cdata != '':
                for situacaoPJ in alteracao.infoCadastro.infoComplementares.situacaoPJ:
                    s1000_alteracao_situacaopj_dados = {}
                    s1000_alteracao_situacaopj_dados['s1000_alteracao_id'] = s1000_alteracao_id

                    try: s1000_alteracao_situacaopj_dados['indsitpj'] = situacaoPJ.indSitPJ.cdata
                    except AttributeError: pass
                    insert = create_insert('s1000_alteracao_situacaopj', s1000_alteracao_situacaopj_dados)
                    resp = executar_sql(insert, True)
                    s1000_alteracao_situacaopj_id = resp[0][0]
                    #print s1000_alteracao_situacaopj_id

            if 'situacaoPF' in dir(alteracao.infoCadastro.infoComplementares) and alteracao.infoCadastro.infoComplementares.situacaoPF.cdata != '':
                for situacaoPF in alteracao.infoCadastro.infoComplementares.situacaoPF:
                    s1000_alteracao_situacaopf_dados = {}
                    s1000_alteracao_situacaopf_dados['s1000_alteracao_id'] = s1000_alteracao_id

                    try: s1000_alteracao_situacaopf_dados['indsitpf'] = situacaoPF.indSitPF.cdata
                    except AttributeError: pass
                    insert = create_insert('s1000_alteracao_situacaopf', s1000_alteracao_situacaopf_dados)
                    resp = executar_sql(insert, True)
                    s1000_alteracao_situacaopf_id = resp[0][0]
                    #print s1000_alteracao_situacaopf_id

            if 'novaValidade' in dir(alteracao) and alteracao.novaValidade.cdata != '':
                for novaValidade in alteracao.novaValidade:
                    s1000_alteracao_novavalidade_dados = {}
                    s1000_alteracao_novavalidade_dados['s1000_alteracao_id'] = s1000_alteracao_id

                    try: s1000_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError: pass
                    try: s1000_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError: pass
                    insert = create_insert('s1000_alteracao_novavalidade', s1000_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1000_alteracao_novavalidade_id = resp[0][0]
                    #print s1000_alteracao_novavalidade_id

    if 'exclusao' in dir(evtInfoEmpregador.infoEmpregador) and evtInfoEmpregador.infoEmpregador.exclusao.cdata != '':
        for exclusao in evtInfoEmpregador.infoEmpregador.exclusao:
            s1000_exclusao_dados = {}
            s1000_exclusao_dados['s1000_evtinfoempregador_id'] = s1000_evtinfoempregador_id

            try: s1000_exclusao_dados['inivalid'] = exclusao.idePeriodo.iniValid.cdata
            except AttributeError: pass
            try: s1000_exclusao_dados['fimvalid'] = exclusao.idePeriodo.fimValid.cdata
            except AttributeError: pass
            insert = create_insert('s1000_exclusao', s1000_exclusao_dados)
            resp = executar_sql(insert, True)
            s1000_exclusao_id = resp[0][0]
            #print s1000_exclusao_id

    from emensageriapro.esocial.views.s1000_evtinfoempregador_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1000_evtinfoempregador_id, 'default')
    return dados