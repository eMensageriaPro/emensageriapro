-- eMensageriaAI --
UPDATE public.s1260_tpcomerc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1260_evtcomprod b
 WHERE a.s1260_evtcomprod_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1260_ideadquir a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1260_tpcomerc b
 WHERE a.s1260_tpcomerc_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1260_nfs a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1260_ideadquir b
 WHERE a.s1260_ideadquir_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1260_infoprocjud a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1260_tpcomerc b
 WHERE a.s1260_tpcomerc_id = b.id AND b.ativo IS NULL AND a.ativo=True;

