#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1080-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_inclusao.apagar', 
        name='s1080_inclusao_apagar'),

url(r'^s1080-inclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_inclusao.listar', 
        name='s1080_inclusao'),

url(r'^s1080-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_inclusao.salvar', 
        name='s1080_inclusao_salvar'),



url(r'^s1080-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_alteracao.apagar', 
        name='s1080_alteracao_apagar'),

url(r'^s1080-alteracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_alteracao.listar', 
        name='s1080_alteracao'),

url(r'^s1080-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_alteracao.salvar', 
        name='s1080_alteracao_salvar'),



url(r'^s1080-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_alteracao_novavalidade.apagar', 
        name='s1080_alteracao_novavalidade_apagar'),

url(r'^s1080-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_alteracao_novavalidade.listar', 
        name='s1080_alteracao_novavalidade'),

url(r'^s1080-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_alteracao_novavalidade.salvar', 
        name='s1080_alteracao_novavalidade_salvar'),



url(r'^s1080-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_exclusao.apagar', 
        name='s1080_exclusao_apagar'),

url(r'^s1080-exclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_exclusao.listar', 
        name='s1080_exclusao'),

url(r'^s1080-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_exclusao.salvar', 
        name='s1080_exclusao_salvar'),





)