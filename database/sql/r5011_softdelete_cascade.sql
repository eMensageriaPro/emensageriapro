UPDATE public.r5011_regocorrs a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r5011_evttotalcontrib b
 WHERE a.r5011_evttotalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r5011_infototalcontrib a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r5011_evttotalcontrib b
 WHERE a.r5011_evttotalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r5011_rtom a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r5011_infototalcontrib b
 WHERE a.r5011_infototalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r5011_infocrtom a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r5011_rtom b
 WHERE a.r5011_rtom_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r5011_rprest a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r5011_infototalcontrib b
 WHERE a.r5011_infototalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r5011_rrecrepad a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r5011_infototalcontrib b
 WHERE a.r5011_infototalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r5011_rcoml a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r5011_infototalcontrib b
 WHERE a.r5011_infototalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r5011_rcprb a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r5011_infototalcontrib b
 WHERE a.r5011_infototalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

