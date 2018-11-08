#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1060.views import s1060_inclusao as s1060_inclusao_views
from emensageriapro.s1060.views import s1060_alteracao as s1060_alteracao_views
from emensageriapro.s1060.views import s1060_alteracao_novavalidade as s1060_alteracao_novavalidade_views
from emensageriapro.s1060.views import s1060_exclusao as s1060_exclusao_views





urlpatterns = [



url(r'^s1060-inclusao/apagar/(?P<hash>.*)/$', 
        s1060_inclusao_views.apagar, 
        name='s1060_inclusao_apagar'),

url(r'^s1060-inclusao/api/$',
            s1060_inclusao_views.s1060inclusaoList.as_view() ),

        url(r'^s1060-inclusao/api/(?P<pk>[0-9]+)/$',
            s1060_inclusao_views.s1060inclusaoDetail.as_view() ),

url(r'^s1060-inclusao/listar/(?P<hash>.*)/$', 
        s1060_inclusao_views.listar, 
        name='s1060_inclusao'),

url(r'^s1060-inclusao/salvar/(?P<hash>.*)/$', 
        s1060_inclusao_views.salvar, 
        name='s1060_inclusao_salvar'),



url(r'^s1060-alteracao/apagar/(?P<hash>.*)/$', 
        s1060_alteracao_views.apagar, 
        name='s1060_alteracao_apagar'),

url(r'^s1060-alteracao/api/$',
            s1060_alteracao_views.s1060alteracaoList.as_view() ),

        url(r'^s1060-alteracao/api/(?P<pk>[0-9]+)/$',
            s1060_alteracao_views.s1060alteracaoDetail.as_view() ),

url(r'^s1060-alteracao/listar/(?P<hash>.*)/$', 
        s1060_alteracao_views.listar, 
        name='s1060_alteracao'),

url(r'^s1060-alteracao/salvar/(?P<hash>.*)/$', 
        s1060_alteracao_views.salvar, 
        name='s1060_alteracao_salvar'),



url(r'^s1060-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        s1060_alteracao_novavalidade_views.apagar, 
        name='s1060_alteracao_novavalidade_apagar'),

url(r'^s1060-alteracao-novavalidade/api/$',
            s1060_alteracao_novavalidade_views.s1060alteracaonovaValidadeList.as_view() ),

        url(r'^s1060-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
            s1060_alteracao_novavalidade_views.s1060alteracaonovaValidadeDetail.as_view() ),

url(r'^s1060-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        s1060_alteracao_novavalidade_views.listar, 
        name='s1060_alteracao_novavalidade'),

url(r'^s1060-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        s1060_alteracao_novavalidade_views.salvar, 
        name='s1060_alteracao_novavalidade_salvar'),



url(r'^s1060-exclusao/apagar/(?P<hash>.*)/$', 
        s1060_exclusao_views.apagar, 
        name='s1060_exclusao_apagar'),

url(r'^s1060-exclusao/api/$',
            s1060_exclusao_views.s1060exclusaoList.as_view() ),

        url(r'^s1060-exclusao/api/(?P<pk>[0-9]+)/$',
            s1060_exclusao_views.s1060exclusaoDetail.as_view() ),

url(r'^s1060-exclusao/listar/(?P<hash>.*)/$', 
        s1060_exclusao_views.listar, 
        name='s1060_exclusao'),

url(r'^s1060-exclusao/salvar/(?P<hash>.*)/$', 
        s1060_exclusao_views.salvar, 
        name='s1060_exclusao_salvar'),





]