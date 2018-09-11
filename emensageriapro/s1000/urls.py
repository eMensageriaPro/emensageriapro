#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1000-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao.apagar', 
        name='s1000_inclusao_apagar'),

url(r'^s1000-inclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao.listar', 
        name='s1000_inclusao'),

url(r'^s1000-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao.salvar', 
        name='s1000_inclusao_salvar'),



url(r'^s1000-inclusao-dadosisencao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_dadosisencao.apagar', 
        name='s1000_inclusao_dadosisencao_apagar'),

url(r'^s1000-inclusao-dadosisencao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_dadosisencao.listar', 
        name='s1000_inclusao_dadosisencao'),

url(r'^s1000-inclusao-dadosisencao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_dadosisencao.salvar', 
        name='s1000_inclusao_dadosisencao_salvar'),



url(r'^s1000-inclusao-infoop/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_infoop.apagar', 
        name='s1000_inclusao_infoop_apagar'),

url(r'^s1000-inclusao-infoop/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_infoop.listar', 
        name='s1000_inclusao_infoop'),

url(r'^s1000-inclusao-infoop/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_infoop.salvar', 
        name='s1000_inclusao_infoop_salvar'),



url(r'^s1000-inclusao-infoefr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_infoefr.apagar', 
        name='s1000_inclusao_infoefr_apagar'),

url(r'^s1000-inclusao-infoefr/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_infoefr.listar', 
        name='s1000_inclusao_infoefr'),

url(r'^s1000-inclusao-infoefr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_infoefr.salvar', 
        name='s1000_inclusao_infoefr_salvar'),



url(r'^s1000-inclusao-infoente/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_infoente.apagar', 
        name='s1000_inclusao_infoente_apagar'),

url(r'^s1000-inclusao-infoente/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_infoente.listar', 
        name='s1000_inclusao_infoente'),

url(r'^s1000-inclusao-infoente/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_infoente.salvar', 
        name='s1000_inclusao_infoente_salvar'),



url(r'^s1000-inclusao-infoorginternacional/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_infoorginternacional.apagar', 
        name='s1000_inclusao_infoorginternacional_apagar'),

url(r'^s1000-inclusao-infoorginternacional/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_infoorginternacional.listar', 
        name='s1000_inclusao_infoorginternacional'),

url(r'^s1000-inclusao-infoorginternacional/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_infoorginternacional.salvar', 
        name='s1000_inclusao_infoorginternacional_salvar'),



url(r'^s1000-inclusao-softwarehouse/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_softwarehouse.apagar', 
        name='s1000_inclusao_softwarehouse_apagar'),

url(r'^s1000-inclusao-softwarehouse/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_softwarehouse.listar', 
        name='s1000_inclusao_softwarehouse'),

url(r'^s1000-inclusao-softwarehouse/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_softwarehouse.salvar', 
        name='s1000_inclusao_softwarehouse_salvar'),



url(r'^s1000-inclusao-situacaopj/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_situacaopj.apagar', 
        name='s1000_inclusao_situacaopj_apagar'),

url(r'^s1000-inclusao-situacaopj/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_situacaopj.listar', 
        name='s1000_inclusao_situacaopj'),

url(r'^s1000-inclusao-situacaopj/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_situacaopj.salvar', 
        name='s1000_inclusao_situacaopj_salvar'),



url(r'^s1000-inclusao-situacaopf/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_situacaopf.apagar', 
        name='s1000_inclusao_situacaopf_apagar'),

url(r'^s1000-inclusao-situacaopf/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_situacaopf.listar', 
        name='s1000_inclusao_situacaopf'),

url(r'^s1000-inclusao-situacaopf/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_inclusao_situacaopf.salvar', 
        name='s1000_inclusao_situacaopf_salvar'),



url(r'^s1000-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao.apagar', 
        name='s1000_alteracao_apagar'),

url(r'^s1000-alteracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao.listar', 
        name='s1000_alteracao'),

url(r'^s1000-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao.salvar', 
        name='s1000_alteracao_salvar'),

)


