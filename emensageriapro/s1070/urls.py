#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1070.views import s1070_inclusao as s1070_inclusao_views
from emensageriapro.s1070.views import s1070_inclusao_dadosprocjud as s1070_inclusao_dadosprocjud_views
from emensageriapro.s1070.views import s1070_inclusao_infosusp as s1070_inclusao_infosusp_views
from emensageriapro.s1070.views import s1070_alteracao as s1070_alteracao_views
from emensageriapro.s1070.views import s1070_alteracao_dadosprocjud as s1070_alteracao_dadosprocjud_views
from emensageriapro.s1070.views import s1070_alteracao_infosusp as s1070_alteracao_infosusp_views
from emensageriapro.s1070.views import s1070_alteracao_novavalidade as s1070_alteracao_novavalidade_views
from emensageriapro.s1070.views import s1070_exclusao as s1070_exclusao_views





urlpatterns = [



url(r'^s1070-inclusao/apagar/(?P<hash>.*)/$', 
        s1070_inclusao_views.apagar, 
        name='s1070_inclusao_apagar'),

url(r'^s1070-inclusao/api/$',
            s1070_inclusao_views.s1070inclusaoList.as_view() ),

        url(r'^s1070-inclusao/api/(?P<pk>[0-9]+)/$',
            s1070_inclusao_views.s1070inclusaoDetail.as_view() ),

url(r'^s1070-inclusao/listar/(?P<hash>.*)/$', 
        s1070_inclusao_views.listar, 
        name='s1070_inclusao'),

url(r'^s1070-inclusao/salvar/(?P<hash>.*)/$', 
        s1070_inclusao_views.salvar, 
        name='s1070_inclusao_salvar'),



url(r'^s1070-inclusao-dadosprocjud/apagar/(?P<hash>.*)/$', 
        s1070_inclusao_dadosprocjud_views.apagar, 
        name='s1070_inclusao_dadosprocjud_apagar'),

url(r'^s1070-inclusao-dadosprocjud/api/$',
            s1070_inclusao_dadosprocjud_views.s1070inclusaodadosProcJudList.as_view() ),

        url(r'^s1070-inclusao-dadosprocjud/api/(?P<pk>[0-9]+)/$',
            s1070_inclusao_dadosprocjud_views.s1070inclusaodadosProcJudDetail.as_view() ),

url(r'^s1070-inclusao-dadosprocjud/listar/(?P<hash>.*)/$', 
        s1070_inclusao_dadosprocjud_views.listar, 
        name='s1070_inclusao_dadosprocjud'),

url(r'^s1070-inclusao-dadosprocjud/salvar/(?P<hash>.*)/$', 
        s1070_inclusao_dadosprocjud_views.salvar, 
        name='s1070_inclusao_dadosprocjud_salvar'),



url(r'^s1070-inclusao-infosusp/apagar/(?P<hash>.*)/$', 
        s1070_inclusao_infosusp_views.apagar, 
        name='s1070_inclusao_infosusp_apagar'),

url(r'^s1070-inclusao-infosusp/api/$',
            s1070_inclusao_infosusp_views.s1070inclusaoinfoSuspList.as_view() ),

        url(r'^s1070-inclusao-infosusp/api/(?P<pk>[0-9]+)/$',
            s1070_inclusao_infosusp_views.s1070inclusaoinfoSuspDetail.as_view() ),

url(r'^s1070-inclusao-infosusp/listar/(?P<hash>.*)/$', 
        s1070_inclusao_infosusp_views.listar, 
        name='s1070_inclusao_infosusp'),

url(r'^s1070-inclusao-infosusp/salvar/(?P<hash>.*)/$', 
        s1070_inclusao_infosusp_views.salvar, 
        name='s1070_inclusao_infosusp_salvar'),



url(r'^s1070-alteracao/apagar/(?P<hash>.*)/$', 
        s1070_alteracao_views.apagar, 
        name='s1070_alteracao_apagar'),

url(r'^s1070-alteracao/api/$',
            s1070_alteracao_views.s1070alteracaoList.as_view() ),

        url(r'^s1070-alteracao/api/(?P<pk>[0-9]+)/$',
            s1070_alteracao_views.s1070alteracaoDetail.as_view() ),

url(r'^s1070-alteracao/listar/(?P<hash>.*)/$', 
        s1070_alteracao_views.listar, 
        name='s1070_alteracao'),

url(r'^s1070-alteracao/salvar/(?P<hash>.*)/$', 
        s1070_alteracao_views.salvar, 
        name='s1070_alteracao_salvar'),



url(r'^s1070-alteracao-dadosprocjud/apagar/(?P<hash>.*)/$', 
        s1070_alteracao_dadosprocjud_views.apagar, 
        name='s1070_alteracao_dadosprocjud_apagar'),

url(r'^s1070-alteracao-dadosprocjud/api/$',
            s1070_alteracao_dadosprocjud_views.s1070alteracaodadosProcJudList.as_view() ),

        url(r'^s1070-alteracao-dadosprocjud/api/(?P<pk>[0-9]+)/$',
            s1070_alteracao_dadosprocjud_views.s1070alteracaodadosProcJudDetail.as_view() ),

url(r'^s1070-alteracao-dadosprocjud/listar/(?P<hash>.*)/$', 
        s1070_alteracao_dadosprocjud_views.listar, 
        name='s1070_alteracao_dadosprocjud'),

url(r'^s1070-alteracao-dadosprocjud/salvar/(?P<hash>.*)/$', 
        s1070_alteracao_dadosprocjud_views.salvar, 
        name='s1070_alteracao_dadosprocjud_salvar'),



url(r'^s1070-alteracao-infosusp/apagar/(?P<hash>.*)/$', 
        s1070_alteracao_infosusp_views.apagar, 
        name='s1070_alteracao_infosusp_apagar'),

url(r'^s1070-alteracao-infosusp/api/$',
            s1070_alteracao_infosusp_views.s1070alteracaoinfoSuspList.as_view() ),

        url(r'^s1070-alteracao-infosusp/api/(?P<pk>[0-9]+)/$',
            s1070_alteracao_infosusp_views.s1070alteracaoinfoSuspDetail.as_view() ),

url(r'^s1070-alteracao-infosusp/listar/(?P<hash>.*)/$', 
        s1070_alteracao_infosusp_views.listar, 
        name='s1070_alteracao_infosusp'),

url(r'^s1070-alteracao-infosusp/salvar/(?P<hash>.*)/$', 
        s1070_alteracao_infosusp_views.salvar, 
        name='s1070_alteracao_infosusp_salvar'),



url(r'^s1070-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        s1070_alteracao_novavalidade_views.apagar, 
        name='s1070_alteracao_novavalidade_apagar'),

url(r'^s1070-alteracao-novavalidade/api/$',
            s1070_alteracao_novavalidade_views.s1070alteracaonovaValidadeList.as_view() ),

        url(r'^s1070-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
            s1070_alteracao_novavalidade_views.s1070alteracaonovaValidadeDetail.as_view() ),

url(r'^s1070-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        s1070_alteracao_novavalidade_views.listar, 
        name='s1070_alteracao_novavalidade'),

url(r'^s1070-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        s1070_alteracao_novavalidade_views.salvar, 
        name='s1070_alteracao_novavalidade_salvar'),



url(r'^s1070-exclusao/apagar/(?P<hash>.*)/$', 
        s1070_exclusao_views.apagar, 
        name='s1070_exclusao_apagar'),

url(r'^s1070-exclusao/api/$',
            s1070_exclusao_views.s1070exclusaoList.as_view() ),

        url(r'^s1070-exclusao/api/(?P<pk>[0-9]+)/$',
            s1070_exclusao_views.s1070exclusaoDetail.as_view() ),

url(r'^s1070-exclusao/listar/(?P<hash>.*)/$', 
        s1070_exclusao_views.listar, 
        name='s1070_exclusao'),

url(r'^s1070-exclusao/salvar/(?P<hash>.*)/$', 
        s1070_exclusao_views.salvar, 
        name='s1070_exclusao_salvar'),





]