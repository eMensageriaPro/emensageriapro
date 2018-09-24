#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.tabelas.views import municipios as municipios_views
from emensageriapro.tabelas.views import cbo as cbo_views
from emensageriapro.tabelas.views import cid as cid_views
from emensageriapro.tabelas.views import cnae as cnae_views
from emensageriapro.tabelas.views import esocial_trabalhadores_categorias as esocial_trabalhadores_categorias_views
from emensageriapro.tabelas.views import esocial_financiamentos_aposentadorias_especiais as esocial_financiamentos_aposentadorias_especiais_views
from emensageriapro.tabelas.views import esocial_naturezas_rubricas as esocial_naturezas_rubricas_views
from emensageriapro.tabelas.views import esocial_codigo_aliquotas_fpas_terceiros as esocial_codigo_aliquotas_fpas_terceiros_views
from emensageriapro.tabelas.views import esocial_inscricoes_tipos as esocial_inscricoes_tipos_views
from emensageriapro.tabelas.views import esocial_paises as esocial_paises_views
from emensageriapro.tabelas.views import esocial_dependentes_tipos as esocial_dependentes_tipos_views
from emensageriapro.tabelas.views import esocial_classificacoes_tributarias as esocial_classificacoes_tributarias_views
from emensageriapro.tabelas.views import esocial_arquivos_esocial_tipos as esocial_arquivos_esocial_tipos_views
from emensageriapro.tabelas.views import esocial_lotacoes_tributarias_tipos as esocial_lotacoes_tributarias_tipos_views
from emensageriapro.tabelas.views import esocial_compatibilidades_categorias_classificacoes_lotacoes as esocial_compatibilidades_categorias_classificacoes_lotacoes_views
from emensageriapro.tabelas.views import esocial_compatibilidades_lotacoes_classificacoes as esocial_compatibilidades_lotacoes_classificacoes_views
from emensageriapro.tabelas.views import esocial_partes_corpo_atingidas as esocial_partes_corpo_atingidas_views
from emensageriapro.tabelas.views import esocial_agentes_causadores_acidentes_trabalho as esocial_agentes_causadores_acidentes_trabalho_views
from emensageriapro.tabelas.views import esocial_agentes_causadores_doencas_profissionais as esocial_agentes_causadores_doencas_profissionais_views
from emensageriapro.tabelas.views import esocial_acidentes_situacoes_geradoras as esocial_acidentes_situacoes_geradoras_views
from emensageriapro.tabelas.views import esocial_naturezas_lesoes as esocial_naturezas_lesoes_views
from emensageriapro.tabelas.views import esocial_afastamentos_motivos as esocial_afastamentos_motivos_views
from emensageriapro.tabelas.views import esocial_desligamentos_motivos as esocial_desligamentos_motivos_views
from emensageriapro.tabelas.views import esocial_logradouros_tipos as esocial_logradouros_tipos_views
from emensageriapro.tabelas.views import esocial_naturezas_juridicas as esocial_naturezas_juridicas_views
from emensageriapro.tabelas.views import esocial_compatibilidades_fpas_classificacoes_tributarias as esocial_compatibilidades_fpas_classificacoes_tributarias_views
from emensageriapro.tabelas.views import esocial_fatores_risco as esocial_fatores_risco_views
from emensageriapro.tabelas.views import esocial_codificacoes_acidente_trabalho as esocial_codificacoes_acidente_trabalho_views
from emensageriapro.tabelas.views import esocial_beneficios_previdenciarios_tipos as esocial_beneficios_previdenciarios_tipos_views
from emensageriapro.tabelas.views import esocial_beneficios_previdenciarios_cessacao_motivos as esocial_beneficios_previdenciarios_cessacao_motivos_views
from emensageriapro.tabelas.views import esocial_procedimentos_diagnosticos as esocial_procedimentos_diagnosticos_views
from emensageriapro.tabelas.views import esocial_atividades_periculosas_insalubres_especiais as esocial_atividades_periculosas_insalubres_especiais_views
from emensageriapro.tabelas.views import esocial_treinamentos_capacitacoes_exercicios_simulados as esocial_treinamentos_capacitacoes_exercicios_simulados_views
from emensageriapro.tabelas.views import esocial_programas_planos_documentos as esocial_programas_planos_documentos_views
from emensageriapro.tabelas.views import efdreinf_pagamentos_codigos as efdreinf_pagamentos_codigos_views
from emensageriapro.tabelas.views import efdreinf_regras_pagamentos_codigos as efdreinf_regras_pagamentos_codigos_views
from emensageriapro.tabelas.views import efdreinf_rendimentos_beneficiarios_exterior as efdreinf_rendimentos_beneficiarios_exterior_views
from emensageriapro.tabelas.views import efdreinf_rendimentos_beneficiarios_exterior_tributacao as efdreinf_rendimentos_beneficiarios_exterior_tributacao_views
from emensageriapro.tabelas.views import efdreinf_informacoes_beneficiarios_exterior as efdreinf_informacoes_beneficiarios_exterior_views
from emensageriapro.tabelas.views import efdreinf_classificacao_servicos_prestados as efdreinf_classificacao_servicos_prestados_views
from emensageriapro.tabelas.views import efdreinf_paises as efdreinf_paises_views
from emensageriapro.tabelas.views import efdreinf_classificacao_tributaria as efdreinf_classificacao_tributaria_views
from emensageriapro.tabelas.views import efdreinf_codigos_atividades_produtos_servicos_cprb as efdreinf_codigos_atividades_produtos_servicos_cprb_views
from emensageriapro.tabelas.views import efdreinf_eventos as efdreinf_eventos_views



"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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
        municipios_views.apagar, 
        name='municipios_apagar'),

url(r'^municipios/api/$',
            municipios_views.MunicipiosList.as_view() ),

        url(r'^municipios/api/(?P<pk>[0-9]+)/$',
            municipios_views.MunicipiosDetail.as_view() ),

url(r'^municipios/listar/(?P<hash>.*)/$', 
        municipios_views.listar, 
        name='municipios'),
        
        
    url(r'^municipios/json-search/(?P<search>[\w ]+)/$', 
    municipios_views.json_search, 
        name='municipios_json_search'),

url(r'^municipios/salvar/(?P<hash>.*)/$', 
        municipios_views.salvar, 
        name='municipios_salvar'),



url(r'^cbo/apagar/(?P<hash>.*)/$', 
        cbo_views.apagar, 
        name='cbo_apagar'),

url(r'^cbo/api/$',
            cbo_views.CBOList.as_view() ),

        url(r'^cbo/api/(?P<pk>[0-9]+)/$',
            cbo_views.CBODetail.as_view() ),

url(r'^cbo/listar/(?P<hash>.*)/$', 
        cbo_views.listar, 
        name='cbo'),
        
        
    url(r'^cbo/json-search/(?P<search>[\w ]+)/$', 
    cbo_views.json_search, 
        name='cbo_json_search'),

url(r'^cbo/salvar/(?P<hash>.*)/$', 
        cbo_views.salvar, 
        name='cbo_salvar'),



url(r'^cid/apagar/(?P<hash>.*)/$', 
        cid_views.apagar, 
        name='cid_apagar'),

url(r'^cid/api/$',
            cid_views.CIDList.as_view() ),

        url(r'^cid/api/(?P<pk>[0-9]+)/$',
            cid_views.CIDDetail.as_view() ),

url(r'^cid/listar/(?P<hash>.*)/$', 
        cid_views.listar, 
        name='cid'),
        
        
    url(r'^cid/json-search/(?P<search>[\w ]+)/$', 
    cid_views.json_search, 
        name='cid_json_search'),

url(r'^cid/salvar/(?P<hash>.*)/$', 
        cid_views.salvar, 
        name='cid_salvar'),



url(r'^cnae/apagar/(?P<hash>.*)/$', 
        cnae_views.apagar, 
        name='cnae_apagar'),

url(r'^cnae/api/$',
            cnae_views.CNAEList.as_view() ),

        url(r'^cnae/api/(?P<pk>[0-9]+)/$',
            cnae_views.CNAEDetail.as_view() ),

