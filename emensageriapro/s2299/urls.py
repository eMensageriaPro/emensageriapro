#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s2299-observacoes/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_observacoes.apagar', 
        name='s2299_observacoes_apagar'),

url(r'^s2299-observacoes/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_observacoes.listar', 
        name='s2299_observacoes'),

url(r'^s2299-observacoes/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_observacoes.salvar', 
        name='s2299_observacoes_salvar'),



url(r'^s2299-sucessaovinc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_sucessaovinc.apagar', 
        name='s2299_sucessaovinc_apagar'),

url(r'^s2299-sucessaovinc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_sucessaovinc.listar', 
        name='s2299_sucessaovinc'),

url(r'^s2299-sucessaovinc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_sucessaovinc.salvar', 
        name='s2299_sucessaovinc_salvar'),



url(r'^s2299-transftit/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_transftit.apagar', 
        name='s2299_transftit_apagar'),

url(r'^s2299-transftit/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_transftit.listar', 
        name='s2299_transftit'),

url(r'^s2299-transftit/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_transftit.salvar', 
        name='s2299_transftit_salvar'),



url(r'^s2299-verbasresc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_verbasresc.apagar', 
        name='s2299_verbasresc_apagar'),

url(r'^s2299-verbasresc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_verbasresc.listar', 
        name='s2299_verbasresc'),

url(r'^s2299-verbasresc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_verbasresc.salvar', 
        name='s2299_verbasresc_salvar'),



url(r'^s2299-dmdev/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_dmdev.apagar', 
        name='s2299_dmdev_apagar'),

url(r'^s2299-dmdev/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_dmdev.listar', 
        name='s2299_dmdev'),

url(r'^s2299-dmdev/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_dmdev.salvar', 
        name='s2299_dmdev_salvar'),



url(r'^s2299-infoperapur/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur.apagar', 
        name='s2299_infoperapur_apagar'),

url(r'^s2299-infoperapur/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur.listar', 
        name='s2299_infoperapur'),

url(r'^s2299-infoperapur/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur.salvar', 
        name='s2299_infoperapur_salvar'),



url(r'^s2299-infoperapur-ideestablot/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_ideestablot.apagar', 
        name='s2299_infoperapur_ideestablot_apagar'),

url(r'^s2299-infoperapur-ideestablot/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_ideestablot.listar', 
        name='s2299_infoperapur_ideestablot'),

url(r'^s2299-infoperapur-ideestablot/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_ideestablot.salvar', 
        name='s2299_infoperapur_ideestablot_salvar'),



url(r'^s2299-infoperapur-detverbas/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_detverbas.apagar', 
        name='s2299_infoperapur_detverbas_apagar'),

url(r'^s2299-infoperapur-detverbas/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_detverbas.listar', 
        name='s2299_infoperapur_detverbas'),

url(r'^s2299-infoperapur-detverbas/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_detverbas.salvar', 
        name='s2299_infoperapur_detverbas_salvar'),



url(r'^s2299-infoperapur-infosaudecolet/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_infosaudecolet.apagar', 
        name='s2299_infoperapur_infosaudecolet_apagar'),

url(r'^s2299-infoperapur-infosaudecolet/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_infosaudecolet.listar', 
        name='s2299_infoperapur_infosaudecolet'),

url(r'^s2299-infoperapur-infosaudecolet/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_infosaudecolet.salvar', 
        name='s2299_infoperapur_infosaudecolet_salvar'),



url(r'^s2299-infoperapur-detoper/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_detoper.apagar', 
        name='s2299_infoperapur_detoper_apagar'),

url(r'^s2299-infoperapur-detoper/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_detoper.listar', 
        name='s2299_infoperapur_detoper'),

url(r'^s2299-infoperapur-detoper/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_detoper.salvar', 
        name='s2299_infoperapur_detoper_salvar'),

)


