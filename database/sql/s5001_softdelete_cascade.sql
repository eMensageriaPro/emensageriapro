-- eMensageriaAI --
UPDATE public.s5001_procjudtrab a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5001_evtbasestrab b
 WHERE a.s5001_evtbasestrab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5001_infocpcalc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5001_evtbasestrab b
 WHERE a.s5001_evtbasestrab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5001_infocp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5001_evtbasestrab b
 WHERE a.s5001_evtbasestrab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5001_ideestablot a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5001_infocp b
 WHERE a.s5001_infocp_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5001_infocategincid a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5001_ideestablot b
 WHERE a.s5001_ideestablot_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5001_infobasecs a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5001_infocategincid b
 WHERE a.s5001_infocategincid_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5001_calcterc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5001_infocategincid b
 WHERE a.s5001_infocategincid_id = b.id AND b.ativo IS NULL AND a.ativo=True;

