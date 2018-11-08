#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1080.views import s1080_inclusao as s1080_inclusao_views
from emensageriapro.s1080.views import s1080_alteracao as s1080_alteracao_views
from emensageriapro.s1080.views import s1080_alteracao_novavalidade as s1080_alteracao_novavalidade_views
from emensageriapro.s1080.views import s1080_exclusao as s1080_exclusao_views





urlpatterns = [



url(r'^s1080-inclusao/apagar/(?P<hash>.*)/$', 
        s1080_inclusao_views.apagar, 
        name='s1080_inclusao_apagar'),

url(r'^s1080-inclusao/api/$',
            s1080_inclusao_views.s1080inclusaoList.as_view() ),

        url(r'^s1080-inclusao/api/(?P<pk>[0-9]+)/$',
            s1080_inclusao_views.s1080inclusaoDetail.as_view() ),

url(r'^s1080-inclusao/listar/(?P<hash>.*)/$', 
        s1080_inclusao_views.listar, 
        name='s1080_inclusao'),

url(r'^s1080-inclusao/salvar/(?P<hash>.*)/$', 
        s1080_inclusao_views.salvar, 
        name='s1080_inclusao_salvar'),



url(r'^s1080-alteracao/apagar/(?P<hash>.*)/$', 
        s1080_alteracao_views.apagar, 
        name='s1080_alteracao_apagar'),

url(r'^s1080-alteracao/api/$',
            s1080_alteracao_views.s1080alteracaoList.as_view() ),

        url(r'^s1080-alteracao/api/(?P<pk>[0-9]+)/$',
            s1080_alteracao_views.s1080alteracaoDetail.as_view() ),

url(r'^s1080-alteracao/listar/(?P<hash>.*)/$', 
        s1080_alteracao_views.listar, 
        name='s1080_alteracao'),

url(r'^s1080-alteracao/salvar/(?P<hash>.*)/$', 
        s1080_alteracao_views.salvar, 
        name='s1080_alteracao_salvar'),



url(r'^s1080-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        s1080_alteracao_novavalidade_views.apagar, 
        name='s1080_alteracao_novavalidade_apagar'),

url(r'^s1080-alteracao-novavalidade/api/$',
            s1080_alteracao_novavalidade_views.s1080alteracaonovaValidadeList.as_view() ),

        url(r'^s1080-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
            s1080_alteracao_novavalidade_views.s1080alteracaonovaValidadeDetail.as_view() ),

url(r'^s1080-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        s1080_alteracao_novavalidade_views.listar, 
        name='s1080_alteracao_novavalidade'),

url(r'^s1080-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        s1080_alteracao_novavalidade_views.salvar, 
        name='s1080_alteracao_novavalidade_salvar'),



url(r'^s1080-exclusao/apagar/(?P<hash>.*)/$', 
        s1080_exclusao_views.apagar, 
        name='s1080_exclusao_apagar'),

url(r'^s1080-exclusao/api/$',
            s1080_exclusao_views.s1080exclusaoList.as_view() ),

        url(r'^s1080-exclusao/api/(?P<pk>[0-9]+)/$',
            s1080_exclusao_views.s1080exclusaoDetail.as_view() ),

url(r'^s1080-exclusao/listar/(?P<hash>.*)/$', 
        s1080_exclusao_views.listar, 
        name='s1080_exclusao'),

url(r'^s1080-exclusao/salvar/(?P<hash>.*)/$', 
        s1080_exclusao_views.salvar, 
        name='s1080_exclusao_salvar'),





]