-- eMensageriaAI --
UPDATE public.s2245_ideprofresp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2245_evttreicap b
 WHERE a.s2245_evttreicap_id = b.id AND b.ativo IS NULL AND a.ativo=True;

