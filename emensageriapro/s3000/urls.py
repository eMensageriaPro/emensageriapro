#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s3000-idetrabalhador/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s3000.views.s3000_idetrabalhador.apagar', 
        name='s3000_idetrabalhador_apagar'),

url(r'^s3000-idetrabalhador/listar/(?P<hash>.*)/$', 
        'emensageriapro.s3000.views.s3000_idetrabalhador.listar', 
        name='s3000_idetrabalhador'),

url(r'^s3000-idetrabalhador/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s3000.views.s3000_idetrabalhador.salvar', 
        name='s3000_idetrabalhador_salvar'),



url(r'^s3000-idefolhapagto/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s3000.views.s3000_idefolhapagto.apagar', 
        name='s3000_idefolhapagto_apagar'),

url(r'^s3000-idefolhapagto/listar/(?P<hash>.*)/$', 
        'emensageriapro.s3000.views.s3000_idefolhapagto.listar', 
        name='s3000_idefolhapagto'),

url(r'^s3000-idefolhapagto/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s3000.views.s3000_idefolhapagto.salvar', 
        name='s3000_idefolhapagto_salvar'),





)