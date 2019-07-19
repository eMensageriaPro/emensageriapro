UPDATE public.s3000_idetrabalhador a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s3000_evtexclusao b
 WHERE a.s3000_evtexclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s3000_idefolhapagto a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s3000_evtexclusao b
 WHERE a.s3000_evtexclusao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

