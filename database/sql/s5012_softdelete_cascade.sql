-- eMensageriaAI --
UPDATE public.s5012_infocrcontrib a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5012_evtirrf b
 WHERE a.s5012_evtirrf_id = b.id AND b.ativo IS NULL AND a.ativo=True;

