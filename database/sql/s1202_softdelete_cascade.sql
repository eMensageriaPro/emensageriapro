-- eMensageriaAI --
UPDATE public.s1202_procjudtrab a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1202_evtrmnrpps b
 WHERE a.s1202_evtrmnrpps_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1202_dmdev a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1202_evtrmnrpps b
 WHERE a.s1202_evtrmnrpps_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1202_infoperapur a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1202_dmdev b
 WHERE a.s1202_dmdev_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1202_infoperapur_ideestab a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1202_infoperapur b
 WHERE a.s1202_infoperapur_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1202_infoperapur_remunperapur a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1202_infoperapur_ideestab b
 WHERE a.s1202_infoperapur_ideestab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1202_infoperapur_itensremun a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1202_infoperapur_remunperapur b
 WHERE a.s1202_infoperapur_remunperapur_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1202_infoperapur_infosaudecolet a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1202_infoperapur_remunperapur b
 WHERE a.s1202_infoperapur_remunperapur_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1202_infoperapur_detoper a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1202_infoperapur_infosaudecolet b
 WHERE a.s1202_infoperapur_infosaudecolet_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1202_infoperapur_detplano a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1202_infoperapur_detoper b
 WHERE a.s1202_infoperapur_detoper_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1202_infoperant a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1202_dmdev b
 WHERE a.s1202_dmdev_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1202_infoperant_ideadc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1202_infoperant b
 WHERE a.s1202_infoperant_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1202_infoperant_ideperiodo a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1202_infoperant_ideadc b
 WHERE a.s1202_infoperant_ideadc_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1202_infoperant_ideestab a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1202_infoperant_ideperiodo b
 WHERE a.s1202_infoperant_ideperiodo_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1202_infoperant_remunperant a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1202_infoperant_ideestab b
 WHERE a.s1202_infoperant_ideestab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1202_infoperant_itensremun a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1202_infoperant_remunperant b
 WHERE a.s1202_infoperant_remunperant_id = b.id AND b.ativo IS NULL AND a.ativo=True;

