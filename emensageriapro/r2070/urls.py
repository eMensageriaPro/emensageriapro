#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.r2070.views import r2070_inforesidext_apagar as r2070_inforesidext_apagar_views
from emensageriapro.r2070.views import r2070_inforesidext_listar as r2070_inforesidext_listar_views
from emensageriapro.r2070.views import r2070_inforesidext_salvar as r2070_inforesidext_salvar_views
from emensageriapro.r2070.views import r2070_inforesidext_api as r2070_inforesidext_api_views
from emensageriapro.r2070.views import r2070_infomolestia_apagar as r2070_infomolestia_apagar_views
from emensageriapro.r2070.views import r2070_infomolestia_listar as r2070_infomolestia_listar_views
from emensageriapro.r2070.views import r2070_infomolestia_salvar as r2070_infomolestia_salvar_views
from emensageriapro.r2070.views import r2070_infomolestia_api as r2070_infomolestia_api_views
from emensageriapro.r2070.views import r2070_ideestab_apagar as r2070_ideestab_apagar_views
from emensageriapro.r2070.views import r2070_ideestab_listar as r2070_ideestab_listar_views
from emensageriapro.r2070.views import r2070_ideestab_salvar as r2070_ideestab_salvar_views
from emensageriapro.r2070.views import r2070_ideestab_api as r2070_ideestab_api_views
from emensageriapro.r2070.views import r2070_pgtoresidbr_apagar as r2070_pgtoresidbr_apagar_views
from emensageriapro.r2070.views import r2070_pgtoresidbr_listar as r2070_pgtoresidbr_listar_views
from emensageriapro.r2070.views import r2070_pgtoresidbr_salvar as r2070_pgtoresidbr_salvar_views
from emensageriapro.r2070.views import r2070_pgtoresidbr_api as r2070_pgtoresidbr_api_views
from emensageriapro.r2070.views import r2070_pgtopf_apagar as r2070_pgtopf_apagar_views
from emensageriapro.r2070.views import r2070_pgtopf_listar as r2070_pgtopf_listar_views
from emensageriapro.r2070.views import r2070_pgtopf_salvar as r2070_pgtopf_salvar_views
from emensageriapro.r2070.views import r2070_pgtopf_api as r2070_pgtopf_api_views
from emensageriapro.r2070.views import r2070_detdeducao_apagar as r2070_detdeducao_apagar_views
from emensageriapro.r2070.views import r2070_detdeducao_listar as r2070_detdeducao_listar_views
from emensageriapro.r2070.views import r2070_detdeducao_salvar as r2070_detdeducao_salvar_views
from emensageriapro.r2070.views import r2070_detdeducao_api as r2070_detdeducao_api_views
from emensageriapro.r2070.views import r2070_rendisento_apagar as r2070_rendisento_apagar_views
from emensageriapro.r2070.views import r2070_rendisento_listar as r2070_rendisento_listar_views
from emensageriapro.r2070.views import r2070_rendisento_salvar as r2070_rendisento_salvar_views
from emensageriapro.r2070.views import r2070_rendisento_api as r2070_rendisento_api_views
from emensageriapro.r2070.views import r2070_detcompet_apagar as r2070_detcompet_apagar_views
from emensageriapro.r2070.views import r2070_detcompet_listar as r2070_detcompet_listar_views
from emensageriapro.r2070.views import r2070_detcompet_salvar as r2070_detcompet_salvar_views
from emensageriapro.r2070.views import r2070_detcompet_api as r2070_detcompet_api_views
from emensageriapro.r2070.views import r2070_compjud_apagar as r2070_compjud_apagar_views
from emensageriapro.r2070.views import r2070_compjud_listar as r2070_compjud_listar_views
from emensageriapro.r2070.views import r2070_compjud_salvar as r2070_compjud_salvar_views
from emensageriapro.r2070.views import r2070_compjud_api as r2070_compjud_api_views
from emensageriapro.r2070.views import r2070_inforra_apagar as r2070_inforra_apagar_views
from emensageriapro.r2070.views import r2070_inforra_listar as r2070_inforra_listar_views
from emensageriapro.r2070.views import r2070_inforra_salvar as r2070_inforra_salvar_views
from emensageriapro.r2070.views import r2070_inforra_api as r2070_inforra_api_views
from emensageriapro.r2070.views import r2070_inforra_despprocjud_apagar as r2070_inforra_despprocjud_apagar_views
from emensageriapro.r2070.views import r2070_inforra_despprocjud_listar as r2070_inforra_despprocjud_listar_views
from emensageriapro.r2070.views import r2070_inforra_despprocjud_salvar as r2070_inforra_despprocjud_salvar_views
from emensageriapro.r2070.views import r2070_inforra_despprocjud_api as r2070_inforra_despprocjud_api_views
from emensageriapro.r2070.views import r2070_inforra_ideadvogado_apagar as r2070_inforra_ideadvogado_apagar_views
from emensageriapro.r2070.views import r2070_inforra_ideadvogado_listar as r2070_inforra_ideadvogado_listar_views
from emensageriapro.r2070.views import r2070_inforra_ideadvogado_salvar as r2070_inforra_ideadvogado_salvar_views
from emensageriapro.r2070.views import r2070_inforra_ideadvogado_api as r2070_inforra_ideadvogado_api_views
from emensageriapro.r2070.views import r2070_infoprocjud_apagar as r2070_infoprocjud_apagar_views
from emensageriapro.r2070.views import r2070_infoprocjud_listar as r2070_infoprocjud_listar_views
from emensageriapro.r2070.views import r2070_infoprocjud_salvar as r2070_infoprocjud_salvar_views
from emensageriapro.r2070.views import r2070_infoprocjud_api as r2070_infoprocjud_api_views
from emensageriapro.r2070.views import r2070_infoprocjud_despprocjud_apagar as r2070_infoprocjud_despprocjud_apagar_views
from emensageriapro.r2070.views import r2070_infoprocjud_despprocjud_listar as r2070_infoprocjud_despprocjud_listar_views
from emensageriapro.r2070.views import r2070_infoprocjud_despprocjud_salvar as r2070_infoprocjud_despprocjud_salvar_views
from emensageriapro.r2070.views import r2070_infoprocjud_despprocjud_api as r2070_infoprocjud_despprocjud_api_views
from emensageriapro.r2070.views import r2070_infoprocjud_ideadvogado_apagar as r2070_infoprocjud_ideadvogado_apagar_views
from emensageriapro.r2070.views import r2070_infoprocjud_ideadvogado_listar as r2070_infoprocjud_ideadvogado_listar_views
from emensageriapro.r2070.views import r2070_infoprocjud_ideadvogado_salvar as r2070_infoprocjud_ideadvogado_salvar_views
from emensageriapro.r2070.views import r2070_infoprocjud_ideadvogado_api as r2070_infoprocjud_ideadvogado_api_views
from emensageriapro.r2070.views import r2070_infoprocjud_origemrecursos_apagar as r2070_infoprocjud_origemrecursos_apagar_views
from emensageriapro.r2070.views import r2070_infoprocjud_origemrecursos_listar as r2070_infoprocjud_origemrecursos_listar_views
from emensageriapro.r2070.views import r2070_infoprocjud_origemrecursos_salvar as r2070_infoprocjud_origemrecursos_salvar_views
from emensageriapro.r2070.views import r2070_infoprocjud_origemrecursos_api as r2070_infoprocjud_origemrecursos_api_views
from emensageriapro.r2070.views import r2070_depjudicial_apagar as r2070_depjudicial_apagar_views
from emensageriapro.r2070.views import r2070_depjudicial_listar as r2070_depjudicial_listar_views
from emensageriapro.r2070.views import r2070_depjudicial_salvar as r2070_depjudicial_salvar_views
from emensageriapro.r2070.views import r2070_depjudicial_api as r2070_depjudicial_api_views
from emensageriapro.r2070.views import r2070_pgtopj_apagar as r2070_pgtopj_apagar_views
from emensageriapro.r2070.views import r2070_pgtopj_listar as r2070_pgtopj_listar_views
from emensageriapro.r2070.views import r2070_pgtopj_salvar as r2070_pgtopj_salvar_views
from emensageriapro.r2070.views import r2070_pgtopj_api as r2070_pgtopj_api_views
from emensageriapro.r2070.views import r2070_pgtopj_infoprocjud_apagar as r2070_pgtopj_infoprocjud_apagar_views
from emensageriapro.r2070.views import r2070_pgtopj_infoprocjud_listar as r2070_pgtopj_infoprocjud_listar_views
from emensageriapro.r2070.views import r2070_pgtopj_infoprocjud_salvar as r2070_pgtopj_infoprocjud_salvar_views
from emensageriapro.r2070.views import r2070_pgtopj_infoprocjud_api as r2070_pgtopj_infoprocjud_api_views
from emensageriapro.r2070.views import r2070_pgtopj_despprocjud_apagar as r2070_pgtopj_despprocjud_apagar_views
from emensageriapro.r2070.views import r2070_pgtopj_despprocjud_listar as r2070_pgtopj_despprocjud_listar_views
from emensageriapro.r2070.views import r2070_pgtopj_despprocjud_salvar as r2070_pgtopj_despprocjud_salvar_views
from emensageriapro.r2070.views import r2070_pgtopj_despprocjud_api as r2070_pgtopj_despprocjud_api_views
from emensageriapro.r2070.views import r2070_pgtopj_ideadvogado_apagar as r2070_pgtopj_ideadvogado_apagar_views
from emensageriapro.r2070.views import r2070_pgtopj_ideadvogado_listar as r2070_pgtopj_ideadvogado_listar_views
from emensageriapro.r2070.views import r2070_pgtopj_ideadvogado_salvar as r2070_pgtopj_ideadvogado_salvar_views
from emensageriapro.r2070.views import r2070_pgtopj_ideadvogado_api as r2070_pgtopj_ideadvogado_api_views
from emensageriapro.r2070.views import r2070_pgtopj_origemrecursos_apagar as r2070_pgtopj_origemrecursos_apagar_views
from emensageriapro.r2070.views import r2070_pgtopj_origemrecursos_listar as r2070_pgtopj_origemrecursos_listar_views
from emensageriapro.r2070.views import r2070_pgtopj_origemrecursos_salvar as r2070_pgtopj_origemrecursos_salvar_views
from emensageriapro.r2070.views import r2070_pgtopj_origemrecursos_api as r2070_pgtopj_origemrecursos_api_views
from emensageriapro.r2070.views import r2070_pgtoresidext_apagar as r2070_pgtoresidext_apagar_views
from emensageriapro.r2070.views import r2070_pgtoresidext_listar as r2070_pgtoresidext_listar_views
from emensageriapro.r2070.views import r2070_pgtoresidext_salvar as r2070_pgtoresidext_salvar_views
from emensageriapro.r2070.views import r2070_pgtoresidext_api as r2070_pgtoresidext_api_views



