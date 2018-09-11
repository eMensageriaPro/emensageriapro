#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^r3010-ideestab/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_ideestab.apagar', 
        name='r3010_ideestab_apagar'),

url(r'^r3010-ideestab/listar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_ideestab.listar', 
        name='r3010_ideestab'),

url(r'^r3010-ideestab/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_ideestab.salvar', 
        name='r3010_ideestab_salvar'),



url(r'^r3010-boletim/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_boletim.apagar', 
        name='r3010_boletim_apagar'),

url(r'^r3010-boletim/listar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_boletim.listar', 
        name='r3010_boletim'),

url(r'^r3010-boletim/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_boletim.salvar', 
        name='r3010_boletim_salvar'),



url(r'^r3010-receitaingressos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_receitaingressos.apagar', 
        name='r3010_receitaingressos_apagar'),

url(r'^r3010-receitaingressos/listar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_receitaingressos.listar', 
        name='r3010_receitaingressos'),

url(r'^r3010-receitaingressos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_receitaingressos.salvar', 
        name='r3010_receitaingressos_salvar'),



url(r'^r3010-outrasreceitas/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_outrasreceitas.apagar', 
        name='r3010_outrasreceitas_apagar'),

url(r'^r3010-outrasreceitas/listar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_outrasreceitas.listar', 
        name='r3010_outrasreceitas'),

url(r'^r3010-outrasreceitas/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_outrasreceitas.salvar', 
        name='r3010_outrasreceitas_salvar'),



url(r'^r3010-infoproc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_infoproc.apagar', 
        name='r3010_infoproc_apagar'),

url(r'^r3010-infoproc/listar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_infoproc.listar', 
        name='r3010_infoproc'),

url(r'^r3010-infoproc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_infoproc.salvar', 
        name='r3010_infoproc_salvar'),





)