#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1250.views import s1250_tpaquis as s1250_tpaquis_views
from emensageriapro.s1250.views import s1250_ideprodutor as s1250_ideprodutor_views
from emensageriapro.s1250.views import s1250_nfs as s1250_nfs_views
from emensageriapro.s1250.views import s1250_infoprocjud as s1250_infoprocjud_views





urlpatterns = [



url(r'^s1250-tpaquis/apagar/(?P<hash>.*)/$', 
        s1250_tpaquis_views.apagar, 
        name='s1250_tpaquis_apagar'),

url(r'^s1250-tpaquis/api/$',
            s1250_tpaquis_views.s1250tpAquisList.as_view() ),

        url(r'^s1250-tpaquis/api/(?P<pk>[0-9]+)/$',
            s1250_tpaquis_views.s1250tpAquisDetail.as_view() ),

url(r'^s1250-tpaquis/listar/(?P<hash>.*)/$', 
        s1250_tpaquis_views.listar, 
        name='s1250_tpaquis'),

url(r'^s1250-tpaquis/salvar/(?P<hash>.*)/$', 
        s1250_tpaquis_views.salvar, 
        name='s1250_tpaquis_salvar'),



url(r'^s1250-ideprodutor/apagar/(?P<hash>.*)/$', 
        s1250_ideprodutor_views.apagar, 
        name='s1250_ideprodutor_apagar'),

url(r'^s1250-ideprodutor/api/$',
            s1250_ideprodutor_views.s1250ideProdutorList.as_view() ),

        url(r'^s1250-ideprodutor/api/(?P<pk>[0-9]+)/$',
            s1250_ideprodutor_views.s1250ideProdutorDetail.as_view() ),

url(r'^s1250-ideprodutor/listar/(?P<hash>.*)/$', 
        s1250_ideprodutor_views.listar, 
        name='s1250_ideprodutor'),

url(r'^s1250-ideprodutor/salvar/(?P<hash>.*)/$', 
        s1250_ideprodutor_views.salvar, 
        name='s1250_ideprodutor_salvar'),



url(r'^s1250-nfs/apagar/(?P<hash>.*)/$', 
        s1250_nfs_views.apagar, 
        name='s1250_nfs_apagar'),

url(r'^s1250-nfs/api/$',
            s1250_nfs_views.s1250nfsList.as_view() ),

        url(r'^s1250-nfs/api/(?P<pk>[0-9]+)/$',
            s1250_nfs_views.s1250nfsDetail.as_view() ),

url(r'^s1250-nfs/listar/(?P<hash>.*)/$', 
        s1250_nfs_views.listar, 
        name='s1250_nfs'),

url(r'^s1250-nfs/salvar/(?P<hash>.*)/$', 
        s1250_nfs_views.salvar, 
        name='s1250_nfs_salvar'),



url(r'^s1250-infoprocjud/apagar/(?P<hash>.*)/$', 
        s1250_infoprocjud_views.apagar, 
        name='s1250_infoprocjud_apagar'),

url(r'^s1250-infoprocjud/api/$',
            s1250_infoprocjud_views.s1250infoProcJudList.as_view() ),

        url(r'^s1250-infoprocjud/api/(?P<pk>[0-9]+)/$',
            s1250_infoprocjud_views.s1250infoProcJudDetail.as_view() ),

url(r'^s1250-infoprocjud/listar/(?P<hash>.*)/$', 
        s1250_infoprocjud_views.listar, 
        name='s1250_infoprocjud'),

url(r'^s1250-infoprocjud/salvar/(?P<hash>.*)/$', 
        s1250_infoprocjud_views.salvar, 
        name='s1250_infoprocjud_salvar'),





]