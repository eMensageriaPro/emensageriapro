#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

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

urlpatterns = patterns('',
    # Examples:



url(r'^municipios/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.municipios.apagar', 
        name='municipios_apagar'),

url(r'^municipios/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.municipios.listar', 
        name='municipios'),
        
        
    url(r'^municipios/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.municipios.json_search', name='municipios_json_search'),

url(r'^municipios/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.municipios.salvar', 
        name='municipios_salvar'),



url(r'^cbo/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.cbo.apagar', 
        name='cbo_apagar'),

url(r'^cbo/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.cbo.listar', 
        name='cbo'),
        
        
    url(r'^cbo/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.cbo.json_search', name='cbo_json_search'),

url(r'^cbo/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.cbo.salvar', 
        name='cbo_salvar'),



url(r'^cid/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.cid.apagar', 
        name='cid_apagar'),

url(r'^cid/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.cid.listar', 
        name='cid'),
        
        
    url(r'^cid/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.cid.json_search', name='cid_json_search'),

url(r'^cid/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.cid.salvar', 
        name='cid_salvar'),



url(r'^cnae/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.cnae.apagar', 
        name='cnae_apagar'),

url(r'^cnae/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.cnae.listar', 
        name='cnae'),
        
        
    url(r'^cnae/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.cnae.json_search', name='cnae_json_search'),

url(r'^cnae/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.cnae.salvar', 
        name='cnae_salvar'),



url(r'^esocial-trabalhadores-categorias/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_trabalhadores_categorias.apagar', 
        name='esocial_trabalhadores_categorias_apagar'),

url(r'^esocial-trabalhadores-categorias/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_trabalhadores_categorias.listar', 
        name='esocial_trabalhadores_categorias'),
        
        
    url(r'^esocial-trabalhadores-categorias/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_trabalhadores_categorias.json_search', name='esocial_trabalhadores_categorias_json_search'),

url(r'^esocial-trabalhadores-categorias/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_trabalhadores_categorias.salvar', 
        name='esocial_trabalhadores_categorias_salvar'),



url(r'^esocial-financiamentos-aposentadorias-especiais/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_financiamentos_aposentadorias_especiais.apagar', 
        name='esocial_financiamentos_aposentadorias_especiais_apagar'),

url(r'^esocial-financiamentos-aposentadorias-especiais/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_financiamentos_aposentadorias_especiais.listar', 
        name='esocial_financiamentos_aposentadorias_especiais'),
        
        
    url(r'^esocial-financiamentos-aposentadorias-especiais/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_financiamentos_aposentadorias_especiais.json_search', name='esocial_financiamentos_aposentadorias_especiais_json_search'),

url(r'^esocial-financiamentos-aposentadorias-especiais/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_financiamentos_aposentadorias_especiais.salvar', 
        name='esocial_financiamentos_aposentadorias_especiais_salvar'),



url(r'^esocial-naturezas-rubricas/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_naturezas_rubricas.apagar', 
        name='esocial_naturezas_rubricas_apagar'),

url(r'^esocial-naturezas-rubricas/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_naturezas_rubricas.listar', 
        name='esocial_naturezas_rubricas'),
        
        
    url(r'^esocial-naturezas-rubricas/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_naturezas_rubricas.json_search', name='esocial_naturezas_rubricas_json_search'),

url(r'^esocial-naturezas-rubricas/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_naturezas_rubricas.salvar', 
        name='esocial_naturezas_rubricas_salvar'),



url(r'^esocial-codigo-aliquotas-fpas-terceiros/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_codigo_aliquotas_fpas_terceiros.apagar', 
        name='esocial_codigo_aliquotas_fpas_terceiros_apagar'),

url(r'^esocial-codigo-aliquotas-fpas-terceiros/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_codigo_aliquotas_fpas_terceiros.listar', 
        name='esocial_codigo_aliquotas_fpas_terceiros'),
        
        
    url(r'^esocial-codigo-aliquotas-fpas-terceiros/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_codigo_aliquotas_fpas_terceiros.json_search', name='esocial_codigo_aliquotas_fpas_terceiros_json_search'),

url(r'^esocial-codigo-aliquotas-fpas-terceiros/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_codigo_aliquotas_fpas_terceiros.salvar', 
        name='esocial_codigo_aliquotas_fpas_terceiros_salvar'),



url(r'^esocial-inscricoes-tipos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_inscricoes_tipos.apagar', 
        name='esocial_inscricoes_tipos_apagar'),

url(r'^esocial-inscricoes-tipos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_inscricoes_tipos.listar', 
        name='esocial_inscricoes_tipos'),
        
        
    url(r'^esocial-inscricoes-tipos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_inscricoes_tipos.json_search', name='esocial_inscricoes_tipos_json_search'),

url(r'^esocial-inscricoes-tipos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_inscricoes_tipos.salvar', 
        name='esocial_inscricoes_tipos_salvar'),



url(r'^esocial-paises/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_paises.apagar', 
        name='esocial_paises_apagar'),

url(r'^esocial-paises/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_paises.listar', 
        name='esocial_paises'),
        
        
    url(r'^esocial-paises/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_paises.json_search', name='esocial_paises_json_search'),

url(r'^esocial-paises/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_paises.salvar', 
        name='esocial_paises_salvar'),

)


