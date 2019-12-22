-- eMensageriaAI --
UPDATE public.s2230_iniafastamento a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2230_evtafasttemp b
 WHERE a.s2230_evtafasttemp_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2230_infoatestado a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2230_iniafastamento b
 WHERE a.s2230_iniafastamento_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2230_emitente a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2230_infoatestado b
 WHERE a.s2230_infoatestado_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2230_infocessao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2230_iniafastamento b
 WHERE a.s2230_iniafastamento_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2230_infomandsind a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2230_iniafastamento b
 WHERE a.s2230_iniafastamento_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2230_inforetif a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2230_evtafasttemp b
 WHERE a.s2230_evtafasttemp_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2230_fimafastamento a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2230_evtafasttemp b
 WHERE a.s2230_evtafasttemp_id = b.id AND b.ativo IS NULL AND a.ativo=True;

