#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2210.views import s2210_idelocalacid as s2210_idelocalacid_views
from emensageriapro.s2210.views import s2210_parteatingida as s2210_parteatingida_views
from emensageriapro.s2210.views import s2210_agentecausador as s2210_agentecausador_views
from emensageriapro.s2210.views import s2210_atestado as s2210_atestado_views
from emensageriapro.s2210.views import s2210_catorigem as s2210_catorigem_views





urlpatterns = [



url(r'^s2210-idelocalacid/apagar/(?P<hash>.*)/$', 
        s2210_idelocalacid_views.apagar, 
        name='s2210_idelocalacid_apagar'),

url(r'^s2210-idelocalacid/api/$',
            s2210_idelocalacid_views.s2210ideLocalAcidList.as_view() ),

        url(r'^s2210-idelocalacid/api/(?P<pk>[0-9]+)/$',
            s2210_idelocalacid_views.s2210ideLocalAcidDetail.as_view() ),

url(r'^s2210-idelocalacid/listar/(?P<hash>.*)/$', 
        s2210_idelocalacid_views.listar, 
        name='s2210_idelocalacid'),

url(r'^s2210-idelocalacid/salvar/(?P<hash>.*)/$', 
        s2210_idelocalacid_views.salvar, 
        name='s2210_idelocalacid_salvar'),



url(r'^s2210-parteatingida/apagar/(?P<hash>.*)/$', 
        s2210_parteatingida_views.apagar, 
        name='s2210_parteatingida_apagar'),

url(r'^s2210-parteatingida/api/$',
            s2210_parteatingida_views.s2210parteAtingidaList.as_view() ),

        url(r'^s2210-parteatingida/api/(?P<pk>[0-9]+)/$',
            s2210_parteatingida_views.s2210parteAtingidaDetail.as_view() ),

url(r'^s2210-parteatingida/listar/(?P<hash>.*)/$', 
        s2210_parteatingida_views.listar, 
        name='s2210_parteatingida'),

url(r'^s2210-parteatingida/salvar/(?P<hash>.*)/$', 
        s2210_parteatingida_views.salvar, 
        name='s2210_parteatingida_salvar'),



url(r'^s2210-agentecausador/apagar/(?P<hash>.*)/$', 
        s2210_agentecausador_views.apagar, 
        name='s2210_agentecausador_apagar'),

url(r'^s2210-agentecausador/api/$',
            s2210_agentecausador_views.s2210agenteCausadorList.as_view() ),

        url(r'^s2210-agentecausador/api/(?P<pk>[0-9]+)/$',
            s2210_agentecausador_views.s2210agenteCausadorDetail.as_view() ),

url(r'^s2210-agentecausador/listar/(?P<hash>.*)/$', 
        s2210_agentecausador_views.listar, 
        name='s2210_agentecausador'),

url(r'^s2210-agentecausador/salvar/(?P<hash>.*)/$', 
        s2210_agentecausador_views.salvar, 
        name='s2210_agentecausador_salvar'),



url(r'^s2210-atestado/apagar/(?P<hash>.*)/$', 
        s2210_atestado_views.apagar, 
        name='s2210_atestado_apagar'),

url(r'^s2210-atestado/api/$',
            s2210_atestado_views.s2210atestadoList.as_view() ),

        url(r'^s2210-atestado/api/(?P<pk>[0-9]+)/$',
            s2210_atestado_views.s2210atestadoDetail.as_view() ),

url(r'^s2210-atestado/listar/(?P<hash>.*)/$', 
        s2210_atestado_views.listar, 
        name='s2210_atestado'),

url(r'^s2210-atestado/salvar/(?P<hash>.*)/$', 
        s2210_atestado_views.salvar, 
        name='s2210_atestado_salvar'),



url(r'^s2210-catorigem/apagar/(?P<hash>.*)/$', 
        s2210_catorigem_views.apagar, 
        name='s2210_catorigem_apagar'),

url(r'^s2210-catorigem/api/$',
            s2210_catorigem_views.s2210catOrigemList.as_view() ),

        url(r'^s2210-catorigem/api/(?P<pk>[0-9]+)/$',
            s2210_catorigem_views.s2210catOrigemDetail.as_view() ),

url(r'^s2210-catorigem/listar/(?P<hash>.*)/$', 
        s2210_catorigem_views.listar, 
        name='s2210_catorigem'),

url(r'^s2210-catorigem/salvar/(?P<hash>.*)/$', 
        s2210_catorigem_views.salvar, 
        name='s2210_catorigem_salvar'),





]