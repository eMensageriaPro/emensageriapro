-- eMensageriaAI --
UPDATE public.r2010_nfs a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2010_evtservtom b
 WHERE a.r2010_evtservtom_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2010_infotpserv a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2010_nfs b
 WHERE a.r2010_nfs_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2010_infoprocretpr a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2010_evtservtom b
 WHERE a.r2010_evtservtom_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2010_infoprocretad a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2010_evtservtom b
 WHERE a.r2010_evtservtom_id = b.id AND b.ativo IS NULL AND a.ativo=True;

