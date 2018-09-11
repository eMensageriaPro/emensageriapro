#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^r2030-recursosrec/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2030.views.r2030_recursosrec.apagar', 
        name='r2030_recursosrec_apagar'),

url(r'^r2030-recursosrec/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2030.views.r2030_recursosrec.listar', 
        name='r2030_recursosrec'),

url(r'^r2030-recursosrec/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2030.views.r2030_recursosrec.salvar', 
        name='r2030_recursosrec_salvar'),



url(r'^r2030-inforecurso/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2030.views.r2030_inforecurso.apagar', 
        name='r2030_inforecurso_apagar'),

url(r'^r2030-inforecurso/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2030.views.r2030_inforecurso.listar', 
        name='r2030_inforecurso'),

url(r'^r2030-inforecurso/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2030.views.r2030_inforecurso.salvar', 
        name='r2030_inforecurso_salvar'),



url(r'^r2030-infoproc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2030.views.r2030_infoproc.apagar', 
        name='r2030_infoproc_apagar'),

url(r'^r2030-infoproc/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2030.views.r2030_infoproc.listar', 
        name='r2030_infoproc'),

url(r'^r2030-infoproc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2030.views.r2030_infoproc.salvar', 
        name='r2030_infoproc_salvar'),





)