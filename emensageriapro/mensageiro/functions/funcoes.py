#coding:utf-8
import psycopg2
import datetime
import os
from django.contrib import messages
from emensageriapro.padrao import ler_arquivo, executar_sql

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

def testar_importacao_xml(dicionario, chave, valor):
    try:
        dicionario[chave] = valor
    except:
        pass
    return dicionario


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
        if dados[a] or dados[a] == 0 or dados[a] == '':
            if (a in campos_numericos_lista):
                valores += "%s, " % str(dados[a]).replace('.','').replace(',','.')
            else:
                valores += "'%s', " % dados[a]
        else:
            valores += "Null, "
    texto = "INSERT INTO public.%s (%s, criado_em, criado_por_id, ativo) VALUES (%s now(), 1, True) RETURNING id;" % (tabela, ', '.join(variaveis), valores)
    return texto