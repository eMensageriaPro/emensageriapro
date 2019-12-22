-- eMensageriaAI --
UPDATE public.s5011_infocpseg a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5011_evtcs b
 WHERE a.s5011_evtcs_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5011_infopj a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5011_evtcs b
 WHERE a.s5011_evtcs_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5011_infoatconc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5011_infopj b
 WHERE a.s5011_infopj_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5011_ideestab a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5011_evtcs b
 WHERE a.s5011_evtcs_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5011_infoestab a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5011_ideestab b
 WHERE a.s5011_ideestab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5011_infocomplobra a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5011_infoestab b
 WHERE a.s5011_infoestab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5011_idelotacao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5011_ideestab b
 WHERE a.s5011_ideestab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5011_infotercsusp a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5011_idelotacao b
 WHERE a.s5011_idelotacao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5011_infoemprparcial a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5011_idelotacao b
 WHERE a.s5011_idelotacao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5011_dadosopport a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5011_idelotacao b
 WHERE a.s5011_idelotacao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5011_basesremun a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5011_idelotacao b
 WHERE a.s5011_idelotacao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5011_basesavnport a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5011_idelotacao b
 WHERE a.s5011_idelotacao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5011_infosubstpatropport a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5011_idelotacao b
 WHERE a.s5011_idelotacao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5011_basesaquis a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5011_ideestab b
 WHERE a.s5011_ideestab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5011_basescomerc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5011_ideestab b
 WHERE a.s5011_ideestab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5011_infocrestab a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5011_ideestab b
 WHERE a.s5011_ideestab_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s5011_infocrcontrib a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s5011_evtcs b
 WHERE a.s5011_evtcs_id = b.id AND b.ativo IS NULL AND a.ativo=True;

