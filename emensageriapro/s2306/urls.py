#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s2306-infocomplementares/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_infocomplementares.apagar', 
        name='s2306_infocomplementares_apagar'),

url(r'^s2306-infocomplementares/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_infocomplementares.listar', 
        name='s2306_infocomplementares'),

url(r'^s2306-infocomplementares/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_infocomplementares.salvar', 
        name='s2306_infocomplementares_salvar'),



url(r'^s2306-cargofuncao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_cargofuncao.apagar', 
        name='s2306_cargofuncao_apagar'),

url(r'^s2306-cargofuncao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_cargofuncao.listar', 
        name='s2306_cargofuncao'),

url(r'^s2306-cargofuncao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_cargofuncao.salvar', 
        name='s2306_cargofuncao_salvar'),



url(r'^s2306-remuneracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_remuneracao.apagar', 
        name='s2306_remuneracao_apagar'),

url(r'^s2306-remuneracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_remuneracao.listar', 
        name='s2306_remuneracao'),

url(r'^s2306-remuneracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_remuneracao.salvar', 
        name='s2306_remuneracao_salvar'),



url(r'^s2306-infoestagiario/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_infoestagiario.apagar', 
        name='s2306_infoestagiario_apagar'),

url(r'^s2306-infoestagiario/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_infoestagiario.listar', 
        name='s2306_infoestagiario'),

url(r'^s2306-infoestagiario/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_infoestagiario.salvar', 
        name='s2306_infoestagiario_salvar'),



url(r'^s2306-ageintegracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_ageintegracao.apagar', 
        name='s2306_ageintegracao_apagar'),

url(r'^s2306-ageintegracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_ageintegracao.listar', 
        name='s2306_ageintegracao'),

url(r'^s2306-ageintegracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_ageintegracao.salvar', 
        name='s2306_ageintegracao_salvar'),



url(r'^s2306-supervisorestagio/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_supervisorestagio.apagar', 
        name='s2306_supervisorestagio_apagar'),

url(r'^s2306-supervisorestagio/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_supervisorestagio.listar', 
        name='s2306_supervisorestagio'),

url(r'^s2306-supervisorestagio/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_supervisorestagio.salvar', 
        name='s2306_supervisorestagio_salvar'),





)