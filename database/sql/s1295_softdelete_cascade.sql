-- eMensageriaAI --
UPDATE public.s1295_iderespinf a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1295_evttotconting b
 WHERE a.s1295_evttotconting_id = b.id AND b.ativo IS NULL AND a.ativo=True;

