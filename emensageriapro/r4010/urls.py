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


    url(r'^r4010-idepgto/apagar/(?P<hash>.*)/$', 
        r4010_idepgto_apagar_views.apagar, 
        name='r4010_idepgto_apagar'),

    url(r'^r4010-idepgto/api/$',
        r4010_idepgto_api_views.r4010idePgtoList.as_view() ),

    url(r'^r4010-idepgto/api/(?P<pk>[0-9]+)/$',
        r4010_idepgto_api_views.r4010idePgtoDetail.as_view() ),

    url(r'^r4010-idepgto/listar/(?P<hash>.*)/$', 
        r4010_idepgto_listar_views.listar, 
        name='r4010_idepgto'),

    url(r'^r4010-idepgto/salvar/(?P<hash>.*)/$', 
        r4010_idepgto_salvar_views.salvar, 
        name='r4010_idepgto_salvar'),

    url(r'^r4010-infopgto/apagar/(?P<hash>.*)/$', 
        r4010_infopgto_apagar_views.apagar, 
        name='r4010_infopgto_apagar'),

    url(r'^r4010-infopgto/api/$',
        r4010_infopgto_api_views.r4010infoPgtoList.as_view() ),

    url(r'^r4010-infopgto/api/(?P<pk>[0-9]+)/$',
        r4010_infopgto_api_views.r4010infoPgtoDetail.as_view() ),

    url(r'^r4010-infopgto/listar/(?P<hash>.*)/$', 
        r4010_infopgto_listar_views.listar, 
        name='r4010_infopgto'),

    url(r'^r4010-infopgto/salvar/(?P<hash>.*)/$', 
        r4010_infopgto_salvar_views.salvar, 
        name='r4010_infopgto_salvar'),

    url(r'^r4010-fci/apagar/(?P<hash>.*)/$', 
        r4010_fci_apagar_views.apagar, 
        name='r4010_fci_apagar'),

    url(r'^r4010-fci/api/$',
        r4010_fci_api_views.r4010FCIList.as_view() ),

    url(r'^r4010-fci/api/(?P<pk>[0-9]+)/$',
        r4010_fci_api_views.r4010FCIDetail.as_view() ),

    url(r'^r4010-fci/listar/(?P<hash>.*)/$', 
        r4010_fci_listar_views.listar, 
        name='r4010_fci'),

    url(r'^r4010-fci/salvar/(?P<hash>.*)/$', 
        r4010_fci_salvar_views.salvar, 
        name='r4010_fci_salvar'),

    url(r'^r4010-scp/apagar/(?P<hash>.*)/$', 
        r4010_scp_apagar_views.apagar, 
        name='r4010_scp_apagar'),

    url(r'^r4010-scp/api/$',
        r4010_scp_api_views.r4010SCPList.as_view() ),

    url(r'^r4010-scp/api/(?P<pk>[0-9]+)/$',
        r4010_scp_api_views.r4010SCPDetail.as_view() ),

    url(r'^r4010-scp/listar/(?P<hash>.*)/$', 
        r4010_scp_listar_views.listar, 
        name='r4010_scp'),

    url(r'^r4010-scp/salvar/(?P<hash>.*)/$', 
        r4010_scp_salvar_views.salvar, 
        name='r4010_scp_salvar'),

    url(r'^r4010-detded/apagar/(?P<hash>.*)/$', 
        r4010_detded_apagar_views.apagar, 
        name='r4010_detded_apagar'),

    url(r'^r4010-detded/api/$',
        r4010_detded_api_views.r4010detDedList.as_view() ),

    url(r'^r4010-detded/api/(?P<pk>[0-9]+)/$',
        r4010_detded_api_views.r4010detDedDetail.as_view() ),

    url(r'^r4010-detded/listar/(?P<hash>.*)/$', 
        r4010_detded_listar_views.listar, 
        name='r4010_detded'),

    url(r'^r4010-detded/salvar/(?P<hash>.*)/$', 
        r4010_detded_salvar_views.salvar, 
        name='r4010_detded_salvar'),

    url(r'^r4010-benefpen/apagar/(?P<hash>.*)/$', 
        r4010_benefpen_apagar_views.apagar, 
        name='r4010_benefpen_apagar'),

    url(r'^r4010-benefpen/api/$',
        r4010_benefpen_api_views.r4010benefPenList.as_view() ),

    url(r'^r4010-benefpen/api/(?P<pk>[0-9]+)/$',
        r4010_benefpen_api_views.r4010benefPenDetail.as_view() ),

    url(r'^r4010-benefpen/listar/(?P<hash>.*)/$', 
        r4010_benefpen_listar_views.listar, 
        name='r4010_benefpen'),

    url(r'^r4010-benefpen/salvar/(?P<hash>.*)/$', 
        r4010_benefpen_salvar_views.salvar, 
        name='r4010_benefpen_salvar'),

    url(r'^r4010-rendisento/apagar/(?P<hash>.*)/$', 
        r4010_rendisento_apagar_views.apagar, 
        name='r4010_rendisento_apagar'),

    url(r'^r4010-rendisento/api/$',
        r4010_rendisento_api_views.r4010rendIsentoList.as_view() ),

    url(r'^r4010-rendisento/api/(?P<pk>[0-9]+)/$',
        r4010_rendisento_api_views.r4010rendIsentoDetail.as_view() ),

    url(r'^r4010-rendisento/listar/(?P<hash>.*)/$', 
        r4010_rendisento_listar_views.listar, 
        name='r4010_rendisento'),

    url(r'^r4010-rendisento/salvar/(?P<hash>.*)/$', 
        r4010_rendisento_salvar_views.salvar, 
        name='r4010_rendisento_salvar'),

    url(r'^r4010-infoprocret/apagar/(?P<hash>.*)/$', 
        r4010_infoprocret_apagar_views.apagar, 
        name='r4010_infoprocret_apagar'),

    url(r'^r4010-infoprocret/api/$',
        r4010_infoprocret_api_views.r4010infoProcRetList.as_view() ),

    url(r'^r4010-infoprocret/api/(?P<pk>[0-9]+)/$',
        r4010_infoprocret_api_views.r4010infoProcRetDetail.as_view() ),

    url(r'^r4010-infoprocret/listar/(?P<hash>.*)/$', 
        r4010_infoprocret_listar_views.listar, 
        name='r4010_infoprocret'),

    url(r'^r4010-infoprocret/salvar/(?P<hash>.*)/$', 
        r4010_infoprocret_salvar_views.salvar, 
        name='r4010_infoprocret_salvar'),

    url(r'^r4010-inforra/apagar/(?P<hash>.*)/$', 
        r4010_inforra_apagar_views.apagar, 
        name='r4010_inforra_apagar'),

    url(r'^r4010-inforra/api/$',
        r4010_inforra_api_views.r4010infoRRAList.as_view() ),

    url(r'^r4010-inforra/api/(?P<pk>[0-9]+)/$',
        r4010_inforra_api_views.r4010infoRRADetail.as_view() ),

    url(r'^r4010-inforra/listar/(?P<hash>.*)/$', 
        r4010_inforra_listar_views.listar, 
        name='r4010_inforra'),

    url(r'^r4010-inforra/salvar/(?P<hash>.*)/$', 
        r4010_inforra_salvar_views.salvar, 
        name='r4010_inforra_salvar'),

    url(r'^r4010-inforra-despprocjud/apagar/(?P<hash>.*)/$', 
        r4010_inforra_despprocjud_apagar_views.apagar, 
        name='r4010_inforra_despprocjud_apagar'),

    url(r'^r4010-inforra-despprocjud/api/$',
        r4010_inforra_despprocjud_api_views.r4010infoRRAdespProcJudList.as_view() ),

    url(r'^r4010-inforra-despprocjud/api/(?P<pk>[0-9]+)/$',
        r4010_inforra_despprocjud_api_views.r4010infoRRAdespProcJudDetail.as_view() ),

    url(r'^r4010-inforra-despprocjud/listar/(?P<hash>.*)/$', 
        r4010_inforra_despprocjud_listar_views.listar, 
        name='r4010_inforra_despprocjud'),

    url(r'^r4010-inforra-despprocjud/salvar/(?P<hash>.*)/$', 
        r4010_inforra_despprocjud_salvar_views.salvar, 
        name='r4010_inforra_despprocjud_salvar'),

    url(r'^r4010-inforra-ideadv/apagar/(?P<hash>.*)/$', 
        r4010_inforra_ideadv_apagar_views.apagar, 
        name='r4010_inforra_ideadv_apagar'),

    url(r'^r4010-inforra-ideadv/api/$',
        r4010_inforra_ideadv_api_views.r4010infoRRAideAdvList.as_view() ),

    url(r'^r4010-inforra-ideadv/api/(?P<pk>[0-9]+)/$',
        r4010_inforra_ideadv_api_views.r4010infoRRAideAdvDetail.as_view() ),

    url(r'^r4010-inforra-ideadv/listar/(?P<hash>.*)/$', 
        r4010_inforra_ideadv_listar_views.listar, 
        name='r4010_inforra_ideadv'),

    url(r'^r4010-inforra-ideadv/salvar/(?P<hash>.*)/$', 
        r4010_inforra_ideadv_salvar_views.salvar, 
        name='r4010_inforra_ideadv_salvar'),

    url(r'^r4010-inforra-origemrec/apagar/(?P<hash>.*)/$', 
        r4010_inforra_origemrec_apagar_views.apagar, 
        name='r4010_inforra_origemrec_apagar'),

    url(r'^r4010-inforra-origemrec/api/$',
        r4010_inforra_origemrec_api_views.r4010infoRRAorigemRecList.as_view() ),

    url(r'^r4010-inforra-origemrec/api/(?P<pk>[0-9]+)/$',
        r4010_inforra_origemrec_api_views.r4010infoRRAorigemRecDetail.as_view() ),

    url(r'^r4010-inforra-origemrec/listar/(?P<hash>.*)/$', 
        r4010_inforra_origemrec_listar_views.listar, 
        name='r4010_inforra_origemrec'),

    url(r'^r4010-inforra-origemrec/salvar/(?P<hash>.*)/$', 
        r4010_inforra_origemrec_salvar_views.salvar, 
        name='r4010_inforra_origemrec_salvar'),

    url(r'^r4010-infoprocjud/apagar/(?P<hash>.*)/$', 
        r4010_infoprocjud_apagar_views.apagar, 
        name='r4010_infoprocjud_apagar'),

    url(r'^r4010-infoprocjud/api/$',
        r4010_infoprocjud_api_views.r4010infoProcJudList.as_view() ),

    url(r'^r4010-infoprocjud/api/(?P<pk>[0-9]+)/$',
        r4010_infoprocjud_api_views.r4010infoProcJudDetail.as_view() ),

    url(r'^r4010-infoprocjud/listar/(?P<hash>.*)/$', 
        r4010_infoprocjud_listar_views.listar, 
        name='r4010_infoprocjud'),

    url(r'^r4010-infoprocjud/salvar/(?P<hash>.*)/$', 
        r4010_infoprocjud_salvar_views.salvar, 
        name='r4010_infoprocjud_salvar'),

    url(r'^r4010-infoprocjud-despprocjud/apagar/(?P<hash>.*)/$', 
        r4010_infoprocjud_despprocjud_apagar_views.apagar, 
        name='r4010_infoprocjud_despprocjud_apagar'),

    url(r'^r4010-infoprocjud-despprocjud/api/$',
        r4010_infoprocjud_despprocjud_api_views.r4010infoProcJuddespProcJudList.as_view() ),

    url(r'^r4010-infoprocjud-despprocjud/api/(?P<pk>[0-9]+)/$',
        r4010_infoprocjud_despprocjud_api_views.r4010infoProcJuddespProcJudDetail.as_view() ),

    url(r'^r4010-infoprocjud-despprocjud/listar/(?P<hash>.*)/$', 
        r4010_infoprocjud_despprocjud_listar_views.listar, 
        name='r4010_infoprocjud_despprocjud'),

    url(r'^r4010-infoprocjud-despprocjud/salvar/(?P<hash>.*)/$', 
        r4010_infoprocjud_despprocjud_salvar_views.salvar, 
        name='r4010_infoprocjud_despprocjud_salvar'),

    url(r'^r4010-infoprocjud-ideadv/apagar/(?P<hash>.*)/$', 
        r4010_infoprocjud_ideadv_apagar_views.apagar, 
        name='r4010_infoprocjud_ideadv_apagar'),

    url(r'^r4010-infoprocjud-ideadv/api/$',
        r4010_infoprocjud_ideadv_api_views.r4010infoProcJudideAdvList.as_view() ),

    url(r'^r4010-infoprocjud-ideadv/api/(?P<pk>[0-9]+)/$',
        r4010_infoprocjud_ideadv_api_views.r4010infoProcJudideAdvDetail.as_view() ),

    url(r'^r4010-infoprocjud-ideadv/listar/(?P<hash>.*)/$', 
        r4010_infoprocjud_ideadv_listar_views.listar, 
        name='r4010_infoprocjud_ideadv'),

    url(r'^r4010-infoprocjud-ideadv/salvar/(?P<hash>.*)/$', 
        r4010_infoprocjud_ideadv_salvar_views.salvar, 
        name='r4010_infoprocjud_ideadv_salvar'),

    url(r'^r4010-infoprocjud-origemrec/apagar/(?P<hash>.*)/$', 
        r4010_infoprocjud_origemrec_apagar_views.apagar, 
        name='r4010_infoprocjud_origemrec_apagar'),

    url(r'^r4010-infoprocjud-origemrec/api/$',
        r4010_infoprocjud_origemrec_api_views.r4010infoProcJudorigemRecList.as_view() ),

    url(r'^r4010-infoprocjud-origemrec/api/(?P<pk>[0-9]+)/$',
        r4010_infoprocjud_origemrec_api_views.r4010infoProcJudorigemRecDetail.as_view() ),

    url(r'^r4010-infoprocjud-origemrec/listar/(?P<hash>.*)/$', 
        r4010_infoprocjud_origemrec_listar_views.listar, 
        name='r4010_infoprocjud_origemrec'),

    url(r'^r4010-infoprocjud-origemrec/salvar/(?P<hash>.*)/$', 
        r4010_infoprocjud_origemrec_salvar_views.salvar, 
        name='r4010_infoprocjud_origemrec_salvar'),

    url(r'^r4010-infopgtoext/apagar/(?P<hash>.*)/$', 
        r4010_infopgtoext_apagar_views.apagar, 
        name='r4010_infopgtoext_apagar'),

    url(r'^r4010-infopgtoext/api/$',
        r4010_infopgtoext_api_views.r4010infoPgtoExtList.as_view() ),

    url(r'^r4010-infopgtoext/api/(?P<pk>[0-9]+)/$',
        r4010_infopgtoext_api_views.r4010infoPgtoExtDetail.as_view() ),

    url(r'^r4010-infopgtoext/listar/(?P<hash>.*)/$', 
        r4010_infopgtoext_listar_views.listar, 
        name='r4010_infopgtoext'),

    url(r'^r4010-infopgtoext/salvar/(?P<hash>.*)/$', 
        r4010_infopgtoext_salvar_views.salvar, 
        name='r4010_infopgtoext_salvar'),

    url(r'^r4010-ideopsaude/apagar/(?P<hash>.*)/$', 
        r4010_ideopsaude_apagar_views.apagar, 
        name='r4010_ideopsaude_apagar'),

    url(r'^r4010-ideopsaude/api/$',
        r4010_ideopsaude_api_views.r4010ideOpSaudeList.as_view() ),

    url(r'^r4010-ideopsaude/api/(?P<pk>[0-9]+)/$',
        r4010_ideopsaude_api_views.r4010ideOpSaudeDetail.as_view() ),

    url(r'^r4010-ideopsaude/listar/(?P<hash>.*)/$', 
        r4010_ideopsaude_listar_views.listar, 
        name='r4010_ideopsaude'),

    url(r'^r4010-ideopsaude/salvar/(?P<hash>.*)/$', 
        r4010_ideopsaude_salvar_views.salvar, 
        name='r4010_ideopsaude_salvar'),

    url(r'^r4010-inforeemb/apagar/(?P<hash>.*)/$', 
        r4010_inforeemb_apagar_views.apagar, 
        name='r4010_inforeemb_apagar'),

    url(r'^r4010-inforeemb/api/$',
        r4010_inforeemb_api_views.r4010infoReembList.as_view() ),

    url(r'^r4010-inforeemb/api/(?P<pk>[0-9]+)/$',
        r4010_inforeemb_api_views.r4010infoReembDetail.as_view() ),

    url(r'^r4010-inforeemb/listar/(?P<hash>.*)/$', 
        r4010_inforeemb_listar_views.listar, 
        name='r4010_inforeemb'),

    url(r'^r4010-inforeemb/salvar/(?P<hash>.*)/$', 
        r4010_inforeemb_salvar_views.salvar, 
        name='r4010_inforeemb_salvar'),

    url(r'^r4010-infodependpl/apagar/(?P<hash>.*)/$', 
        r4010_infodependpl_apagar_views.apagar, 
        name='r4010_infodependpl_apagar'),

    url(r'^r4010-infodependpl/api/$',
        r4010_infodependpl_api_views.r4010infoDependPlList.as_view() ),

    url(r'^r4010-infodependpl/api/(?P<pk>[0-9]+)/$',
        r4010_infodependpl_api_views.r4010infoDependPlDetail.as_view() ),

    url(r'^r4010-infodependpl/listar/(?P<hash>.*)/$', 
        r4010_infodependpl_listar_views.listar, 
        name='r4010_infodependpl'),

    url(r'^r4010-infodependpl/salvar/(?P<hash>.*)/$', 
        r4010_infodependpl_salvar_views.salvar, 
        name='r4010_infodependpl_salvar'),

    url(r'^r4010-inforeembdep/apagar/(?P<hash>.*)/$', 
        r4010_inforeembdep_apagar_views.apagar, 
        name='r4010_inforeembdep_apagar'),

    url(r'^r4010-inforeembdep/api/$',
        r4010_inforeembdep_api_views.r4010infoReembDepList.as_view() ),

    url(r'^r4010-inforeembdep/api/(?P<pk>[0-9]+)/$',
        r4010_inforeembdep_api_views.r4010infoReembDepDetail.as_view() ),

    url(r'^r4010-inforeembdep/listar/(?P<hash>.*)/$', 
        r4010_inforeembdep_listar_views.listar, 
        name='r4010_inforeembdep'),

    url(r'^r4010-inforeembdep/salvar/(?P<hash>.*)/$', 
        r4010_inforeembdep_salvar_views.salvar, 
        name='r4010_inforeembdep_salvar'),


]