UPDATE public.s2410_infopenmorte a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2410_evtcdbenin b
 WHERE a.s2410_evtcdbenin_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2410_instpenmorte a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2410_infopenmorte b
 WHERE a.s2410_infopenmorte_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2410_homologtc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2410_evtcdbenin b
 WHERE a.s2410_evtcdbenin_id = b.id AND b.ativo IS NULL AND a.ativo=True;

