#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1065.views import s1065_inclusao as s1065_inclusao_views
from emensageriapro.s1065.views import s1065_alteracao as s1065_alteracao_views
from emensageriapro.s1065.views import s1065_alteracao_novavalidade as s1065_alteracao_novavalidade_views
from emensageriapro.s1065.views import s1065_exclusao as s1065_exclusao_views





urlpatterns = [



url(r'^s1065-inclusao/apagar/(?P<hash>.*)/$', 
        s1065_inclusao_views.apagar, 
        name='s1065_inclusao_apagar'),

url(r'^s1065-inclusao/api/$',
            s1065_inclusao_views.s1065inclusaoList.as_view() ),

        url(r'^s1065-inclusao/api/(?P<pk>[0-9]+)/$',
            s1065_inclusao_views.s1065inclusaoDetail.as_view() ),

url(r'^s1065-inclusao/listar/(?P<hash>.*)/$', 
        s1065_inclusao_views.listar, 
        name='s1065_inclusao'),

url(r'^s1065-inclusao/salvar/(?P<hash>.*)/$', 
        s1065_inclusao_views.salvar, 
        name='s1065_inclusao_salvar'),



url(r'^s1065-alteracao/apagar/(?P<hash>.*)/$', 
        s1065_alteracao_views.apagar, 
        name='s1065_alteracao_apagar'),

url(r'^s1065-alteracao/api/$',
            s1065_alteracao_views.s1065alteracaoList.as_view() ),

        url(r'^s1065-alteracao/api/(?P<pk>[0-9]+)/$',
            s1065_alteracao_views.s1065alteracaoDetail.as_view() ),

url(r'^s1065-alteracao/listar/(?P<hash>.*)/$', 
        s1065_alteracao_views.listar, 
        name='s1065_alteracao'),

url(r'^s1065-alteracao/salvar/(?P<hash>.*)/$', 
        s1065_alteracao_views.salvar, 
        name='s1065_alteracao_salvar'),



url(r'^s1065-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        s1065_alteracao_novavalidade_views.apagar, 
        name='s1065_alteracao_novavalidade_apagar'),

url(r'^s1065-alteracao-novavalidade/api/$',
            s1065_alteracao_novavalidade_views.s1065alteracaonovaValidadeList.as_view() ),

        url(r'^s1065-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
            s1065_alteracao_novavalidade_views.s1065alteracaonovaValidadeDetail.as_view() ),

url(r'^s1065-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        s1065_alteracao_novavalidade_views.listar, 
        name='s1065_alteracao_novavalidade'),

url(r'^s1065-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        s1065_alteracao_novavalidade_views.salvar, 
        name='s1065_alteracao_novavalidade_salvar'),



url(r'^s1065-exclusao/apagar/(?P<hash>.*)/$', 
        s1065_exclusao_views.apagar, 
        name='s1065_exclusao_apagar'),

url(r'^s1065-exclusao/api/$',
            s1065_exclusao_views.s1065exclusaoList.as_view() ),

        url(r'^s1065-exclusao/api/(?P<pk>[0-9]+)/$',
            s1065_exclusao_views.s1065exclusaoDetail.as_view() ),

url(r'^s1065-exclusao/listar/(?P<hash>.*)/$', 
        s1065_exclusao_views.listar, 
        name='s1065_exclusao'),

url(r'^s1065-exclusao/salvar/(?P<hash>.*)/$', 
        s1065_exclusao_views.salvar, 
        name='s1065_exclusao_salvar'),





]