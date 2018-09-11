#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



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



url(r'^trabalhadores-categorias/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.trabalhadores_categorias.apagar', 
        name='trabalhadores_categorias_apagar'),

url(r'^trabalhadores-categorias/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.trabalhadores_categorias.listar', 
        name='trabalhadores_categorias'),
        
        
    url(r'^trabalhadores-categorias/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.trabalhadores_categorias.json_search', name='trabalhadores_categorias_json_search'),

url(r'^trabalhadores-categorias/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.trabalhadores_categorias.salvar', 
        name='trabalhadores_categorias_salvar'),



url(r'^financiamentos-aposentadorias-especiais/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.financiamentos_aposentadorias_especiais.apagar', 
        name='financiamentos_aposentadorias_especiais_apagar'),

url(r'^financiamentos-aposentadorias-especiais/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.financiamentos_aposentadorias_especiais.listar', 
        name='financiamentos_aposentadorias_especiais'),
        
        
    url(r'^financiamentos-aposentadorias-especiais/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.financiamentos_aposentadorias_especiais.json_search', name='financiamentos_aposentadorias_especiais_json_search'),

url(r'^financiamentos-aposentadorias-especiais/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.financiamentos_aposentadorias_especiais.salvar', 
        name='financiamentos_aposentadorias_especiais_salvar'),



url(r'^naturezas-rubricas/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.naturezas_rubricas.apagar', 
        name='naturezas_rubricas_apagar'),

url(r'^naturezas-rubricas/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.naturezas_rubricas.listar', 
        name='naturezas_rubricas'),
        
        
    url(r'^naturezas-rubricas/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.naturezas_rubricas.json_search', name='naturezas_rubricas_json_search'),

url(r'^naturezas-rubricas/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.naturezas_rubricas.salvar', 
        name='naturezas_rubricas_salvar'),



url(r'^codigo-aliquotas-fpas-terceiros/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.codigo_aliquotas_fpas_terceiros.apagar', 
        name='codigo_aliquotas_fpas_terceiros_apagar'),

url(r'^codigo-aliquotas-fpas-terceiros/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.codigo_aliquotas_fpas_terceiros.listar', 
        name='codigo_aliquotas_fpas_terceiros'),
        
        
    url(r'^codigo-aliquotas-fpas-terceiros/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.codigo_aliquotas_fpas_terceiros.json_search', name='codigo_aliquotas_fpas_terceiros_json_search'),

url(r'^codigo-aliquotas-fpas-terceiros/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.codigo_aliquotas_fpas_terceiros.salvar', 
        name='codigo_aliquotas_fpas_terceiros_salvar'),



url(r'^inscricoes-tipos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.inscricoes_tipos.apagar', 
        name='inscricoes_tipos_apagar'),

url(r'^inscricoes-tipos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.inscricoes_tipos.listar', 
        name='inscricoes_tipos'),
        
        
    url(r'^inscricoes-tipos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.inscricoes_tipos.json_search', name='inscricoes_tipos_json_search'),

url(r'^inscricoes-tipos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.inscricoes_tipos.salvar', 
        name='inscricoes_tipos_salvar'),



url(r'^paises/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.paises.apagar', 
        name='paises_apagar'),

url(r'^paises/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.paises.listar', 
        name='paises'),
        
        
    url(r'^paises/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.paises.json_search', name='paises_json_search'),

url(r'^paises/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.paises.salvar', 
        name='paises_salvar'),

)