url(r'^cnae/listar/(?P<hash>.*)/$', 
        cnae_views.listar, 
        name='cnae'),
        
        
    url(r'^cnae/json-search/(?P<search>[\w ]+)/$', 
    cnae_views.json_search, 
        name='cnae_json_search'),

url(r'^cnae/salvar/(?P<hash>.*)/$', 
        cnae_views.salvar, 
        name='cnae_salvar'),



url(r'^esocial-trabalhadores-categorias/apagar/(?P<hash>.*)/$', 
        esocial_trabalhadores_categorias_views.apagar, 
        name='esocial_trabalhadores_categorias_apagar'),

url(r'^esocial-trabalhadores-categorias/api/$',
            esocial_trabalhadores_categorias_views.eSocialTrabalhadoresCategoriasList.as_view() ),

        url(r'^esocial-trabalhadores-categorias/api/(?P<pk>[0-9]+)/$',
            esocial_trabalhadores_categorias_views.eSocialTrabalhadoresCategoriasDetail.as_view() ),

url(r'^esocial-trabalhadores-categorias/listar/(?P<hash>.*)/$', 
        esocial_trabalhadores_categorias_views.listar, 
        name='esocial_trabalhadores_categorias'),
        
        
    url(r'^esocial-trabalhadores-categorias/json-search/(?P<search>[\w ]+)/$', 
    esocial_trabalhadores_categorias_views.json_search, 
        name='esocial_trabalhadores_categorias_json_search'),

url(r'^esocial-trabalhadores-categorias/salvar/(?P<hash>.*)/$', 
        esocial_trabalhadores_categorias_views.salvar, 
        name='esocial_trabalhadores_categorias_salvar'),



url(r'^esocial-financiamentos-aposentadorias-especiais/apagar/(?P<hash>.*)/$', 
        esocial_financiamentos_aposentadorias_especiais_views.apagar, 
        name='esocial_financiamentos_aposentadorias_especiais_apagar'),

url(r'^esocial-financiamentos-aposentadorias-especiais/api/$',
            esocial_financiamentos_aposentadorias_especiais_views.eSocialFinanciamentosAposentadoriasEspeciaisList.as_view() ),

        url(r'^esocial-financiamentos-aposentadorias-especiais/api/(?P<pk>[0-9]+)/$',
            esocial_financiamentos_aposentadorias_especiais_views.eSocialFinanciamentosAposentadoriasEspeciaisDetail.as_view() ),

url(r'^esocial-financiamentos-aposentadorias-especiais/listar/(?P<hash>.*)/$', 
        esocial_financiamentos_aposentadorias_especiais_views.listar, 
        name='esocial_financiamentos_aposentadorias_especiais'),
        
        
    url(r'^esocial-financiamentos-aposentadorias-especiais/json-search/(?P<search>[\w ]+)/$', 
    esocial_financiamentos_aposentadorias_especiais_views.json_search, 
        name='esocial_financiamentos_aposentadorias_especiais_json_search'),

url(r'^esocial-financiamentos-aposentadorias-especiais/salvar/(?P<hash>.*)/$', 
        esocial_financiamentos_aposentadorias_especiais_views.salvar, 
        name='esocial_financiamentos_aposentadorias_especiais_salvar'),



url(r'^esocial-naturezas-rubricas/apagar/(?P<hash>.*)/$', 
        esocial_naturezas_rubricas_views.apagar, 
        name='esocial_naturezas_rubricas_apagar'),

url(r'^esocial-naturezas-rubricas/api/$',
            esocial_naturezas_rubricas_views.eSocialNaturezasRubricasList.as_view() ),

        url(r'^esocial-naturezas-rubricas/api/(?P<pk>[0-9]+)/$',
            esocial_naturezas_rubricas_views.eSocialNaturezasRubricasDetail.as_view() ),

url(r'^esocial-naturezas-rubricas/listar/(?P<hash>.*)/$', 
        esocial_naturezas_rubricas_views.listar, 
        name='esocial_naturezas_rubricas'),
        
        
    url(r'^esocial-naturezas-rubricas/json-search/(?P<search>[\w ]+)/$', 
    esocial_naturezas_rubricas_views.json_search, 
        name='esocial_naturezas_rubricas_json_search'),

url(r'^esocial-naturezas-rubricas/salvar/(?P<hash>.*)/$', 
        esocial_naturezas_rubricas_views.salvar, 
        name='esocial_naturezas_rubricas_salvar'),



url(r'^esocial-codigo-aliquotas-fpas-terceiros/apagar/(?P<hash>.*)/$', 
        esocial_codigo_aliquotas_fpas_terceiros_views.apagar, 
        name='esocial_codigo_aliquotas_fpas_terceiros_apagar'),

url(r'^esocial-codigo-aliquotas-fpas-terceiros/api/$',
            esocial_codigo_aliquotas_fpas_terceiros_views.eSocialCodigoAliquotasFPASTerceirosList.as_view() ),

        url(r'^esocial-codigo-aliquotas-fpas-terceiros/api/(?P<pk>[0-9]+)/$',
            esocial_codigo_aliquotas_fpas_terceiros_views.eSocialCodigoAliquotasFPASTerceirosDetail.as_view() ),

url(r'^esocial-codigo-aliquotas-fpas-terceiros/listar/(?P<hash>.*)/$', 
        esocial_codigo_aliquotas_fpas_terceiros_views.listar, 
        name='esocial_codigo_aliquotas_fpas_terceiros'),
        
        
    url(r'^esocial-codigo-aliquotas-fpas-terceiros/json-search/(?P<search>[\w ]+)/$', 
    esocial_codigo_aliquotas_fpas_terceiros_views.json_search, 
        name='esocial_codigo_aliquotas_fpas_terceiros_json_search'),

url(r'^esocial-codigo-aliquotas-fpas-terceiros/salvar/(?P<hash>.*)/$', 
        esocial_codigo_aliquotas_fpas_terceiros_views.salvar, 
        name='esocial_codigo_aliquotas_fpas_terceiros_salvar'),



url(r'^esocial-inscricoes-tipos/apagar/(?P<hash>.*)/$', 
        esocial_inscricoes_tipos_views.apagar, 
        name='esocial_inscricoes_tipos_apagar'),

url(r'^esocial-inscricoes-tipos/api/$',
            esocial_inscricoes_tipos_views.eSocialInscricoesTiposList.as_view() ),

        url(r'^esocial-inscricoes-tipos/api/(?P<pk>[0-9]+)/$',
            esocial_inscricoes_tipos_views.eSocialInscricoesTiposDetail.as_view() ),

url(r'^esocial-inscricoes-tipos/listar/(?P<hash>.*)/$', 
        esocial_inscricoes_tipos_views.listar, 
        name='esocial_inscricoes_tipos'),
        
        
    url(r'^esocial-inscricoes-tipos/json-search/(?P<search>[\w ]+)/$', 
    esocial_inscricoes_tipos_views.json_search, 
        name='esocial_inscricoes_tipos_json_search'),

url(r'^esocial-inscricoes-tipos/salvar/(?P<hash>.*)/$', 
        esocial_inscricoes_tipos_views.salvar, 
        name='esocial_inscricoes_tipos_salvar'),



url(r'^esocial-paises/apagar/(?P<hash>.*)/$', 
        esocial_paises_views.apagar, 
        name='esocial_paises_apagar'),

url(r'^esocial-paises/api/$',
            esocial_paises_views.eSocialPaisesList.as_view() ),

        url(r'^esocial-paises/api/(?P<pk>[0-9]+)/$',
            esocial_paises_views.eSocialPaisesDetail.as_view() ),

url(r'^esocial-paises/listar/(?P<hash>.*)/$', 
        esocial_paises_views.listar, 
        name='esocial_paises'),
        
        
    url(r'^esocial-paises/json-search/(?P<search>[\w ]+)/$', 
    esocial_paises_views.json_search, 
        name='esocial_paises_json_search'),

