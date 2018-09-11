#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1270-remunavnp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1270.views.s1270_remunavnp.apagar', 
        name='s1270_remunavnp_apagar'),

url(r'^s1270-remunavnp/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1270.views.s1270_remunavnp.listar', 
        name='s1270_remunavnp'),

url(r'^s1270-remunavnp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1270.views.s1270_remunavnp.salvar', 
        name='s1270_remunavnp_salvar'),





)