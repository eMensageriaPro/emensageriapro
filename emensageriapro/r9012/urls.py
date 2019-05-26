#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.r9012.views import r9012_regocorrs_apagar as r9012_regocorrs_apagar_views
from emensageriapro.r9012.views import r9012_regocorrs_listar as r9012_regocorrs_listar_views
from emensageriapro.r9012.views import r9012_regocorrs_salvar as r9012_regocorrs_salvar_views
from emensageriapro.r9012.views import r9012_regocorrs_api as r9012_regocorrs_api_views
from emensageriapro.r9012.views import r9012_infototalcontrib_apagar as r9012_infototalcontrib_apagar_views
from emensageriapro.r9012.views import r9012_infototalcontrib_listar as r9012_infototalcontrib_listar_views
from emensageriapro.r9012.views import r9012_infototalcontrib_salvar as r9012_infototalcontrib_salvar_views
from emensageriapro.r9012.views import r9012_infototalcontrib_api as r9012_infototalcontrib_api_views
from emensageriapro.r9012.views import r9012_totapurmen_apagar as r9012_totapurmen_apagar_views
from emensageriapro.r9012.views import r9012_totapurmen_listar as r9012_totapurmen_listar_views
from emensageriapro.r9012.views import r9012_totapurmen_salvar as r9012_totapurmen_salvar_views
from emensageriapro.r9012.views import r9012_totapurmen_api as r9012_totapurmen_api_views
from emensageriapro.r9012.views import r9012_totapurqui_apagar as r9012_totapurqui_apagar_views
from emensageriapro.r9012.views import r9012_totapurqui_listar as r9012_totapurqui_listar_views
from emensageriapro.r9012.views import r9012_totapurqui_salvar as r9012_totapurqui_salvar_views
from emensageriapro.r9012.views import r9012_totapurqui_api as r9012_totapurqui_api_views
from emensageriapro.r9012.views import r9012_totapurdec_apagar as r9012_totapurdec_apagar_views
from emensageriapro.r9012.views import r9012_totapurdec_listar as r9012_totapurdec_listar_views
from emensageriapro.r9012.views import r9012_totapurdec_salvar as r9012_totapurdec_salvar_views
from emensageriapro.r9012.views import r9012_totapurdec_api as r9012_totapurdec_api_views
from emensageriapro.r9012.views import r9012_totapursem_apagar as r9012_totapursem_apagar_views
from emensageriapro.r9012.views import r9012_totapursem_listar as r9012_totapursem_listar_views
from emensageriapro.r9012.views import r9012_totapursem_salvar as r9012_totapursem_salvar_views
from emensageriapro.r9012.views import r9012_totapursem_api as r9012_totapursem_api_views
from emensageriapro.r9012.views import r9012_totapurdia_apagar as r9012_totapurdia_apagar_views
from emensageriapro.r9012.views import r9012_totapurdia_listar as r9012_totapurdia_listar_views
from emensageriapro.r9012.views import r9012_totapurdia_salvar as r9012_totapurdia_salvar_views
from emensageriapro.r9012.views import r9012_totapurdia_api as r9012_totapurdia_api_views



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


    url(r'^r9012-regocorrs/apagar/(?P<hash>.*)/$', 
        r9012_regocorrs_apagar_views.apagar, 
        name='r9012_regocorrs_apagar'),

    url(r'^r9012-regocorrs/api/$',
        r9012_regocorrs_api_views.r9012regOcorrsList.as_view() ),

    url(r'^r9012-regocorrs/api/(?P<pk>[0-9]+)/$',
        r9012_regocorrs_api_views.r9012regOcorrsDetail.as_view() ),

    url(r'^r9012-regocorrs/listar/(?P<hash>.*)/$', 
        r9012_regocorrs_listar_views.listar, 
        name='r9012_regocorrs'),

    url(r'^r9012-regocorrs/salvar/(?P<hash>.*)/$', 
        r9012_regocorrs_salvar_views.salvar, 
        name='r9012_regocorrs_salvar'),

    url(r'^r9012-infototalcontrib/apagar/(?P<hash>.*)/$', 
        r9012_infototalcontrib_apagar_views.apagar, 
        name='r9012_infototalcontrib_apagar'),

    url(r'^r9012-infototalcontrib/api/$',
        r9012_infototalcontrib_api_views.r9012infoTotalContribList.as_view() ),

    url(r'^r9012-infototalcontrib/api/(?P<pk>[0-9]+)/$',
        r9012_infototalcontrib_api_views.r9012infoTotalContribDetail.as_view() ),

    url(r'^r9012-infototalcontrib/listar/(?P<hash>.*)/$', 
        r9012_infototalcontrib_listar_views.listar, 
        name='r9012_infototalcontrib'),

    url(r'^r9012-infototalcontrib/salvar/(?P<hash>.*)/$', 
        r9012_infototalcontrib_salvar_views.salvar, 
        name='r9012_infototalcontrib_salvar'),

    url(r'^r9012-totapurmen/apagar/(?P<hash>.*)/$', 
        r9012_totapurmen_apagar_views.apagar, 
        name='r9012_totapurmen_apagar'),

    url(r'^r9012-totapurmen/api/$',
        r9012_totapurmen_api_views.r9012totApurMenList.as_view() ),

    url(r'^r9012-totapurmen/api/(?P<pk>[0-9]+)/$',
        r9012_totapurmen_api_views.r9012totApurMenDetail.as_view() ),

    url(r'^r9012-totapurmen/listar/(?P<hash>.*)/$', 
        r9012_totapurmen_listar_views.listar, 
        name='r9012_totapurmen'),

    url(r'^r9012-totapurmen/salvar/(?P<hash>.*)/$', 
        r9012_totapurmen_salvar_views.salvar, 
        name='r9012_totapurmen_salvar'),

    url(r'^r9012-totapurqui/apagar/(?P<hash>.*)/$', 
        r9012_totapurqui_apagar_views.apagar, 
        name='r9012_totapurqui_apagar'),

    url(r'^r9012-totapurqui/api/$',
        r9012_totapurqui_api_views.r9012totApurQuiList.as_view() ),

    url(r'^r9012-totapurqui/api/(?P<pk>[0-9]+)/$',
        r9012_totapurqui_api_views.r9012totApurQuiDetail.as_view() ),

    url(r'^r9012-totapurqui/listar/(?P<hash>.*)/$', 
        r9012_totapurqui_listar_views.listar, 
        name='r9012_totapurqui'),

    url(r'^r9012-totapurqui/salvar/(?P<hash>.*)/$', 
        r9012_totapurqui_salvar_views.salvar, 
        name='r9012_totapurqui_salvar'),

    url(r'^r9012-totapurdec/apagar/(?P<hash>.*)/$', 
        r9012_totapurdec_apagar_views.apagar, 
        name='r9012_totapurdec_apagar'),

    url(r'^r9012-totapurdec/api/$',
        r9012_totapurdec_api_views.r9012totApurDecList.as_view() ),

    url(r'^r9012-totapurdec/api/(?P<pk>[0-9]+)/$',
        r9012_totapurdec_api_views.r9012totApurDecDetail.as_view() ),

    url(r'^r9012-totapurdec/listar/(?P<hash>.*)/$', 
        r9012_totapurdec_listar_views.listar, 
        name='r9012_totapurdec'),

    url(r'^r9012-totapurdec/salvar/(?P<hash>.*)/$', 
        r9012_totapurdec_salvar_views.salvar, 
        name='r9012_totapurdec_salvar'),

    url(r'^r9012-totapursem/apagar/(?P<hash>.*)/$', 
        r9012_totapursem_apagar_views.apagar, 
        name='r9012_totapursem_apagar'),

    url(r'^r9012-totapursem/api/$',
        r9012_totapursem_api_views.r9012totApurSemList.as_view() ),

    url(r'^r9012-totapursem/api/(?P<pk>[0-9]+)/$',
        r9012_totapursem_api_views.r9012totApurSemDetail.as_view() ),

    url(r'^r9012-totapursem/listar/(?P<hash>.*)/$', 
        r9012_totapursem_listar_views.listar, 
        name='r9012_totapursem'),

    url(r'^r9012-totapursem/salvar/(?P<hash>.*)/$', 
        r9012_totapursem_salvar_views.salvar, 
        name='r9012_totapursem_salvar'),

    url(r'^r9012-totapurdia/apagar/(?P<hash>.*)/$', 
        r9012_totapurdia_apagar_views.apagar, 
        name='r9012_totapurdia_apagar'),

    url(r'^r9012-totapurdia/api/$',
        r9012_totapurdia_api_views.r9012totApurDiaList.as_view() ),

    url(r'^r9012-totapurdia/api/(?P<pk>[0-9]+)/$',
        r9012_totapurdia_api_views.r9012totApurDiaDetail.as_view() ),

    url(r'^r9012-totapurdia/listar/(?P<hash>.*)/$', 
        r9012_totapurdia_listar_views.listar, 
        name='r9012_totapurdia'),

    url(r'^r9012-totapurdia/salvar/(?P<hash>.*)/$', 
        r9012_totapurdia_salvar_views.salvar, 
        name='r9012_totapurdia_salvar'),


]