#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s2260-localtrabinterm/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2260.views.s2260_localtrabinterm.apagar', 
        name='s2260_localtrabinterm_apagar'),

url(r'^s2260-localtrabinterm/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2260.views.s2260_localtrabinterm.listar', 
        name='s2260_localtrabinterm'),

url(r'^s2260-localtrabinterm/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2260.views.s2260_localtrabinterm.salvar', 
        name='s2260_localtrabinterm_salvar'),





)