urlpatterns += patterns('',


url(r'^s1000-alteracao-dadosisencao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_dadosisencao.apagar', 
        name='s1000_alteracao_dadosisencao_apagar'),

url(r'^s1000-alteracao-dadosisencao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_dadosisencao.listar', 
        name='s1000_alteracao_dadosisencao'),

url(r'^s1000-alteracao-dadosisencao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_dadosisencao.salvar', 
        name='s1000_alteracao_dadosisencao_salvar'),



url(r'^s1000-alteracao-infoop/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_infoop.apagar', 
        name='s1000_alteracao_infoop_apagar'),

url(r'^s1000-alteracao-infoop/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_infoop.listar', 
        name='s1000_alteracao_infoop'),

url(r'^s1000-alteracao-infoop/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_infoop.salvar', 
        name='s1000_alteracao_infoop_salvar'),



url(r'^s1000-alteracao-infoefr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_infoefr.apagar', 
        name='s1000_alteracao_infoefr_apagar'),

url(r'^s1000-alteracao-infoefr/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_infoefr.listar', 
        name='s1000_alteracao_infoefr'),

url(r'^s1000-alteracao-infoefr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_infoefr.salvar', 
        name='s1000_alteracao_infoefr_salvar'),



url(r'^s1000-alteracao-infoente/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_infoente.apagar', 
        name='s1000_alteracao_infoente_apagar'),

url(r'^s1000-alteracao-infoente/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_infoente.listar', 
        name='s1000_alteracao_infoente'),

url(r'^s1000-alteracao-infoente/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_infoente.salvar', 
        name='s1000_alteracao_infoente_salvar'),



url(r'^s1000-alteracao-infoorginternacional/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_infoorginternacional.apagar', 
        name='s1000_alteracao_infoorginternacional_apagar'),

url(r'^s1000-alteracao-infoorginternacional/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_infoorginternacional.listar', 
        name='s1000_alteracao_infoorginternacional'),

url(r'^s1000-alteracao-infoorginternacional/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_infoorginternacional.salvar', 
        name='s1000_alteracao_infoorginternacional_salvar'),



url(r'^s1000-alteracao-softwarehouse/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_softwarehouse.apagar', 
        name='s1000_alteracao_softwarehouse_apagar'),

url(r'^s1000-alteracao-softwarehouse/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_softwarehouse.listar', 
        name='s1000_alteracao_softwarehouse'),

url(r'^s1000-alteracao-softwarehouse/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_softwarehouse.salvar', 
        name='s1000_alteracao_softwarehouse_salvar'),



url(r'^s1000-alteracao-situacaopj/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_situacaopj.apagar', 
        name='s1000_alteracao_situacaopj_apagar'),

url(r'^s1000-alteracao-situacaopj/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_situacaopj.listar', 
        name='s1000_alteracao_situacaopj'),

url(r'^s1000-alteracao-situacaopj/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_situacaopj.salvar', 
        name='s1000_alteracao_situacaopj_salvar'),



url(r'^s1000-alteracao-situacaopf/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_situacaopf.apagar', 
        name='s1000_alteracao_situacaopf_apagar'),

url(r'^s1000-alteracao-situacaopf/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_situacaopf.listar', 
        name='s1000_alteracao_situacaopf'),

url(r'^s1000-alteracao-situacaopf/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_situacaopf.salvar', 
        name='s1000_alteracao_situacaopf_salvar'),



url(r'^s1000-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_novavalidade.apagar', 
        name='s1000_alteracao_novavalidade_apagar'),

url(r'^s1000-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_novavalidade.listar', 
        name='s1000_alteracao_novavalidade'),

url(r'^s1000-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_alteracao_novavalidade.salvar', 
        name='s1000_alteracao_novavalidade_salvar'),



url(r'^s1000-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_exclusao.apagar', 
        name='s1000_exclusao_apagar'),

url(r'^s1000-exclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_exclusao.listar', 
        name='s1000_exclusao'),

url(r'^s1000-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1000.views.s1000_exclusao.salvar', 
        name='s1000_exclusao_salvar'),

)


urlpatterns += patterns('',




)