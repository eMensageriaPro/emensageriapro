# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0031_transmissoreventos'),
    ]

    operations = [
        migrations.RunSQL("DROP VIEW IF EXISTS transmissor_eventos_efdreinf;"),
        migrations.RunSQL("DROP VIEW IF EXISTS  transmissor_eventos_efdreinf_totalizacoes;"),
        migrations.RunSQL("""
CREATE OR REPLACE VIEW transmissor_eventos_efdreinf_totalizacoes AS
SELECT id, 'r5001' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 'r5001_evttotal' as tabela, 'r5001_evttotal_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 'r5001_evttotal_recibo' as url_recibo, validacao_precedencia, validacoes, status, ocorrencias FROM public.r5001_evttotal WHERE excluido=False UNION
SELECT id, 'r5011' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 'r5011_evttotalcontrib' as tabela, 'r5011_evttotalcontrib_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 'r5011_evttotalcontrib_recibo' as url_recibo, validacao_precedencia, validacoes, status, ocorrencias FROM public.r5011_evttotalcontrib WHERE excluido=False;       
        """),
        migrations.RunSQL("""
        
        CREATE OR REPLACE VIEW transmissor_eventos_efdreinf AS
SELECT id, 'r1000' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 1 as grupo, 'r1000_evtinfocontri' as tabela, 'r1000_evtinfocontri_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 'r1000_evtinfocontri_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_evttotal_id, retornos_evttotalcontrib_id, ocorrencias FROM public.r1000_evtinfocontri WHERE excluido=False UNION
SELECT id, 'r1070' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 1 as grupo, 'r1070_evttabprocesso' as tabela, 'r1070_evttabprocesso_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 'r1070_evttabprocesso_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_evttotal_id, retornos_evttotalcontrib_id, ocorrencias FROM public.r1070_evttabprocesso WHERE excluido=False UNION
SELECT id, 'r2010' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 'r2010_evtservtom' as tabela, 'r2010_evtservtom_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 'r2010_evtservtom_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_evttotal_id, retornos_evttotalcontrib_id, ocorrencias FROM public.r2010_evtservtom WHERE excluido=False UNION
SELECT id, 'r2020' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 'r2020_evtservprest' as tabela, 'r2020_evtservprest_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 'r2020_evtservprest_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_evttotal_id, retornos_evttotalcontrib_id, ocorrencias FROM public.r2020_evtservprest WHERE excluido=False UNION
SELECT id, 'r2030' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 'r2030_evtassocdesprec' as tabela, 'r2030_evtassocdesprec_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 'r2030_evtassocdesprec_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_evttotal_id, retornos_evttotalcontrib_id, ocorrencias FROM public.r2030_evtassocdesprec WHERE excluido=False UNION
SELECT id, 'r2040' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 'r2040_evtassocdesprep' as tabela, 'r2040_evtassocdesprep_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 'r2040_evtassocdesprep_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_evttotal_id, retornos_evttotalcontrib_id, ocorrencias FROM public.r2040_evtassocdesprep WHERE excluido=False UNION
SELECT id, 'r2050' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 'r2050_evtcomprod' as tabela, 'r2050_evtcomprod_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 'r2050_evtcomprod_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_evttotal_id, retornos_evttotalcontrib_id, ocorrencias FROM public.r2050_evtcomprod WHERE excluido=False UNION
SELECT id, 'r2060' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 'r2060_evtcprb' as tabela, 'r2060_evtcprb_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 'r2060_evtcprb_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_evttotal_id, retornos_evttotalcontrib_id, ocorrencias FROM public.r2060_evtcprb WHERE excluido=False UNION
SELECT id, 'r2070' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 'r2070_evtpgtosdivs' as tabela, 'r2070_evtpgtosdivs_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 'r2070_evtpgtosdivs_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_evttotal_id, retornos_evttotalcontrib_id, ocorrencias FROM public.r2070_evtpgtosdivs WHERE excluido=False UNION
SELECT id, 'r2098' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 'r2098_evtreabreevper' as tabela, 'r2098_evtreabreevper_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 'r2098_evtreabreevper_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_evttotal_id, retornos_evttotalcontrib_id, ocorrencias FROM public.r2098_evtreabreevper WHERE excluido=False UNION
SELECT id, 'r2099' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 'r2099_evtfechaevper' as tabela, 'r2099_evtfechaevper_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 'r2099_evtfechaevper_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_evttotal_id, retornos_evttotalcontrib_id, ocorrencias FROM public.r2099_evtfechaevper WHERE excluido=False UNION
SELECT id, 'r3010' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 'r3010_evtespdesportivo' as tabela, 'r3010_evtespdesportivo_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 'r3010_evtespdesportivo_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_evttotal_id, retornos_evttotalcontrib_id, ocorrencias FROM public.r3010_evtespdesportivo WHERE excluido=False UNION


SELECT id, 'r9000' as evento, identidade, transmissor_lote_efdreinf_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 'r9000_evtexclusao' as tabela, 'r9000_evtexclusao_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 'r9000_evtexclusao_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_evttotal_id, retornos_evttotalcontrib_id, ocorrencias FROM public.r9000_evtexclusao WHERE excluido=False;
        """),

    ]
