#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^r2060-tipocod/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_tipocod.apagar', 
        name='r2060_tipocod_apagar'),

url(r'^r2060-tipocod/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_tipocod.listar', 
        name='r2060_tipocod'),

url(r'^r2060-tipocod/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_tipocod.salvar', 
        name='r2060_tipocod_salvar'),



url(r'^r2060-tipoajuste/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_tipoajuste.apagar', 
        name='r2060_tipoajuste_apagar'),

url(r'^r2060-tipoajuste/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_tipoajuste.listar', 
        name='r2060_tipoajuste'),

url(r'^r2060-tipoajuste/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_tipoajuste.salvar', 
        name='r2060_tipoajuste_salvar'),



url(r'^r2060-infoproc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_infoproc.apagar', 
        name='r2060_infoproc_apagar'),

url(r'^r2060-infoproc/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_infoproc.listar', 
        name='r2060_infoproc'),

url(r'^r2060-infoproc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_infoproc.salvar', 
        name='r2060_infoproc_salvar'),





)