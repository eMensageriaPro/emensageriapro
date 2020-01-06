-- eMensageriaAI --
-- View: public.vw_transmissor_eventos_efdreinf_totalizacoes

DROP VIEW IF EXISTS public.vw_transmissor_eventos_efdreinf_totalizacoes;

CREATE OR REPLACE VIEW public.vw_transmissor_eventos_efdreinf_totalizacoes AS SELECT r5001_evttotal.id,
    'r5001'::text AS evento,
    r5001_evttotal.identidade,
    r5001_evttotal.transmissor_lote_efdreinf_id,
    r5001_evttotal.criado_em,
    r5001_evttotal.criado_por_id,
    r5001_evttotal.modificado_em,
    r5001_evttotal.modificado_por_id,
    r5001_evttotal.desativado_em,
    r5001_evttotal.desativado_por_id,
    r5001_evttotal.ativo,
    4 AS grupo,
    'r5001_evttotal'::text AS tabela,
    'r5001_evttotal_salvar'::text AS tabela_salvar,
    r5001_evttotal.id AS ordem,
    r5001_evttotal.tpinsc,
    r5001_evttotal.nrinsc,
    'r5001_evttotal_recibo'::text AS url_recibo,
    r5001_evttotal.validacao_precedencia,
    r5001_evttotal.validacoes,
    r5001_evttotal.status,
    r5001_evttotal.retorno_envio_json,
    r5001_evttotal.retorno_consulta_json,
    r5001_evttotal.evento_json,
    r5001_evttotal.ocorrencias_json

   FROM r5001_evttotal
  WHERE r5001_evttotal.ativo = true
 UNION
SELECT r5011_evttotalcontrib.id,
    'r5011'::text AS evento,
    r5011_evttotalcontrib.identidade,
    r5011_evttotalcontrib.transmissor_lote_efdreinf_id,
    r5011_evttotalcontrib.criado_em,
    r5011_evttotalcontrib.criado_por_id,
    r5011_evttotalcontrib.modificado_em,
    r5011_evttotalcontrib.modificado_por_id,
    r5011_evttotalcontrib.desativado_em,
    r5011_evttotalcontrib.desativado_por_id,
    r5011_evttotalcontrib.ativo,
    4 AS grupo,
    'r5011_evttotalcontrib'::text AS tabela,
    'r5011_evttotalcontrib_salvar'::text AS tabela_salvar,
    r5011_evttotalcontrib.id AS ordem,
    r5011_evttotalcontrib.tpinsc,
    r5011_evttotalcontrib.nrinsc,
    'r5011_evttotalcontrib_recibo'::text AS url_recibo,
    r5011_evttotalcontrib.validacao_precedencia,
    r5011_evttotalcontrib.validacoes,
    r5011_evttotalcontrib.status,
    r5011_evttotalcontrib.retorno_envio_json,
    r5011_evttotalcontrib.retorno_consulta_json,
    r5011_evttotalcontrib.evento_json,
    r5011_evttotalcontrib.ocorrencias_json

   FROM r5011_evttotalcontrib
  WHERE r5011_evttotalcontrib.ativo = true;