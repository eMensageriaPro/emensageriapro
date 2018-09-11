#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^r2070-inforesidext/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_inforesidext.apagar', 
        name='r2070_inforesidext_apagar'),

url(r'^r2070-inforesidext/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_inforesidext.listar', 
        name='r2070_inforesidext'),

url(r'^r2070-inforesidext/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_inforesidext.salvar', 
        name='r2070_inforesidext_salvar'),



url(r'^r2070-infomolestia/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_infomolestia.apagar', 
        name='r2070_infomolestia_apagar'),

url(r'^r2070-infomolestia/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_infomolestia.listar', 
        name='r2070_infomolestia'),

url(r'^r2070-infomolestia/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_infomolestia.salvar', 
        name='r2070_infomolestia_salvar'),



url(r'^r2070-ideestab/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_ideestab.apagar', 
        name='r2070_ideestab_apagar'),

url(r'^r2070-ideestab/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_ideestab.listar', 
        name='r2070_ideestab'),

url(r'^r2070-ideestab/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_ideestab.salvar', 
        name='r2070_ideestab_salvar'),



url(r'^r2070-pgtoresidbr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtoresidbr.apagar', 
        name='r2070_pgtoresidbr_apagar'),

url(r'^r2070-pgtoresidbr/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtoresidbr.listar', 
        name='r2070_pgtoresidbr'),

url(r'^r2070-pgtoresidbr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtoresidbr.salvar', 
        name='r2070_pgtoresidbr_salvar'),



url(r'^r2070-pgtopf/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopf.apagar', 
        name='r2070_pgtopf_apagar'),

url(r'^r2070-pgtopf/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopf.listar', 
        name='r2070_pgtopf'),

url(r'^r2070-pgtopf/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopf.salvar', 
        name='r2070_pgtopf_salvar'),



url(r'^r2070-detdeducao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_detdeducao.apagar', 
        name='r2070_detdeducao_apagar'),

url(r'^r2070-detdeducao/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_detdeducao.listar', 
        name='r2070_detdeducao'),

url(r'^r2070-detdeducao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_detdeducao.salvar', 
        name='r2070_detdeducao_salvar'),



url(r'^r2070-rendisento/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_rendisento.apagar', 
        name='r2070_rendisento_apagar'),

url(r'^r2070-rendisento/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_rendisento.listar', 
        name='r2070_rendisento'),

url(r'^r2070-rendisento/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_rendisento.salvar', 
        name='r2070_rendisento_salvar'),



url(r'^r2070-detcompet/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_detcompet.apagar', 
        name='r2070_detcompet_apagar'),

url(r'^r2070-detcompet/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_detcompet.listar', 
        name='r2070_detcompet'),

url(r'^r2070-detcompet/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_detcompet.salvar', 
        name='r2070_detcompet_salvar'),



url(r'^r2070-compjud/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_compjud.apagar', 
        name='r2070_compjud_apagar'),

url(r'^r2070-compjud/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_compjud.listar', 
        name='r2070_compjud'),

url(r'^r2070-compjud/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_compjud.salvar', 
        name='r2070_compjud_salvar'),



url(r'^r2070-inforra/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_inforra.apagar', 
        name='r2070_inforra_apagar'),

url(r'^r2070-inforra/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_inforra.listar', 
        name='r2070_inforra'),

url(r'^r2070-inforra/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_inforra.salvar', 
        name='r2070_inforra_salvar'),

)


