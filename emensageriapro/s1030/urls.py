#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1030.views import s1030_inclusao as s1030_inclusao_views
from emensageriapro.s1030.views import s1030_inclusao_cargopublico as s1030_inclusao_cargopublico_views
from emensageriapro.s1030.views import s1030_alteracao as s1030_alteracao_views
from emensageriapro.s1030.views import s1030_alteracao_cargopublico as s1030_alteracao_cargopublico_views
from emensageriapro.s1030.views import s1030_alteracao_novavalidade as s1030_alteracao_novavalidade_views
from emensageriapro.s1030.views import s1030_exclusao as s1030_exclusao_views





urlpatterns = [



url(r'^s1030-inclusao/apagar/(?P<hash>.*)/$', 
        s1030_inclusao_views.apagar, 
        name='s1030_inclusao_apagar'),

url(r'^s1030-inclusao/api/$',
            s1030_inclusao_views.s1030inclusaoList.as_view() ),

        url(r'^s1030-inclusao/api/(?P<pk>[0-9]+)/$',
            s1030_inclusao_views.s1030inclusaoDetail.as_view() ),

url(r'^s1030-inclusao/listar/(?P<hash>.*)/$', 
        s1030_inclusao_views.listar, 
        name='s1030_inclusao'),

url(r'^s1030-inclusao/salvar/(?P<hash>.*)/$', 
        s1030_inclusao_views.salvar, 
        name='s1030_inclusao_salvar'),



url(r'^s1030-inclusao-cargopublico/apagar/(?P<hash>.*)/$', 
        s1030_inclusao_cargopublico_views.apagar, 
        name='s1030_inclusao_cargopublico_apagar'),

url(r'^s1030-inclusao-cargopublico/api/$',
            s1030_inclusao_cargopublico_views.s1030inclusaocargoPublicoList.as_view() ),

        url(r'^s1030-inclusao-cargopublico/api/(?P<pk>[0-9]+)/$',
            s1030_inclusao_cargopublico_views.s1030inclusaocargoPublicoDetail.as_view() ),

url(r'^s1030-inclusao-cargopublico/listar/(?P<hash>.*)/$', 
        s1030_inclusao_cargopublico_views.listar, 
        name='s1030_inclusao_cargopublico'),

url(r'^s1030-inclusao-cargopublico/salvar/(?P<hash>.*)/$', 
        s1030_inclusao_cargopublico_views.salvar, 
        name='s1030_inclusao_cargopublico_salvar'),



url(r'^s1030-alteracao/apagar/(?P<hash>.*)/$', 
        s1030_alteracao_views.apagar, 
        name='s1030_alteracao_apagar'),

url(r'^s1030-alteracao/api/$',
            s1030_alteracao_views.s1030alteracaoList.as_view() ),

        url(r'^s1030-alteracao/api/(?P<pk>[0-9]+)/$',
            s1030_alteracao_views.s1030alteracaoDetail.as_view() ),

url(r'^s1030-alteracao/listar/(?P<hash>.*)/$', 
        s1030_alteracao_views.listar, 
        name='s1030_alteracao'),

url(r'^s1030-alteracao/salvar/(?P<hash>.*)/$', 
        s1030_alteracao_views.salvar, 
        name='s1030_alteracao_salvar'),



url(r'^s1030-alteracao-cargopublico/apagar/(?P<hash>.*)/$', 
        s1030_alteracao_cargopublico_views.apagar, 
        name='s1030_alteracao_cargopublico_apagar'),

url(r'^s1030-alteracao-cargopublico/api/$',
            s1030_alteracao_cargopublico_views.s1030alteracaocargoPublicoList.as_view() ),

        url(r'^s1030-alteracao-cargopublico/api/(?P<pk>[0-9]+)/$',
            s1030_alteracao_cargopublico_views.s1030alteracaocargoPublicoDetail.as_view() ),

url(r'^s1030-alteracao-cargopublico/listar/(?P<hash>.*)/$', 
        s1030_alteracao_cargopublico_views.listar, 
        name='s1030_alteracao_cargopublico'),

url(r'^s1030-alteracao-cargopublico/salvar/(?P<hash>.*)/$', 
        s1030_alteracao_cargopublico_views.salvar, 
        name='s1030_alteracao_cargopublico_salvar'),



url(r'^s1030-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        s1030_alteracao_novavalidade_views.apagar, 
        name='s1030_alteracao_novavalidade_apagar'),

url(r'^s1030-alteracao-novavalidade/api/$',
            s1030_alteracao_novavalidade_views.s1030alteracaonovaValidadeList.as_view() ),

        url(r'^s1030-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
            s1030_alteracao_novavalidade_views.s1030alteracaonovaValidadeDetail.as_view() ),

url(r'^s1030-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        s1030_alteracao_novavalidade_views.listar, 
        name='s1030_alteracao_novavalidade'),

url(r'^s1030-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        s1030_alteracao_novavalidade_views.salvar, 
        name='s1030_alteracao_novavalidade_salvar'),



url(r'^s1030-exclusao/apagar/(?P<hash>.*)/$', 
        s1030_exclusao_views.apagar, 
        name='s1030_exclusao_apagar'),

url(r'^s1030-exclusao/api/$',
            s1030_exclusao_views.s1030exclusaoList.as_view() ),

        url(r'^s1030-exclusao/api/(?P<pk>[0-9]+)/$',
            s1030_exclusao_views.s1030exclusaoDetail.as_view() ),

url(r'^s1030-exclusao/listar/(?P<hash>.*)/$', 
        s1030_exclusao_views.listar, 
        name='s1030_exclusao'),

url(r'^s1030-exclusao/salvar/(?P<hash>.*)/$', 
        s1030_exclusao_views.salvar, 
        name='s1030_exclusao_salvar'),





]