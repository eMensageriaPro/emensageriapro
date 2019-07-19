UPDATE public.s2399_mudancacpf a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2399_evttsvtermino b
 WHERE a.s2399_evttsvtermino_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2399_verbasresc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2399_evttsvtermino b
 WHERE a.s2399_evttsvtermino_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2399_dmdev a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2399_verbasresc b
 WHERE a.s2399_verbasresc_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2399_ideestablot a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2399_dmdev b
 WHERE a.s2399_dmdev_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2399_detverbas a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2399_ideestablot b
 WHERE a.s2399_ideestablot_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2399_infosaudecolet a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2399_ideestablot b
 WHERE a.s2399_ideestablot_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2399_detoper a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2399_infosaudecolet b
 WHERE a.s2399_infosaudecolet_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2399_detplano a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2399_detoper b
 WHERE a.s2399_detoper_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2399_infoagnocivo a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2399_ideestablot b
 WHERE a.s2399_ideestablot_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2399_infosimples a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2399_ideestablot b
 WHERE a.s2399_ideestablot_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2399_procjudtrab a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2399_verbasresc b
 WHERE a.s2399_verbasresc_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2399_infomv a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2399_verbasresc b
 WHERE a.s2399_verbasresc_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2399_remunoutrempr a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2399_infomv b
 WHERE a.s2399_infomv_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2399_quarentena a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2399_evttsvtermino b
 WHERE a.s2399_evttsvtermino_id = b.id AND b.ativo IS NULL AND a.ativo=True;

