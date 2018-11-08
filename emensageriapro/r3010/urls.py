#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.r3010.views import r3010_ideestab as r3010_ideestab_views
from emensageriapro.r3010.views import r3010_boletim as r3010_boletim_views
from emensageriapro.r3010.views import r3010_receitaingressos as r3010_receitaingressos_views
from emensageriapro.r3010.views import r3010_outrasreceitas as r3010_outrasreceitas_views
from emensageriapro.r3010.views import r3010_infoproc as r3010_infoproc_views





urlpatterns = [



url(r'^r3010-ideestab/apagar/(?P<hash>.*)/$', 
        r3010_ideestab_views.apagar, 
        name='r3010_ideestab_apagar'),

url(r'^r3010-ideestab/api/$',
            r3010_ideestab_views.r3010ideEstabList.as_view() ),

        url(r'^r3010-ideestab/api/(?P<pk>[0-9]+)/$',
            r3010_ideestab_views.r3010ideEstabDetail.as_view() ),

url(r'^r3010-ideestab/listar/(?P<hash>.*)/$', 
        r3010_ideestab_views.listar, 
        name='r3010_ideestab'),

url(r'^r3010-ideestab/salvar/(?P<hash>.*)/$', 
        r3010_ideestab_views.salvar, 
        name='r3010_ideestab_salvar'),



url(r'^r3010-boletim/apagar/(?P<hash>.*)/$', 
        r3010_boletim_views.apagar, 
        name='r3010_boletim_apagar'),

url(r'^r3010-boletim/api/$',
            r3010_boletim_views.r3010boletimList.as_view() ),

        url(r'^r3010-boletim/api/(?P<pk>[0-9]+)/$',
            r3010_boletim_views.r3010boletimDetail.as_view() ),

url(r'^r3010-boletim/listar/(?P<hash>.*)/$', 
        r3010_boletim_views.listar, 
        name='r3010_boletim'),

url(r'^r3010-boletim/salvar/(?P<hash>.*)/$', 
        r3010_boletim_views.salvar, 
        name='r3010_boletim_salvar'),



url(r'^r3010-receitaingressos/apagar/(?P<hash>.*)/$', 
        r3010_receitaingressos_views.apagar, 
        name='r3010_receitaingressos_apagar'),

url(r'^r3010-receitaingressos/api/$',
            r3010_receitaingressos_views.r3010receitaIngressosList.as_view() ),

        url(r'^r3010-receitaingressos/api/(?P<pk>[0-9]+)/$',
            r3010_receitaingressos_views.r3010receitaIngressosDetail.as_view() ),

url(r'^r3010-receitaingressos/listar/(?P<hash>.*)/$', 
        r3010_receitaingressos_views.listar, 
        name='r3010_receitaingressos'),

url(r'^r3010-receitaingressos/salvar/(?P<hash>.*)/$', 
        r3010_receitaingressos_views.salvar, 
        name='r3010_receitaingressos_salvar'),



url(r'^r3010-outrasreceitas/apagar/(?P<hash>.*)/$', 
        r3010_outrasreceitas_views.apagar, 
        name='r3010_outrasreceitas_apagar'),

url(r'^r3010-outrasreceitas/api/$',
            r3010_outrasreceitas_views.r3010outrasReceitasList.as_view() ),

        url(r'^r3010-outrasreceitas/api/(?P<pk>[0-9]+)/$',
            r3010_outrasreceitas_views.r3010outrasReceitasDetail.as_view() ),

url(r'^r3010-outrasreceitas/listar/(?P<hash>.*)/$', 
        r3010_outrasreceitas_views.listar, 
        name='r3010_outrasreceitas'),

url(r'^r3010-outrasreceitas/salvar/(?P<hash>.*)/$', 
        r3010_outrasreceitas_views.salvar, 
        name='r3010_outrasreceitas_salvar'),



url(r'^r3010-infoproc/apagar/(?P<hash>.*)/$', 
        r3010_infoproc_views.apagar, 
        name='r3010_infoproc_apagar'),

url(r'^r3010-infoproc/api/$',
            r3010_infoproc_views.r3010infoProcList.as_view() ),

        url(r'^r3010-infoproc/api/(?P<pk>[0-9]+)/$',
            r3010_infoproc_views.r3010infoProcDetail.as_view() ),

url(r'^r3010-infoproc/listar/(?P<hash>.*)/$', 
        r3010_infoproc_views.listar, 
        name='r3010_infoproc'),

url(r'^r3010-infoproc/salvar/(?P<hash>.*)/$', 
        r3010_infoproc_views.salvar, 
        name='r3010_infoproc_salvar'),





]