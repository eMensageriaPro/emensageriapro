#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s2241-insalperic/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_insalperic.apagar', 
        name='s2241_insalperic_apagar'),

url(r'^s2241-insalperic/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_insalperic.listar', 
        name='s2241_insalperic'),

url(r'^s2241-insalperic/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_insalperic.salvar', 
        name='s2241_insalperic_salvar'),



url(r'^s2241-iniinsalperic/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniinsalperic.apagar', 
        name='s2241_iniinsalperic_apagar'),

url(r'^s2241-iniinsalperic/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniinsalperic.listar', 
        name='s2241_iniinsalperic'),

url(r'^s2241-iniinsalperic/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniinsalperic.salvar', 
        name='s2241_iniinsalperic_salvar'),



url(r'^s2241-iniinsalperic-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniinsalperic_infoamb.apagar', 
        name='s2241_iniinsalperic_infoamb_apagar'),

url(r'^s2241-iniinsalperic-infoamb/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniinsalperic_infoamb.listar', 
        name='s2241_iniinsalperic_infoamb'),

url(r'^s2241-iniinsalperic-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniinsalperic_infoamb.salvar', 
        name='s2241_iniinsalperic_infoamb_salvar'),



url(r'^s2241-iniinsalperic-fatrisco/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniinsalperic_fatrisco.apagar', 
        name='s2241_iniinsalperic_fatrisco_apagar'),

url(r'^s2241-iniinsalperic-fatrisco/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniinsalperic_fatrisco.listar', 
        name='s2241_iniinsalperic_fatrisco'),

url(r'^s2241-iniinsalperic-fatrisco/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniinsalperic_fatrisco.salvar', 
        name='s2241_iniinsalperic_fatrisco_salvar'),



url(r'^s2241-altinsalperic/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altinsalperic.apagar', 
        name='s2241_altinsalperic_apagar'),

url(r'^s2241-altinsalperic/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altinsalperic.listar', 
        name='s2241_altinsalperic'),

url(r'^s2241-altinsalperic/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altinsalperic.salvar', 
        name='s2241_altinsalperic_salvar'),



url(r'^s2241-altinsalperic-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altinsalperic_infoamb.apagar', 
        name='s2241_altinsalperic_infoamb_apagar'),

url(r'^s2241-altinsalperic-infoamb/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altinsalperic_infoamb.listar', 
        name='s2241_altinsalperic_infoamb'),

url(r'^s2241-altinsalperic-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altinsalperic_infoamb.salvar', 
        name='s2241_altinsalperic_infoamb_salvar'),



url(r'^s2241-altinsalperic-fatrisco/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altinsalperic_fatrisco.apagar', 
        name='s2241_altinsalperic_fatrisco_apagar'),

url(r'^s2241-altinsalperic-fatrisco/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altinsalperic_fatrisco.listar', 
        name='s2241_altinsalperic_fatrisco'),

url(r'^s2241-altinsalperic-fatrisco/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altinsalperic_fatrisco.salvar', 
        name='s2241_altinsalperic_fatrisco_salvar'),



url(r'^s2241-fiminsalperic/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_fiminsalperic.apagar', 
        name='s2241_fiminsalperic_apagar'),

url(r'^s2241-fiminsalperic/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_fiminsalperic.listar', 
        name='s2241_fiminsalperic'),

url(r'^s2241-fiminsalperic/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_fiminsalperic.salvar', 
        name='s2241_fiminsalperic_salvar'),



url(r'^s2241-fiminsalperic-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_fiminsalperic_infoamb.apagar', 
        name='s2241_fiminsalperic_infoamb_apagar'),

url(r'^s2241-fiminsalperic-infoamb/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_fiminsalperic_infoamb.listar', 
        name='s2241_fiminsalperic_infoamb'),

url(r'^s2241-fiminsalperic-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_fiminsalperic_infoamb.salvar', 
        name='s2241_fiminsalperic_infoamb_salvar'),



