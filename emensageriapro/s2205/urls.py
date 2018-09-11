#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s2205-documentos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_documentos.apagar', 
        name='s2205_documentos_apagar'),

url(r'^s2205-documentos/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_documentos.listar', 
        name='s2205_documentos'),

url(r'^s2205-documentos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_documentos.salvar', 
        name='s2205_documentos_salvar'),



url(r'^s2205-ctps/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_ctps.apagar', 
        name='s2205_ctps_apagar'),

url(r'^s2205-ctps/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_ctps.listar', 
        name='s2205_ctps'),

url(r'^s2205-ctps/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_ctps.salvar', 
        name='s2205_ctps_salvar'),



url(r'^s2205-ric/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_ric.apagar', 
        name='s2205_ric_apagar'),

url(r'^s2205-ric/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_ric.listar', 
        name='s2205_ric'),

url(r'^s2205-ric/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_ric.salvar', 
        name='s2205_ric_salvar'),



url(r'^s2205-rg/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_rg.apagar', 
        name='s2205_rg_apagar'),

url(r'^s2205-rg/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_rg.listar', 
        name='s2205_rg'),

url(r'^s2205-rg/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_rg.salvar', 
        name='s2205_rg_salvar'),



url(r'^s2205-rne/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_rne.apagar', 
        name='s2205_rne_apagar'),

url(r'^s2205-rne/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_rne.listar', 
        name='s2205_rne'),

url(r'^s2205-rne/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_rne.salvar', 
        name='s2205_rne_salvar'),



url(r'^s2205-oc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_oc.apagar', 
        name='s2205_oc_apagar'),

url(r'^s2205-oc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_oc.listar', 
        name='s2205_oc'),

url(r'^s2205-oc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_oc.salvar', 
        name='s2205_oc_salvar'),



url(r'^s2205-cnh/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_cnh.apagar', 
        name='s2205_cnh_apagar'),

url(r'^s2205-cnh/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_cnh.listar', 
        name='s2205_cnh'),

url(r'^s2205-cnh/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_cnh.salvar', 
        name='s2205_cnh_salvar'),



url(r'^s2205-brasil/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_brasil.apagar', 
        name='s2205_brasil_apagar'),

url(r'^s2205-brasil/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_brasil.listar', 
        name='s2205_brasil'),

url(r'^s2205-brasil/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_brasil.salvar', 
        name='s2205_brasil_salvar'),



url(r'^s2205-exterior/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_exterior.apagar', 
        name='s2205_exterior_apagar'),

url(r'^s2205-exterior/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_exterior.listar', 
        name='s2205_exterior'),

url(r'^s2205-exterior/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_exterior.salvar', 
        name='s2205_exterior_salvar'),



url(r'^s2205-trabestrangeiro/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_trabestrangeiro.apagar', 
        name='s2205_trabestrangeiro_apagar'),

url(r'^s2205-trabestrangeiro/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_trabestrangeiro.listar', 
        name='s2205_trabestrangeiro'),

url(r'^s2205-trabestrangeiro/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_trabestrangeiro.salvar', 
        name='s2205_trabestrangeiro_salvar'),

)


urlpatterns += patterns('',


url(r'^s2205-infodeficiencia/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_infodeficiencia.apagar', 
        name='s2205_infodeficiencia_apagar'),

url(r'^s2205-infodeficiencia/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_infodeficiencia.listar', 
        name='s2205_infodeficiencia'),

url(r'^s2205-infodeficiencia/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_infodeficiencia.salvar', 
        name='s2205_infodeficiencia_salvar'),



url(r'^s2205-dependente/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_dependente.apagar', 
        name='s2205_dependente_apagar'),

url(r'^s2205-dependente/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_dependente.listar', 
        name='s2205_dependente'),

url(r'^s2205-dependente/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_dependente.salvar', 
        name='s2205_dependente_salvar'),



url(r'^s2205-aposentadoria/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_aposentadoria.apagar', 
        name='s2205_aposentadoria_apagar'),

url(r'^s2205-aposentadoria/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_aposentadoria.listar', 
        name='s2205_aposentadoria'),

url(r'^s2205-aposentadoria/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_aposentadoria.salvar', 
        name='s2205_aposentadoria_salvar'),



url(r'^s2205-contato/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_contato.apagar', 
        name='s2205_contato_apagar'),

url(r'^s2205-contato/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_contato.listar', 
        name='s2205_contato'),

url(r'^s2205-contato/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2205.views.s2205_contato.salvar', 
        name='s2205_contato_salvar'),





)