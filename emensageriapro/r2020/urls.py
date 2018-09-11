#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^r2020-nfs/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_nfs.apagar', 
        name='r2020_nfs_apagar'),

url(r'^r2020-nfs/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_nfs.listar', 
        name='r2020_nfs'),

url(r'^r2020-nfs/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_nfs.salvar', 
        name='r2020_nfs_salvar'),



url(r'^r2020-infotpserv/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infotpserv.apagar', 
        name='r2020_infotpserv_apagar'),

url(r'^r2020-infotpserv/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infotpserv.listar', 
        name='r2020_infotpserv'),

url(r'^r2020-infotpserv/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infotpserv.salvar', 
        name='r2020_infotpserv_salvar'),



url(r'^r2020-infoprocretpr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infoprocretpr.apagar', 
        name='r2020_infoprocretpr_apagar'),

url(r'^r2020-infoprocretpr/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infoprocretpr.listar', 
        name='r2020_infoprocretpr'),

url(r'^r2020-infoprocretpr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infoprocretpr.salvar', 
        name='r2020_infoprocretpr_salvar'),



url(r'^r2020-infoprocretad/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infoprocretad.apagar', 
        name='r2020_infoprocretad_apagar'),

url(r'^r2020-infoprocretad/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infoprocretad.listar', 
        name='r2020_infoprocretad'),

url(r'^r2020-infoprocretad/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infoprocretad.salvar', 
        name='r2020_infoprocretad_salvar'),





)