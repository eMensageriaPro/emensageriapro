#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.r4010.views import r4010_idepgto_apagar as r4010_idepgto_apagar_views
from emensageriapro.r4010.views import r4010_idepgto_listar as r4010_idepgto_listar_views
from emensageriapro.r4010.views import r4010_idepgto_salvar as r4010_idepgto_salvar_views
from emensageriapro.r4010.views import r4010_idepgto_api as r4010_idepgto_api_views
from emensageriapro.r4010.views import r4010_infopgto_apagar as r4010_infopgto_apagar_views
from emensageriapro.r4010.views import r4010_infopgto_listar as r4010_infopgto_listar_views
from emensageriapro.r4010.views import r4010_infopgto_salvar as r4010_infopgto_salvar_views
from emensageriapro.r4010.views import r4010_infopgto_api as r4010_infopgto_api_views
from emensageriapro.r4010.views import r4010_fci_apagar as r4010_fci_apagar_views
from emensageriapro.r4010.views import r4010_fci_listar as r4010_fci_listar_views
from emensageriapro.r4010.views import r4010_fci_salvar as r4010_fci_salvar_views
from emensageriapro.r4010.views import r4010_fci_api as r4010_fci_api_views
from emensageriapro.r4010.views import r4010_scp_apagar as r4010_scp_apagar_views
from emensageriapro.r4010.views import r4010_scp_listar as r4010_scp_listar_views
from emensageriapro.r4010.views import r4010_scp_salvar as r4010_scp_salvar_views
from emensageriapro.r4010.views import r4010_scp_api as r4010_scp_api_views
from emensageriapro.r4010.views import r4010_detded_apagar as r4010_detded_apagar_views
from emensageriapro.r4010.views import r4010_detded_listar as r4010_detded_listar_views
from emensageriapro.r4010.views import r4010_detded_salvar as r4010_detded_salvar_views
from emensageriapro.r4010.views import r4010_detded_api as r4010_detded_api_views
from emensageriapro.r4010.views import r4010_benefpen_apagar as r4010_benefpen_apagar_views
from emensageriapro.r4010.views import r4010_benefpen_listar as r4010_benefpen_listar_views
from emensageriapro.r4010.views import r4010_benefpen_salvar as r4010_benefpen_salvar_views
from emensageriapro.r4010.views import r4010_benefpen_api as r4010_benefpen_api_views
from emensageriapro.r4010.views import r4010_rendisento_apagar as r4010_rendisento_apagar_views
from emensageriapro.r4010.views import r4010_rendisento_listar as r4010_rendisento_listar_views
from emensageriapro.r4010.views import r4010_rendisento_salvar as r4010_rendisento_salvar_views
from emensageriapro.r4010.views import r4010_rendisento_api as r4010_rendisento_api_views
from emensageriapro.r4010.views import r4010_infoprocret_apagar as r4010_infoprocret_apagar_views
from emensageriapro.r4010.views import r4010_infoprocret_listar as r4010_infoprocret_listar_views
from emensageriapro.r4010.views import r4010_infoprocret_salvar as r4010_infoprocret_salvar_views
from emensageriapro.r4010.views import r4010_infoprocret_api as r4010_infoprocret_api_views
from emensageriapro.r4010.views import r4010_inforra_apagar as r4010_inforra_apagar_views
from emensageriapro.r4010.views import r4010_inforra_listar as r4010_inforra_listar_views
from emensageriapro.r4010.views import r4010_inforra_salvar as r4010_inforra_salvar_views
from emensageriapro.r4010.views import r4010_inforra_api as r4010_inforra_api_views
from emensageriapro.r4010.views import r4010_inforra_despprocjud_apagar as r4010_inforra_despprocjud_apagar_views
from emensageriapro.r4010.views import r4010_inforra_despprocjud_listar as r4010_inforra_despprocjud_listar_views
from emensageriapro.r4010.views import r4010_inforra_despprocjud_salvar as r4010_inforra_despprocjud_salvar_views
from emensageriapro.r4010.views import r4010_inforra_despprocjud_api as r4010_inforra_despprocjud_api_views
from emensageriapro.r4010.views import r4010_inforra_ideadv_apagar as r4010_inforra_ideadv_apagar_views
from emensageriapro.r4010.views import r4010_inforra_ideadv_listar as r4010_inforra_ideadv_listar_views
from emensageriapro.r4010.views import r4010_inforra_ideadv_salvar as r4010_inforra_ideadv_salvar_views
from emensageriapro.r4010.views import r4010_inforra_ideadv_api as r4010_inforra_ideadv_api_views
from emensageriapro.r4010.views import r4010_inforra_origemrec_apagar as r4010_inforra_origemrec_apagar_views
from emensageriapro.r4010.views import r4010_inforra_origemrec_listar as r4010_inforra_origemrec_listar_views
from emensageriapro.r4010.views import r4010_inforra_origemrec_salvar as r4010_inforra_origemrec_salvar_views
from emensageriapro.r4010.views import r4010_inforra_origemrec_api as r4010_inforra_origemrec_api_views
from emensageriapro.r4010.views import r4010_infoprocjud_apagar as r4010_infoprocjud_apagar_views
from emensageriapro.r4010.views import r4010_infoprocjud_listar as r4010_infoprocjud_listar_views
from emensageriapro.r4010.views import r4010_infoprocjud_salvar as r4010_infoprocjud_salvar_views
from emensageriapro.r4010.views import r4010_infoprocjud_api as r4010_infoprocjud_api_views
from emensageriapro.r4010.views import r4010_infoprocjud_despprocjud_apagar as r4010_infoprocjud_despprocjud_apagar_views
from emensageriapro.r4010.views import r4010_infoprocjud_despprocjud_listar as r4010_infoprocjud_despprocjud_listar_views
from emensageriapro.r4010.views import r4010_infoprocjud_despprocjud_salvar as r4010_infoprocjud_despprocjud_salvar_views
from emensageriapro.r4010.views import r4010_infoprocjud_despprocjud_api as r4010_infoprocjud_despprocjud_api_views
from emensageriapro.r4010.views import r4010_infoprocjud_ideadv_apagar as r4010_infoprocjud_ideadv_apagar_views
from emensageriapro.r4010.views import r4010_infoprocjud_ideadv_listar as r4010_infoprocjud_ideadv_listar_views
from emensageriapro.r4010.views import r4010_infoprocjud_ideadv_salvar as r4010_infoprocjud_ideadv_salvar_views
from emensageriapro.r4010.views import r4010_infoprocjud_ideadv_api as r4010_infoprocjud_ideadv_api_views
from emensageriapro.r4010.views import r4010_infoprocjud_origemrec_apagar as r4010_infoprocjud_origemrec_apagar_views
from emensageriapro.r4010.views import r4010_infoprocjud_origemrec_listar as r4010_infoprocjud_origemrec_listar_views
from emensageriapro.r4010.views import r4010_infoprocjud_origemrec_salvar as r4010_infoprocjud_origemrec_salvar_views
from emensageriapro.r4010.views import r4010_infoprocjud_origemrec_api as r4010_infoprocjud_origemrec_api_views
from emensageriapro.r4010.views import r4010_infopgtoext_apagar as r4010_infopgtoext_apagar_views
from emensageriapro.r4010.views import r4010_infopgtoext_listar as r4010_infopgtoext_listar_views
from emensageriapro.r4010.views import r4010_infopgtoext_salvar as r4010_infopgtoext_salvar_views
from emensageriapro.r4010.views import r4010_infopgtoext_api as r4010_infopgtoext_api_views
from emensageriapro.r4010.views import r4010_ideopsaude_apagar as r4010_ideopsaude_apagar_views
from emensageriapro.r4010.views import r4010_ideopsaude_listar as r4010_ideopsaude_listar_views
from emensageriapro.r4010.views import r4010_ideopsaude_salvar as r4010_ideopsaude_salvar_views
from emensageriapro.r4010.views import r4010_ideopsaude_api as r4010_ideopsaude_api_views
from emensageriapro.r4010.views import r4010_inforeemb_apagar as r4010_inforeemb_apagar_views
from emensageriapro.r4010.views import r4010_inforeemb_listar as r4010_inforeemb_listar_views
from emensageriapro.r4010.views import r4010_inforeemb_salvar as r4010_inforeemb_salvar_views
from emensageriapro.r4010.views import r4010_inforeemb_api as r4010_inforeemb_api_views
from emensageriapro.r4010.views import r4010_infodependpl_apagar as r4010_infodependpl_apagar_views
from emensageriapro.r4010.views import r4010_infodependpl_listar as r4010_infodependpl_listar_views
from emensageriapro.r4010.views import r4010_infodependpl_salvar as r4010_infodependpl_salvar_views
from emensageriapro.r4010.views import r4010_infodependpl_api as r4010_infodependpl_api_views
from emensageriapro.r4010.views import r4010_inforeembdep_apagar as r4010_inforeembdep_apagar_views
from emensageriapro.r4010.views import r4010_inforeembdep_listar as r4010_inforeembdep_listar_views
from emensageriapro.r4010.views import r4010_inforeembdep_salvar as r4010_inforeembdep_salvar_views
from emensageriapro.r4010.views import r4010_inforeembdep_api as r4010_inforeembdep_api_views



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


    url(r'^r4010-idepgto/apagar/(?P<pk>[0-9]+)/$',
        r4010_idepgto_apagar_views.apagar,
        name='r4010_idepgto_apagar'),

    url(r'^r4010-idepgto/api/$',
        r4010_idepgto_api_views.r4010idePgtoList.as_view() ),

    url(r'^r4010-idepgto/api/(?P<pk>[0-9]+)/$',
        r4010_idepgto_api_views.r4010idePgtoDetail.as_view() ),

    url(r'^r4010-idepgto/$',
        r4010_idepgto_listar_views.listar,
        name='r4010_idepgto'),

    url(r'^r4010-idepgto/salvar/(?P<pk>[0-9]+)/$',
        r4010_idepgto_salvar_views.salvar,
        name='r4010_idepgto_salvar'),

    url(r'^r4010-idepgto/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_idepgto_salvar_views.salvar,
        name='r4010_idepgto_salvar_tab'),

    url(r'^r4010-idepgto/cadastrar/$',
        r4010_idepgto_salvar_views.salvar,
        name='r4010_idepgto_cadastrar'),

    url(r'^r4010-idepgto/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_idepgto_salvar_views.salvar,
        name='r4010_idepgto_salvar_output'),

    url(r'^r4010-idepgto/(?P<output>[\w-]+)/$',
        r4010_idepgto_listar_views.listar,
        name='r4010_idepgto_output'),

    url(r'^r4010-infopgto/apagar/(?P<pk>[0-9]+)/$',
        r4010_infopgto_apagar_views.apagar,
        name='r4010_infopgto_apagar'),

    url(r'^r4010-infopgto/api/$',
        r4010_infopgto_api_views.r4010infoPgtoList.as_view() ),

    url(r'^r4010-infopgto/api/(?P<pk>[0-9]+)/$',
        r4010_infopgto_api_views.r4010infoPgtoDetail.as_view() ),

    url(r'^r4010-infopgto/$',
        r4010_infopgto_listar_views.listar,
        name='r4010_infopgto'),

    url(r'^r4010-infopgto/salvar/(?P<pk>[0-9]+)/$',
        r4010_infopgto_salvar_views.salvar,
        name='r4010_infopgto_salvar'),

    url(r'^r4010-infopgto/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_infopgto_salvar_views.salvar,
        name='r4010_infopgto_salvar_tab'),

    url(r'^r4010-infopgto/cadastrar/$',
        r4010_infopgto_salvar_views.salvar,
        name='r4010_infopgto_cadastrar'),

    url(r'^r4010-infopgto/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_infopgto_salvar_views.salvar,
        name='r4010_infopgto_salvar_output'),

    url(r'^r4010-infopgto/(?P<output>[\w-]+)/$',
        r4010_infopgto_listar_views.listar,
        name='r4010_infopgto_output'),

    url(r'^r4010-fci/apagar/(?P<pk>[0-9]+)/$',
        r4010_fci_apagar_views.apagar,
        name='r4010_fci_apagar'),

    url(r'^r4010-fci/api/$',
        r4010_fci_api_views.r4010FCIList.as_view() ),

    url(r'^r4010-fci/api/(?P<pk>[0-9]+)/$',
        r4010_fci_api_views.r4010FCIDetail.as_view() ),

    url(r'^r4010-fci/$',
        r4010_fci_listar_views.listar,
        name='r4010_fci'),

    url(r'^r4010-fci/salvar/(?P<pk>[0-9]+)/$',
        r4010_fci_salvar_views.salvar,
        name='r4010_fci_salvar'),

    url(r'^r4010-fci/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_fci_salvar_views.salvar,
        name='r4010_fci_salvar_tab'),

    url(r'^r4010-fci/cadastrar/$',
        r4010_fci_salvar_views.salvar,
        name='r4010_fci_cadastrar'),

    url(r'^r4010-fci/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_fci_salvar_views.salvar,
        name='r4010_fci_salvar_output'),

    url(r'^r4010-fci/(?P<output>[\w-]+)/$',
        r4010_fci_listar_views.listar,
        name='r4010_fci_output'),

    url(r'^r4010-scp/apagar/(?P<pk>[0-9]+)/$',
        r4010_scp_apagar_views.apagar,
        name='r4010_scp_apagar'),

    url(r'^r4010-scp/api/$',
        r4010_scp_api_views.r4010SCPList.as_view() ),

    url(r'^r4010-scp/api/(?P<pk>[0-9]+)/$',
        r4010_scp_api_views.r4010SCPDetail.as_view() ),

    url(r'^r4010-scp/$',
        r4010_scp_listar_views.listar,
        name='r4010_scp'),

    url(r'^r4010-scp/salvar/(?P<pk>[0-9]+)/$',
        r4010_scp_salvar_views.salvar,
        name='r4010_scp_salvar'),

    url(r'^r4010-scp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_scp_salvar_views.salvar,
        name='r4010_scp_salvar_tab'),

    url(r'^r4010-scp/cadastrar/$',
        r4010_scp_salvar_views.salvar,
        name='r4010_scp_cadastrar'),

    url(r'^r4010-scp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_scp_salvar_views.salvar,
        name='r4010_scp_salvar_output'),

    url(r'^r4010-scp/(?P<output>[\w-]+)/$',
        r4010_scp_listar_views.listar,
        name='r4010_scp_output'),

    url(r'^r4010-detded/apagar/(?P<pk>[0-9]+)/$',
        r4010_detded_apagar_views.apagar,
        name='r4010_detded_apagar'),

    url(r'^r4010-detded/api/$',
        r4010_detded_api_views.r4010detDedList.as_view() ),

    url(r'^r4010-detded/api/(?P<pk>[0-9]+)/$',
        r4010_detded_api_views.r4010detDedDetail.as_view() ),

    url(r'^r4010-detded/$',
        r4010_detded_listar_views.listar,
        name='r4010_detded'),

    url(r'^r4010-detded/salvar/(?P<pk>[0-9]+)/$',
        r4010_detded_salvar_views.salvar,
        name='r4010_detded_salvar'),

    url(r'^r4010-detded/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_detded_salvar_views.salvar,
        name='r4010_detded_salvar_tab'),

    url(r'^r4010-detded/cadastrar/$',
        r4010_detded_salvar_views.salvar,
        name='r4010_detded_cadastrar'),

    url(r'^r4010-detded/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_detded_salvar_views.salvar,
        name='r4010_detded_salvar_output'),

    url(r'^r4010-detded/(?P<output>[\w-]+)/$',
        r4010_detded_listar_views.listar,
        name='r4010_detded_output'),

    url(r'^r4010-benefpen/apagar/(?P<pk>[0-9]+)/$',
        r4010_benefpen_apagar_views.apagar,
        name='r4010_benefpen_apagar'),

    url(r'^r4010-benefpen/api/$',
        r4010_benefpen_api_views.r4010benefPenList.as_view() ),

    url(r'^r4010-benefpen/api/(?P<pk>[0-9]+)/$',
        r4010_benefpen_api_views.r4010benefPenDetail.as_view() ),

    url(r'^r4010-benefpen/$',
        r4010_benefpen_listar_views.listar,
        name='r4010_benefpen'),

    url(r'^r4010-benefpen/salvar/(?P<pk>[0-9]+)/$',
        r4010_benefpen_salvar_views.salvar,
        name='r4010_benefpen_salvar'),

    url(r'^r4010-benefpen/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_benefpen_salvar_views.salvar,
        name='r4010_benefpen_salvar_tab'),

    url(r'^r4010-benefpen/cadastrar/$',
        r4010_benefpen_salvar_views.salvar,
        name='r4010_benefpen_cadastrar'),

    url(r'^r4010-benefpen/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_benefpen_salvar_views.salvar,
        name='r4010_benefpen_salvar_output'),

    url(r'^r4010-benefpen/(?P<output>[\w-]+)/$',
        r4010_benefpen_listar_views.listar,
        name='r4010_benefpen_output'),

    url(r'^r4010-rendisento/apagar/(?P<pk>[0-9]+)/$',
        r4010_rendisento_apagar_views.apagar,
        name='r4010_rendisento_apagar'),

    url(r'^r4010-rendisento/api/$',
        r4010_rendisento_api_views.r4010rendIsentoList.as_view() ),

    url(r'^r4010-rendisento/api/(?P<pk>[0-9]+)/$',
        r4010_rendisento_api_views.r4010rendIsentoDetail.as_view() ),

    url(r'^r4010-rendisento/$',
        r4010_rendisento_listar_views.listar,
        name='r4010_rendisento'),

    url(r'^r4010-rendisento/salvar/(?P<pk>[0-9]+)/$',
        r4010_rendisento_salvar_views.salvar,
        name='r4010_rendisento_salvar'),

    url(r'^r4010-rendisento/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_rendisento_salvar_views.salvar,
        name='r4010_rendisento_salvar_tab'),

    url(r'^r4010-rendisento/cadastrar/$',
        r4010_rendisento_salvar_views.salvar,
        name='r4010_rendisento_cadastrar'),

    url(r'^r4010-rendisento/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_rendisento_salvar_views.salvar,
        name='r4010_rendisento_salvar_output'),

    url(r'^r4010-rendisento/(?P<output>[\w-]+)/$',
        r4010_rendisento_listar_views.listar,
        name='r4010_rendisento_output'),

    url(r'^r4010-infoprocret/apagar/(?P<pk>[0-9]+)/$',
        r4010_infoprocret_apagar_views.apagar,
        name='r4010_infoprocret_apagar'),

    url(r'^r4010-infoprocret/api/$',
        r4010_infoprocret_api_views.r4010infoProcRetList.as_view() ),

    url(r'^r4010-infoprocret/api/(?P<pk>[0-9]+)/$',
        r4010_infoprocret_api_views.r4010infoProcRetDetail.as_view() ),

    url(r'^r4010-infoprocret/$',
        r4010_infoprocret_listar_views.listar,
        name='r4010_infoprocret'),

    url(r'^r4010-infoprocret/salvar/(?P<pk>[0-9]+)/$',
        r4010_infoprocret_salvar_views.salvar,
        name='r4010_infoprocret_salvar'),

    url(r'^r4010-infoprocret/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_infoprocret_salvar_views.salvar,
        name='r4010_infoprocret_salvar_tab'),

    url(r'^r4010-infoprocret/cadastrar/$',
        r4010_infoprocret_salvar_views.salvar,
        name='r4010_infoprocret_cadastrar'),

    url(r'^r4010-infoprocret/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_infoprocret_salvar_views.salvar,
        name='r4010_infoprocret_salvar_output'),

    url(r'^r4010-infoprocret/(?P<output>[\w-]+)/$',
        r4010_infoprocret_listar_views.listar,
        name='r4010_infoprocret_output'),

    url(r'^r4010-inforra/apagar/(?P<pk>[0-9]+)/$',
        r4010_inforra_apagar_views.apagar,
        name='r4010_inforra_apagar'),

    url(r'^r4010-inforra/api/$',
        r4010_inforra_api_views.r4010infoRRAList.as_view() ),

    url(r'^r4010-inforra/api/(?P<pk>[0-9]+)/$',
        r4010_inforra_api_views.r4010infoRRADetail.as_view() ),

    url(r'^r4010-inforra/$',
        r4010_inforra_listar_views.listar,
        name='r4010_inforra'),

    url(r'^r4010-inforra/salvar/(?P<pk>[0-9]+)/$',
        r4010_inforra_salvar_views.salvar,
        name='r4010_inforra_salvar'),

    url(r'^r4010-inforra/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_inforra_salvar_views.salvar,
        name='r4010_inforra_salvar_tab'),

    url(r'^r4010-inforra/cadastrar/$',
        r4010_inforra_salvar_views.salvar,
        name='r4010_inforra_cadastrar'),

    url(r'^r4010-inforra/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_inforra_salvar_views.salvar,
        name='r4010_inforra_salvar_output'),

    url(r'^r4010-inforra/(?P<output>[\w-]+)/$',
        r4010_inforra_listar_views.listar,
        name='r4010_inforra_output'),

    url(r'^r4010-inforra-despprocjud/apagar/(?P<pk>[0-9]+)/$',
        r4010_inforra_despprocjud_apagar_views.apagar,
        name='r4010_inforra_despprocjud_apagar'),

    url(r'^r4010-inforra-despprocjud/api/$',
        r4010_inforra_despprocjud_api_views.r4010infoRRAdespProcJudList.as_view() ),

    url(r'^r4010-inforra-despprocjud/api/(?P<pk>[0-9]+)/$',
        r4010_inforra_despprocjud_api_views.r4010infoRRAdespProcJudDetail.as_view() ),

    url(r'^r4010-inforra-despprocjud/$',
        r4010_inforra_despprocjud_listar_views.listar,
        name='r4010_inforra_despprocjud'),

    url(r'^r4010-inforra-despprocjud/salvar/(?P<pk>[0-9]+)/$',
        r4010_inforra_despprocjud_salvar_views.salvar,
        name='r4010_inforra_despprocjud_salvar'),

    url(r'^r4010-inforra-despprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_inforra_despprocjud_salvar_views.salvar,
        name='r4010_inforra_despprocjud_salvar_tab'),

    url(r'^r4010-inforra-despprocjud/cadastrar/$',
        r4010_inforra_despprocjud_salvar_views.salvar,
        name='r4010_inforra_despprocjud_cadastrar'),

    url(r'^r4010-inforra-despprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_inforra_despprocjud_salvar_views.salvar,
        name='r4010_inforra_despprocjud_salvar_output'),

    url(r'^r4010-inforra-despprocjud/(?P<output>[\w-]+)/$',
        r4010_inforra_despprocjud_listar_views.listar,
        name='r4010_inforra_despprocjud_output'),

    url(r'^r4010-inforra-ideadv/apagar/(?P<pk>[0-9]+)/$',
        r4010_inforra_ideadv_apagar_views.apagar,
        name='r4010_inforra_ideadv_apagar'),

    url(r'^r4010-inforra-ideadv/api/$',
        r4010_inforra_ideadv_api_views.r4010infoRRAideAdvList.as_view() ),

    url(r'^r4010-inforra-ideadv/api/(?P<pk>[0-9]+)/$',
        r4010_inforra_ideadv_api_views.r4010infoRRAideAdvDetail.as_view() ),

    url(r'^r4010-inforra-ideadv/$',
        r4010_inforra_ideadv_listar_views.listar,
        name='r4010_inforra_ideadv'),

    url(r'^r4010-inforra-ideadv/salvar/(?P<pk>[0-9]+)/$',
        r4010_inforra_ideadv_salvar_views.salvar,
        name='r4010_inforra_ideadv_salvar'),

    url(r'^r4010-inforra-ideadv/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_inforra_ideadv_salvar_views.salvar,
        name='r4010_inforra_ideadv_salvar_tab'),

    url(r'^r4010-inforra-ideadv/cadastrar/$',
        r4010_inforra_ideadv_salvar_views.salvar,
        name='r4010_inforra_ideadv_cadastrar'),

    url(r'^r4010-inforra-ideadv/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_inforra_ideadv_salvar_views.salvar,
        name='r4010_inforra_ideadv_salvar_output'),

    url(r'^r4010-inforra-ideadv/(?P<output>[\w-]+)/$',
        r4010_inforra_ideadv_listar_views.listar,
        name='r4010_inforra_ideadv_output'),

    url(r'^r4010-inforra-origemrec/apagar/(?P<pk>[0-9]+)/$',
        r4010_inforra_origemrec_apagar_views.apagar,
        name='r4010_inforra_origemrec_apagar'),

    url(r'^r4010-inforra-origemrec/api/$',
        r4010_inforra_origemrec_api_views.r4010infoRRAorigemRecList.as_view() ),

    url(r'^r4010-inforra-origemrec/api/(?P<pk>[0-9]+)/$',
        r4010_inforra_origemrec_api_views.r4010infoRRAorigemRecDetail.as_view() ),

    url(r'^r4010-inforra-origemrec/$',
        r4010_inforra_origemrec_listar_views.listar,
        name='r4010_inforra_origemrec'),

    url(r'^r4010-inforra-origemrec/salvar/(?P<pk>[0-9]+)/$',
        r4010_inforra_origemrec_salvar_views.salvar,
        name='r4010_inforra_origemrec_salvar'),

    url(r'^r4010-inforra-origemrec/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_inforra_origemrec_salvar_views.salvar,
        name='r4010_inforra_origemrec_salvar_tab'),

    url(r'^r4010-inforra-origemrec/cadastrar/$',
        r4010_inforra_origemrec_salvar_views.salvar,
        name='r4010_inforra_origemrec_cadastrar'),

    url(r'^r4010-inforra-origemrec/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_inforra_origemrec_salvar_views.salvar,
        name='r4010_inforra_origemrec_salvar_output'),

    url(r'^r4010-inforra-origemrec/(?P<output>[\w-]+)/$',
        r4010_inforra_origemrec_listar_views.listar,
        name='r4010_inforra_origemrec_output'),

    url(r'^r4010-infoprocjud/apagar/(?P<pk>[0-9]+)/$',
        r4010_infoprocjud_apagar_views.apagar,
        name='r4010_infoprocjud_apagar'),

    url(r'^r4010-infoprocjud/api/$',
        r4010_infoprocjud_api_views.r4010infoProcJudList.as_view() ),

    url(r'^r4010-infoprocjud/api/(?P<pk>[0-9]+)/$',
        r4010_infoprocjud_api_views.r4010infoProcJudDetail.as_view() ),

    url(r'^r4010-infoprocjud/$',
        r4010_infoprocjud_listar_views.listar,
        name='r4010_infoprocjud'),

    url(r'^r4010-infoprocjud/salvar/(?P<pk>[0-9]+)/$',
        r4010_infoprocjud_salvar_views.salvar,
        name='r4010_infoprocjud_salvar'),

    url(r'^r4010-infoprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_infoprocjud_salvar_views.salvar,
        name='r4010_infoprocjud_salvar_tab'),

    url(r'^r4010-infoprocjud/cadastrar/$',
        r4010_infoprocjud_salvar_views.salvar,
        name='r4010_infoprocjud_cadastrar'),

    url(r'^r4010-infoprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_infoprocjud_salvar_views.salvar,
        name='r4010_infoprocjud_salvar_output'),

    url(r'^r4010-infoprocjud/(?P<output>[\w-]+)/$',
        r4010_infoprocjud_listar_views.listar,
        name='r4010_infoprocjud_output'),

    url(r'^r4010-infoprocjud-despprocjud/apagar/(?P<pk>[0-9]+)/$',
        r4010_infoprocjud_despprocjud_apagar_views.apagar,
        name='r4010_infoprocjud_despprocjud_apagar'),

    url(r'^r4010-infoprocjud-despprocjud/api/$',
        r4010_infoprocjud_despprocjud_api_views.r4010infoProcJuddespProcJudList.as_view() ),

    url(r'^r4010-infoprocjud-despprocjud/api/(?P<pk>[0-9]+)/$',
        r4010_infoprocjud_despprocjud_api_views.r4010infoProcJuddespProcJudDetail.as_view() ),

    url(r'^r4010-infoprocjud-despprocjud/$',
        r4010_infoprocjud_despprocjud_listar_views.listar,
        name='r4010_infoprocjud_despprocjud'),

    url(r'^r4010-infoprocjud-despprocjud/salvar/(?P<pk>[0-9]+)/$',
        r4010_infoprocjud_despprocjud_salvar_views.salvar,
        name='r4010_infoprocjud_despprocjud_salvar'),

    url(r'^r4010-infoprocjud-despprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_infoprocjud_despprocjud_salvar_views.salvar,
        name='r4010_infoprocjud_despprocjud_salvar_tab'),

    url(r'^r4010-infoprocjud-despprocjud/cadastrar/$',
        r4010_infoprocjud_despprocjud_salvar_views.salvar,
        name='r4010_infoprocjud_despprocjud_cadastrar'),

    url(r'^r4010-infoprocjud-despprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_infoprocjud_despprocjud_salvar_views.salvar,
        name='r4010_infoprocjud_despprocjud_salvar_output'),

    url(r'^r4010-infoprocjud-despprocjud/(?P<output>[\w-]+)/$',
        r4010_infoprocjud_despprocjud_listar_views.listar,
        name='r4010_infoprocjud_despprocjud_output'),

    url(r'^r4010-infoprocjud-ideadv/apagar/(?P<pk>[0-9]+)/$',
        r4010_infoprocjud_ideadv_apagar_views.apagar,
        name='r4010_infoprocjud_ideadv_apagar'),

    url(r'^r4010-infoprocjud-ideadv/api/$',
        r4010_infoprocjud_ideadv_api_views.r4010infoProcJudideAdvList.as_view() ),

    url(r'^r4010-infoprocjud-ideadv/api/(?P<pk>[0-9]+)/$',
        r4010_infoprocjud_ideadv_api_views.r4010infoProcJudideAdvDetail.as_view() ),

    url(r'^r4010-infoprocjud-ideadv/$',
        r4010_infoprocjud_ideadv_listar_views.listar,
        name='r4010_infoprocjud_ideadv'),

    url(r'^r4010-infoprocjud-ideadv/salvar/(?P<pk>[0-9]+)/$',
        r4010_infoprocjud_ideadv_salvar_views.salvar,
        name='r4010_infoprocjud_ideadv_salvar'),

    url(r'^r4010-infoprocjud-ideadv/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_infoprocjud_ideadv_salvar_views.salvar,
        name='r4010_infoprocjud_ideadv_salvar_tab'),

    url(r'^r4010-infoprocjud-ideadv/cadastrar/$',
        r4010_infoprocjud_ideadv_salvar_views.salvar,
        name='r4010_infoprocjud_ideadv_cadastrar'),

    url(r'^r4010-infoprocjud-ideadv/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_infoprocjud_ideadv_salvar_views.salvar,
        name='r4010_infoprocjud_ideadv_salvar_output'),

    url(r'^r4010-infoprocjud-ideadv/(?P<output>[\w-]+)/$',
        r4010_infoprocjud_ideadv_listar_views.listar,
        name='r4010_infoprocjud_ideadv_output'),

    url(r'^r4010-infoprocjud-origemrec/apagar/(?P<pk>[0-9]+)/$',
        r4010_infoprocjud_origemrec_apagar_views.apagar,
        name='r4010_infoprocjud_origemrec_apagar'),

    url(r'^r4010-infoprocjud-origemrec/api/$',
        r4010_infoprocjud_origemrec_api_views.r4010infoProcJudorigemRecList.as_view() ),

    url(r'^r4010-infoprocjud-origemrec/api/(?P<pk>[0-9]+)/$',
        r4010_infoprocjud_origemrec_api_views.r4010infoProcJudorigemRecDetail.as_view() ),

    url(r'^r4010-infoprocjud-origemrec/$',
        r4010_infoprocjud_origemrec_listar_views.listar,
        name='r4010_infoprocjud_origemrec'),

    url(r'^r4010-infoprocjud-origemrec/salvar/(?P<pk>[0-9]+)/$',
        r4010_infoprocjud_origemrec_salvar_views.salvar,
        name='r4010_infoprocjud_origemrec_salvar'),

    url(r'^r4010-infoprocjud-origemrec/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_infoprocjud_origemrec_salvar_views.salvar,
        name='r4010_infoprocjud_origemrec_salvar_tab'),

    url(r'^r4010-infoprocjud-origemrec/cadastrar/$',
        r4010_infoprocjud_origemrec_salvar_views.salvar,
        name='r4010_infoprocjud_origemrec_cadastrar'),

    url(r'^r4010-infoprocjud-origemrec/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_infoprocjud_origemrec_salvar_views.salvar,
        name='r4010_infoprocjud_origemrec_salvar_output'),

    url(r'^r4010-infoprocjud-origemrec/(?P<output>[\w-]+)/$',
        r4010_infoprocjud_origemrec_listar_views.listar,
        name='r4010_infoprocjud_origemrec_output'),

    url(r'^r4010-infopgtoext/apagar/(?P<pk>[0-9]+)/$',
        r4010_infopgtoext_apagar_views.apagar,
        name='r4010_infopgtoext_apagar'),

    url(r'^r4010-infopgtoext/api/$',
        r4010_infopgtoext_api_views.r4010infoPgtoExtList.as_view() ),

    url(r'^r4010-infopgtoext/api/(?P<pk>[0-9]+)/$',
        r4010_infopgtoext_api_views.r4010infoPgtoExtDetail.as_view() ),

    url(r'^r4010-infopgtoext/$',
        r4010_infopgtoext_listar_views.listar,
        name='r4010_infopgtoext'),

    url(r'^r4010-infopgtoext/salvar/(?P<pk>[0-9]+)/$',
        r4010_infopgtoext_salvar_views.salvar,
        name='r4010_infopgtoext_salvar'),

    url(r'^r4010-infopgtoext/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_infopgtoext_salvar_views.salvar,
        name='r4010_infopgtoext_salvar_tab'),

    url(r'^r4010-infopgtoext/cadastrar/$',
        r4010_infopgtoext_salvar_views.salvar,
        name='r4010_infopgtoext_cadastrar'),

    url(r'^r4010-infopgtoext/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_infopgtoext_salvar_views.salvar,
        name='r4010_infopgtoext_salvar_output'),

    url(r'^r4010-infopgtoext/(?P<output>[\w-]+)/$',
        r4010_infopgtoext_listar_views.listar,
        name='r4010_infopgtoext_output'),

    url(r'^r4010-ideopsaude/apagar/(?P<pk>[0-9]+)/$',
        r4010_ideopsaude_apagar_views.apagar,
        name='r4010_ideopsaude_apagar'),

    url(r'^r4010-ideopsaude/api/$',
        r4010_ideopsaude_api_views.r4010ideOpSaudeList.as_view() ),

    url(r'^r4010-ideopsaude/api/(?P<pk>[0-9]+)/$',
        r4010_ideopsaude_api_views.r4010ideOpSaudeDetail.as_view() ),

    url(r'^r4010-ideopsaude/$',
        r4010_ideopsaude_listar_views.listar,
        name='r4010_ideopsaude'),

    url(r'^r4010-ideopsaude/salvar/(?P<pk>[0-9]+)/$',
        r4010_ideopsaude_salvar_views.salvar,
        name='r4010_ideopsaude_salvar'),

    url(r'^r4010-ideopsaude/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_ideopsaude_salvar_views.salvar,
        name='r4010_ideopsaude_salvar_tab'),

    url(r'^r4010-ideopsaude/cadastrar/$',
        r4010_ideopsaude_salvar_views.salvar,
        name='r4010_ideopsaude_cadastrar'),

    url(r'^r4010-ideopsaude/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_ideopsaude_salvar_views.salvar,
        name='r4010_ideopsaude_salvar_output'),

    url(r'^r4010-ideopsaude/(?P<output>[\w-]+)/$',
        r4010_ideopsaude_listar_views.listar,
        name='r4010_ideopsaude_output'),

    url(r'^r4010-inforeemb/apagar/(?P<pk>[0-9]+)/$',
        r4010_inforeemb_apagar_views.apagar,
        name='r4010_inforeemb_apagar'),

    url(r'^r4010-inforeemb/api/$',
        r4010_inforeemb_api_views.r4010infoReembList.as_view() ),

    url(r'^r4010-inforeemb/api/(?P<pk>[0-9]+)/$',
        r4010_inforeemb_api_views.r4010infoReembDetail.as_view() ),

    url(r'^r4010-inforeemb/$',
        r4010_inforeemb_listar_views.listar,
        name='r4010_inforeemb'),

    url(r'^r4010-inforeemb/salvar/(?P<pk>[0-9]+)/$',
        r4010_inforeemb_salvar_views.salvar,
        name='r4010_inforeemb_salvar'),

    url(r'^r4010-inforeemb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_inforeemb_salvar_views.salvar,
        name='r4010_inforeemb_salvar_tab'),

    url(r'^r4010-inforeemb/cadastrar/$',
        r4010_inforeemb_salvar_views.salvar,
        name='r4010_inforeemb_cadastrar'),

    url(r'^r4010-inforeemb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_inforeemb_salvar_views.salvar,
        name='r4010_inforeemb_salvar_output'),

    url(r'^r4010-inforeemb/(?P<output>[\w-]+)/$',
        r4010_inforeemb_listar_views.listar,
        name='r4010_inforeemb_output'),

    url(r'^r4010-infodependpl/apagar/(?P<pk>[0-9]+)/$',
        r4010_infodependpl_apagar_views.apagar,
        name='r4010_infodependpl_apagar'),

    url(r'^r4010-infodependpl/api/$',
        r4010_infodependpl_api_views.r4010infoDependPlList.as_view() ),

    url(r'^r4010-infodependpl/api/(?P<pk>[0-9]+)/$',
        r4010_infodependpl_api_views.r4010infoDependPlDetail.as_view() ),

    url(r'^r4010-infodependpl/$',
        r4010_infodependpl_listar_views.listar,
        name='r4010_infodependpl'),

    url(r'^r4010-infodependpl/salvar/(?P<pk>[0-9]+)/$',
        r4010_infodependpl_salvar_views.salvar,
        name='r4010_infodependpl_salvar'),

    url(r'^r4010-infodependpl/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_infodependpl_salvar_views.salvar,
        name='r4010_infodependpl_salvar_tab'),

    url(r'^r4010-infodependpl/cadastrar/$',
        r4010_infodependpl_salvar_views.salvar,
        name='r4010_infodependpl_cadastrar'),

    url(r'^r4010-infodependpl/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_infodependpl_salvar_views.salvar,
        name='r4010_infodependpl_salvar_output'),

    url(r'^r4010-infodependpl/(?P<output>[\w-]+)/$',
        r4010_infodependpl_listar_views.listar,
        name='r4010_infodependpl_output'),

    url(r'^r4010-inforeembdep/apagar/(?P<pk>[0-9]+)/$',
        r4010_inforeembdep_apagar_views.apagar,
        name='r4010_inforeembdep_apagar'),

    url(r'^r4010-inforeembdep/api/$',
        r4010_inforeembdep_api_views.r4010infoReembDepList.as_view() ),

    url(r'^r4010-inforeembdep/api/(?P<pk>[0-9]+)/$',
        r4010_inforeembdep_api_views.r4010infoReembDepDetail.as_view() ),

    url(r'^r4010-inforeembdep/$',
        r4010_inforeembdep_listar_views.listar,
        name='r4010_inforeembdep'),

    url(r'^r4010-inforeembdep/salvar/(?P<pk>[0-9]+)/$',
        r4010_inforeembdep_salvar_views.salvar,
        name='r4010_inforeembdep_salvar'),

    url(r'^r4010-inforeembdep/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_inforeembdep_salvar_views.salvar,
        name='r4010_inforeembdep_salvar_tab'),

    url(r'^r4010-inforeembdep/cadastrar/$',
        r4010_inforeembdep_salvar_views.salvar,
        name='r4010_inforeembdep_cadastrar'),

    url(r'^r4010-inforeembdep/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_inforeembdep_salvar_views.salvar,
        name='r4010_inforeembdep_salvar_output'),

    url(r'^r4010-inforeembdep/(?P<output>[\w-]+)/$',
        r4010_inforeembdep_listar_views.listar,
        name='r4010_inforeembdep_output'),


]