url(r'^esocial-paises/salvar/(?P<hash>.*)/$', 
        esocial_paises_views.salvar, 
        name='esocial_paises_salvar'),



url(r'^esocial-dependentes-tipos/apagar/(?P<hash>.*)/$', 
        esocial_dependentes_tipos_views.apagar, 
        name='esocial_dependentes_tipos_apagar'),

url(r'^esocial-dependentes-tipos/api/$',
            esocial_dependentes_tipos_views.eSocialDependentesTiposList.as_view() ),

        url(r'^esocial-dependentes-tipos/api/(?P<pk>[0-9]+)/$',
            esocial_dependentes_tipos_views.eSocialDependentesTiposDetail.as_view() ),

url(r'^esocial-dependentes-tipos/listar/(?P<hash>.*)/$', 
        esocial_dependentes_tipos_views.listar, 
        name='esocial_dependentes_tipos'),
        
        
    url(r'^esocial-dependentes-tipos/json-search/(?P<search>[\w ]+)/$', 
    esocial_dependentes_tipos_views.json_search, 
        name='esocial_dependentes_tipos_json_search'),

url(r'^esocial-dependentes-tipos/salvar/(?P<hash>.*)/$', 
        esocial_dependentes_tipos_views.salvar, 
        name='esocial_dependentes_tipos_salvar'),



url(r'^esocial-classificacoes-tributarias/apagar/(?P<hash>.*)/$', 
        esocial_classificacoes_tributarias_views.apagar, 
        name='esocial_classificacoes_tributarias_apagar'),

url(r'^esocial-classificacoes-tributarias/api/$',
            esocial_classificacoes_tributarias_views.eSocialClassificacoesTributariasList.as_view() ),

        url(r'^esocial-classificacoes-tributarias/api/(?P<pk>[0-9]+)/$',
            esocial_classificacoes_tributarias_views.eSocialClassificacoesTributariasDetail.as_view() ),

url(r'^esocial-classificacoes-tributarias/listar/(?P<hash>.*)/$', 
        esocial_classificacoes_tributarias_views.listar, 
        name='esocial_classificacoes_tributarias'),
        
        
    url(r'^esocial-classificacoes-tributarias/json-search/(?P<search>[\w ]+)/$', 
    esocial_classificacoes_tributarias_views.json_search, 
        name='esocial_classificacoes_tributarias_json_search'),

url(r'^esocial-classificacoes-tributarias/salvar/(?P<hash>.*)/$', 
        esocial_classificacoes_tributarias_views.salvar, 
        name='esocial_classificacoes_tributarias_salvar'),



url(r'^esocial-arquivos-esocial-tipos/apagar/(?P<hash>.*)/$', 
        esocial_arquivos_esocial_tipos_views.apagar, 
        name='esocial_arquivos_esocial_tipos_apagar'),

url(r'^esocial-arquivos-esocial-tipos/api/$',
            esocial_arquivos_esocial_tipos_views.eSocialArquivosEsocialTiposList.as_view() ),

        url(r'^esocial-arquivos-esocial-tipos/api/(?P<pk>[0-9]+)/$',
            esocial_arquivos_esocial_tipos_views.eSocialArquivosEsocialTiposDetail.as_view() ),

url(r'^esocial-arquivos-esocial-tipos/listar/(?P<hash>.*)/$', 
        esocial_arquivos_esocial_tipos_views.listar, 
        name='esocial_arquivos_esocial_tipos'),
        
        
    url(r'^esocial-arquivos-esocial-tipos/json-search/(?P<search>[\w ]+)/$', 
    esocial_arquivos_esocial_tipos_views.json_search, 
        name='esocial_arquivos_esocial_tipos_json_search'),

url(r'^esocial-arquivos-esocial-tipos/salvar/(?P<hash>.*)/$', 
        esocial_arquivos_esocial_tipos_views.salvar, 
        name='esocial_arquivos_esocial_tipos_salvar'),



url(r'^esocial-lotacoes-tributarias-tipos/apagar/(?P<hash>.*)/$', 
        esocial_lotacoes_tributarias_tipos_views.apagar, 
        name='esocial_lotacoes_tributarias_tipos_apagar'),

url(r'^esocial-lotacoes-tributarias-tipos/api/$',
            esocial_lotacoes_tributarias_tipos_views.eSocialLotacoesTributariasTiposList.as_view() ),

        url(r'^esocial-lotacoes-tributarias-tipos/api/(?P<pk>[0-9]+)/$',
            esocial_lotacoes_tributarias_tipos_views.eSocialLotacoesTributariasTiposDetail.as_view() ),

url(r'^esocial-lotacoes-tributarias-tipos/listar/(?P<hash>.*)/$', 
        esocial_lotacoes_tributarias_tipos_views.listar, 
        name='esocial_lotacoes_tributarias_tipos'),
        
        
    url(r'^esocial-lotacoes-tributarias-tipos/json-search/(?P<search>[\w ]+)/$', 
    esocial_lotacoes_tributarias_tipos_views.json_search, 
        name='esocial_lotacoes_tributarias_tipos_json_search'),

url(r'^esocial-lotacoes-tributarias-tipos/salvar/(?P<hash>.*)/$', 
        esocial_lotacoes_tributarias_tipos_views.salvar, 
        name='esocial_lotacoes_tributarias_tipos_salvar'),



url(r'^esocial-compatibilidades-categorias-classificacoes-lotacoes/apagar/(?P<hash>.*)/$', 
        esocial_compatibilidades_categorias_classificacoes_lotacoes_views.apagar, 
        name='esocial_compatibilidades_categorias_classificacoes_lotacoes_apagar'),

url(r'^esocial-compatibilidades-categorias-classificacoes-lotacoes/api/$',
            esocial_compatibilidades_categorias_classificacoes_lotacoes_views.eSocialCompatibilidadesCategoriasClassificacoesLotacoesList.as_view() ),

        url(r'^esocial-compatibilidades-categorias-classificacoes-lotacoes/api/(?P<pk>[0-9]+)/$',
            esocial_compatibilidades_categorias_classificacoes_lotacoes_views.eSocialCompatibilidadesCategoriasClassificacoesLotacoesDetail.as_view() ),

url(r'^esocial-compatibilidades-categorias-classificacoes-lotacoes/listar/(?P<hash>.*)/$', 
        esocial_compatibilidades_categorias_classificacoes_lotacoes_views.listar, 
        name='esocial_compatibilidades_categorias_classificacoes_lotacoes'),
        
        
    url(r'^esocial-compatibilidades-categorias-classificacoes-lotacoes/json-search/(?P<search>[\w ]+)/$', 
    esocial_compatibilidades_categorias_classificacoes_lotacoes_views.json_search, 
        name='esocial_compatibilidades_categorias_classificacoes_lotacoes_json_search'),

url(r'^esocial-compatibilidades-categorias-classificacoes-lotacoes/salvar/(?P<hash>.*)/$', 
        esocial_compatibilidades_categorias_classificacoes_lotacoes_views.salvar, 
        name='esocial_compatibilidades_categorias_classificacoes_lotacoes_salvar'),



url(r'^esocial-compatibilidades-lotacoes-classificacoes/apagar/(?P<hash>.*)/$', 
        esocial_compatibilidades_lotacoes_classificacoes_views.apagar, 
        name='esocial_compatibilidades_lotacoes_classificacoes_apagar'),

url(r'^esocial-compatibilidades-lotacoes-classificacoes/api/$',
            esocial_compatibilidades_lotacoes_classificacoes_views.eSocialCompatibilidadesLotacoesClassificacoesList.as_view() ),

        url(r'^esocial-compatibilidades-lotacoes-classificacoes/api/(?P<pk>[0-9]+)/$',
            esocial_compatibilidades_lotacoes_classificacoes_views.eSocialCompatibilidadesLotacoesClassificacoesDetail.as_view() ),

