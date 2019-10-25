UPDATE public.r4010_idepgto a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_evtretpf b
 WHERE a.r4010_evtretpf_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_infopgto a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_idepgto b
 WHERE a.r4010_idepgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_fci a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_infopgto b
 WHERE a.r4010_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_scp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_infopgto b
 WHERE a.r4010_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_detded a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_infopgto b
 WHERE a.r4010_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_benefpen a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_detded b
 WHERE a.r4010_detded_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_rendisento a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_infopgto b
 WHERE a.r4010_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_infoprocret a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_infopgto b
 WHERE a.r4010_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_inforra a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_infopgto b
 WHERE a.r4010_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_inforra_despprocjud a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_inforra b
 WHERE a.r4010_inforra_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_inforra_ideadv a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_inforra_despprocjud b
 WHERE a.r4010_inforra_despprocjud_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_inforra_origemrec a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_inforra b
 WHERE a.r4010_inforra_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_infoprocjud a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_infopgto b
 WHERE a.r4010_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_infoprocjud_despprocjud a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_infoprocjud b
 WHERE a.r4010_infoprocjud_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_infoprocjud_ideadv a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_infoprocjud_despprocjud b
 WHERE a.r4010_infoprocjud_despprocjud_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_infoprocjud_origemrec a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_infoprocjud b
 WHERE a.r4010_infoprocjud_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_infopgtoext a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_idepgto b
 WHERE a.r4010_idepgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_ideopsaude a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_evtretpf b
 WHERE a.r4010_evtretpf_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_inforeemb a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_ideopsaude b
 WHERE a.r4010_ideopsaude_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_infodependpl a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_ideopsaude b
 WHERE a.r4010_ideopsaude_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r4010_inforeembdep a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r4010_infodependpl b
 WHERE a.r4010_infodependpl_id = b.id AND b.ativo IS NULL AND a.ativo=True;

