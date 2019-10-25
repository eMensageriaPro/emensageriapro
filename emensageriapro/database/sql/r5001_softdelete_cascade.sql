UPDATE public.r5001_regocorrs a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r5001_evttotal b
 WHERE a.r5001_evttotal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r5001_infototal a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r5001_evttotal b
 WHERE a.r5001_evttotal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r5001_rtom a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r5001_infototal b
 WHERE a.r5001_infototal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r5001_infocrtom a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r5001_rtom b
 WHERE a.r5001_rtom_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r5001_rprest a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r5001_infototal b
 WHERE a.r5001_infototal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r5001_rrecrepad a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r5001_infototal b
 WHERE a.r5001_infototal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r5001_rcoml a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r5001_infototal b
 WHERE a.r5001_infototal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r5001_rcprb a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r5001_infototal b
 WHERE a.r5001_infototal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r5001_rrecespetdesp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r5001_infototal b
 WHERE a.r5001_infototal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

