-- eMensageriaAI --
UPDATE public.s1270_remunavnp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1270_evtcontratavnp b
 WHERE a.s1270_evtcontratavnp_id = b.id AND b.ativo IS NULL AND a.ativo=True;

