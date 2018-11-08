#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2400.views import s2400_endereco as s2400_endereco_views
from emensageriapro.s2400.views import s2400_brasil as s2400_brasil_views
from emensageriapro.s2400.views import s2400_exterior as s2400_exterior_views
from emensageriapro.s2400.views import s2400_dependente as s2400_dependente_views





urlpatterns = [



url(r'^s2400-endereco/apagar/(?P<hash>.*)/$', 
        s2400_endereco_views.apagar, 
        name='s2400_endereco_apagar'),

url(r'^s2400-endereco/api/$',
            s2400_endereco_views.s2400enderecoList.as_view() ),

        url(r'^s2400-endereco/api/(?P<pk>[0-9]+)/$',
            s2400_endereco_views.s2400enderecoDetail.as_view() ),

url(r'^s2400-endereco/listar/(?P<hash>.*)/$', 
        s2400_endereco_views.listar, 
        name='s2400_endereco'),

url(r'^s2400-endereco/salvar/(?P<hash>.*)/$', 
        s2400_endereco_views.salvar, 
        name='s2400_endereco_salvar'),



url(r'^s2400-brasil/apagar/(?P<hash>.*)/$', 
        s2400_brasil_views.apagar, 
        name='s2400_brasil_apagar'),

url(r'^s2400-brasil/api/$',
            s2400_brasil_views.s2400brasilList.as_view() ),

        url(r'^s2400-brasil/api/(?P<pk>[0-9]+)/$',
            s2400_brasil_views.s2400brasilDetail.as_view() ),

url(r'^s2400-brasil/listar/(?P<hash>.*)/$', 
        s2400_brasil_views.listar, 
        name='s2400_brasil'),

url(r'^s2400-brasil/salvar/(?P<hash>.*)/$', 
        s2400_brasil_views.salvar, 
        name='s2400_brasil_salvar'),



url(r'^s2400-exterior/apagar/(?P<hash>.*)/$', 
        s2400_exterior_views.apagar, 
        name='s2400_exterior_apagar'),

url(r'^s2400-exterior/api/$',
            s2400_exterior_views.s2400exteriorList.as_view() ),

        url(r'^s2400-exterior/api/(?P<pk>[0-9]+)/$',
            s2400_exterior_views.s2400exteriorDetail.as_view() ),

url(r'^s2400-exterior/listar/(?P<hash>.*)/$', 
        s2400_exterior_views.listar, 
        name='s2400_exterior'),

url(r'^s2400-exterior/salvar/(?P<hash>.*)/$', 
        s2400_exterior_views.salvar, 
        name='s2400_exterior_salvar'),



url(r'^s2400-dependente/apagar/(?P<hash>.*)/$', 
        s2400_dependente_views.apagar, 
        name='s2400_dependente_apagar'),

url(r'^s2400-dependente/api/$',
            s2400_dependente_views.s2400dependenteList.as_view() ),

        url(r'^s2400-dependente/api/(?P<pk>[0-9]+)/$',
            s2400_dependente_views.s2400dependenteDetail.as_view() ),

url(r'^s2400-dependente/listar/(?P<hash>.*)/$', 
        s2400_dependente_views.listar, 
        name='s2400_dependente'),

url(r'^s2400-dependente/salvar/(?P<hash>.*)/$', 
        s2400_dependente_views.salvar, 
        name='s2400_dependente_salvar'),





]