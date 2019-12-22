-- eMensageriaAI --
UPDATE public.s2205_documentos a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2205_evtaltcadastral b
 WHERE a.s2205_evtaltcadastral_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2205_ctps a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2205_documentos b
 WHERE a.s2205_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2205_ric a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2205_documentos b
 WHERE a.s2205_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2205_rg a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2205_documentos b
 WHERE a.s2205_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2205_rne a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2205_documentos b
 WHERE a.s2205_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2205_oc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2205_documentos b
 WHERE a.s2205_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2205_cnh a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2205_documentos b
 WHERE a.s2205_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2205_brasil a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2205_evtaltcadastral b
 WHERE a.s2205_evtaltcadastral_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2205_exterior a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2205_evtaltcadastral b
 WHERE a.s2205_evtaltcadastral_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2205_trabestrangeiro a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2205_evtaltcadastral b
 WHERE a.s2205_evtaltcadastral_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2205_infodeficiencia a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2205_evtaltcadastral b
 WHERE a.s2205_evtaltcadastral_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2205_dependente a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2205_evtaltcadastral b
 WHERE a.s2205_evtaltcadastral_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2205_aposentadoria a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2205_evtaltcadastral b
 WHERE a.s2205_evtaltcadastral_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2205_contato a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2205_evtaltcadastral b
 WHERE a.s2205_evtaltcadastral_id = b.id AND b.ativo IS NULL AND a.ativo=True;

