-- eMensageriaAI --
UPDATE public.s1005_inclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1005_evttabestab b
 WHERE a.s1005_evttabestab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1005_inclusao_procadmjudrat a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1005_inclusao b
 WHERE a.s1005_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1005_inclusao_procadmjudfap a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1005_inclusao b
 WHERE a.s1005_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1005_inclusao_infocaepf a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1005_inclusao b
 WHERE a.s1005_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1005_inclusao_infoobra a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1005_inclusao b
 WHERE a.s1005_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1005_inclusao_infoenteduc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1005_inclusao b
 WHERE a.s1005_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1005_inclusao_infopcd a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1005_inclusao b
 WHERE a.s1005_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1005_alteracao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1005_evttabestab b
 WHERE a.s1005_evttabestab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1005_alteracao_procadmjudrat a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1005_alteracao b
 WHERE a.s1005_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1005_alteracao_procadmjudfap a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1005_alteracao b
 WHERE a.s1005_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1005_alteracao_infocaepf a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1005_alteracao b
 WHERE a.s1005_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1005_alteracao_infoobra a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1005_alteracao b
 WHERE a.s1005_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1005_alteracao_infoenteduc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1005_alteracao b
 WHERE a.s1005_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1005_alteracao_infopcd a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1005_alteracao b
 WHERE a.s1005_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1005_alteracao_novavalidade a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1005_alteracao b
 WHERE a.s1005_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1005_exclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1005_evttabestab b
 WHERE a.s1005_evttabestab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

