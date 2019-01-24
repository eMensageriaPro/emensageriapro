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


def read_r1000_evtinfocontri_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_r1000_evtinfocontri_obj(doc, status, validar)
    return dados

def read_r1000_evtinfocontri(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_r1000_evtinfocontri_obj(doc, status, validar)
    return dados



def read_r1000_evtinfocontri_obj(doc, status, validar=False):
    r1000_evtinfocontri_dados = {}
    r1000_evtinfocontri_dados['status'] = status
    xmlns_lista = doc.Reinf['xmlns'].split('/')
    r1000_evtinfocontri_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r1000_evtinfocontri_dados['identidade'] = doc.Reinf.evtInfoContri['id']
    r1000_evtinfocontri_dados['processamento_codigo_resposta'] = 1
    evtInfoContri = doc.Reinf.evtInfoContri

    if 'tpAmb' in dir(evtInfoContri.ideEvento): r1000_evtinfocontri_dados['tpamb'] = evtInfoContri.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtInfoContri.ideEvento): r1000_evtinfocontri_dados['procemi'] = evtInfoContri.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtInfoContri.ideEvento): r1000_evtinfocontri_dados['verproc'] = evtInfoContri.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtInfoContri.ideContri): r1000_evtinfocontri_dados['tpinsc'] = evtInfoContri.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtInfoContri.ideContri): r1000_evtinfocontri_dados['nrinsc'] = evtInfoContri.ideContri.nrInsc.cdata
    if 'inclusao' in dir(evtInfoContri.infoContri): r1000_evtinfocontri_dados['operacao'] = 1
    elif 'alteracao' in dir(evtInfoContri.infoContri): r1000_evtinfocontri_dados['operacao'] = 2
    elif 'exclusao' in dir(evtInfoContri.infoContri): r1000_evtinfocontri_dados['operacao'] = 3
    #print dados
    insert = create_insert('r1000_evtinfocontri', r1000_evtinfocontri_dados)
    resp = executar_sql(insert, True)
    r1000_evtinfocontri_id = resp[0][0]
    dados = r1000_evtinfocontri_dados
    dados['evento'] = 'r1000'
    dados['id'] = r1000_evtinfocontri_id
    dados['identidade_evento'] = doc.Reinf.evtInfoContri['id']
    dados['status'] = 1

    if 'inclusao' in dir(evtInfoContri.infoContri):
        for inclusao in evtInfoContri.infoContri.inclusao:
            r1000_inclusao_dados = {}
            r1000_inclusao_dados['r1000_evtinfocontri_id'] = r1000_evtinfocontri_id

            if 'iniValid' in dir(inclusao.idePeriodo): r1000_inclusao_dados['inivalid'] = inclusao.idePeriodo.iniValid.cdata
            if 'fimValid' in dir(inclusao.idePeriodo): r1000_inclusao_dados['fimvalid'] = inclusao.idePeriodo.fimValid.cdata
            if 'classTrib' in dir(inclusao.infoCadastro): r1000_inclusao_dados['classtrib'] = inclusao.infoCadastro.classTrib.cdata
            if 'indEscrituracao' in dir(inclusao.infoCadastro): r1000_inclusao_dados['indescrituracao'] = inclusao.infoCadastro.indEscrituracao.cdata
            if 'indDesoneracao' in dir(inclusao.infoCadastro): r1000_inclusao_dados['inddesoneracao'] = inclusao.infoCadastro.indDesoneracao.cdata
            if 'indAcordoIsenMulta' in dir(inclusao.infoCadastro): r1000_inclusao_dados['indacordoisenmulta'] = inclusao.infoCadastro.indAcordoIsenMulta.cdata
            if 'indSitPJ' in dir(inclusao.infoCadastro): r1000_inclusao_dados['indsitpj'] = inclusao.infoCadastro.indSitPJ.cdata
            if 'nmCtt' in dir(inclusao.infoCadastro.contato): r1000_inclusao_dados['nmctt'] = inclusao.infoCadastro.contato.nmCtt.cdata
            if 'cpfCtt' in dir(inclusao.infoCadastro.contato): r1000_inclusao_dados['cpfctt'] = inclusao.infoCadastro.contato.cpfCtt.cdata
            if 'foneFixo' in dir(inclusao.infoCadastro.contato): r1000_inclusao_dados['fonefixo'] = inclusao.infoCadastro.contato.foneFixo.cdata
            if 'foneCel' in dir(inclusao.infoCadastro.contato): r1000_inclusao_dados['fonecel'] = inclusao.infoCadastro.contato.foneCel.cdata
            if 'email' in dir(inclusao.infoCadastro.contato): r1000_inclusao_dados['email'] = inclusao.infoCadastro.contato.email.cdata
            insert = create_insert('r1000_inclusao', r1000_inclusao_dados)
            resp = executar_sql(insert, True)
            r1000_inclusao_id = resp[0][0]
            #print r1000_inclusao_id

            if 'softHouse' in dir(inclusao.infoCadastro):
                for softHouse in inclusao.infoCadastro.softHouse:
                    r1000_inclusao_softhouse_dados = {}
                    r1000_inclusao_softhouse_dados['r1000_inclusao_id'] = r1000_inclusao_id

                    if 'cnpjSoftHouse' in dir(softHouse): r1000_inclusao_softhouse_dados['cnpjsofthouse'] = softHouse.cnpjSoftHouse.cdata
                    if 'nmRazao' in dir(softHouse): r1000_inclusao_softhouse_dados['nmrazao'] = softHouse.nmRazao.cdata
                    if 'nmCont' in dir(softHouse): r1000_inclusao_softhouse_dados['nmcont'] = softHouse.nmCont.cdata
                    if 'telefone' in dir(softHouse): r1000_inclusao_softhouse_dados['telefone'] = softHouse.telefone.cdata
                    if 'email' in dir(softHouse): r1000_inclusao_softhouse_dados['email'] = softHouse.email.cdata
                    insert = create_insert('r1000_inclusao_softhouse', r1000_inclusao_softhouse_dados)
                    resp = executar_sql(insert, True)
                    r1000_inclusao_softhouse_id = resp[0][0]
                    #print r1000_inclusao_softhouse_id

            if 'infoEFR' in dir(inclusao.infoCadastro):
                for infoEFR in inclusao.infoCadastro.infoEFR:
                    r1000_inclusao_infoefr_dados = {}
                    r1000_inclusao_infoefr_dados['r1000_inclusao_id'] = r1000_inclusao_id

                    if 'ideEFR' in dir(infoEFR): r1000_inclusao_infoefr_dados['ideefr'] = infoEFR.ideEFR.cdata
                    if 'cnpjEFR' in dir(infoEFR): r1000_inclusao_infoefr_dados['cnpjefr'] = infoEFR.cnpjEFR.cdata
                    insert = create_insert('r1000_inclusao_infoefr', r1000_inclusao_infoefr_dados)
                    resp = executar_sql(insert, True)
                    r1000_inclusao_infoefr_id = resp[0][0]
                    #print r1000_inclusao_infoefr_id

    if 'alteracao' in dir(evtInfoContri.infoContri):
        for alteracao in evtInfoContri.infoContri.alteracao:
            r1000_alteracao_dados = {}
            r1000_alteracao_dados['r1000_evtinfocontri_id'] = r1000_evtinfocontri_id

            if 'iniValid' in dir(alteracao.idePeriodo): r1000_alteracao_dados['inivalid'] = alteracao.idePeriodo.iniValid.cdata
            if 'fimValid' in dir(alteracao.idePeriodo): r1000_alteracao_dados['fimvalid'] = alteracao.idePeriodo.fimValid.cdata
            if 'classTrib' in dir(alteracao.infoCadastro): r1000_alteracao_dados['classtrib'] = alteracao.infoCadastro.classTrib.cdata
            if 'indEscrituracao' in dir(alteracao.infoCadastro): r1000_alteracao_dados['indescrituracao'] = alteracao.infoCadastro.indEscrituracao.cdata
            if 'indDesoneracao' in dir(alteracao.infoCadastro): r1000_alteracao_dados['inddesoneracao'] = alteracao.infoCadastro.indDesoneracao.cdata
            if 'indAcordoIsenMulta' in dir(alteracao.infoCadastro): r1000_alteracao_dados['indacordoisenmulta'] = alteracao.infoCadastro.indAcordoIsenMulta.cdata
            if 'indSitPJ' in dir(alteracao.infoCadastro): r1000_alteracao_dados['indsitpj'] = alteracao.infoCadastro.indSitPJ.cdata
            if 'nmCtt' in dir(alteracao.infoCadastro.contato): r1000_alteracao_dados['nmctt'] = alteracao.infoCadastro.contato.nmCtt.cdata
            if 'cpfCtt' in dir(alteracao.infoCadastro.contato): r1000_alteracao_dados['cpfctt'] = alteracao.infoCadastro.contato.cpfCtt.cdata
            if 'foneFixo' in dir(alteracao.infoCadastro.contato): r1000_alteracao_dados['fonefixo'] = alteracao.infoCadastro.contato.foneFixo.cdata
            if 'foneCel' in dir(alteracao.infoCadastro.contato): r1000_alteracao_dados['fonecel'] = alteracao.infoCadastro.contato.foneCel.cdata
            if 'email' in dir(alteracao.infoCadastro.contato): r1000_alteracao_dados['email'] = alteracao.infoCadastro.contato.email.cdata
            insert = create_insert('r1000_alteracao', r1000_alteracao_dados)
            resp = executar_sql(insert, True)
            r1000_alteracao_id = resp[0][0]
            #print r1000_alteracao_id

            if 'softHouse' in dir(alteracao.infoCadastro):
                for softHouse in alteracao.infoCadastro.softHouse:
                    r1000_alteracao_softhouse_dados = {}
                    r1000_alteracao_softhouse_dados['r1000_alteracao_id'] = r1000_alteracao_id

                    if 'cnpjSoftHouse' in dir(softHouse): r1000_alteracao_softhouse_dados['cnpjsofthouse'] = softHouse.cnpjSoftHouse.cdata
                    if 'nmRazao' in dir(softHouse): r1000_alteracao_softhouse_dados['nmrazao'] = softHouse.nmRazao.cdata
                    if 'nmCont' in dir(softHouse): r1000_alteracao_softhouse_dados['nmcont'] = softHouse.nmCont.cdata
                    if 'telefone' in dir(softHouse): r1000_alteracao_softhouse_dados['telefone'] = softHouse.telefone.cdata
                    if 'email' in dir(softHouse): r1000_alteracao_softhouse_dados['email'] = softHouse.email.cdata
                    insert = create_insert('r1000_alteracao_softhouse', r1000_alteracao_softhouse_dados)
                    resp = executar_sql(insert, True)
                    r1000_alteracao_softhouse_id = resp[0][0]
                    #print r1000_alteracao_softhouse_id

            if 'infoEFR' in dir(alteracao.infoCadastro):
                for infoEFR in alteracao.infoCadastro.infoEFR:
                    r1000_alteracao_infoefr_dados = {}
                    r1000_alteracao_infoefr_dados['r1000_alteracao_id'] = r1000_alteracao_id

                    if 'ideEFR' in dir(infoEFR): r1000_alteracao_infoefr_dados['ideefr'] = infoEFR.ideEFR.cdata
                    if 'cnpjEFR' in dir(infoEFR): r1000_alteracao_infoefr_dados['cnpjefr'] = infoEFR.cnpjEFR.cdata
                    insert = create_insert('r1000_alteracao_infoefr', r1000_alteracao_infoefr_dados)
                    resp = executar_sql(insert, True)
                    r1000_alteracao_infoefr_id = resp[0][0]
                    #print r1000_alteracao_infoefr_id

            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    r1000_alteracao_novavalidade_dados = {}
                    r1000_alteracao_novavalidade_dados['r1000_alteracao_id'] = r1000_alteracao_id

                    if 'iniValid' in dir(novaValidade): r1000_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    if 'fimValid' in dir(novaValidade): r1000_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    insert = create_insert('r1000_alteracao_novavalidade', r1000_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    r1000_alteracao_novavalidade_id = resp[0][0]
                    #print r1000_alteracao_novavalidade_id

    if 'exclusao' in dir(evtInfoContri.infoContri):
        for exclusao in evtInfoContri.infoContri.exclusao:
            r1000_exclusao_dados = {}
            r1000_exclusao_dados['r1000_evtinfocontri_id'] = r1000_evtinfocontri_id

            if 'iniValid' in dir(exclusao.idePeriodo): r1000_exclusao_dados['inivalid'] = exclusao.idePeriodo.iniValid.cdata
            if 'fimValid' in dir(exclusao.idePeriodo): r1000_exclusao_dados['fimvalid'] = exclusao.idePeriodo.fimValid.cdata
            insert = create_insert('r1000_exclusao', r1000_exclusao_dados)
            resp = executar_sql(insert, True)
            r1000_exclusao_id = resp[0][0]
            #print r1000_exclusao_id

    from emensageriapro.efdreinf.views.r1000_evtinfocontri_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r1000_evtinfocontri_id, 'default')
    return dados