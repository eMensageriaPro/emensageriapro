UPDATE public.s2300_documentos a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_evttsvinicio b
 WHERE a.s2300_evttsvinicio_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_ctps a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_documentos b
 WHERE a.s2300_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_ric a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_documentos b
 WHERE a.s2300_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_rg a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_documentos b
 WHERE a.s2300_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_rne a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_documentos b
 WHERE a.s2300_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_oc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_documentos b
 WHERE a.s2300_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_cnh a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_documentos b
 WHERE a.s2300_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_brasil a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_evttsvinicio b
 WHERE a.s2300_evttsvinicio_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_exterior a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_evttsvinicio b
 WHERE a.s2300_evttsvinicio_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_trabestrangeiro a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_evttsvinicio b
 WHERE a.s2300_evttsvinicio_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_infodeficiencia a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_evttsvinicio b
 WHERE a.s2300_evttsvinicio_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_dependente a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_evttsvinicio b
 WHERE a.s2300_evttsvinicio_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_contato a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_evttsvinicio b
 WHERE a.s2300_evttsvinicio_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_infocomplementares a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_evttsvinicio b
 WHERE a.s2300_evttsvinicio_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_cargofuncao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_infocomplementares b
 WHERE a.s2300_infocomplementares_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_remuneracao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_infocomplementares b
 WHERE a.s2300_infocomplementares_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_fgts a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_infocomplementares b
 WHERE a.s2300_infocomplementares_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_infodirigentesindical a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_infocomplementares b
 WHERE a.s2300_infocomplementares_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_infotrabcedido a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_infocomplementares b
 WHERE a.s2300_infocomplementares_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_infoestagiario a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_infocomplementares b
 WHERE a.s2300_infocomplementares_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_ageintegracao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_infoestagiario b
 WHERE a.s2300_infoestagiario_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_supervisorestagio a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_infoestagiario b
 WHERE a.s2300_infoestagiario_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_mudancacpf a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_evttsvinicio b
 WHERE a.s2300_evttsvinicio_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_afastamento a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_evttsvinicio b
 WHERE a.s2300_evttsvinicio_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2300_termino a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2300_evttsvinicio b
 WHERE a.s2300_evttsvinicio_id = b.id AND b.ativo IS NULL AND a.ativo=True;

