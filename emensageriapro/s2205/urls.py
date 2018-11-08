#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2205.views import s2205_exterior as s2205_exterior_views
from emensageriapro.s2205.views import s2205_documentos as s2205_documentos_views
from emensageriapro.s2205.views import s2205_ctps as s2205_ctps_views
from emensageriapro.s2205.views import s2205_ric as s2205_ric_views
from emensageriapro.s2205.views import s2205_rg as s2205_rg_views
from emensageriapro.s2205.views import s2205_rne as s2205_rne_views
from emensageriapro.s2205.views import s2205_oc as s2205_oc_views
from emensageriapro.s2205.views import s2205_cnh as s2205_cnh_views
from emensageriapro.s2205.views import s2205_brasil as s2205_brasil_views
from emensageriapro.s2205.views import s2205_trabestrangeiro as s2205_trabestrangeiro_views
from emensageriapro.s2205.views import s2205_infodeficiencia as s2205_infodeficiencia_views
from emensageriapro.s2205.views import s2205_dependente as s2205_dependente_views
from emensageriapro.s2205.views import s2205_aposentadoria as s2205_aposentadoria_views
from emensageriapro.s2205.views import s2205_contato as s2205_contato_views





urlpatterns = [



url(r'^s2205-exterior/apagar/(?P<hash>.*)/$', 
        s2205_exterior_views.apagar, 
        name='s2205_exterior_apagar'),

url(r'^s2205-exterior/api/$',
            s2205_exterior_views.s2205exteriorList.as_view() ),

        url(r'^s2205-exterior/api/(?P<pk>[0-9]+)/$',
            s2205_exterior_views.s2205exteriorDetail.as_view() ),

url(r'^s2205-exterior/listar/(?P<hash>.*)/$', 
        s2205_exterior_views.listar, 
        name='s2205_exterior'),

url(r'^s2205-exterior/salvar/(?P<hash>.*)/$', 
        s2205_exterior_views.salvar, 
        name='s2205_exterior_salvar'),



url(r'^s2205-documentos/apagar/(?P<hash>.*)/$', 
        s2205_documentos_views.apagar, 
        name='s2205_documentos_apagar'),

url(r'^s2205-documentos/api/$',
            s2205_documentos_views.s2205documentosList.as_view() ),

        url(r'^s2205-documentos/api/(?P<pk>[0-9]+)/$',
            s2205_documentos_views.s2205documentosDetail.as_view() ),

url(r'^s2205-documentos/listar/(?P<hash>.*)/$', 
        s2205_documentos_views.listar, 
        name='s2205_documentos'),

url(r'^s2205-documentos/salvar/(?P<hash>.*)/$', 
        s2205_documentos_views.salvar, 
        name='s2205_documentos_salvar'),



url(r'^s2205-ctps/apagar/(?P<hash>.*)/$', 
        s2205_ctps_views.apagar, 
        name='s2205_ctps_apagar'),

url(r'^s2205-ctps/api/$',
            s2205_ctps_views.s2205CTPSList.as_view() ),

        url(r'^s2205-ctps/api/(?P<pk>[0-9]+)/$',
            s2205_ctps_views.s2205CTPSDetail.as_view() ),

url(r'^s2205-ctps/listar/(?P<hash>.*)/$', 
        s2205_ctps_views.listar, 
        name='s2205_ctps'),

url(r'^s2205-ctps/salvar/(?P<hash>.*)/$', 
        s2205_ctps_views.salvar, 
        name='s2205_ctps_salvar'),



url(r'^s2205-ric/apagar/(?P<hash>.*)/$', 
        s2205_ric_views.apagar, 
        name='s2205_ric_apagar'),

url(r'^s2205-ric/api/$',
            s2205_ric_views.s2205RICList.as_view() ),

        url(r'^s2205-ric/api/(?P<pk>[0-9]+)/$',
            s2205_ric_views.s2205RICDetail.as_view() ),

url(r'^s2205-ric/listar/(?P<hash>.*)/$', 
        s2205_ric_views.listar, 
        name='s2205_ric'),

url(r'^s2205-ric/salvar/(?P<hash>.*)/$', 
        s2205_ric_views.salvar, 
        name='s2205_ric_salvar'),



url(r'^s2205-rg/apagar/(?P<hash>.*)/$', 
        s2205_rg_views.apagar, 
        name='s2205_rg_apagar'),

url(r'^s2205-rg/api/$',
            s2205_rg_views.s2205RGList.as_view() ),

        url(r'^s2205-rg/api/(?P<pk>[0-9]+)/$',
            s2205_rg_views.s2205RGDetail.as_view() ),

url(r'^s2205-rg/listar/(?P<hash>.*)/$', 
        s2205_rg_views.listar, 
        name='s2205_rg'),

url(r'^s2205-rg/salvar/(?P<hash>.*)/$', 
        s2205_rg_views.salvar, 
        name='s2205_rg_salvar'),



url(r'^s2205-rne/apagar/(?P<hash>.*)/$', 
        s2205_rne_views.apagar, 
        name='s2205_rne_apagar'),

url(r'^s2205-rne/api/$',
            s2205_rne_views.s2205RNEList.as_view() ),

        url(r'^s2205-rne/api/(?P<pk>[0-9]+)/$',
            s2205_rne_views.s2205RNEDetail.as_view() ),

url(r'^s2205-rne/listar/(?P<hash>.*)/$', 
        s2205_rne_views.listar, 
        name='s2205_rne'),

url(r'^s2205-rne/salvar/(?P<hash>.*)/$', 
        s2205_rne_views.salvar, 
        name='s2205_rne_salvar'),



url(r'^s2205-oc/apagar/(?P<hash>.*)/$', 
        s2205_oc_views.apagar, 
        name='s2205_oc_apagar'),

url(r'^s2205-oc/api/$',
            s2205_oc_views.s2205OCList.as_view() ),

        url(r'^s2205-oc/api/(?P<pk>[0-9]+)/$',
            s2205_oc_views.s2205OCDetail.as_view() ),

url(r'^s2205-oc/listar/(?P<hash>.*)/$', 
        s2205_oc_views.listar, 
        name='s2205_oc'),

url(r'^s2205-oc/salvar/(?P<hash>.*)/$', 
        s2205_oc_views.salvar, 
        name='s2205_oc_salvar'),



url(r'^s2205-cnh/apagar/(?P<hash>.*)/$', 
        s2205_cnh_views.apagar, 
        name='s2205_cnh_apagar'),

url(r'^s2205-cnh/api/$',
            s2205_cnh_views.s2205CNHList.as_view() ),

        url(r'^s2205-cnh/api/(?P<pk>[0-9]+)/$',
            s2205_cnh_views.s2205CNHDetail.as_view() ),

url(r'^s2205-cnh/listar/(?P<hash>.*)/$', 
        s2205_cnh_views.listar, 
        name='s2205_cnh'),

url(r'^s2205-cnh/salvar/(?P<hash>.*)/$', 
        s2205_cnh_views.salvar, 
        name='s2205_cnh_salvar'),



url(r'^s2205-brasil/apagar/(?P<hash>.*)/$', 
        s2205_brasil_views.apagar, 
        name='s2205_brasil_apagar'),

url(r'^s2205-brasil/api/$',
            s2205_brasil_views.s2205brasilList.as_view() ),

        url(r'^s2205-brasil/api/(?P<pk>[0-9]+)/$',
            s2205_brasil_views.s2205brasilDetail.as_view() ),

url(r'^s2205-brasil/listar/(?P<hash>.*)/$', 
        s2205_brasil_views.listar, 
        name='s2205_brasil'),

url(r'^s2205-brasil/salvar/(?P<hash>.*)/$', 
        s2205_brasil_views.salvar, 
        name='s2205_brasil_salvar'),



url(r'^s2205-trabestrangeiro/apagar/(?P<hash>.*)/$', 
        s2205_trabestrangeiro_views.apagar, 
        name='s2205_trabestrangeiro_apagar'),

url(r'^s2205-trabestrangeiro/api/$',
            s2205_trabestrangeiro_views.s2205trabEstrangeiroList.as_view() ),

        url(r'^s2205-trabestrangeiro/api/(?P<pk>[0-9]+)/$',
            s2205_trabestrangeiro_views.s2205trabEstrangeiroDetail.as_view() ),

url(r'^s2205-trabestrangeiro/listar/(?P<hash>.*)/$', 
        s2205_trabestrangeiro_views.listar, 
        name='s2205_trabestrangeiro'),

url(r'^s2205-trabestrangeiro/salvar/(?P<hash>.*)/$', 
        s2205_trabestrangeiro_views.salvar, 
        name='s2205_trabestrangeiro_salvar'),



url(r'^s2205-infodeficiencia/apagar/(?P<hash>.*)/$', 
        s2205_infodeficiencia_views.apagar, 
        name='s2205_infodeficiencia_apagar'),

url(r'^s2205-infodeficiencia/api/$',
            s2205_infodeficiencia_views.s2205infoDeficienciaList.as_view() ),

        url(r'^s2205-infodeficiencia/api/(?P<pk>[0-9]+)/$',
            s2205_infodeficiencia_views.s2205infoDeficienciaDetail.as_view() ),

url(r'^s2205-infodeficiencia/listar/(?P<hash>.*)/$', 
        s2205_infodeficiencia_views.listar, 
        name='s2205_infodeficiencia'),

url(r'^s2205-infodeficiencia/salvar/(?P<hash>.*)/$', 
        s2205_infodeficiencia_views.salvar, 
        name='s2205_infodeficiencia_salvar'),



url(r'^s2205-dependente/apagar/(?P<hash>.*)/$', 
        s2205_dependente_views.apagar, 
        name='s2205_dependente_apagar'),

url(r'^s2205-dependente/api/$',
            s2205_dependente_views.s2205dependenteList.as_view() ),

        url(r'^s2205-dependente/api/(?P<pk>[0-9]+)/$',
            s2205_dependente_views.s2205dependenteDetail.as_view() ),

url(r'^s2205-dependente/listar/(?P<hash>.*)/$', 
        s2205_dependente_views.listar, 
        name='s2205_dependente'),

url(r'^s2205-dependente/salvar/(?P<hash>.*)/$', 
        s2205_dependente_views.salvar, 
        name='s2205_dependente_salvar'),



url(r'^s2205-aposentadoria/apagar/(?P<hash>.*)/$', 
        s2205_aposentadoria_views.apagar, 
        name='s2205_aposentadoria_apagar'),

url(r'^s2205-aposentadoria/api/$',
            s2205_aposentadoria_views.s2205aposentadoriaList.as_view() ),

        url(r'^s2205-aposentadoria/api/(?P<pk>[0-9]+)/$',
            s2205_aposentadoria_views.s2205aposentadoriaDetail.as_view() ),

url(r'^s2205-aposentadoria/listar/(?P<hash>.*)/$', 
        s2205_aposentadoria_views.listar, 
        name='s2205_aposentadoria'),

url(r'^s2205-aposentadoria/salvar/(?P<hash>.*)/$', 
        s2205_aposentadoria_views.salvar, 
        name='s2205_aposentadoria_salvar'),



url(r'^s2205-contato/apagar/(?P<hash>.*)/$', 
        s2205_contato_views.apagar, 
        name='s2205_contato_apagar'),

url(r'^s2205-contato/api/$',
            s2205_contato_views.s2205contatoList.as_view() ),

        url(r'^s2205-contato/api/(?P<pk>[0-9]+)/$',
            s2205_contato_views.s2205contatoDetail.as_view() ),

url(r'^s2205-contato/listar/(?P<hash>.*)/$', 
        s2205_contato_views.listar, 
        name='s2205_contato'),

url(r'^s2205-contato/salvar/(?P<hash>.*)/$', 
        s2205_contato_views.salvar, 
        name='s2205_contato_salvar'),





]