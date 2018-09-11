#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1060-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_inclusao.apagar', 
        name='s1060_inclusao_apagar'),

url(r'^s1060-inclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_inclusao.listar', 
        name='s1060_inclusao'),

url(r'^s1060-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_inclusao.salvar', 
        name='s1060_inclusao_salvar'),



url(r'^s1060-inclusao-fatorrisco/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_inclusao_fatorrisco.apagar', 
        name='s1060_inclusao_fatorrisco_apagar'),

url(r'^s1060-inclusao-fatorrisco/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_inclusao_fatorrisco.listar', 
        name='s1060_inclusao_fatorrisco'),

url(r'^s1060-inclusao-fatorrisco/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_inclusao_fatorrisco.salvar', 
        name='s1060_inclusao_fatorrisco_salvar'),



url(r'^s1060-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_alteracao.apagar', 
        name='s1060_alteracao_apagar'),

url(r'^s1060-alteracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_alteracao.listar', 
        name='s1060_alteracao'),

url(r'^s1060-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_alteracao.salvar', 
        name='s1060_alteracao_salvar'),



url(r'^s1060-alteracao-fatorrisco/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_alteracao_fatorrisco.apagar', 
        name='s1060_alteracao_fatorrisco_apagar'),

url(r'^s1060-alteracao-fatorrisco/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_alteracao_fatorrisco.listar', 
        name='s1060_alteracao_fatorrisco'),

url(r'^s1060-alteracao-fatorrisco/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_alteracao_fatorrisco.salvar', 
        name='s1060_alteracao_fatorrisco_salvar'),



url(r'^s1060-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_alteracao_novavalidade.apagar', 
        name='s1060_alteracao_novavalidade_apagar'),

url(r'^s1060-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_alteracao_novavalidade.listar', 
        name='s1060_alteracao_novavalidade'),

url(r'^s1060-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_alteracao_novavalidade.salvar', 
        name='s1060_alteracao_novavalidade_salvar'),



url(r'^s1060-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_exclusao.apagar', 
        name='s1060_exclusao_apagar'),

url(r'^s1060-exclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_exclusao.listar', 
        name='s1060_exclusao'),

url(r'^s1060-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1060.views.s1060_exclusao.salvar', 
        name='s1060_exclusao_salvar'),





)