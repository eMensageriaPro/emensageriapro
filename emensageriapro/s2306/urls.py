#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2306.views import s2306_infocomplementares as s2306_infocomplementares_views
from emensageriapro.s2306.views import s2306_cargofuncao as s2306_cargofuncao_views
from emensageriapro.s2306.views import s2306_remuneracao as s2306_remuneracao_views
from emensageriapro.s2306.views import s2306_infotrabcedido as s2306_infotrabcedido_views
from emensageriapro.s2306.views import s2306_infoestagiario as s2306_infoestagiario_views
from emensageriapro.s2306.views import s2306_ageintegracao as s2306_ageintegracao_views
from emensageriapro.s2306.views import s2306_supervisorestagio as s2306_supervisorestagio_views





urlpatterns = [



url(r'^s2306-infocomplementares/apagar/(?P<hash>.*)/$', 
        s2306_infocomplementares_views.apagar, 
        name='s2306_infocomplementares_apagar'),

url(r'^s2306-infocomplementares/api/$',
            s2306_infocomplementares_views.s2306infoComplementaresList.as_view() ),

        url(r'^s2306-infocomplementares/api/(?P<pk>[0-9]+)/$',
            s2306_infocomplementares_views.s2306infoComplementaresDetail.as_view() ),

url(r'^s2306-infocomplementares/listar/(?P<hash>.*)/$', 
        s2306_infocomplementares_views.listar, 
        name='s2306_infocomplementares'),

url(r'^s2306-infocomplementares/salvar/(?P<hash>.*)/$', 
        s2306_infocomplementares_views.salvar, 
        name='s2306_infocomplementares_salvar'),



url(r'^s2306-cargofuncao/apagar/(?P<hash>.*)/$', 
        s2306_cargofuncao_views.apagar, 
        name='s2306_cargofuncao_apagar'),

url(r'^s2306-cargofuncao/api/$',
            s2306_cargofuncao_views.s2306cargoFuncaoList.as_view() ),

        url(r'^s2306-cargofuncao/api/(?P<pk>[0-9]+)/$',
            s2306_cargofuncao_views.s2306cargoFuncaoDetail.as_view() ),

url(r'^s2306-cargofuncao/listar/(?P<hash>.*)/$', 
        s2306_cargofuncao_views.listar, 
        name='s2306_cargofuncao'),

url(r'^s2306-cargofuncao/salvar/(?P<hash>.*)/$', 
        s2306_cargofuncao_views.salvar, 
        name='s2306_cargofuncao_salvar'),



url(r'^s2306-remuneracao/apagar/(?P<hash>.*)/$', 
        s2306_remuneracao_views.apagar, 
        name='s2306_remuneracao_apagar'),

url(r'^s2306-remuneracao/api/$',
            s2306_remuneracao_views.s2306remuneracaoList.as_view() ),

        url(r'^s2306-remuneracao/api/(?P<pk>[0-9]+)/$',
            s2306_remuneracao_views.s2306remuneracaoDetail.as_view() ),

url(r'^s2306-remuneracao/listar/(?P<hash>.*)/$', 
        s2306_remuneracao_views.listar, 
        name='s2306_remuneracao'),

url(r'^s2306-remuneracao/salvar/(?P<hash>.*)/$', 
        s2306_remuneracao_views.salvar, 
        name='s2306_remuneracao_salvar'),



url(r'^s2306-infotrabcedido/apagar/(?P<hash>.*)/$', 
        s2306_infotrabcedido_views.apagar, 
        name='s2306_infotrabcedido_apagar'),

url(r'^s2306-infotrabcedido/api/$',
            s2306_infotrabcedido_views.s2306infoTrabCedidoList.as_view() ),

        url(r'^s2306-infotrabcedido/api/(?P<pk>[0-9]+)/$',
            s2306_infotrabcedido_views.s2306infoTrabCedidoDetail.as_view() ),

url(r'^s2306-infotrabcedido/listar/(?P<hash>.*)/$', 
        s2306_infotrabcedido_views.listar, 
        name='s2306_infotrabcedido'),

url(r'^s2306-infotrabcedido/salvar/(?P<hash>.*)/$', 
        s2306_infotrabcedido_views.salvar, 
        name='s2306_infotrabcedido_salvar'),



url(r'^s2306-infoestagiario/apagar/(?P<hash>.*)/$', 
        s2306_infoestagiario_views.apagar, 
        name='s2306_infoestagiario_apagar'),

url(r'^s2306-infoestagiario/api/$',
            s2306_infoestagiario_views.s2306infoEstagiarioList.as_view() ),

        url(r'^s2306-infoestagiario/api/(?P<pk>[0-9]+)/$',
            s2306_infoestagiario_views.s2306infoEstagiarioDetail.as_view() ),

url(r'^s2306-infoestagiario/listar/(?P<hash>.*)/$', 
        s2306_infoestagiario_views.listar, 
        name='s2306_infoestagiario'),

url(r'^s2306-infoestagiario/salvar/(?P<hash>.*)/$', 
        s2306_infoestagiario_views.salvar, 
        name='s2306_infoestagiario_salvar'),



url(r'^s2306-ageintegracao/apagar/(?P<hash>.*)/$', 
        s2306_ageintegracao_views.apagar, 
        name='s2306_ageintegracao_apagar'),

url(r'^s2306-ageintegracao/api/$',
            s2306_ageintegracao_views.s2306ageIntegracaoList.as_view() ),

        url(r'^s2306-ageintegracao/api/(?P<pk>[0-9]+)/$',
            s2306_ageintegracao_views.s2306ageIntegracaoDetail.as_view() ),

url(r'^s2306-ageintegracao/listar/(?P<hash>.*)/$', 
        s2306_ageintegracao_views.listar, 
        name='s2306_ageintegracao'),

url(r'^s2306-ageintegracao/salvar/(?P<hash>.*)/$', 
        s2306_ageintegracao_views.salvar, 
        name='s2306_ageintegracao_salvar'),



url(r'^s2306-supervisorestagio/apagar/(?P<hash>.*)/$', 
        s2306_supervisorestagio_views.apagar, 
        name='s2306_supervisorestagio_apagar'),

url(r'^s2306-supervisorestagio/api/$',
            s2306_supervisorestagio_views.s2306supervisorEstagioList.as_view() ),

        url(r'^s2306-supervisorestagio/api/(?P<pk>[0-9]+)/$',
            s2306_supervisorestagio_views.s2306supervisorEstagioDetail.as_view() ),

url(r'^s2306-supervisorestagio/listar/(?P<hash>.*)/$', 
        s2306_supervisorestagio_views.listar, 
        name='s2306_supervisorestagio'),

url(r'^s2306-supervisorestagio/salvar/(?P<hash>.*)/$', 
        s2306_supervisorestagio_views.salvar, 
        name='s2306_supervisorestagio_salvar'),





]