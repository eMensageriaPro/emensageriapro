#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.tabelas.views import municipios_apagar as municipios_apagar_views
from emensageriapro.tabelas.views import municipios_listar as municipios_listar_views
from emensageriapro.tabelas.views import municipios_salvar as municipios_salvar_views
from emensageriapro.tabelas.views import municipios_api as municipios_api_views
from emensageriapro.tabelas.views import cbo_apagar as cbo_apagar_views
from emensageriapro.tabelas.views import cbo_listar as cbo_listar_views
from emensageriapro.tabelas.views import cbo_salvar as cbo_salvar_views
from emensageriapro.tabelas.views import cbo_api as cbo_api_views
from emensageriapro.tabelas.views import cid_apagar as cid_apagar_views
from emensageriapro.tabelas.views import cid_listar as cid_listar_views
from emensageriapro.tabelas.views import cid_salvar as cid_salvar_views
from emensageriapro.tabelas.views import cid_api as cid_api_views
from emensageriapro.tabelas.views import cnae_apagar as cnae_apagar_views
from emensageriapro.tabelas.views import cnae_listar as cnae_listar_views
from emensageriapro.tabelas.views import cnae_salvar as cnae_salvar_views
from emensageriapro.tabelas.views import cnae_api as cnae_api_views
from emensageriapro.tabelas.views import esocial_trabalhadores_categorias_apagar as esocial_trabalhadores_categorias_apagar_views
from emensageriapro.tabelas.views import esocial_trabalhadores_categorias_listar as esocial_trabalhadores_categorias_listar_views
from emensageriapro.tabelas.views import esocial_trabalhadores_categorias_salvar as esocial_trabalhadores_categorias_salvar_views
from emensageriapro.tabelas.views import esocial_trabalhadores_categorias_api as esocial_trabalhadores_categorias_api_views
from emensageriapro.tabelas.views import esocial_financiamentos_aposentadorias_especiais_apagar as esocial_financiamentos_aposentadorias_especiais_apagar_views
from emensageriapro.tabelas.views import esocial_financiamentos_aposentadorias_especiais_listar as esocial_financiamentos_aposentadorias_especiais_listar_views
from emensageriapro.tabelas.views import esocial_financiamentos_aposentadorias_especiais_salvar as esocial_financiamentos_aposentadorias_especiais_salvar_views
from emensageriapro.tabelas.views import esocial_financiamentos_aposentadorias_especiais_api as esocial_financiamentos_aposentadorias_especiais_api_views
from emensageriapro.tabelas.views import esocial_naturezas_rubricas_apagar as esocial_naturezas_rubricas_apagar_views
from emensageriapro.tabelas.views import esocial_naturezas_rubricas_listar as esocial_naturezas_rubricas_listar_views
from emensageriapro.tabelas.views import esocial_naturezas_rubricas_salvar as esocial_naturezas_rubricas_salvar_views
from emensageriapro.tabelas.views import esocial_naturezas_rubricas_api as esocial_naturezas_rubricas_api_views
from emensageriapro.tabelas.views import esocial_codigo_aliquotas_fpas_terceiros_apagar as esocial_codigo_aliquotas_fpas_terceiros_apagar_views
from emensageriapro.tabelas.views import esocial_codigo_aliquotas_fpas_terceiros_listar as esocial_codigo_aliquotas_fpas_terceiros_listar_views
from emensageriapro.tabelas.views import esocial_codigo_aliquotas_fpas_terceiros_salvar as esocial_codigo_aliquotas_fpas_terceiros_salvar_views
from emensageriapro.tabelas.views import esocial_codigo_aliquotas_fpas_terceiros_api as esocial_codigo_aliquotas_fpas_terceiros_api_views
from emensageriapro.tabelas.views import esocial_inscricoes_tipos_apagar as esocial_inscricoes_tipos_apagar_views
from emensageriapro.tabelas.views import esocial_inscricoes_tipos_listar as esocial_inscricoes_tipos_listar_views
from emensageriapro.tabelas.views import esocial_inscricoes_tipos_salvar as esocial_inscricoes_tipos_salvar_views
from emensageriapro.tabelas.views import esocial_inscricoes_tipos_api as esocial_inscricoes_tipos_api_views
from emensageriapro.tabelas.views import esocial_paises_apagar as esocial_paises_apagar_views
from emensageriapro.tabelas.views import esocial_paises_listar as esocial_paises_listar_views
from emensageriapro.tabelas.views import esocial_paises_salvar as esocial_paises_salvar_views
from emensageriapro.tabelas.views import esocial_paises_api as esocial_paises_api_views
from emensageriapro.tabelas.views import esocial_dependentes_tipos_apagar as esocial_dependentes_tipos_apagar_views
from emensageriapro.tabelas.views import esocial_dependentes_tipos_listar as esocial_dependentes_tipos_listar_views
from emensageriapro.tabelas.views import esocial_dependentes_tipos_salvar as esocial_dependentes_tipos_salvar_views
from emensageriapro.tabelas.views import esocial_dependentes_tipos_api as esocial_dependentes_tipos_api_views
from emensageriapro.tabelas.views import esocial_classificacoes_tributarias_apagar as esocial_classificacoes_tributarias_apagar_views
from emensageriapro.tabelas.views import esocial_classificacoes_tributarias_listar as esocial_classificacoes_tributarias_listar_views
from emensageriapro.tabelas.views import esocial_classificacoes_tributarias_salvar as esocial_classificacoes_tributarias_salvar_views
from emensageriapro.tabelas.views import esocial_classificacoes_tributarias_api as esocial_classificacoes_tributarias_api_views
from emensageriapro.tabelas.views import esocial_arquivos_esocial_tipos_apagar as esocial_arquivos_esocial_tipos_apagar_views
from emensageriapro.tabelas.views import esocial_arquivos_esocial_tipos_listar as esocial_arquivos_esocial_tipos_listar_views
from emensageriapro.tabelas.views import esocial_arquivos_esocial_tipos_salvar as esocial_arquivos_esocial_tipos_salvar_views
from emensageriapro.tabelas.views import esocial_arquivos_esocial_tipos_api as esocial_arquivos_esocial_tipos_api_views
from emensageriapro.tabelas.views import esocial_lotacoes_tributarias_tipos_apagar as esocial_lotacoes_tributarias_tipos_apagar_views
from emensageriapro.tabelas.views import esocial_lotacoes_tributarias_tipos_listar as esocial_lotacoes_tributarias_tipos_listar_views
from emensageriapro.tabelas.views import esocial_lotacoes_tributarias_tipos_salvar as esocial_lotacoes_tributarias_tipos_salvar_views
from emensageriapro.tabelas.views import esocial_lotacoes_tributarias_tipos_api as esocial_lotacoes_tributarias_tipos_api_views
from emensageriapro.tabelas.views import esocial_compatibilidades_categorias_classificacoes_lotacoes_apagar as esocial_compatibilidades_categorias_classificacoes_lotacoes_apagar_views
from emensageriapro.tabelas.views import esocial_compatibilidades_categorias_classificacoes_lotacoes_listar as esocial_compatibilidades_categorias_classificacoes_lotacoes_listar_views
from emensageriapro.tabelas.views import esocial_compatibilidades_categorias_classificacoes_lotacoes_salvar as esocial_compatibilidades_categorias_classificacoes_lotacoes_salvar_views
from emensageriapro.tabelas.views import esocial_compatibilidades_categorias_classificacoes_lotacoes_api as esocial_compatibilidades_categorias_classificacoes_lotacoes_api_views
from emensageriapro.tabelas.views import esocial_compatibilidades_lotacoes_classificacoes_apagar as esocial_compatibilidades_lotacoes_classificacoes_apagar_views
from emensageriapro.tabelas.views import esocial_compatibilidades_lotacoes_classificacoes_listar as esocial_compatibilidades_lotacoes_classificacoes_listar_views
from emensageriapro.tabelas.views import esocial_compatibilidades_lotacoes_classificacoes_salvar as esocial_compatibilidades_lotacoes_classificacoes_salvar_views
from emensageriapro.tabelas.views import esocial_compatibilidades_lotacoes_classificacoes_api as esocial_compatibilidades_lotacoes_classificacoes_api_views
from emensageriapro.tabelas.views import esocial_partes_corpo_atingidas_apagar as esocial_partes_corpo_atingidas_apagar_views
from emensageriapro.tabelas.views import esocial_partes_corpo_atingidas_listar as esocial_partes_corpo_atingidas_listar_views
from emensageriapro.tabelas.views import esocial_partes_corpo_atingidas_salvar as esocial_partes_corpo_atingidas_salvar_views
from emensageriapro.tabelas.views import esocial_partes_corpo_atingidas_api as esocial_partes_corpo_atingidas_api_views
from emensageriapro.tabelas.views import esocial_agentes_causadores_acidentes_trabalho_apagar as esocial_agentes_causadores_acidentes_trabalho_apagar_views
from emensageriapro.tabelas.views import esocial_agentes_causadores_acidentes_trabalho_listar as esocial_agentes_causadores_acidentes_trabalho_listar_views
from emensageriapro.tabelas.views import esocial_agentes_causadores_acidentes_trabalho_salvar as esocial_agentes_causadores_acidentes_trabalho_salvar_views
from emensageriapro.tabelas.views import esocial_agentes_causadores_acidentes_trabalho_api as esocial_agentes_causadores_acidentes_trabalho_api_views
from emensageriapro.tabelas.views import esocial_agentes_causadores_doencas_profissionais_apagar as esocial_agentes_causadores_doencas_profissionais_apagar_views
from emensageriapro.tabelas.views import esocial_agentes_causadores_doencas_profissionais_listar as esocial_agentes_causadores_doencas_profissionais_listar_views
from emensageriapro.tabelas.views import esocial_agentes_causadores_doencas_profissionais_salvar as esocial_agentes_causadores_doencas_profissionais_salvar_views
from emensageriapro.tabelas.views import esocial_agentes_causadores_doencas_profissionais_api as esocial_agentes_causadores_doencas_profissionais_api_views
from emensageriapro.tabelas.views import esocial_acidentes_situacoes_geradoras_apagar as esocial_acidentes_situacoes_geradoras_apagar_views
from emensageriapro.tabelas.views import esocial_acidentes_situacoes_geradoras_listar as esocial_acidentes_situacoes_geradoras_listar_views
from emensageriapro.tabelas.views import esocial_acidentes_situacoes_geradoras_salvar as esocial_acidentes_situacoes_geradoras_salvar_views
from emensageriapro.tabelas.views import esocial_acidentes_situacoes_geradoras_api as esocial_acidentes_situacoes_geradoras_api_views
from emensageriapro.tabelas.views import esocial_naturezas_lesoes_apagar as esocial_naturezas_lesoes_apagar_views
from emensageriapro.tabelas.views import esocial_naturezas_lesoes_listar as esocial_naturezas_lesoes_listar_views
from emensageriapro.tabelas.views import esocial_naturezas_lesoes_salvar as esocial_naturezas_lesoes_salvar_views
from emensageriapro.tabelas.views import esocial_naturezas_lesoes_api as esocial_naturezas_lesoes_api_views
from emensageriapro.tabelas.views import esocial_afastamentos_motivos_apagar as esocial_afastamentos_motivos_apagar_views
from emensageriapro.tabelas.views import esocial_afastamentos_motivos_listar as esocial_afastamentos_motivos_listar_views
from emensageriapro.tabelas.views import esocial_afastamentos_motivos_salvar as esocial_afastamentos_motivos_salvar_views
from emensageriapro.tabelas.views import esocial_afastamentos_motivos_api as esocial_afastamentos_motivos_api_views
from emensageriapro.tabelas.views import esocial_desligamentos_motivos_apagar as esocial_desligamentos_motivos_apagar_views
from emensageriapro.tabelas.views import esocial_desligamentos_motivos_listar as esocial_desligamentos_motivos_listar_views
from emensageriapro.tabelas.views import esocial_desligamentos_motivos_salvar as esocial_desligamentos_motivos_salvar_views
from emensageriapro.tabelas.views import esocial_desligamentos_motivos_api as esocial_desligamentos_motivos_api_views
from emensageriapro.tabelas.views import esocial_logradouros_tipos_apagar as esocial_logradouros_tipos_apagar_views
from emensageriapro.tabelas.views import esocial_logradouros_tipos_listar as esocial_logradouros_tipos_listar_views
from emensageriapro.tabelas.views import esocial_logradouros_tipos_salvar as esocial_logradouros_tipos_salvar_views
from emensageriapro.tabelas.views import esocial_logradouros_tipos_api as esocial_logradouros_tipos_api_views
from emensageriapro.tabelas.views import esocial_naturezas_juridicas_apagar as esocial_naturezas_juridicas_apagar_views
from emensageriapro.tabelas.views import esocial_naturezas_juridicas_listar as esocial_naturezas_juridicas_listar_views
from emensageriapro.tabelas.views import esocial_naturezas_juridicas_salvar as esocial_naturezas_juridicas_salvar_views
from emensageriapro.tabelas.views import esocial_naturezas_juridicas_api as esocial_naturezas_juridicas_api_views
from emensageriapro.tabelas.views import esocial_compatibilidades_fpas_classificacoes_tributarias_apagar as esocial_compatibilidades_fpas_classificacoes_tributarias_apagar_views
from emensageriapro.tabelas.views import esocial_compatibilidades_fpas_classificacoes_tributarias_listar as esocial_compatibilidades_fpas_classificacoes_tributarias_listar_views
from emensageriapro.tabelas.views import esocial_compatibilidades_fpas_classificacoes_tributarias_salvar as esocial_compatibilidades_fpas_classificacoes_tributarias_salvar_views
from emensageriapro.tabelas.views import esocial_compatibilidades_fpas_classificacoes_tributarias_api as esocial_compatibilidades_fpas_classificacoes_tributarias_api_views
from emensageriapro.tabelas.views import esocial_fatores_risco_apagar as esocial_fatores_risco_apagar_views
from emensageriapro.tabelas.views import esocial_fatores_risco_listar as esocial_fatores_risco_listar_views
from emensageriapro.tabelas.views import esocial_fatores_risco_salvar as esocial_fatores_risco_salvar_views
from emensageriapro.tabelas.views import esocial_fatores_risco_api as esocial_fatores_risco_api_views
from emensageriapro.tabelas.views import esocial_codificacoes_acidente_trabalho_apagar as esocial_codificacoes_acidente_trabalho_apagar_views
from emensageriapro.tabelas.views import esocial_codificacoes_acidente_trabalho_listar as esocial_codificacoes_acidente_trabalho_listar_views
from emensageriapro.tabelas.views import esocial_codificacoes_acidente_trabalho_salvar as esocial_codificacoes_acidente_trabalho_salvar_views
from emensageriapro.tabelas.views import esocial_codificacoes_acidente_trabalho_api as esocial_codificacoes_acidente_trabalho_api_views
from emensageriapro.tabelas.views import esocial_beneficios_previdenciarios_tipos_apagar as esocial_beneficios_previdenciarios_tipos_apagar_views
from emensageriapro.tabelas.views import esocial_beneficios_previdenciarios_tipos_listar as esocial_beneficios_previdenciarios_tipos_listar_views
from emensageriapro.tabelas.views import esocial_beneficios_previdenciarios_tipos_salvar as esocial_beneficios_previdenciarios_tipos_salvar_views
from emensageriapro.tabelas.views import esocial_beneficios_previdenciarios_tipos_api as esocial_beneficios_previdenciarios_tipos_api_views
from emensageriapro.tabelas.views import esocial_beneficios_previdenciarios_cessacao_motivos_apagar as esocial_beneficios_previdenciarios_cessacao_motivos_apagar_views
from emensageriapro.tabelas.views import esocial_beneficios_previdenciarios_cessacao_motivos_listar as esocial_beneficios_previdenciarios_cessacao_motivos_listar_views
from emensageriapro.tabelas.views import esocial_beneficios_previdenciarios_cessacao_motivos_salvar as esocial_beneficios_previdenciarios_cessacao_motivos_salvar_views
from emensageriapro.tabelas.views import esocial_beneficios_previdenciarios_cessacao_motivos_api as esocial_beneficios_previdenciarios_cessacao_motivos_api_views
from emensageriapro.tabelas.views import esocial_procedimentos_diagnosticos_apagar as esocial_procedimentos_diagnosticos_apagar_views
from emensageriapro.tabelas.views import esocial_procedimentos_diagnosticos_listar as esocial_procedimentos_diagnosticos_listar_views
from emensageriapro.tabelas.views import esocial_procedimentos_diagnosticos_salvar as esocial_procedimentos_diagnosticos_salvar_views
from emensageriapro.tabelas.views import esocial_procedimentos_diagnosticos_api as esocial_procedimentos_diagnosticos_api_views
from emensageriapro.tabelas.views import esocial_atividades_periculosas_insalubres_especiais_apagar as esocial_atividades_periculosas_insalubres_especiais_apagar_views
from emensageriapro.tabelas.views import esocial_atividades_periculosas_insalubres_especiais_listar as esocial_atividades_periculosas_insalubres_especiais_listar_views
from emensageriapro.tabelas.views import esocial_atividades_periculosas_insalubres_especiais_salvar as esocial_atividades_periculosas_insalubres_especiais_salvar_views
from emensageriapro.tabelas.views import esocial_atividades_periculosas_insalubres_especiais_api as esocial_atividades_periculosas_insalubres_especiais_api_views
from emensageriapro.tabelas.views import esocial_treinamentos_capacitacoes_exercicios_simulados_apagar as esocial_treinamentos_capacitacoes_exercicios_simulados_apagar_views
from emensageriapro.tabelas.views import esocial_treinamentos_capacitacoes_exercicios_simulados_listar as esocial_treinamentos_capacitacoes_exercicios_simulados_listar_views
from emensageriapro.tabelas.views import esocial_treinamentos_capacitacoes_exercicios_simulados_salvar as esocial_treinamentos_capacitacoes_exercicios_simulados_salvar_views
from emensageriapro.tabelas.views import esocial_treinamentos_capacitacoes_exercicios_simulados_api as esocial_treinamentos_capacitacoes_exercicios_simulados_api_views
from emensageriapro.tabelas.views import esocial_programas_planos_documentos_apagar as esocial_programas_planos_documentos_apagar_views
from emensageriapro.tabelas.views import esocial_programas_planos_documentos_listar as esocial_programas_planos_documentos_listar_views
from emensageriapro.tabelas.views import esocial_programas_planos_documentos_salvar as esocial_programas_planos_documentos_salvar_views
from emensageriapro.tabelas.views import esocial_programas_planos_documentos_api as esocial_programas_planos_documentos_api_views
from emensageriapro.tabelas.views import efdreinf_pagamentos_codigos_apagar as efdreinf_pagamentos_codigos_apagar_views
from emensageriapro.tabelas.views import efdreinf_pagamentos_codigos_listar as efdreinf_pagamentos_codigos_listar_views
from emensageriapro.tabelas.views import efdreinf_pagamentos_codigos_salvar as efdreinf_pagamentos_codigos_salvar_views
from emensageriapro.tabelas.views import efdreinf_pagamentos_codigos_api as efdreinf_pagamentos_codigos_api_views
from emensageriapro.tabelas.views import efdreinf_regras_pagamentos_codigos_apagar as efdreinf_regras_pagamentos_codigos_apagar_views
from emensageriapro.tabelas.views import efdreinf_regras_pagamentos_codigos_listar as efdreinf_regras_pagamentos_codigos_listar_views
from emensageriapro.tabelas.views import efdreinf_regras_pagamentos_codigos_salvar as efdreinf_regras_pagamentos_codigos_salvar_views
from emensageriapro.tabelas.views import efdreinf_regras_pagamentos_codigos_api as efdreinf_regras_pagamentos_codigos_api_views
from emensageriapro.tabelas.views import efdreinf_rendimentos_beneficiarios_exterior_apagar as efdreinf_rendimentos_beneficiarios_exterior_apagar_views
from emensageriapro.tabelas.views import efdreinf_rendimentos_beneficiarios_exterior_listar as efdreinf_rendimentos_beneficiarios_exterior_listar_views
from emensageriapro.tabelas.views import efdreinf_rendimentos_beneficiarios_exterior_salvar as efdreinf_rendimentos_beneficiarios_exterior_salvar_views
from emensageriapro.tabelas.views import efdreinf_rendimentos_beneficiarios_exterior_api as efdreinf_rendimentos_beneficiarios_exterior_api_views
from emensageriapro.tabelas.views import efdreinf_rendimentos_beneficiarios_exterior_tributacao_apagar as efdreinf_rendimentos_beneficiarios_exterior_tributacao_apagar_views
from emensageriapro.tabelas.views import efdreinf_rendimentos_beneficiarios_exterior_tributacao_listar as efdreinf_rendimentos_beneficiarios_exterior_tributacao_listar_views
from emensageriapro.tabelas.views import efdreinf_rendimentos_beneficiarios_exterior_tributacao_salvar as efdreinf_rendimentos_beneficiarios_exterior_tributacao_salvar_views
from emensageriapro.tabelas.views import efdreinf_rendimentos_beneficiarios_exterior_tributacao_api as efdreinf_rendimentos_beneficiarios_exterior_tributacao_api_views
from emensageriapro.tabelas.views import efdreinf_informacoes_beneficiarios_exterior_apagar as efdreinf_informacoes_beneficiarios_exterior_apagar_views
from emensageriapro.tabelas.views import efdreinf_informacoes_beneficiarios_exterior_listar as efdreinf_informacoes_beneficiarios_exterior_listar_views
from emensageriapro.tabelas.views import efdreinf_informacoes_beneficiarios_exterior_salvar as efdreinf_informacoes_beneficiarios_exterior_salvar_views
from emensageriapro.tabelas.views import efdreinf_informacoes_beneficiarios_exterior_api as efdreinf_informacoes_beneficiarios_exterior_api_views
from emensageriapro.tabelas.views import efdreinf_classificacao_servicos_prestados_apagar as efdreinf_classificacao_servicos_prestados_apagar_views
from emensageriapro.tabelas.views import efdreinf_classificacao_servicos_prestados_listar as efdreinf_classificacao_servicos_prestados_listar_views
from emensageriapro.tabelas.views import efdreinf_classificacao_servicos_prestados_salvar as efdreinf_classificacao_servicos_prestados_salvar_views
from emensageriapro.tabelas.views import efdreinf_classificacao_servicos_prestados_api as efdreinf_classificacao_servicos_prestados_api_views
from emensageriapro.tabelas.views import efdreinf_paises_apagar as efdreinf_paises_apagar_views
from emensageriapro.tabelas.views import efdreinf_paises_listar as efdreinf_paises_listar_views
from emensageriapro.tabelas.views import efdreinf_paises_salvar as efdreinf_paises_salvar_views
from emensageriapro.tabelas.views import efdreinf_paises_api as efdreinf_paises_api_views
from emensageriapro.tabelas.views import efdreinf_classificacao_tributaria_apagar as efdreinf_classificacao_tributaria_apagar_views
from emensageriapro.tabelas.views import efdreinf_classificacao_tributaria_listar as efdreinf_classificacao_tributaria_listar_views
from emensageriapro.tabelas.views import efdreinf_classificacao_tributaria_salvar as efdreinf_classificacao_tributaria_salvar_views
from emensageriapro.tabelas.views import efdreinf_classificacao_tributaria_api as efdreinf_classificacao_tributaria_api_views
from emensageriapro.tabelas.views import efdreinf_codigos_atividades_produtos_servicos_cprb_apagar as efdreinf_codigos_atividades_produtos_servicos_cprb_apagar_views
from emensageriapro.tabelas.views import efdreinf_codigos_atividades_produtos_servicos_cprb_listar as efdreinf_codigos_atividades_produtos_servicos_cprb_listar_views
from emensageriapro.tabelas.views import efdreinf_codigos_atividades_produtos_servicos_cprb_salvar as efdreinf_codigos_atividades_produtos_servicos_cprb_salvar_views
from emensageriapro.tabelas.views import efdreinf_codigos_atividades_produtos_servicos_cprb_api as efdreinf_codigos_atividades_produtos_servicos_cprb_api_views
from emensageriapro.tabelas.views import efdreinf_eventos_apagar as efdreinf_eventos_apagar_views
from emensageriapro.tabelas.views import efdreinf_eventos_listar as efdreinf_eventos_listar_views
from emensageriapro.tabelas.views import efdreinf_eventos_salvar as efdreinf_eventos_salvar_views
from emensageriapro.tabelas.views import efdreinf_eventos_api as efdreinf_eventos_api_views



