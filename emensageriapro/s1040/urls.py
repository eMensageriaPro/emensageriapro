#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1040-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1040.views.s1040_inclusao.apagar', 
        name='s1040_inclusao_apagar'),

url(r'^s1040-inclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1040.views.s1040_inclusao.listar', 
        name='s1040_inclusao'),

url(r'^s1040-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1040.views.s1040_inclusao.salvar', 
        name='s1040_inclusao_salvar'),



url(r'^s1040-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1040.views.s1040_alteracao.apagar', 
        name='s1040_alteracao_apagar'),

url(r'^s1040-alteracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1040.views.s1040_alteracao.listar', 
        name='s1040_alteracao'),

url(r'^s1040-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1040.views.s1040_alteracao.salvar', 
        name='s1040_alteracao_salvar'),



url(r'^s1040-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1040.views.s1040_alteracao_novavalidade.apagar', 
        name='s1040_alteracao_novavalidade_apagar'),

url(r'^s1040-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1040.views.s1040_alteracao_novavalidade.listar', 
        name='s1040_alteracao_novavalidade'),

url(r'^s1040-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1040.views.s1040_alteracao_novavalidade.salvar', 
        name='s1040_alteracao_novavalidade_salvar'),



url(r'^s1040-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1040.views.s1040_exclusao.apagar', 
        name='s1040_exclusao_apagar'),

url(r'^s1040-exclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1040.views.s1040_exclusao.listar', 
        name='s1040_exclusao'),

url(r'^s1040-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1040.views.s1040_exclusao.salvar', 
        name='s1040_exclusao_salvar'),





)