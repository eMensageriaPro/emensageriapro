-- eMensageriaAI --
UPDATE public.s1250_tpaquis a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1250_evtaqprod b
 WHERE a.s1250_evtaqprod_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1250_ideprodutor a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1250_tpaquis b
 WHERE a.s1250_tpaquis_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1250_nfs a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1250_ideprodutor b
 WHERE a.s1250_ideprodutor_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1250_infoprocjud a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1250_ideprodutor b
 WHERE a.s1250_ideprodutor_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1250_infoprocj a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1250_tpaquis b
 WHERE a.s1250_tpaquis_id = b.id AND b.ativo IS NULL AND a.ativo=True;

