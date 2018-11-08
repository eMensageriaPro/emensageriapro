#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2405.views import s2405_endereco as s2405_endereco_views
from emensageriapro.s2405.views import s2405_brasil as s2405_brasil_views
from emensageriapro.s2405.views import s2405_exterior as s2405_exterior_views
from emensageriapro.s2405.views import s2405_dependente as s2405_dependente_views





urlpatterns = [



url(r'^s2405-endereco/apagar/(?P<hash>.*)/$', 
        s2405_endereco_views.apagar, 
        name='s2405_endereco_apagar'),

url(r'^s2405-endereco/api/$',
            s2405_endereco_views.s2405enderecoList.as_view() ),

        url(r'^s2405-endereco/api/(?P<pk>[0-9]+)/$',
            s2405_endereco_views.s2405enderecoDetail.as_view() ),

url(r'^s2405-endereco/listar/(?P<hash>.*)/$', 
        s2405_endereco_views.listar, 
        name='s2405_endereco'),

url(r'^s2405-endereco/salvar/(?P<hash>.*)/$', 
        s2405_endereco_views.salvar, 
        name='s2405_endereco_salvar'),



url(r'^s2405-brasil/apagar/(?P<hash>.*)/$', 
        s2405_brasil_views.apagar, 
        name='s2405_brasil_apagar'),

url(r'^s2405-brasil/api/$',
            s2405_brasil_views.s2405brasilList.as_view() ),

        url(r'^s2405-brasil/api/(?P<pk>[0-9]+)/$',
            s2405_brasil_views.s2405brasilDetail.as_view() ),

url(r'^s2405-brasil/listar/(?P<hash>.*)/$', 
        s2405_brasil_views.listar, 
        name='s2405_brasil'),

url(r'^s2405-brasil/salvar/(?P<hash>.*)/$', 
        s2405_brasil_views.salvar, 
        name='s2405_brasil_salvar'),



url(r'^s2405-exterior/apagar/(?P<hash>.*)/$', 
        s2405_exterior_views.apagar, 
        name='s2405_exterior_apagar'),

url(r'^s2405-exterior/api/$',
            s2405_exterior_views.s2405exteriorList.as_view() ),

        url(r'^s2405-exterior/api/(?P<pk>[0-9]+)/$',
            s2405_exterior_views.s2405exteriorDetail.as_view() ),

url(r'^s2405-exterior/listar/(?P<hash>.*)/$', 
        s2405_exterior_views.listar, 
        name='s2405_exterior'),

url(r'^s2405-exterior/salvar/(?P<hash>.*)/$', 
        s2405_exterior_views.salvar, 
        name='s2405_exterior_salvar'),



url(r'^s2405-dependente/apagar/(?P<hash>.*)/$', 
        s2405_dependente_views.apagar, 
        name='s2405_dependente_apagar'),

url(r'^s2405-dependente/api/$',
            s2405_dependente_views.s2405dependenteList.as_view() ),

        url(r'^s2405-dependente/api/(?P<pk>[0-9]+)/$',
            s2405_dependente_views.s2405dependenteDetail.as_view() ),

url(r'^s2405-dependente/listar/(?P<hash>.*)/$', 
        s2405_dependente_views.listar, 
        name='s2405_dependente'),

url(r'^s2405-dependente/salvar/(?P<hash>.*)/$', 
        s2405_dependente_views.salvar, 
        name='s2405_dependente_salvar'),





]