UPDATE public.r9012_regocorrs a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9012_evtretcons b
 WHERE a.r9012_evtretcons_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9012_infototalcontrib a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9012_evtretcons b
 WHERE a.r9012_evtretcons_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9012_totapurmen a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9012_infototalcontrib b
 WHERE a.r9012_infototalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9012_totapurqui a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9012_infototalcontrib b
 WHERE a.r9012_infototalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9012_totapurdec a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9012_infototalcontrib b
 WHERE a.r9012_infototalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9012_totapursem a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9012_infototalcontrib b
 WHERE a.r9012_infototalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9012_totapurdia a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9012_infototalcontrib b
 WHERE a.r9012_infototalcontrib_id = b.id AND b.ativo IS NULL AND a.ativo=True;