url(r'^esocial-compatibilidades-lotacoes-classificacoes/listar/(?P<hash>.*)/$', 
        esocial_compatibilidades_lotacoes_classificacoes_views.listar, 
        name='esocial_compatibilidades_lotacoes_classificacoes'),
        
        
    url(r'^esocial-compatibilidades-lotacoes-classificacoes/json-search/(?P<search>[\w ]+)/$', 
    esocial_compatibilidades_lotacoes_classificacoes_views.json_search, 
        name='esocial_compatibilidades_lotacoes_classificacoes_json_search'),

url(r'^esocial-compatibilidades-lotacoes-classificacoes/salvar/(?P<hash>.*)/$', 
        esocial_compatibilidades_lotacoes_classificacoes_views.salvar, 
        name='esocial_compatibilidades_lotacoes_classificacoes_salvar'),



url(r'^esocial-partes-corpo-atingidas/apagar/(?P<hash>.*)/$', 
        esocial_partes_corpo_atingidas_views.apagar, 
        name='esocial_partes_corpo_atingidas_apagar'),

url(r'^esocial-partes-corpo-atingidas/api/$',
            esocial_partes_corpo_atingidas_views.eSocialPartesCorpoAtingidasList.as_view() ),

        url(r'^esocial-partes-corpo-atingidas/api/(?P<pk>[0-9]+)/$',
            esocial_partes_corpo_atingidas_views.eSocialPartesCorpoAtingidasDetail.as_view() ),

url(r'^esocial-partes-corpo-atingidas/listar/(?P<hash>.*)/$', 
        esocial_partes_corpo_atingidas_views.listar, 
        name='esocial_partes_corpo_atingidas'),
        
        
    url(r'^esocial-partes-corpo-atingidas/json-search/(?P<search>[\w ]+)/$', 
    esocial_partes_corpo_atingidas_views.json_search, 
        name='esocial_partes_corpo_atingidas_json_search'),

url(r'^esocial-partes-corpo-atingidas/salvar/(?P<hash>.*)/$', 
        esocial_partes_corpo_atingidas_views.salvar, 
        name='esocial_partes_corpo_atingidas_salvar'),



url(r'^esocial-agentes-causadores-acidentes-trabalho/apagar/(?P<hash>.*)/$', 
        esocial_agentes_causadores_acidentes_trabalho_views.apagar, 
        name='esocial_agentes_causadores_acidentes_trabalho_apagar'),

url(r'^esocial-agentes-causadores-acidentes-trabalho/api/$',
            esocial_agentes_causadores_acidentes_trabalho_views.eSocialAgentesCausadoresAcidentesTrabalhoList.as_view() ),

        url(r'^esocial-agentes-causadores-acidentes-trabalho/api/(?P<pk>[0-9]+)/$',
            esocial_agentes_causadores_acidentes_trabalho_views.eSocialAgentesCausadoresAcidentesTrabalhoDetail.as_view() ),

url(r'^esocial-agentes-causadores-acidentes-trabalho/listar/(?P<hash>.*)/$', 
        esocial_agentes_causadores_acidentes_trabalho_views.listar, 
        name='esocial_agentes_causadores_acidentes_trabalho'),
        
        
    url(r'^esocial-agentes-causadores-acidentes-trabalho/json-search/(?P<search>[\w ]+)/$', 
    esocial_agentes_causadores_acidentes_trabalho_views.json_search, 
        name='esocial_agentes_causadores_acidentes_trabalho_json_search'),

url(r'^esocial-agentes-causadores-acidentes-trabalho/salvar/(?P<hash>.*)/$', 
        esocial_agentes_causadores_acidentes_trabalho_views.salvar, 
        name='esocial_agentes_causadores_acidentes_trabalho_salvar'),



url(r'^esocial-agentes-causadores-doencas-profissionais/apagar/(?P<hash>.*)/$', 
        esocial_agentes_causadores_doencas_profissionais_views.apagar, 
        name='esocial_agentes_causadores_doencas_profissionais_apagar'),

url(r'^esocial-agentes-causadores-doencas-profissionais/api/$',
            esocial_agentes_causadores_doencas_profissionais_views.eSocialAgentesCausadoresDoencasProfissionaisList.as_view() ),

        url(r'^esocial-agentes-causadores-doencas-profissionais/api/(?P<pk>[0-9]+)/$',
            esocial_agentes_causadores_doencas_profissionais_views.eSocialAgentesCausadoresDoencasProfissionaisDetail.as_view() ),

url(r'^esocial-agentes-causadores-doencas-profissionais/listar/(?P<hash>.*)/$', 
        esocial_agentes_causadores_doencas_profissionais_views.listar, 
        name='esocial_agentes_causadores_doencas_profissionais'),
        
        
    url(r'^esocial-agentes-causadores-doencas-profissionais/json-search/(?P<search>[\w ]+)/$', 
    esocial_agentes_causadores_doencas_profissionais_views.json_search, 
        name='esocial_agentes_causadores_doencas_profissionais_json_search'),

url(r'^esocial-agentes-causadores-doencas-profissionais/salvar/(?P<hash>.*)/$', 
        esocial_agentes_causadores_doencas_profissionais_views.salvar, 
        name='esocial_agentes_causadores_doencas_profissionais_salvar'),



url(r'^esocial-acidentes-situacoes-geradoras/apagar/(?P<hash>.*)/$', 
        esocial_acidentes_situacoes_geradoras_views.apagar, 
        name='esocial_acidentes_situacoes_geradoras_apagar'),

url(r'^esocial-acidentes-situacoes-geradoras/api/$',
            esocial_acidentes_situacoes_geradoras_views.eSocialAcidentesSituacoesGeradorasList.as_view() ),

        url(r'^esocial-acidentes-situacoes-geradoras/api/(?P<pk>[0-9]+)/$',
            esocial_acidentes_situacoes_geradoras_views.eSocialAcidentesSituacoesGeradorasDetail.as_view() ),

url(r'^esocial-acidentes-situacoes-geradoras/listar/(?P<hash>.*)/$', 
        esocial_acidentes_situacoes_geradoras_views.listar, 
        name='esocial_acidentes_situacoes_geradoras'),
        
        
    url(r'^esocial-acidentes-situacoes-geradoras/json-search/(?P<search>[\w ]+)/$', 
    esocial_acidentes_situacoes_geradoras_views.json_search, 
        name='esocial_acidentes_situacoes_geradoras_json_search'),

url(r'^esocial-acidentes-situacoes-geradoras/salvar/(?P<hash>.*)/$', 
        esocial_acidentes_situacoes_geradoras_views.salvar, 
        name='esocial_acidentes_situacoes_geradoras_salvar'),



url(r'^esocial-naturezas-lesoes/apagar/(?P<hash>.*)/$', 
        esocial_naturezas_lesoes_views.apagar, 
        name='esocial_naturezas_lesoes_apagar'),

url(r'^esocial-naturezas-lesoes/api/$',
            esocial_naturezas_lesoes_views.eSocialNaturezasLesoesList.as_view() ),

        url(r'^esocial-naturezas-lesoes/api/(?P<pk>[0-9]+)/$',
            esocial_naturezas_lesoes_views.eSocialNaturezasLesoesDetail.as_view() ),

url(r'^esocial-naturezas-lesoes/listar/(?P<hash>.*)/$', 
        esocial_naturezas_lesoes_views.listar, 
        name='esocial_naturezas_lesoes'),
        
        
    url(r'^esocial-naturezas-lesoes/json-search/(?P<search>[\w ]+)/$', 
    esocial_naturezas_lesoes_views.json_search, 
        name='esocial_naturezas_lesoes_json_search'),

url(r'^esocial-naturezas-lesoes/salvar/(?P<hash>.*)/$', 
        esocial_naturezas_lesoes_views.salvar, 
        name='esocial_naturezas_lesoes_salvar'),



url(r'^esocial-afastamentos-motivos/apagar/(?P<hash>.*)/$', 
        esocial_afastamentos_motivos_views.apagar, 
        name='esocial_afastamentos_motivos_apagar'),

