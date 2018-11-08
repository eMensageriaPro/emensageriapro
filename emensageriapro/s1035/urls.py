#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1035.views import s1035_inclusao as s1035_inclusao_views
from emensageriapro.s1035.views import s1035_alteracao as s1035_alteracao_views
from emensageriapro.s1035.views import s1035_alteracao_novavalidade as s1035_alteracao_novavalidade_views
from emensageriapro.s1035.views import s1035_exclusao as s1035_exclusao_views





urlpatterns = [



url(r'^s1035-inclusao/apagar/(?P<hash>.*)/$', 
        s1035_inclusao_views.apagar, 
        name='s1035_inclusao_apagar'),

url(r'^s1035-inclusao/api/$',
            s1035_inclusao_views.s1035inclusaoList.as_view() ),

        url(r'^s1035-inclusao/api/(?P<pk>[0-9]+)/$',
            s1035_inclusao_views.s1035inclusaoDetail.as_view() ),

url(r'^s1035-inclusao/listar/(?P<hash>.*)/$', 
        s1035_inclusao_views.listar, 
        name='s1035_inclusao'),

url(r'^s1035-inclusao/salvar/(?P<hash>.*)/$', 
        s1035_inclusao_views.salvar, 
        name='s1035_inclusao_salvar'),



url(r'^s1035-alteracao/apagar/(?P<hash>.*)/$', 
        s1035_alteracao_views.apagar, 
        name='s1035_alteracao_apagar'),

url(r'^s1035-alteracao/api/$',
            s1035_alteracao_views.s1035alteracaoList.as_view() ),

        url(r'^s1035-alteracao/api/(?P<pk>[0-9]+)/$',
            s1035_alteracao_views.s1035alteracaoDetail.as_view() ),

url(r'^s1035-alteracao/listar/(?P<hash>.*)/$', 
        s1035_alteracao_views.listar, 
        name='s1035_alteracao'),

url(r'^s1035-alteracao/salvar/(?P<hash>.*)/$', 
        s1035_alteracao_views.salvar, 
        name='s1035_alteracao_salvar'),



url(r'^s1035-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        s1035_alteracao_novavalidade_views.apagar, 
        name='s1035_alteracao_novavalidade_apagar'),

url(r'^s1035-alteracao-novavalidade/api/$',
            s1035_alteracao_novavalidade_views.s1035alteracaonovaValidadeList.as_view() ),

        url(r'^s1035-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
            s1035_alteracao_novavalidade_views.s1035alteracaonovaValidadeDetail.as_view() ),

url(r'^s1035-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        s1035_alteracao_novavalidade_views.listar, 
        name='s1035_alteracao_novavalidade'),

url(r'^s1035-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        s1035_alteracao_novavalidade_views.salvar, 
        name='s1035_alteracao_novavalidade_salvar'),



url(r'^s1035-exclusao/apagar/(?P<hash>.*)/$', 
        s1035_exclusao_views.apagar, 
        name='s1035_exclusao_apagar'),

url(r'^s1035-exclusao/api/$',
            s1035_exclusao_views.s1035exclusaoList.as_view() ),

        url(r'^s1035-exclusao/api/(?P<pk>[0-9]+)/$',
            s1035_exclusao_views.s1035exclusaoDetail.as_view() ),

url(r'^s1035-exclusao/listar/(?P<hash>.*)/$', 
        s1035_exclusao_views.listar, 
        name='s1035_exclusao'),

url(r'^s1035-exclusao/salvar/(?P<hash>.*)/$', 
        s1035_exclusao_views.salvar, 
        name='s1035_exclusao_salvar'),





]