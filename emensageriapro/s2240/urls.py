#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s2240-iniexprisco/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_iniexprisco.apagar', 
        name='s2240_iniexprisco_apagar'),

url(r'^s2240-iniexprisco/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_iniexprisco.listar', 
        name='s2240_iniexprisco'),

url(r'^s2240-iniexprisco/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_iniexprisco.salvar', 
        name='s2240_iniexprisco_salvar'),



url(r'^s2240-iniexprisco-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_iniexprisco_infoamb.apagar', 
        name='s2240_iniexprisco_infoamb_apagar'),

url(r'^s2240-iniexprisco-infoamb/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_iniexprisco_infoamb.listar', 
        name='s2240_iniexprisco_infoamb'),

url(r'^s2240-iniexprisco-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_iniexprisco_infoamb.salvar', 
        name='s2240_iniexprisco_infoamb_salvar'),



url(r'^s2240-iniexprisco-fatrisco/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_iniexprisco_fatrisco.apagar', 
        name='s2240_iniexprisco_fatrisco_apagar'),

url(r'^s2240-iniexprisco-fatrisco/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_iniexprisco_fatrisco.listar', 
        name='s2240_iniexprisco_fatrisco'),

url(r'^s2240-iniexprisco-fatrisco/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_iniexprisco_fatrisco.salvar', 
        name='s2240_iniexprisco_fatrisco_salvar'),



url(r'^s2240-iniexprisco-epc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_iniexprisco_epc.apagar', 
        name='s2240_iniexprisco_epc_apagar'),

url(r'^s2240-iniexprisco-epc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_iniexprisco_epc.listar', 
        name='s2240_iniexprisco_epc'),

url(r'^s2240-iniexprisco-epc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_iniexprisco_epc.salvar', 
        name='s2240_iniexprisco_epc_salvar'),



url(r'^s2240-iniexprisco-epi/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_iniexprisco_epi.apagar', 
        name='s2240_iniexprisco_epi_apagar'),

url(r'^s2240-iniexprisco-epi/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_iniexprisco_epi.listar', 
        name='s2240_iniexprisco_epi'),

url(r'^s2240-iniexprisco-epi/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_iniexprisco_epi.salvar', 
        name='s2240_iniexprisco_epi_salvar'),



url(r'^s2240-altexprisco/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_altexprisco.apagar', 
        name='s2240_altexprisco_apagar'),

url(r'^s2240-altexprisco/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_altexprisco.listar', 
        name='s2240_altexprisco'),

url(r'^s2240-altexprisco/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_altexprisco.salvar', 
        name='s2240_altexprisco_salvar'),



url(r'^s2240-altexprisco-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_altexprisco_infoamb.apagar', 
        name='s2240_altexprisco_infoamb_apagar'),

url(r'^s2240-altexprisco-infoamb/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_altexprisco_infoamb.listar', 
        name='s2240_altexprisco_infoamb'),

url(r'^s2240-altexprisco-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_altexprisco_infoamb.salvar', 
        name='s2240_altexprisco_infoamb_salvar'),



url(r'^s2240-altexprisco-fatrisco/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_altexprisco_fatrisco.apagar', 
        name='s2240_altexprisco_fatrisco_apagar'),

url(r'^s2240-altexprisco-fatrisco/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_altexprisco_fatrisco.listar', 
        name='s2240_altexprisco_fatrisco'),

url(r'^s2240-altexprisco-fatrisco/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_altexprisco_fatrisco.salvar', 
        name='s2240_altexprisco_fatrisco_salvar'),



url(r'^s2240-altexprisco-epc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_altexprisco_epc.apagar', 
        name='s2240_altexprisco_epc_apagar'),

url(r'^s2240-altexprisco-epc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_altexprisco_epc.listar', 
        name='s2240_altexprisco_epc'),

url(r'^s2240-altexprisco-epc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_altexprisco_epc.salvar', 
        name='s2240_altexprisco_epc_salvar'),



url(r'^s2240-altexprisco-epi/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_altexprisco_epi.apagar', 
        name='s2240_altexprisco_epi_apagar'),

url(r'^s2240-altexprisco-epi/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_altexprisco_epi.listar', 
        name='s2240_altexprisco_epi'),

url(r'^s2240-altexprisco-epi/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_altexprisco_epi.salvar', 
        name='s2240_altexprisco_epi_salvar'),

)


urlpatterns += patterns('',


url(r'^s2240-fimexprisco/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_fimexprisco.apagar', 
        name='s2240_fimexprisco_apagar'),

url(r'^s2240-fimexprisco/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_fimexprisco.listar', 
        name='s2240_fimexprisco'),

url(r'^s2240-fimexprisco/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_fimexprisco.salvar', 
        name='s2240_fimexprisco_salvar'),



url(r'^s2240-fimexprisco-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_fimexprisco_infoamb.apagar', 
        name='s2240_fimexprisco_infoamb_apagar'),

url(r'^s2240-fimexprisco-infoamb/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_fimexprisco_infoamb.listar', 
        name='s2240_fimexprisco_infoamb'),

url(r'^s2240-fimexprisco-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_fimexprisco_infoamb.salvar', 
        name='s2240_fimexprisco_infoamb_salvar'),



url(r'^s2240-fimexprisco-respreg/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_fimexprisco_respreg.apagar', 
        name='s2240_fimexprisco_respreg_apagar'),

url(r'^s2240-fimexprisco-respreg/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_fimexprisco_respreg.listar', 
        name='s2240_fimexprisco_respreg'),

url(r'^s2240-fimexprisco-respreg/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2240.views.s2240_fimexprisco_respreg.salvar', 
        name='s2240_fimexprisco_respreg_salvar'),





)