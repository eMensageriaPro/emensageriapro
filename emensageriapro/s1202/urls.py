#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1202-procjudtrab/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_procjudtrab.apagar', 
        name='s1202_procjudtrab_apagar'),

url(r'^s1202-procjudtrab/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_procjudtrab.listar', 
        name='s1202_procjudtrab'),

url(r'^s1202-procjudtrab/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_procjudtrab.salvar', 
        name='s1202_procjudtrab_salvar'),



url(r'^s1202-dmdev/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_dmdev.apagar', 
        name='s1202_dmdev_apagar'),

url(r'^s1202-dmdev/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_dmdev.listar', 
        name='s1202_dmdev'),

url(r'^s1202-dmdev/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_dmdev.salvar', 
        name='s1202_dmdev_salvar'),



url(r'^s1202-infoperapur/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur.apagar', 
        name='s1202_infoperapur_apagar'),

url(r'^s1202-infoperapur/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur.listar', 
        name='s1202_infoperapur'),

url(r'^s1202-infoperapur/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur.salvar', 
        name='s1202_infoperapur_salvar'),



url(r'^s1202-infoperapur-ideestab/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_ideestab.apagar', 
        name='s1202_infoperapur_ideestab_apagar'),

url(r'^s1202-infoperapur-ideestab/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_ideestab.listar', 
        name='s1202_infoperapur_ideestab'),

url(r'^s1202-infoperapur-ideestab/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_ideestab.salvar', 
        name='s1202_infoperapur_ideestab_salvar'),



url(r'^s1202-infoperapur-remunperapur/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_remunperapur.apagar', 
        name='s1202_infoperapur_remunperapur_apagar'),

url(r'^s1202-infoperapur-remunperapur/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_remunperapur.listar', 
        name='s1202_infoperapur_remunperapur'),

url(r'^s1202-infoperapur-remunperapur/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_remunperapur.salvar', 
        name='s1202_infoperapur_remunperapur_salvar'),



url(r'^s1202-infoperapur-itensremun/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_itensremun.apagar', 
        name='s1202_infoperapur_itensremun_apagar'),

url(r'^s1202-infoperapur-itensremun/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_itensremun.listar', 
        name='s1202_infoperapur_itensremun'),

url(r'^s1202-infoperapur-itensremun/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_itensremun.salvar', 
        name='s1202_infoperapur_itensremun_salvar'),



url(r'^s1202-infoperapur-infosaudecolet/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_infosaudecolet.apagar', 
        name='s1202_infoperapur_infosaudecolet_apagar'),

url(r'^s1202-infoperapur-infosaudecolet/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_infosaudecolet.listar', 
        name='s1202_infoperapur_infosaudecolet'),

url(r'^s1202-infoperapur-infosaudecolet/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_infosaudecolet.salvar', 
        name='s1202_infoperapur_infosaudecolet_salvar'),



url(r'^s1202-infoperapur-detoper/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_detoper.apagar', 
        name='s1202_infoperapur_detoper_apagar'),

url(r'^s1202-infoperapur-detoper/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_detoper.listar', 
        name='s1202_infoperapur_detoper'),

url(r'^s1202-infoperapur-detoper/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_detoper.salvar', 
        name='s1202_infoperapur_detoper_salvar'),



url(r'^s1202-infoperapur-detplano/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_detplano.apagar', 
        name='s1202_infoperapur_detplano_apagar'),

url(r'^s1202-infoperapur-detplano/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_detplano.listar', 
        name='s1202_infoperapur_detplano'),

url(r'^s1202-infoperapur-detplano/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperapur_detplano.salvar', 
        name='s1202_infoperapur_detplano_salvar'),



url(r'^s1202-infoperant/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant.apagar', 
        name='s1202_infoperant_apagar'),

url(r'^s1202-infoperant/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant.listar', 
        name='s1202_infoperant'),

url(r'^s1202-infoperant/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant.salvar', 
        name='s1202_infoperant_salvar'),

)


urlpatterns += patterns('',


url(r'^s1202-infoperant-ideadc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant_ideadc.apagar', 
        name='s1202_infoperant_ideadc_apagar'),

url(r'^s1202-infoperant-ideadc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant_ideadc.listar', 
        name='s1202_infoperant_ideadc'),

url(r'^s1202-infoperant-ideadc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant_ideadc.salvar', 
        name='s1202_infoperant_ideadc_salvar'),



url(r'^s1202-infoperant-ideperiodo/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant_ideperiodo.apagar', 
        name='s1202_infoperant_ideperiodo_apagar'),

url(r'^s1202-infoperant-ideperiodo/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant_ideperiodo.listar', 
        name='s1202_infoperant_ideperiodo'),

url(r'^s1202-infoperant-ideperiodo/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant_ideperiodo.salvar', 
        name='s1202_infoperant_ideperiodo_salvar'),



url(r'^s1202-infoperant-ideestab/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant_ideestab.apagar', 
        name='s1202_infoperant_ideestab_apagar'),

url(r'^s1202-infoperant-ideestab/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant_ideestab.listar', 
        name='s1202_infoperant_ideestab'),

url(r'^s1202-infoperant-ideestab/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant_ideestab.salvar', 
        name='s1202_infoperant_ideestab_salvar'),



url(r'^s1202-infoperant-remunperant/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant_remunperant.apagar', 
        name='s1202_infoperant_remunperant_apagar'),

url(r'^s1202-infoperant-remunperant/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant_remunperant.listar', 
        name='s1202_infoperant_remunperant'),

url(r'^s1202-infoperant-remunperant/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant_remunperant.salvar', 
        name='s1202_infoperant_remunperant_salvar'),



url(r'^s1202-infoperant-itensremun/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant_itensremun.apagar', 
        name='s1202_infoperant_itensremun_apagar'),

url(r'^s1202-infoperant-itensremun/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant_itensremun.listar', 
        name='s1202_infoperant_itensremun'),

url(r'^s1202-infoperant-itensremun/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1202.views.s1202_infoperant_itensremun.salvar', 
        name='s1202_infoperant_itensremun_salvar'),





)