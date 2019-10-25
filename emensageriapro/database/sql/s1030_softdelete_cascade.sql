UPDATE public.s1030_inclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1030_evttabcargo b
 WHERE a.s1030_evttabcargo_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1030_inclusao_cargopublico a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1030_inclusao b
 WHERE a.s1030_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1030_alteracao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1030_evttabcargo b
 WHERE a.s1030_evttabcargo_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1030_alteracao_cargopublico a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1030_alteracao b
 WHERE a.s1030_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1030_alteracao_novavalidade a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1030_alteracao b
 WHERE a.s1030_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1030_exclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1030_evttabcargo b
 WHERE a.s1030_evttabcargo_id = b.id AND b.ativo IS NULL AND a.ativo=True;

