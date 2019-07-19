UPDATE public.r2050_tipocom a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2050_evtcomprod b
 WHERE a.r2050_evtcomprod_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2050_infoproc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2050_tipocom b
 WHERE a.r2050_tipocom_id = b.id AND b.ativo IS NULL AND a.ativo=True;

