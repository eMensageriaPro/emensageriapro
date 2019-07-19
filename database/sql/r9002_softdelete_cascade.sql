UPDATE public.r9002_regocorrs a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9002_evtret b
 WHERE a.r9002_evtret_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9002_infototal a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9002_evtret b
 WHERE a.r9002_evtret_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9002_totapurmen a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9002_infototal b
 WHERE a.r9002_infototal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9002_totapurqui a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9002_infototal b
 WHERE a.r9002_infototal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9002_totapurdec a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9002_infototal b
 WHERE a.r9002_infototal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9002_totapursem a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9002_infototal b
 WHERE a.r9002_infototal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r9002_totapurdia a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r9002_infototal b
 WHERE a.r9002_infototal_id = b.id AND b.ativo IS NULL AND a.ativo=True;