"""

    eMensageria - Sistema Open-Source de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""


urlpatterns = [


    url(r'^r2070-inforesidext/apagar/(?P<pk>[0-9]+)/$', 
        r2070_inforesidext_apagar_views.apagar, 
        name='r2070_inforesidext_apagar'),

    url(r'^r2070-inforesidext/api/$',
        r2070_inforesidext_api_views.r2070infoResidExtList.as_view() ),

    url(r'^r2070-inforesidext/api/(?P<pk>[0-9]+)/$',
        r2070_inforesidext_api_views.r2070infoResidExtDetail.as_view() ),

    url(r'^r2070-inforesidext/$', 
        r2070_inforesidext_listar_views.listar, 
        name='r2070_inforesidext'),

    url(r'^r2070-inforesidext/salvar/(?P<pk>[0-9]+)/$', 
        r2070_inforesidext_salvar_views.salvar, 
        name='r2070_inforesidext_salvar'),

    url(r'^r2070-inforesidext/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_inforesidext_salvar_views.salvar, 
        name='r2070_inforesidext_salvar_tab'),
        
    url(r'^r2070-inforesidext/cadastrar/$', 
        r2070_inforesidext_salvar_views.salvar, 
        name='r2070_inforesidext_cadastrar'),

    url(r'^r2070-inforesidext/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_inforesidext_salvar_views.salvar, 
        name='r2070_inforesidext_salvar_output'),
        
    url(r'^r2070-inforesidext/(?P<output>[\w-]+)/$', 
        r2070_inforesidext_listar_views.listar, 
        name='r2070_inforesidext_output'),

    url(r'^r2070-infomolestia/apagar/(?P<pk>[0-9]+)/$', 
        r2070_infomolestia_apagar_views.apagar, 
        name='r2070_infomolestia_apagar'),

    url(r'^r2070-infomolestia/api/$',
        r2070_infomolestia_api_views.r2070infoMolestiaList.as_view() ),

    url(r'^r2070-infomolestia/api/(?P<pk>[0-9]+)/$',
        r2070_infomolestia_api_views.r2070infoMolestiaDetail.as_view() ),

    url(r'^r2070-infomolestia/$', 
        r2070_infomolestia_listar_views.listar, 
        name='r2070_infomolestia'),

    url(r'^r2070-infomolestia/salvar/(?P<pk>[0-9]+)/$', 
        r2070_infomolestia_salvar_views.salvar, 
        name='r2070_infomolestia_salvar'),

    url(r'^r2070-infomolestia/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_infomolestia_salvar_views.salvar, 
        name='r2070_infomolestia_salvar_tab'),
        
    url(r'^r2070-infomolestia/cadastrar/$', 
        r2070_infomolestia_salvar_views.salvar, 
        name='r2070_infomolestia_cadastrar'),

    url(r'^r2070-infomolestia/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_infomolestia_salvar_views.salvar, 
        name='r2070_infomolestia_salvar_output'),
        
    url(r'^r2070-infomolestia/(?P<output>[\w-]+)/$', 
        r2070_infomolestia_listar_views.listar, 
        name='r2070_infomolestia_output'),

    url(r'^r2070-ideestab/apagar/(?P<pk>[0-9]+)/$', 
        r2070_ideestab_apagar_views.apagar, 
        name='r2070_ideestab_apagar'),

    url(r'^r2070-ideestab/api/$',
        r2070_ideestab_api_views.r2070ideEstabList.as_view() ),

    url(r'^r2070-ideestab/api/(?P<pk>[0-9]+)/$',
        r2070_ideestab_api_views.r2070ideEstabDetail.as_view() ),

    url(r'^r2070-ideestab/$', 
        r2070_ideestab_listar_views.listar, 
        name='r2070_ideestab'),

    url(r'^r2070-ideestab/salvar/(?P<pk>[0-9]+)/$', 
        r2070_ideestab_salvar_views.salvar, 
        name='r2070_ideestab_salvar'),

    url(r'^r2070-ideestab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_ideestab_salvar_views.salvar, 
        name='r2070_ideestab_salvar_tab'),
        
    url(r'^r2070-ideestab/cadastrar/$', 
        r2070_ideestab_salvar_views.salvar, 
        name='r2070_ideestab_cadastrar'),

    url(r'^r2070-ideestab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_ideestab_salvar_views.salvar, 
        name='r2070_ideestab_salvar_output'),
        
    url(r'^r2070-ideestab/(?P<output>[\w-]+)/$', 
        r2070_ideestab_listar_views.listar, 
        name='r2070_ideestab_output'),

    url(r'^r2070-pgtoresidbr/apagar/(?P<pk>[0-9]+)/$', 
        r2070_pgtoresidbr_apagar_views.apagar, 
        name='r2070_pgtoresidbr_apagar'),

    url(r'^r2070-pgtoresidbr/api/$',
        r2070_pgtoresidbr_api_views.r2070pgtoResidBRList.as_view() ),

    url(r'^r2070-pgtoresidbr/api/(?P<pk>[0-9]+)/$',
        r2070_pgtoresidbr_api_views.r2070pgtoResidBRDetail.as_view() ),

    url(r'^r2070-pgtoresidbr/$', 
        r2070_pgtoresidbr_listar_views.listar, 
        name='r2070_pgtoresidbr'),

    url(r'^r2070-pgtoresidbr/salvar/(?P<pk>[0-9]+)/$', 
        r2070_pgtoresidbr_salvar_views.salvar, 
        name='r2070_pgtoresidbr_salvar'),

    url(r'^r2070-pgtoresidbr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_pgtoresidbr_salvar_views.salvar, 
        name='r2070_pgtoresidbr_salvar_tab'),
        
    url(r'^r2070-pgtoresidbr/cadastrar/$', 
        r2070_pgtoresidbr_salvar_views.salvar, 
        name='r2070_pgtoresidbr_cadastrar'),

    url(r'^r2070-pgtoresidbr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_pgtoresidbr_salvar_views.salvar, 
        name='r2070_pgtoresidbr_salvar_output'),
        
    url(r'^r2070-pgtoresidbr/(?P<output>[\w-]+)/$', 
        r2070_pgtoresidbr_listar_views.listar, 
        name='r2070_pgtoresidbr_output'),

    url(r'^r2070-pgtopf/apagar/(?P<pk>[0-9]+)/$', 
        r2070_pgtopf_apagar_views.apagar, 
        name='r2070_pgtopf_apagar'),

    url(r'^r2070-pgtopf/api/$',
        r2070_pgtopf_api_views.r2070pgtoPFList.as_view() ),

    url(r'^r2070-pgtopf/api/(?P<pk>[0-9]+)/$',
        r2070_pgtopf_api_views.r2070pgtoPFDetail.as_view() ),

    url(r'^r2070-pgtopf/$', 
        r2070_pgtopf_listar_views.listar, 
        name='r2070_pgtopf'),

    url(r'^r2070-pgtopf/salvar/(?P<pk>[0-9]+)/$', 
        r2070_pgtopf_salvar_views.salvar, 
        name='r2070_pgtopf_salvar'),

    url(r'^r2070-pgtopf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_pgtopf_salvar_views.salvar, 
        name='r2070_pgtopf_salvar_tab'),
        
    url(r'^r2070-pgtopf/cadastrar/$', 
        r2070_pgtopf_salvar_views.salvar, 
        name='r2070_pgtopf_cadastrar'),

    url(r'^r2070-pgtopf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_pgtopf_salvar_views.salvar, 
        name='r2070_pgtopf_salvar_output'),
        
    url(r'^r2070-pgtopf/(?P<output>[\w-]+)/$', 
        r2070_pgtopf_listar_views.listar, 
        name='r2070_pgtopf_output'),

    url(r'^r2070-detdeducao/apagar/(?P<pk>[0-9]+)/$', 
        r2070_detdeducao_apagar_views.apagar, 
        name='r2070_detdeducao_apagar'),

    url(r'^r2070-detdeducao/api/$',
        r2070_detdeducao_api_views.r2070detDeducaoList.as_view() ),

    url(r'^r2070-detdeducao/api/(?P<pk>[0-9]+)/$',
        r2070_detdeducao_api_views.r2070detDeducaoDetail.as_view() ),

    url(r'^r2070-detdeducao/$', 
        r2070_detdeducao_listar_views.listar, 
        name='r2070_detdeducao'),

    url(r'^r2070-detdeducao/salvar/(?P<pk>[0-9]+)/$', 
        r2070_detdeducao_salvar_views.salvar, 
        name='r2070_detdeducao_salvar'),

    url(r'^r2070-detdeducao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_detdeducao_salvar_views.salvar, 
        name='r2070_detdeducao_salvar_tab'),
        
    url(r'^r2070-detdeducao/cadastrar/$', 
        r2070_detdeducao_salvar_views.salvar, 
        name='r2070_detdeducao_cadastrar'),

    url(r'^r2070-detdeducao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_detdeducao_salvar_views.salvar, 
        name='r2070_detdeducao_salvar_output'),
        
    url(r'^r2070-detdeducao/(?P<output>[\w-]+)/$', 
        r2070_detdeducao_listar_views.listar, 
        name='r2070_detdeducao_output'),

    url(r'^r2070-rendisento/apagar/(?P<pk>[0-9]+)/$', 
        r2070_rendisento_apagar_views.apagar, 
        name='r2070_rendisento_apagar'),

    url(r'^r2070-rendisento/api/$',
        r2070_rendisento_api_views.r2070rendIsentoList.as_view() ),

    url(r'^r2070-rendisento/api/(?P<pk>[0-9]+)/$',
        r2070_rendisento_api_views.r2070rendIsentoDetail.as_view() ),

    url(r'^r2070-rendisento/$', 
        r2070_rendisento_listar_views.listar, 
        name='r2070_rendisento'),

    url(r'^r2070-rendisento/salvar/(?P<pk>[0-9]+)/$', 
        r2070_rendisento_salvar_views.salvar, 
        name='r2070_rendisento_salvar'),

    url(r'^r2070-rendisento/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_rendisento_salvar_views.salvar, 
        name='r2070_rendisento_salvar_tab'),
        
    url(r'^r2070-rendisento/cadastrar/$', 
        r2070_rendisento_salvar_views.salvar, 
        name='r2070_rendisento_cadastrar'),

    url(r'^r2070-rendisento/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_rendisento_salvar_views.salvar, 
        name='r2070_rendisento_salvar_output'),
        
    url(r'^r2070-rendisento/(?P<output>[\w-]+)/$', 
        r2070_rendisento_listar_views.listar, 
        name='r2070_rendisento_output'),

    url(r'^r2070-detcompet/apagar/(?P<pk>[0-9]+)/$', 
        r2070_detcompet_apagar_views.apagar, 
        name='r2070_detcompet_apagar'),

    url(r'^r2070-detcompet/api/$',
        r2070_detcompet_api_views.r2070detCompetList.as_view() ),

    url(r'^r2070-detcompet/api/(?P<pk>[0-9]+)/$',
        r2070_detcompet_api_views.r2070detCompetDetail.as_view() ),

    url(r'^r2070-detcompet/$', 
        r2070_detcompet_listar_views.listar, 
        name='r2070_detcompet'),

    url(r'^r2070-detcompet/salvar/(?P<pk>[0-9]+)/$', 
        r2070_detcompet_salvar_views.salvar, 
        name='r2070_detcompet_salvar'),

    url(r'^r2070-detcompet/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_detcompet_salvar_views.salvar, 
        name='r2070_detcompet_salvar_tab'),
        
    url(r'^r2070-detcompet/cadastrar/$', 
        r2070_detcompet_salvar_views.salvar, 
        name='r2070_detcompet_cadastrar'),

    url(r'^r2070-detcompet/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_detcompet_salvar_views.salvar, 
        name='r2070_detcompet_salvar_output'),
        
    url(r'^r2070-detcompet/(?P<output>[\w-]+)/$', 
        r2070_detcompet_listar_views.listar, 
        name='r2070_detcompet_output'),

    url(r'^r2070-compjud/apagar/(?P<pk>[0-9]+)/$', 
        r2070_compjud_apagar_views.apagar, 
        name='r2070_compjud_apagar'),

    url(r'^r2070-compjud/api/$',
        r2070_compjud_api_views.r2070compJudList.as_view() ),

    url(r'^r2070-compjud/api/(?P<pk>[0-9]+)/$',
        r2070_compjud_api_views.r2070compJudDetail.as_view() ),

    url(r'^r2070-compjud/$', 
        r2070_compjud_listar_views.listar, 
        name='r2070_compjud'),

    url(r'^r2070-compjud/salvar/(?P<pk>[0-9]+)/$', 
        r2070_compjud_salvar_views.salvar, 
        name='r2070_compjud_salvar'),

    url(r'^r2070-compjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_compjud_salvar_views.salvar, 
        name='r2070_compjud_salvar_tab'),
        
    url(r'^r2070-compjud/cadastrar/$', 
        r2070_compjud_salvar_views.salvar, 
        name='r2070_compjud_cadastrar'),

    url(r'^r2070-compjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_compjud_salvar_views.salvar, 
        name='r2070_compjud_salvar_output'),
        
    url(r'^r2070-compjud/(?P<output>[\w-]+)/$', 
        r2070_compjud_listar_views.listar, 
        name='r2070_compjud_output'),

    url(r'^r2070-inforra/apagar/(?P<pk>[0-9]+)/$', 
        r2070_inforra_apagar_views.apagar, 
        name='r2070_inforra_apagar'),

    url(r'^r2070-inforra/api/$',
        r2070_inforra_api_views.r2070infoRRAList.as_view() ),

    url(r'^r2070-inforra/api/(?P<pk>[0-9]+)/$',
        r2070_inforra_api_views.r2070infoRRADetail.as_view() ),

    url(r'^r2070-inforra/$', 
        r2070_inforra_listar_views.listar, 
        name='r2070_inforra'),

    url(r'^r2070-inforra/salvar/(?P<pk>[0-9]+)/$', 
        r2070_inforra_salvar_views.salvar, 
        name='r2070_inforra_salvar'),

    url(r'^r2070-inforra/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_inforra_salvar_views.salvar, 
        name='r2070_inforra_salvar_tab'),
        
    url(r'^r2070-inforra/cadastrar/$', 
        r2070_inforra_salvar_views.salvar, 
        name='r2070_inforra_cadastrar'),

    url(r'^r2070-inforra/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_inforra_salvar_views.salvar, 
        name='r2070_inforra_salvar_output'),
        
    url(r'^r2070-inforra/(?P<output>[\w-]+)/$', 
        r2070_inforra_listar_views.listar, 
        name='r2070_inforra_output'),

    url(r'^r2070-inforra-despprocjud/apagar/(?P<pk>[0-9]+)/$', 
        r2070_inforra_despprocjud_apagar_views.apagar, 
        name='r2070_inforra_despprocjud_apagar'),

    url(r'^r2070-inforra-despprocjud/api/$',
        r2070_inforra_despprocjud_api_views.r2070infoRRAdespProcJudList.as_view() ),

    url(r'^r2070-inforra-despprocjud/api/(?P<pk>[0-9]+)/$',
        r2070_inforra_despprocjud_api_views.r2070infoRRAdespProcJudDetail.as_view() ),

    url(r'^r2070-inforra-despprocjud/$', 
        r2070_inforra_despprocjud_listar_views.listar, 
        name='r2070_inforra_despprocjud'),

    url(r'^r2070-inforra-despprocjud/salvar/(?P<pk>[0-9]+)/$', 
        r2070_inforra_despprocjud_salvar_views.salvar, 
        name='r2070_inforra_despprocjud_salvar'),

    url(r'^r2070-inforra-despprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_inforra_despprocjud_salvar_views.salvar, 
        name='r2070_inforra_despprocjud_salvar_tab'),
        
    url(r'^r2070-inforra-despprocjud/cadastrar/$', 
        r2070_inforra_despprocjud_salvar_views.salvar, 
        name='r2070_inforra_despprocjud_cadastrar'),

    url(r'^r2070-inforra-despprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_inforra_despprocjud_salvar_views.salvar, 
        name='r2070_inforra_despprocjud_salvar_output'),
        
    url(r'^r2070-inforra-despprocjud/(?P<output>[\w-]+)/$', 
        r2070_inforra_despprocjud_listar_views.listar, 
        name='r2070_inforra_despprocjud_output'),

    url(r'^r2070-inforra-ideadvogado/apagar/(?P<pk>[0-9]+)/$', 
        r2070_inforra_ideadvogado_apagar_views.apagar, 
        name='r2070_inforra_ideadvogado_apagar'),

    url(r'^r2070-inforra-ideadvogado/api/$',
        r2070_inforra_ideadvogado_api_views.r2070infoRRAideAdvogadoList.as_view() ),

    url(r'^r2070-inforra-ideadvogado/api/(?P<pk>[0-9]+)/$',
        r2070_inforra_ideadvogado_api_views.r2070infoRRAideAdvogadoDetail.as_view() ),

    url(r'^r2070-inforra-ideadvogado/$', 
        r2070_inforra_ideadvogado_listar_views.listar, 
        name='r2070_inforra_ideadvogado'),

    url(r'^r2070-inforra-ideadvogado/salvar/(?P<pk>[0-9]+)/$', 
        r2070_inforra_ideadvogado_salvar_views.salvar, 
        name='r2070_inforra_ideadvogado_salvar'),

    url(r'^r2070-inforra-ideadvogado/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_inforra_ideadvogado_salvar_views.salvar, 
        name='r2070_inforra_ideadvogado_salvar_tab'),
        
    url(r'^r2070-inforra-ideadvogado/cadastrar/$', 
        r2070_inforra_ideadvogado_salvar_views.salvar, 
        name='r2070_inforra_ideadvogado_cadastrar'),

    url(r'^r2070-inforra-ideadvogado/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_inforra_ideadvogado_salvar_views.salvar, 
        name='r2070_inforra_ideadvogado_salvar_output'),
        
    url(r'^r2070-inforra-ideadvogado/(?P<output>[\w-]+)/$', 
        r2070_inforra_ideadvogado_listar_views.listar, 
        name='r2070_inforra_ideadvogado_output'),

    url(r'^r2070-infoprocjud/apagar/(?P<pk>[0-9]+)/$', 
        r2070_infoprocjud_apagar_views.apagar, 
        name='r2070_infoprocjud_apagar'),

    url(r'^r2070-infoprocjud/api/$',
        r2070_infoprocjud_api_views.r2070infoProcJudList.as_view() ),

    url(r'^r2070-infoprocjud/api/(?P<pk>[0-9]+)/$',
        r2070_infoprocjud_api_views.r2070infoProcJudDetail.as_view() ),

    url(r'^r2070-infoprocjud/$', 
        r2070_infoprocjud_listar_views.listar, 
        name='r2070_infoprocjud'),

    url(r'^r2070-infoprocjud/salvar/(?P<pk>[0-9]+)/$', 
        r2070_infoprocjud_salvar_views.salvar, 
        name='r2070_infoprocjud_salvar'),

    url(r'^r2070-infoprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_infoprocjud_salvar_views.salvar, 
        name='r2070_infoprocjud_salvar_tab'),
        
    url(r'^r2070-infoprocjud/cadastrar/$', 
        r2070_infoprocjud_salvar_views.salvar, 
        name='r2070_infoprocjud_cadastrar'),

    url(r'^r2070-infoprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_infoprocjud_salvar_views.salvar, 
        name='r2070_infoprocjud_salvar_output'),
        
    url(r'^r2070-infoprocjud/(?P<output>[\w-]+)/$', 
        r2070_infoprocjud_listar_views.listar, 
        name='r2070_infoprocjud_output'),

    url(r'^r2070-infoprocjud-despprocjud/apagar/(?P<pk>[0-9]+)/$', 
        r2070_infoprocjud_despprocjud_apagar_views.apagar, 
        name='r2070_infoprocjud_despprocjud_apagar'),

    url(r'^r2070-infoprocjud-despprocjud/api/$',
        r2070_infoprocjud_despprocjud_api_views.r2070infoProcJuddespProcJudList.as_view() ),

    url(r'^r2070-infoprocjud-despprocjud/api/(?P<pk>[0-9]+)/$',
        r2070_infoprocjud_despprocjud_api_views.r2070infoProcJuddespProcJudDetail.as_view() ),

    url(r'^r2070-infoprocjud-despprocjud/$', 
        r2070_infoprocjud_despprocjud_listar_views.listar, 
        name='r2070_infoprocjud_despprocjud'),

    url(r'^r2070-infoprocjud-despprocjud/salvar/(?P<pk>[0-9]+)/$', 
        r2070_infoprocjud_despprocjud_salvar_views.salvar, 
        name='r2070_infoprocjud_despprocjud_salvar'),

    url(r'^r2070-infoprocjud-despprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_infoprocjud_despprocjud_salvar_views.salvar, 
        name='r2070_infoprocjud_despprocjud_salvar_tab'),
        
    url(r'^r2070-infoprocjud-despprocjud/cadastrar/$', 
        r2070_infoprocjud_despprocjud_salvar_views.salvar, 
        name='r2070_infoprocjud_despprocjud_cadastrar'),

    url(r'^r2070-infoprocjud-despprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_infoprocjud_despprocjud_salvar_views.salvar, 
        name='r2070_infoprocjud_despprocjud_salvar_output'),
        
    url(r'^r2070-infoprocjud-despprocjud/(?P<output>[\w-]+)/$', 
        r2070_infoprocjud_despprocjud_listar_views.listar, 
        name='r2070_infoprocjud_despprocjud_output'),

    url(r'^r2070-infoprocjud-ideadvogado/apagar/(?P<pk>[0-9]+)/$', 
        r2070_infoprocjud_ideadvogado_apagar_views.apagar, 
        name='r2070_infoprocjud_ideadvogado_apagar'),

    url(r'^r2070-infoprocjud-ideadvogado/api/$',
        r2070_infoprocjud_ideadvogado_api_views.r2070infoProcJudideAdvogadoList.as_view() ),

    url(r'^r2070-infoprocjud-ideadvogado/api/(?P<pk>[0-9]+)/$',
        r2070_infoprocjud_ideadvogado_api_views.r2070infoProcJudideAdvogadoDetail.as_view() ),

    url(r'^r2070-infoprocjud-ideadvogado/$', 
        r2070_infoprocjud_ideadvogado_listar_views.listar, 
        name='r2070_infoprocjud_ideadvogado'),

    url(r'^r2070-infoprocjud-ideadvogado/salvar/(?P<pk>[0-9]+)/$', 
        r2070_infoprocjud_ideadvogado_salvar_views.salvar, 
        name='r2070_infoprocjud_ideadvogado_salvar'),

    url(r'^r2070-infoprocjud-ideadvogado/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_infoprocjud_ideadvogado_salvar_views.salvar, 
        name='r2070_infoprocjud_ideadvogado_salvar_tab'),
        
    url(r'^r2070-infoprocjud-ideadvogado/cadastrar/$', 
        r2070_infoprocjud_ideadvogado_salvar_views.salvar, 
        name='r2070_infoprocjud_ideadvogado_cadastrar'),

    url(r'^r2070-infoprocjud-ideadvogado/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_infoprocjud_ideadvogado_salvar_views.salvar, 
        name='r2070_infoprocjud_ideadvogado_salvar_output'),
        
    url(r'^r2070-infoprocjud-ideadvogado/(?P<output>[\w-]+)/$', 
        r2070_infoprocjud_ideadvogado_listar_views.listar, 
        name='r2070_infoprocjud_ideadvogado_output'),

    url(r'^r2070-infoprocjud-origemrecursos/apagar/(?P<pk>[0-9]+)/$', 
        r2070_infoprocjud_origemrecursos_apagar_views.apagar, 
        name='r2070_infoprocjud_origemrecursos_apagar'),

    url(r'^r2070-infoprocjud-origemrecursos/api/$',
        r2070_infoprocjud_origemrecursos_api_views.r2070infoProcJudorigemRecursosList.as_view() ),

    url(r'^r2070-infoprocjud-origemrecursos/api/(?P<pk>[0-9]+)/$',
        r2070_infoprocjud_origemrecursos_api_views.r2070infoProcJudorigemRecursosDetail.as_view() ),

    url(r'^r2070-infoprocjud-origemrecursos/$', 
        r2070_infoprocjud_origemrecursos_listar_views.listar, 
        name='r2070_infoprocjud_origemrecursos'),

    url(r'^r2070-infoprocjud-origemrecursos/salvar/(?P<pk>[0-9]+)/$', 
        r2070_infoprocjud_origemrecursos_salvar_views.salvar, 
        name='r2070_infoprocjud_origemrecursos_salvar'),

    url(r'^r2070-infoprocjud-origemrecursos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_infoprocjud_origemrecursos_salvar_views.salvar, 
        name='r2070_infoprocjud_origemrecursos_salvar_tab'),
        
    url(r'^r2070-infoprocjud-origemrecursos/cadastrar/$', 
        r2070_infoprocjud_origemrecursos_salvar_views.salvar, 
        name='r2070_infoprocjud_origemrecursos_cadastrar'),

    url(r'^r2070-infoprocjud-origemrecursos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_infoprocjud_origemrecursos_salvar_views.salvar, 
        name='r2070_infoprocjud_origemrecursos_salvar_output'),
        
    url(r'^r2070-infoprocjud-origemrecursos/(?P<output>[\w-]+)/$', 
        r2070_infoprocjud_origemrecursos_listar_views.listar, 
        name='r2070_infoprocjud_origemrecursos_output'),

    url(r'^r2070-depjudicial/apagar/(?P<pk>[0-9]+)/$', 
        r2070_depjudicial_apagar_views.apagar, 
        name='r2070_depjudicial_apagar'),

    url(r'^r2070-depjudicial/api/$',
        r2070_depjudicial_api_views.r2070depJudicialList.as_view() ),

    url(r'^r2070-depjudicial/api/(?P<pk>[0-9]+)/$',
        r2070_depjudicial_api_views.r2070depJudicialDetail.as_view() ),

    url(r'^r2070-depjudicial/$', 
        r2070_depjudicial_listar_views.listar, 
        name='r2070_depjudicial'),

    url(r'^r2070-depjudicial/salvar/(?P<pk>[0-9]+)/$', 
        r2070_depjudicial_salvar_views.salvar, 
        name='r2070_depjudicial_salvar'),

    url(r'^r2070-depjudicial/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_depjudicial_salvar_views.salvar, 
        name='r2070_depjudicial_salvar_tab'),
        
    url(r'^r2070-depjudicial/cadastrar/$', 
        r2070_depjudicial_salvar_views.salvar, 
        name='r2070_depjudicial_cadastrar'),

    url(r'^r2070-depjudicial/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_depjudicial_salvar_views.salvar, 
        name='r2070_depjudicial_salvar_output'),
        
    url(r'^r2070-depjudicial/(?P<output>[\w-]+)/$', 
        r2070_depjudicial_listar_views.listar, 
        name='r2070_depjudicial_output'),

    url(r'^r2070-pgtopj/apagar/(?P<pk>[0-9]+)/$', 
        r2070_pgtopj_apagar_views.apagar, 
        name='r2070_pgtopj_apagar'),

    url(r'^r2070-pgtopj/api/$',
        r2070_pgtopj_api_views.r2070pgtoPJList.as_view() ),

    url(r'^r2070-pgtopj/api/(?P<pk>[0-9]+)/$',
        r2070_pgtopj_api_views.r2070pgtoPJDetail.as_view() ),

    url(r'^r2070-pgtopj/$', 
        r2070_pgtopj_listar_views.listar, 
        name='r2070_pgtopj'),

    url(r'^r2070-pgtopj/salvar/(?P<pk>[0-9]+)/$', 
        r2070_pgtopj_salvar_views.salvar, 
        name='r2070_pgtopj_salvar'),

    url(r'^r2070-pgtopj/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_pgtopj_salvar_views.salvar, 
        name='r2070_pgtopj_salvar_tab'),
        
    url(r'^r2070-pgtopj/cadastrar/$', 
        r2070_pgtopj_salvar_views.salvar, 
        name='r2070_pgtopj_cadastrar'),

    url(r'^r2070-pgtopj/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_pgtopj_salvar_views.salvar, 
        name='r2070_pgtopj_salvar_output'),
        
    url(r'^r2070-pgtopj/(?P<output>[\w-]+)/$', 
        r2070_pgtopj_listar_views.listar, 
        name='r2070_pgtopj_output'),

    url(r'^r2070-pgtopj-infoprocjud/apagar/(?P<pk>[0-9]+)/$', 
        r2070_pgtopj_infoprocjud_apagar_views.apagar, 
        name='r2070_pgtopj_infoprocjud_apagar'),

    url(r'^r2070-pgtopj-infoprocjud/api/$',
        r2070_pgtopj_infoprocjud_api_views.r2070pgtoPJinfoProcJudList.as_view() ),

    url(r'^r2070-pgtopj-infoprocjud/api/(?P<pk>[0-9]+)/$',
        r2070_pgtopj_infoprocjud_api_views.r2070pgtoPJinfoProcJudDetail.as_view() ),

    url(r'^r2070-pgtopj-infoprocjud/$', 
        r2070_pgtopj_infoprocjud_listar_views.listar, 
        name='r2070_pgtopj_infoprocjud'),

    url(r'^r2070-pgtopj-infoprocjud/salvar/(?P<pk>[0-9]+)/$', 
        r2070_pgtopj_infoprocjud_salvar_views.salvar, 
        name='r2070_pgtopj_infoprocjud_salvar'),

    url(r'^r2070-pgtopj-infoprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_pgtopj_infoprocjud_salvar_views.salvar, 
        name='r2070_pgtopj_infoprocjud_salvar_tab'),
        
    url(r'^r2070-pgtopj-infoprocjud/cadastrar/$', 
        r2070_pgtopj_infoprocjud_salvar_views.salvar, 
        name='r2070_pgtopj_infoprocjud_cadastrar'),

    url(r'^r2070-pgtopj-infoprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_pgtopj_infoprocjud_salvar_views.salvar, 
        name='r2070_pgtopj_infoprocjud_salvar_output'),
        
    url(r'^r2070-pgtopj-infoprocjud/(?P<output>[\w-]+)/$', 
        r2070_pgtopj_infoprocjud_listar_views.listar, 
        name='r2070_pgtopj_infoprocjud_output'),

    url(r'^r2070-pgtopj-despprocjud/apagar/(?P<pk>[0-9]+)/$', 
        r2070_pgtopj_despprocjud_apagar_views.apagar, 
        name='r2070_pgtopj_despprocjud_apagar'),

    url(r'^r2070-pgtopj-despprocjud/api/$',
        r2070_pgtopj_despprocjud_api_views.r2070pgtoPJdespProcJudList.as_view() ),

    url(r'^r2070-pgtopj-despprocjud/api/(?P<pk>[0-9]+)/$',
        r2070_pgtopj_despprocjud_api_views.r2070pgtoPJdespProcJudDetail.as_view() ),

    url(r'^r2070-pgtopj-despprocjud/$', 
        r2070_pgtopj_despprocjud_listar_views.listar, 
        name='r2070_pgtopj_despprocjud'),

    url(r'^r2070-pgtopj-despprocjud/salvar/(?P<pk>[0-9]+)/$', 
        r2070_pgtopj_despprocjud_salvar_views.salvar, 
        name='r2070_pgtopj_despprocjud_salvar'),

    url(r'^r2070-pgtopj-despprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_pgtopj_despprocjud_salvar_views.salvar, 
        name='r2070_pgtopj_despprocjud_salvar_tab'),
        
    url(r'^r2070-pgtopj-despprocjud/cadastrar/$', 
        r2070_pgtopj_despprocjud_salvar_views.salvar, 
        name='r2070_pgtopj_despprocjud_cadastrar'),

    url(r'^r2070-pgtopj-despprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_pgtopj_despprocjud_salvar_views.salvar, 
        name='r2070_pgtopj_despprocjud_salvar_output'),
        
    url(r'^r2070-pgtopj-despprocjud/(?P<output>[\w-]+)/$', 
        r2070_pgtopj_despprocjud_listar_views.listar, 
        name='r2070_pgtopj_despprocjud_output'),

    url(r'^r2070-pgtopj-ideadvogado/apagar/(?P<pk>[0-9]+)/$', 
        r2070_pgtopj_ideadvogado_apagar_views.apagar, 
        name='r2070_pgtopj_ideadvogado_apagar'),

    url(r'^r2070-pgtopj-ideadvogado/api/$',
        r2070_pgtopj_ideadvogado_api_views.r2070pgtoPJideAdvogadoList.as_view() ),

    url(r'^r2070-pgtopj-ideadvogado/api/(?P<pk>[0-9]+)/$',
        r2070_pgtopj_ideadvogado_api_views.r2070pgtoPJideAdvogadoDetail.as_view() ),

    url(r'^r2070-pgtopj-ideadvogado/$', 
        r2070_pgtopj_ideadvogado_listar_views.listar, 
        name='r2070_pgtopj_ideadvogado'),

    url(r'^r2070-pgtopj-ideadvogado/salvar/(?P<pk>[0-9]+)/$', 
        r2070_pgtopj_ideadvogado_salvar_views.salvar, 
        name='r2070_pgtopj_ideadvogado_salvar'),

    url(r'^r2070-pgtopj-ideadvogado/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_pgtopj_ideadvogado_salvar_views.salvar, 
        name='r2070_pgtopj_ideadvogado_salvar_tab'),
        
    url(r'^r2070-pgtopj-ideadvogado/cadastrar/$', 
        r2070_pgtopj_ideadvogado_salvar_views.salvar, 
        name='r2070_pgtopj_ideadvogado_cadastrar'),

    url(r'^r2070-pgtopj-ideadvogado/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_pgtopj_ideadvogado_salvar_views.salvar, 
        name='r2070_pgtopj_ideadvogado_salvar_output'),
        
    url(r'^r2070-pgtopj-ideadvogado/(?P<output>[\w-]+)/$', 
        r2070_pgtopj_ideadvogado_listar_views.listar, 
        name='r2070_pgtopj_ideadvogado_output'),

    url(r'^r2070-pgtopj-origemrecursos/apagar/(?P<pk>[0-9]+)/$', 
        r2070_pgtopj_origemrecursos_apagar_views.apagar, 
        name='r2070_pgtopj_origemrecursos_apagar'),

    url(r'^r2070-pgtopj-origemrecursos/api/$',
        r2070_pgtopj_origemrecursos_api_views.r2070pgtoPJorigemRecursosList.as_view() ),

    url(r'^r2070-pgtopj-origemrecursos/api/(?P<pk>[0-9]+)/$',
        r2070_pgtopj_origemrecursos_api_views.r2070pgtoPJorigemRecursosDetail.as_view() ),

    url(r'^r2070-pgtopj-origemrecursos/$', 
        r2070_pgtopj_origemrecursos_listar_views.listar, 
        name='r2070_pgtopj_origemrecursos'),

    url(r'^r2070-pgtopj-origemrecursos/salvar/(?P<pk>[0-9]+)/$', 
        r2070_pgtopj_origemrecursos_salvar_views.salvar, 
        name='r2070_pgtopj_origemrecursos_salvar'),

    url(r'^r2070-pgtopj-origemrecursos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_pgtopj_origemrecursos_salvar_views.salvar, 
        name='r2070_pgtopj_origemrecursos_salvar_tab'),
        
    url(r'^r2070-pgtopj-origemrecursos/cadastrar/$', 
        r2070_pgtopj_origemrecursos_salvar_views.salvar, 
        name='r2070_pgtopj_origemrecursos_cadastrar'),

    url(r'^r2070-pgtopj-origemrecursos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_pgtopj_origemrecursos_salvar_views.salvar, 
        name='r2070_pgtopj_origemrecursos_salvar_output'),
        
    url(r'^r2070-pgtopj-origemrecursos/(?P<output>[\w-]+)/$', 
        r2070_pgtopj_origemrecursos_listar_views.listar, 
        name='r2070_pgtopj_origemrecursos_output'),

    url(r'^r2070-pgtoresidext/apagar/(?P<pk>[0-9]+)/$', 
        r2070_pgtoresidext_apagar_views.apagar, 
        name='r2070_pgtoresidext_apagar'),

    url(r'^r2070-pgtoresidext/api/$',
        r2070_pgtoresidext_api_views.r2070pgtoResidExtList.as_view() ),

    url(r'^r2070-pgtoresidext/api/(?P<pk>[0-9]+)/$',
        r2070_pgtoresidext_api_views.r2070pgtoResidExtDetail.as_view() ),

    url(r'^r2070-pgtoresidext/$', 
        r2070_pgtoresidext_listar_views.listar, 
        name='r2070_pgtoresidext'),

    url(r'^r2070-pgtoresidext/salvar/(?P<pk>[0-9]+)/$', 
        r2070_pgtoresidext_salvar_views.salvar, 
        name='r2070_pgtoresidext_salvar'),

    url(r'^r2070-pgtoresidext/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2070_pgtoresidext_salvar_views.salvar, 
        name='r2070_pgtoresidext_salvar_tab'),
        
    url(r'^r2070-pgtoresidext/cadastrar/$', 
        r2070_pgtoresidext_salvar_views.salvar, 
        name='r2070_pgtoresidext_cadastrar'),

    url(r'^r2070-pgtoresidext/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2070_pgtoresidext_salvar_views.salvar, 
        name='r2070_pgtoresidext_salvar_output'),
        
    url(r'^r2070-pgtoresidext/(?P<output>[\w-]+)/$', 
        r2070_pgtoresidext_listar_views.listar, 
        name='r2070_pgtoresidext_output'),


]