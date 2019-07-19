UPDATE public.s5002_infodep a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5002_evtirrfbenef b
 WHERE a.s5002_evtirrfbenef_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5002_infoirrf a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5002_evtirrfbenef b
 WHERE a.s5002_evtirrfbenef_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5002_basesirrf a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5002_infoirrf b
 WHERE a.s5002_infoirrf_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5002_irrf a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5002_infoirrf b
 WHERE a.s5002_infoirrf_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5002_idepgtoext a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5002_infoirrf b
 WHERE a.s5002_infoirrf_id = b.id AND b.ativo IS NULL AND a.ativo=True;