url(r'^esocial-afastamentos-motivos/api/$',
            esocial_afastamentos_motivos_views.eSocialAfastamentosMotivosList.as_view() ),

        url(r'^esocial-afastamentos-motivos/api/(?P<pk>[0-9]+)/$',
            esocial_afastamentos_motivos_views.eSocialAfastamentosMotivosDetail.as_view() ),

url(r'^esocial-afastamentos-motivos/listar/(?P<hash>.*)/$', 
        esocial_afastamentos_motivos_views.listar, 
        name='esocial_afastamentos_motivos'),
        
        
    url(r'^esocial-afastamentos-motivos/json-search/(?P<search>[\w ]+)/$', 
    esocial_afastamentos_motivos_views.json_search, 
        name='esocial_afastamentos_motivos_json_search'),

url(r'^esocial-afastamentos-motivos/salvar/(?P<hash>.*)/$', 
        esocial_afastamentos_motivos_views.salvar, 
        name='esocial_afastamentos_motivos_salvar'),



url(r'^esocial-desligamentos-motivos/apagar/(?P<hash>.*)/$', 
        esocial_desligamentos_motivos_views.apagar, 
        name='esocial_desligamentos_motivos_apagar'),

url(r'^esocial-desligamentos-motivos/api/$',
            esocial_desligamentos_motivos_views.eSocialDesligamentosMotivosList.as_view() ),

        url(r'^esocial-desligamentos-motivos/api/(?P<pk>[0-9]+)/$',
            esocial_desligamentos_motivos_views.eSocialDesligamentosMotivosDetail.as_view() ),

url(r'^esocial-desligamentos-motivos/listar/(?P<hash>.*)/$', 
        esocial_desligamentos_motivos_views.listar, 
        name='esocial_desligamentos_motivos'),
        
        
    url(r'^esocial-desligamentos-motivos/json-search/(?P<search>[\w ]+)/$', 
    esocial_desligamentos_motivos_views.json_search, 
        name='esocial_desligamentos_motivos_json_search'),

url(r'^esocial-desligamentos-motivos/salvar/(?P<hash>.*)/$', 
        esocial_desligamentos_motivos_views.salvar, 
        name='esocial_desligamentos_motivos_salvar'),



url(r'^esocial-logradouros-tipos/apagar/(?P<hash>.*)/$', 
        esocial_logradouros_tipos_views.apagar, 
        name='esocial_logradouros_tipos_apagar'),

url(r'^esocial-logradouros-tipos/api/$',
            esocial_logradouros_tipos_views.eSocialLogradourosTiposList.as_view() ),

        url(r'^esocial-logradouros-tipos/api/(?P<pk>[0-9]+)/$',
            esocial_logradouros_tipos_views.eSocialLogradourosTiposDetail.as_view() ),

url(r'^esocial-logradouros-tipos/listar/(?P<hash>.*)/$', 
        esocial_logradouros_tipos_views.listar, 
        name='esocial_logradouros_tipos'),
        
        
    url(r'^esocial-logradouros-tipos/json-search/(?P<search>[\w ]+)/$', 
    esocial_logradouros_tipos_views.json_search, 
        name='esocial_logradouros_tipos_json_search'),

url(r'^esocial-logradouros-tipos/salvar/(?P<hash>.*)/$', 
        esocial_logradouros_tipos_views.salvar, 
        name='esocial_logradouros_tipos_salvar'),



url(r'^esocial-naturezas-juridicas/apagar/(?P<hash>.*)/$', 
        esocial_naturezas_juridicas_views.apagar, 
        name='esocial_naturezas_juridicas_apagar'),

url(r'^esocial-naturezas-juridicas/api/$',
            esocial_naturezas_juridicas_views.eSocialNaturezasJuridicasList.as_view() ),

        url(r'^esocial-naturezas-juridicas/api/(?P<pk>[0-9]+)/$',
            esocial_naturezas_juridicas_views.eSocialNaturezasJuridicasDetail.as_view() ),

url(r'^esocial-naturezas-juridicas/listar/(?P<hash>.*)/$', 
        esocial_naturezas_juridicas_views.listar, 
        name='esocial_naturezas_juridicas'),
        
        
    url(r'^esocial-naturezas-juridicas/json-search/(?P<search>[\w ]+)/$', 
    esocial_naturezas_juridicas_views.json_search, 
        name='esocial_naturezas_juridicas_json_search'),

url(r'^esocial-naturezas-juridicas/salvar/(?P<hash>.*)/$', 
        esocial_naturezas_juridicas_views.salvar, 
        name='esocial_naturezas_juridicas_salvar'),



url(r'^esocial-compatibilidades-fpas-classificacoes-tributarias/apagar/(?P<hash>.*)/$', 
        esocial_compatibilidades_fpas_classificacoes_tributarias_views.apagar, 
        name='esocial_compatibilidades_fpas_classificacoes_tributarias_apagar'),

url(r'^esocial-compatibilidades-fpas-classificacoes-tributarias/api/$',
            esocial_compatibilidades_fpas_classificacoes_tributarias_views.eSocialCompatibilidadesFPASClassificacoesTributariasList.as_view() ),

        url(r'^esocial-compatibilidades-fpas-classificacoes-tributarias/api/(?P<pk>[0-9]+)/$',
            esocial_compatibilidades_fpas_classificacoes_tributarias_views.eSocialCompatibilidadesFPASClassificacoesTributariasDetail.as_view() ),

url(r'^esocial-compatibilidades-fpas-classificacoes-tributarias/listar/(?P<hash>.*)/$', 
        esocial_compatibilidades_fpas_classificacoes_tributarias_views.listar, 
        name='esocial_compatibilidades_fpas_classificacoes_tributarias'),
        
        
    url(r'^esocial-compatibilidades-fpas-classificacoes-tributarias/json-search/(?P<search>[\w ]+)/$', 
    esocial_compatibilidades_fpas_classificacoes_tributarias_views.json_search, 
        name='esocial_compatibilidades_fpas_classificacoes_tributarias_json_search'),

url(r'^esocial-compatibilidades-fpas-classificacoes-tributarias/salvar/(?P<hash>.*)/$', 
        esocial_compatibilidades_fpas_classificacoes_tributarias_views.salvar, 
        name='esocial_compatibilidades_fpas_classificacoes_tributarias_salvar'),



url(r'^esocial-fatores-risco/apagar/(?P<hash>.*)/$', 
        esocial_fatores_risco_views.apagar, 
        name='esocial_fatores_risco_apagar'),

url(r'^esocial-fatores-risco/api/$',
            esocial_fatores_risco_views.eSocialFatoresRiscoList.as_view() ),

        url(r'^esocial-fatores-risco/api/(?P<pk>[0-9]+)/$',
            esocial_fatores_risco_views.eSocialFatoresRiscoDetail.as_view() ),

url(r'^esocial-fatores-risco/listar/(?P<hash>.*)/$', 
        esocial_fatores_risco_views.listar, 
        name='esocial_fatores_risco'),
        
        
    url(r'^esocial-fatores-risco/json-search/(?P<search>[\w ]+)/$', 
    esocial_fatores_risco_views.json_search, 
        name='esocial_fatores_risco_json_search'),

url(r'^esocial-fatores-risco/salvar/(?P<hash>.*)/$', 
        esocial_fatores_risco_views.salvar, 
        name='esocial_fatores_risco_salvar'),



url(r'^esocial-codificacoes-acidente-trabalho/apagar/(?P<hash>.*)/$', 
        esocial_codificacoes_acidente_trabalho_views.apagar, 
        name='esocial_codificacoes_acidente_trabalho_apagar'),

url(r'^esocial-codificacoes-acidente-trabalho/api/$',
            esocial_codificacoes_acidente_trabalho_views.eSocialCodificacoesAcidenteTrabalhoList.as_view() ),

        url(r'^esocial-codificacoes-acidente-trabalho/api/(?P<pk>[0-9]+)/$',
            esocial_codificacoes_acidente_trabalho_views.eSocialCodificacoesAcidenteTrabalhoDetail.as_view() ),

