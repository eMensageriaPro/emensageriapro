UPDATE public.s2206_infoceletista a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2206_evtaltcontratual b
 WHERE a.s2206_evtaltcontratual_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2206_trabtemp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2206_infoceletista b
 WHERE a.s2206_infoceletista_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2206_aprend a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2206_infoceletista b
 WHERE a.s2206_infoceletista_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2206_infoestatutario a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2206_evtaltcontratual b
 WHERE a.s2206_evtaltcontratual_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2206_localtrabgeral a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2206_evtaltcontratual b
 WHERE a.s2206_evtaltcontratual_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2206_localtrabdom a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2206_evtaltcontratual b
 WHERE a.s2206_evtaltcontratual_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2206_horcontratual a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2206_evtaltcontratual b
 WHERE a.s2206_evtaltcontratual_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2206_horario a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2206_horcontratual b
 WHERE a.s2206_horcontratual_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2206_filiacaosindical a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2206_evtaltcontratual b
 WHERE a.s2206_evtaltcontratual_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2206_alvarajudicial a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2206_evtaltcontratual b
 WHERE a.s2206_evtaltcontratual_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2206_observacoes a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2206_evtaltcontratual b
 WHERE a.s2206_evtaltcontratual_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2206_servpubl a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2206_evtaltcontratual b
 WHERE a.s2206_evtaltcontratual_id = b.id AND b.ativo IS NULL AND a.ativo=True;

