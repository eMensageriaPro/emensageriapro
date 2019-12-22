-- eMensageriaAI --
UPDATE public.s1210_deps a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1210_evtpgtos b
 WHERE a.s1210_evtpgtos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1210_infopgto a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1210_evtpgtos b
 WHERE a.s1210_evtpgtos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1210_detpgtofl a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1210_infopgto b
 WHERE a.s1210_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1210_detpgtofl_retpgtotot a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1210_detpgtofl b
 WHERE a.s1210_detpgtofl_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1210_detpgtofl_penalim a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1210_detpgtofl_retpgtotot b
 WHERE a.s1210_detpgtofl_retpgtotot_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1210_detpgtofl_infopgtoparc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1210_detpgtofl b
 WHERE a.s1210_detpgtofl_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1210_detpgtobenpr a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1210_infopgto b
 WHERE a.s1210_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1210_detpgtobenpr_retpgtotot a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1210_detpgtobenpr b
 WHERE a.s1210_detpgtobenpr_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1210_detpgtobenpr_infopgtoparc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1210_detpgtobenpr b
 WHERE a.s1210_detpgtobenpr_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1210_detpgtofer a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1210_infopgto b
 WHERE a.s1210_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1210_detpgtofer_detrubrfer a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1210_detpgtofer b
 WHERE a.s1210_detpgtofer_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1210_detpgtofer_penalim a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1210_detpgtofer_detrubrfer b
 WHERE a.s1210_detpgtofer_detrubrfer_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1210_detpgtoant a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1210_infopgto b
 WHERE a.s1210_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1210_detpgtoant_infopgtoant a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1210_detpgtoant b
 WHERE a.s1210_detpgtoant_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s1210_idepgtoext a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s1210_infopgto b
 WHERE a.s1210_infopgto_id = b.id AND b.ativo IS NULL AND a.ativo=True;

