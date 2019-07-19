UPDATE public.s5013_infobasefgts a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5013_evtfgts b
 WHERE a.s5013_evtfgts_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5013_baseperapur a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5013_infobasefgts b
 WHERE a.s5013_infobasefgts_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5013_infobaseperante a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5013_infobasefgts b
 WHERE a.s5013_infobasefgts_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5013_baseperante a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5013_infobaseperante b
 WHERE a.s5013_infobaseperante_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5013_infodpsfgts a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5013_evtfgts b
 WHERE a.s5013_evtfgts_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5013_dpsperapur a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5013_infodpsfgts b
 WHERE a.s5013_infodpsfgts_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5013_infodpsperante a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5013_infodpsfgts b
 WHERE a.s5013_infodpsfgts_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5013_dpsperante a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5013_infodpsperante b
 WHERE a.s5013_infodpsperante_id = b.id AND b.ativo IS NULL AND a.ativo=True;

