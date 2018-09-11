#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s5001-procjudtrab/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_procjudtrab.apagar', 
        name='s5001_procjudtrab_apagar'),

url(r'^s5001-procjudtrab/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_procjudtrab.listar', 
        name='s5001_procjudtrab'),

url(r'^s5001-procjudtrab/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_procjudtrab.salvar', 
        name='s5001_procjudtrab_salvar'),



url(r'^s5001-infocpcalc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocpcalc.apagar', 
        name='s5001_infocpcalc_apagar'),

url(r'^s5001-infocpcalc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocpcalc.listar', 
        name='s5001_infocpcalc'),

url(r'^s5001-infocpcalc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocpcalc.salvar', 
        name='s5001_infocpcalc_salvar'),



url(r'^s5001-infocp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocp.apagar', 
        name='s5001_infocp_apagar'),

url(r'^s5001-infocp/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocp.listar', 
        name='s5001_infocp'),

url(r'^s5001-infocp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocp.salvar', 
        name='s5001_infocp_salvar'),



url(r'^s5001-ideestablot/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_ideestablot.apagar', 
        name='s5001_ideestablot_apagar'),

url(r'^s5001-ideestablot/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_ideestablot.listar', 
        name='s5001_ideestablot'),

url(r'^s5001-ideestablot/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_ideestablot.salvar', 
        name='s5001_ideestablot_salvar'),



url(r'^s5001-infocategincid/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocategincid.apagar', 
        name='s5001_infocategincid_apagar'),

url(r'^s5001-infocategincid/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocategincid.listar', 
        name='s5001_infocategincid'),

url(r'^s5001-infocategincid/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocategincid.salvar', 
        name='s5001_infocategincid_salvar'),



url(r'^s5001-infobasecs/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infobasecs.apagar', 
        name='s5001_infobasecs_apagar'),

url(r'^s5001-infobasecs/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infobasecs.listar', 
        name='s5001_infobasecs'),

url(r'^s5001-infobasecs/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infobasecs.salvar', 
        name='s5001_infobasecs_salvar'),



url(r'^s5001-calcterc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_calcterc.apagar', 
        name='s5001_calcterc_apagar'),

url(r'^s5001-calcterc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_calcterc.listar', 
        name='s5001_calcterc'),

url(r'^s5001-calcterc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_calcterc.salvar', 
        name='s5001_calcterc_salvar'),





)