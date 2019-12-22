-- eMensageriaAI --
UPDATE public.s1070_inclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1070_evttabprocesso b
 WHERE a.s1070_evttabprocesso_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1070_inclusao_dadosprocjud a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1070_inclusao b
 WHERE a.s1070_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1070_inclusao_infosusp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1070_inclusao b
 WHERE a.s1070_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1070_alteracao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1070_evttabprocesso b
 WHERE a.s1070_evttabprocesso_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1070_alteracao_dadosprocjud a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1070_alteracao b
 WHERE a.s1070_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1070_alteracao_infosusp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1070_alteracao b
 WHERE a.s1070_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1070_alteracao_novavalidade a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1070_alteracao b
 WHERE a.s1070_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1070_exclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1070_evttabprocesso b
 WHERE a.s1070_evttabprocesso_id = b.id AND b.ativo IS NULL AND a.ativo=True;

