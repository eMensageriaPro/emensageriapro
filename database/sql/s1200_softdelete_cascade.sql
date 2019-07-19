UPDATE public.s1200_infomv a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_evtremun b
 WHERE a.s1200_evtremun_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_remunoutrempr a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_infomv b
 WHERE a.s1200_infomv_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infocomplem a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_evtremun b
 WHERE a.s1200_evtremun_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_sucessaovinc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_infocomplem b
 WHERE a.s1200_infocomplem_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_procjudtrab a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_evtremun b
 WHERE a.s1200_evtremun_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infointerm a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_evtremun b
 WHERE a.s1200_evtremun_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_dmdev a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_evtremun b
 WHERE a.s1200_evtremun_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperapur a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_dmdev b
 WHERE a.s1200_dmdev_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperapur_ideestablot a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_infoperapur b
 WHERE a.s1200_infoperapur_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperapur_remunperapur a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_infoperapur_ideestablot b
 WHERE a.s1200_infoperapur_ideestablot_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperapur_itensremun a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_infoperapur_remunperapur b
 WHERE a.s1200_infoperapur_remunperapur_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperapur_infosaudecolet a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_infoperapur_remunperapur b
 WHERE a.s1200_infoperapur_remunperapur_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperapur_detoper a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_infoperapur_infosaudecolet b
 WHERE a.s1200_infoperapur_infosaudecolet_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperapur_detplano a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_infoperapur_detoper b
 WHERE a.s1200_infoperapur_detoper_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperapur_infoagnocivo a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_infoperapur_remunperapur b
 WHERE a.s1200_infoperapur_remunperapur_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperapur_infotrabinterm a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_infoperapur_remunperapur b
 WHERE a.s1200_infoperapur_remunperapur_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperant a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_dmdev b
 WHERE a.s1200_dmdev_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperant_ideadc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_infoperant b
 WHERE a.s1200_infoperant_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperant_ideperiodo a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_infoperant_ideadc b
 WHERE a.s1200_infoperant_ideadc_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperant_ideestablot a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_infoperant_ideperiodo b
 WHERE a.s1200_infoperant_ideperiodo_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperant_remunperant a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_infoperant_ideestablot b
 WHERE a.s1200_infoperant_ideestablot_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperant_itensremun a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_infoperant_remunperant b
 WHERE a.s1200_infoperant_remunperant_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperant_infoagnocivo a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_infoperant_remunperant b
 WHERE a.s1200_infoperant_remunperant_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperant_infotrabinterm a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_infoperant_remunperant b
 WHERE a.s1200_infoperant_remunperant_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1200_infoperant_infocomplcont a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1200_dmdev b
 WHERE a.s1200_dmdev_id = b.id AND b.ativo IS NULL AND a.ativo=True;

