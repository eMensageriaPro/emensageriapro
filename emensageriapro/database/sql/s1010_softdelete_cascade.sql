UPDATE public.s1010_inclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1010_evttabrubrica b
 WHERE a.s1010_evttabrubrica_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1010_inclusao_ideprocessocp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1010_inclusao b
 WHERE a.s1010_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1010_inclusao_ideprocessoirrf a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1010_inclusao b
 WHERE a.s1010_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1010_inclusao_ideprocessofgts a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1010_inclusao b
 WHERE a.s1010_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1010_inclusao_ideprocessosind a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1010_inclusao b
 WHERE a.s1010_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1010_inclusao_ideprocessocprp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1010_inclusao b
 WHERE a.s1010_inclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1010_alteracao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1010_evttabrubrica b
 WHERE a.s1010_evttabrubrica_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1010_alteracao_ideprocessocp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1010_alteracao b
 WHERE a.s1010_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1010_alteracao_ideprocessoirrf a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1010_alteracao b
 WHERE a.s1010_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1010_alteracao_ideprocessofgts a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1010_alteracao b
 WHERE a.s1010_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1010_alteracao_ideprocessosind a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1010_alteracao b
 WHERE a.s1010_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1010_alteracao_ideprocessocprp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1010_alteracao b
 WHERE a.s1010_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1010_alteracao_novavalidade a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1010_alteracao b
 WHERE a.s1010_alteracao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1010_exclusao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1010_evttabrubrica b
 WHERE a.s1010_evttabrubrica_id = b.id AND b.ativo IS NULL AND a.ativo=True;

