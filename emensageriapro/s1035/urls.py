#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1035-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1035.views.s1035_inclusao.apagar', 
        name='s1035_inclusao_apagar'),

url(r'^s1035-inclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1035.views.s1035_inclusao.listar', 
        name='s1035_inclusao'),

url(r'^s1035-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1035.views.s1035_inclusao.salvar', 
        name='s1035_inclusao_salvar'),



url(r'^s1035-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1035.views.s1035_alteracao.apagar', 
        name='s1035_alteracao_apagar'),

url(r'^s1035-alteracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1035.views.s1035_alteracao.listar', 
        name='s1035_alteracao'),

url(r'^s1035-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1035.views.s1035_alteracao.salvar', 
        name='s1035_alteracao_salvar'),



url(r'^s1035-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1035.views.s1035_alteracao_novavalidade.apagar', 
        name='s1035_alteracao_novavalidade_apagar'),

url(r'^s1035-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1035.views.s1035_alteracao_novavalidade.listar', 
        name='s1035_alteracao_novavalidade'),

url(r'^s1035-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1035.views.s1035_alteracao_novavalidade.salvar', 
        name='s1035_alteracao_novavalidade_salvar'),



url(r'^s1035-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1035.views.s1035_exclusao.apagar', 
        name='s1035_exclusao_apagar'),

url(r'^s1035-exclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1035.views.s1035_exclusao.listar', 
        name='s1035_exclusao'),

url(r'^s1035-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1035.views.s1035_exclusao.salvar', 
        name='s1035_exclusao_salvar'),





)