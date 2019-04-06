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



def read_s2298_evtreintegr_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2298_evtreintegr_obj(doc, status, validar)
    return dados

def read_s2298_evtreintegr(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2298_evtreintegr_obj(doc, status, validar)
    return dados



def read_s2298_evtreintegr_obj(doc, status, validar=False):
    s2298_evtreintegr_dados = {}
    s2298_evtreintegr_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2298_evtreintegr_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2298_evtreintegr_dados['identidade'] = doc.eSocial.evtReintegr['Id']
    evtReintegr = doc.eSocial.evtReintegr

    try: s2298_evtreintegr_dados['indretif'] = evtReintegr.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s2298_evtreintegr_dados['nrrecibo'] = evtReintegr.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s2298_evtreintegr_dados['tpamb'] = evtReintegr.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s2298_evtreintegr_dados['procemi'] = evtReintegr.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s2298_evtreintegr_dados['verproc'] = evtReintegr.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s2298_evtreintegr_dados['tpinsc'] = evtReintegr.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s2298_evtreintegr_dados['nrinsc'] = evtReintegr.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s2298_evtreintegr_dados['cpftrab'] = evtReintegr.ideVinculo.cpfTrab.cdata
    except AttributeError: pass
    try: s2298_evtreintegr_dados['nistrab'] = evtReintegr.ideVinculo.nisTrab.cdata
    except AttributeError: pass
    try: s2298_evtreintegr_dados['matricula'] = evtReintegr.ideVinculo.matricula.cdata
    except AttributeError: pass
    try: s2298_evtreintegr_dados['tpreint'] = evtReintegr.infoReintegr.tpReint.cdata
    except AttributeError: pass
    try: s2298_evtreintegr_dados['nrprocjud'] = evtReintegr.infoReintegr.nrProcJud.cdata
    except AttributeError: pass
    try: s2298_evtreintegr_dados['nrleianistia'] = evtReintegr.infoReintegr.nrLeiAnistia.cdata
    except AttributeError: pass
    try: s2298_evtreintegr_dados['dtefetretorno'] = evtReintegr.infoReintegr.dtEfetRetorno.cdata
    except AttributeError: pass
    try: s2298_evtreintegr_dados['dtefeito'] = evtReintegr.infoReintegr.dtEfeito.cdata
    except AttributeError: pass
    try: s2298_evtreintegr_dados['indpagtojuizo'] = evtReintegr.infoReintegr.indPagtoJuizo.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['operacao'] = 1
    elif 'alteracao' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['operacao'] = 2
    elif 'exclusao' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2298_evtreintegr', s2298_evtreintegr_dados)
    resp = executar_sql(insert, True)
    s2298_evtreintegr_id = resp[0][0]
    dados = s2298_evtreintegr_dados
    dados['evento'] = 's2298'
    dados['id'] = s2298_evtreintegr_id
    dados['identidade_evento'] = doc.eSocial.evtReintegr['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    from emensageriapro.esocial.views.s2298_evtreintegr_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2298_evtreintegr_id, 'default')
    return dados