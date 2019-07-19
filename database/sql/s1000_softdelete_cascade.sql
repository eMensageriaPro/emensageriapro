UPDATE public.s1000_inclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_evtinfoempregador b
 WHERE a.s1000_evtinfoempregador_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_inclusao_dadosisencao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_inclusao b
 WHERE a.s1000_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_inclusao_infoop a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_inclusao b
 WHERE a.s1000_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_inclusao_infoefr a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_inclusao_infoop b
 WHERE a.s1000_inclusao_infoop_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_inclusao_infoente a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_inclusao_infoop b
 WHERE a.s1000_inclusao_infoop_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_inclusao_infoorginternacional a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_inclusao b
 WHERE a.s1000_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_inclusao_softwarehouse a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_inclusao b
 WHERE a.s1000_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_inclusao_situacaopj a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_inclusao b
 WHERE a.s1000_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_inclusao_situacaopf a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_inclusao b
 WHERE a.s1000_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_alteracao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_evtinfoempregador b
 WHERE a.s1000_evtinfoempregador_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_alteracao_dadosisencao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_alteracao b
 WHERE a.s1000_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_alteracao_infoop a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_alteracao b
 WHERE a.s1000_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_alteracao_infoefr a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_alteracao_infoop b
 WHERE a.s1000_alteracao_infoop_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_alteracao_infoente a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_alteracao_infoop b
 WHERE a.s1000_alteracao_infoop_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_alteracao_infoorginternacional a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_alteracao b
 WHERE a.s1000_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_alteracao_softwarehouse a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_alteracao b
 WHERE a.s1000_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_alteracao_situacaopj a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_alteracao b
 WHERE a.s1000_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_alteracao_situacaopf a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_alteracao b
 WHERE a.s1000_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_alteracao_novavalidade a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_alteracao b
 WHERE a.s1000_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1000_exclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1000_evtinfoempregador b
 WHERE a.s1000_evtinfoempregador_id = b.id AND b.ativo IS NULL AND a.ativo=True;

