#coding:utf-8

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

import psycopg2
import datetime
import os
from django.contrib import messages
from emensageriapro.settings import BASE_DIR
from emensageriapro.padrao import executar_sql



def validacao_automatica_eventos():
    """ Validar Automaticamente os eventos com status 1 - Importado"""
    transmissor_lista = executar_sql("""
    SELECT id, evento, identidade, transmissor_lote_efdreinf_id, criado_em, 
           criado_por_id, modificado_em, modificado_por_id, excluido, grupo, 
           tabela, tabela_salvar, ordem, tpinsc, nrinsc, recibo_numero, 
           recibo_hash, url_recibo, processamento_codigo_resposta, processamento_descricao_resposta, 
           validacao_precedencia, validacoes, status
      FROM public.transmissor_eventos_efdreinf WHERE status=1;
    """, True)

    for a in lista:
        pass

    transmissor_lista = executar_sql("""
    SELECT id, evento, identidade, transmissor_lote_esocial_id, criado_em, 
           criado_por_id, modificado_em, modificado_por_id, excluido, grupo, 
           tabela, tabela_salvar, ordem, tpinsc, nrinsc, recibo_numero, 
           recibo_hash, url_recibo, processamento_codigo_resposta, processamento_descricao_resposta, 
           validacao_precedencia, validacoes, status
      FROM public.transmissor_eventos_esocial WHERE status=1;
    """, True)
    for a in lista:
        pass

if __name__ == "__main__":
    validacao_automatica_eventos()