urlpatterns += patterns('',


url(r'^esocial-dependentes-tipos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_dependentes_tipos.apagar', 
        name='esocial_dependentes_tipos_apagar'),

url(r'^esocial-dependentes-tipos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_dependentes_tipos.listar', 
        name='esocial_dependentes_tipos'),
        
        
    url(r'^esocial-dependentes-tipos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_dependentes_tipos.json_search', name='esocial_dependentes_tipos_json_search'),

url(r'^esocial-dependentes-tipos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_dependentes_tipos.salvar', 
        name='esocial_dependentes_tipos_salvar'),



url(r'^esocial-classificacoes-tributarias/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_classificacoes_tributarias.apagar', 
        name='esocial_classificacoes_tributarias_apagar'),

url(r'^esocial-classificacoes-tributarias/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_classificacoes_tributarias.listar', 
        name='esocial_classificacoes_tributarias'),
        
        
    url(r'^esocial-classificacoes-tributarias/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_classificacoes_tributarias.json_search', name='esocial_classificacoes_tributarias_json_search'),

url(r'^esocial-classificacoes-tributarias/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_classificacoes_tributarias.salvar', 
        name='esocial_classificacoes_tributarias_salvar'),



url(r'^esocial-arquivos-esocial-tipos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_arquivos_esocial_tipos.apagar', 
        name='esocial_arquivos_esocial_tipos_apagar'),

url(r'^esocial-arquivos-esocial-tipos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_arquivos_esocial_tipos.listar', 
        name='esocial_arquivos_esocial_tipos'),
        
        
    url(r'^esocial-arquivos-esocial-tipos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_arquivos_esocial_tipos.json_search', name='esocial_arquivos_esocial_tipos_json_search'),

url(r'^esocial-arquivos-esocial-tipos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_arquivos_esocial_tipos.salvar', 
        name='esocial_arquivos_esocial_tipos_salvar'),



url(r'^esocial-lotacoes-tributarias-tipos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_lotacoes_tributarias_tipos.apagar', 
        name='esocial_lotacoes_tributarias_tipos_apagar'),

url(r'^esocial-lotacoes-tributarias-tipos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_lotacoes_tributarias_tipos.listar', 
        name='esocial_lotacoes_tributarias_tipos'),
        
        
    url(r'^esocial-lotacoes-tributarias-tipos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_lotacoes_tributarias_tipos.json_search', name='esocial_lotacoes_tributarias_tipos_json_search'),

url(r'^esocial-lotacoes-tributarias-tipos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_lotacoes_tributarias_tipos.salvar', 
        name='esocial_lotacoes_tributarias_tipos_salvar'),



url(r'^esocial-compatibilidades-categorias-classificacoes-lotacoes/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_compatibilidades_categorias_classificacoes_lotacoes.apagar', 
        name='esocial_compatibilidades_categorias_classificacoes_lotacoes_apagar'),

url(r'^esocial-compatibilidades-categorias-classificacoes-lotacoes/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_compatibilidades_categorias_classificacoes_lotacoes.listar', 
        name='esocial_compatibilidades_categorias_classificacoes_lotacoes'),
        
        
    url(r'^esocial-compatibilidades-categorias-classificacoes-lotacoes/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_compatibilidades_categorias_classificacoes_lotacoes.json_search', name='esocial_compatibilidades_categorias_classificacoes_lotacoes_json_search'),

url(r'^esocial-compatibilidades-categorias-classificacoes-lotacoes/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_compatibilidades_categorias_classificacoes_lotacoes.salvar', 
        name='esocial_compatibilidades_categorias_classificacoes_lotacoes_salvar'),



url(r'^esocial-compatibilidades-lotacoes-classificacoes/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_compatibilidades_lotacoes_classificacoes.apagar', 
        name='esocial_compatibilidades_lotacoes_classificacoes_apagar'),

url(r'^esocial-compatibilidades-lotacoes-classificacoes/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_compatibilidades_lotacoes_classificacoes.listar', 
        name='esocial_compatibilidades_lotacoes_classificacoes'),
        
        
    url(r'^esocial-compatibilidades-lotacoes-classificacoes/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_compatibilidades_lotacoes_classificacoes.json_search', name='esocial_compatibilidades_lotacoes_classificacoes_json_search'),

url(r'^esocial-compatibilidades-lotacoes-classificacoes/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_compatibilidades_lotacoes_classificacoes.salvar', 
        name='esocial_compatibilidades_lotacoes_classificacoes_salvar'),



url(r'^esocial-partes-corpo-atingidas/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_partes_corpo_atingidas.apagar', 
        name='esocial_partes_corpo_atingidas_apagar'),

url(r'^esocial-partes-corpo-atingidas/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_partes_corpo_atingidas.listar', 
        name='esocial_partes_corpo_atingidas'),
        
        
    url(r'^esocial-partes-corpo-atingidas/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_partes_corpo_atingidas.json_search', name='esocial_partes_corpo_atingidas_json_search'),

url(r'^esocial-partes-corpo-atingidas/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_partes_corpo_atingidas.salvar', 
        name='esocial_partes_corpo_atingidas_salvar'),



url(r'^esocial-agentes-causadores-acidentes-trabalho/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_agentes_causadores_acidentes_trabalho.apagar', 
        name='esocial_agentes_causadores_acidentes_trabalho_apagar'),

url(r'^esocial-agentes-causadores-acidentes-trabalho/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_agentes_causadores_acidentes_trabalho.listar', 
        name='esocial_agentes_causadores_acidentes_trabalho'),
        
        
    url(r'^esocial-agentes-causadores-acidentes-trabalho/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_agentes_causadores_acidentes_trabalho.json_search', name='esocial_agentes_causadores_acidentes_trabalho_json_search'),

url(r'^esocial-agentes-causadores-acidentes-trabalho/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_agentes_causadores_acidentes_trabalho.salvar', 
        name='esocial_agentes_causadores_acidentes_trabalho_salvar'),



url(r'^esocial-agentes-causadores-doencas-profissionais/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_agentes_causadores_doencas_profissionais.apagar', 
        name='esocial_agentes_causadores_doencas_profissionais_apagar'),

url(r'^esocial-agentes-causadores-doencas-profissionais/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_agentes_causadores_doencas_profissionais.listar', 
        name='esocial_agentes_causadores_doencas_profissionais'),
        
        
    url(r'^esocial-agentes-causadores-doencas-profissionais/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_agentes_causadores_doencas_profissionais.json_search', name='esocial_agentes_causadores_doencas_profissionais_json_search'),

url(r'^esocial-agentes-causadores-doencas-profissionais/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_agentes_causadores_doencas_profissionais.salvar', 
        name='esocial_agentes_causadores_doencas_profissionais_salvar'),



url(r'^esocial-acidentes-situacoes-geradoras/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_acidentes_situacoes_geradoras.apagar', 
        name='esocial_acidentes_situacoes_geradoras_apagar'),

url(r'^esocial-acidentes-situacoes-geradoras/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_acidentes_situacoes_geradoras.listar', 
        name='esocial_acidentes_situacoes_geradoras'),
        
        
    url(r'^esocial-acidentes-situacoes-geradoras/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_acidentes_situacoes_geradoras.json_search', name='esocial_acidentes_situacoes_geradoras_json_search'),

url(r'^esocial-acidentes-situacoes-geradoras/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_acidentes_situacoes_geradoras.salvar', 
        name='esocial_acidentes_situacoes_geradoras_salvar'),

)


