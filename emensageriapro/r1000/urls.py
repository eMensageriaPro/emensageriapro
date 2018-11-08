#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.r1000.views import r1000_inclusao as r1000_inclusao_views
from emensageriapro.r1000.views import r1000_inclusao_softhouse as r1000_inclusao_softhouse_views
from emensageriapro.r1000.views import r1000_inclusao_infoefr as r1000_inclusao_infoefr_views
from emensageriapro.r1000.views import r1000_alteracao as r1000_alteracao_views
from emensageriapro.r1000.views import r1000_alteracao_softhouse as r1000_alteracao_softhouse_views
from emensageriapro.r1000.views import r1000_alteracao_infoefr as r1000_alteracao_infoefr_views
from emensageriapro.r1000.views import r1000_alteracao_novavalidade as r1000_alteracao_novavalidade_views
from emensageriapro.r1000.views import r1000_exclusao as r1000_exclusao_views





urlpatterns = [



url(r'^r1000-inclusao/apagar/(?P<hash>.*)/$', 
        r1000_inclusao_views.apagar, 
        name='r1000_inclusao_apagar'),

url(r'^r1000-inclusao/api/$',
            r1000_inclusao_views.r1000inclusaoList.as_view() ),

        url(r'^r1000-inclusao/api/(?P<pk>[0-9]+)/$',
            r1000_inclusao_views.r1000inclusaoDetail.as_view() ),

url(r'^r1000-inclusao/listar/(?P<hash>.*)/$', 
        r1000_inclusao_views.listar, 
        name='r1000_inclusao'),

url(r'^r1000-inclusao/salvar/(?P<hash>.*)/$', 
        r1000_inclusao_views.salvar, 
        name='r1000_inclusao_salvar'),



url(r'^r1000-inclusao-softhouse/apagar/(?P<hash>.*)/$', 
        r1000_inclusao_softhouse_views.apagar, 
        name='r1000_inclusao_softhouse_apagar'),

url(r'^r1000-inclusao-softhouse/api/$',
            r1000_inclusao_softhouse_views.r1000inclusaosoftHouseList.as_view() ),

        url(r'^r1000-inclusao-softhouse/api/(?P<pk>[0-9]+)/$',
            r1000_inclusao_softhouse_views.r1000inclusaosoftHouseDetail.as_view() ),

url(r'^r1000-inclusao-softhouse/listar/(?P<hash>.*)/$', 
        r1000_inclusao_softhouse_views.listar, 
        name='r1000_inclusao_softhouse'),

url(r'^r1000-inclusao-softhouse/salvar/(?P<hash>.*)/$', 
        r1000_inclusao_softhouse_views.salvar, 
        name='r1000_inclusao_softhouse_salvar'),



url(r'^r1000-inclusao-infoefr/apagar/(?P<hash>.*)/$', 
        r1000_inclusao_infoefr_views.apagar, 
        name='r1000_inclusao_infoefr_apagar'),

url(r'^r1000-inclusao-infoefr/api/$',
            r1000_inclusao_infoefr_views.r1000inclusaoinfoEFRList.as_view() ),

        url(r'^r1000-inclusao-infoefr/api/(?P<pk>[0-9]+)/$',
            r1000_inclusao_infoefr_views.r1000inclusaoinfoEFRDetail.as_view() ),

url(r'^r1000-inclusao-infoefr/listar/(?P<hash>.*)/$', 
        r1000_inclusao_infoefr_views.listar, 
        name='r1000_inclusao_infoefr'),

url(r'^r1000-inclusao-infoefr/salvar/(?P<hash>.*)/$', 
        r1000_inclusao_infoefr_views.salvar, 
        name='r1000_inclusao_infoefr_salvar'),



url(r'^r1000-alteracao/apagar/(?P<hash>.*)/$', 
        r1000_alteracao_views.apagar, 
        name='r1000_alteracao_apagar'),

url(r'^r1000-alteracao/api/$',
            r1000_alteracao_views.r1000alteracaoList.as_view() ),

        url(r'^r1000-alteracao/api/(?P<pk>[0-9]+)/$',
            r1000_alteracao_views.r1000alteracaoDetail.as_view() ),

url(r'^r1000-alteracao/listar/(?P<hash>.*)/$', 
        r1000_alteracao_views.listar, 
        name='r1000_alteracao'),

url(r'^r1000-alteracao/salvar/(?P<hash>.*)/$', 
        r1000_alteracao_views.salvar, 
        name='r1000_alteracao_salvar'),



url(r'^r1000-alteracao-softhouse/apagar/(?P<hash>.*)/$', 
        r1000_alteracao_softhouse_views.apagar, 
        name='r1000_alteracao_softhouse_apagar'),

url(r'^r1000-alteracao-softhouse/api/$',
            r1000_alteracao_softhouse_views.r1000alteracaosoftHouseList.as_view() ),

        url(r'^r1000-alteracao-softhouse/api/(?P<pk>[0-9]+)/$',
            r1000_alteracao_softhouse_views.r1000alteracaosoftHouseDetail.as_view() ),

url(r'^r1000-alteracao-softhouse/listar/(?P<hash>.*)/$', 
        r1000_alteracao_softhouse_views.listar, 
        name='r1000_alteracao_softhouse'),

url(r'^r1000-alteracao-softhouse/salvar/(?P<hash>.*)/$', 
        r1000_alteracao_softhouse_views.salvar, 
        name='r1000_alteracao_softhouse_salvar'),



url(r'^r1000-alteracao-infoefr/apagar/(?P<hash>.*)/$', 
        r1000_alteracao_infoefr_views.apagar, 
        name='r1000_alteracao_infoefr_apagar'),

url(r'^r1000-alteracao-infoefr/api/$',
            r1000_alteracao_infoefr_views.r1000alteracaoinfoEFRList.as_view() ),

        url(r'^r1000-alteracao-infoefr/api/(?P<pk>[0-9]+)/$',
            r1000_alteracao_infoefr_views.r1000alteracaoinfoEFRDetail.as_view() ),

url(r'^r1000-alteracao-infoefr/listar/(?P<hash>.*)/$', 
        r1000_alteracao_infoefr_views.listar, 
        name='r1000_alteracao_infoefr'),

url(r'^r1000-alteracao-infoefr/salvar/(?P<hash>.*)/$', 
        r1000_alteracao_infoefr_views.salvar, 
        name='r1000_alteracao_infoefr_salvar'),



url(r'^r1000-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        r1000_alteracao_novavalidade_views.apagar, 
        name='r1000_alteracao_novavalidade_apagar'),

url(r'^r1000-alteracao-novavalidade/api/$',
            r1000_alteracao_novavalidade_views.r1000alteracaonovaValidadeList.as_view() ),

        url(r'^r1000-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
            r1000_alteracao_novavalidade_views.r1000alteracaonovaValidadeDetail.as_view() ),

url(r'^r1000-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        r1000_alteracao_novavalidade_views.listar, 
        name='r1000_alteracao_novavalidade'),

url(r'^r1000-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        r1000_alteracao_novavalidade_views.salvar, 
        name='r1000_alteracao_novavalidade_salvar'),



url(r'^r1000-exclusao/apagar/(?P<hash>.*)/$', 
        r1000_exclusao_views.apagar, 
        name='r1000_exclusao_apagar'),

url(r'^r1000-exclusao/api/$',
            r1000_exclusao_views.r1000exclusaoList.as_view() ),

        url(r'^r1000-exclusao/api/(?P<pk>[0-9]+)/$',
            r1000_exclusao_views.r1000exclusaoDetail.as_view() ),

url(r'^r1000-exclusao/listar/(?P<hash>.*)/$', 
        r1000_exclusao_views.listar, 
        name='r1000_exclusao'),

url(r'^r1000-exclusao/salvar/(?P<hash>.*)/$', 
        r1000_exclusao_views.salvar, 
        name='r1000_exclusao_salvar'),





]