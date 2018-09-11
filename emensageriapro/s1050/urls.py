#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1050-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_inclusao.apagar', 
        name='s1050_inclusao_apagar'),

url(r'^s1050-inclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_inclusao.listar', 
        name='s1050_inclusao'),

url(r'^s1050-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_inclusao.salvar', 
        name='s1050_inclusao_salvar'),



url(r'^s1050-inclusao-horariointervalo/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_inclusao_horariointervalo.apagar', 
        name='s1050_inclusao_horariointervalo_apagar'),

url(r'^s1050-inclusao-horariointervalo/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_inclusao_horariointervalo.listar', 
        name='s1050_inclusao_horariointervalo'),

url(r'^s1050-inclusao-horariointervalo/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_inclusao_horariointervalo.salvar', 
        name='s1050_inclusao_horariointervalo_salvar'),



url(r'^s1050-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_alteracao.apagar', 
        name='s1050_alteracao_apagar'),

url(r'^s1050-alteracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_alteracao.listar', 
        name='s1050_alteracao'),

url(r'^s1050-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_alteracao.salvar', 
        name='s1050_alteracao_salvar'),



url(r'^s1050-alteracao-horariointervalo/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_alteracao_horariointervalo.apagar', 
        name='s1050_alteracao_horariointervalo_apagar'),

url(r'^s1050-alteracao-horariointervalo/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_alteracao_horariointervalo.listar', 
        name='s1050_alteracao_horariointervalo'),

url(r'^s1050-alteracao-horariointervalo/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_alteracao_horariointervalo.salvar', 
        name='s1050_alteracao_horariointervalo_salvar'),



url(r'^s1050-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_alteracao_novavalidade.apagar', 
        name='s1050_alteracao_novavalidade_apagar'),

url(r'^s1050-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_alteracao_novavalidade.listar', 
        name='s1050_alteracao_novavalidade'),

url(r'^s1050-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_alteracao_novavalidade.salvar', 
        name='s1050_alteracao_novavalidade_salvar'),



url(r'^s1050-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_exclusao.apagar', 
        name='s1050_exclusao_apagar'),

url(r'^s1050-exclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_exclusao.listar', 
        name='s1050_exclusao'),

url(r'^s1050-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1050.views.s1050_exclusao.salvar', 
        name='s1050_exclusao_salvar'),





)