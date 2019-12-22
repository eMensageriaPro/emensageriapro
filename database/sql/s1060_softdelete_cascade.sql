-- eMensageriaAI --
UPDATE public.s1060_inclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1060_evttabambiente b
 WHERE a.s1060_evttabambiente_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1060_alteracao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1060_evttabambiente b
 WHERE a.s1060_evttabambiente_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1060_alteracao_novavalidade a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1060_alteracao b
 WHERE a.s1060_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1060_exclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1060_evttabambiente b
 WHERE a.s1060_evttabambiente_id = b.id AND b.ativo IS NULL AND a.ativo=True;

