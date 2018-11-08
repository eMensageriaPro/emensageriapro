#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2230.views import s2230_iniafastamento as s2230_iniafastamento_views
from emensageriapro.s2230.views import s2230_infoatestado as s2230_infoatestado_views
from emensageriapro.s2230.views import s2230_emitente as s2230_emitente_views
from emensageriapro.s2230.views import s2230_infocessao as s2230_infocessao_views
from emensageriapro.s2230.views import s2230_infomandsind as s2230_infomandsind_views
from emensageriapro.s2230.views import s2230_inforetif as s2230_inforetif_views
from emensageriapro.s2230.views import s2230_fimafastamento as s2230_fimafastamento_views





urlpatterns = [



url(r'^s2230-iniafastamento/apagar/(?P<hash>.*)/$', 
        s2230_iniafastamento_views.apagar, 
        name='s2230_iniafastamento_apagar'),

url(r'^s2230-iniafastamento/api/$',
            s2230_iniafastamento_views.s2230iniAfastamentoList.as_view() ),

        url(r'^s2230-iniafastamento/api/(?P<pk>[0-9]+)/$',
            s2230_iniafastamento_views.s2230iniAfastamentoDetail.as_view() ),

url(r'^s2230-iniafastamento/listar/(?P<hash>.*)/$', 
        s2230_iniafastamento_views.listar, 
        name='s2230_iniafastamento'),

url(r'^s2230-iniafastamento/salvar/(?P<hash>.*)/$', 
        s2230_iniafastamento_views.salvar, 
        name='s2230_iniafastamento_salvar'),



url(r'^s2230-infoatestado/apagar/(?P<hash>.*)/$', 
        s2230_infoatestado_views.apagar, 
        name='s2230_infoatestado_apagar'),

url(r'^s2230-infoatestado/api/$',
            s2230_infoatestado_views.s2230infoAtestadoList.as_view() ),

        url(r'^s2230-infoatestado/api/(?P<pk>[0-9]+)/$',
            s2230_infoatestado_views.s2230infoAtestadoDetail.as_view() ),

url(r'^s2230-infoatestado/listar/(?P<hash>.*)/$', 
        s2230_infoatestado_views.listar, 
        name='s2230_infoatestado'),

url(r'^s2230-infoatestado/salvar/(?P<hash>.*)/$', 
        s2230_infoatestado_views.salvar, 
        name='s2230_infoatestado_salvar'),



url(r'^s2230-emitente/apagar/(?P<hash>.*)/$', 
        s2230_emitente_views.apagar, 
        name='s2230_emitente_apagar'),

url(r'^s2230-emitente/api/$',
            s2230_emitente_views.s2230emitenteList.as_view() ),

        url(r'^s2230-emitente/api/(?P<pk>[0-9]+)/$',
            s2230_emitente_views.s2230emitenteDetail.as_view() ),

url(r'^s2230-emitente/listar/(?P<hash>.*)/$', 
        s2230_emitente_views.listar, 
        name='s2230_emitente'),

url(r'^s2230-emitente/salvar/(?P<hash>.*)/$', 
        s2230_emitente_views.salvar, 
        name='s2230_emitente_salvar'),



url(r'^s2230-infocessao/apagar/(?P<hash>.*)/$', 
        s2230_infocessao_views.apagar, 
        name='s2230_infocessao_apagar'),

url(r'^s2230-infocessao/api/$',
            s2230_infocessao_views.s2230infoCessaoList.as_view() ),

        url(r'^s2230-infocessao/api/(?P<pk>[0-9]+)/$',
            s2230_infocessao_views.s2230infoCessaoDetail.as_view() ),

url(r'^s2230-infocessao/listar/(?P<hash>.*)/$', 
        s2230_infocessao_views.listar, 
        name='s2230_infocessao'),

url(r'^s2230-infocessao/salvar/(?P<hash>.*)/$', 
        s2230_infocessao_views.salvar, 
        name='s2230_infocessao_salvar'),



url(r'^s2230-infomandsind/apagar/(?P<hash>.*)/$', 
        s2230_infomandsind_views.apagar, 
        name='s2230_infomandsind_apagar'),

url(r'^s2230-infomandsind/api/$',
            s2230_infomandsind_views.s2230infoMandSindList.as_view() ),

        url(r'^s2230-infomandsind/api/(?P<pk>[0-9]+)/$',
            s2230_infomandsind_views.s2230infoMandSindDetail.as_view() ),

url(r'^s2230-infomandsind/listar/(?P<hash>.*)/$', 
        s2230_infomandsind_views.listar, 
        name='s2230_infomandsind'),

url(r'^s2230-infomandsind/salvar/(?P<hash>.*)/$', 
        s2230_infomandsind_views.salvar, 
        name='s2230_infomandsind_salvar'),



url(r'^s2230-inforetif/apagar/(?P<hash>.*)/$', 
        s2230_inforetif_views.apagar, 
        name='s2230_inforetif_apagar'),

url(r'^s2230-inforetif/api/$',
            s2230_inforetif_views.s2230infoRetifList.as_view() ),

        url(r'^s2230-inforetif/api/(?P<pk>[0-9]+)/$',
            s2230_inforetif_views.s2230infoRetifDetail.as_view() ),

url(r'^s2230-inforetif/listar/(?P<hash>.*)/$', 
        s2230_inforetif_views.listar, 
        name='s2230_inforetif'),

url(r'^s2230-inforetif/salvar/(?P<hash>.*)/$', 
        s2230_inforetif_views.salvar, 
        name='s2230_inforetif_salvar'),



url(r'^s2230-fimafastamento/apagar/(?P<hash>.*)/$', 
        s2230_fimafastamento_views.apagar, 
        name='s2230_fimafastamento_apagar'),

url(r'^s2230-fimafastamento/api/$',
            s2230_fimafastamento_views.s2230fimAfastamentoList.as_view() ),

        url(r'^s2230-fimafastamento/api/(?P<pk>[0-9]+)/$',
            s2230_fimafastamento_views.s2230fimAfastamentoDetail.as_view() ),

url(r'^s2230-fimafastamento/listar/(?P<hash>.*)/$', 
        s2230_fimafastamento_views.listar, 
        name='s2230_fimafastamento'),

url(r'^s2230-fimafastamento/salvar/(?P<hash>.*)/$', 
        s2230_fimafastamento_views.salvar, 
        name='s2230_fimafastamento_salvar'),





]