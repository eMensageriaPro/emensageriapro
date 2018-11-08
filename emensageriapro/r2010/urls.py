#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.r2010.views import r2010_nfs as r2010_nfs_views
from emensageriapro.r2010.views import r2010_infotpserv as r2010_infotpserv_views
from emensageriapro.r2010.views import r2010_infoprocretpr as r2010_infoprocretpr_views
from emensageriapro.r2010.views import r2010_infoprocretad as r2010_infoprocretad_views





urlpatterns = [



url(r'^r2010-nfs/apagar/(?P<hash>.*)/$', 
        r2010_nfs_views.apagar, 
        name='r2010_nfs_apagar'),

url(r'^r2010-nfs/api/$',
            r2010_nfs_views.r2010nfsList.as_view() ),

        url(r'^r2010-nfs/api/(?P<pk>[0-9]+)/$',
            r2010_nfs_views.r2010nfsDetail.as_view() ),

url(r'^r2010-nfs/listar/(?P<hash>.*)/$', 
        r2010_nfs_views.listar, 
        name='r2010_nfs'),

url(r'^r2010-nfs/salvar/(?P<hash>.*)/$', 
        r2010_nfs_views.salvar, 
        name='r2010_nfs_salvar'),



url(r'^r2010-infotpserv/apagar/(?P<hash>.*)/$', 
        r2010_infotpserv_views.apagar, 
        name='r2010_infotpserv_apagar'),

url(r'^r2010-infotpserv/api/$',
            r2010_infotpserv_views.r2010infoTpServList.as_view() ),

        url(r'^r2010-infotpserv/api/(?P<pk>[0-9]+)/$',
            r2010_infotpserv_views.r2010infoTpServDetail.as_view() ),

url(r'^r2010-infotpserv/listar/(?P<hash>.*)/$', 
        r2010_infotpserv_views.listar, 
        name='r2010_infotpserv'),

url(r'^r2010-infotpserv/salvar/(?P<hash>.*)/$', 
        r2010_infotpserv_views.salvar, 
        name='r2010_infotpserv_salvar'),



url(r'^r2010-infoprocretpr/apagar/(?P<hash>.*)/$', 
        r2010_infoprocretpr_views.apagar, 
        name='r2010_infoprocretpr_apagar'),

url(r'^r2010-infoprocretpr/api/$',
            r2010_infoprocretpr_views.r2010infoProcRetPrList.as_view() ),

        url(r'^r2010-infoprocretpr/api/(?P<pk>[0-9]+)/$',
            r2010_infoprocretpr_views.r2010infoProcRetPrDetail.as_view() ),

url(r'^r2010-infoprocretpr/listar/(?P<hash>.*)/$', 
        r2010_infoprocretpr_views.listar, 
        name='r2010_infoprocretpr'),

url(r'^r2010-infoprocretpr/salvar/(?P<hash>.*)/$', 
        r2010_infoprocretpr_views.salvar, 
        name='r2010_infoprocretpr_salvar'),



url(r'^r2010-infoprocretad/apagar/(?P<hash>.*)/$', 
        r2010_infoprocretad_views.apagar, 
        name='r2010_infoprocretad_apagar'),

url(r'^r2010-infoprocretad/api/$',
            r2010_infoprocretad_views.r2010infoProcRetAdList.as_view() ),

        url(r'^r2010-infoprocretad/api/(?P<pk>[0-9]+)/$',
            r2010_infoprocretad_views.r2010infoProcRetAdDetail.as_view() ),

url(r'^r2010-infoprocretad/listar/(?P<hash>.*)/$', 
        r2010_infoprocretad_views.listar, 
        name='r2010_infoprocretad'),

url(r'^r2010-infoprocretad/salvar/(?P<hash>.*)/$', 
        r2010_infoprocretad_views.salvar, 
        name='r2010_infoprocretad_salvar'),





]