-- eMensageriaAI --
UPDATE public.s1035_inclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1035_evttabcarreira b
 WHERE a.s1035_evttabcarreira_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1035_alteracao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1035_evttabcarreira b
 WHERE a.s1035_evttabcarreira_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1035_alteracao_novavalidade a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1035_alteracao b
 WHERE a.s1035_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1035_exclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1035_evttabcarreira b
 WHERE a.s1035_evttabcarreira_id = b.id AND b.ativo IS NULL AND a.ativo=True;

