-- eMensageriaAI --
UPDATE public.s1080_inclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1080_evttaboperport b
 WHERE a.s1080_evttaboperport_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1080_alteracao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1080_evttaboperport b
 WHERE a.s1080_evttaboperport_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1080_alteracao_novavalidade a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1080_alteracao b
 WHERE a.s1080_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1080_exclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1080_evttaboperport b
 WHERE a.s1080_evttaboperport_id = b.id AND b.ativo IS NULL AND a.ativo=True;