url(r'^esocial-codificacoes-acidente-trabalho/listar/(?P<hash>.*)/$', 
        esocial_codificacoes_acidente_trabalho_views.listar, 
        name='esocial_codificacoes_acidente_trabalho'),
        
        
    url(r'^esocial-codificacoes-acidente-trabalho/json-search/(?P<search>[\w ]+)/$', 
    esocial_codificacoes_acidente_trabalho_views.json_search, 
        name='esocial_codificacoes_acidente_trabalho_json_search'),

url(r'^esocial-codificacoes-acidente-trabalho/salvar/(?P<hash>.*)/$', 
        esocial_codificacoes_acidente_trabalho_views.salvar, 
        name='esocial_codificacoes_acidente_trabalho_salvar'),



url(r'^esocial-beneficios-previdenciarios-tipos/apagar/(?P<hash>.*)/$', 
        esocial_beneficios_previdenciarios_tipos_views.apagar, 
        name='esocial_beneficios_previdenciarios_tipos_apagar'),

url(r'^esocial-beneficios-previdenciarios-tipos/api/$',
            esocial_beneficios_previdenciarios_tipos_views.eSocialBeneficiosPrevidenciariosTiposList.as_view() ),

        url(r'^esocial-beneficios-previdenciarios-tipos/api/(?P<pk>[0-9]+)/$',
            esocial_beneficios_previdenciarios_tipos_views.eSocialBeneficiosPrevidenciariosTiposDetail.as_view() ),

url(r'^esocial-beneficios-previdenciarios-tipos/listar/(?P<hash>.*)/$', 
        esocial_beneficios_previdenciarios_tipos_views.listar, 
        name='esocial_beneficios_previdenciarios_tipos'),
        
        
    url(r'^esocial-beneficios-previdenciarios-tipos/json-search/(?P<search>[\w ]+)/$', 
    esocial_beneficios_previdenciarios_tipos_views.json_search, 
        name='esocial_beneficios_previdenciarios_tipos_json_search'),

url(r'^esocial-beneficios-previdenciarios-tipos/salvar/(?P<hash>.*)/$', 
        esocial_beneficios_previdenciarios_tipos_views.salvar, 
        name='esocial_beneficios_previdenciarios_tipos_salvar'),



url(r'^esocial-beneficios-previdenciarios-cessacao-motivos/apagar/(?P<hash>.*)/$', 
        esocial_beneficios_previdenciarios_cessacao_motivos_views.apagar, 
        name='esocial_beneficios_previdenciarios_cessacao_motivos_apagar'),

url(r'^esocial-beneficios-previdenciarios-cessacao-motivos/api/$',
            esocial_beneficios_previdenciarios_cessacao_motivos_views.eSocialBeneficiosPrevidenciariosCessacaoMotivosList.as_view() ),

        url(r'^esocial-beneficios-previdenciarios-cessacao-motivos/api/(?P<pk>[0-9]+)/$',
            esocial_beneficios_previdenciarios_cessacao_motivos_views.eSocialBeneficiosPrevidenciariosCessacaoMotivosDetail.as_view() ),

url(r'^esocial-beneficios-previdenciarios-cessacao-motivos/listar/(?P<hash>.*)/$', 
        esocial_beneficios_previdenciarios_cessacao_motivos_views.listar, 
        name='esocial_beneficios_previdenciarios_cessacao_motivos'),
        
        
    url(r'^esocial-beneficios-previdenciarios-cessacao-motivos/json-search/(?P<search>[\w ]+)/$', 
    esocial_beneficios_previdenciarios_cessacao_motivos_views.json_search, 
        name='esocial_beneficios_previdenciarios_cessacao_motivos_json_search'),

url(r'^esocial-beneficios-previdenciarios-cessacao-motivos/salvar/(?P<hash>.*)/$', 
        esocial_beneficios_previdenciarios_cessacao_motivos_views.salvar, 
        name='esocial_beneficios_previdenciarios_cessacao_motivos_salvar'),



url(r'^esocial-procedimentos-diagnosticos/apagar/(?P<hash>.*)/$', 
        esocial_procedimentos_diagnosticos_views.apagar, 
        name='esocial_procedimentos_diagnosticos_apagar'),

url(r'^esocial-procedimentos-diagnosticos/api/$',
            esocial_procedimentos_diagnosticos_views.eSocialProcedimentosDiagnosticosList.as_view() ),

        url(r'^esocial-procedimentos-diagnosticos/api/(?P<pk>[0-9]+)/$',
            esocial_procedimentos_diagnosticos_views.eSocialProcedimentosDiagnosticosDetail.as_view() ),

url(r'^esocial-procedimentos-diagnosticos/listar/(?P<hash>.*)/$', 
        esocial_procedimentos_diagnosticos_views.listar, 
        name='esocial_procedimentos_diagnosticos'),
        
        
    url(r'^esocial-procedimentos-diagnosticos/json-search/(?P<search>[\w ]+)/$', 
    esocial_procedimentos_diagnosticos_views.json_search, 
        name='esocial_procedimentos_diagnosticos_json_search'),

url(r'^esocial-procedimentos-diagnosticos/salvar/(?P<hash>.*)/$', 
        esocial_procedimentos_diagnosticos_views.salvar, 
        name='esocial_procedimentos_diagnosticos_salvar'),



url(r'^esocial-atividades-periculosas-insalubres-especiais/apagar/(?P<hash>.*)/$', 
        esocial_atividades_periculosas_insalubres_especiais_views.apagar, 
        name='esocial_atividades_periculosas_insalubres_especiais_apagar'),

url(r'^esocial-atividades-periculosas-insalubres-especiais/api/$',
            esocial_atividades_periculosas_insalubres_especiais_views.eSocialAtividadesPericulosasInsalubresEspeciaisList.as_view() ),

        url(r'^esocial-atividades-periculosas-insalubres-especiais/api/(?P<pk>[0-9]+)/$',
            esocial_atividades_periculosas_insalubres_especiais_views.eSocialAtividadesPericulosasInsalubresEspeciaisDetail.as_view() ),

url(r'^esocial-atividades-periculosas-insalubres-especiais/listar/(?P<hash>.*)/$', 
        esocial_atividades_periculosas_insalubres_especiais_views.listar, 
        name='esocial_atividades_periculosas_insalubres_especiais'),
        
        
    url(r'^esocial-atividades-periculosas-insalubres-especiais/json-search/(?P<search>[\w ]+)/$', 
    esocial_atividades_periculosas_insalubres_especiais_views.json_search, 
        name='esocial_atividades_periculosas_insalubres_especiais_json_search'),

url(r'^esocial-atividades-periculosas-insalubres-especiais/salvar/(?P<hash>.*)/$', 
        esocial_atividades_periculosas_insalubres_especiais_views.salvar, 
        name='esocial_atividades_periculosas_insalubres_especiais_salvar'),



url(r'^esocial-treinamentos-capacitacoes-exercicios-simulados/apagar/(?P<hash>.*)/$', 
        esocial_treinamentos_capacitacoes_exercicios_simulados_views.apagar, 
        name='esocial_treinamentos_capacitacoes_exercicios_simulados_apagar'),

url(r'^esocial-treinamentos-capacitacoes-exercicios-simulados/api/$',
            esocial_treinamentos_capacitacoes_exercicios_simulados_views.eSocialTreinamentosCapacitacoesExerciciosSimuladosList.as_view() ),

        url(r'^esocial-treinamentos-capacitacoes-exercicios-simulados/api/(?P<pk>[0-9]+)/$',
            esocial_treinamentos_capacitacoes_exercicios_simulados_views.eSocialTreinamentosCapacitacoesExerciciosSimuladosDetail.as_view() ),

