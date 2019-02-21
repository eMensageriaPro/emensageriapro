-- View: public.transmissor_eventos_esocial_totalizacoes

-- DROP VIEW public.transmissor_eventos_esocial_totalizacoes;

CREATE OR REPLACE VIEW public.transmissor_eventos_esocial_totalizacoes AS 
 SELECT s5001_evtbasestrab.id,
    's5001' AS evento,
    s5001_evtbasestrab.identidade,
    s5001_evtbasestrab.transmissor_lote_esocial_id,
    s5001_evtbasestrab.criado_em,
    s5001_evtbasestrab.criado_por_id,
    s5001_evtbasestrab.modificado_em,
    s5001_evtbasestrab.modificado_por_id,
    s5001_evtbasestrab.excluido,
    2 AS grupo,
    's5001_evtbasestrab' AS tabela,
    's5001_evtbasestrab_salvar' AS tabela_salvar,
    s5001_evtbasestrab.id AS ordem,
    s5001_evtbasestrab.tpinsc,
    s5001_evtbasestrab.nrinsc,
    s5001_evtbasestrab.recibo_numero,
    s5001_evtbasestrab.recibo_hash,
    's5001_evtbasestrab_recibo' AS url_recibo,
    s5001_evtbasestrab.processamento_codigo_resposta,
    s5001_evtbasestrab.processamento_descricao_resposta,
    s5001_evtbasestrab.validacao_precedencia,
    s5001_evtbasestrab.validacoes,
    s5001_evtbasestrab.status
   FROM s5001_evtbasestrab
  WHERE s5001_evtbasestrab.excluido = false;

