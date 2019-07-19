UPDATE public.r9011_regocorrs a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9011_evttotalcontrib b
 WHERE a.r9011_evttotalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9011_infototalcontrib a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9011_evttotalcontrib b
 WHERE a.r9011_evttotalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9011_rtom a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9011_infototalcontrib b
 WHERE a.r9011_infototalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9011_infocrtom a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9011_rtom b
 WHERE a.r9011_rtom_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9011_rprest a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9011_infototalcontrib b
 WHERE a.r9011_infototalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9011_rrecrepad a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9011_infototalcontrib b
 WHERE a.r9011_infototalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9011_rcoml a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9011_infototalcontrib b
 WHERE a.r9011_infototalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9011_rcprb a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9011_infototalcontrib b
 WHERE a.r9011_infototalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

