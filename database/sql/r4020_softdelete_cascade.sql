UPDATE public.r4020_idepgto a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4020_evtretpj b
 WHERE a.r4020_evtretpj_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4020_infopgto a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4020_idepgto b
 WHERE a.r4020_idepgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4020_ir a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4020_infopgto b
 WHERE a.r4020_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4020_csll a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4020_infopgto b
 WHERE a.r4020_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4020_cofins a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4020_infopgto b
 WHERE a.r4020_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4020_pp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4020_infopgto b
 WHERE a.r4020_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4020_fci a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4020_infopgto b
 WHERE a.r4020_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4020_scp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4020_infopgto b
 WHERE a.r4020_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4020_infoprocret a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4020_infopgto b
 WHERE a.r4020_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4020_infoprocjud a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4020_infopgto b
 WHERE a.r4020_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4020_despprocjud a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4020_infoprocjud b
 WHERE a.r4020_infoprocjud_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4020_ideadv a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4020_despprocjud b
 WHERE a.r4020_despprocjud_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4020_origemrec a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4020_infoprocjud b
 WHERE a.r4020_infoprocjud_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4020_infopgtoext a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4020_idepgto b
 WHERE a.r4020_idepgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

