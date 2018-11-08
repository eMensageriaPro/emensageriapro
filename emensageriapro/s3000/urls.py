#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s3000.views import s3000_idetrabalhador as s3000_idetrabalhador_views
from emensageriapro.s3000.views import s3000_idefolhapagto as s3000_idefolhapagto_views





urlpatterns = [



url(r'^s3000-idetrabalhador/apagar/(?P<hash>.*)/$', 
        s3000_idetrabalhador_views.apagar, 
        name='s3000_idetrabalhador_apagar'),

url(r'^s3000-idetrabalhador/api/$',
            s3000_idetrabalhador_views.s3000ideTrabalhadorList.as_view() ),

        url(r'^s3000-idetrabalhador/api/(?P<pk>[0-9]+)/$',
            s3000_idetrabalhador_views.s3000ideTrabalhadorDetail.as_view() ),

url(r'^s3000-idetrabalhador/listar/(?P<hash>.*)/$', 
        s3000_idetrabalhador_views.listar, 
        name='s3000_idetrabalhador'),

url(r'^s3000-idetrabalhador/salvar/(?P<hash>.*)/$', 
        s3000_idetrabalhador_views.salvar, 
        name='s3000_idetrabalhador_salvar'),



url(r'^s3000-idefolhapagto/apagar/(?P<hash>.*)/$', 
        s3000_idefolhapagto_views.apagar, 
        name='s3000_idefolhapagto_apagar'),

url(r'^s3000-idefolhapagto/api/$',
            s3000_idefolhapagto_views.s3000ideFolhaPagtoList.as_view() ),

        url(r'^s3000-idefolhapagto/api/(?P<pk>[0-9]+)/$',
            s3000_idefolhapagto_views.s3000ideFolhaPagtoDetail.as_view() ),

url(r'^s3000-idefolhapagto/listar/(?P<hash>.*)/$', 
        s3000_idefolhapagto_views.listar, 
        name='s3000_idefolhapagto'),

url(r'^s3000-idefolhapagto/salvar/(?P<hash>.*)/$', 
        s3000_idefolhapagto_views.salvar, 
        name='s3000_idefolhapagto_salvar'),





]