urlpatterns += patterns('',


url(r'^r2070-inforra-despprocjud/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_inforra_despprocjud.apagar', 
        name='r2070_inforra_despprocjud_apagar'),

url(r'^r2070-inforra-despprocjud/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_inforra_despprocjud.listar', 
        name='r2070_inforra_despprocjud'),

url(r'^r2070-inforra-despprocjud/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_inforra_despprocjud.salvar', 
        name='r2070_inforra_despprocjud_salvar'),



url(r'^r2070-inforra-ideadvogado/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_inforra_ideadvogado.apagar', 
        name='r2070_inforra_ideadvogado_apagar'),

url(r'^r2070-inforra-ideadvogado/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_inforra_ideadvogado.listar', 
        name='r2070_inforra_ideadvogado'),

url(r'^r2070-inforra-ideadvogado/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_inforra_ideadvogado.salvar', 
        name='r2070_inforra_ideadvogado_salvar'),



url(r'^r2070-infoprocjud/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_infoprocjud.apagar', 
        name='r2070_infoprocjud_apagar'),

url(r'^r2070-infoprocjud/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_infoprocjud.listar', 
        name='r2070_infoprocjud'),

url(r'^r2070-infoprocjud/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_infoprocjud.salvar', 
        name='r2070_infoprocjud_salvar'),



url(r'^r2070-infoprocjud-despprocjud/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_infoprocjud_despprocjud.apagar', 
        name='r2070_infoprocjud_despprocjud_apagar'),

url(r'^r2070-infoprocjud-despprocjud/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_infoprocjud_despprocjud.listar', 
        name='r2070_infoprocjud_despprocjud'),

url(r'^r2070-infoprocjud-despprocjud/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_infoprocjud_despprocjud.salvar', 
        name='r2070_infoprocjud_despprocjud_salvar'),



url(r'^r2070-infoprocjud-ideadvogado/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_infoprocjud_ideadvogado.apagar', 
        name='r2070_infoprocjud_ideadvogado_apagar'),

url(r'^r2070-infoprocjud-ideadvogado/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_infoprocjud_ideadvogado.listar', 
        name='r2070_infoprocjud_ideadvogado'),

url(r'^r2070-infoprocjud-ideadvogado/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_infoprocjud_ideadvogado.salvar', 
        name='r2070_infoprocjud_ideadvogado_salvar'),



url(r'^r2070-infoprocjud-origemrecursos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_infoprocjud_origemrecursos.apagar', 
        name='r2070_infoprocjud_origemrecursos_apagar'),

url(r'^r2070-infoprocjud-origemrecursos/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_infoprocjud_origemrecursos.listar', 
        name='r2070_infoprocjud_origemrecursos'),

url(r'^r2070-infoprocjud-origemrecursos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_infoprocjud_origemrecursos.salvar', 
        name='r2070_infoprocjud_origemrecursos_salvar'),



url(r'^r2070-depjudicial/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_depjudicial.apagar', 
        name='r2070_depjudicial_apagar'),

url(r'^r2070-depjudicial/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_depjudicial.listar', 
        name='r2070_depjudicial'),

url(r'^r2070-depjudicial/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_depjudicial.salvar', 
        name='r2070_depjudicial_salvar'),



url(r'^r2070-pgtopj/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopj.apagar', 
        name='r2070_pgtopj_apagar'),

url(r'^r2070-pgtopj/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopj.listar', 
        name='r2070_pgtopj'),

url(r'^r2070-pgtopj/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopj.salvar', 
        name='r2070_pgtopj_salvar'),



url(r'^r2070-pgtopj-infoprocjud/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopj_infoprocjud.apagar', 
        name='r2070_pgtopj_infoprocjud_apagar'),

url(r'^r2070-pgtopj-infoprocjud/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopj_infoprocjud.listar', 
        name='r2070_pgtopj_infoprocjud'),

url(r'^r2070-pgtopj-infoprocjud/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopj_infoprocjud.salvar', 
        name='r2070_pgtopj_infoprocjud_salvar'),



url(r'^r2070-pgtopj-despprocjud/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopj_despprocjud.apagar', 
        name='r2070_pgtopj_despprocjud_apagar'),

url(r'^r2070-pgtopj-despprocjud/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopj_despprocjud.listar', 
        name='r2070_pgtopj_despprocjud'),

url(r'^r2070-pgtopj-despprocjud/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopj_despprocjud.salvar', 
        name='r2070_pgtopj_despprocjud_salvar'),

)


urlpatterns += patterns('',


url(r'^r2070-pgtopj-ideadvogado/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopj_ideadvogado.apagar', 
        name='r2070_pgtopj_ideadvogado_apagar'),

url(r'^r2070-pgtopj-ideadvogado/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopj_ideadvogado.listar', 
        name='r2070_pgtopj_ideadvogado'),

url(r'^r2070-pgtopj-ideadvogado/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopj_ideadvogado.salvar', 
        name='r2070_pgtopj_ideadvogado_salvar'),



url(r'^r2070-pgtopj-origemrecursos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopj_origemrecursos.apagar', 
        name='r2070_pgtopj_origemrecursos_apagar'),

url(r'^r2070-pgtopj-origemrecursos/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopj_origemrecursos.listar', 
        name='r2070_pgtopj_origemrecursos'),

url(r'^r2070-pgtopj-origemrecursos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtopj_origemrecursos.salvar', 
        name='r2070_pgtopj_origemrecursos_salvar'),



url(r'^r2070-pgtoresidext/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtoresidext.apagar', 
        name='r2070_pgtoresidext_apagar'),

url(r'^r2070-pgtoresidext/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtoresidext.listar', 
        name='r2070_pgtoresidext'),

url(r'^r2070-pgtoresidext/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2070.views.r2070_pgtoresidext.salvar', 
        name='r2070_pgtoresidext_salvar'),





)