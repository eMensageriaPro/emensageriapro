-- eMensageriaAI --
UPDATE public.s2299_observacoes a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_evtdeslig b
 WHERE a.s2299_evtdeslig_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_sucessaovinc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_evtdeslig b
 WHERE a.s2299_evtdeslig_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_transftit a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_evtdeslig b
 WHERE a.s2299_evtdeslig_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_mudancacpf a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_evtdeslig b
 WHERE a.s2299_evtdeslig_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_verbasresc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_evtdeslig b
 WHERE a.s2299_evtdeslig_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_dmdev a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_verbasresc b
 WHERE a.s2299_verbasresc_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infoperapur a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_dmdev b
 WHERE a.s2299_dmdev_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infoperapur_ideestablot a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_infoperapur b
 WHERE a.s2299_infoperapur_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infoperapur_detverbas a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_infoperapur_ideestablot b
 WHERE a.s2299_infoperapur_ideestablot_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infoperapur_infosaudecolet a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_infoperapur_ideestablot b
 WHERE a.s2299_infoperapur_ideestablot_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infoperapur_detoper a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_infoperapur_infosaudecolet b
 WHERE a.s2299_infoperapur_infosaudecolet_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infoperapur_detplano a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_infoperapur_detoper b
 WHERE a.s2299_infoperapur_detoper_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infoperapur_infoagnocivo a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_infoperapur_ideestablot b
 WHERE a.s2299_infoperapur_ideestablot_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infoperapur_infosimples a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_infoperapur_ideestablot b
 WHERE a.s2299_infoperapur_ideestablot_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infoperant a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_dmdev b
 WHERE a.s2299_dmdev_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infoperant_ideadc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_infoperant b
 WHERE a.s2299_infoperant_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infoperant_ideperiodo a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_infoperant_ideadc b
 WHERE a.s2299_infoperant_ideadc_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infoperant_ideestablot a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_infoperant_ideperiodo b
 WHERE a.s2299_infoperant_ideperiodo_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infoperant_detverbas a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_infoperant_ideestablot b
 WHERE a.s2299_infoperant_ideestablot_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infoperant_infoagnocivo a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_infoperant_ideestablot b
 WHERE a.s2299_infoperant_ideestablot_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infoperant_infosimples a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_infoperant_ideestablot b
 WHERE a.s2299_infoperant_ideestablot_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infotrabinterm a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_dmdev b
 WHERE a.s2299_dmdev_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infotrabinterm_procjudtrab a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_verbasresc b
 WHERE a.s2299_verbasresc_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infotrabinterm_infomv a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_verbasresc b
 WHERE a.s2299_verbasresc_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infotrabinterm_remunoutrempr a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_infotrabinterm_infomv b
 WHERE a.s2299_infotrabinterm_infomv_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infotrabinterm_proccs a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_verbasresc b
 WHERE a.s2299_verbasresc_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infotrabinterm_quarentena a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_evtdeslig b
 WHERE a.s2299_evtdeslig_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2299_infotrabinterm_consigfgts a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2299_evtdeslig b
 WHERE a.s2299_evtdeslig_id = b.id AND b.ativo IS NULL AND a.ativo=True;

