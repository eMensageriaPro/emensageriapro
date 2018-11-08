#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1040.views import s1040_inclusao as s1040_inclusao_views
from emensageriapro.s1040.views import s1040_alteracao as s1040_alteracao_views
from emensageriapro.s1040.views import s1040_alteracao_novavalidade as s1040_alteracao_novavalidade_views
from emensageriapro.s1040.views import s1040_exclusao as s1040_exclusao_views





urlpatterns = [



url(r'^s1040-inclusao/apagar/(?P<hash>.*)/$', 
        s1040_inclusao_views.apagar, 
        name='s1040_inclusao_apagar'),

url(r'^s1040-inclusao/api/$',
            s1040_inclusao_views.s1040inclusaoList.as_view() ),

        url(r'^s1040-inclusao/api/(?P<pk>[0-9]+)/$',
            s1040_inclusao_views.s1040inclusaoDetail.as_view() ),

url(r'^s1040-inclusao/listar/(?P<hash>.*)/$', 
        s1040_inclusao_views.listar, 
        name='s1040_inclusao'),

url(r'^s1040-inclusao/salvar/(?P<hash>.*)/$', 
        s1040_inclusao_views.salvar, 
        name='s1040_inclusao_salvar'),



url(r'^s1040-alteracao/apagar/(?P<hash>.*)/$', 
        s1040_alteracao_views.apagar, 
        name='s1040_alteracao_apagar'),

url(r'^s1040-alteracao/api/$',
            s1040_alteracao_views.s1040alteracaoList.as_view() ),

        url(r'^s1040-alteracao/api/(?P<pk>[0-9]+)/$',
            s1040_alteracao_views.s1040alteracaoDetail.as_view() ),

url(r'^s1040-alteracao/listar/(?P<hash>.*)/$', 
        s1040_alteracao_views.listar, 
        name='s1040_alteracao'),

url(r'^s1040-alteracao/salvar/(?P<hash>.*)/$', 
        s1040_alteracao_views.salvar, 
        name='s1040_alteracao_salvar'),



url(r'^s1040-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        s1040_alteracao_novavalidade_views.apagar, 
        name='s1040_alteracao_novavalidade_apagar'),

url(r'^s1040-alteracao-novavalidade/api/$',
            s1040_alteracao_novavalidade_views.s1040alteracaonovaValidadeList.as_view() ),

        url(r'^s1040-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
            s1040_alteracao_novavalidade_views.s1040alteracaonovaValidadeDetail.as_view() ),

url(r'^s1040-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        s1040_alteracao_novavalidade_views.listar, 
        name='s1040_alteracao_novavalidade'),

url(r'^s1040-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        s1040_alteracao_novavalidade_views.salvar, 
        name='s1040_alteracao_novavalidade_salvar'),



url(r'^s1040-exclusao/apagar/(?P<hash>.*)/$', 
        s1040_exclusao_views.apagar, 
        name='s1040_exclusao_apagar'),

url(r'^s1040-exclusao/api/$',
            s1040_exclusao_views.s1040exclusaoList.as_view() ),

        url(r'^s1040-exclusao/api/(?P<pk>[0-9]+)/$',
            s1040_exclusao_views.s1040exclusaoDetail.as_view() ),

url(r'^s1040-exclusao/listar/(?P<hash>.*)/$', 
        s1040_exclusao_views.listar, 
        name='s1040_exclusao'),

url(r'^s1040-exclusao/salvar/(?P<hash>.*)/$', 
        s1040_exclusao_views.salvar, 
        name='s1040_exclusao_salvar'),





]