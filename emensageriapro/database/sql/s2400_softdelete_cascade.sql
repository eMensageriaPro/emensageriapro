UPDATE public.s2400_endereco a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2400_evtcdbenefin b
 WHERE a.s2400_evtcdbenefin_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2400_brasil a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2400_endereco b
 WHERE a.s2400_endereco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2400_exterior a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2400_endereco b
 WHERE a.s2400_endereco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2400_dependente a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2400_evtcdbenefin b
 WHERE a.s2400_evtcdbenefin_id = b.id AND b.ativo IS NULL AND a.ativo=True;

