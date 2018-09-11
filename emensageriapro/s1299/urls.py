#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1299-iderespinf/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1299.views.s1299_iderespinf.apagar', 
        name='s1299_iderespinf_apagar'),

url(r'^s1299-iderespinf/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1299.views.s1299_iderespinf.listar', 
        name='s1299_iderespinf'),

url(r'^s1299-iderespinf/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1299.views.s1299_iderespinf.salvar', 
        name='s1299_iderespinf_salvar'),





)