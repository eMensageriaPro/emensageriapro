#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.r1070.views import r1070_inclusao as r1070_inclusao_views
from emensageriapro.r1070.views import r1070_inclusao_infosusp as r1070_inclusao_infosusp_views
from emensageriapro.r1070.views import r1070_inclusao_dadosprocjud as r1070_inclusao_dadosprocjud_views
from emensageriapro.r1070.views import r1070_alteracao as r1070_alteracao_views
from emensageriapro.r1070.views import r1070_alteracao_infosusp as r1070_alteracao_infosusp_views
from emensageriapro.r1070.views import r1070_alteracao_dadosprocjud as r1070_alteracao_dadosprocjud_views
from emensageriapro.r1070.views import r1070_alteracao_novavalidade as r1070_alteracao_novavalidade_views
from emensageriapro.r1070.views import r1070_exclusao as r1070_exclusao_views





urlpatterns = [



url(r'^r1070-inclusao/apagar/(?P<hash>.*)/$', 
        r1070_inclusao_views.apagar, 
        name='r1070_inclusao_apagar'),

url(r'^r1070-inclusao/api/$',
            r1070_inclusao_views.r1070inclusaoList.as_view() ),

        url(r'^r1070-inclusao/api/(?P<pk>[0-9]+)/$',
            r1070_inclusao_views.r1070inclusaoDetail.as_view() ),

url(r'^r1070-inclusao/listar/(?P<hash>.*)/$', 
        r1070_inclusao_views.listar, 
        name='r1070_inclusao'),

url(r'^r1070-inclusao/salvar/(?P<hash>.*)/$', 
        r1070_inclusao_views.salvar, 
        name='r1070_inclusao_salvar'),



url(r'^r1070-inclusao-infosusp/apagar/(?P<hash>.*)/$', 
        r1070_inclusao_infosusp_views.apagar, 
        name='r1070_inclusao_infosusp_apagar'),

url(r'^r1070-inclusao-infosusp/api/$',
            r1070_inclusao_infosusp_views.r1070inclusaoinfoSuspList.as_view() ),

        url(r'^r1070-inclusao-infosusp/api/(?P<pk>[0-9]+)/$',
            r1070_inclusao_infosusp_views.r1070inclusaoinfoSuspDetail.as_view() ),

url(r'^r1070-inclusao-infosusp/listar/(?P<hash>.*)/$', 
        r1070_inclusao_infosusp_views.listar, 
        name='r1070_inclusao_infosusp'),

url(r'^r1070-inclusao-infosusp/salvar/(?P<hash>.*)/$', 
        r1070_inclusao_infosusp_views.salvar, 
        name='r1070_inclusao_infosusp_salvar'),



url(r'^r1070-inclusao-dadosprocjud/apagar/(?P<hash>.*)/$', 
        r1070_inclusao_dadosprocjud_views.apagar, 
        name='r1070_inclusao_dadosprocjud_apagar'),

url(r'^r1070-inclusao-dadosprocjud/api/$',
            r1070_inclusao_dadosprocjud_views.r1070inclusaodadosProcJudList.as_view() ),

        url(r'^r1070-inclusao-dadosprocjud/api/(?P<pk>[0-9]+)/$',
            r1070_inclusao_dadosprocjud_views.r1070inclusaodadosProcJudDetail.as_view() ),

url(r'^r1070-inclusao-dadosprocjud/listar/(?P<hash>.*)/$', 
        r1070_inclusao_dadosprocjud_views.listar, 
        name='r1070_inclusao_dadosprocjud'),

url(r'^r1070-inclusao-dadosprocjud/salvar/(?P<hash>.*)/$', 
        r1070_inclusao_dadosprocjud_views.salvar, 
        name='r1070_inclusao_dadosprocjud_salvar'),



url(r'^r1070-alteracao/apagar/(?P<hash>.*)/$', 
        r1070_alteracao_views.apagar, 
        name='r1070_alteracao_apagar'),

url(r'^r1070-alteracao/api/$',
            r1070_alteracao_views.r1070alteracaoList.as_view() ),

        url(r'^r1070-alteracao/api/(?P<pk>[0-9]+)/$',
            r1070_alteracao_views.r1070alteracaoDetail.as_view() ),

url(r'^r1070-alteracao/listar/(?P<hash>.*)/$', 
        r1070_alteracao_views.listar, 
        name='r1070_alteracao'),

url(r'^r1070-alteracao/salvar/(?P<hash>.*)/$', 
        r1070_alteracao_views.salvar, 
        name='r1070_alteracao_salvar'),



url(r'^r1070-alteracao-infosusp/apagar/(?P<hash>.*)/$', 
        r1070_alteracao_infosusp_views.apagar, 
        name='r1070_alteracao_infosusp_apagar'),

url(r'^r1070-alteracao-infosusp/api/$',
            r1070_alteracao_infosusp_views.r1070alteracaoinfoSuspList.as_view() ),

        url(r'^r1070-alteracao-infosusp/api/(?P<pk>[0-9]+)/$',
            r1070_alteracao_infosusp_views.r1070alteracaoinfoSuspDetail.as_view() ),

url(r'^r1070-alteracao-infosusp/listar/(?P<hash>.*)/$', 
        r1070_alteracao_infosusp_views.listar, 
        name='r1070_alteracao_infosusp'),

url(r'^r1070-alteracao-infosusp/salvar/(?P<hash>.*)/$', 
        r1070_alteracao_infosusp_views.salvar, 
        name='r1070_alteracao_infosusp_salvar'),



url(r'^r1070-alteracao-dadosprocjud/apagar/(?P<hash>.*)/$', 
        r1070_alteracao_dadosprocjud_views.apagar, 
        name='r1070_alteracao_dadosprocjud_apagar'),

url(r'^r1070-alteracao-dadosprocjud/api/$',
            r1070_alteracao_dadosprocjud_views.r1070alteracaodadosProcJudList.as_view() ),

        url(r'^r1070-alteracao-dadosprocjud/api/(?P<pk>[0-9]+)/$',
            r1070_alteracao_dadosprocjud_views.r1070alteracaodadosProcJudDetail.as_view() ),

url(r'^r1070-alteracao-dadosprocjud/listar/(?P<hash>.*)/$', 
        r1070_alteracao_dadosprocjud_views.listar, 
        name='r1070_alteracao_dadosprocjud'),

url(r'^r1070-alteracao-dadosprocjud/salvar/(?P<hash>.*)/$', 
        r1070_alteracao_dadosprocjud_views.salvar, 
        name='r1070_alteracao_dadosprocjud_salvar'),



url(r'^r1070-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        r1070_alteracao_novavalidade_views.apagar, 
        name='r1070_alteracao_novavalidade_apagar'),

url(r'^r1070-alteracao-novavalidade/api/$',
            r1070_alteracao_novavalidade_views.r1070alteracaonovaValidadeList.as_view() ),

        url(r'^r1070-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
            r1070_alteracao_novavalidade_views.r1070alteracaonovaValidadeDetail.as_view() ),

url(r'^r1070-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        r1070_alteracao_novavalidade_views.listar, 
        name='r1070_alteracao_novavalidade'),

url(r'^r1070-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        r1070_alteracao_novavalidade_views.salvar, 
        name='r1070_alteracao_novavalidade_salvar'),



url(r'^r1070-exclusao/apagar/(?P<hash>.*)/$', 
        r1070_exclusao_views.apagar, 
        name='r1070_exclusao_apagar'),

url(r'^r1070-exclusao/api/$',
            r1070_exclusao_views.r1070exclusaoList.as_view() ),

        url(r'^r1070-exclusao/api/(?P<pk>[0-9]+)/$',
            r1070_exclusao_views.r1070exclusaoDetail.as_view() ),

url(r'^r1070-exclusao/listar/(?P<hash>.*)/$', 
        r1070_exclusao_views.listar, 
        name='r1070_exclusao'),

url(r'^r1070-exclusao/salvar/(?P<hash>.*)/$', 
        r1070_exclusao_views.salvar, 
        name='r1070_exclusao_salvar'),





]