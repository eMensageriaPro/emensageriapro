#coding:utf-8
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