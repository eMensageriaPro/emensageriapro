-- eMensageriaAI --
UPDATE public.r1000_inclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r1000_evtinfocontri b
 WHERE a.r1000_evtinfocontri_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r1000_inclusao_softhouse a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r1000_inclusao b
 WHERE a.r1000_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r1000_inclusao_infoefr a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r1000_inclusao b
 WHERE a.r1000_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r1000_alteracao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r1000_evtinfocontri b
 WHERE a.r1000_evtinfocontri_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r1000_alteracao_softhouse a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r1000_alteracao b
 WHERE a.r1000_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r1000_alteracao_infoefr a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r1000_alteracao b
 WHERE a.r1000_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r1000_alteracao_novavalidade a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r1000_alteracao b
 WHERE a.r1000_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r1000_exclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r1000_evtinfocontri b
 WHERE a.r1000_evtinfocontri_id = b.id AND b.ativo IS NULL AND a.ativo=True;

