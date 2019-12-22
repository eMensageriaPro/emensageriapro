-- eMensageriaAI --
UPDATE public.s2240_iniexprisco_infoamb a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2240_evtexprisco b
 WHERE a.s2240_evtexprisco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2240_iniexprisco_ativpericinsal a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2240_evtexprisco b
 WHERE a.s2240_evtexprisco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2240_iniexprisco_fatrisco a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2240_evtexprisco b
 WHERE a.s2240_evtexprisco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2240_iniexprisco_epc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2240_iniexprisco_fatrisco b
 WHERE a.s2240_iniexprisco_fatrisco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2240_iniexprisco_epi a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2240_iniexprisco_fatrisco b
 WHERE a.s2240_iniexprisco_fatrisco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2240_iniexprisco_respreg a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2240_evtexprisco b
 WHERE a.s2240_evtexprisco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2240_iniexprisco_obs a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2240_evtexprisco b
 WHERE a.s2240_evtexprisco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2240_altexprisco a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2240_evtexprisco b
 WHERE a.s2240_evtexprisco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2240_altexprisco_infoamb a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2240_altexprisco b
 WHERE a.s2240_altexprisco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2240_altexprisco_fatrisco a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2240_altexprisco_infoamb b
 WHERE a.s2240_altexprisco_infoamb_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2240_altexprisco_epc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2240_altexprisco_fatrisco b
 WHERE a.s2240_altexprisco_fatrisco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2240_altexprisco_epi a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2240_altexprisco_fatrisco b
 WHERE a.s2240_altexprisco_fatrisco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2240_fimexprisco a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2240_evtexprisco b
 WHERE a.s2240_evtexprisco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2240_fimexprisco_infoamb a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2240_fimexprisco b
 WHERE a.s2240_fimexprisco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2240_fimexprisco_respreg a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2240_evtexprisco b
 WHERE a.s2240_evtexprisco_id = b.id AND b.ativo IS NULL AND a.ativo=True;

