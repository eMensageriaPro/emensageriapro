#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1010-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_inclusao.apagar', 
        name='s1010_inclusao_apagar'),

url(r'^s1010-inclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_inclusao.listar', 
        name='s1010_inclusao'),

url(r'^s1010-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_inclusao.salvar', 
        name='s1010_inclusao_salvar'),



url(r'^s1010-inclusao-ideprocessocp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_inclusao_ideprocessocp.apagar', 
        name='s1010_inclusao_ideprocessocp_apagar'),

url(r'^s1010-inclusao-ideprocessocp/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_inclusao_ideprocessocp.listar', 
        name='s1010_inclusao_ideprocessocp'),

url(r'^s1010-inclusao-ideprocessocp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_inclusao_ideprocessocp.salvar', 
        name='s1010_inclusao_ideprocessocp_salvar'),



url(r'^s1010-inclusao-ideprocessoirrf/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_inclusao_ideprocessoirrf.apagar', 
        name='s1010_inclusao_ideprocessoirrf_apagar'),

url(r'^s1010-inclusao-ideprocessoirrf/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_inclusao_ideprocessoirrf.listar', 
        name='s1010_inclusao_ideprocessoirrf'),

url(r'^s1010-inclusao-ideprocessoirrf/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_inclusao_ideprocessoirrf.salvar', 
        name='s1010_inclusao_ideprocessoirrf_salvar'),



url(r'^s1010-inclusao-ideprocessofgts/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_inclusao_ideprocessofgts.apagar', 
        name='s1010_inclusao_ideprocessofgts_apagar'),

url(r'^s1010-inclusao-ideprocessofgts/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_inclusao_ideprocessofgts.listar', 
        name='s1010_inclusao_ideprocessofgts'),

url(r'^s1010-inclusao-ideprocessofgts/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_inclusao_ideprocessofgts.salvar', 
        name='s1010_inclusao_ideprocessofgts_salvar'),



url(r'^s1010-inclusao-ideprocessosind/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_inclusao_ideprocessosind.apagar', 
        name='s1010_inclusao_ideprocessosind_apagar'),

url(r'^s1010-inclusao-ideprocessosind/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_inclusao_ideprocessosind.listar', 
        name='s1010_inclusao_ideprocessosind'),

url(r'^s1010-inclusao-ideprocessosind/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_inclusao_ideprocessosind.salvar', 
        name='s1010_inclusao_ideprocessosind_salvar'),



url(r'^s1010-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao.apagar', 
        name='s1010_alteracao_apagar'),

url(r'^s1010-alteracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao.listar', 
        name='s1010_alteracao'),

url(r'^s1010-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao.salvar', 
        name='s1010_alteracao_salvar'),



url(r'^s1010-alteracao-ideprocessocp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao_ideprocessocp.apagar', 
        name='s1010_alteracao_ideprocessocp_apagar'),

url(r'^s1010-alteracao-ideprocessocp/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao_ideprocessocp.listar', 
        name='s1010_alteracao_ideprocessocp'),

url(r'^s1010-alteracao-ideprocessocp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao_ideprocessocp.salvar', 
        name='s1010_alteracao_ideprocessocp_salvar'),



url(r'^s1010-alteracao-ideprocessoirrf/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao_ideprocessoirrf.apagar', 
        name='s1010_alteracao_ideprocessoirrf_apagar'),

url(r'^s1010-alteracao-ideprocessoirrf/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao_ideprocessoirrf.listar', 
        name='s1010_alteracao_ideprocessoirrf'),

url(r'^s1010-alteracao-ideprocessoirrf/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao_ideprocessoirrf.salvar', 
        name='s1010_alteracao_ideprocessoirrf_salvar'),



url(r'^s1010-alteracao-ideprocessofgts/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao_ideprocessofgts.apagar', 
        name='s1010_alteracao_ideprocessofgts_apagar'),

url(r'^s1010-alteracao-ideprocessofgts/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao_ideprocessofgts.listar', 
        name='s1010_alteracao_ideprocessofgts'),

url(r'^s1010-alteracao-ideprocessofgts/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao_ideprocessofgts.salvar', 
        name='s1010_alteracao_ideprocessofgts_salvar'),



url(r'^s1010-alteracao-ideprocessosind/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao_ideprocessosind.apagar', 
        name='s1010_alteracao_ideprocessosind_apagar'),

url(r'^s1010-alteracao-ideprocessosind/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao_ideprocessosind.listar', 
        name='s1010_alteracao_ideprocessosind'),

url(r'^s1010-alteracao-ideprocessosind/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao_ideprocessosind.salvar', 
        name='s1010_alteracao_ideprocessosind_salvar'),

)


urlpatterns += patterns('',


url(r'^s1010-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao_novavalidade.apagar', 
        name='s1010_alteracao_novavalidade_apagar'),

url(r'^s1010-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao_novavalidade.listar', 
        name='s1010_alteracao_novavalidade'),

url(r'^s1010-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_alteracao_novavalidade.salvar', 
        name='s1010_alteracao_novavalidade_salvar'),



url(r'^s1010-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_exclusao.apagar', 
        name='s1010_exclusao_apagar'),

url(r'^s1010-exclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_exclusao.listar', 
        name='s1010_exclusao'),

url(r'^s1010-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1010.views.s1010_exclusao.salvar', 
        name='s1010_exclusao_salvar'),





)