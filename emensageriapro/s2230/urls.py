#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s2230-iniafastamento/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_iniafastamento.apagar', 
        name='s2230_iniafastamento_apagar'),

url(r'^s2230-iniafastamento/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_iniafastamento.listar', 
        name='s2230_iniafastamento'),

url(r'^s2230-iniafastamento/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_iniafastamento.salvar', 
        name='s2230_iniafastamento_salvar'),



url(r'^s2230-infoatestado/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_infoatestado.apagar', 
        name='s2230_infoatestado_apagar'),

url(r'^s2230-infoatestado/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_infoatestado.listar', 
        name='s2230_infoatestado'),

url(r'^s2230-infoatestado/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_infoatestado.salvar', 
        name='s2230_infoatestado_salvar'),



url(r'^s2230-emitente/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_emitente.apagar', 
        name='s2230_emitente_apagar'),

url(r'^s2230-emitente/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_emitente.listar', 
        name='s2230_emitente'),

url(r'^s2230-emitente/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_emitente.salvar', 
        name='s2230_emitente_salvar'),



url(r'^s2230-infocessao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_infocessao.apagar', 
        name='s2230_infocessao_apagar'),

url(r'^s2230-infocessao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_infocessao.listar', 
        name='s2230_infocessao'),

url(r'^s2230-infocessao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_infocessao.salvar', 
        name='s2230_infocessao_salvar'),



url(r'^s2230-infomandsind/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_infomandsind.apagar', 
        name='s2230_infomandsind_apagar'),

url(r'^s2230-infomandsind/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_infomandsind.listar', 
        name='s2230_infomandsind'),

url(r'^s2230-infomandsind/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_infomandsind.salvar', 
        name='s2230_infomandsind_salvar'),



url(r'^s2230-inforetif/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_inforetif.apagar', 
        name='s2230_inforetif_apagar'),

url(r'^s2230-inforetif/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_inforetif.listar', 
        name='s2230_inforetif'),

url(r'^s2230-inforetif/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_inforetif.salvar', 
        name='s2230_inforetif_salvar'),



url(r'^s2230-fimafastamento/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_fimafastamento.apagar', 
        name='s2230_fimafastamento_apagar'),

url(r'^s2230-fimafastamento/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_fimafastamento.listar', 
        name='s2230_fimafastamento'),

url(r'^s2230-fimafastamento/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2230.views.s2230_fimafastamento.salvar', 
        name='s2230_fimafastamento_salvar'),





)