urlpatterns += patterns('',


url(r'^esocial-naturezas-lesoes/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_naturezas_lesoes.apagar', 
        name='esocial_naturezas_lesoes_apagar'),

url(r'^esocial-naturezas-lesoes/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_naturezas_lesoes.listar', 
        name='esocial_naturezas_lesoes'),
        
        
    url(r'^esocial-naturezas-lesoes/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_naturezas_lesoes.json_search', name='esocial_naturezas_lesoes_json_search'),

url(r'^esocial-naturezas-lesoes/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_naturezas_lesoes.salvar', 
        name='esocial_naturezas_lesoes_salvar'),



url(r'^esocial-afastamentos-motivos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_afastamentos_motivos.apagar', 
        name='esocial_afastamentos_motivos_apagar'),

url(r'^esocial-afastamentos-motivos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_afastamentos_motivos.listar', 
        name='esocial_afastamentos_motivos'),
        
        
    url(r'^esocial-afastamentos-motivos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_afastamentos_motivos.json_search', name='esocial_afastamentos_motivos_json_search'),

url(r'^esocial-afastamentos-motivos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_afastamentos_motivos.salvar', 
        name='esocial_afastamentos_motivos_salvar'),



url(r'^esocial-desligamentos-motivos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_desligamentos_motivos.apagar', 
        name='esocial_desligamentos_motivos_apagar'),

url(r'^esocial-desligamentos-motivos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_desligamentos_motivos.listar', 
        name='esocial_desligamentos_motivos'),
        
        
    url(r'^esocial-desligamentos-motivos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_desligamentos_motivos.json_search', name='esocial_desligamentos_motivos_json_search'),

url(r'^esocial-desligamentos-motivos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_desligamentos_motivos.salvar', 
        name='esocial_desligamentos_motivos_salvar'),



url(r'^esocial-logradouros-tipos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_logradouros_tipos.apagar', 
        name='esocial_logradouros_tipos_apagar'),

url(r'^esocial-logradouros-tipos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_logradouros_tipos.listar', 
        name='esocial_logradouros_tipos'),
        
        
    url(r'^esocial-logradouros-tipos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_logradouros_tipos.json_search', name='esocial_logradouros_tipos_json_search'),

url(r'^esocial-logradouros-tipos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_logradouros_tipos.salvar', 
        name='esocial_logradouros_tipos_salvar'),



url(r'^esocial-naturezas-juridicas/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_naturezas_juridicas.apagar', 
        name='esocial_naturezas_juridicas_apagar'),

url(r'^esocial-naturezas-juridicas/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_naturezas_juridicas.listar', 
        name='esocial_naturezas_juridicas'),
        
        
    url(r'^esocial-naturezas-juridicas/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_naturezas_juridicas.json_search', name='esocial_naturezas_juridicas_json_search'),

url(r'^esocial-naturezas-juridicas/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_naturezas_juridicas.salvar', 
        name='esocial_naturezas_juridicas_salvar'),



url(r'^esocial-compatibilidades-fpas-classificacoes-tributarias/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_compatibilidades_fpas_classificacoes_tributarias.apagar', 
        name='esocial_compatibilidades_fpas_classificacoes_tributarias_apagar'),

url(r'^esocial-compatibilidades-fpas-classificacoes-tributarias/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_compatibilidades_fpas_classificacoes_tributarias.listar', 
        name='esocial_compatibilidades_fpas_classificacoes_tributarias'),
        
        
    url(r'^esocial-compatibilidades-fpas-classificacoes-tributarias/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_compatibilidades_fpas_classificacoes_tributarias.json_search', name='esocial_compatibilidades_fpas_classificacoes_tributarias_json_search'),

url(r'^esocial-compatibilidades-fpas-classificacoes-tributarias/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_compatibilidades_fpas_classificacoes_tributarias.salvar', 
        name='esocial_compatibilidades_fpas_classificacoes_tributarias_salvar'),



url(r'^esocial-fatores-risco/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_fatores_risco.apagar', 
        name='esocial_fatores_risco_apagar'),

url(r'^esocial-fatores-risco/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_fatores_risco.listar', 
        name='esocial_fatores_risco'),
        
        
    url(r'^esocial-fatores-risco/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_fatores_risco.json_search', name='esocial_fatores_risco_json_search'),

url(r'^esocial-fatores-risco/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_fatores_risco.salvar', 
        name='esocial_fatores_risco_salvar'),



url(r'^esocial-codificacoes-acidente-trabalho/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_codificacoes_acidente_trabalho.apagar', 
        name='esocial_codificacoes_acidente_trabalho_apagar'),

url(r'^esocial-codificacoes-acidente-trabalho/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_codificacoes_acidente_trabalho.listar', 
        name='esocial_codificacoes_acidente_trabalho'),
        
        
    url(r'^esocial-codificacoes-acidente-trabalho/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_codificacoes_acidente_trabalho.json_search', name='esocial_codificacoes_acidente_trabalho_json_search'),

url(r'^esocial-codificacoes-acidente-trabalho/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_codificacoes_acidente_trabalho.salvar', 
        name='esocial_codificacoes_acidente_trabalho_salvar'),



url(r'^esocial-beneficios-previdenciarios-tipos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_beneficios_previdenciarios_tipos.apagar', 
        name='esocial_beneficios_previdenciarios_tipos_apagar'),

url(r'^esocial-beneficios-previdenciarios-tipos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_beneficios_previdenciarios_tipos.listar', 
        name='esocial_beneficios_previdenciarios_tipos'),
        
        
    url(r'^esocial-beneficios-previdenciarios-tipos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_beneficios_previdenciarios_tipos.json_search', name='esocial_beneficios_previdenciarios_tipos_json_search'),

url(r'^esocial-beneficios-previdenciarios-tipos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_beneficios_previdenciarios_tipos.salvar', 
        name='esocial_beneficios_previdenciarios_tipos_salvar'),



url(r'^esocial-beneficios-previdenciarios-cessacao-motivos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_beneficios_previdenciarios_cessacao_motivos.apagar', 
        name='esocial_beneficios_previdenciarios_cessacao_motivos_apagar'),

url(r'^esocial-beneficios-previdenciarios-cessacao-motivos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_beneficios_previdenciarios_cessacao_motivos.listar', 
        name='esocial_beneficios_previdenciarios_cessacao_motivos'),
        
        
    url(r'^esocial-beneficios-previdenciarios-cessacao-motivos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_beneficios_previdenciarios_cessacao_motivos.json_search', name='esocial_beneficios_previdenciarios_cessacao_motivos_json_search'),

url(r'^esocial-beneficios-previdenciarios-cessacao-motivos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_beneficios_previdenciarios_cessacao_motivos.salvar', 
        name='esocial_beneficios_previdenciarios_cessacao_motivos_salvar'),

)


