#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2231.views import s2231_inicessao as s2231_inicessao_views
from emensageriapro.s2231.views import s2231_fimcessao as s2231_fimcessao_views





urlpatterns = [



url(r'^s2231-inicessao/apagar/(?P<hash>.*)/$', 
        s2231_inicessao_views.apagar, 
        name='s2231_inicessao_apagar'),

url(r'^s2231-inicessao/api/$',
            s2231_inicessao_views.s2231iniCessaoList.as_view() ),

        url(r'^s2231-inicessao/api/(?P<pk>[0-9]+)/$',
            s2231_inicessao_views.s2231iniCessaoDetail.as_view() ),

url(r'^s2231-inicessao/listar/(?P<hash>.*)/$', 
        s2231_inicessao_views.listar, 
        name='s2231_inicessao'),

url(r'^s2231-inicessao/salvar/(?P<hash>.*)/$', 
        s2231_inicessao_views.salvar, 
        name='s2231_inicessao_salvar'),



url(r'^s2231-fimcessao/apagar/(?P<hash>.*)/$', 
        s2231_fimcessao_views.apagar, 
        name='s2231_fimcessao_apagar'),

url(r'^s2231-fimcessao/api/$',
            s2231_fimcessao_views.s2231fimCessaoList.as_view() ),

        url(r'^s2231-fimcessao/api/(?P<pk>[0-9]+)/$',
            s2231_fimcessao_views.s2231fimCessaoDetail.as_view() ),

url(r'^s2231-fimcessao/listar/(?P<hash>.*)/$', 
        s2231_fimcessao_views.listar, 
        name='s2231_fimcessao'),

url(r'^s2231-fimcessao/salvar/(?P<hash>.*)/$', 
        s2231_fimcessao_views.salvar, 
        name='s2231_fimcessao_salvar'),





]