url(r'^s2241-aposentesp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_aposentesp.apagar', 
        name='s2241_aposentesp_apagar'),

url(r'^s2241-aposentesp/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_aposentesp.listar', 
        name='s2241_aposentesp'),

url(r'^s2241-aposentesp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_aposentesp.salvar', 
        name='s2241_aposentesp_salvar'),

)


urlpatterns += patterns('',


url(r'^s2241-iniaposentesp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniaposentesp.apagar', 
        name='s2241_iniaposentesp_apagar'),

url(r'^s2241-iniaposentesp/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniaposentesp.listar', 
        name='s2241_iniaposentesp'),

url(r'^s2241-iniaposentesp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniaposentesp.salvar', 
        name='s2241_iniaposentesp_salvar'),



url(r'^s2241-iniaposentesp-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniaposentesp_infoamb.apagar', 
        name='s2241_iniaposentesp_infoamb_apagar'),

url(r'^s2241-iniaposentesp-infoamb/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniaposentesp_infoamb.listar', 
        name='s2241_iniaposentesp_infoamb'),

url(r'^s2241-iniaposentesp-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniaposentesp_infoamb.salvar', 
        name='s2241_iniaposentesp_infoamb_salvar'),



url(r'^s2241-iniaposentesp-fatrisco/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniaposentesp_fatrisco.apagar', 
        name='s2241_iniaposentesp_fatrisco_apagar'),

url(r'^s2241-iniaposentesp-fatrisco/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniaposentesp_fatrisco.listar', 
        name='s2241_iniaposentesp_fatrisco'),

url(r'^s2241-iniaposentesp-fatrisco/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_iniaposentesp_fatrisco.salvar', 
        name='s2241_iniaposentesp_fatrisco_salvar'),



url(r'^s2241-altaposentesp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altaposentesp.apagar', 
        name='s2241_altaposentesp_apagar'),

url(r'^s2241-altaposentesp/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altaposentesp.listar', 
        name='s2241_altaposentesp'),

url(r'^s2241-altaposentesp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altaposentesp.salvar', 
        name='s2241_altaposentesp_salvar'),



url(r'^s2241-altaposentesp-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altaposentesp_infoamb.apagar', 
        name='s2241_altaposentesp_infoamb_apagar'),

url(r'^s2241-altaposentesp-infoamb/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altaposentesp_infoamb.listar', 
        name='s2241_altaposentesp_infoamb'),

url(r'^s2241-altaposentesp-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altaposentesp_infoamb.salvar', 
        name='s2241_altaposentesp_infoamb_salvar'),



url(r'^s2241-altaposentesp-fatrisco/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altaposentesp_fatrisco.apagar', 
        name='s2241_altaposentesp_fatrisco_apagar'),

url(r'^s2241-altaposentesp-fatrisco/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altaposentesp_fatrisco.listar', 
        name='s2241_altaposentesp_fatrisco'),

url(r'^s2241-altaposentesp-fatrisco/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_altaposentesp_fatrisco.salvar', 
        name='s2241_altaposentesp_fatrisco_salvar'),



url(r'^s2241-fimaposentesp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_fimaposentesp.apagar', 
        name='s2241_fimaposentesp_apagar'),

url(r'^s2241-fimaposentesp/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_fimaposentesp.listar', 
        name='s2241_fimaposentesp'),

url(r'^s2241-fimaposentesp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_fimaposentesp.salvar', 
        name='s2241_fimaposentesp_salvar'),



url(r'^s2241-fimaposentesp-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_fimaposentesp_infoamb.apagar', 
        name='s2241_fimaposentesp_infoamb_apagar'),

url(r'^s2241-fimaposentesp-infoamb/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_fimaposentesp_infoamb.listar', 
        name='s2241_fimaposentesp_infoamb'),

url(r'^s2241-fimaposentesp-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2241.views.s2241_fimaposentesp_infoamb.salvar', 
        name='s2241_fimaposentesp_infoamb_salvar'),





)