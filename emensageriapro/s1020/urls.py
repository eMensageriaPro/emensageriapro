#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1020-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_inclusao.apagar', 
        name='s1020_inclusao_apagar'),

url(r'^s1020-inclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_inclusao.listar', 
        name='s1020_inclusao'),

url(r'^s1020-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_inclusao.salvar', 
        name='s1020_inclusao_salvar'),



url(r'^s1020-inclusao-infoprocjudterceiros/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_inclusao_infoprocjudterceiros.apagar', 
        name='s1020_inclusao_infoprocjudterceiros_apagar'),

url(r'^s1020-inclusao-infoprocjudterceiros/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_inclusao_infoprocjudterceiros.listar', 
        name='s1020_inclusao_infoprocjudterceiros'),

url(r'^s1020-inclusao-infoprocjudterceiros/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_inclusao_infoprocjudterceiros.salvar', 
        name='s1020_inclusao_infoprocjudterceiros_salvar'),



url(r'^s1020-inclusao-procjudterceiro/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_inclusao_procjudterceiro.apagar', 
        name='s1020_inclusao_procjudterceiro_apagar'),

url(r'^s1020-inclusao-procjudterceiro/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_inclusao_procjudterceiro.listar', 
        name='s1020_inclusao_procjudterceiro'),

url(r'^s1020-inclusao-procjudterceiro/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_inclusao_procjudterceiro.salvar', 
        name='s1020_inclusao_procjudterceiro_salvar'),



url(r'^s1020-inclusao-infoemprparcial/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_inclusao_infoemprparcial.apagar', 
        name='s1020_inclusao_infoemprparcial_apagar'),

url(r'^s1020-inclusao-infoemprparcial/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_inclusao_infoemprparcial.listar', 
        name='s1020_inclusao_infoemprparcial'),

url(r'^s1020-inclusao-infoemprparcial/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_inclusao_infoemprparcial.salvar', 
        name='s1020_inclusao_infoemprparcial_salvar'),



url(r'^s1020-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_alteracao.apagar', 
        name='s1020_alteracao_apagar'),

url(r'^s1020-alteracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_alteracao.listar', 
        name='s1020_alteracao'),

url(r'^s1020-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_alteracao.salvar', 
        name='s1020_alteracao_salvar'),



url(r'^s1020-alteracao-infoprocjudterceiros/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_alteracao_infoprocjudterceiros.apagar', 
        name='s1020_alteracao_infoprocjudterceiros_apagar'),

url(r'^s1020-alteracao-infoprocjudterceiros/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_alteracao_infoprocjudterceiros.listar', 
        name='s1020_alteracao_infoprocjudterceiros'),

url(r'^s1020-alteracao-infoprocjudterceiros/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_alteracao_infoprocjudterceiros.salvar', 
        name='s1020_alteracao_infoprocjudterceiros_salvar'),



url(r'^s1020-alteracao-procjudterceiro/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_alteracao_procjudterceiro.apagar', 
        name='s1020_alteracao_procjudterceiro_apagar'),

url(r'^s1020-alteracao-procjudterceiro/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_alteracao_procjudterceiro.listar', 
        name='s1020_alteracao_procjudterceiro'),

url(r'^s1020-alteracao-procjudterceiro/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_alteracao_procjudterceiro.salvar', 
        name='s1020_alteracao_procjudterceiro_salvar'),



url(r'^s1020-alteracao-infoemprparcial/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_alteracao_infoemprparcial.apagar', 
        name='s1020_alteracao_infoemprparcial_apagar'),

url(r'^s1020-alteracao-infoemprparcial/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_alteracao_infoemprparcial.listar', 
        name='s1020_alteracao_infoemprparcial'),

url(r'^s1020-alteracao-infoemprparcial/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_alteracao_infoemprparcial.salvar', 
        name='s1020_alteracao_infoemprparcial_salvar'),



url(r'^s1020-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_alteracao_novavalidade.apagar', 
        name='s1020_alteracao_novavalidade_apagar'),

url(r'^s1020-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_alteracao_novavalidade.listar', 
        name='s1020_alteracao_novavalidade'),

url(r'^s1020-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_alteracao_novavalidade.salvar', 
        name='s1020_alteracao_novavalidade_salvar'),



url(r'^s1020-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_exclusao.apagar', 
        name='s1020_exclusao_apagar'),

url(r'^s1020-exclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_exclusao.listar', 
        name='s1020_exclusao'),

url(r'^s1020-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1020.views.s1020_exclusao.salvar', 
        name='s1020_exclusao_salvar'),

)


urlpatterns += patterns('',




)