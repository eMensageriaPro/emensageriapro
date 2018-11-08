#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1020.views import s1020_inclusao as s1020_inclusao_views
from emensageriapro.s1020.views import s1020_inclusao_infoprocjudterceiros as s1020_inclusao_infoprocjudterceiros_views
from emensageriapro.s1020.views import s1020_inclusao_procjudterceiro as s1020_inclusao_procjudterceiro_views
from emensageriapro.s1020.views import s1020_inclusao_infoemprparcial as s1020_inclusao_infoemprparcial_views
from emensageriapro.s1020.views import s1020_alteracao as s1020_alteracao_views
from emensageriapro.s1020.views import s1020_alteracao_infoprocjudterceiros as s1020_alteracao_infoprocjudterceiros_views
from emensageriapro.s1020.views import s1020_alteracao_procjudterceiro as s1020_alteracao_procjudterceiro_views
from emensageriapro.s1020.views import s1020_alteracao_infoemprparcial as s1020_alteracao_infoemprparcial_views
from emensageriapro.s1020.views import s1020_alteracao_novavalidade as s1020_alteracao_novavalidade_views
from emensageriapro.s1020.views import s1020_exclusao as s1020_exclusao_views





urlpatterns = [



url(r'^s1020-inclusao/apagar/(?P<hash>.*)/$', 
        s1020_inclusao_views.apagar, 
        name='s1020_inclusao_apagar'),

url(r'^s1020-inclusao/api/$',
            s1020_inclusao_views.s1020inclusaoList.as_view() ),

        url(r'^s1020-inclusao/api/(?P<pk>[0-9]+)/$',
            s1020_inclusao_views.s1020inclusaoDetail.as_view() ),

url(r'^s1020-inclusao/listar/(?P<hash>.*)/$', 
        s1020_inclusao_views.listar, 
        name='s1020_inclusao'),

url(r'^s1020-inclusao/salvar/(?P<hash>.*)/$', 
        s1020_inclusao_views.salvar, 
        name='s1020_inclusao_salvar'),



url(r'^s1020-inclusao-infoprocjudterceiros/apagar/(?P<hash>.*)/$', 
        s1020_inclusao_infoprocjudterceiros_views.apagar, 
        name='s1020_inclusao_infoprocjudterceiros_apagar'),

url(r'^s1020-inclusao-infoprocjudterceiros/api/$',
            s1020_inclusao_infoprocjudterceiros_views.s1020inclusaoinfoProcJudTerceirosList.as_view() ),

        url(r'^s1020-inclusao-infoprocjudterceiros/api/(?P<pk>[0-9]+)/$',
            s1020_inclusao_infoprocjudterceiros_views.s1020inclusaoinfoProcJudTerceirosDetail.as_view() ),

url(r'^s1020-inclusao-infoprocjudterceiros/listar/(?P<hash>.*)/$', 
        s1020_inclusao_infoprocjudterceiros_views.listar, 
        name='s1020_inclusao_infoprocjudterceiros'),

url(r'^s1020-inclusao-infoprocjudterceiros/salvar/(?P<hash>.*)/$', 
        s1020_inclusao_infoprocjudterceiros_views.salvar, 
        name='s1020_inclusao_infoprocjudterceiros_salvar'),



url(r'^s1020-inclusao-procjudterceiro/apagar/(?P<hash>.*)/$', 
        s1020_inclusao_procjudterceiro_views.apagar, 
        name='s1020_inclusao_procjudterceiro_apagar'),

url(r'^s1020-inclusao-procjudterceiro/api/$',
            s1020_inclusao_procjudterceiro_views.s1020inclusaoprocJudTerceiroList.as_view() ),

        url(r'^s1020-inclusao-procjudterceiro/api/(?P<pk>[0-9]+)/$',
            s1020_inclusao_procjudterceiro_views.s1020inclusaoprocJudTerceiroDetail.as_view() ),

url(r'^s1020-inclusao-procjudterceiro/listar/(?P<hash>.*)/$', 
        s1020_inclusao_procjudterceiro_views.listar, 
        name='s1020_inclusao_procjudterceiro'),

url(r'^s1020-inclusao-procjudterceiro/salvar/(?P<hash>.*)/$', 
        s1020_inclusao_procjudterceiro_views.salvar, 
        name='s1020_inclusao_procjudterceiro_salvar'),



url(r'^s1020-inclusao-infoemprparcial/apagar/(?P<hash>.*)/$', 
        s1020_inclusao_infoemprparcial_views.apagar, 
        name='s1020_inclusao_infoemprparcial_apagar'),

url(r'^s1020-inclusao-infoemprparcial/api/$',
            s1020_inclusao_infoemprparcial_views.s1020inclusaoinfoEmprParcialList.as_view() ),

        url(r'^s1020-inclusao-infoemprparcial/api/(?P<pk>[0-9]+)/$',
            s1020_inclusao_infoemprparcial_views.s1020inclusaoinfoEmprParcialDetail.as_view() ),

url(r'^s1020-inclusao-infoemprparcial/listar/(?P<hash>.*)/$', 
        s1020_inclusao_infoemprparcial_views.listar, 
        name='s1020_inclusao_infoemprparcial'),

url(r'^s1020-inclusao-infoemprparcial/salvar/(?P<hash>.*)/$', 
        s1020_inclusao_infoemprparcial_views.salvar, 
        name='s1020_inclusao_infoemprparcial_salvar'),



url(r'^s1020-alteracao/apagar/(?P<hash>.*)/$', 
        s1020_alteracao_views.apagar, 
        name='s1020_alteracao_apagar'),

url(r'^s1020-alteracao/api/$',
            s1020_alteracao_views.s1020alteracaoList.as_view() ),

        url(r'^s1020-alteracao/api/(?P<pk>[0-9]+)/$',
            s1020_alteracao_views.s1020alteracaoDetail.as_view() ),

url(r'^s1020-alteracao/listar/(?P<hash>.*)/$', 
        s1020_alteracao_views.listar, 
        name='s1020_alteracao'),

url(r'^s1020-alteracao/salvar/(?P<hash>.*)/$', 
        s1020_alteracao_views.salvar, 
        name='s1020_alteracao_salvar'),



url(r'^s1020-alteracao-infoprocjudterceiros/apagar/(?P<hash>.*)/$', 
        s1020_alteracao_infoprocjudterceiros_views.apagar, 
        name='s1020_alteracao_infoprocjudterceiros_apagar'),

url(r'^s1020-alteracao-infoprocjudterceiros/api/$',
            s1020_alteracao_infoprocjudterceiros_views.s1020alteracaoinfoProcJudTerceirosList.as_view() ),

        url(r'^s1020-alteracao-infoprocjudterceiros/api/(?P<pk>[0-9]+)/$',
            s1020_alteracao_infoprocjudterceiros_views.s1020alteracaoinfoProcJudTerceirosDetail.as_view() ),

url(r'^s1020-alteracao-infoprocjudterceiros/listar/(?P<hash>.*)/$', 
        s1020_alteracao_infoprocjudterceiros_views.listar, 
        name='s1020_alteracao_infoprocjudterceiros'),

url(r'^s1020-alteracao-infoprocjudterceiros/salvar/(?P<hash>.*)/$', 
        s1020_alteracao_infoprocjudterceiros_views.salvar, 
        name='s1020_alteracao_infoprocjudterceiros_salvar'),



url(r'^s1020-alteracao-procjudterceiro/apagar/(?P<hash>.*)/$', 
        s1020_alteracao_procjudterceiro_views.apagar, 
        name='s1020_alteracao_procjudterceiro_apagar'),

url(r'^s1020-alteracao-procjudterceiro/api/$',
            s1020_alteracao_procjudterceiro_views.s1020alteracaoprocJudTerceiroList.as_view() ),

        url(r'^s1020-alteracao-procjudterceiro/api/(?P<pk>[0-9]+)/$',
            s1020_alteracao_procjudterceiro_views.s1020alteracaoprocJudTerceiroDetail.as_view() ),

url(r'^s1020-alteracao-procjudterceiro/listar/(?P<hash>.*)/$', 
        s1020_alteracao_procjudterceiro_views.listar, 
        name='s1020_alteracao_procjudterceiro'),

url(r'^s1020-alteracao-procjudterceiro/salvar/(?P<hash>.*)/$', 
        s1020_alteracao_procjudterceiro_views.salvar, 
        name='s1020_alteracao_procjudterceiro_salvar'),



url(r'^s1020-alteracao-infoemprparcial/apagar/(?P<hash>.*)/$', 
        s1020_alteracao_infoemprparcial_views.apagar, 
        name='s1020_alteracao_infoemprparcial_apagar'),

url(r'^s1020-alteracao-infoemprparcial/api/$',
            s1020_alteracao_infoemprparcial_views.s1020alteracaoinfoEmprParcialList.as_view() ),

        url(r'^s1020-alteracao-infoemprparcial/api/(?P<pk>[0-9]+)/$',
            s1020_alteracao_infoemprparcial_views.s1020alteracaoinfoEmprParcialDetail.as_view() ),

url(r'^s1020-alteracao-infoemprparcial/listar/(?P<hash>.*)/$', 
        s1020_alteracao_infoemprparcial_views.listar, 
        name='s1020_alteracao_infoemprparcial'),

url(r'^s1020-alteracao-infoemprparcial/salvar/(?P<hash>.*)/$', 
        s1020_alteracao_infoemprparcial_views.salvar, 
        name='s1020_alteracao_infoemprparcial_salvar'),



url(r'^s1020-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        s1020_alteracao_novavalidade_views.apagar, 
        name='s1020_alteracao_novavalidade_apagar'),

url(r'^s1020-alteracao-novavalidade/api/$',
            s1020_alteracao_novavalidade_views.s1020alteracaonovaValidadeList.as_view() ),

        url(r'^s1020-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
            s1020_alteracao_novavalidade_views.s1020alteracaonovaValidadeDetail.as_view() ),

url(r'^s1020-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        s1020_alteracao_novavalidade_views.listar, 
        name='s1020_alteracao_novavalidade'),

url(r'^s1020-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        s1020_alteracao_novavalidade_views.salvar, 
        name='s1020_alteracao_novavalidade_salvar'),



url(r'^s1020-exclusao/apagar/(?P<hash>.*)/$', 
        s1020_exclusao_views.apagar, 
        name='s1020_exclusao_apagar'),

url(r'^s1020-exclusao/api/$',
            s1020_exclusao_views.s1020exclusaoList.as_view() ),

        url(r'^s1020-exclusao/api/(?P<pk>[0-9]+)/$',
            s1020_exclusao_views.s1020exclusaoDetail.as_view() ),

url(r'^s1020-exclusao/listar/(?P<hash>.*)/$', 
        s1020_exclusao_views.listar, 
        name='s1020_exclusao'),

url(r'^s1020-exclusao/salvar/(?P<hash>.*)/$', 
        s1020_exclusao_views.salvar, 
        name='s1020_exclusao_salvar'),





]