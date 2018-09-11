#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1207-dmdev/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1207.views.s1207_dmdev.apagar', 
        name='s1207_dmdev_apagar'),

url(r'^s1207-dmdev/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1207.views.s1207_dmdev.listar', 
        name='s1207_dmdev'),

url(r'^s1207-dmdev/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1207.views.s1207_dmdev.salvar', 
        name='s1207_dmdev_salvar'),



url(r'^s1207-itens/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1207.views.s1207_itens.apagar', 
        name='s1207_itens_apagar'),

url(r'^s1207-itens/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1207.views.s1207_itens.listar', 
        name='s1207_itens'),

url(r'^s1207-itens/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1207.views.s1207_itens.salvar', 
        name='s1207_itens_salvar'),





)