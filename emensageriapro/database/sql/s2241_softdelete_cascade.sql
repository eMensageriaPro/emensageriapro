UPDATE public.s2241_insalperic a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_evtinsapo b
 WHERE a.s2241_evtinsapo_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2241_iniinsalperic a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_insalperic b
 WHERE a.s2241_insalperic_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2241_iniinsalperic_infoamb a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_iniinsalperic b
 WHERE a.s2241_iniinsalperic_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2241_iniinsalperic_fatrisco a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_iniinsalperic_infoamb b
 WHERE a.s2241_iniinsalperic_infoamb_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2241_altinsalperic a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_insalperic b
 WHERE a.s2241_insalperic_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2241_altinsalperic_infoamb a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_altinsalperic b
 WHERE a.s2241_altinsalperic_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2241_altinsalperic_fatrisco a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_altinsalperic_infoamb b
 WHERE a.s2241_altinsalperic_infoamb_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2241_fiminsalperic a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_insalperic b
 WHERE a.s2241_insalperic_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2241_fiminsalperic_infoamb a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_fiminsalperic b
 WHERE a.s2241_fiminsalperic_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2241_aposentesp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_evtinsapo b
 WHERE a.s2241_evtinsapo_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2241_iniaposentesp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_aposentesp b
 WHERE a.s2241_aposentesp_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2241_iniaposentesp_infoamb a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_iniaposentesp b
 WHERE a.s2241_iniaposentesp_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2241_iniaposentesp_fatrisco a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_iniaposentesp_infoamb b
 WHERE a.s2241_iniaposentesp_infoamb_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2241_altaposentesp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_aposentesp b
 WHERE a.s2241_aposentesp_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2241_altaposentesp_infoamb a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_altaposentesp b
 WHERE a.s2241_altaposentesp_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2241_altaposentesp_fatrisco a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_altaposentesp_infoamb b
 WHERE a.s2241_altaposentesp_infoamb_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2241_fimaposentesp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_aposentesp b
 WHERE a.s2241_aposentesp_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2241_fimaposentesp_infoamb a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2241_fimaposentesp b
 WHERE a.s2241_fimaposentesp_id = b.id AND b.ativo IS NULL AND a.ativo=True;