urlpatterns += patterns('',


url(r'^esocial-procedimentos-diagnosticos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_procedimentos_diagnosticos.apagar', 
        name='esocial_procedimentos_diagnosticos_apagar'),

url(r'^esocial-procedimentos-diagnosticos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_procedimentos_diagnosticos.listar', 
        name='esocial_procedimentos_diagnosticos'),
        
        
    url(r'^esocial-procedimentos-diagnosticos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_procedimentos_diagnosticos.json_search', name='esocial_procedimentos_diagnosticos_json_search'),

url(r'^esocial-procedimentos-diagnosticos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_procedimentos_diagnosticos.salvar', 
        name='esocial_procedimentos_diagnosticos_salvar'),



url(r'^esocial-atividades-periculosas-insalubres-especiais/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_atividades_periculosas_insalubres_especiais.apagar', 
        name='esocial_atividades_periculosas_insalubres_especiais_apagar'),

url(r'^esocial-atividades-periculosas-insalubres-especiais/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_atividades_periculosas_insalubres_especiais.listar', 
        name='esocial_atividades_periculosas_insalubres_especiais'),
        
        
    url(r'^esocial-atividades-periculosas-insalubres-especiais/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_atividades_periculosas_insalubres_especiais.json_search', name='esocial_atividades_periculosas_insalubres_especiais_json_search'),

url(r'^esocial-atividades-periculosas-insalubres-especiais/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_atividades_periculosas_insalubres_especiais.salvar', 
        name='esocial_atividades_periculosas_insalubres_especiais_salvar'),



url(r'^esocial-treinamentos-capacitacoes-exercicios-simulados/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_treinamentos_capacitacoes_exercicios_simulados.apagar', 
        name='esocial_treinamentos_capacitacoes_exercicios_simulados_apagar'),

url(r'^esocial-treinamentos-capacitacoes-exercicios-simulados/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_treinamentos_capacitacoes_exercicios_simulados.listar', 
        name='esocial_treinamentos_capacitacoes_exercicios_simulados'),
        
        
    url(r'^esocial-treinamentos-capacitacoes-exercicios-simulados/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_treinamentos_capacitacoes_exercicios_simulados.json_search', name='esocial_treinamentos_capacitacoes_exercicios_simulados_json_search'),

url(r'^esocial-treinamentos-capacitacoes-exercicios-simulados/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_treinamentos_capacitacoes_exercicios_simulados.salvar', 
        name='esocial_treinamentos_capacitacoes_exercicios_simulados_salvar'),



url(r'^esocial-programas-planos-documentos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_programas_planos_documentos.apagar', 
        name='esocial_programas_planos_documentos_apagar'),

url(r'^esocial-programas-planos-documentos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_programas_planos_documentos.listar', 
        name='esocial_programas_planos_documentos'),
        
        
    url(r'^esocial-programas-planos-documentos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.esocial_programas_planos_documentos.json_search', name='esocial_programas_planos_documentos_json_search'),

url(r'^esocial-programas-planos-documentos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.esocial_programas_planos_documentos.salvar', 
        name='esocial_programas_planos_documentos_salvar'),



url(r'^efdreinf-pagamentos-codigos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_pagamentos_codigos.apagar', 
        name='efdreinf_pagamentos_codigos_apagar'),

url(r'^efdreinf-pagamentos-codigos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_pagamentos_codigos.listar', 
        name='efdreinf_pagamentos_codigos'),
        
        
    url(r'^efdreinf-pagamentos-codigos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.efdreinf_pagamentos_codigos.json_search', name='efdreinf_pagamentos_codigos_json_search'),

url(r'^efdreinf-pagamentos-codigos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_pagamentos_codigos.salvar', 
        name='efdreinf_pagamentos_codigos_salvar'),



url(r'^efdreinf-regras-pagamentos-codigos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_regras_pagamentos_codigos.apagar', 
        name='efdreinf_regras_pagamentos_codigos_apagar'),

url(r'^efdreinf-regras-pagamentos-codigos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_regras_pagamentos_codigos.listar', 
        name='efdreinf_regras_pagamentos_codigos'),
        
        
    url(r'^efdreinf-regras-pagamentos-codigos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.efdreinf_regras_pagamentos_codigos.json_search', name='efdreinf_regras_pagamentos_codigos_json_search'),

url(r'^efdreinf-regras-pagamentos-codigos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_regras_pagamentos_codigos.salvar', 
        name='efdreinf_regras_pagamentos_codigos_salvar'),



url(r'^efdreinf-rendimentos-beneficiarios-exterior/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_rendimentos_beneficiarios_exterior.apagar', 
        name='efdreinf_rendimentos_beneficiarios_exterior_apagar'),

url(r'^efdreinf-rendimentos-beneficiarios-exterior/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_rendimentos_beneficiarios_exterior.listar', 
        name='efdreinf_rendimentos_beneficiarios_exterior'),
        
        
    url(r'^efdreinf-rendimentos-beneficiarios-exterior/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.efdreinf_rendimentos_beneficiarios_exterior.json_search', name='efdreinf_rendimentos_beneficiarios_exterior_json_search'),

url(r'^efdreinf-rendimentos-beneficiarios-exterior/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_rendimentos_beneficiarios_exterior.salvar', 
        name='efdreinf_rendimentos_beneficiarios_exterior_salvar'),



url(r'^efdreinf-rendimentos-beneficiarios-exterior-tributacao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_rendimentos_beneficiarios_exterior_tributacao.apagar', 
        name='efdreinf_rendimentos_beneficiarios_exterior_tributacao_apagar'),

url(r'^efdreinf-rendimentos-beneficiarios-exterior-tributacao/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_rendimentos_beneficiarios_exterior_tributacao.listar', 
        name='efdreinf_rendimentos_beneficiarios_exterior_tributacao'),
        
        
    url(r'^efdreinf-rendimentos-beneficiarios-exterior-tributacao/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.efdreinf_rendimentos_beneficiarios_exterior_tributacao.json_search', name='efdreinf_rendimentos_beneficiarios_exterior_tributacao_json_search'),

url(r'^efdreinf-rendimentos-beneficiarios-exterior-tributacao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_rendimentos_beneficiarios_exterior_tributacao.salvar', 
        name='efdreinf_rendimentos_beneficiarios_exterior_tributacao_salvar'),



url(r'^efdreinf-informacoes-beneficiarios-exterior/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_informacoes_beneficiarios_exterior.apagar', 
        name='efdreinf_informacoes_beneficiarios_exterior_apagar'),

url(r'^efdreinf-informacoes-beneficiarios-exterior/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_informacoes_beneficiarios_exterior.listar', 
        name='efdreinf_informacoes_beneficiarios_exterior'),
        
        
    url(r'^efdreinf-informacoes-beneficiarios-exterior/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.efdreinf_informacoes_beneficiarios_exterior.json_search', name='efdreinf_informacoes_beneficiarios_exterior_json_search'),

url(r'^efdreinf-informacoes-beneficiarios-exterior/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_informacoes_beneficiarios_exterior.salvar', 
        name='efdreinf_informacoes_beneficiarios_exterior_salvar'),



url(r'^efdreinf-classificacao-servicos-prestados/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_classificacao_servicos_prestados.apagar', 
        name='efdreinf_classificacao_servicos_prestados_apagar'),

url(r'^efdreinf-classificacao-servicos-prestados/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_classificacao_servicos_prestados.listar', 
        name='efdreinf_classificacao_servicos_prestados'),
        
        
    url(r'^efdreinf-classificacao-servicos-prestados/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.efdreinf_classificacao_servicos_prestados.json_search', name='efdreinf_classificacao_servicos_prestados_json_search'),

url(r'^efdreinf-classificacao-servicos-prestados/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_classificacao_servicos_prestados.salvar', 
        name='efdreinf_classificacao_servicos_prestados_salvar'),

)


