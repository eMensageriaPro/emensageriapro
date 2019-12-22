-- eMensageriaAI --
UPDATE public.s2250_detavprevio a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2250_evtavprevio b
 WHERE a.s2250_evtavprevio_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2250_cancavprevio a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2250_evtavprevio b
 WHERE a.s2250_evtavprevio_id = b.id AND b.ativo IS NULL AND a.ativo=True;

