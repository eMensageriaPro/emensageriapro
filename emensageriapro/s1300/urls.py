#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1300-contribsind/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1300.views.s1300_contribsind.apagar', 
        name='s1300_contribsind_apagar'),

url(r'^s1300-contribsind/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1300.views.s1300_contribsind.listar', 
        name='s1300_contribsind'),

url(r'^s1300-contribsind/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1300.views.s1300_contribsind.salvar', 
        name='s1300_contribsind_salvar'),





)