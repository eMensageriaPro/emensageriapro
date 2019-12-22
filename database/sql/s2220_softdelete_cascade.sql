-- eMensageriaAI --
UPDATE public.s2220_exame a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2220_evtmonit b
 WHERE a.s2220_evtmonit_id = b.id AND b.ativo IS NULL AND a.ativo=True;

