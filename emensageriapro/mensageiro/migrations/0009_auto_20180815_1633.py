# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0008_auto_20180812_1257'),
    ]

    operations = [
        migrations.RunSQL("""
CREATE OR REPLACE VIEW transmissor_eventos_esocial_totalizacoes AS
SELECT id, 's5001' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's5001_evtbasestrab' as tabela, 's5001_evtbasestrab_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, recibo_numero, recibo_hash, 's5001_evtbasestrab_recibo' as url_recibo, processamento_codigo_resposta, processamento_descricao_resposta FROM public.s5001_evtbasestrab WHERE excluido=False UNION
SELECT id, 's5002' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's5002_evtirrfbenef' as tabela, 's5002_evtirrfbenef_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, recibo_numero, recibo_hash, 's5002_evtirrfbenef_recibo' as url_recibo, processamento_codigo_resposta, processamento_descricao_resposta FROM public.s5002_evtirrfbenef WHERE excluido=False UNION
SELECT id, 's5011' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's5011_evtcs' as tabela, 's5011_evtcs_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, recibo_numero, recibo_hash, 's5011_evtcs_recibo' as url_recibo, processamento_codigo_resposta, processamento_descricao_resposta FROM public.s5011_evtcs WHERE excluido=False UNION
SELECT id, 's5012' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's5012_evtirrf' as tabela, 's5012_evtirrf_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, recibo_numero, recibo_hash, 's5012_evtirrf_recibo' as url_recibo, processamento_codigo_resposta, processamento_descricao_resposta FROM public.s5012_evtirrf WHERE excluido=False;        
        
        """),
        migrations.RunSQL("""

CREATE OR REPLACE VIEW transmissor_eventos_efdreinf_totalizacoes AS
SELECT id, 'r5001' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 'r5001_evttotal' as tabela, 'r5001_evttotal_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, recibo_numero, recibo_hash, 'r5001_evttotal_recibo' as url_recibo, processamento_codigo_resposta, processamento_descricao_resposta FROM public.r5001_evttotal WHERE excluido=False UNION
SELECT id, 'r5011' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 'r5011_evttotalcontrib' as tabela, 'r5011_evttotalcontrib_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, recibo_numero, recibo_hash, 'r5011_evttotalcontrib_recibo' as url_recibo, processamento_codigo_resposta, processamento_descricao_resposta FROM public.r5011_evttotalcontrib WHERE excluido=False;        
        
        """),
    ]
