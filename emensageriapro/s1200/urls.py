#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1200-infomv/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infomv.apagar', 
        name='s1200_infomv_apagar'),

url(r'^s1200-infomv/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infomv.listar', 
        name='s1200_infomv'),

url(r'^s1200-infomv/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infomv.salvar', 
        name='s1200_infomv_salvar'),



url(r'^s1200-remunoutrempr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_remunoutrempr.apagar', 
        name='s1200_remunoutrempr_apagar'),

url(r'^s1200-remunoutrempr/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_remunoutrempr.listar', 
        name='s1200_remunoutrempr'),

url(r'^s1200-remunoutrempr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_remunoutrempr.salvar', 
        name='s1200_remunoutrempr_salvar'),



url(r'^s1200-infocomplem/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infocomplem.apagar', 
        name='s1200_infocomplem_apagar'),

url(r'^s1200-infocomplem/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infocomplem.listar', 
        name='s1200_infocomplem'),

url(r'^s1200-infocomplem/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infocomplem.salvar', 
        name='s1200_infocomplem_salvar'),



url(r'^s1200-sucessaovinc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_sucessaovinc.apagar', 
        name='s1200_sucessaovinc_apagar'),

url(r'^s1200-sucessaovinc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_sucessaovinc.listar', 
        name='s1200_sucessaovinc'),

url(r'^s1200-sucessaovinc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_sucessaovinc.salvar', 
        name='s1200_sucessaovinc_salvar'),



url(r'^s1200-procjudtrab/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_procjudtrab.apagar', 
        name='s1200_procjudtrab_apagar'),

url(r'^s1200-procjudtrab/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_procjudtrab.listar', 
        name='s1200_procjudtrab'),

url(r'^s1200-procjudtrab/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_procjudtrab.salvar', 
        name='s1200_procjudtrab_salvar'),



url(r'^s1200-infointerm/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infointerm.apagar', 
        name='s1200_infointerm_apagar'),

url(r'^s1200-infointerm/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infointerm.listar', 
        name='s1200_infointerm'),

url(r'^s1200-infointerm/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infointerm.salvar', 
        name='s1200_infointerm_salvar'),



url(r'^s1200-dmdev/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_dmdev.apagar', 
        name='s1200_dmdev_apagar'),

url(r'^s1200-dmdev/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_dmdev.listar', 
        name='s1200_dmdev'),

url(r'^s1200-dmdev/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_dmdev.salvar', 
        name='s1200_dmdev_salvar'),



url(r'^s1200-infoperapur/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur.apagar', 
        name='s1200_infoperapur_apagar'),

url(r'^s1200-infoperapur/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur.listar', 
        name='s1200_infoperapur'),

url(r'^s1200-infoperapur/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur.salvar', 
        name='s1200_infoperapur_salvar'),



url(r'^s1200-infoperapur-ideestablot/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_ideestablot.apagar', 
        name='s1200_infoperapur_ideestablot_apagar'),

url(r'^s1200-infoperapur-ideestablot/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_ideestablot.listar', 
        name='s1200_infoperapur_ideestablot'),

url(r'^s1200-infoperapur-ideestablot/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_ideestablot.salvar', 
        name='s1200_infoperapur_ideestablot_salvar'),



url(r'^s1200-infoperapur-remunperapur/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_remunperapur.apagar', 
        name='s1200_infoperapur_remunperapur_apagar'),

url(r'^s1200-infoperapur-remunperapur/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_remunperapur.listar', 
        name='s1200_infoperapur_remunperapur'),

url(r'^s1200-infoperapur-remunperapur/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_remunperapur.salvar', 
        name='s1200_infoperapur_remunperapur_salvar'),

)


