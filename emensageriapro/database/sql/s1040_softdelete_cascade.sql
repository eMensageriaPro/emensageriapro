UPDATE public.s1040_inclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1040_evttabfuncao b
 WHERE a.s1040_evttabfuncao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1040_alteracao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1040_evttabfuncao b
 WHERE a.s1040_evttabfuncao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1040_alteracao_novavalidade a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1040_alteracao b
 WHERE a.s1040_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1040_exclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1040_evttabfuncao b
 WHERE a.s1040_evttabfuncao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

