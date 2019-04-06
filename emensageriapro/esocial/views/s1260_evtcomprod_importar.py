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



def read_s1260_evtcomprod_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1260_evtcomprod_obj(doc, status, validar)
    return dados

def read_s1260_evtcomprod(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1260_evtcomprod_obj(doc, status, validar)
    return dados



def read_s1260_evtcomprod_obj(doc, status, validar=False):
    s1260_evtcomprod_dados = {}
    s1260_evtcomprod_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1260_evtcomprod_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1260_evtcomprod_dados['identidade'] = doc.eSocial.evtComProd['Id']
    evtComProd = doc.eSocial.evtComProd

    try: s1260_evtcomprod_dados['indretif'] = evtComProd.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s1260_evtcomprod_dados['nrrecibo'] = evtComProd.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s1260_evtcomprod_dados['indapuracao'] = evtComProd.ideEvento.indApuracao.cdata
    except AttributeError: pass
    try: s1260_evtcomprod_dados['perapur'] = evtComProd.ideEvento.perApur.cdata
    except AttributeError: pass
    try: s1260_evtcomprod_dados['tpamb'] = evtComProd.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s1260_evtcomprod_dados['procemi'] = evtComProd.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s1260_evtcomprod_dados['verproc'] = evtComProd.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s1260_evtcomprod_dados['tpinsc'] = evtComProd.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s1260_evtcomprod_dados['nrinsc'] = evtComProd.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s1260_evtcomprod_dados['nrinscestabrural'] = evtComProd.infoComProd.ideEstabel.nrInscEstabRural.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtComProd.infoComProd): s1260_evtcomprod_dados['operacao'] = 1
    elif 'alteracao' in dir(evtComProd.infoComProd): s1260_evtcomprod_dados['operacao'] = 2
    elif 'exclusao' in dir(evtComProd.infoComProd): s1260_evtcomprod_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1260_evtcomprod', s1260_evtcomprod_dados)
    resp = executar_sql(insert, True)
    s1260_evtcomprod_id = resp[0][0]
    dados = s1260_evtcomprod_dados
    dados['evento'] = 's1260'
    dados['id'] = s1260_evtcomprod_id
    dados['identidade_evento'] = doc.eSocial.evtComProd['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'tpComerc' in dir(evtComProd.infoComProd.ideEstabel) and evtComProd.infoComProd.ideEstabel.tpComerc.cdata != '':
        for tpComerc in evtComProd.infoComProd.ideEstabel.tpComerc:
            s1260_tpcomerc_dados = {}
            s1260_tpcomerc_dados['s1260_evtcomprod_id'] = s1260_evtcomprod_id

            try: s1260_tpcomerc_dados['indcomerc'] = tpComerc.indComerc.cdata
            except AttributeError: pass
            try: s1260_tpcomerc_dados['vrtotcom'] = tpComerc.vrTotCom.cdata
            except AttributeError: pass
            insert = create_insert('s1260_tpcomerc', s1260_tpcomerc_dados)
            resp = executar_sql(insert, True)
            s1260_tpcomerc_id = resp[0][0]
            #print s1260_tpcomerc_id

            if 'ideAdquir' in dir(tpComerc) and tpComerc.ideAdquir.cdata != '':
                for ideAdquir in tpComerc.ideAdquir:
                    s1260_ideadquir_dados = {}
                    s1260_ideadquir_dados['s1260_tpcomerc_id'] = s1260_tpcomerc_id

                    try: s1260_ideadquir_dados['tpinsc'] = ideAdquir.tpInsc.cdata
                    except AttributeError: pass
                    try: s1260_ideadquir_dados['nrinsc'] = ideAdquir.nrInsc.cdata
                    except AttributeError: pass
                    try: s1260_ideadquir_dados['vrcomerc'] = ideAdquir.vrComerc.cdata
                    except AttributeError: pass
                    insert = create_insert('s1260_ideadquir', s1260_ideadquir_dados)
                    resp = executar_sql(insert, True)
                    s1260_ideadquir_id = resp[0][0]
                    #print s1260_ideadquir_id

            if 'infoProcJud' in dir(tpComerc) and tpComerc.infoProcJud.cdata != '':
                for infoProcJud in tpComerc.infoProcJud:
                    s1260_infoprocjud_dados = {}
                    s1260_infoprocjud_dados['s1260_tpcomerc_id'] = s1260_tpcomerc_id

                    try: s1260_infoprocjud_dados['tpproc'] = infoProcJud.tpProc.cdata
                    except AttributeError: pass
                    try: s1260_infoprocjud_dados['nrproc'] = infoProcJud.nrProc.cdata
                    except AttributeError: pass
                    try: s1260_infoprocjud_dados['codsusp'] = infoProcJud.codSusp.cdata
                    except AttributeError: pass
                    try: s1260_infoprocjud_dados['vrcpsusp'] = infoProcJud.vrCPSusp.cdata
                    except AttributeError: pass
                    try: s1260_infoprocjud_dados['vrratsusp'] = infoProcJud.vrRatSusp.cdata
                    except AttributeError: pass
                    try: s1260_infoprocjud_dados['vrsenarsusp'] = infoProcJud.vrSenarSusp.cdata
                    except AttributeError: pass
                    insert = create_insert('s1260_infoprocjud', s1260_infoprocjud_dados)
                    resp = executar_sql(insert, True)
                    s1260_infoprocjud_id = resp[0][0]
                    #print s1260_infoprocjud_id

    from emensageriapro.esocial.views.s1260_evtcomprod_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1260_evtcomprod_id, 'default')
    return dados