#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^r2010-nfs/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2010.views.r2010_nfs.apagar', 
        name='r2010_nfs_apagar'),

url(r'^r2010-nfs/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2010.views.r2010_nfs.listar', 
        name='r2010_nfs'),

url(r'^r2010-nfs/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2010.views.r2010_nfs.salvar', 
        name='r2010_nfs_salvar'),



url(r'^r2010-infotpserv/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2010.views.r2010_infotpserv.apagar', 
        name='r2010_infotpserv_apagar'),

url(r'^r2010-infotpserv/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2010.views.r2010_infotpserv.listar', 
        name='r2010_infotpserv'),

url(r'^r2010-infotpserv/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2010.views.r2010_infotpserv.salvar', 
        name='r2010_infotpserv_salvar'),



url(r'^r2010-infoprocretpr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2010.views.r2010_infoprocretpr.apagar', 
        name='r2010_infoprocretpr_apagar'),

url(r'^r2010-infoprocretpr/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2010.views.r2010_infoprocretpr.listar', 
        name='r2010_infoprocretpr'),

url(r'^r2010-infoprocretpr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2010.views.r2010_infoprocretpr.salvar', 
        name='r2010_infoprocretpr_salvar'),



url(r'^r2010-infoprocretad/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2010.views.r2010_infoprocretad.apagar', 
        name='r2010_infoprocretad_apagar'),

url(r'^r2010-infoprocretad/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2010.views.r2010_infoprocretad.listar', 
        name='r2010_infoprocretad'),

url(r'^r2010-infoprocretad/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2010.views.r2010_infoprocretad.salvar', 
        name='r2010_infoprocretad_salvar'),





)