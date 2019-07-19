UPDATE public.s2200_documentos a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_ctps a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_documentos b
 WHERE a.s2200_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_ric a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_documentos b
 WHERE a.s2200_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_rg a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_documentos b
 WHERE a.s2200_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_rne a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_documentos b
 WHERE a.s2200_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_oc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_documentos b
 WHERE a.s2200_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_cnh a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_documentos b
 WHERE a.s2200_documentos_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_brasil a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_exterior a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_trabestrangeiro a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_infodeficiencia a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_dependente a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_aposentadoria a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_contato a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_infoceletista a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_trabtemporario a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_infoceletista b
 WHERE a.s2200_infoceletista_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_ideestabvinc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_trabtemporario b
 WHERE a.s2200_trabtemporario_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_idetrabsubstituido a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_trabtemporario b
 WHERE a.s2200_trabtemporario_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_aprend a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_infoceletista b
 WHERE a.s2200_infoceletista_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_infoestatutario a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_infodecjud a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_infoestatutario b
 WHERE a.s2200_infoestatutario_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_localtrabgeral a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_localtrabdom a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_horcontratual a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_horario a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_horcontratual b
 WHERE a.s2200_horcontratual_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_filiacaosindical a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_alvarajudicial a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_observacoes a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_sucessaovinc a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_transfdom a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_mudancacpf a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_afastamento a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_desligamento a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

UPDATE public.s2200_cessao a
   SET ativo=b.ativo, desativado_em=b.desativado_em, desativado_por_id=b.desativado_por_id
  FROM public.s2200_evtadmissao b
 WHERE a.s2200_evtadmissao_id = b.id AND b.ativo IS NULL AND a.ativo=True;

