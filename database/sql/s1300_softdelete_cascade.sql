-- eMensageriaAI --
UPDATE public.s1300_contribsind a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1300_evtcontrsindpatr b
 WHERE a.s1300_evtcontrsindpatr_id = b.id AND b.ativo IS NULL AND a.ativo=True;

