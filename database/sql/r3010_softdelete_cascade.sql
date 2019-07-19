UPDATE public.r3010_boletim a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r3010_evtespdesportivo b
 WHERE a.r3010_evtespdesportivo_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r3010_receitaingressos a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r3010_boletim b
 WHERE a.r3010_boletim_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r3010_outrasreceitas a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r3010_boletim b
 WHERE a.r3010_boletim_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r3010_infoproc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r3010_evtespdesportivo b
 WHERE a.r3010_evtespdesportivo_id = b.id AND b.ativo IS NULL AND a.ativo=True;

