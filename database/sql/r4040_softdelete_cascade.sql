UPDATE public.r4040_idenat a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4040_evtbenefnid b
 WHERE a.r4040_evtbenefnid_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4040_infopgto a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4040_idenat b
 WHERE a.r4040_idenat_id = b.id AND b.ativo IS NULL AND a.ativo=True;

