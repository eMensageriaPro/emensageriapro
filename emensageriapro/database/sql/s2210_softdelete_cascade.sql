UPDATE public.s2210_idelocalacid a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2210_evtcat b
 WHERE a.s2210_evtcat_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2210_parteatingida a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2210_evtcat b
 WHERE a.s2210_evtcat_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2210_agentecausador a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2210_evtcat b
 WHERE a.s2210_evtcat_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2210_atestado a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2210_evtcat b
 WHERE a.s2210_evtcat_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2210_catorigem a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2210_evtcat b
 WHERE a.s2210_evtcat_id = b.id AND b.ativo IS NULL AND a.ativo=True;

