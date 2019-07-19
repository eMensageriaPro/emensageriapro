UPDATE public.s1020_inclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1020_evttablotacao b
 WHERE a.s1020_evttablotacao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1020_inclusao_infoprocjudterceiros a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1020_inclusao b
 WHERE a.s1020_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1020_inclusao_procjudterceiro a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1020_inclusao_infoprocjudterceiros b
 WHERE a.s1020_inclusao_infoprocjudterceiros_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1020_inclusao_infoemprparcial a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1020_inclusao b
 WHERE a.s1020_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1020_alteracao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1020_evttablotacao b
 WHERE a.s1020_evttablotacao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1020_alteracao_infoprocjudterceiros a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1020_alteracao b
 WHERE a.s1020_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1020_alteracao_procjudterceiro a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1020_alteracao_infoprocjudterceiros b
 WHERE a.s1020_alteracao_infoprocjudterceiros_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1020_alteracao_infoemprparcial a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1020_alteracao b
 WHERE a.s1020_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1020_alteracao_novavalidade a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1020_alteracao b
 WHERE a.s1020_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1020_exclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1020_evttablotacao b
 WHERE a.s1020_evttablotacao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

