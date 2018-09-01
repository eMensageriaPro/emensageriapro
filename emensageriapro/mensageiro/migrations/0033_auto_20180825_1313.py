# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0032_auto_20180825_0039'),
    ]

    operations = [
    migrations.RunSQL("DROP VIEW transmissor_eventos_efdreinf_totalizacoes;"),

    migrations.RunSQL("""

CREATE OR REPLACE VIEW transmissor_eventos_efdreinf_totalizacoes AS
SELECT id, 'r5001' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 'r5001_evttotal' as tabela, 'r5001_evttotal_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 'r5001_evttotal_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_evttotal_id, retornos_evttotalcontrib_id, ocorrencias FROM public.r5001_evttotal WHERE excluido=False UNION
SELECT id, 'r5011' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 'r5011_evttotalcontrib' as tabela, 'r5011_evttotalcontrib_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 'r5011_evttotalcontrib_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_evttotal_id, retornos_evttotalcontrib_id, ocorrencias FROM public.r5011_evttotalcontrib WHERE excluido=False;
    	""")
    ]
