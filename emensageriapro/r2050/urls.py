#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^r2050-tipocom/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2050.views.r2050_tipocom.apagar', 
        name='r2050_tipocom_apagar'),

url(r'^r2050-tipocom/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2050.views.r2050_tipocom.listar', 
        name='r2050_tipocom'),

url(r'^r2050-tipocom/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2050.views.r2050_tipocom.salvar', 
        name='r2050_tipocom_salvar'),



url(r'^r2050-infoproc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2050.views.r2050_infoproc.apagar', 
        name='r2050_infoproc_apagar'),

url(r'^r2050-infoproc/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2050.views.r2050_infoproc.listar', 
        name='r2050_infoproc'),

url(r'^r2050-infoproc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2050.views.r2050_infoproc.salvar', 
        name='r2050_infoproc_salvar'),





)