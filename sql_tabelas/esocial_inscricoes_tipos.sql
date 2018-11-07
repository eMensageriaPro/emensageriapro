DELETE FROM public.esocial_inscricoes_tipos;
INSERT INTO public.esocial_inscricoes_tipos (codigo, descricao, criado_em, criado_por_id, excluido) VALUES ('1', 'CNPJ', now(), 1, False);
INSERT INTO public.esocial_inscricoes_tipos (codigo, descricao, criado_em, criado_por_id, excluido) VALUES ('2', 'CPF', now(), 1, False);
INSERT INTO public.esocial_inscricoes_tipos (codigo, descricao, criado_em, criado_por_id, excluido) VALUES ('3', 'CAEPF (Cadastro de Atividade Econômica de Pessoa Física)', now(), 1, False);
INSERT INTO public.esocial_inscricoes_tipos (codigo, descricao, criado_em, criado_por_id, excluido) VALUES ('4', 'CNO (Cadastro Nacional de Obra)', now(), 1, False);