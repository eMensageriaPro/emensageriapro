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



def read_s3000_evtexclusao_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s3000_evtexclusao_obj(doc, status, validar)
    return dados

def read_s3000_evtexclusao(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s3000_evtexclusao_obj(doc, status, validar)
    return dados



def read_s3000_evtexclusao_obj(doc, status, validar=False):
    s3000_evtexclusao_dados = {}
    s3000_evtexclusao_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s3000_evtexclusao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s3000_evtexclusao_dados['identidade'] = doc.eSocial.evtExclusao['Id']
    evtExclusao = doc.eSocial.evtExclusao

    if 'tpAmb' in dir(evtExclusao.ideEvento): s3000_evtexclusao_dados['tpamb'] = evtExclusao.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtExclusao.ideEvento): s3000_evtexclusao_dados['procemi'] = evtExclusao.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtExclusao.ideEvento): s3000_evtexclusao_dados['verproc'] = evtExclusao.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtExclusao.ideEmpregador): s3000_evtexclusao_dados['tpinsc'] = evtExclusao.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtExclusao.ideEmpregador): s3000_evtexclusao_dados['nrinsc'] = evtExclusao.ideEmpregador.nrInsc.cdata
    if 'tpEvento' in dir(evtExclusao.infoExclusao): s3000_evtexclusao_dados['tpevento'] = evtExclusao.infoExclusao.tpEvento.cdata
    if 'nrRecEvt' in dir(evtExclusao.infoExclusao): s3000_evtexclusao_dados['nrrecevt'] = evtExclusao.infoExclusao.nrRecEvt.cdata
    if 'inclusao' in dir(evtExclusao.infoExclusao): s3000_evtexclusao_dados['operacao'] = 1
    elif 'alteracao' in dir(evtExclusao.infoExclusao): s3000_evtexclusao_dados['operacao'] = 2
    elif 'exclusao' in dir(evtExclusao.infoExclusao): s3000_evtexclusao_dados['operacao'] = 3
    #print dados
    insert = create_insert('s3000_evtexclusao', s3000_evtexclusao_dados)
    resp = executar_sql(insert, True)
    s3000_evtexclusao_id = resp[0][0]
    dados = s3000_evtexclusao_dados
    dados['evento'] = 's3000'
    dados['id'] = s3000_evtexclusao_id
    dados['identidade_evento'] = doc.eSocial.evtExclusao['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'ideTrabalhador' in dir(evtExclusao.infoExclusao):
        for ideTrabalhador in evtExclusao.infoExclusao.ideTrabalhador:
            s3000_idetrabalhador_dados = {}
            s3000_idetrabalhador_dados['s3000_evtexclusao_id'] = s3000_evtexclusao_id

            if 'cpfTrab' in dir(ideTrabalhador): s3000_idetrabalhador_dados['cpftrab'] = ideTrabalhador.cpfTrab.cdata
            if 'nisTrab' in dir(ideTrabalhador): s3000_idetrabalhador_dados['nistrab'] = ideTrabalhador.nisTrab.cdata
            insert = create_insert('s3000_idetrabalhador', s3000_idetrabalhador_dados)
            resp = executar_sql(insert, True)
            s3000_idetrabalhador_id = resp[0][0]
            #print s3000_idetrabalhador_id

    if 'ideFolhaPagto' in dir(evtExclusao.infoExclusao):
        for ideFolhaPagto in evtExclusao.infoExclusao.ideFolhaPagto:
            s3000_idefolhapagto_dados = {}
            s3000_idefolhapagto_dados['s3000_evtexclusao_id'] = s3000_evtexclusao_id

            if 'indApuracao' in dir(ideFolhaPagto): s3000_idefolhapagto_dados['indapuracao'] = ideFolhaPagto.indApuracao.cdata
            if 'perApur' in dir(ideFolhaPagto): s3000_idefolhapagto_dados['perapur'] = ideFolhaPagto.perApur.cdata
            insert = create_insert('s3000_idefolhapagto', s3000_idefolhapagto_dados)
            resp = executar_sql(insert, True)
            s3000_idefolhapagto_id = resp[0][0]
            #print s3000_idefolhapagto_id

    from emensageriapro.esocial.views.s3000_evtexclusao_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s3000_evtexclusao_id, 'default')
    return dados