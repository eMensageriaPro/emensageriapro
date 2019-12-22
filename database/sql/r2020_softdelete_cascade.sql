-- eMensageriaAI --
UPDATE public.r2020_nfs a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2020_evtservprest b
 WHERE a.r2020_evtservprest_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2020_infotpserv a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2020_nfs b
 WHERE a.r2020_nfs_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2020_infoprocretpr a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2020_evtservprest b
 WHERE a.r2020_evtservprest_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2020_infoprocretad a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2020_evtservprest b
 WHERE a.r2020_evtservprest_id = b.id AND b.ativo IS NULL AND a.ativo=True;

