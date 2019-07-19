UPDATE public.r2099_iderespinf a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2099_evtfechaevper b
 WHERE a.r2099_evtfechaevper_id = b.id AND b.ativo IS NULL AND a.ativo=True;

