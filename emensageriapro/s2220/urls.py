#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s2220-exame/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2220.views.s2220_exame.apagar', 
        name='s2220_exame_apagar'),

url(r'^s2220-exame/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2220.views.s2220_exame.listar', 
        name='s2220_exame'),

url(r'^s2220-exame/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2220.views.s2220_exame.salvar', 
        name='s2220_exame_salvar'),





)