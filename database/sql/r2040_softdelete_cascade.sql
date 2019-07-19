UPDATE public.r2040_recursosrep a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2040_evtassocdesprep b
 WHERE a.r2040_evtassocdesprep_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2040_inforecurso a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2040_recursosrep b
 WHERE a.r2040_recursosrep_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2040_infoproc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2040_recursosrep b
 WHERE a.r2040_recursosrep_id = b.id AND b.ativo IS NULL AND a.ativo=True;