urlpatterns += patterns('',


url(r'^s1200-infoperapur-itensremun/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_itensremun.apagar', 
        name='s1200_infoperapur_itensremun_apagar'),

url(r'^s1200-infoperapur-itensremun/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_itensremun.listar', 
        name='s1200_infoperapur_itensremun'),

url(r'^s1200-infoperapur-itensremun/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_itensremun.salvar', 
        name='s1200_infoperapur_itensremun_salvar'),



url(r'^s1200-infoperapur-infosaudecolet/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_infosaudecolet.apagar', 
        name='s1200_infoperapur_infosaudecolet_apagar'),

url(r'^s1200-infoperapur-infosaudecolet/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_infosaudecolet.listar', 
        name='s1200_infoperapur_infosaudecolet'),

url(r'^s1200-infoperapur-infosaudecolet/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_infosaudecolet.salvar', 
        name='s1200_infoperapur_infosaudecolet_salvar'),



url(r'^s1200-infoperapur-detoper/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_detoper.apagar', 
        name='s1200_infoperapur_detoper_apagar'),

url(r'^s1200-infoperapur-detoper/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_detoper.listar', 
        name='s1200_infoperapur_detoper'),

url(r'^s1200-infoperapur-detoper/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_detoper.salvar', 
        name='s1200_infoperapur_detoper_salvar'),



url(r'^s1200-infoperapur-detplano/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_detplano.apagar', 
        name='s1200_infoperapur_detplano_apagar'),

url(r'^s1200-infoperapur-detplano/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_detplano.listar', 
        name='s1200_infoperapur_detplano'),

url(r'^s1200-infoperapur-detplano/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_detplano.salvar', 
        name='s1200_infoperapur_detplano_salvar'),



url(r'^s1200-infoperapur-infoagnocivo/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_infoagnocivo.apagar', 
        name='s1200_infoperapur_infoagnocivo_apagar'),

url(r'^s1200-infoperapur-infoagnocivo/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_infoagnocivo.listar', 
        name='s1200_infoperapur_infoagnocivo'),

url(r'^s1200-infoperapur-infoagnocivo/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_infoagnocivo.salvar', 
        name='s1200_infoperapur_infoagnocivo_salvar'),



url(r'^s1200-infoperapur-infotrabinterm/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_infotrabinterm.apagar', 
        name='s1200_infoperapur_infotrabinterm_apagar'),

url(r'^s1200-infoperapur-infotrabinterm/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_infotrabinterm.listar', 
        name='s1200_infoperapur_infotrabinterm'),

url(r'^s1200-infoperapur-infotrabinterm/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperapur_infotrabinterm.salvar', 
        name='s1200_infoperapur_infotrabinterm_salvar'),



url(r'^s1200-infoperant/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant.apagar', 
        name='s1200_infoperant_apagar'),

url(r'^s1200-infoperant/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant.listar', 
        name='s1200_infoperant'),

url(r'^s1200-infoperant/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant.salvar', 
        name='s1200_infoperant_salvar'),



url(r'^s1200-infoperant-ideadc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_ideadc.apagar', 
        name='s1200_infoperant_ideadc_apagar'),

url(r'^s1200-infoperant-ideadc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_ideadc.listar', 
        name='s1200_infoperant_ideadc'),

url(r'^s1200-infoperant-ideadc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_ideadc.salvar', 
        name='s1200_infoperant_ideadc_salvar'),



url(r'^s1200-infoperant-ideperiodo/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_ideperiodo.apagar', 
        name='s1200_infoperant_ideperiodo_apagar'),

url(r'^s1200-infoperant-ideperiodo/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_ideperiodo.listar', 
        name='s1200_infoperant_ideperiodo'),

url(r'^s1200-infoperant-ideperiodo/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_ideperiodo.salvar', 
        name='s1200_infoperant_ideperiodo_salvar'),



url(r'^s1200-infoperant-ideestablot/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_ideestablot.apagar', 
        name='s1200_infoperant_ideestablot_apagar'),

url(r'^s1200-infoperant-ideestablot/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_ideestablot.listar', 
        name='s1200_infoperant_ideestablot'),

url(r'^s1200-infoperant-ideestablot/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_ideestablot.salvar', 
        name='s1200_infoperant_ideestablot_salvar'),

)


urlpatterns += patterns('',


url(r'^s1200-infoperant-remunperant/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_remunperant.apagar', 
        name='s1200_infoperant_remunperant_apagar'),

url(r'^s1200-infoperant-remunperant/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_remunperant.listar', 
        name='s1200_infoperant_remunperant'),

url(r'^s1200-infoperant-remunperant/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_remunperant.salvar', 
        name='s1200_infoperant_remunperant_salvar'),



url(r'^s1200-infoperant-itensremun/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_itensremun.apagar', 
        name='s1200_infoperant_itensremun_apagar'),

url(r'^s1200-infoperant-itensremun/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_itensremun.listar', 
        name='s1200_infoperant_itensremun'),

url(r'^s1200-infoperant-itensremun/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_itensremun.salvar', 
        name='s1200_infoperant_itensremun_salvar'),



url(r'^s1200-infoperant-infoagnocivo/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_infoagnocivo.apagar', 
        name='s1200_infoperant_infoagnocivo_apagar'),

url(r'^s1200-infoperant-infoagnocivo/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_infoagnocivo.listar', 
        name='s1200_infoperant_infoagnocivo'),

url(r'^s1200-infoperant-infoagnocivo/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_infoagnocivo.salvar', 
        name='s1200_infoperant_infoagnocivo_salvar'),



url(r'^s1200-infoperant-infotrabinterm/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_infotrabinterm.apagar', 
        name='s1200_infoperant_infotrabinterm_apagar'),

url(r'^s1200-infoperant-infotrabinterm/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_infotrabinterm.listar', 
        name='s1200_infoperant_infotrabinterm'),

url(r'^s1200-infoperant-infotrabinterm/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_infotrabinterm.salvar', 
        name='s1200_infoperant_infotrabinterm_salvar'),



url(r'^s1200-infoperant-infocomplcont/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_infocomplcont.apagar', 
        name='s1200_infoperant_infocomplcont_apagar'),

url(r'^s1200-infoperant-infocomplcont/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_infocomplcont.listar', 
        name='s1200_infoperant_infocomplcont'),

url(r'^s1200-infoperant-infocomplcont/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1200.views.s1200_infoperant_infocomplcont.salvar', 
        name='s1200_infoperant_infocomplcont_salvar'),





)