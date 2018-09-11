#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s2210-parteatingida/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2210.views.s2210_parteatingida.apagar', 
        name='s2210_parteatingida_apagar'),

url(r'^s2210-parteatingida/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2210.views.s2210_parteatingida.listar', 
        name='s2210_parteatingida'),

url(r'^s2210-parteatingida/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2210.views.s2210_parteatingida.salvar', 
        name='s2210_parteatingida_salvar'),



url(r'^s2210-agentecausador/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2210.views.s2210_agentecausador.apagar', 
        name='s2210_agentecausador_apagar'),

url(r'^s2210-agentecausador/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2210.views.s2210_agentecausador.listar', 
        name='s2210_agentecausador'),

url(r'^s2210-agentecausador/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2210.views.s2210_agentecausador.salvar', 
        name='s2210_agentecausador_salvar'),



url(r'^s2210-atestado/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2210.views.s2210_atestado.apagar', 
        name='s2210_atestado_apagar'),

url(r'^s2210-atestado/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2210.views.s2210_atestado.listar', 
        name='s2210_atestado'),

url(r'^s2210-atestado/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2210.views.s2210_atestado.salvar', 
        name='s2210_atestado_salvar'),



url(r'^s2210-catorigem/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2210.views.s2210_catorigem.apagar', 
        name='s2210_catorigem_apagar'),

url(r'^s2210-catorigem/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2210.views.s2210_catorigem.listar', 
        name='s2210_catorigem'),

url(r'^s2210-catorigem/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2210.views.s2210_catorigem.salvar', 
        name='s2210_catorigem_salvar'),





)