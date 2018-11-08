#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2240.views import s2240_iniexprisco as s2240_iniexprisco_views
from emensageriapro.s2240.views import s2240_iniexprisco_infoamb as s2240_iniexprisco_infoamb_views
from emensageriapro.s2240.views import s2240_iniexprisco_ativpericinsal as s2240_iniexprisco_ativpericinsal_views
from emensageriapro.s2240.views import s2240_iniexprisco_fatrisco as s2240_iniexprisco_fatrisco_views
from emensageriapro.s2240.views import s2240_iniexprisco_epc as s2240_iniexprisco_epc_views
from emensageriapro.s2240.views import s2240_iniexprisco_epi as s2240_iniexprisco_epi_views
from emensageriapro.s2240.views import s2240_iniexprisco_respreg as s2240_iniexprisco_respreg_views
from emensageriapro.s2240.views import s2240_iniexprisco_obs as s2240_iniexprisco_obs_views
from emensageriapro.s2240.views import s2240_altexprisco as s2240_altexprisco_views
from emensageriapro.s2240.views import s2240_altexprisco_infoamb as s2240_altexprisco_infoamb_views
from emensageriapro.s2240.views import s2240_altexprisco_fatrisco as s2240_altexprisco_fatrisco_views
from emensageriapro.s2240.views import s2240_altexprisco_epc as s2240_altexprisco_epc_views
from emensageriapro.s2240.views import s2240_altexprisco_epi as s2240_altexprisco_epi_views
from emensageriapro.s2240.views import s2240_fimexprisco as s2240_fimexprisco_views
from emensageriapro.s2240.views import s2240_fimexprisco_infoamb as s2240_fimexprisco_infoamb_views
from emensageriapro.s2240.views import s2240_fimexprisco_respreg as s2240_fimexprisco_respreg_views





