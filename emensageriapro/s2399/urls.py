#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s2399-verbasresc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_verbasresc.apagar', 
        name='s2399_verbasresc_apagar'),

url(r'^s2399-verbasresc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_verbasresc.listar', 
        name='s2399_verbasresc'),

url(r'^s2399-verbasresc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_verbasresc.salvar', 
        name='s2399_verbasresc_salvar'),



url(r'^s2399-dmdev/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_dmdev.apagar', 
        name='s2399_dmdev_apagar'),

url(r'^s2399-dmdev/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_dmdev.listar', 
        name='s2399_dmdev'),

url(r'^s2399-dmdev/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_dmdev.salvar', 
        name='s2399_dmdev_salvar'),



url(r'^s2399-ideestablot/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_ideestablot.apagar', 
        name='s2399_ideestablot_apagar'),

url(r'^s2399-ideestablot/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_ideestablot.listar', 
        name='s2399_ideestablot'),

url(r'^s2399-ideestablot/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_ideestablot.salvar', 
        name='s2399_ideestablot_salvar'),



url(r'^s2399-detverbas/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_detverbas.apagar', 
        name='s2399_detverbas_apagar'),

url(r'^s2399-detverbas/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_detverbas.listar', 
        name='s2399_detverbas'),

url(r'^s2399-detverbas/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_detverbas.salvar', 
        name='s2399_detverbas_salvar'),



url(r'^s2399-infosaudecolet/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_infosaudecolet.apagar', 
        name='s2399_infosaudecolet_apagar'),

url(r'^s2399-infosaudecolet/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_infosaudecolet.listar', 
        name='s2399_infosaudecolet'),

url(r'^s2399-infosaudecolet/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_infosaudecolet.salvar', 
        name='s2399_infosaudecolet_salvar'),



url(r'^s2399-detoper/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_detoper.apagar', 
        name='s2399_detoper_apagar'),

url(r'^s2399-detoper/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_detoper.listar', 
        name='s2399_detoper'),

url(r'^s2399-detoper/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_detoper.salvar', 
        name='s2399_detoper_salvar'),



url(r'^s2399-detplano/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_detplano.apagar', 
        name='s2399_detplano_apagar'),

url(r'^s2399-detplano/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_detplano.listar', 
        name='s2399_detplano'),

url(r'^s2399-detplano/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_detplano.salvar', 
        name='s2399_detplano_salvar'),



url(r'^s2399-infoagnocivo/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_infoagnocivo.apagar', 
        name='s2399_infoagnocivo_apagar'),

url(r'^s2399-infoagnocivo/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_infoagnocivo.listar', 
        name='s2399_infoagnocivo'),

url(r'^s2399-infoagnocivo/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_infoagnocivo.salvar', 
        name='s2399_infoagnocivo_salvar'),



url(r'^s2399-infosimples/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_infosimples.apagar', 
        name='s2399_infosimples_apagar'),

url(r'^s2399-infosimples/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_infosimples.listar', 
        name='s2399_infosimples'),

url(r'^s2399-infosimples/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_infosimples.salvar', 
        name='s2399_infosimples_salvar'),



url(r'^s2399-procjudtrab/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_procjudtrab.apagar', 
        name='s2399_procjudtrab_apagar'),

url(r'^s2399-procjudtrab/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_procjudtrab.listar', 
        name='s2399_procjudtrab'),

url(r'^s2399-procjudtrab/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_procjudtrab.salvar', 
        name='s2399_procjudtrab_salvar'),

)


urlpatterns += patterns('',


url(r'^s2399-infomv/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_infomv.apagar', 
        name='s2399_infomv_apagar'),

url(r'^s2399-infomv/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_infomv.listar', 
        name='s2399_infomv'),

url(r'^s2399-infomv/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_infomv.salvar', 
        name='s2399_infomv_salvar'),



url(r'^s2399-remunoutrempr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_remunoutrempr.apagar', 
        name='s2399_remunoutrempr_apagar'),

url(r'^s2399-remunoutrempr/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_remunoutrempr.listar', 
        name='s2399_remunoutrempr'),

url(r'^s2399-remunoutrempr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_remunoutrempr.salvar', 
        name='s2399_remunoutrempr_salvar'),



url(r'^s2399-quarentena/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_quarentena.apagar', 
        name='s2399_quarentena_apagar'),

url(r'^s2399-quarentena/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_quarentena.listar', 
        name='s2399_quarentena'),

url(r'^s2399-quarentena/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2399.views.s2399_quarentena.salvar', 
        name='s2399_quarentena_salvar'),





)