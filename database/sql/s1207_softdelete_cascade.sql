-- eMensageriaAI --
UPDATE public.s1207_procjudtrab a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1207_evtbenprrp b
 WHERE a.s1207_evtbenprrp_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1207_dmdev a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1207_evtbenprrp b
 WHERE a.s1207_evtbenprrp_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1207_itens a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1207_dmdev b
 WHERE a.s1207_dmdev_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1207_infoperapur a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1207_dmdev b
 WHERE a.s1207_dmdev_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1207_infoperapur_ideestab a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1207_infoperapur b
 WHERE a.s1207_infoperapur_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1207_infoperapur_remunperapur a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1207_infoperapur_ideestab b
 WHERE a.s1207_infoperapur_ideestab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1207_infoperapur_itensremun a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1207_infoperapur_remunperapur b
 WHERE a.s1207_infoperapur_remunperapur_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1207_infoperant a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1207_dmdev b
 WHERE a.s1207_dmdev_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1207_infoperant_ideadc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1207_infoperant b
 WHERE a.s1207_infoperant_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1207_infoperant_ideperiodo a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1207_infoperant_ideadc b
 WHERE a.s1207_infoperant_ideadc_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1207_infoperant_ideestab a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1207_infoperant_ideperiodo b
 WHERE a.s1207_infoperant_ideperiodo_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1207_infoperant_remunperant a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1207_infoperant_ideestab b
 WHERE a.s1207_infoperant_ideestab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1207_infoperant_itensremun a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1207_infoperant_remunperant b
 WHERE a.s1207_infoperant_remunperant_id = b.id AND b.ativo IS NULL AND a.ativo=True;

