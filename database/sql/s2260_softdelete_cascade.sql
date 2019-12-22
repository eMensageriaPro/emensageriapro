-- eMensageriaAI --
UPDATE public.s2260_localtrabinterm a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2260_evtconvinterm b
 WHERE a.s2260_evtconvinterm_id = b.id AND b.ativo IS NULL AND a.ativo=True;