urlpatterns += patterns('',


url(r'^s2299-infoperapur-detplano/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_detplano.apagar', 
        name='s2299_infoperapur_detplano_apagar'),

url(r'^s2299-infoperapur-detplano/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_detplano.listar', 
        name='s2299_infoperapur_detplano'),

url(r'^s2299-infoperapur-detplano/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_detplano.salvar', 
        name='s2299_infoperapur_detplano_salvar'),



url(r'^s2299-infoperapur-infoagnocivo/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_infoagnocivo.apagar', 
        name='s2299_infoperapur_infoagnocivo_apagar'),

url(r'^s2299-infoperapur-infoagnocivo/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_infoagnocivo.listar', 
        name='s2299_infoperapur_infoagnocivo'),

url(r'^s2299-infoperapur-infoagnocivo/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_infoagnocivo.salvar', 
        name='s2299_infoperapur_infoagnocivo_salvar'),



url(r'^s2299-infoperapur-infosimples/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_infosimples.apagar', 
        name='s2299_infoperapur_infosimples_apagar'),

url(r'^s2299-infoperapur-infosimples/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_infosimples.listar', 
        name='s2299_infoperapur_infosimples'),

url(r'^s2299-infoperapur-infosimples/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperapur_infosimples.salvar', 
        name='s2299_infoperapur_infosimples_salvar'),



url(r'^s2299-infoperant/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant.apagar', 
        name='s2299_infoperant_apagar'),

url(r'^s2299-infoperant/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant.listar', 
        name='s2299_infoperant'),

url(r'^s2299-infoperant/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant.salvar', 
        name='s2299_infoperant_salvar'),



url(r'^s2299-infoperant-ideadc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_ideadc.apagar', 
        name='s2299_infoperant_ideadc_apagar'),

url(r'^s2299-infoperant-ideadc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_ideadc.listar', 
        name='s2299_infoperant_ideadc'),

url(r'^s2299-infoperant-ideadc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_ideadc.salvar', 
        name='s2299_infoperant_ideadc_salvar'),



url(r'^s2299-infoperant-ideperiodo/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_ideperiodo.apagar', 
        name='s2299_infoperant_ideperiodo_apagar'),

url(r'^s2299-infoperant-ideperiodo/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_ideperiodo.listar', 
        name='s2299_infoperant_ideperiodo'),

url(r'^s2299-infoperant-ideperiodo/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_ideperiodo.salvar', 
        name='s2299_infoperant_ideperiodo_salvar'),



url(r'^s2299-infoperant-ideestablot/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_ideestablot.apagar', 
        name='s2299_infoperant_ideestablot_apagar'),

url(r'^s2299-infoperant-ideestablot/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_ideestablot.listar', 
        name='s2299_infoperant_ideestablot'),

url(r'^s2299-infoperant-ideestablot/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_ideestablot.salvar', 
        name='s2299_infoperant_ideestablot_salvar'),



url(r'^s2299-infoperant-detverbas/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_detverbas.apagar', 
        name='s2299_infoperant_detverbas_apagar'),

url(r'^s2299-infoperant-detverbas/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_detverbas.listar', 
        name='s2299_infoperant_detverbas'),

url(r'^s2299-infoperant-detverbas/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_detverbas.salvar', 
        name='s2299_infoperant_detverbas_salvar'),



url(r'^s2299-infoperant-infoagnocivo/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_infoagnocivo.apagar', 
        name='s2299_infoperant_infoagnocivo_apagar'),

url(r'^s2299-infoperant-infoagnocivo/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_infoagnocivo.listar', 
        name='s2299_infoperant_infoagnocivo'),

url(r'^s2299-infoperant-infoagnocivo/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_infoagnocivo.salvar', 
        name='s2299_infoperant_infoagnocivo_salvar'),



url(r'^s2299-infoperant-infosimples/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_infosimples.apagar', 
        name='s2299_infoperant_infosimples_apagar'),

url(r'^s2299-infoperant-infosimples/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_infosimples.listar', 
        name='s2299_infoperant_infosimples'),

url(r'^s2299-infoperant-infosimples/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infoperant_infosimples.salvar', 
        name='s2299_infoperant_infosimples_salvar'),

)


urlpatterns += patterns('',


url(r'^s2299-infotrabinterm/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm.apagar', 
        name='s2299_infotrabinterm_apagar'),

url(r'^s2299-infotrabinterm/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm.listar', 
        name='s2299_infotrabinterm'),

url(r'^s2299-infotrabinterm/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm.salvar', 
        name='s2299_infotrabinterm_salvar'),



url(r'^s2299-infotrabinterm-procjudtrab/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_procjudtrab.apagar', 
        name='s2299_infotrabinterm_procjudtrab_apagar'),

url(r'^s2299-infotrabinterm-procjudtrab/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_procjudtrab.listar', 
        name='s2299_infotrabinterm_procjudtrab'),

url(r'^s2299-infotrabinterm-procjudtrab/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_procjudtrab.salvar', 
        name='s2299_infotrabinterm_procjudtrab_salvar'),



url(r'^s2299-infotrabinterm-infomv/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_infomv.apagar', 
        name='s2299_infotrabinterm_infomv_apagar'),

url(r'^s2299-infotrabinterm-infomv/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_infomv.listar', 
        name='s2299_infotrabinterm_infomv'),

url(r'^s2299-infotrabinterm-infomv/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_infomv.salvar', 
        name='s2299_infotrabinterm_infomv_salvar'),



url(r'^s2299-infotrabinterm-remunoutrempr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_remunoutrempr.apagar', 
        name='s2299_infotrabinterm_remunoutrempr_apagar'),

url(r'^s2299-infotrabinterm-remunoutrempr/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_remunoutrempr.listar', 
        name='s2299_infotrabinterm_remunoutrempr'),

url(r'^s2299-infotrabinterm-remunoutrempr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_remunoutrempr.salvar', 
        name='s2299_infotrabinterm_remunoutrempr_salvar'),



url(r'^s2299-infotrabinterm-proccs/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_proccs.apagar', 
        name='s2299_infotrabinterm_proccs_apagar'),

url(r'^s2299-infotrabinterm-proccs/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_proccs.listar', 
        name='s2299_infotrabinterm_proccs'),

url(r'^s2299-infotrabinterm-proccs/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_proccs.salvar', 
        name='s2299_infotrabinterm_proccs_salvar'),



url(r'^s2299-infotrabinterm-quarentena/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_quarentena.apagar', 
        name='s2299_infotrabinterm_quarentena_apagar'),

url(r'^s2299-infotrabinterm-quarentena/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_quarentena.listar', 
        name='s2299_infotrabinterm_quarentena'),

url(r'^s2299-infotrabinterm-quarentena/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_quarentena.salvar', 
        name='s2299_infotrabinterm_quarentena_salvar'),



url(r'^s2299-infotrabinterm-consigfgts/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_consigfgts.apagar', 
        name='s2299_infotrabinterm_consigfgts_apagar'),

url(r'^s2299-infotrabinterm-consigfgts/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_consigfgts.listar', 
        name='s2299_infotrabinterm_consigfgts'),

url(r'^s2299-infotrabinterm-consigfgts/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2299.views.s2299_infotrabinterm_consigfgts.salvar', 
        name='s2299_infotrabinterm_consigfgts_salvar'),





)