#coding: utf-8
import datetime

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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

class objectview(object):
    def __init__(self, d):
        self.__dict__ = d



def testar_importacao_xml(dicionario, chave, valor):
    try:
        dicionario[chave] = valor
    except:
        pass
    return dicionario


def salvar_arquivo(arquivo, texto):
    from emensageriapro.settings import BASE_DIR
    arquivo1 = BASE_DIR+'/'+arquivo
    file = open(arquivo1, "w")
    file.write( texto )
    file.close()
    #print arquivo


def ler_arquivo(arquivo):
    from emensageriapro.settings import BASE_DIR
    arquivo = BASE_DIR+'/'+arquivo
    file = open(arquivo, 'r')
    texto = file.read()
    file.close()
    return texto


def range_ano_mes():
    from datetime import datetime
    anos = range(2010,datetime.now().year+1)
    meses = ['01','02','03','04','05','06','07','08','09','10','11','12',]
    meses_ext = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez',]
    lista = []
    for a in anos: 
        for (m, me) in zip(meses, meses_ext): 
            lista.append( (str(a)+'-'+m, me+'/'+str(a)) )
    print lista


def listar_ids(objeto):
    lista = []
    for a in objeto:
        lista.append(a.id)
    return lista

    

def get_json(slug_conta):
    import json
    try:
        data = json.loads(ler_arquivo('emensageriapro/' + slug_conta + '.json'))
        retorno = objectview(data['contas'][0])
    except:
        retorno = None
    return retorno


def get_permissoes(permissoes):
    dict = {}
    for a in permissoes:
        chave = a.config_paginas.endereco
        dict[chave+'_listar'] = a.permite_listar
        dict[chave+'_cadastrar'] = a.permite_cadastrar
        dict[chave+'_editar'] = a.permite_editar
        dict[chave+'_visualizar'] = a.permite_visualizar
        dict[chave+'_apagar'] = a.permite_apagar    
    return dict


def json_to_dict(texto):
    import json
    dicionario = json.loads(texto)
    return dicionario


def dict_to_json(dicionario):
    import json
    json_string = json.dumps(dicionario)
    return json_string


def correcao_data_range(data):
    a = data.split('/')
    return a[2]+'-'+a[1]+'-'+a[0]


def texto_to_int_list(texto):
    dados = []
    lista = texto.split(',')
    for a in lista:
        dados.append(int(a))
    return dados


def get_hash_url(hash):
    import base64
    texto = base64.b64decode( hash )
    return json_to_dict(texto)


def disabled_form_fields(form, permite_editar):
    if not permite_editar:
        for a in form.fields:
            form.fields[a].widget.attrs['readonly'] = True
            form.fields[a].widget.attrs['disabled'] = True
    return form


def disabled_form_for_print(form):
    for a in form.fields:
        form.fields[a].widget.attrs['readonly'] = True
        form.fields[a].widget.attrs['disabled'] = True
    return form


def clear_dict_fields(dict):
    dict_new = {}
    for a in dict:
        if dict[a]:
            dict_new[a] = dict[a]
    for a in dict_new:
        if 'data' in a:
            b = dict_new[a]
            c = b.split(' - ')
            n1 = correcao_data_range(c[0])
            n2 = correcao_data_range(c[1])
            dict_new[a] = [n1, n2]
    return dict_new



def executar_sql(select, array):
    import psycopg2
    from emensageriapro.settings import DATABASES
    database = DATABASES['default']
    try:
        conn = psycopg2.connect("user='%(USER)s' host='%(HOST)s' password='%(PASSWORD)s' dbname='%(NAME)s'" % database)
        conn.autocommit = True
    except:
        print "I am unable to connect to the database"
    if select:
        cur = conn.cursor()
        select = select.replace("'Null'", 'Null')
        cur.execute(select)
        if array: lista = cur.fetchall()
        else: lista = None
        cur.close()
        return lista
    else:
        return None


def gravar_auditoria(situacao_anterior, situacao_posterior, tabela, tabela_id, usuario_id, tipo):
    executar_sql("""
    INSERT INTO public.auditoria(
            tabela, identidade, situacao_anterior, situacao_posterior, 
            tipo, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido)
    VALUES ('%s', %s, '%s', '%s', 
            %s, now(), %s, now(), %s, False);
    """ % (tabela, tabela_id, situacao_anterior, situacao_posterior, tipo, usuario_id, usuario_id), False)


def create_insert(tabela, dados):
    variaveis = dados.keys()
    campos_numericos = executar_sql("""
        SELECT column_name FROM information_schema.columns 
        WHERE table_name ='%s' 
        AND data_type in ('numeric', 'integer');
        """ % tabela, True)
    campos_numericos_lista = []
    for a in campos_numericos:
        campos_numericos_lista.append(a[0])
    valores = ''
    for a in variaveis:
        if dados[a] or dados[a] == 0:
            if (a in campos_numericos_lista):
                valores += "%s, " % str(dados[a]).replace('.','').replace(',','.')
            else:
                valores += "'%s', " % dados[a]
        else:
            valores += "Null, "
    texto = "INSERT INTO public.%s (%s, criado_em, criado_por_id, excluido) VALUES (%s now(), 1, False) RETURNING id;" % (tabela, ', '.join(variaveis), valores)
    return texto

