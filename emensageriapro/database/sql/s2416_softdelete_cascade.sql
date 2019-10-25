UPDATE public.s2416_infopenmorte a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2416_evtcdbenalt b
 WHERE a.s2416_evtcdbenalt_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2416_homologtc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2416_evtcdbenalt b
 WHERE a.s2416_evtcdbenalt_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2416_suspensao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2416_evtcdbenalt b
 WHERE a.s2416_evtcdbenalt_id = b.id AND b.ativo IS NULL AND a.ativo=True;