urlpatterns += patterns('',


url(r'^dependentes-tipos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.dependentes_tipos.apagar', 
        name='dependentes_tipos_apagar'),

url(r'^dependentes-tipos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.dependentes_tipos.listar', 
        name='dependentes_tipos'),
        
        
    url(r'^dependentes-tipos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.dependentes_tipos.json_search', name='dependentes_tipos_json_search'),

url(r'^dependentes-tipos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.dependentes_tipos.salvar', 
        name='dependentes_tipos_salvar'),



url(r'^classificacoes-tributarias/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.classificacoes_tributarias.apagar', 
        name='classificacoes_tributarias_apagar'),

url(r'^classificacoes-tributarias/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.classificacoes_tributarias.listar', 
        name='classificacoes_tributarias'),
        
        
    url(r'^classificacoes-tributarias/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.classificacoes_tributarias.json_search', name='classificacoes_tributarias_json_search'),

url(r'^classificacoes-tributarias/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.classificacoes_tributarias.salvar', 
        name='classificacoes_tributarias_salvar'),



url(r'^arquivos-esocial-tipos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.arquivos_esocial_tipos.apagar', 
        name='arquivos_esocial_tipos_apagar'),

url(r'^arquivos-esocial-tipos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.arquivos_esocial_tipos.listar', 
        name='arquivos_esocial_tipos'),
        
        
    url(r'^arquivos-esocial-tipos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.arquivos_esocial_tipos.json_search', name='arquivos_esocial_tipos_json_search'),

url(r'^arquivos-esocial-tipos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.arquivos_esocial_tipos.salvar', 
        name='arquivos_esocial_tipos_salvar'),



url(r'^lotacoes-tributarias-tipos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.lotacoes_tributarias_tipos.apagar', 
        name='lotacoes_tributarias_tipos_apagar'),

url(r'^lotacoes-tributarias-tipos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.lotacoes_tributarias_tipos.listar', 
        name='lotacoes_tributarias_tipos'),
        
        
    url(r'^lotacoes-tributarias-tipos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.lotacoes_tributarias_tipos.json_search', name='lotacoes_tributarias_tipos_json_search'),

url(r'^lotacoes-tributarias-tipos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.lotacoes_tributarias_tipos.salvar', 
        name='lotacoes_tributarias_tipos_salvar'),



url(r'^compatibilidades-categorias-classificacoes-lotacoes/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.compatibilidades_categorias_classificacoes_lotacoes.apagar', 
        name='compatibilidades_categorias_classificacoes_lotacoes_apagar'),

url(r'^compatibilidades-categorias-classificacoes-lotacoes/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.compatibilidades_categorias_classificacoes_lotacoes.listar', 
        name='compatibilidades_categorias_classificacoes_lotacoes'),
        
        
    url(r'^compatibilidades-categorias-classificacoes-lotacoes/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.compatibilidades_categorias_classificacoes_lotacoes.json_search', name='compatibilidades_categorias_classificacoes_lotacoes_json_search'),

url(r'^compatibilidades-categorias-classificacoes-lotacoes/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.compatibilidades_categorias_classificacoes_lotacoes.salvar', 
        name='compatibilidades_categorias_classificacoes_lotacoes_salvar'),



url(r'^compatibilidades-lotacoes-classificacoes/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.compatibilidades_lotacoes_classificacoes.apagar', 
        name='compatibilidades_lotacoes_classificacoes_apagar'),

url(r'^compatibilidades-lotacoes-classificacoes/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.compatibilidades_lotacoes_classificacoes.listar', 
        name='compatibilidades_lotacoes_classificacoes'),
        
        
    url(r'^compatibilidades-lotacoes-classificacoes/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.compatibilidades_lotacoes_classificacoes.json_search', name='compatibilidades_lotacoes_classificacoes_json_search'),

url(r'^compatibilidades-lotacoes-classificacoes/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.compatibilidades_lotacoes_classificacoes.salvar', 
        name='compatibilidades_lotacoes_classificacoes_salvar'),



url(r'^partes-corpo-atingidas/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.partes_corpo_atingidas.apagar', 
        name='partes_corpo_atingidas_apagar'),

url(r'^partes-corpo-atingidas/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.partes_corpo_atingidas.listar', 
        name='partes_corpo_atingidas'),
        
        
    url(r'^partes-corpo-atingidas/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.partes_corpo_atingidas.json_search', name='partes_corpo_atingidas_json_search'),

url(r'^partes-corpo-atingidas/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.partes_corpo_atingidas.salvar', 
        name='partes_corpo_atingidas_salvar'),



url(r'^agentes-causadores-acidentes-trabalho/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.agentes_causadores_acidentes_trabalho.apagar', 
        name='agentes_causadores_acidentes_trabalho_apagar'),

url(r'^agentes-causadores-acidentes-trabalho/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.agentes_causadores_acidentes_trabalho.listar', 
        name='agentes_causadores_acidentes_trabalho'),
        
        
    url(r'^agentes-causadores-acidentes-trabalho/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.agentes_causadores_acidentes_trabalho.json_search', name='agentes_causadores_acidentes_trabalho_json_search'),

url(r'^agentes-causadores-acidentes-trabalho/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.agentes_causadores_acidentes_trabalho.salvar', 
        name='agentes_causadores_acidentes_trabalho_salvar'),



url(r'^agentes-causadores-doencas-profissionais/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.agentes_causadores_doencas_profissionais.apagar', 
        name='agentes_causadores_doencas_profissionais_apagar'),

url(r'^agentes-causadores-doencas-profissionais/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.agentes_causadores_doencas_profissionais.listar', 
        name='agentes_causadores_doencas_profissionais'),
        
        
    url(r'^agentes-causadores-doencas-profissionais/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.agentes_causadores_doencas_profissionais.json_search', name='agentes_causadores_doencas_profissionais_json_search'),

url(r'^agentes-causadores-doencas-profissionais/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.agentes_causadores_doencas_profissionais.salvar', 
        name='agentes_causadores_doencas_profissionais_salvar'),



url(r'^acidentes-situacoes-geradoras/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.acidentes_situacoes_geradoras.apagar', 
        name='acidentes_situacoes_geradoras_apagar'),

url(r'^acidentes-situacoes-geradoras/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.acidentes_situacoes_geradoras.listar', 
        name='acidentes_situacoes_geradoras'),
        
        
    url(r'^acidentes-situacoes-geradoras/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.acidentes_situacoes_geradoras.json_search', name='acidentes_situacoes_geradoras_json_search'),

url(r'^acidentes-situacoes-geradoras/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.acidentes_situacoes_geradoras.salvar', 
        name='acidentes_situacoes_geradoras_salvar'),

)


