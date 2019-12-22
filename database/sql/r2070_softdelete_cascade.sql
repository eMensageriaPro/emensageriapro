-- eMensageriaAI --
UPDATE public.r2070_inforesidext a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_evtpgtosdivs b
 WHERE a.r2070_evtpgtosdivs_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_infomolestia a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_evtpgtosdivs b
 WHERE a.r2070_evtpgtosdivs_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_ideestab a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_evtpgtosdivs b
 WHERE a.r2070_evtpgtosdivs_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_pgtoresidbr a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_ideestab b
 WHERE a.r2070_ideestab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_pgtopf a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_pgtoresidbr b
 WHERE a.r2070_pgtoresidbr_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_detdeducao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_pgtopf b
 WHERE a.r2070_pgtopf_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_rendisento a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_pgtopf b
 WHERE a.r2070_pgtopf_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_detcompet a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_pgtopf b
 WHERE a.r2070_pgtopf_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_compjud a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_pgtopf b
 WHERE a.r2070_pgtopf_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_inforra a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_pgtopf b
 WHERE a.r2070_pgtopf_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_inforra_despprocjud a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_inforra b
 WHERE a.r2070_inforra_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_inforra_ideadvogado a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_inforra_despprocjud b
 WHERE a.r2070_inforra_despprocjud_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_infoprocjud a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_pgtopf b
 WHERE a.r2070_pgtopf_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_infoprocjud_despprocjud a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_infoprocjud b
 WHERE a.r2070_infoprocjud_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_infoprocjud_ideadvogado a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_infoprocjud_despprocjud b
 WHERE a.r2070_infoprocjud_despprocjud_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_infoprocjud_origemrecursos a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_infoprocjud b
 WHERE a.r2070_infoprocjud_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_depjudicial a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_pgtopf b
 WHERE a.r2070_pgtopf_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_pgtopj a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_pgtoresidbr b
 WHERE a.r2070_pgtoresidbr_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_pgtopj_infoprocjud a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_pgtopj b
 WHERE a.r2070_pgtopj_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_pgtopj_despprocjud a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_pgtopj_infoprocjud b
 WHERE a.r2070_pgtopj_infoprocjud_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_pgtopj_ideadvogado a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_pgtopj_despprocjud b
 WHERE a.r2070_pgtopj_despprocjud_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_pgtopj_origemrecursos a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_pgtopj_infoprocjud b
 WHERE a.r2070_pgtopj_infoprocjud_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.r2070_pgtoresidext a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.r2070_ideestab b
 WHERE a.r2070_ideestab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

