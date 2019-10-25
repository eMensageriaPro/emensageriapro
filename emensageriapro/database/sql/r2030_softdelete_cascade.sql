UPDATE public.r2030_recursosrec a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2030_evtassocdesprec b
 WHERE a.r2030_evtassocdesprec_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2030_inforecurso a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2030_recursosrec b
 WHERE a.r2030_recursosrec_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2030_infoproc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2030_recursosrec b
 WHERE a.r2030_recursosrec_id = b.id AND b.ativo IS NULL AND a.ativo=True;