urlpatterns = [



url(r'^s2240-iniexprisco/apagar/(?P<hash>.*)/$', 
        s2240_iniexprisco_views.apagar, 
        name='s2240_iniexprisco_apagar'),

url(r'^s2240-iniexprisco/api/$',
            s2240_iniexprisco_views.s2240iniExpRiscoList.as_view() ),

        url(r'^s2240-iniexprisco/api/(?P<pk>[0-9]+)/$',
            s2240_iniexprisco_views.s2240iniExpRiscoDetail.as_view() ),

url(r'^s2240-iniexprisco/listar/(?P<hash>.*)/$', 
        s2240_iniexprisco_views.listar, 
        name='s2240_iniexprisco'),

url(r'^s2240-iniexprisco/salvar/(?P<hash>.*)/$', 
        s2240_iniexprisco_views.salvar, 
        name='s2240_iniexprisco_salvar'),



url(r'^s2240-iniexprisco-infoamb/apagar/(?P<hash>.*)/$', 
        s2240_iniexprisco_infoamb_views.apagar, 
        name='s2240_iniexprisco_infoamb_apagar'),

url(r'^s2240-iniexprisco-infoamb/api/$',
            s2240_iniexprisco_infoamb_views.s2240iniExpRiscoinfoAmbList.as_view() ),

        url(r'^s2240-iniexprisco-infoamb/api/(?P<pk>[0-9]+)/$',
            s2240_iniexprisco_infoamb_views.s2240iniExpRiscoinfoAmbDetail.as_view() ),

url(r'^s2240-iniexprisco-infoamb/listar/(?P<hash>.*)/$', 
        s2240_iniexprisco_infoamb_views.listar, 
        name='s2240_iniexprisco_infoamb'),

url(r'^s2240-iniexprisco-infoamb/salvar/(?P<hash>.*)/$', 
        s2240_iniexprisco_infoamb_views.salvar, 
        name='s2240_iniexprisco_infoamb_salvar'),



url(r'^s2240-iniexprisco-ativpericinsal/apagar/(?P<hash>.*)/$', 
        s2240_iniexprisco_ativpericinsal_views.apagar, 
        name='s2240_iniexprisco_ativpericinsal_apagar'),

url(r'^s2240-iniexprisco-ativpericinsal/api/$',
            s2240_iniexprisco_ativpericinsal_views.s2240iniExpRiscoativPericInsalList.as_view() ),

        url(r'^s2240-iniexprisco-ativpericinsal/api/(?P<pk>[0-9]+)/$',
            s2240_iniexprisco_ativpericinsal_views.s2240iniExpRiscoativPericInsalDetail.as_view() ),

url(r'^s2240-iniexprisco-ativpericinsal/listar/(?P<hash>.*)/$', 
        s2240_iniexprisco_ativpericinsal_views.listar, 
        name='s2240_iniexprisco_ativpericinsal'),

url(r'^s2240-iniexprisco-ativpericinsal/salvar/(?P<hash>.*)/$', 
        s2240_iniexprisco_ativpericinsal_views.salvar, 
        name='s2240_iniexprisco_ativpericinsal_salvar'),



url(r'^s2240-iniexprisco-fatrisco/apagar/(?P<hash>.*)/$', 
        s2240_iniexprisco_fatrisco_views.apagar, 
        name='s2240_iniexprisco_fatrisco_apagar'),

url(r'^s2240-iniexprisco-fatrisco/api/$',
            s2240_iniexprisco_fatrisco_views.s2240iniExpRiscofatRiscoList.as_view() ),

        url(r'^s2240-iniexprisco-fatrisco/api/(?P<pk>[0-9]+)/$',
            s2240_iniexprisco_fatrisco_views.s2240iniExpRiscofatRiscoDetail.as_view() ),

url(r'^s2240-iniexprisco-fatrisco/listar/(?P<hash>.*)/$', 
        s2240_iniexprisco_fatrisco_views.listar, 
        name='s2240_iniexprisco_fatrisco'),

url(r'^s2240-iniexprisco-fatrisco/salvar/(?P<hash>.*)/$', 
        s2240_iniexprisco_fatrisco_views.salvar, 
        name='s2240_iniexprisco_fatrisco_salvar'),



url(r'^s2240-iniexprisco-epc/apagar/(?P<hash>.*)/$', 
        s2240_iniexprisco_epc_views.apagar, 
        name='s2240_iniexprisco_epc_apagar'),

url(r'^s2240-iniexprisco-epc/api/$',
            s2240_iniexprisco_epc_views.s2240iniExpRiscoepcList.as_view() ),

        url(r'^s2240-iniexprisco-epc/api/(?P<pk>[0-9]+)/$',
            s2240_iniexprisco_epc_views.s2240iniExpRiscoepcDetail.as_view() ),

url(r'^s2240-iniexprisco-epc/listar/(?P<hash>.*)/$', 
        s2240_iniexprisco_epc_views.listar, 
        name='s2240_iniexprisco_epc'),

url(r'^s2240-iniexprisco-epc/salvar/(?P<hash>.*)/$', 
        s2240_iniexprisco_epc_views.salvar, 
        name='s2240_iniexprisco_epc_salvar'),



url(r'^s2240-iniexprisco-epi/apagar/(?P<hash>.*)/$', 
        s2240_iniexprisco_epi_views.apagar, 
        name='s2240_iniexprisco_epi_apagar'),

url(r'^s2240-iniexprisco-epi/api/$',
            s2240_iniexprisco_epi_views.s2240iniExpRiscoepiList.as_view() ),

        url(r'^s2240-iniexprisco-epi/api/(?P<pk>[0-9]+)/$',
            s2240_iniexprisco_epi_views.s2240iniExpRiscoepiDetail.as_view() ),

url(r'^s2240-iniexprisco-epi/listar/(?P<hash>.*)/$', 
        s2240_iniexprisco_epi_views.listar, 
        name='s2240_iniexprisco_epi'),

url(r'^s2240-iniexprisco-epi/salvar/(?P<hash>.*)/$', 
        s2240_iniexprisco_epi_views.salvar, 
        name='s2240_iniexprisco_epi_salvar'),



url(r'^s2240-iniexprisco-respreg/apagar/(?P<hash>.*)/$', 
        s2240_iniexprisco_respreg_views.apagar, 
        name='s2240_iniexprisco_respreg_apagar'),

url(r'^s2240-iniexprisco-respreg/api/$',
            s2240_iniexprisco_respreg_views.s2240iniExpRiscorespRegList.as_view() ),

        url(r'^s2240-iniexprisco-respreg/api/(?P<pk>[0-9]+)/$',
            s2240_iniexprisco_respreg_views.s2240iniExpRiscorespRegDetail.as_view() ),

url(r'^s2240-iniexprisco-respreg/listar/(?P<hash>.*)/$', 
        s2240_iniexprisco_respreg_views.listar, 
        name='s2240_iniexprisco_respreg'),

url(r'^s2240-iniexprisco-respreg/salvar/(?P<hash>.*)/$', 
        s2240_iniexprisco_respreg_views.salvar, 
        name='s2240_iniexprisco_respreg_salvar'),



url(r'^s2240-iniexprisco-obs/apagar/(?P<hash>.*)/$', 
        s2240_iniexprisco_obs_views.apagar, 
        name='s2240_iniexprisco_obs_apagar'),

url(r'^s2240-iniexprisco-obs/api/$',
            s2240_iniexprisco_obs_views.s2240iniExpRiscoobsList.as_view() ),

        url(r'^s2240-iniexprisco-obs/api/(?P<pk>[0-9]+)/$',
            s2240_iniexprisco_obs_views.s2240iniExpRiscoobsDetail.as_view() ),

url(r'^s2240-iniexprisco-obs/listar/(?P<hash>.*)/$', 
        s2240_iniexprisco_obs_views.listar, 
        name='s2240_iniexprisco_obs'),

url(r'^s2240-iniexprisco-obs/salvar/(?P<hash>.*)/$', 
        s2240_iniexprisco_obs_views.salvar, 
        name='s2240_iniexprisco_obs_salvar'),



url(r'^s2240-altexprisco/apagar/(?P<hash>.*)/$', 
        s2240_altexprisco_views.apagar, 
        name='s2240_altexprisco_apagar'),

url(r'^s2240-altexprisco/api/$',
            s2240_altexprisco_views.s2240altExpRiscoList.as_view() ),

        url(r'^s2240-altexprisco/api/(?P<pk>[0-9]+)/$',
            s2240_altexprisco_views.s2240altExpRiscoDetail.as_view() ),

url(r'^s2240-altexprisco/listar/(?P<hash>.*)/$', 
        s2240_altexprisco_views.listar, 
        name='s2240_altexprisco'),

url(r'^s2240-altexprisco/salvar/(?P<hash>.*)/$', 
        s2240_altexprisco_views.salvar, 
        name='s2240_altexprisco_salvar'),



url(r'^s2240-altexprisco-infoamb/apagar/(?P<hash>.*)/$', 
        s2240_altexprisco_infoamb_views.apagar, 
        name='s2240_altexprisco_infoamb_apagar'),

url(r'^s2240-altexprisco-infoamb/api/$',
            s2240_altexprisco_infoamb_views.s2240altExpRiscoinfoAmbList.as_view() ),

        url(r'^s2240-altexprisco-infoamb/api/(?P<pk>[0-9]+)/$',
            s2240_altexprisco_infoamb_views.s2240altExpRiscoinfoAmbDetail.as_view() ),

url(r'^s2240-altexprisco-infoamb/listar/(?P<hash>.*)/$', 
        s2240_altexprisco_infoamb_views.listar, 
        name='s2240_altexprisco_infoamb'),

url(r'^s2240-altexprisco-infoamb/salvar/(?P<hash>.*)/$', 
        s2240_altexprisco_infoamb_views.salvar, 
        name='s2240_altexprisco_infoamb_salvar'),



url(r'^s2240-altexprisco-fatrisco/apagar/(?P<hash>.*)/$', 
        s2240_altexprisco_fatrisco_views.apagar, 
        name='s2240_altexprisco_fatrisco_apagar'),

url(r'^s2240-altexprisco-fatrisco/api/$',
            s2240_altexprisco_fatrisco_views.s2240altExpRiscofatRiscoList.as_view() ),

        url(r'^s2240-altexprisco-fatrisco/api/(?P<pk>[0-9]+)/$',
            s2240_altexprisco_fatrisco_views.s2240altExpRiscofatRiscoDetail.as_view() ),

url(r'^s2240-altexprisco-fatrisco/listar/(?P<hash>.*)/$', 
        s2240_altexprisco_fatrisco_views.listar, 
        name='s2240_altexprisco_fatrisco'),

url(r'^s2240-altexprisco-fatrisco/salvar/(?P<hash>.*)/$', 
        s2240_altexprisco_fatrisco_views.salvar, 
        name='s2240_altexprisco_fatrisco_salvar'),



url(r'^s2240-altexprisco-epc/apagar/(?P<hash>.*)/$', 
        s2240_altexprisco_epc_views.apagar, 
        name='s2240_altexprisco_epc_apagar'),

url(r'^s2240-altexprisco-epc/api/$',
            s2240_altexprisco_epc_views.s2240altExpRiscoepcList.as_view() ),

        url(r'^s2240-altexprisco-epc/api/(?P<pk>[0-9]+)/$',
            s2240_altexprisco_epc_views.s2240altExpRiscoepcDetail.as_view() ),

url(r'^s2240-altexprisco-epc/listar/(?P<hash>.*)/$', 
        s2240_altexprisco_epc_views.listar, 
        name='s2240_altexprisco_epc'),

url(r'^s2240-altexprisco-epc/salvar/(?P<hash>.*)/$', 
        s2240_altexprisco_epc_views.salvar, 
        name='s2240_altexprisco_epc_salvar'),



url(r'^s2240-altexprisco-epi/apagar/(?P<hash>.*)/$', 
        s2240_altexprisco_epi_views.apagar, 
        name='s2240_altexprisco_epi_apagar'),

url(r'^s2240-altexprisco-epi/api/$',
            s2240_altexprisco_epi_views.s2240altExpRiscoepiList.as_view() ),

        url(r'^s2240-altexprisco-epi/api/(?P<pk>[0-9]+)/$',
            s2240_altexprisco_epi_views.s2240altExpRiscoepiDetail.as_view() ),

url(r'^s2240-altexprisco-epi/listar/(?P<hash>.*)/$', 
        s2240_altexprisco_epi_views.listar, 
        name='s2240_altexprisco_epi'),

url(r'^s2240-altexprisco-epi/salvar/(?P<hash>.*)/$', 
        s2240_altexprisco_epi_views.salvar, 
        name='s2240_altexprisco_epi_salvar'),



url(r'^s2240-fimexprisco/apagar/(?P<hash>.*)/$', 
        s2240_fimexprisco_views.apagar, 
        name='s2240_fimexprisco_apagar'),

url(r'^s2240-fimexprisco/api/$',
            s2240_fimexprisco_views.s2240fimExpRiscoList.as_view() ),

        url(r'^s2240-fimexprisco/api/(?P<pk>[0-9]+)/$',
            s2240_fimexprisco_views.s2240fimExpRiscoDetail.as_view() ),

url(r'^s2240-fimexprisco/listar/(?P<hash>.*)/$', 
        s2240_fimexprisco_views.listar, 
        name='s2240_fimexprisco'),

url(r'^s2240-fimexprisco/salvar/(?P<hash>.*)/$', 
        s2240_fimexprisco_views.salvar, 
        name='s2240_fimexprisco_salvar'),



url(r'^s2240-fimexprisco-infoamb/apagar/(?P<hash>.*)/$', 
        s2240_fimexprisco_infoamb_views.apagar, 
        name='s2240_fimexprisco_infoamb_apagar'),

url(r'^s2240-fimexprisco-infoamb/api/$',
            s2240_fimexprisco_infoamb_views.s2240fimExpRiscoinfoAmbList.as_view() ),

        url(r'^s2240-fimexprisco-infoamb/api/(?P<pk>[0-9]+)/$',
            s2240_fimexprisco_infoamb_views.s2240fimExpRiscoinfoAmbDetail.as_view() ),

url(r'^s2240-fimexprisco-infoamb/listar/(?P<hash>.*)/$', 
        s2240_fimexprisco_infoamb_views.listar, 
        name='s2240_fimexprisco_infoamb'),

url(r'^s2240-fimexprisco-infoamb/salvar/(?P<hash>.*)/$', 
        s2240_fimexprisco_infoamb_views.salvar, 
        name='s2240_fimexprisco_infoamb_salvar'),



url(r'^s2240-fimexprisco-respreg/apagar/(?P<hash>.*)/$', 
        s2240_fimexprisco_respreg_views.apagar, 
        name='s2240_fimexprisco_respreg_apagar'),

url(r'^s2240-fimexprisco-respreg/api/$',
            s2240_fimexprisco_respreg_views.s2240fimExpRiscorespRegList.as_view() ),

        url(r'^s2240-fimexprisco-respreg/api/(?P<pk>[0-9]+)/$',
            s2240_fimexprisco_respreg_views.s2240fimExpRiscorespRegDetail.as_view() ),

url(r'^s2240-fimexprisco-respreg/listar/(?P<hash>.*)/$', 
        s2240_fimexprisco_respreg_views.listar, 
        name='s2240_fimexprisco_respreg'),

url(r'^s2240-fimexprisco-respreg/salvar/(?P<hash>.*)/$', 
        s2240_fimexprisco_respreg_views.salvar, 
        name='s2240_fimexprisco_respreg_salvar'),





]