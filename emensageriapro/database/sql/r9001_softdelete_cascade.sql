UPDATE public.r9001_regocorrs a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9001_evttotal b
 WHERE a.r9001_evttotal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9001_infototal a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9001_evttotal b
 WHERE a.r9001_evttotal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9001_rtom a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9001_infototal b
 WHERE a.r9001_infototal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9001_infocrtom a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9001_rtom b
 WHERE a.r9001_rtom_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9001_rprest a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9001_infototal b
 WHERE a.r9001_infototal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9001_rrecrepad a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9001_infototal b
 WHERE a.r9001_infototal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9001_rcoml a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9001_infototal b
 WHERE a.r9001_infototal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9001_rcprb a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9001_infototal b
 WHERE a.r9001_infototal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9001_rrecespetdesp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9001_infototal b
 WHERE a.r9001_infototal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

