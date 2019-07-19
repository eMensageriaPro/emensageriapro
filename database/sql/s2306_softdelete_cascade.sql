UPDATE public.s2306_infocomplementares a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2306_evttsvaltcontr b
 WHERE a.s2306_evttsvaltcontr_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2306_cargofuncao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2306_infocomplementares b
 WHERE a.s2306_infocomplementares_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2306_remuneracao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2306_infocomplementares b
 WHERE a.s2306_infocomplementares_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2306_infotrabcedido a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2306_infocomplementares b
 WHERE a.s2306_infocomplementares_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2306_infoestagiario a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2306_infocomplementares b
 WHERE a.s2306_infocomplementares_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2306_ageintegracao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2306_infoestagiario b
 WHERE a.s2306_infoestagiario_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2306_supervisorestagio a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2306_infoestagiario b
 WHERE a.s2306_infoestagiario_id = b.id AND b.ativo IS NULL AND a.ativo=True;

