#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.r2030.views import r2030_recursosrec as r2030_recursosrec_views
from emensageriapro.r2030.views import r2030_inforecurso as r2030_inforecurso_views
from emensageriapro.r2030.views import r2030_infoproc as r2030_infoproc_views





urlpatterns = [



url(r'^r2030-recursosrec/apagar/(?P<hash>.*)/$', 
        r2030_recursosrec_views.apagar, 
        name='r2030_recursosrec_apagar'),

url(r'^r2030-recursosrec/api/$',
            r2030_recursosrec_views.r2030recursosRecList.as_view() ),

        url(r'^r2030-recursosrec/api/(?P<pk>[0-9]+)/$',
            r2030_recursosrec_views.r2030recursosRecDetail.as_view() ),

url(r'^r2030-recursosrec/listar/(?P<hash>.*)/$', 
        r2030_recursosrec_views.listar, 
        name='r2030_recursosrec'),

url(r'^r2030-recursosrec/salvar/(?P<hash>.*)/$', 
        r2030_recursosrec_views.salvar, 
        name='r2030_recursosrec_salvar'),



url(r'^r2030-inforecurso/apagar/(?P<hash>.*)/$', 
        r2030_inforecurso_views.apagar, 
        name='r2030_inforecurso_apagar'),

url(r'^r2030-inforecurso/api/$',
            r2030_inforecurso_views.r2030infoRecursoList.as_view() ),

        url(r'^r2030-inforecurso/api/(?P<pk>[0-9]+)/$',
            r2030_inforecurso_views.r2030infoRecursoDetail.as_view() ),

url(r'^r2030-inforecurso/listar/(?P<hash>.*)/$', 
        r2030_inforecurso_views.listar, 
        name='r2030_inforecurso'),

url(r'^r2030-inforecurso/salvar/(?P<hash>.*)/$', 
        r2030_inforecurso_views.salvar, 
        name='r2030_inforecurso_salvar'),



url(r'^r2030-infoproc/apagar/(?P<hash>.*)/$', 
        r2030_infoproc_views.apagar, 
        name='r2030_infoproc_apagar'),

url(r'^r2030-infoproc/api/$',
            r2030_infoproc_views.r2030infoProcList.as_view() ),

        url(r'^r2030-infoproc/api/(?P<pk>[0-9]+)/$',
            r2030_infoproc_views.r2030infoProcDetail.as_view() ),

url(r'^r2030-infoproc/listar/(?P<hash>.*)/$', 
        r2030_infoproc_views.listar, 
        name='r2030_infoproc'),

url(r'^r2030-infoproc/salvar/(?P<hash>.*)/$', 
        r2030_infoproc_views.salvar, 
        name='r2030_infoproc_salvar'),





]