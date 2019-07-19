UPDATE public.s1050_inclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1050_evttabhortur b
 WHERE a.s1050_evttabhortur_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1050_inclusao_horariointervalo a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1050_inclusao b
 WHERE a.s1050_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1050_alteracao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1050_evttabhortur b
 WHERE a.s1050_evttabhortur_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1050_alteracao_horariointervalo a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1050_alteracao b
 WHERE a.s1050_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1050_alteracao_novavalidade a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1050_alteracao b
 WHERE a.s1050_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1050_exclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1050_evttabhortur b
 WHERE a.s1050_evttabhortur_id = b.id AND b.ativo IS NULL AND a.ativo=True;

