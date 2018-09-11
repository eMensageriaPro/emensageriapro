#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1070-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_inclusao.apagar', 
        name='s1070_inclusao_apagar'),

url(r'^s1070-inclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_inclusao.listar', 
        name='s1070_inclusao'),

url(r'^s1070-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_inclusao.salvar', 
        name='s1070_inclusao_salvar'),



url(r'^s1070-inclusao-dadosprocjud/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_inclusao_dadosprocjud.apagar', 
        name='s1070_inclusao_dadosprocjud_apagar'),

url(r'^s1070-inclusao-dadosprocjud/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_inclusao_dadosprocjud.listar', 
        name='s1070_inclusao_dadosprocjud'),

url(r'^s1070-inclusao-dadosprocjud/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_inclusao_dadosprocjud.salvar', 
        name='s1070_inclusao_dadosprocjud_salvar'),



url(r'^s1070-inclusao-infosusp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_inclusao_infosusp.apagar', 
        name='s1070_inclusao_infosusp_apagar'),

url(r'^s1070-inclusao-infosusp/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_inclusao_infosusp.listar', 
        name='s1070_inclusao_infosusp'),

url(r'^s1070-inclusao-infosusp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_inclusao_infosusp.salvar', 
        name='s1070_inclusao_infosusp_salvar'),



url(r'^s1070-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_alteracao.apagar', 
        name='s1070_alteracao_apagar'),

url(r'^s1070-alteracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_alteracao.listar', 
        name='s1070_alteracao'),

url(r'^s1070-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_alteracao.salvar', 
        name='s1070_alteracao_salvar'),



url(r'^s1070-alteracao-dadosprocjud/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_alteracao_dadosprocjud.apagar', 
        name='s1070_alteracao_dadosprocjud_apagar'),

url(r'^s1070-alteracao-dadosprocjud/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_alteracao_dadosprocjud.listar', 
        name='s1070_alteracao_dadosprocjud'),

url(r'^s1070-alteracao-dadosprocjud/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_alteracao_dadosprocjud.salvar', 
        name='s1070_alteracao_dadosprocjud_salvar'),



url(r'^s1070-alteracao-infosusp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_alteracao_infosusp.apagar', 
        name='s1070_alteracao_infosusp_apagar'),

url(r'^s1070-alteracao-infosusp/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_alteracao_infosusp.listar', 
        name='s1070_alteracao_infosusp'),

url(r'^s1070-alteracao-infosusp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_alteracao_infosusp.salvar', 
        name='s1070_alteracao_infosusp_salvar'),



url(r'^s1070-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_alteracao_novavalidade.apagar', 
        name='s1070_alteracao_novavalidade_apagar'),

url(r'^s1070-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_alteracao_novavalidade.listar', 
        name='s1070_alteracao_novavalidade'),

url(r'^s1070-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_alteracao_novavalidade.salvar', 
        name='s1070_alteracao_novavalidade_salvar'),



url(r'^s1070-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_exclusao.apagar', 
        name='s1070_exclusao_apagar'),

url(r'^s1070-exclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_exclusao.listar', 
        name='s1070_exclusao'),

url(r'^s1070-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1070.views.s1070_exclusao.salvar', 
        name='s1070_exclusao_salvar'),





)