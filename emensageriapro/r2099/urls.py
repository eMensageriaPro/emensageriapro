#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^r2099-iderespinf/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2099.views.r2099_iderespinf.apagar', 
        name='r2099_iderespinf_apagar'),

url(r'^r2099-iderespinf/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2099.views.r2099_iderespinf.listar', 
        name='r2099_iderespinf'),

url(r'^r2099-iderespinf/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2099.views.r2099_iderespinf.salvar', 
        name='r2099_iderespinf_salvar'),





)