urlpatterns += patterns('',


url(r'^efdreinf-paises/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_paises.apagar', 
        name='efdreinf_paises_apagar'),

url(r'^efdreinf-paises/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_paises.listar', 
        name='efdreinf_paises'),
        
        
    url(r'^efdreinf-paises/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.efdreinf_paises.json_search', name='efdreinf_paises_json_search'),

url(r'^efdreinf-paises/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_paises.salvar', 
        name='efdreinf_paises_salvar'),



url(r'^efdreinf-classificacao-tributaria/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_classificacao_tributaria.apagar', 
        name='efdreinf_classificacao_tributaria_apagar'),

url(r'^efdreinf-classificacao-tributaria/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_classificacao_tributaria.listar', 
        name='efdreinf_classificacao_tributaria'),
        
        
    url(r'^efdreinf-classificacao-tributaria/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.efdreinf_classificacao_tributaria.json_search', name='efdreinf_classificacao_tributaria_json_search'),

url(r'^efdreinf-classificacao-tributaria/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_classificacao_tributaria.salvar', 
        name='efdreinf_classificacao_tributaria_salvar'),



url(r'^efdreinf-codigos-atividades-produtos-servicos-cprb/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_codigos_atividades_produtos_servicos_cprb.apagar', 
        name='efdreinf_codigos_atividades_produtos_servicos_cprb_apagar'),

url(r'^efdreinf-codigos-atividades-produtos-servicos-cprb/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_codigos_atividades_produtos_servicos_cprb.listar', 
        name='efdreinf_codigos_atividades_produtos_servicos_cprb'),
        
        
    url(r'^efdreinf-codigos-atividades-produtos-servicos-cprb/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.efdreinf_codigos_atividades_produtos_servicos_cprb.json_search', name='efdreinf_codigos_atividades_produtos_servicos_cprb_json_search'),

url(r'^efdreinf-codigos-atividades-produtos-servicos-cprb/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_codigos_atividades_produtos_servicos_cprb.salvar', 
        name='efdreinf_codigos_atividades_produtos_servicos_cprb_salvar'),



url(r'^efdreinf-eventos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_eventos.apagar', 
        name='efdreinf_eventos_apagar'),

url(r'^efdreinf-eventos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_eventos.listar', 
        name='efdreinf_eventos'),
        
        
    url(r'^efdreinf-eventos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.efdreinf_eventos.json_search', name='efdreinf_eventos_json_search'),

url(r'^efdreinf-eventos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.efdreinf_eventos.salvar', 
        name='efdreinf_eventos_salvar'),





)