url(r'^esocial-treinamentos-capacitacoes-exercicios-simulados/listar/(?P<hash>.*)/$', 
        esocial_treinamentos_capacitacoes_exercicios_simulados_views.listar, 
        name='esocial_treinamentos_capacitacoes_exercicios_simulados'),
        
        
    url(r'^esocial-treinamentos-capacitacoes-exercicios-simulados/json-search/(?P<search>[\w ]+)/$', 
    esocial_treinamentos_capacitacoes_exercicios_simulados_views.json_search, 
        name='esocial_treinamentos_capacitacoes_exercicios_simulados_json_search'),

url(r'^esocial-treinamentos-capacitacoes-exercicios-simulados/salvar/(?P<hash>.*)/$', 
        esocial_treinamentos_capacitacoes_exercicios_simulados_views.salvar, 
        name='esocial_treinamentos_capacitacoes_exercicios_simulados_salvar'),



url(r'^esocial-programas-planos-documentos/apagar/(?P<hash>.*)/$', 
        esocial_programas_planos_documentos_views.apagar, 
        name='esocial_programas_planos_documentos_apagar'),

url(r'^esocial-programas-planos-documentos/api/$',
            esocial_programas_planos_documentos_views.eSocialProgramasPlanosDocumentosList.as_view() ),

        url(r'^esocial-programas-planos-documentos/api/(?P<pk>[0-9]+)/$',
            esocial_programas_planos_documentos_views.eSocialProgramasPlanosDocumentosDetail.as_view() ),

url(r'^esocial-programas-planos-documentos/listar/(?P<hash>.*)/$', 
        esocial_programas_planos_documentos_views.listar, 
        name='esocial_programas_planos_documentos'),
        
        
    url(r'^esocial-programas-planos-documentos/json-search/(?P<search>[\w ]+)/$', 
    esocial_programas_planos_documentos_views.json_search, 
        name='esocial_programas_planos_documentos_json_search'),

url(r'^esocial-programas-planos-documentos/salvar/(?P<hash>.*)/$', 
        esocial_programas_planos_documentos_views.salvar, 
        name='esocial_programas_planos_documentos_salvar'),



url(r'^efdreinf-pagamentos-codigos/apagar/(?P<hash>.*)/$', 
        efdreinf_pagamentos_codigos_views.apagar, 
        name='efdreinf_pagamentos_codigos_apagar'),

url(r'^efdreinf-pagamentos-codigos/api/$',
            efdreinf_pagamentos_codigos_views.EFDReinfPagamentosCodigosList.as_view() ),

        url(r'^efdreinf-pagamentos-codigos/api/(?P<pk>[0-9]+)/$',
            efdreinf_pagamentos_codigos_views.EFDReinfPagamentosCodigosDetail.as_view() ),

url(r'^efdreinf-pagamentos-codigos/listar/(?P<hash>.*)/$', 
        efdreinf_pagamentos_codigos_views.listar, 
        name='efdreinf_pagamentos_codigos'),
        
        
    url(r'^efdreinf-pagamentos-codigos/json-search/(?P<search>[\w ]+)/$', 
    efdreinf_pagamentos_codigos_views.json_search, 
        name='efdreinf_pagamentos_codigos_json_search'),

url(r'^efdreinf-pagamentos-codigos/salvar/(?P<hash>.*)/$', 
        efdreinf_pagamentos_codigos_views.salvar, 
        name='efdreinf_pagamentos_codigos_salvar'),



url(r'^efdreinf-regras-pagamentos-codigos/apagar/(?P<hash>.*)/$', 
        efdreinf_regras_pagamentos_codigos_views.apagar, 
        name='efdreinf_regras_pagamentos_codigos_apagar'),

url(r'^efdreinf-regras-pagamentos-codigos/api/$',
            efdreinf_regras_pagamentos_codigos_views.EFDReinfRegrasPagamentosCodigosList.as_view() ),

        url(r'^efdreinf-regras-pagamentos-codigos/api/(?P<pk>[0-9]+)/$',
            efdreinf_regras_pagamentos_codigos_views.EFDReinfRegrasPagamentosCodigosDetail.as_view() ),

url(r'^efdreinf-regras-pagamentos-codigos/listar/(?P<hash>.*)/$', 
        efdreinf_regras_pagamentos_codigos_views.listar, 
        name='efdreinf_regras_pagamentos_codigos'),
        
        
    url(r'^efdreinf-regras-pagamentos-codigos/json-search/(?P<search>[\w ]+)/$', 
    efdreinf_regras_pagamentos_codigos_views.json_search, 
        name='efdreinf_regras_pagamentos_codigos_json_search'),

url(r'^efdreinf-regras-pagamentos-codigos/salvar/(?P<hash>.*)/$', 
        efdreinf_regras_pagamentos_codigos_views.salvar, 
        name='efdreinf_regras_pagamentos_codigos_salvar'),



url(r'^efdreinf-rendimentos-beneficiarios-exterior/apagar/(?P<hash>.*)/$', 
        efdreinf_rendimentos_beneficiarios_exterior_views.apagar, 
        name='efdreinf_rendimentos_beneficiarios_exterior_apagar'),

url(r'^efdreinf-rendimentos-beneficiarios-exterior/api/$',
            efdreinf_rendimentos_beneficiarios_exterior_views.EFDReinfRendimentosBeneficiariosExteriorList.as_view() ),

        url(r'^efdreinf-rendimentos-beneficiarios-exterior/api/(?P<pk>[0-9]+)/$',
            efdreinf_rendimentos_beneficiarios_exterior_views.EFDReinfRendimentosBeneficiariosExteriorDetail.as_view() ),

url(r'^efdreinf-rendimentos-beneficiarios-exterior/listar/(?P<hash>.*)/$', 
        efdreinf_rendimentos_beneficiarios_exterior_views.listar, 
        name='efdreinf_rendimentos_beneficiarios_exterior'),
        
        
    url(r'^efdreinf-rendimentos-beneficiarios-exterior/json-search/(?P<search>[\w ]+)/$', 
    efdreinf_rendimentos_beneficiarios_exterior_views.json_search, 
        name='efdreinf_rendimentos_beneficiarios_exterior_json_search'),

url(r'^efdreinf-rendimentos-beneficiarios-exterior/salvar/(?P<hash>.*)/$', 
        efdreinf_rendimentos_beneficiarios_exterior_views.salvar, 
        name='efdreinf_rendimentos_beneficiarios_exterior_salvar'),



url(r'^efdreinf-rendimentos-beneficiarios-exterior-tributacao/apagar/(?P<hash>.*)/$', 
        efdreinf_rendimentos_beneficiarios_exterior_tributacao_views.apagar, 
        name='efdreinf_rendimentos_beneficiarios_exterior_tributacao_apagar'),

url(r'^efdreinf-rendimentos-beneficiarios-exterior-tributacao/api/$',
            efdreinf_rendimentos_beneficiarios_exterior_tributacao_views.EFDReinfRendimentosBeneficiariosExteriorTributacaoList.as_view() ),

        url(r'^efdreinf-rendimentos-beneficiarios-exterior-tributacao/api/(?P<pk>[0-9]+)/$',
            efdreinf_rendimentos_beneficiarios_exterior_tributacao_views.EFDReinfRendimentosBeneficiariosExteriorTributacaoDetail.as_view() ),

url(r'^efdreinf-rendimentos-beneficiarios-exterior-tributacao/listar/(?P<hash>.*)/$', 
        efdreinf_rendimentos_beneficiarios_exterior_tributacao_views.listar, 
        name='efdreinf_rendimentos_beneficiarios_exterior_tributacao'),
        
        
    url(r'^efdreinf-rendimentos-beneficiarios-exterior-tributacao/json-search/(?P<search>[\w ]+)/$', 
    efdreinf_rendimentos_beneficiarios_exterior_tributacao_views.json_search, 
        name='efdreinf_rendimentos_beneficiarios_exterior_tributacao_json_search'),

url(r'^efdreinf-rendimentos-beneficiarios-exterior-tributacao/salvar/(?P<hash>.*)/$', 
        efdreinf_rendimentos_beneficiarios_exterior_tributacao_views.salvar, 
        name='efdreinf_rendimentos_beneficiarios_exterior_tributacao_salvar'),