urlpatterns += patterns('',


url(r'^naturezas-lesoes/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.naturezas_lesoes.apagar', 
        name='naturezas_lesoes_apagar'),

url(r'^naturezas-lesoes/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.naturezas_lesoes.listar', 
        name='naturezas_lesoes'),
        
        
    url(r'^naturezas-lesoes/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.naturezas_lesoes.json_search', name='naturezas_lesoes_json_search'),

url(r'^naturezas-lesoes/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.naturezas_lesoes.salvar', 
        name='naturezas_lesoes_salvar'),



url(r'^afastamentos-motivos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.afastamentos_motivos.apagar', 
        name='afastamentos_motivos_apagar'),

url(r'^afastamentos-motivos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.afastamentos_motivos.listar', 
        name='afastamentos_motivos'),
        
        
    url(r'^afastamentos-motivos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.afastamentos_motivos.json_search', name='afastamentos_motivos_json_search'),

url(r'^afastamentos-motivos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.afastamentos_motivos.salvar', 
        name='afastamentos_motivos_salvar'),



url(r'^desligamentos-motivos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.desligamentos_motivos.apagar', 
        name='desligamentos_motivos_apagar'),

url(r'^desligamentos-motivos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.desligamentos_motivos.listar', 
        name='desligamentos_motivos'),
        
        
    url(r'^desligamentos-motivos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.desligamentos_motivos.json_search', name='desligamentos_motivos_json_search'),

url(r'^desligamentos-motivos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.desligamentos_motivos.salvar', 
        name='desligamentos_motivos_salvar'),



url(r'^logradouros-tipos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.logradouros_tipos.apagar', 
        name='logradouros_tipos_apagar'),

url(r'^logradouros-tipos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.logradouros_tipos.listar', 
        name='logradouros_tipos'),
        
        
    url(r'^logradouros-tipos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.logradouros_tipos.json_search', name='logradouros_tipos_json_search'),

url(r'^logradouros-tipos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.logradouros_tipos.salvar', 
        name='logradouros_tipos_salvar'),



url(r'^naturezas-juridicas/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.naturezas_juridicas.apagar', 
        name='naturezas_juridicas_apagar'),

url(r'^naturezas-juridicas/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.naturezas_juridicas.listar', 
        name='naturezas_juridicas'),
        
        
    url(r'^naturezas-juridicas/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.naturezas_juridicas.json_search', name='naturezas_juridicas_json_search'),

url(r'^naturezas-juridicas/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.naturezas_juridicas.salvar', 
        name='naturezas_juridicas_salvar'),



url(r'^compatibilidades-fpas-classificacoes-tributarias/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.compatibilidades_fpas_classificacoes_tributarias.apagar', 
        name='compatibilidades_fpas_classificacoes_tributarias_apagar'),

url(r'^compatibilidades-fpas-classificacoes-tributarias/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.compatibilidades_fpas_classificacoes_tributarias.listar', 
        name='compatibilidades_fpas_classificacoes_tributarias'),
        
        
    url(r'^compatibilidades-fpas-classificacoes-tributarias/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.compatibilidades_fpas_classificacoes_tributarias.json_search', name='compatibilidades_fpas_classificacoes_tributarias_json_search'),

url(r'^compatibilidades-fpas-classificacoes-tributarias/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.compatibilidades_fpas_classificacoes_tributarias.salvar', 
        name='compatibilidades_fpas_classificacoes_tributarias_salvar'),



url(r'^fatores-risco/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.fatores_risco.apagar', 
        name='fatores_risco_apagar'),

url(r'^fatores-risco/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.fatores_risco.listar', 
        name='fatores_risco'),
        
        
    url(r'^fatores-risco/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.fatores_risco.json_search', name='fatores_risco_json_search'),

url(r'^fatores-risco/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.fatores_risco.salvar', 
        name='fatores_risco_salvar'),



url(r'^codificacoes-acidente-trabalho/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.codificacoes_acidente_trabalho.apagar', 
        name='codificacoes_acidente_trabalho_apagar'),

url(r'^codificacoes-acidente-trabalho/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.codificacoes_acidente_trabalho.listar', 
        name='codificacoes_acidente_trabalho'),
        
        
    url(r'^codificacoes-acidente-trabalho/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.codificacoes_acidente_trabalho.json_search', name='codificacoes_acidente_trabalho_json_search'),

url(r'^codificacoes-acidente-trabalho/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.codificacoes_acidente_trabalho.salvar', 
        name='codificacoes_acidente_trabalho_salvar'),



url(r'^beneficios-previdenciarios-tipos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.beneficios_previdenciarios_tipos.apagar', 
        name='beneficios_previdenciarios_tipos_apagar'),

url(r'^beneficios-previdenciarios-tipos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.beneficios_previdenciarios_tipos.listar', 
        name='beneficios_previdenciarios_tipos'),
        
        
    url(r'^beneficios-previdenciarios-tipos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.beneficios_previdenciarios_tipos.json_search', name='beneficios_previdenciarios_tipos_json_search'),

url(r'^beneficios-previdenciarios-tipos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.beneficios_previdenciarios_tipos.salvar', 
        name='beneficios_previdenciarios_tipos_salvar'),



url(r'^beneficios-previdenciarios-cessacao-motivos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.beneficios_previdenciarios_cessacao_motivos.apagar', 
        name='beneficios_previdenciarios_cessacao_motivos_apagar'),

url(r'^beneficios-previdenciarios-cessacao-motivos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.beneficios_previdenciarios_cessacao_motivos.listar', 
        name='beneficios_previdenciarios_cessacao_motivos'),
        
        
    url(r'^beneficios-previdenciarios-cessacao-motivos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.beneficios_previdenciarios_cessacao_motivos.json_search', name='beneficios_previdenciarios_cessacao_motivos_json_search'),

url(r'^beneficios-previdenciarios-cessacao-motivos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.beneficios_previdenciarios_cessacao_motivos.salvar', 
        name='beneficios_previdenciarios_cessacao_motivos_salvar'),

)


