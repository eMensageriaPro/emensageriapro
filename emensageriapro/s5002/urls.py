#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s5002-infodep/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5002.views.s5002_infodep.apagar', 
        name='s5002_infodep_apagar'),

url(r'^s5002-infodep/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5002.views.s5002_infodep.listar', 
        name='s5002_infodep'),

url(r'^s5002-infodep/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5002.views.s5002_infodep.salvar', 
        name='s5002_infodep_salvar'),



url(r'^s5002-infoirrf/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5002.views.s5002_infoirrf.apagar', 
        name='s5002_infoirrf_apagar'),

url(r'^s5002-infoirrf/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5002.views.s5002_infoirrf.listar', 
        name='s5002_infoirrf'),

url(r'^s5002-infoirrf/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5002.views.s5002_infoirrf.salvar', 
        name='s5002_infoirrf_salvar'),



url(r'^s5002-basesirrf/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5002.views.s5002_basesirrf.apagar', 
        name='s5002_basesirrf_apagar'),

url(r'^s5002-basesirrf/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5002.views.s5002_basesirrf.listar', 
        name='s5002_basesirrf'),

url(r'^s5002-basesirrf/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5002.views.s5002_basesirrf.salvar', 
        name='s5002_basesirrf_salvar'),



url(r'^s5002-irrf/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5002.views.s5002_irrf.apagar', 
        name='s5002_irrf_apagar'),

url(r'^s5002-irrf/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5002.views.s5002_irrf.listar', 
        name='s5002_irrf'),

url(r'^s5002-irrf/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5002.views.s5002_irrf.salvar', 
        name='s5002_irrf_salvar'),



url(r'^s5002-idepgtoext/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5002.views.s5002_idepgtoext.apagar', 
        name='s5002_idepgtoext_apagar'),

url(r'^s5002-idepgtoext/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5002.views.s5002_idepgtoext.listar', 
        name='s5002_idepgtoext'),

url(r'^s5002-idepgtoext/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5002.views.s5002_idepgtoext.salvar', 
        name='s5002_idepgtoext_salvar'),





)