url(r'^efdreinf-informacoes-beneficiarios-exterior/apagar/(?P<hash>.*)/$', 
        efdreinf_informacoes_beneficiarios_exterior_views.apagar, 
        name='efdreinf_informacoes_beneficiarios_exterior_apagar'),

url(r'^efdreinf-informacoes-beneficiarios-exterior/api/$',
            efdreinf_informacoes_beneficiarios_exterior_views.EFDReinfInformacoesBeneficiariosExteriorList.as_view() ),

        url(r'^efdreinf-informacoes-beneficiarios-exterior/api/(?P<pk>[0-9]+)/$',
            efdreinf_informacoes_beneficiarios_exterior_views.EFDReinfInformacoesBeneficiariosExteriorDetail.as_view() ),

url(r'^efdreinf-informacoes-beneficiarios-exterior/listar/(?P<hash>.*)/$', 
        efdreinf_informacoes_beneficiarios_exterior_views.listar, 
        name='efdreinf_informacoes_beneficiarios_exterior'),
        
        
    url(r'^efdreinf-informacoes-beneficiarios-exterior/json-search/(?P<search>[\w ]+)/$', 
    efdreinf_informacoes_beneficiarios_exterior_views.json_search, 
        name='efdreinf_informacoes_beneficiarios_exterior_json_search'),

url(r'^efdreinf-informacoes-beneficiarios-exterior/salvar/(?P<hash>.*)/$', 
        efdreinf_informacoes_beneficiarios_exterior_views.salvar, 
        name='efdreinf_informacoes_beneficiarios_exterior_salvar'),



url(r'^efdreinf-classificacao-servicos-prestados/apagar/(?P<hash>.*)/$', 
        efdreinf_classificacao_servicos_prestados_views.apagar, 
        name='efdreinf_classificacao_servicos_prestados_apagar'),

url(r'^efdreinf-classificacao-servicos-prestados/api/$',
            efdreinf_classificacao_servicos_prestados_views.EFDReinfClassificacaoServicosPrestadosList.as_view() ),

        url(r'^efdreinf-classificacao-servicos-prestados/api/(?P<pk>[0-9]+)/$',
            efdreinf_classificacao_servicos_prestados_views.EFDReinfClassificacaoServicosPrestadosDetail.as_view() ),

url(r'^efdreinf-classificacao-servicos-prestados/listar/(?P<hash>.*)/$', 
        efdreinf_classificacao_servicos_prestados_views.listar, 
        name='efdreinf_classificacao_servicos_prestados'),
        
        
    url(r'^efdreinf-classificacao-servicos-prestados/json-search/(?P<search>[\w ]+)/$', 
    efdreinf_classificacao_servicos_prestados_views.json_search, 
        name='efdreinf_classificacao_servicos_prestados_json_search'),

url(r'^efdreinf-classificacao-servicos-prestados/salvar/(?P<hash>.*)/$', 
        efdreinf_classificacao_servicos_prestados_views.salvar, 
        name='efdreinf_classificacao_servicos_prestados_salvar'),



url(r'^efdreinf-paises/apagar/(?P<hash>.*)/$', 
        efdreinf_paises_views.apagar, 
        name='efdreinf_paises_apagar'),

url(r'^efdreinf-paises/api/$',
            efdreinf_paises_views.EFDReinfPaisesList.as_view() ),

        url(r'^efdreinf-paises/api/(?P<pk>[0-9]+)/$',
            efdreinf_paises_views.EFDReinfPaisesDetail.as_view() ),

url(r'^efdreinf-paises/listar/(?P<hash>.*)/$', 
        efdreinf_paises_views.listar, 
        name='efdreinf_paises'),
        
        
    url(r'^efdreinf-paises/json-search/(?P<search>[\w ]+)/$', 
    efdreinf_paises_views.json_search, 
        name='efdreinf_paises_json_search'),

url(r'^efdreinf-paises/salvar/(?P<hash>.*)/$', 
        efdreinf_paises_views.salvar, 
        name='efdreinf_paises_salvar'),



url(r'^efdreinf-classificacao-tributaria/apagar/(?P<hash>.*)/$', 
        efdreinf_classificacao_tributaria_views.apagar, 
        name='efdreinf_classificacao_tributaria_apagar'),

url(r'^efdreinf-classificacao-tributaria/api/$',
            efdreinf_classificacao_tributaria_views.EFDReinfClassificacaoTributariaList.as_view() ),

        url(r'^efdreinf-classificacao-tributaria/api/(?P<pk>[0-9]+)/$',
            efdreinf_classificacao_tributaria_views.EFDReinfClassificacaoTributariaDetail.as_view() ),

url(r'^efdreinf-classificacao-tributaria/listar/(?P<hash>.*)/$', 
        efdreinf_classificacao_tributaria_views.listar, 
        name='efdreinf_classificacao_tributaria'),
        
        
    url(r'^efdreinf-classificacao-tributaria/json-search/(?P<search>[\w ]+)/$', 
    efdreinf_classificacao_tributaria_views.json_search, 
        name='efdreinf_classificacao_tributaria_json_search'),

url(r'^efdreinf-classificacao-tributaria/salvar/(?P<hash>.*)/$', 
        efdreinf_classificacao_tributaria_views.salvar, 
        name='efdreinf_classificacao_tributaria_salvar'),



url(r'^efdreinf-codigos-atividades-produtos-servicos-cprb/apagar/(?P<hash>.*)/$', 
        efdreinf_codigos_atividades_produtos_servicos_cprb_views.apagar, 
        name='efdreinf_codigos_atividades_produtos_servicos_cprb_apagar'),

url(r'^efdreinf-codigos-atividades-produtos-servicos-cprb/api/$',
            efdreinf_codigos_atividades_produtos_servicos_cprb_views.EFDReinfCodigosAtividadesProdutosServicosCPRBList.as_view() ),

        url(r'^efdreinf-codigos-atividades-produtos-servicos-cprb/api/(?P<pk>[0-9]+)/$',
            efdreinf_codigos_atividades_produtos_servicos_cprb_views.EFDReinfCodigosAtividadesProdutosServicosCPRBDetail.as_view() ),

url(r'^efdreinf-codigos-atividades-produtos-servicos-cprb/listar/(?P<hash>.*)/$', 
        efdreinf_codigos_atividades_produtos_servicos_cprb_views.listar, 
        name='efdreinf_codigos_atividades_produtos_servicos_cprb'),
        
        
    url(r'^efdreinf-codigos-atividades-produtos-servicos-cprb/json-search/(?P<search>[\w ]+)/$', 
    efdreinf_codigos_atividades_produtos_servicos_cprb_views.json_search, 
        name='efdreinf_codigos_atividades_produtos_servicos_cprb_json_search'),

url(r'^efdreinf-codigos-atividades-produtos-servicos-cprb/salvar/(?P<hash>.*)/$', 
        efdreinf_codigos_atividades_produtos_servicos_cprb_views.salvar, 
        name='efdreinf_codigos_atividades_produtos_servicos_cprb_salvar'),



url(r'^efdreinf-eventos/apagar/(?P<hash>.*)/$', 
        efdreinf_eventos_views.apagar, 
        name='efdreinf_eventos_apagar'),

url(r'^efdreinf-eventos/api/$',
            efdreinf_eventos_views.EFDReinfEventosList.as_view() ),

        url(r'^efdreinf-eventos/api/(?P<pk>[0-9]+)/$',
            efdreinf_eventos_views.EFDReinfEventosDetail.as_view() ),

url(r'^efdreinf-eventos/listar/(?P<hash>.*)/$', 
        efdreinf_eventos_views.listar, 
        name='efdreinf_eventos'),
        
        
    url(r'^efdreinf-eventos/json-search/(?P<search>[\w ]+)/$', 
    efdreinf_eventos_views.json_search, 
        name='efdreinf_eventos_json_search'),

url(r'^efdreinf-eventos/salvar/(?P<hash>.*)/$', 
        efdreinf_eventos_views.salvar, 
        name='efdreinf_eventos_salvar'),





]