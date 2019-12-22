-- eMensageriaAI --
-- View: public.vw_transmissor_eventos_esocial_totalizacoes

DROP VIEW IF EXISTS public.vw_transmissor_eventos_esocial_totalizacoes;

CREATE OR REPLACE VIEW public.vw_transmissor_eventos_esocial_totalizacoes AS SELECT s5001_evtbasestrab.id,
    's5001' AS evento,
    s5001_evtbasestrab.identidade,
    s5001_evtbasestrab.transmissor_lote_esocial_id,
    s5001_evtbasestrab.criado_em,
    s5001_evtbasestrab.criado_por_id,
    s5001_evtbasestrab.modificado_em,
    s5001_evtbasestrab.modificado_por_id,
    s5001_evtbasestrab.desativado_em,
    s5001_evtbasestrab.desativado_por_id,
    s5001_evtbasestrab.ativo,
    4 AS grupo,
    's5001_evtbasestrab' AS tabela,
    's5001_evtbasestrab_salvar' AS tabela_salvar,
    s5001_evtbasestrab.id AS ordem,
    s5001_evtbasestrab.tpinsc,
    s5001_evtbasestrab.nrinsc,
    s5001_evtbasestrab.validacao_precedencia,
    s5001_evtbasestrab.validacoes,
    s5001_evtbasestrab.status
   FROM s5001_evtbasestrab
  WHERE s5001_evtbasestrab.ativo = true
 UNION
SELECT s5002_evtirrfbenef.id,
    's5002' AS evento,
    s5002_evtirrfbenef.identidade,
    s5002_evtirrfbenef.transmissor_lote_esocial_id,
    s5002_evtirrfbenef.criado_em,
    s5002_evtirrfbenef.criado_por_id,
    s5002_evtirrfbenef.modificado_em,
    s5002_evtirrfbenef.modificado_por_id,
    s5002_evtirrfbenef.desativado_em,
    s5002_evtirrfbenef.desativado_por_id,
    s5002_evtirrfbenef.ativo,
    4 AS grupo,
    's5002_evtirrfbenef' AS tabela,
    's5002_evtirrfbenef_salvar' AS tabela_salvar,
    s5002_evtirrfbenef.id AS ordem,
    s5002_evtirrfbenef.tpinsc,
    s5002_evtirrfbenef.nrinsc,
    s5002_evtirrfbenef.validacao_precedencia,
    s5002_evtirrfbenef.validacoes,
    s5002_evtirrfbenef.status
   FROM s5002_evtirrfbenef
  WHERE s5002_evtirrfbenef.ativo = true
 UNION
SELECT s5003_evtbasesfgts.id,
    's5003' AS evento,
    s5003_evtbasesfgts.identidade,
    s5003_evtbasesfgts.transmissor_lote_esocial_id,
    s5003_evtbasesfgts.criado_em,
    s5003_evtbasesfgts.criado_por_id,
    s5003_evtbasesfgts.modificado_em,
    s5003_evtbasesfgts.modificado_por_id,
    s5003_evtbasesfgts.desativado_em,
    s5003_evtbasesfgts.desativado_por_id,
    s5003_evtbasesfgts.ativo,
    4 AS grupo,
    's5003_evtbasesfgts' AS tabela,
    's5003_evtbasesfgts_salvar' AS tabela_salvar,
    s5003_evtbasesfgts.id AS ordem,
    s5003_evtbasesfgts.tpinsc,
    s5003_evtbasesfgts.nrinsc,
    s5003_evtbasesfgts.validacao_precedencia,
    s5003_evtbasesfgts.validacoes,
    s5003_evtbasesfgts.status
   FROM s5003_evtbasesfgts
  WHERE s5003_evtbasesfgts.ativo = true
 UNION
SELECT s5011_evtcs.id,
    's5011' AS evento,
    s5011_evtcs.identidade,
    s5011_evtcs.transmissor_lote_esocial_id,
    s5011_evtcs.criado_em,
    s5011_evtcs.criado_por_id,
    s5011_evtcs.modificado_em,
    s5011_evtcs.modificado_por_id,
    s5011_evtcs.desativado_em,
    s5011_evtcs.desativado_por_id,
    s5011_evtcs.ativo,
    4 AS grupo,
    's5011_evtcs' AS tabela,
    's5011_evtcs_salvar' AS tabela_salvar,
    s5011_evtcs.id AS ordem,
    s5011_evtcs.tpinsc,
    s5011_evtcs.nrinsc,
    s5011_evtcs.validacao_precedencia,
    s5011_evtcs.validacoes,
    s5011_evtcs.status
   FROM s5011_evtcs
  WHERE s5011_evtcs.ativo = true
 UNION
SELECT s5012_evtirrf.id,
    's5012' AS evento,
    s5012_evtirrf.identidade,
    s5012_evtirrf.transmissor_lote_esocial_id,
    s5012_evtirrf.criado_em,
    s5012_evtirrf.criado_por_id,
    s5012_evtirrf.modificado_em,
    s5012_evtirrf.modificado_por_id,
    s5012_evtirrf.desativado_em,
    s5012_evtirrf.desativado_por_id,
    s5012_evtirrf.ativo,
    4 AS grupo,
    's5012_evtirrf' AS tabela,
    's5012_evtirrf_salvar' AS tabela_salvar,
    s5012_evtirrf.id AS ordem,
    s5012_evtirrf.tpinsc,
    s5012_evtirrf.nrinsc,
    s5012_evtirrf.validacao_precedencia,
    s5012_evtirrf.validacoes,
    s5012_evtirrf.status
   FROM s5012_evtirrf
  WHERE s5012_evtirrf.ativo = true
 UNION
SELECT s5013_evtfgts.id,
    's5013' AS evento,
    s5013_evtfgts.identidade,
    s5013_evtfgts.transmissor_lote_esocial_id,
    s5013_evtfgts.criado_em,
    s5013_evtfgts.criado_por_id,
    s5013_evtfgts.modificado_em,
    s5013_evtfgts.modificado_por_id,
    s5013_evtfgts.desativado_em,
    s5013_evtfgts.desativado_por_id,
    s5013_evtfgts.ativo,
    4 AS grupo,
    's5013_evtfgts' AS tabela,
    's5013_evtfgts_salvar' AS tabela_salvar,
    s5013_evtfgts.id AS ordem,
    s5013_evtfgts.tpinsc,
    s5013_evtfgts.nrinsc,
    s5013_evtfgts.validacao_precedencia,
    s5013_evtfgts.validacoes,
    s5013_evtfgts.status
   FROM s5013_evtfgts
  WHERE s5013_evtfgts.ativo = true;