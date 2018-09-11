#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1030-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_inclusao.apagar', 
        name='s1030_inclusao_apagar'),

url(r'^s1030-inclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_inclusao.listar', 
        name='s1030_inclusao'),

url(r'^s1030-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_inclusao.salvar', 
        name='s1030_inclusao_salvar'),



url(r'^s1030-inclusao-cargopublico/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_inclusao_cargopublico.apagar', 
        name='s1030_inclusao_cargopublico_apagar'),

url(r'^s1030-inclusao-cargopublico/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_inclusao_cargopublico.listar', 
        name='s1030_inclusao_cargopublico'),

url(r'^s1030-inclusao-cargopublico/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_inclusao_cargopublico.salvar', 
        name='s1030_inclusao_cargopublico_salvar'),



url(r'^s1030-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_alteracao.apagar', 
        name='s1030_alteracao_apagar'),

url(r'^s1030-alteracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_alteracao.listar', 
        name='s1030_alteracao'),

url(r'^s1030-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_alteracao.salvar', 
        name='s1030_alteracao_salvar'),



url(r'^s1030-alteracao-cargopublico/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_alteracao_cargopublico.apagar', 
        name='s1030_alteracao_cargopublico_apagar'),

url(r'^s1030-alteracao-cargopublico/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_alteracao_cargopublico.listar', 
        name='s1030_alteracao_cargopublico'),

url(r'^s1030-alteracao-cargopublico/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_alteracao_cargopublico.salvar', 
        name='s1030_alteracao_cargopublico_salvar'),



url(r'^s1030-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_alteracao_novavalidade.apagar', 
        name='s1030_alteracao_novavalidade_apagar'),

url(r'^s1030-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_alteracao_novavalidade.listar', 
        name='s1030_alteracao_novavalidade'),

url(r'^s1030-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_alteracao_novavalidade.salvar', 
        name='s1030_alteracao_novavalidade_salvar'),



url(r'^s1030-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_exclusao.apagar', 
        name='s1030_exclusao_apagar'),

url(r'^s1030-exclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_exclusao.listar', 
        name='s1030_exclusao'),

url(r'^s1030-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1030.views.s1030_exclusao.salvar', 
        name='s1030_exclusao_salvar'),





)