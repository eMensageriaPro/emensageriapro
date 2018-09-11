#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1250-tpaquis/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_tpaquis.apagar', 
        name='s1250_tpaquis_apagar'),

url(r'^s1250-tpaquis/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_tpaquis.listar', 
        name='s1250_tpaquis'),

url(r'^s1250-tpaquis/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_tpaquis.salvar', 
        name='s1250_tpaquis_salvar'),



url(r'^s1250-ideprodutor/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_ideprodutor.apagar', 
        name='s1250_ideprodutor_apagar'),

url(r'^s1250-ideprodutor/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_ideprodutor.listar', 
        name='s1250_ideprodutor'),

url(r'^s1250-ideprodutor/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_ideprodutor.salvar', 
        name='s1250_ideprodutor_salvar'),



url(r'^s1250-nfs/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_nfs.apagar', 
        name='s1250_nfs_apagar'),

url(r'^s1250-nfs/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_nfs.listar', 
        name='s1250_nfs'),

url(r'^s1250-nfs/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_nfs.salvar', 
        name='s1250_nfs_salvar'),



url(r'^s1250-infoprocjud/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_infoprocjud.apagar', 
        name='s1250_infoprocjud_apagar'),

url(r'^s1250-infoprocjud/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_infoprocjud.listar', 
        name='s1250_infoprocjud'),

url(r'^s1250-infoprocjud/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_infoprocjud.salvar', 
        name='s1250_infoprocjud_salvar'),





)