urlpatterns += patterns('',


url(r'^procedimentos-diagnosticos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.procedimentos_diagnosticos.apagar', 
        name='procedimentos_diagnosticos_apagar'),

url(r'^procedimentos-diagnosticos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.procedimentos_diagnosticos.listar', 
        name='procedimentos_diagnosticos'),
        
        
    url(r'^procedimentos-diagnosticos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.procedimentos_diagnosticos.json_search', name='procedimentos_diagnosticos_json_search'),

url(r'^procedimentos-diagnosticos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.procedimentos_diagnosticos.salvar', 
        name='procedimentos_diagnosticos_salvar'),



url(r'^atividades-periculosas-insalubres-especiais/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.atividades_periculosas_insalubres_especiais.apagar', 
        name='atividades_periculosas_insalubres_especiais_apagar'),

url(r'^atividades-periculosas-insalubres-especiais/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.atividades_periculosas_insalubres_especiais.listar', 
        name='atividades_periculosas_insalubres_especiais'),
        
        
    url(r'^atividades-periculosas-insalubres-especiais/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.atividades_periculosas_insalubres_especiais.json_search', name='atividades_periculosas_insalubres_especiais_json_search'),

url(r'^atividades-periculosas-insalubres-especiais/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.atividades_periculosas_insalubres_especiais.salvar', 
        name='atividades_periculosas_insalubres_especiais_salvar'),



url(r'^treinamentos-capacitacoes-exercicios-simulados/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.treinamentos_capacitacoes_exercicios_simulados.apagar', 
        name='treinamentos_capacitacoes_exercicios_simulados_apagar'),

url(r'^treinamentos-capacitacoes-exercicios-simulados/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.treinamentos_capacitacoes_exercicios_simulados.listar', 
        name='treinamentos_capacitacoes_exercicios_simulados'),
        
        
    url(r'^treinamentos-capacitacoes-exercicios-simulados/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.treinamentos_capacitacoes_exercicios_simulados.json_search', name='treinamentos_capacitacoes_exercicios_simulados_json_search'),

url(r'^treinamentos-capacitacoes-exercicios-simulados/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.treinamentos_capacitacoes_exercicios_simulados.salvar', 
        name='treinamentos_capacitacoes_exercicios_simulados_salvar'),



url(r'^programas-planos-documentos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.programas_planos_documentos.apagar', 
        name='programas_planos_documentos_apagar'),

url(r'^programas-planos-documentos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.programas_planos_documentos.listar', 
        name='programas_planos_documentos'),
        
        
    url(r'^programas-planos-documentos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.programas_planos_documentos.json_search', name='programas_planos_documentos_json_search'),

url(r'^programas-planos-documentos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.programas_planos_documentos.salvar', 
        name='programas_planos_documentos_salvar'),



url(r'^pagamentos-codigos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.pagamentos_codigos.apagar', 
        name='pagamentos_codigos_apagar'),

url(r'^pagamentos-codigos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.pagamentos_codigos.listar', 
        name='pagamentos_codigos'),
        
        
    url(r'^pagamentos-codigos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.pagamentos_codigos.json_search', name='pagamentos_codigos_json_search'),

url(r'^pagamentos-codigos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.pagamentos_codigos.salvar', 
        name='pagamentos_codigos_salvar'),



url(r'^regras-pagamentos-codigos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.regras_pagamentos_codigos.apagar', 
        name='regras_pagamentos_codigos_apagar'),

url(r'^regras-pagamentos-codigos/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.regras_pagamentos_codigos.listar', 
        name='regras_pagamentos_codigos'),
        
        
    url(r'^regras-pagamentos-codigos/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.regras_pagamentos_codigos.json_search', name='regras_pagamentos_codigos_json_search'),

url(r'^regras-pagamentos-codigos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.regras_pagamentos_codigos.salvar', 
        name='regras_pagamentos_codigos_salvar'),



url(r'^rendimentos-beneficiarios-exterior/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.rendimentos_beneficiarios_exterior.apagar', 
        name='rendimentos_beneficiarios_exterior_apagar'),

url(r'^rendimentos-beneficiarios-exterior/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.rendimentos_beneficiarios_exterior.listar', 
        name='rendimentos_beneficiarios_exterior'),
        
        
    url(r'^rendimentos-beneficiarios-exterior/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.rendimentos_beneficiarios_exterior.json_search', name='rendimentos_beneficiarios_exterior_json_search'),

url(r'^rendimentos-beneficiarios-exterior/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.rendimentos_beneficiarios_exterior.salvar', 
        name='rendimentos_beneficiarios_exterior_salvar'),



url(r'^rendimentos-beneficiarios-exterior-tributacao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.rendimentos_beneficiarios_exterior_tributacao.apagar', 
        name='rendimentos_beneficiarios_exterior_tributacao_apagar'),

url(r'^rendimentos-beneficiarios-exterior-tributacao/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.rendimentos_beneficiarios_exterior_tributacao.listar', 
        name='rendimentos_beneficiarios_exterior_tributacao'),
        
        
    url(r'^rendimentos-beneficiarios-exterior-tributacao/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.rendimentos_beneficiarios_exterior_tributacao.json_search', name='rendimentos_beneficiarios_exterior_tributacao_json_search'),

url(r'^rendimentos-beneficiarios-exterior-tributacao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.rendimentos_beneficiarios_exterior_tributacao.salvar', 
        name='rendimentos_beneficiarios_exterior_tributacao_salvar'),



url(r'^informacoes-beneficiarios-exterior/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.informacoes_beneficiarios_exterior.apagar', 
        name='informacoes_beneficiarios_exterior_apagar'),

url(r'^informacoes-beneficiarios-exterior/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.informacoes_beneficiarios_exterior.listar', 
        name='informacoes_beneficiarios_exterior'),
        
        
    url(r'^informacoes-beneficiarios-exterior/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.informacoes_beneficiarios_exterior.json_search', name='informacoes_beneficiarios_exterior_json_search'),

url(r'^informacoes-beneficiarios-exterior/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.informacoes_beneficiarios_exterior.salvar', 
        name='informacoes_beneficiarios_exterior_salvar'),



url(r'^classificacao-servicos-prestados/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.classificacao_servicos_prestados.apagar', 
        name='classificacao_servicos_prestados_apagar'),

url(r'^classificacao-servicos-prestados/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.classificacao_servicos_prestados.listar', 
        name='classificacao_servicos_prestados'),
        
        
    url(r'^classificacao-servicos-prestados/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.classificacao_servicos_prestados.json_search', name='classificacao_servicos_prestados_json_search'),

url(r'^classificacao-servicos-prestados/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.classificacao_servicos_prestados.salvar', 
        name='classificacao_servicos_prestados_salvar'),

)


