#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^r2040-recursosrep/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2040.views.r2040_recursosrep.apagar', 
        name='r2040_recursosrep_apagar'),

url(r'^r2040-recursosrep/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2040.views.r2040_recursosrep.listar', 
        name='r2040_recursosrep'),

url(r'^r2040-recursosrep/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2040.views.r2040_recursosrep.salvar', 
        name='r2040_recursosrep_salvar'),



url(r'^r2040-inforecurso/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2040.views.r2040_inforecurso.apagar', 
        name='r2040_inforecurso_apagar'),

url(r'^r2040-inforecurso/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2040.views.r2040_inforecurso.listar', 
        name='r2040_inforecurso'),

url(r'^r2040-inforecurso/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2040.views.r2040_inforecurso.salvar', 
        name='r2040_inforecurso_salvar'),



url(r'^r2040-infoproc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2040.views.r2040_infoproc.apagar', 
        name='r2040_infoproc_apagar'),

url(r'^r2040-infoproc/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2040.views.r2040_infoproc.listar', 
        name='r2040_infoproc'),

url(r'^r2040-infoproc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2040.views.r2040_infoproc.salvar', 
        name='r2040_infoproc_salvar'),





)