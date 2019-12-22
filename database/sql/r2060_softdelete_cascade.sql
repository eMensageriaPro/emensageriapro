-- eMensageriaAI --
UPDATE public.r2060_tipocod a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2060_evtcprb b
 WHERE a.r2060_evtcprb_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2060_tipoajuste a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2060_tipocod b
 WHERE a.r2060_tipocod_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2060_infoproc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2060_tipocod b
 WHERE a.r2060_tipocod_id = b.id AND b.ativo IS NULL AND a.ativo=True;