urlpatterns += patterns('',


url(r'^paises/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.paises.apagar', 
        name='paises_apagar'),

url(r'^paises/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.paises.listar', 
        name='paises'),
        
        
    url(r'^paises/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.paises.json_search', name='paises_json_search'),

url(r'^paises/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.paises.salvar', 
        name='paises_salvar'),



url(r'^classificacao-tributaria/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.classificacao_tributaria.apagar', 
        name='classificacao_tributaria_apagar'),

url(r'^classificacao-tributaria/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.classificacao_tributaria.listar', 
        name='classificacao_tributaria'),
        
        
    url(r'^classificacao-tributaria/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.classificacao_tributaria.json_search', name='classificacao_tributaria_json_search'),

url(r'^classificacao-tributaria/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.classificacao_tributaria.salvar', 
        name='classificacao_tributaria_salvar'),



url(r'^codigos-atividades-produtos-servicos-cprb/apagar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.codigos_atividades_produtos_servicos_cprb.apagar', 
        name='codigos_atividades_produtos_servicos_cprb_apagar'),

url(r'^codigos-atividades-produtos-servicos-cprb/listar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.codigos_atividades_produtos_servicos_cprb.listar', 
        name='codigos_atividades_produtos_servicos_cprb'),
        
        
    url(r'^codigos-atividades-produtos-servicos-cprb/json-search/(?P<search>[\w ]+)/$', 
    'emensageriapro.tabelas.views.codigos_atividades_produtos_servicos_cprb.json_search', name='codigos_atividades_produtos_servicos_cprb_json_search'),

url(r'^codigos-atividades-produtos-servicos-cprb/salvar/(?P<hash>.*)/$', 
        'emensageriapro.tabelas.views.codigos_atividades_produtos_servicos_cprb.salvar', 
        name='codigos_atividades_produtos_servicos_cprb_salvar'),



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