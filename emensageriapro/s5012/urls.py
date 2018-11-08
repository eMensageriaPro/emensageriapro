#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s5012.views import s5012_infocrcontrib as s5012_infocrcontrib_views





urlpatterns = [



url(r'^s5012-infocrcontrib/apagar/(?P<hash>.*)/$', 
        s5012_infocrcontrib_views.apagar, 
        name='s5012_infocrcontrib_apagar'),

url(r'^s5012-infocrcontrib/api/$',
            s5012_infocrcontrib_views.s5012infoCRContribList.as_view() ),

        url(r'^s5012-infocrcontrib/api/(?P<pk>[0-9]+)/$',
            s5012_infocrcontrib_views.s5012infoCRContribDetail.as_view() ),

url(r'^s5012-infocrcontrib/listar/(?P<hash>.*)/$', 
        s5012_infocrcontrib_views.listar, 
        name='s5012_infocrcontrib'),

url(r'^s5012-infocrcontrib/salvar/(?P<hash>.*)/$', 
        s5012_infocrcontrib_views.salvar, 
        name='s5012_infocrcontrib_salvar'),





]