"""

    eMensageria - Sistema Open-Source de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""


urlpatterns = [


    url(r'^municipios/apagar/(?P<hash>.*)/$', 
        municipios_apagar_views.apagar, 
        name='municipios_apagar'),

    url(r'^municipios/api/$',
        municipios_api_views.MunicipiosList.as_view() ),

    url(r'^municipios/api/(?P<pk>[0-9]+)/$',
        municipios_api_views.MunicipiosDetail.as_view() ),

    url(r'^municipios/listar/(?P<hash>.*)/$', 
        municipios_listar_views.listar, 
        name='municipios'),
        
    url(r'^municipios/json-search/(?P<search>[\w ]+)/$', 
        municipios_api_views.json_search, 
        name='municipios_json_search'),

    url(r'^municipios/salvar/(?P<hash>.*)/$', 
        municipios_salvar_views.salvar, 
        name='municipios_salvar'),

    url(r'^cbo/apagar/(?P<hash>.*)/$', 
        cbo_apagar_views.apagar, 
        name='cbo_apagar'),

    url(r'^cbo/api/$',
        cbo_api_views.CBOList.as_view() ),

    url(r'^cbo/api/(?P<pk>[0-9]+)/$',
        cbo_api_views.CBODetail.as_view() ),

    url(r'^cbo/listar/(?P<hash>.*)/$', 
        cbo_listar_views.listar, 
        name='cbo'),
        
    url(r'^cbo/json-search/(?P<search>[\w ]+)/$', 
        cbo_api_views.json_search, 
        name='cbo_json_search'),

    url(r'^cbo/salvar/(?P<hash>.*)/$', 
        cbo_salvar_views.salvar, 
        name='cbo_salvar'),

    url(r'^cid/apagar/(?P<hash>.*)/$', 
        cid_apagar_views.apagar, 
        name='cid_apagar'),

    url(r'^cid/api/$',
        cid_api_views.CIDList.as_view() ),

    url(r'^cid/api/(?P<pk>[0-9]+)/$',
        cid_api_views.CIDDetail.as_view() ),

    url(r'^cid/listar/(?P<hash>.*)/$', 
        cid_listar_views.listar, 
        name='cid'),
        
    url(r'^cid/json-search/(?P<search>[\w ]+)/$', 
        cid_api_views.json_search, 
        name='cid_json_search'),

    url(r'^cid/salvar/(?P<hash>.*)/$', 
        cid_salvar_views.salvar, 
        name='cid_salvar'),

    url(r'^cnae/apagar/(?P<hash>.*)/$', 
        cnae_apagar_views.apagar, 
        name='cnae_apagar'),

    url(r'^cnae/api/$',
        cnae_api_views.CNAEList.as_view() ),

    url(r'^cnae/api/(?P<pk>[0-9]+)/$',
        cnae_api_views.CNAEDetail.as_view() ),

    url(r'^cnae/listar/(?P<hash>.*)/$', 
        cnae_listar_views.listar, 
        name='cnae'),
        
    url(r'^cnae/json-search/(?P<search>[\w ]+)/$', 
        cnae_api_views.json_search, 
        name='cnae_json_search'),

    url(r'^cnae/salvar/(?P<hash>.*)/$', 
        cnae_salvar_views.salvar, 
        name='cnae_salvar'),

    url(r'^esocial-trabalhadores-categorias/apagar/(?P<hash>.*)/$', 
        esocial_trabalhadores_categorias_apagar_views.apagar, 
        name='esocial_trabalhadores_categorias_apagar'),

    url(r'^esocial-trabalhadores-categorias/api/$',
        esocial_trabalhadores_categorias_api_views.eSocialTrabalhadoresCategoriasList.as_view() ),

    url(r'^esocial-trabalhadores-categorias/api/(?P<pk>[0-9]+)/$',
        esocial_trabalhadores_categorias_api_views.eSocialTrabalhadoresCategoriasDetail.as_view() ),

    url(r'^esocial-trabalhadores-categorias/listar/(?P<hash>.*)/$', 
        esocial_trabalhadores_categorias_listar_views.listar, 
        name='esocial_trabalhadores_categorias'),
        
    url(r'^esocial-trabalhadores-categorias/json-search/(?P<search>[\w ]+)/$', 
        esocial_trabalhadores_categorias_api_views.json_search, 
        name='esocial_trabalhadores_categorias_json_search'),

    url(r'^esocial-trabalhadores-categorias/salvar/(?P<hash>.*)/$', 
        esocial_trabalhadores_categorias_salvar_views.salvar, 
        name='esocial_trabalhadores_categorias_salvar'),

    url(r'^esocial-financiamentos-aposentadorias-especiais/apagar/(?P<hash>.*)/$', 
        esocial_financiamentos_aposentadorias_especiais_apagar_views.apagar, 
        name='esocial_financiamentos_aposentadorias_especiais_apagar'),

    url(r'^esocial-financiamentos-aposentadorias-especiais/api/$',
        esocial_financiamentos_aposentadorias_especiais_api_views.eSocialFinanciamentosAposentadoriasEspeciaisList.as_view() ),

    url(r'^esocial-financiamentos-aposentadorias-especiais/api/(?P<pk>[0-9]+)/$',
        esocial_financiamentos_aposentadorias_especiais_api_views.eSocialFinanciamentosAposentadoriasEspeciaisDetail.as_view() ),

    url(r'^esocial-financiamentos-aposentadorias-especiais/listar/(?P<hash>.*)/$', 
        esocial_financiamentos_aposentadorias_especiais_listar_views.listar, 
        name='esocial_financiamentos_aposentadorias_especiais'),
        
    url(r'^esocial-financiamentos-aposentadorias-especiais/json-search/(?P<search>[\w ]+)/$', 
        esocial_financiamentos_aposentadorias_especiais_api_views.json_search, 
        name='esocial_financiamentos_aposentadorias_especiais_json_search'),

    url(r'^esocial-financiamentos-aposentadorias-especiais/salvar/(?P<hash>.*)/$', 
        esocial_financiamentos_aposentadorias_especiais_salvar_views.salvar, 
        name='esocial_financiamentos_aposentadorias_especiais_salvar'),

    url(r'^esocial-naturezas-rubricas/apagar/(?P<hash>.*)/$', 
        esocial_naturezas_rubricas_apagar_views.apagar, 
        name='esocial_naturezas_rubricas_apagar'),

    url(r'^esocial-naturezas-rubricas/api/$',
        esocial_naturezas_rubricas_api_views.eSocialNaturezasRubricasList.as_view() ),

    url(r'^esocial-naturezas-rubricas/api/(?P<pk>[0-9]+)/$',
        esocial_naturezas_rubricas_api_views.eSocialNaturezasRubricasDetail.as_view() ),

    url(r'^esocial-naturezas-rubricas/listar/(?P<hash>.*)/$', 
        esocial_naturezas_rubricas_listar_views.listar, 
        name='esocial_naturezas_rubricas'),
        
    url(r'^esocial-naturezas-rubricas/json-search/(?P<search>[\w ]+)/$', 
        esocial_naturezas_rubricas_api_views.json_search, 
        name='esocial_naturezas_rubricas_json_search'),

    url(r'^esocial-naturezas-rubricas/salvar/(?P<hash>.*)/$', 
        esocial_naturezas_rubricas_salvar_views.salvar, 
        name='esocial_naturezas_rubricas_salvar'),

    url(r'^esocial-codigo-aliquotas-fpas-terceiros/apagar/(?P<hash>.*)/$', 
        esocial_codigo_aliquotas_fpas_terceiros_apagar_views.apagar, 
        name='esocial_codigo_aliquotas_fpas_terceiros_apagar'),

    url(r'^esocial-codigo-aliquotas-fpas-terceiros/api/$',
        esocial_codigo_aliquotas_fpas_terceiros_api_views.eSocialCodigoAliquotasFPASTerceirosList.as_view() ),

    url(r'^esocial-codigo-aliquotas-fpas-terceiros/api/(?P<pk>[0-9]+)/$',
        esocial_codigo_aliquotas_fpas_terceiros_api_views.eSocialCodigoAliquotasFPASTerceirosDetail.as_view() ),

    url(r'^esocial-codigo-aliquotas-fpas-terceiros/listar/(?P<hash>.*)/$', 
        esocial_codigo_aliquotas_fpas_terceiros_listar_views.listar, 
        name='esocial_codigo_aliquotas_fpas_terceiros'),
        
    url(r'^esocial-codigo-aliquotas-fpas-terceiros/json-search/(?P<search>[\w ]+)/$', 
        esocial_codigo_aliquotas_fpas_terceiros_api_views.json_search, 
        name='esocial_codigo_aliquotas_fpas_terceiros_json_search'),

    url(r'^esocial-codigo-aliquotas-fpas-terceiros/salvar/(?P<hash>.*)/$', 
        esocial_codigo_aliquotas_fpas_terceiros_salvar_views.salvar, 
        name='esocial_codigo_aliquotas_fpas_terceiros_salvar'),

    url(r'^esocial-inscricoes-tipos/apagar/(?P<hash>.*)/$', 
        esocial_inscricoes_tipos_apagar_views.apagar, 
        name='esocial_inscricoes_tipos_apagar'),

    url(r'^esocial-inscricoes-tipos/api/$',
        esocial_inscricoes_tipos_api_views.eSocialInscricoesTiposList.as_view() ),

    url(r'^esocial-inscricoes-tipos/api/(?P<pk>[0-9]+)/$',
        esocial_inscricoes_tipos_api_views.eSocialInscricoesTiposDetail.as_view() ),

    url(r'^esocial-inscricoes-tipos/listar/(?P<hash>.*)/$', 
        esocial_inscricoes_tipos_listar_views.listar, 
        name='esocial_inscricoes_tipos'),
        
    url(r'^esocial-inscricoes-tipos/json-search/(?P<search>[\w ]+)/$', 
        esocial_inscricoes_tipos_api_views.json_search, 
        name='esocial_inscricoes_tipos_json_search'),

    url(r'^esocial-inscricoes-tipos/salvar/(?P<hash>.*)/$', 
        esocial_inscricoes_tipos_salvar_views.salvar, 
        name='esocial_inscricoes_tipos_salvar'),

    url(r'^esocial-paises/apagar/(?P<hash>.*)/$', 
        esocial_paises_apagar_views.apagar, 
        name='esocial_paises_apagar'),

    url(r'^esocial-paises/api/$',
        esocial_paises_api_views.eSocialPaisesList.as_view() ),

    url(r'^esocial-paises/api/(?P<pk>[0-9]+)/$',
        esocial_paises_api_views.eSocialPaisesDetail.as_view() ),

    url(r'^esocial-paises/listar/(?P<hash>.*)/$', 
        esocial_paises_listar_views.listar, 
        name='esocial_paises'),
        
    url(r'^esocial-paises/json-search/(?P<search>[\w ]+)/$', 
        esocial_paises_api_views.json_search, 
        name='esocial_paises_json_search'),

    url(r'^esocial-paises/salvar/(?P<hash>.*)/$', 
        esocial_paises_salvar_views.salvar, 
        name='esocial_paises_salvar'),

    url(r'^esocial-dependentes-tipos/apagar/(?P<hash>.*)/$', 
        esocial_dependentes_tipos_apagar_views.apagar, 
        name='esocial_dependentes_tipos_apagar'),

    url(r'^esocial-dependentes-tipos/api/$',
        esocial_dependentes_tipos_api_views.eSocialDependentesTiposList.as_view() ),

    url(r'^esocial-dependentes-tipos/api/(?P<pk>[0-9]+)/$',
        esocial_dependentes_tipos_api_views.eSocialDependentesTiposDetail.as_view() ),

    url(r'^esocial-dependentes-tipos/listar/(?P<hash>.*)/$', 
        esocial_dependentes_tipos_listar_views.listar, 
        name='esocial_dependentes_tipos'),
        
    url(r'^esocial-dependentes-tipos/json-search/(?P<search>[\w ]+)/$', 
        esocial_dependentes_tipos_api_views.json_search, 
        name='esocial_dependentes_tipos_json_search'),

    url(r'^esocial-dependentes-tipos/salvar/(?P<hash>.*)/$', 
        esocial_dependentes_tipos_salvar_views.salvar, 
        name='esocial_dependentes_tipos_salvar'),

    url(r'^esocial-classificacoes-tributarias/apagar/(?P<hash>.*)/$', 
        esocial_classificacoes_tributarias_apagar_views.apagar, 
        name='esocial_classificacoes_tributarias_apagar'),

    url(r'^esocial-classificacoes-tributarias/api/$',
        esocial_classificacoes_tributarias_api_views.eSocialClassificacoesTributariasList.as_view() ),

    url(r'^esocial-classificacoes-tributarias/api/(?P<pk>[0-9]+)/$',
        esocial_classificacoes_tributarias_api_views.eSocialClassificacoesTributariasDetail.as_view() ),

    url(r'^esocial-classificacoes-tributarias/listar/(?P<hash>.*)/$', 
        esocial_classificacoes_tributarias_listar_views.listar, 
        name='esocial_classificacoes_tributarias'),
        
    url(r'^esocial-classificacoes-tributarias/json-search/(?P<search>[\w ]+)/$', 
        esocial_classificacoes_tributarias_api_views.json_search, 
        name='esocial_classificacoes_tributarias_json_search'),

    url(r'^esocial-classificacoes-tributarias/salvar/(?P<hash>.*)/$', 
        esocial_classificacoes_tributarias_salvar_views.salvar, 
        name='esocial_classificacoes_tributarias_salvar'),

    url(r'^esocial-arquivos-esocial-tipos/apagar/(?P<hash>.*)/$', 
        esocial_arquivos_esocial_tipos_apagar_views.apagar, 
        name='esocial_arquivos_esocial_tipos_apagar'),

    url(r'^esocial-arquivos-esocial-tipos/api/$',
        esocial_arquivos_esocial_tipos_api_views.eSocialArquivosEsocialTiposList.as_view() ),

    url(r'^esocial-arquivos-esocial-tipos/api/(?P<pk>[0-9]+)/$',
        esocial_arquivos_esocial_tipos_api_views.eSocialArquivosEsocialTiposDetail.as_view() ),

    url(r'^esocial-arquivos-esocial-tipos/listar/(?P<hash>.*)/$', 
        esocial_arquivos_esocial_tipos_listar_views.listar, 
        name='esocial_arquivos_esocial_tipos'),
        
    url(r'^esocial-arquivos-esocial-tipos/json-search/(?P<search>[\w ]+)/$', 
        esocial_arquivos_esocial_tipos_api_views.json_search, 
        name='esocial_arquivos_esocial_tipos_json_search'),

    url(r'^esocial-arquivos-esocial-tipos/salvar/(?P<hash>.*)/$', 
        esocial_arquivos_esocial_tipos_salvar_views.salvar, 
        name='esocial_arquivos_esocial_tipos_salvar'),

    url(r'^esocial-lotacoes-tributarias-tipos/apagar/(?P<hash>.*)/$', 
        esocial_lotacoes_tributarias_tipos_apagar_views.apagar, 
        name='esocial_lotacoes_tributarias_tipos_apagar'),

    url(r'^esocial-lotacoes-tributarias-tipos/api/$',
        esocial_lotacoes_tributarias_tipos_api_views.eSocialLotacoesTributariasTiposList.as_view() ),

    url(r'^esocial-lotacoes-tributarias-tipos/api/(?P<pk>[0-9]+)/$',
        esocial_lotacoes_tributarias_tipos_api_views.eSocialLotacoesTributariasTiposDetail.as_view() ),

    url(r'^esocial-lotacoes-tributarias-tipos/listar/(?P<hash>.*)/$', 
        esocial_lotacoes_tributarias_tipos_listar_views.listar, 
        name='esocial_lotacoes_tributarias_tipos'),
        
    url(r'^esocial-lotacoes-tributarias-tipos/json-search/(?P<search>[\w ]+)/$', 
        esocial_lotacoes_tributarias_tipos_api_views.json_search, 
        name='esocial_lotacoes_tributarias_tipos_json_search'),

    url(r'^esocial-lotacoes-tributarias-tipos/salvar/(?P<hash>.*)/$', 
        esocial_lotacoes_tributarias_tipos_salvar_views.salvar, 
        name='esocial_lotacoes_tributarias_tipos_salvar'),

    url(r'^esocial-compatibilidades-categorias-classificacoes-lotacoes/apagar/(?P<hash>.*)/$', 
        esocial_compatibilidades_categorias_classificacoes_lotacoes_apagar_views.apagar, 
        name='esocial_compatibilidades_categorias_classificacoes_lotacoes_apagar'),

    url(r'^esocial-compatibilidades-categorias-classificacoes-lotacoes/api/$',
        esocial_compatibilidades_categorias_classificacoes_lotacoes_api_views.eSocialCompatibilidadesCategoriasClassificacoesLotacoesList.as_view() ),

    url(r'^esocial-compatibilidades-categorias-classificacoes-lotacoes/api/(?P<pk>[0-9]+)/$',
        esocial_compatibilidades_categorias_classificacoes_lotacoes_api_views.eSocialCompatibilidadesCategoriasClassificacoesLotacoesDetail.as_view() ),

    url(r'^esocial-compatibilidades-categorias-classificacoes-lotacoes/listar/(?P<hash>.*)/$', 
        esocial_compatibilidades_categorias_classificacoes_lotacoes_listar_views.listar, 
        name='esocial_compatibilidades_categorias_classificacoes_lotacoes'),
        
    url(r'^esocial-compatibilidades-categorias-classificacoes-lotacoes/json-search/(?P<search>[\w ]+)/$', 
        esocial_compatibilidades_categorias_classificacoes_lotacoes_api_views.json_search, 
        name='esocial_compatibilidades_categorias_classificacoes_lotacoes_json_search'),

    url(r'^esocial-compatibilidades-categorias-classificacoes-lotacoes/salvar/(?P<hash>.*)/$', 
        esocial_compatibilidades_categorias_classificacoes_lotacoes_salvar_views.salvar, 
        name='esocial_compatibilidades_categorias_classificacoes_lotacoes_salvar'),

    url(r'^esocial-compatibilidades-lotacoes-classificacoes/apagar/(?P<hash>.*)/$', 
        esocial_compatibilidades_lotacoes_classificacoes_apagar_views.apagar, 
        name='esocial_compatibilidades_lotacoes_classificacoes_apagar'),

    url(r'^esocial-compatibilidades-lotacoes-classificacoes/api/$',
        esocial_compatibilidades_lotacoes_classificacoes_api_views.eSocialCompatibilidadesLotacoesClassificacoesList.as_view() ),

    url(r'^esocial-compatibilidades-lotacoes-classificacoes/api/(?P<pk>[0-9]+)/$',
        esocial_compatibilidades_lotacoes_classificacoes_api_views.eSocialCompatibilidadesLotacoesClassificacoesDetail.as_view() ),

    url(r'^esocial-compatibilidades-lotacoes-classificacoes/listar/(?P<hash>.*)/$', 
        esocial_compatibilidades_lotacoes_classificacoes_listar_views.listar, 
        name='esocial_compatibilidades_lotacoes_classificacoes'),
        
    url(r'^esocial-compatibilidades-lotacoes-classificacoes/json-search/(?P<search>[\w ]+)/$', 
        esocial_compatibilidades_lotacoes_classificacoes_api_views.json_search, 
        name='esocial_compatibilidades_lotacoes_classificacoes_json_search'),

    url(r'^esocial-compatibilidades-lotacoes-classificacoes/salvar/(?P<hash>.*)/$', 
        esocial_compatibilidades_lotacoes_classificacoes_salvar_views.salvar, 
        name='esocial_compatibilidades_lotacoes_classificacoes_salvar'),

    url(r'^esocial-partes-corpo-atingidas/apagar/(?P<hash>.*)/$', 
        esocial_partes_corpo_atingidas_apagar_views.apagar, 
        name='esocial_partes_corpo_atingidas_apagar'),

    url(r'^esocial-partes-corpo-atingidas/api/$',
        esocial_partes_corpo_atingidas_api_views.eSocialPartesCorpoAtingidasList.as_view() ),

    url(r'^esocial-partes-corpo-atingidas/api/(?P<pk>[0-9]+)/$',
        esocial_partes_corpo_atingidas_api_views.eSocialPartesCorpoAtingidasDetail.as_view() ),

    url(r'^esocial-partes-corpo-atingidas/listar/(?P<hash>.*)/$', 
        esocial_partes_corpo_atingidas_listar_views.listar, 
        name='esocial_partes_corpo_atingidas'),
        
    url(r'^esocial-partes-corpo-atingidas/json-search/(?P<search>[\w ]+)/$', 
        esocial_partes_corpo_atingidas_api_views.json_search, 
        name='esocial_partes_corpo_atingidas_json_search'),

    url(r'^esocial-partes-corpo-atingidas/salvar/(?P<hash>.*)/$', 
        esocial_partes_corpo_atingidas_salvar_views.salvar, 
        name='esocial_partes_corpo_atingidas_salvar'),

    url(r'^esocial-agentes-causadores-acidentes-trabalho/apagar/(?P<hash>.*)/$', 
        esocial_agentes_causadores_acidentes_trabalho_apagar_views.apagar, 
        name='esocial_agentes_causadores_acidentes_trabalho_apagar'),

    url(r'^esocial-agentes-causadores-acidentes-trabalho/api/$',
        esocial_agentes_causadores_acidentes_trabalho_api_views.eSocialAgentesCausadoresAcidentesTrabalhoList.as_view() ),

    url(r'^esocial-agentes-causadores-acidentes-trabalho/api/(?P<pk>[0-9]+)/$',
        esocial_agentes_causadores_acidentes_trabalho_api_views.eSocialAgentesCausadoresAcidentesTrabalhoDetail.as_view() ),

    url(r'^esocial-agentes-causadores-acidentes-trabalho/listar/(?P<hash>.*)/$', 
        esocial_agentes_causadores_acidentes_trabalho_listar_views.listar, 
        name='esocial_agentes_causadores_acidentes_trabalho'),
        
    url(r'^esocial-agentes-causadores-acidentes-trabalho/json-search/(?P<search>[\w ]+)/$', 
        esocial_agentes_causadores_acidentes_trabalho_api_views.json_search, 
        name='esocial_agentes_causadores_acidentes_trabalho_json_search'),

    url(r'^esocial-agentes-causadores-acidentes-trabalho/salvar/(?P<hash>.*)/$', 
        esocial_agentes_causadores_acidentes_trabalho_salvar_views.salvar, 
        name='esocial_agentes_causadores_acidentes_trabalho_salvar'),

    url(r'^esocial-agentes-causadores-doencas-profissionais/apagar/(?P<hash>.*)/$', 
        esocial_agentes_causadores_doencas_profissionais_apagar_views.apagar, 
        name='esocial_agentes_causadores_doencas_profissionais_apagar'),

    url(r'^esocial-agentes-causadores-doencas-profissionais/api/$',
        esocial_agentes_causadores_doencas_profissionais_api_views.eSocialAgentesCausadoresDoencasProfissionaisList.as_view() ),

    url(r'^esocial-agentes-causadores-doencas-profissionais/api/(?P<pk>[0-9]+)/$',
        esocial_agentes_causadores_doencas_profissionais_api_views.eSocialAgentesCausadoresDoencasProfissionaisDetail.as_view() ),

    url(r'^esocial-agentes-causadores-doencas-profissionais/listar/(?P<hash>.*)/$', 
        esocial_agentes_causadores_doencas_profissionais_listar_views.listar, 
        name='esocial_agentes_causadores_doencas_profissionais'),
        
    url(r'^esocial-agentes-causadores-doencas-profissionais/json-search/(?P<search>[\w ]+)/$', 
        esocial_agentes_causadores_doencas_profissionais_api_views.json_search, 
        name='esocial_agentes_causadores_doencas_profissionais_json_search'),

    url(r'^esocial-agentes-causadores-doencas-profissionais/salvar/(?P<hash>.*)/$', 
        esocial_agentes_causadores_doencas_profissionais_salvar_views.salvar, 
        name='esocial_agentes_causadores_doencas_profissionais_salvar'),

    url(r'^esocial-acidentes-situacoes-geradoras/apagar/(?P<hash>.*)/$', 
        esocial_acidentes_situacoes_geradoras_apagar_views.apagar, 
        name='esocial_acidentes_situacoes_geradoras_apagar'),

    url(r'^esocial-acidentes-situacoes-geradoras/api/$',
        esocial_acidentes_situacoes_geradoras_api_views.eSocialAcidentesSituacoesGeradorasList.as_view() ),

    url(r'^esocial-acidentes-situacoes-geradoras/api/(?P<pk>[0-9]+)/$',
        esocial_acidentes_situacoes_geradoras_api_views.eSocialAcidentesSituacoesGeradorasDetail.as_view() ),

    url(r'^esocial-acidentes-situacoes-geradoras/listar/(?P<hash>.*)/$', 
        esocial_acidentes_situacoes_geradoras_listar_views.listar, 
        name='esocial_acidentes_situacoes_geradoras'),
        
    url(r'^esocial-acidentes-situacoes-geradoras/json-search/(?P<search>[\w ]+)/$', 
        esocial_acidentes_situacoes_geradoras_api_views.json_search, 
        name='esocial_acidentes_situacoes_geradoras_json_search'),

    url(r'^esocial-acidentes-situacoes-geradoras/salvar/(?P<hash>.*)/$', 
        esocial_acidentes_situacoes_geradoras_salvar_views.salvar, 
        name='esocial_acidentes_situacoes_geradoras_salvar'),

    url(r'^esocial-naturezas-lesoes/apagar/(?P<hash>.*)/$', 
        esocial_naturezas_lesoes_apagar_views.apagar, 
        name='esocial_naturezas_lesoes_apagar'),

    url(r'^esocial-naturezas-lesoes/api/$',
        esocial_naturezas_lesoes_api_views.eSocialNaturezasLesoesList.as_view() ),

    url(r'^esocial-naturezas-lesoes/api/(?P<pk>[0-9]+)/$',
        esocial_naturezas_lesoes_api_views.eSocialNaturezasLesoesDetail.as_view() ),

    url(r'^esocial-naturezas-lesoes/listar/(?P<hash>.*)/$', 
        esocial_naturezas_lesoes_listar_views.listar, 
        name='esocial_naturezas_lesoes'),
        
    url(r'^esocial-naturezas-lesoes/json-search/(?P<search>[\w ]+)/$', 
        esocial_naturezas_lesoes_api_views.json_search, 
        name='esocial_naturezas_lesoes_json_search'),

    url(r'^esocial-naturezas-lesoes/salvar/(?P<hash>.*)/$', 
        esocial_naturezas_lesoes_salvar_views.salvar, 
        name='esocial_naturezas_lesoes_salvar'),

    url(r'^esocial-afastamentos-motivos/apagar/(?P<hash>.*)/$', 
        esocial_afastamentos_motivos_apagar_views.apagar, 
        name='esocial_afastamentos_motivos_apagar'),

    url(r'^esocial-afastamentos-motivos/api/$',
        esocial_afastamentos_motivos_api_views.eSocialAfastamentosMotivosList.as_view() ),

    url(r'^esocial-afastamentos-motivos/api/(?P<pk>[0-9]+)/$',
        esocial_afastamentos_motivos_api_views.eSocialAfastamentosMotivosDetail.as_view() ),

    url(r'^esocial-afastamentos-motivos/listar/(?P<hash>.*)/$', 
        esocial_afastamentos_motivos_listar_views.listar, 
        name='esocial_afastamentos_motivos'),
        
    url(r'^esocial-afastamentos-motivos/json-search/(?P<search>[\w ]+)/$', 
        esocial_afastamentos_motivos_api_views.json_search, 
        name='esocial_afastamentos_motivos_json_search'),

    url(r'^esocial-afastamentos-motivos/salvar/(?P<hash>.*)/$', 
        esocial_afastamentos_motivos_salvar_views.salvar, 
        name='esocial_afastamentos_motivos_salvar'),

    url(r'^esocial-desligamentos-motivos/apagar/(?P<hash>.*)/$', 
        esocial_desligamentos_motivos_apagar_views.apagar, 
        name='esocial_desligamentos_motivos_apagar'),

    url(r'^esocial-desligamentos-motivos/api/$',
        esocial_desligamentos_motivos_api_views.eSocialDesligamentosMotivosList.as_view() ),

    url(r'^esocial-desligamentos-motivos/api/(?P<pk>[0-9]+)/$',
        esocial_desligamentos_motivos_api_views.eSocialDesligamentosMotivosDetail.as_view() ),

    url(r'^esocial-desligamentos-motivos/listar/(?P<hash>.*)/$', 
        esocial_desligamentos_motivos_listar_views.listar, 
        name='esocial_desligamentos_motivos'),
        
    url(r'^esocial-desligamentos-motivos/json-search/(?P<search>[\w ]+)/$', 
        esocial_desligamentos_motivos_api_views.json_search, 
        name='esocial_desligamentos_motivos_json_search'),

    url(r'^esocial-desligamentos-motivos/salvar/(?P<hash>.*)/$', 
        esocial_desligamentos_motivos_salvar_views.salvar, 
        name='esocial_desligamentos_motivos_salvar'),

    url(r'^esocial-logradouros-tipos/apagar/(?P<hash>.*)/$', 
        esocial_logradouros_tipos_apagar_views.apagar, 
        name='esocial_logradouros_tipos_apagar'),

    url(r'^esocial-logradouros-tipos/api/$',
        esocial_logradouros_tipos_api_views.eSocialLogradourosTiposList.as_view() ),

    url(r'^esocial-logradouros-tipos/api/(?P<pk>[0-9]+)/$',
        esocial_logradouros_tipos_api_views.eSocialLogradourosTiposDetail.as_view() ),

    url(r'^esocial-logradouros-tipos/listar/(?P<hash>.*)/$', 
        esocial_logradouros_tipos_listar_views.listar, 
        name='esocial_logradouros_tipos'),
        
    url(r'^esocial-logradouros-tipos/json-search/(?P<search>[\w ]+)/$', 
        esocial_logradouros_tipos_api_views.json_search, 
        name='esocial_logradouros_tipos_json_search'),

    url(r'^esocial-logradouros-tipos/salvar/(?P<hash>.*)/$', 
        esocial_logradouros_tipos_salvar_views.salvar, 
        name='esocial_logradouros_tipos_salvar'),

    url(r'^esocial-naturezas-juridicas/apagar/(?P<hash>.*)/$', 
        esocial_naturezas_juridicas_apagar_views.apagar, 
        name='esocial_naturezas_juridicas_apagar'),

    url(r'^esocial-naturezas-juridicas/api/$',
        esocial_naturezas_juridicas_api_views.eSocialNaturezasJuridicasList.as_view() ),

    url(r'^esocial-naturezas-juridicas/api/(?P<pk>[0-9]+)/$',
        esocial_naturezas_juridicas_api_views.eSocialNaturezasJuridicasDetail.as_view() ),

    url(r'^esocial-naturezas-juridicas/listar/(?P<hash>.*)/$', 
        esocial_naturezas_juridicas_listar_views.listar, 
        name='esocial_naturezas_juridicas'),
        
    url(r'^esocial-naturezas-juridicas/json-search/(?P<search>[\w ]+)/$', 
        esocial_naturezas_juridicas_api_views.json_search, 
        name='esocial_naturezas_juridicas_json_search'),

    url(r'^esocial-naturezas-juridicas/salvar/(?P<hash>.*)/$', 
        esocial_naturezas_juridicas_salvar_views.salvar, 
        name='esocial_naturezas_juridicas_salvar'),

    url(r'^esocial-compatibilidades-fpas-classificacoes-tributarias/apagar/(?P<hash>.*)/$', 
        esocial_compatibilidades_fpas_classificacoes_tributarias_apagar_views.apagar, 
        name='esocial_compatibilidades_fpas_classificacoes_tributarias_apagar'),

    url(r'^esocial-compatibilidades-fpas-classificacoes-tributarias/api/$',
        esocial_compatibilidades_fpas_classificacoes_tributarias_api_views.eSocialCompatibilidadesFPASClassificacoesTributariasList.as_view() ),

    url(r'^esocial-compatibilidades-fpas-classificacoes-tributarias/api/(?P<pk>[0-9]+)/$',
        esocial_compatibilidades_fpas_classificacoes_tributarias_api_views.eSocialCompatibilidadesFPASClassificacoesTributariasDetail.as_view() ),

    url(r'^esocial-compatibilidades-fpas-classificacoes-tributarias/listar/(?P<hash>.*)/$', 
        esocial_compatibilidades_fpas_classificacoes_tributarias_listar_views.listar, 
        name='esocial_compatibilidades_fpas_classificacoes_tributarias'),
        
    url(r'^esocial-compatibilidades-fpas-classificacoes-tributarias/json-search/(?P<search>[\w ]+)/$', 
        esocial_compatibilidades_fpas_classificacoes_tributarias_api_views.json_search, 
        name='esocial_compatibilidades_fpas_classificacoes_tributarias_json_search'),

    url(r'^esocial-compatibilidades-fpas-classificacoes-tributarias/salvar/(?P<hash>.*)/$', 
        esocial_compatibilidades_fpas_classificacoes_tributarias_salvar_views.salvar, 
        name='esocial_compatibilidades_fpas_classificacoes_tributarias_salvar'),

    url(r'^esocial-fatores-risco/apagar/(?P<hash>.*)/$', 
        esocial_fatores_risco_apagar_views.apagar, 
        name='esocial_fatores_risco_apagar'),

    url(r'^esocial-fatores-risco/api/$',
        esocial_fatores_risco_api_views.eSocialFatoresRiscoList.as_view() ),

    url(r'^esocial-fatores-risco/api/(?P<pk>[0-9]+)/$',
        esocial_fatores_risco_api_views.eSocialFatoresRiscoDetail.as_view() ),

    url(r'^esocial-fatores-risco/listar/(?P<hash>.*)/$', 
        esocial_fatores_risco_listar_views.listar, 
        name='esocial_fatores_risco'),
        
    url(r'^esocial-fatores-risco/json-search/(?P<search>[\w ]+)/$', 
        esocial_fatores_risco_api_views.json_search, 
        name='esocial_fatores_risco_json_search'),

    url(r'^esocial-fatores-risco/salvar/(?P<hash>.*)/$', 
        esocial_fatores_risco_salvar_views.salvar, 
        name='esocial_fatores_risco_salvar'),

    url(r'^esocial-codificacoes-acidente-trabalho/apagar/(?P<hash>.*)/$', 
        esocial_codificacoes_acidente_trabalho_apagar_views.apagar, 
        name='esocial_codificacoes_acidente_trabalho_apagar'),

    url(r'^esocial-codificacoes-acidente-trabalho/api/$',
        esocial_codificacoes_acidente_trabalho_api_views.eSocialCodificacoesAcidenteTrabalhoList.as_view() ),

    url(r'^esocial-codificacoes-acidente-trabalho/api/(?P<pk>[0-9]+)/$',
        esocial_codificacoes_acidente_trabalho_api_views.eSocialCodificacoesAcidenteTrabalhoDetail.as_view() ),

    url(r'^esocial-codificacoes-acidente-trabalho/listar/(?P<hash>.*)/$', 
        esocial_codificacoes_acidente_trabalho_listar_views.listar, 
        name='esocial_codificacoes_acidente_trabalho'),
        
    url(r'^esocial-codificacoes-acidente-trabalho/json-search/(?P<search>[\w ]+)/$', 
        esocial_codificacoes_acidente_trabalho_api_views.json_search, 
        name='esocial_codificacoes_acidente_trabalho_json_search'),

    url(r'^esocial-codificacoes-acidente-trabalho/salvar/(?P<hash>.*)/$', 
        esocial_codificacoes_acidente_trabalho_salvar_views.salvar, 
        name='esocial_codificacoes_acidente_trabalho_salvar'),

    url(r'^esocial-beneficios-previdenciarios-tipos/apagar/(?P<hash>.*)/$', 
        esocial_beneficios_previdenciarios_tipos_apagar_views.apagar, 
        name='esocial_beneficios_previdenciarios_tipos_apagar'),

    url(r'^esocial-beneficios-previdenciarios-tipos/api/$',
        esocial_beneficios_previdenciarios_tipos_api_views.eSocialBeneficiosPrevidenciariosTiposList.as_view() ),

    url(r'^esocial-beneficios-previdenciarios-tipos/api/(?P<pk>[0-9]+)/$',
        esocial_beneficios_previdenciarios_tipos_api_views.eSocialBeneficiosPrevidenciariosTiposDetail.as_view() ),

    url(r'^esocial-beneficios-previdenciarios-tipos/listar/(?P<hash>.*)/$', 
        esocial_beneficios_previdenciarios_tipos_listar_views.listar, 
        name='esocial_beneficios_previdenciarios_tipos'),
        
    url(r'^esocial-beneficios-previdenciarios-tipos/json-search/(?P<search>[\w ]+)/$', 
        esocial_beneficios_previdenciarios_tipos_api_views.json_search, 
        name='esocial_beneficios_previdenciarios_tipos_json_search'),

    url(r'^esocial-beneficios-previdenciarios-tipos/salvar/(?P<hash>.*)/$', 
        esocial_beneficios_previdenciarios_tipos_salvar_views.salvar, 
        name='esocial_beneficios_previdenciarios_tipos_salvar'),

    url(r'^esocial-beneficios-previdenciarios-cessacao-motivos/apagar/(?P<hash>.*)/$', 
        esocial_beneficios_previdenciarios_cessacao_motivos_apagar_views.apagar, 
        name='esocial_beneficios_previdenciarios_cessacao_motivos_apagar'),

    url(r'^esocial-beneficios-previdenciarios-cessacao-motivos/api/$',
        esocial_beneficios_previdenciarios_cessacao_motivos_api_views.eSocialBeneficiosPrevidenciariosCessacaoMotivosList.as_view() ),

    url(r'^esocial-beneficios-previdenciarios-cessacao-motivos/api/(?P<pk>[0-9]+)/$',
        esocial_beneficios_previdenciarios_cessacao_motivos_api_views.eSocialBeneficiosPrevidenciariosCessacaoMotivosDetail.as_view() ),

    url(r'^esocial-beneficios-previdenciarios-cessacao-motivos/listar/(?P<hash>.*)/$', 
        esocial_beneficios_previdenciarios_cessacao_motivos_listar_views.listar, 
        name='esocial_beneficios_previdenciarios_cessacao_motivos'),
        
    url(r'^esocial-beneficios-previdenciarios-cessacao-motivos/json-search/(?P<search>[\w ]+)/$', 
        esocial_beneficios_previdenciarios_cessacao_motivos_api_views.json_search, 
        name='esocial_beneficios_previdenciarios_cessacao_motivos_json_search'),

    url(r'^esocial-beneficios-previdenciarios-cessacao-motivos/salvar/(?P<hash>.*)/$', 
        esocial_beneficios_previdenciarios_cessacao_motivos_salvar_views.salvar, 
        name='esocial_beneficios_previdenciarios_cessacao_motivos_salvar'),

    url(r'^esocial-procedimentos-diagnosticos/apagar/(?P<hash>.*)/$', 
        esocial_procedimentos_diagnosticos_apagar_views.apagar, 
        name='esocial_procedimentos_diagnosticos_apagar'),

    url(r'^esocial-procedimentos-diagnosticos/api/$',
        esocial_procedimentos_diagnosticos_api_views.eSocialProcedimentosDiagnosticosList.as_view() ),

    url(r'^esocial-procedimentos-diagnosticos/api/(?P<pk>[0-9]+)/$',
        esocial_procedimentos_diagnosticos_api_views.eSocialProcedimentosDiagnosticosDetail.as_view() ),

    url(r'^esocial-procedimentos-diagnosticos/listar/(?P<hash>.*)/$', 
        esocial_procedimentos_diagnosticos_listar_views.listar, 
        name='esocial_procedimentos_diagnosticos'),
        
    url(r'^esocial-procedimentos-diagnosticos/json-search/(?P<search>[\w ]+)/$', 
        esocial_procedimentos_diagnosticos_api_views.json_search, 
        name='esocial_procedimentos_diagnosticos_json_search'),

    url(r'^esocial-procedimentos-diagnosticos/salvar/(?P<hash>.*)/$', 
        esocial_procedimentos_diagnosticos_salvar_views.salvar, 
        name='esocial_procedimentos_diagnosticos_salvar'),

    url(r'^esocial-atividades-periculosas-insalubres-especiais/apagar/(?P<hash>.*)/$', 
        esocial_atividades_periculosas_insalubres_especiais_apagar_views.apagar, 
        name='esocial_atividades_periculosas_insalubres_especiais_apagar'),

    url(r'^esocial-atividades-periculosas-insalubres-especiais/api/$',
        esocial_atividades_periculosas_insalubres_especiais_api_views.eSocialAtividadesPericulosasInsalubresEspeciaisList.as_view() ),

    url(r'^esocial-atividades-periculosas-insalubres-especiais/api/(?P<pk>[0-9]+)/$',
        esocial_atividades_periculosas_insalubres_especiais_api_views.eSocialAtividadesPericulosasInsalubresEspeciaisDetail.as_view() ),

    url(r'^esocial-atividades-periculosas-insalubres-especiais/listar/(?P<hash>.*)/$', 
        esocial_atividades_periculosas_insalubres_especiais_listar_views.listar, 
        name='esocial_atividades_periculosas_insalubres_especiais'),
        
    url(r'^esocial-atividades-periculosas-insalubres-especiais/json-search/(?P<search>[\w ]+)/$', 
        esocial_atividades_periculosas_insalubres_especiais_api_views.json_search, 
        name='esocial_atividades_periculosas_insalubres_especiais_json_search'),

    url(r'^esocial-atividades-periculosas-insalubres-especiais/salvar/(?P<hash>.*)/$', 
        esocial_atividades_periculosas_insalubres_especiais_salvar_views.salvar, 
        name='esocial_atividades_periculosas_insalubres_especiais_salvar'),

    url(r'^esocial-treinamentos-capacitacoes-exercicios-simulados/apagar/(?P<hash>.*)/$', 
        esocial_treinamentos_capacitacoes_exercicios_simulados_apagar_views.apagar, 
        name='esocial_treinamentos_capacitacoes_exercicios_simulados_apagar'),

    url(r'^esocial-treinamentos-capacitacoes-exercicios-simulados/api/$',
        esocial_treinamentos_capacitacoes_exercicios_simulados_api_views.eSocialTreinamentosCapacitacoesExerciciosSimuladosList.as_view() ),

    url(r'^esocial-treinamentos-capacitacoes-exercicios-simulados/api/(?P<pk>[0-9]+)/$',
        esocial_treinamentos_capacitacoes_exercicios_simulados_api_views.eSocialTreinamentosCapacitacoesExerciciosSimuladosDetail.as_view() ),

    url(r'^esocial-treinamentos-capacitacoes-exercicios-simulados/listar/(?P<hash>.*)/$', 
        esocial_treinamentos_capacitacoes_exercicios_simulados_listar_views.listar, 
        name='esocial_treinamentos_capacitacoes_exercicios_simulados'),
        
    url(r'^esocial-treinamentos-capacitacoes-exercicios-simulados/json-search/(?P<search>[\w ]+)/$', 
        esocial_treinamentos_capacitacoes_exercicios_simulados_api_views.json_search, 
        name='esocial_treinamentos_capacitacoes_exercicios_simulados_json_search'),

    url(r'^esocial-treinamentos-capacitacoes-exercicios-simulados/salvar/(?P<hash>.*)/$', 
        esocial_treinamentos_capacitacoes_exercicios_simulados_salvar_views.salvar, 
        name='esocial_treinamentos_capacitacoes_exercicios_simulados_salvar'),

    url(r'^esocial-programas-planos-documentos/apagar/(?P<hash>.*)/$', 
        esocial_programas_planos_documentos_apagar_views.apagar, 
        name='esocial_programas_planos_documentos_apagar'),

    url(r'^esocial-programas-planos-documentos/api/$',
        esocial_programas_planos_documentos_api_views.eSocialProgramasPlanosDocumentosList.as_view() ),

    url(r'^esocial-programas-planos-documentos/api/(?P<pk>[0-9]+)/$',
        esocial_programas_planos_documentos_api_views.eSocialProgramasPlanosDocumentosDetail.as_view() ),

    url(r'^esocial-programas-planos-documentos/listar/(?P<hash>.*)/$', 
        esocial_programas_planos_documentos_listar_views.listar, 
        name='esocial_programas_planos_documentos'),
        
    url(r'^esocial-programas-planos-documentos/json-search/(?P<search>[\w ]+)/$', 
        esocial_programas_planos_documentos_api_views.json_search, 
        name='esocial_programas_planos_documentos_json_search'),

    url(r'^esocial-programas-planos-documentos/salvar/(?P<hash>.*)/$', 
        esocial_programas_planos_documentos_salvar_views.salvar, 
        name='esocial_programas_planos_documentos_salvar'),

    url(r'^efdreinf-pagamentos-codigos/apagar/(?P<hash>.*)/$', 
        efdreinf_pagamentos_codigos_apagar_views.apagar, 
        name='efdreinf_pagamentos_codigos_apagar'),

    url(r'^efdreinf-pagamentos-codigos/api/$',
        efdreinf_pagamentos_codigos_api_views.EFDReinfPagamentosCodigosList.as_view() ),

    url(r'^efdreinf-pagamentos-codigos/api/(?P<pk>[0-9]+)/$',
        efdreinf_pagamentos_codigos_api_views.EFDReinfPagamentosCodigosDetail.as_view() ),

    url(r'^efdreinf-pagamentos-codigos/listar/(?P<hash>.*)/$', 
        efdreinf_pagamentos_codigos_listar_views.listar, 
        name='efdreinf_pagamentos_codigos'),
        
    url(r'^efdreinf-pagamentos-codigos/json-search/(?P<search>[\w ]+)/$', 
        efdreinf_pagamentos_codigos_api_views.json_search, 
        name='efdreinf_pagamentos_codigos_json_search'),

    url(r'^efdreinf-pagamentos-codigos/salvar/(?P<hash>.*)/$', 
        efdreinf_pagamentos_codigos_salvar_views.salvar, 
        name='efdreinf_pagamentos_codigos_salvar'),

    url(r'^efdreinf-regras-pagamentos-codigos/apagar/(?P<hash>.*)/$', 
        efdreinf_regras_pagamentos_codigos_apagar_views.apagar, 
        name='efdreinf_regras_pagamentos_codigos_apagar'),

    url(r'^efdreinf-regras-pagamentos-codigos/api/$',
        efdreinf_regras_pagamentos_codigos_api_views.EFDReinfRegrasPagamentosCodigosList.as_view() ),

    url(r'^efdreinf-regras-pagamentos-codigos/api/(?P<pk>[0-9]+)/$',
        efdreinf_regras_pagamentos_codigos_api_views.EFDReinfRegrasPagamentosCodigosDetail.as_view() ),

    url(r'^efdreinf-regras-pagamentos-codigos/listar/(?P<hash>.*)/$', 
        efdreinf_regras_pagamentos_codigos_listar_views.listar, 
        name='efdreinf_regras_pagamentos_codigos'),
        
    url(r'^efdreinf-regras-pagamentos-codigos/json-search/(?P<search>[\w ]+)/$', 
        efdreinf_regras_pagamentos_codigos_api_views.json_search, 
        name='efdreinf_regras_pagamentos_codigos_json_search'),

    url(r'^efdreinf-regras-pagamentos-codigos/salvar/(?P<hash>.*)/$', 
        efdreinf_regras_pagamentos_codigos_salvar_views.salvar, 
        name='efdreinf_regras_pagamentos_codigos_salvar'),

    url(r'^efdreinf-rendimentos-beneficiarios-exterior/apagar/(?P<hash>.*)/$', 
        efdreinf_rendimentos_beneficiarios_exterior_apagar_views.apagar, 
        name='efdreinf_rendimentos_beneficiarios_exterior_apagar'),

    url(r'^efdreinf-rendimentos-beneficiarios-exterior/api/$',
        efdreinf_rendimentos_beneficiarios_exterior_api_views.EFDReinfRendimentosBeneficiariosExteriorList.as_view() ),

    url(r'^efdreinf-rendimentos-beneficiarios-exterior/api/(?P<pk>[0-9]+)/$',
        efdreinf_rendimentos_beneficiarios_exterior_api_views.EFDReinfRendimentosBeneficiariosExteriorDetail.as_view() ),

    url(r'^efdreinf-rendimentos-beneficiarios-exterior/listar/(?P<hash>.*)/$', 
        efdreinf_rendimentos_beneficiarios_exterior_listar_views.listar, 
        name='efdreinf_rendimentos_beneficiarios_exterior'),
        
    url(r'^efdreinf-rendimentos-beneficiarios-exterior/json-search/(?P<search>[\w ]+)/$', 
        efdreinf_rendimentos_beneficiarios_exterior_api_views.json_search, 
        name='efdreinf_rendimentos_beneficiarios_exterior_json_search'),

    url(r'^efdreinf-rendimentos-beneficiarios-exterior/salvar/(?P<hash>.*)/$', 
        efdreinf_rendimentos_beneficiarios_exterior_salvar_views.salvar, 
        name='efdreinf_rendimentos_beneficiarios_exterior_salvar'),

    url(r'^efdreinf-rendimentos-beneficiarios-exterior-tributacao/apagar/(?P<hash>.*)/$', 
        efdreinf_rendimentos_beneficiarios_exterior_tributacao_apagar_views.apagar, 
        name='efdreinf_rendimentos_beneficiarios_exterior_tributacao_apagar'),

    url(r'^efdreinf-rendimentos-beneficiarios-exterior-tributacao/api/$',
        efdreinf_rendimentos_beneficiarios_exterior_tributacao_api_views.EFDReinfRendimentosBeneficiariosExteriorTributacaoList.as_view() ),

    url(r'^efdreinf-rendimentos-beneficiarios-exterior-tributacao/api/(?P<pk>[0-9]+)/$',
        efdreinf_rendimentos_beneficiarios_exterior_tributacao_api_views.EFDReinfRendimentosBeneficiariosExteriorTributacaoDetail.as_view() ),

    url(r'^efdreinf-rendimentos-beneficiarios-exterior-tributacao/listar/(?P<hash>.*)/$', 
        efdreinf_rendimentos_beneficiarios_exterior_tributacao_listar_views.listar, 
        name='efdreinf_rendimentos_beneficiarios_exterior_tributacao'),
        
    url(r'^efdreinf-rendimentos-beneficiarios-exterior-tributacao/json-search/(?P<search>[\w ]+)/$', 
        efdreinf_rendimentos_beneficiarios_exterior_tributacao_api_views.json_search, 
        name='efdreinf_rendimentos_beneficiarios_exterior_tributacao_json_search'),

    url(r'^efdreinf-rendimentos-beneficiarios-exterior-tributacao/salvar/(?P<hash>.*)/$', 
        efdreinf_rendimentos_beneficiarios_exterior_tributacao_salvar_views.salvar, 
        name='efdreinf_rendimentos_beneficiarios_exterior_tributacao_salvar'),

    url(r'^efdreinf-informacoes-beneficiarios-exterior/apagar/(?P<hash>.*)/$', 
        efdreinf_informacoes_beneficiarios_exterior_apagar_views.apagar, 
        name='efdreinf_informacoes_beneficiarios_exterior_apagar'),

    url(r'^efdreinf-informacoes-beneficiarios-exterior/api/$',
        efdreinf_informacoes_beneficiarios_exterior_api_views.EFDReinfInformacoesBeneficiariosExteriorList.as_view() ),

    url(r'^efdreinf-informacoes-beneficiarios-exterior/api/(?P<pk>[0-9]+)/$',
        efdreinf_informacoes_beneficiarios_exterior_api_views.EFDReinfInformacoesBeneficiariosExteriorDetail.as_view() ),

    url(r'^efdreinf-informacoes-beneficiarios-exterior/listar/(?P<hash>.*)/$', 
        efdreinf_informacoes_beneficiarios_exterior_listar_views.listar, 
        name='efdreinf_informacoes_beneficiarios_exterior'),
        
    url(r'^efdreinf-informacoes-beneficiarios-exterior/json-search/(?P<search>[\w ]+)/$', 
        efdreinf_informacoes_beneficiarios_exterior_api_views.json_search, 
        name='efdreinf_informacoes_beneficiarios_exterior_json_search'),

    url(r'^efdreinf-informacoes-beneficiarios-exterior/salvar/(?P<hash>.*)/$', 
        efdreinf_informacoes_beneficiarios_exterior_salvar_views.salvar, 
        name='efdreinf_informacoes_beneficiarios_exterior_salvar'),

    url(r'^efdreinf-classificacao-servicos-prestados/apagar/(?P<hash>.*)/$', 
        efdreinf_classificacao_servicos_prestados_apagar_views.apagar, 
        name='efdreinf_classificacao_servicos_prestados_apagar'),

    url(r'^efdreinf-classificacao-servicos-prestados/api/$',
        efdreinf_classificacao_servicos_prestados_api_views.EFDReinfClassificacaoServicosPrestadosList.as_view() ),

    url(r'^efdreinf-classificacao-servicos-prestados/api/(?P<pk>[0-9]+)/$',
        efdreinf_classificacao_servicos_prestados_api_views.EFDReinfClassificacaoServicosPrestadosDetail.as_view() ),

    url(r'^efdreinf-classificacao-servicos-prestados/listar/(?P<hash>.*)/$', 
        efdreinf_classificacao_servicos_prestados_listar_views.listar, 
        name='efdreinf_classificacao_servicos_prestados'),
        
    url(r'^efdreinf-classificacao-servicos-prestados/json-search/(?P<search>[\w ]+)/$', 
        efdreinf_classificacao_servicos_prestados_api_views.json_search, 
        name='efdreinf_classificacao_servicos_prestados_json_search'),

    url(r'^efdreinf-classificacao-servicos-prestados/salvar/(?P<hash>.*)/$', 
        efdreinf_classificacao_servicos_prestados_salvar_views.salvar, 
        name='efdreinf_classificacao_servicos_prestados_salvar'),

    url(r'^efdreinf-paises/apagar/(?P<hash>.*)/$', 
        efdreinf_paises_apagar_views.apagar, 
        name='efdreinf_paises_apagar'),

    url(r'^efdreinf-paises/api/$',
        efdreinf_paises_api_views.EFDReinfPaisesList.as_view() ),

    url(r'^efdreinf-paises/api/(?P<pk>[0-9]+)/$',
        efdreinf_paises_api_views.EFDReinfPaisesDetail.as_view() ),

    url(r'^efdreinf-paises/listar/(?P<hash>.*)/$', 
        efdreinf_paises_listar_views.listar, 
        name='efdreinf_paises'),
        
    url(r'^efdreinf-paises/json-search/(?P<search>[\w ]+)/$', 
        efdreinf_paises_api_views.json_search, 
        name='efdreinf_paises_json_search'),

    url(r'^efdreinf-paises/salvar/(?P<hash>.*)/$', 
        efdreinf_paises_salvar_views.salvar, 
        name='efdreinf_paises_salvar'),

    url(r'^efdreinf-classificacao-tributaria/apagar/(?P<hash>.*)/$', 
        efdreinf_classificacao_tributaria_apagar_views.apagar, 
        name='efdreinf_classificacao_tributaria_apagar'),

    url(r'^efdreinf-classificacao-tributaria/api/$',
        efdreinf_classificacao_tributaria_api_views.EFDReinfClassificacaoTributariaList.as_view() ),

    url(r'^efdreinf-classificacao-tributaria/api/(?P<pk>[0-9]+)/$',
        efdreinf_classificacao_tributaria_api_views.EFDReinfClassificacaoTributariaDetail.as_view() ),

    url(r'^efdreinf-classificacao-tributaria/listar/(?P<hash>.*)/$', 
        efdreinf_classificacao_tributaria_listar_views.listar, 
        name='efdreinf_classificacao_tributaria'),
        
    url(r'^efdreinf-classificacao-tributaria/json-search/(?P<search>[\w ]+)/$', 
        efdreinf_classificacao_tributaria_api_views.json_search, 
        name='efdreinf_classificacao_tributaria_json_search'),

    url(r'^efdreinf-classificacao-tributaria/salvar/(?P<hash>.*)/$', 
        efdreinf_classificacao_tributaria_salvar_views.salvar, 
        name='efdreinf_classificacao_tributaria_salvar'),

    url(r'^efdreinf-codigos-atividades-produtos-servicos-cprb/apagar/(?P<hash>.*)/$', 
        efdreinf_codigos_atividades_produtos_servicos_cprb_apagar_views.apagar, 
        name='efdreinf_codigos_atividades_produtos_servicos_cprb_apagar'),

    url(r'^efdreinf-codigos-atividades-produtos-servicos-cprb/api/$',
        efdreinf_codigos_atividades_produtos_servicos_cprb_api_views.EFDReinfCodigosAtividadesProdutosServicosCPRBList.as_view() ),

    url(r'^efdreinf-codigos-atividades-produtos-servicos-cprb/api/(?P<pk>[0-9]+)/$',
        efdreinf_codigos_atividades_produtos_servicos_cprb_api_views.EFDReinfCodigosAtividadesProdutosServicosCPRBDetail.as_view() ),

    url(r'^efdreinf-codigos-atividades-produtos-servicos-cprb/listar/(?P<hash>.*)/$', 
        efdreinf_codigos_atividades_produtos_servicos_cprb_listar_views.listar, 
        name='efdreinf_codigos_atividades_produtos_servicos_cprb'),
        
    url(r'^efdreinf-codigos-atividades-produtos-servicos-cprb/json-search/(?P<search>[\w ]+)/$', 
        efdreinf_codigos_atividades_produtos_servicos_cprb_api_views.json_search, 
        name='efdreinf_codigos_atividades_produtos_servicos_cprb_json_search'),

    url(r'^efdreinf-codigos-atividades-produtos-servicos-cprb/salvar/(?P<hash>.*)/$', 
        efdreinf_codigos_atividades_produtos_servicos_cprb_salvar_views.salvar, 
        name='efdreinf_codigos_atividades_produtos_servicos_cprb_salvar'),

    url(r'^efdreinf-eventos/apagar/(?P<hash>.*)/$', 
        efdreinf_eventos_apagar_views.apagar, 
        name='efdreinf_eventos_apagar'),

    url(r'^efdreinf-eventos/api/$',
        efdreinf_eventos_api_views.EFDReinfEventosList.as_view() ),

    url(r'^efdreinf-eventos/api/(?P<pk>[0-9]+)/$',
        efdreinf_eventos_api_views.EFDReinfEventosDetail.as_view() ),

    url(r'^efdreinf-eventos/listar/(?P<hash>.*)/$', 
        efdreinf_eventos_listar_views.listar, 
        name='efdreinf_eventos'),
        
    url(r'^efdreinf-eventos/json-search/(?P<search>[\w ]+)/$', 
        efdreinf_eventos_api_views.json_search, 
        name='efdreinf_eventos_json_search'),

    url(r'^efdreinf-eventos/salvar/(?P<hash>.*)/$', 
        efdreinf_eventos_salvar_views.salvar, 
        name='efdreinf_eventos_salvar'),


]