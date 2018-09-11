#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1280-infosubstpatr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1280.views.s1280_infosubstpatr.apagar', 
        name='s1280_infosubstpatr_apagar'),

url(r'^s1280-infosubstpatr/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1280.views.s1280_infosubstpatr.listar', 
        name='s1280_infosubstpatr'),

url(r'^s1280-infosubstpatr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1280.views.s1280_infosubstpatr.salvar', 
        name='s1280_infosubstpatr_salvar'),



url(r'^s1280-infosubstpatropport/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1280.views.s1280_infosubstpatropport.apagar', 
        name='s1280_infosubstpatropport_apagar'),

url(r'^s1280-infosubstpatropport/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1280.views.s1280_infosubstpatropport.listar', 
        name='s1280_infosubstpatropport'),

url(r'^s1280-infosubstpatropport/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1280.views.s1280_infosubstpatropport.salvar', 
        name='s1280_infosubstpatropport_salvar'),



url(r'^s1280-infoativconcom/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1280.views.s1280_infoativconcom.apagar', 
        name='s1280_infoativconcom_apagar'),

url(r'^s1280-infoativconcom/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1280.views.s1280_infoativconcom.listar', 
        name='s1280_infoativconcom'),

url(r'^s1280-infoativconcom/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1280.views.s1280_infoativconcom.salvar', 
        name='s1280_infoativconcom_salvar'),





)