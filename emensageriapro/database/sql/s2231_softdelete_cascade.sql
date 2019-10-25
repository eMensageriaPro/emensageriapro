UPDATE public.s2231_inicessao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2231_evtcessao b
 WHERE a.s2231_evtcessao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2231_fimcessao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2231_evtcessao b
 WHERE a.s2231_evtcessao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

