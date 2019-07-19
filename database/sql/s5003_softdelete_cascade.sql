UPDATE public.s5003_ideestablot a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5003_evtbasesfgts b
 WHERE a.s5003_evtbasesfgts_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5003_infotrabfgts a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5003_ideestablot b
 WHERE a.s5003_ideestablot_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5003_infobasefgts a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5003_infotrabfgts b
 WHERE a.s5003_infotrabfgts_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5003_baseperapur a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5003_infobasefgts b
 WHERE a.s5003_infobasefgts_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5003_infobaseperante a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5003_infobasefgts b
 WHERE a.s5003_infobasefgts_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5003_baseperante a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5003_infobaseperante b
 WHERE a.s5003_infobaseperante_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5003_infodpsfgts a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5003_evtbasesfgts b
 WHERE a.s5003_evtbasesfgts_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5003_infotrabdps a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5003_infodpsfgts b
 WHERE a.s5003_infodpsfgts_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5003_dpsperapur a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5003_infotrabdps b
 WHERE a.s5003_infotrabdps_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5003_infodpsperante a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5003_infotrabdps b
 WHERE a.s5003_infotrabdps_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5003_dpsperante a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5003_infodpsperante b
 WHERE a.s5003_infodpsperante_id = b.id AND b.ativo IS NULL AND a.ativo=True;

