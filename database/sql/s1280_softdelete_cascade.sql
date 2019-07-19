UPDATE public.s1280_infosubstpatr a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1280_evtinfocomplper b
 WHERE a.s1280_evtinfocomplper_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1280_infosubstpatropport a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1280_evtinfocomplper b
 WHERE a.s1280_evtinfocomplper_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1280_infoativconcom a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1280_evtinfocomplper b
 WHERE a.s1280_evtinfocomplper_id = b.id AND b.ativo IS NULL AND a.ativo=True;

