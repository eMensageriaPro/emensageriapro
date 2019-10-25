UPDATE public.s2405_endereco a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2405_evtcdbenefalt b
 WHERE a.s2405_evtcdbenefalt_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2405_brasil a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2405_endereco b
 WHERE a.s2405_endereco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2405_exterior a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2405_endereco b
 WHERE a.s2405_endereco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2405_dependente a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2405_evtcdbenefalt b
 WHERE a.s2405_evtcdbenefalt_id = b.id AND b.ativo IS NULL AND a.ativo=True;

