#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s2250-detavprevio/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2250.views.s2250_detavprevio.apagar', 
        name='s2250_detavprevio_apagar'),

url(r'^s2250-detavprevio/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2250.views.s2250_detavprevio.listar', 
        name='s2250_detavprevio'),

url(r'^s2250-detavprevio/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2250.views.s2250_detavprevio.salvar', 
        name='s2250_detavprevio_salvar'),



url(r'^s2250-cancavprevio/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2250.views.s2250_cancavprevio.apagar', 
        name='s2250_cancavprevio_apagar'),

url(r'^s2250-cancavprevio/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2250.views.s2250_cancavprevio.listar', 
        name='s2250_cancavprevio'),

url(r'^s2250-cancavprevio/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2250.views.s2250_cancavprevio.salvar', 
        name='s2250_cancavprevio_salvar'),





)