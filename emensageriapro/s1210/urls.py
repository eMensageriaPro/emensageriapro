#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1210-deps/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_deps.apagar', 
        name='s1210_deps_apagar'),

url(r'^s1210-deps/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_deps.listar', 
        name='s1210_deps'),

url(r'^s1210-deps/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_deps.salvar', 
        name='s1210_deps_salvar'),



url(r'^s1210-infopgto/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_infopgto.apagar', 
        name='s1210_infopgto_apagar'),

url(r'^s1210-infopgto/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_infopgto.listar', 
        name='s1210_infopgto'),

url(r'^s1210-infopgto/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_infopgto.salvar', 
        name='s1210_infopgto_salvar'),



url(r'^s1210-detpgtofl/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofl.apagar', 
        name='s1210_detpgtofl_apagar'),

url(r'^s1210-detpgtofl/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofl.listar', 
        name='s1210_detpgtofl'),

url(r'^s1210-detpgtofl/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofl.salvar', 
        name='s1210_detpgtofl_salvar'),



url(r'^s1210-detpgtofl-retpgtotot/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofl_retpgtotot.apagar', 
        name='s1210_detpgtofl_retpgtotot_apagar'),

url(r'^s1210-detpgtofl-retpgtotot/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofl_retpgtotot.listar', 
        name='s1210_detpgtofl_retpgtotot'),

url(r'^s1210-detpgtofl-retpgtotot/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofl_retpgtotot.salvar', 
        name='s1210_detpgtofl_retpgtotot_salvar'),



url(r'^s1210-detpgtofl-penalim/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofl_penalim.apagar', 
        name='s1210_detpgtofl_penalim_apagar'),

url(r'^s1210-detpgtofl-penalim/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofl_penalim.listar', 
        name='s1210_detpgtofl_penalim'),

url(r'^s1210-detpgtofl-penalim/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofl_penalim.salvar', 
        name='s1210_detpgtofl_penalim_salvar'),



url(r'^s1210-detpgtofl-infopgtoparc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofl_infopgtoparc.apagar', 
        name='s1210_detpgtofl_infopgtoparc_apagar'),

url(r'^s1210-detpgtofl-infopgtoparc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofl_infopgtoparc.listar', 
        name='s1210_detpgtofl_infopgtoparc'),

url(r'^s1210-detpgtofl-infopgtoparc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofl_infopgtoparc.salvar', 
        name='s1210_detpgtofl_infopgtoparc_salvar'),



url(r'^s1210-detpgtobenpr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtobenpr.apagar', 
        name='s1210_detpgtobenpr_apagar'),

url(r'^s1210-detpgtobenpr/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtobenpr.listar', 
        name='s1210_detpgtobenpr'),

url(r'^s1210-detpgtobenpr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtobenpr.salvar', 
        name='s1210_detpgtobenpr_salvar'),



url(r'^s1210-detpgtobenpr-retpgtotot/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtobenpr_retpgtotot.apagar', 
        name='s1210_detpgtobenpr_retpgtotot_apagar'),

url(r'^s1210-detpgtobenpr-retpgtotot/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtobenpr_retpgtotot.listar', 
        name='s1210_detpgtobenpr_retpgtotot'),

url(r'^s1210-detpgtobenpr-retpgtotot/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtobenpr_retpgtotot.salvar', 
        name='s1210_detpgtobenpr_retpgtotot_salvar'),



url(r'^s1210-detpgtobenpr-infopgtoparc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtobenpr_infopgtoparc.apagar', 
        name='s1210_detpgtobenpr_infopgtoparc_apagar'),

url(r'^s1210-detpgtobenpr-infopgtoparc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtobenpr_infopgtoparc.listar', 
        name='s1210_detpgtobenpr_infopgtoparc'),

url(r'^s1210-detpgtobenpr-infopgtoparc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtobenpr_infopgtoparc.salvar', 
        name='s1210_detpgtobenpr_infopgtoparc_salvar'),



url(r'^s1210-detpgtofer/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofer.apagar', 
        name='s1210_detpgtofer_apagar'),

url(r'^s1210-detpgtofer/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofer.listar', 
        name='s1210_detpgtofer'),

url(r'^s1210-detpgtofer/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofer.salvar', 
        name='s1210_detpgtofer_salvar'),

)


urlpatterns += patterns('',


url(r'^s1210-detpgtofer-detrubrfer/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofer_detrubrfer.apagar', 
        name='s1210_detpgtofer_detrubrfer_apagar'),

url(r'^s1210-detpgtofer-detrubrfer/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofer_detrubrfer.listar', 
        name='s1210_detpgtofer_detrubrfer'),

url(r'^s1210-detpgtofer-detrubrfer/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofer_detrubrfer.salvar', 
        name='s1210_detpgtofer_detrubrfer_salvar'),



url(r'^s1210-detpgtofer-penalim/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofer_penalim.apagar', 
        name='s1210_detpgtofer_penalim_apagar'),

url(r'^s1210-detpgtofer-penalim/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofer_penalim.listar', 
        name='s1210_detpgtofer_penalim'),

url(r'^s1210-detpgtofer-penalim/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtofer_penalim.salvar', 
        name='s1210_detpgtofer_penalim_salvar'),



url(r'^s1210-detpgtoant/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtoant.apagar', 
        name='s1210_detpgtoant_apagar'),

url(r'^s1210-detpgtoant/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtoant.listar', 
        name='s1210_detpgtoant'),

url(r'^s1210-detpgtoant/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtoant.salvar', 
        name='s1210_detpgtoant_salvar'),



url(r'^s1210-detpgtoant-infopgtoant/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtoant_infopgtoant.apagar', 
        name='s1210_detpgtoant_infopgtoant_apagar'),

url(r'^s1210-detpgtoant-infopgtoant/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtoant_infopgtoant.listar', 
        name='s1210_detpgtoant_infopgtoant'),

url(r'^s1210-detpgtoant-infopgtoant/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_detpgtoant_infopgtoant.salvar', 
        name='s1210_detpgtoant_infopgtoant_salvar'),



url(r'^s1210-idepgtoext/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_idepgtoext.apagar', 
        name='s1210_idepgtoext_apagar'),

url(r'^s1210-idepgtoext/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_idepgtoext.listar', 
        name='s1210_idepgtoext'),

url(r'^s1210-idepgtoext/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1210.views.s1210_idepgtoext.salvar', 
        name='s1210_idepgtoext_salvar'),





)