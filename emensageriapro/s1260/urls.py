#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1260-tpcomerc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_tpcomerc.apagar', 
        name='s1260_tpcomerc_apagar'),

url(r'^s1260-tpcomerc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_tpcomerc.listar', 
        name='s1260_tpcomerc'),

url(r'^s1260-tpcomerc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_tpcomerc.salvar', 
        name='s1260_tpcomerc_salvar'),



url(r'^s1260-ideadquir/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_ideadquir.apagar', 
        name='s1260_ideadquir_apagar'),

url(r'^s1260-ideadquir/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_ideadquir.listar', 
        name='s1260_ideadquir'),

url(r'^s1260-ideadquir/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_ideadquir.salvar', 
        name='s1260_ideadquir_salvar'),



url(r'^s1260-nfs/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_nfs.apagar', 
        name='s1260_nfs_apagar'),

url(r'^s1260-nfs/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_nfs.listar', 
        name='s1260_nfs'),

url(r'^s1260-nfs/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_nfs.salvar', 
        name='s1260_nfs_salvar'),



url(r'^s1260-infoprocjud/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_infoprocjud.apagar', 
        name='s1260_infoprocjud_apagar'),

url(r'^s1260-infoprocjud/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_infoprocjud.listar', 
        name='s1260_infoprocjud'),

url(r'^s1260-infoprocjud/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_infoprocjud.salvar', 
        name='s1260_infoprocjud_salvar'),





)