#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s5011.views import s5011_infocpseg_apagar as s5011_infocpseg_apagar_views
from emensageriapro.s5011.views import s5011_infocpseg_listar as s5011_infocpseg_listar_views
from emensageriapro.s5011.views import s5011_infocpseg_salvar as s5011_infocpseg_salvar_views
from emensageriapro.s5011.views import s5011_infocpseg_api as s5011_infocpseg_api_views
from emensageriapro.s5011.views import s5011_infopj_apagar as s5011_infopj_apagar_views
from emensageriapro.s5011.views import s5011_infopj_listar as s5011_infopj_listar_views
from emensageriapro.s5011.views import s5011_infopj_salvar as s5011_infopj_salvar_views
from emensageriapro.s5011.views import s5011_infopj_api as s5011_infopj_api_views
from emensageriapro.s5011.views import s5011_infoatconc_apagar as s5011_infoatconc_apagar_views
from emensageriapro.s5011.views import s5011_infoatconc_listar as s5011_infoatconc_listar_views
from emensageriapro.s5011.views import s5011_infoatconc_salvar as s5011_infoatconc_salvar_views
from emensageriapro.s5011.views import s5011_infoatconc_api as s5011_infoatconc_api_views
from emensageriapro.s5011.views import s5011_ideestab_apagar as s5011_ideestab_apagar_views
from emensageriapro.s5011.views import s5011_ideestab_listar as s5011_ideestab_listar_views
from emensageriapro.s5011.views import s5011_ideestab_salvar as s5011_ideestab_salvar_views
from emensageriapro.s5011.views import s5011_ideestab_api as s5011_ideestab_api_views
from emensageriapro.s5011.views import s5011_infoestab_apagar as s5011_infoestab_apagar_views
from emensageriapro.s5011.views import s5011_infoestab_listar as s5011_infoestab_listar_views
from emensageriapro.s5011.views import s5011_infoestab_salvar as s5011_infoestab_salvar_views
from emensageriapro.s5011.views import s5011_infoestab_api as s5011_infoestab_api_views
from emensageriapro.s5011.views import s5011_infocomplobra_apagar as s5011_infocomplobra_apagar_views
from emensageriapro.s5011.views import s5011_infocomplobra_listar as s5011_infocomplobra_listar_views
from emensageriapro.s5011.views import s5011_infocomplobra_salvar as s5011_infocomplobra_salvar_views
from emensageriapro.s5011.views import s5011_infocomplobra_api as s5011_infocomplobra_api_views
from emensageriapro.s5011.views import s5011_idelotacao_apagar as s5011_idelotacao_apagar_views
from emensageriapro.s5011.views import s5011_idelotacao_listar as s5011_idelotacao_listar_views
from emensageriapro.s5011.views import s5011_idelotacao_salvar as s5011_idelotacao_salvar_views
from emensageriapro.s5011.views import s5011_idelotacao_api as s5011_idelotacao_api_views
from emensageriapro.s5011.views import s5011_infotercsusp_apagar as s5011_infotercsusp_apagar_views
from emensageriapro.s5011.views import s5011_infotercsusp_listar as s5011_infotercsusp_listar_views
from emensageriapro.s5011.views import s5011_infotercsusp_salvar as s5011_infotercsusp_salvar_views
from emensageriapro.s5011.views import s5011_infotercsusp_api as s5011_infotercsusp_api_views
from emensageriapro.s5011.views import s5011_infoemprparcial_apagar as s5011_infoemprparcial_apagar_views
from emensageriapro.s5011.views import s5011_infoemprparcial_listar as s5011_infoemprparcial_listar_views
from emensageriapro.s5011.views import s5011_infoemprparcial_salvar as s5011_infoemprparcial_salvar_views
from emensageriapro.s5011.views import s5011_infoemprparcial_api as s5011_infoemprparcial_api_views
from emensageriapro.s5011.views import s5011_dadosopport_apagar as s5011_dadosopport_apagar_views
from emensageriapro.s5011.views import s5011_dadosopport_listar as s5011_dadosopport_listar_views
from emensageriapro.s5011.views import s5011_dadosopport_salvar as s5011_dadosopport_salvar_views
from emensageriapro.s5011.views import s5011_dadosopport_api as s5011_dadosopport_api_views
from emensageriapro.s5011.views import s5011_basesremun_apagar as s5011_basesremun_apagar_views
from emensageriapro.s5011.views import s5011_basesremun_listar as s5011_basesremun_listar_views
from emensageriapro.s5011.views import s5011_basesremun_salvar as s5011_basesremun_salvar_views
from emensageriapro.s5011.views import s5011_basesremun_api as s5011_basesremun_api_views
from emensageriapro.s5011.views import s5011_basesavnport_apagar as s5011_basesavnport_apagar_views
from emensageriapro.s5011.views import s5011_basesavnport_listar as s5011_basesavnport_listar_views
from emensageriapro.s5011.views import s5011_basesavnport_salvar as s5011_basesavnport_salvar_views
from emensageriapro.s5011.views import s5011_basesavnport_api as s5011_basesavnport_api_views
from emensageriapro.s5011.views import s5011_infosubstpatropport_apagar as s5011_infosubstpatropport_apagar_views
from emensageriapro.s5011.views import s5011_infosubstpatropport_listar as s5011_infosubstpatropport_listar_views
from emensageriapro.s5011.views import s5011_infosubstpatropport_salvar as s5011_infosubstpatropport_salvar_views
from emensageriapro.s5011.views import s5011_infosubstpatropport_api as s5011_infosubstpatropport_api_views
from emensageriapro.s5011.views import s5011_basesaquis_apagar as s5011_basesaquis_apagar_views
from emensageriapro.s5011.views import s5011_basesaquis_listar as s5011_basesaquis_listar_views
from emensageriapro.s5011.views import s5011_basesaquis_salvar as s5011_basesaquis_salvar_views
from emensageriapro.s5011.views import s5011_basesaquis_api as s5011_basesaquis_api_views
from emensageriapro.s5011.views import s5011_basescomerc_apagar as s5011_basescomerc_apagar_views
from emensageriapro.s5011.views import s5011_basescomerc_listar as s5011_basescomerc_listar_views
from emensageriapro.s5011.views import s5011_basescomerc_salvar as s5011_basescomerc_salvar_views
from emensageriapro.s5011.views import s5011_basescomerc_api as s5011_basescomerc_api_views
from emensageriapro.s5011.views import s5011_infocrestab_apagar as s5011_infocrestab_apagar_views
from emensageriapro.s5011.views import s5011_infocrestab_listar as s5011_infocrestab_listar_views
from emensageriapro.s5011.views import s5011_infocrestab_salvar as s5011_infocrestab_salvar_views
from emensageriapro.s5011.views import s5011_infocrestab_api as s5011_infocrestab_api_views
from emensageriapro.s5011.views import s5011_infocrcontrib_apagar as s5011_infocrcontrib_apagar_views
from emensageriapro.s5011.views import s5011_infocrcontrib_listar as s5011_infocrcontrib_listar_views
from emensageriapro.s5011.views import s5011_infocrcontrib_salvar as s5011_infocrcontrib_salvar_views
from emensageriapro.s5011.views import s5011_infocrcontrib_api as s5011_infocrcontrib_api_views



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


    url(r'^s5011-infocpseg/apagar/(?P<hash>.*)/$', 
        s5011_infocpseg_apagar_views.apagar, 
        name='s5011_infocpseg_apagar'),

    url(r'^s5011-infocpseg/api/$',
        s5011_infocpseg_api_views.s5011infoCPSegList.as_view() ),

    url(r'^s5011-infocpseg/api/(?P<pk>[0-9]+)/$',
        s5011_infocpseg_api_views.s5011infoCPSegDetail.as_view() ),

    url(r'^s5011-infocpseg/listar/(?P<hash>.*)/$', 
        s5011_infocpseg_listar_views.listar, 
        name='s5011_infocpseg'),

    url(r'^s5011-infocpseg/salvar/(?P<hash>.*)/$', 
        s5011_infocpseg_salvar_views.salvar, 
        name='s5011_infocpseg_salvar'),

    url(r'^s5011-infopj/apagar/(?P<hash>.*)/$', 
        s5011_infopj_apagar_views.apagar, 
        name='s5011_infopj_apagar'),

    url(r'^s5011-infopj/api/$',
        s5011_infopj_api_views.s5011infoPJList.as_view() ),

    url(r'^s5011-infopj/api/(?P<pk>[0-9]+)/$',
        s5011_infopj_api_views.s5011infoPJDetail.as_view() ),

    url(r'^s5011-infopj/listar/(?P<hash>.*)/$', 
        s5011_infopj_listar_views.listar, 
        name='s5011_infopj'),

    url(r'^s5011-infopj/salvar/(?P<hash>.*)/$', 
        s5011_infopj_salvar_views.salvar, 
        name='s5011_infopj_salvar'),

    url(r'^s5011-infoatconc/apagar/(?P<hash>.*)/$', 
        s5011_infoatconc_apagar_views.apagar, 
        name='s5011_infoatconc_apagar'),

    url(r'^s5011-infoatconc/api/$',
        s5011_infoatconc_api_views.s5011infoAtConcList.as_view() ),

    url(r'^s5011-infoatconc/api/(?P<pk>[0-9]+)/$',
        s5011_infoatconc_api_views.s5011infoAtConcDetail.as_view() ),

    url(r'^s5011-infoatconc/listar/(?P<hash>.*)/$', 
        s5011_infoatconc_listar_views.listar, 
        name='s5011_infoatconc'),

    url(r'^s5011-infoatconc/salvar/(?P<hash>.*)/$', 
        s5011_infoatconc_salvar_views.salvar, 
        name='s5011_infoatconc_salvar'),

    url(r'^s5011-ideestab/apagar/(?P<hash>.*)/$', 
        s5011_ideestab_apagar_views.apagar, 
        name='s5011_ideestab_apagar'),

    url(r'^s5011-ideestab/api/$',
        s5011_ideestab_api_views.s5011ideEstabList.as_view() ),

    url(r'^s5011-ideestab/api/(?P<pk>[0-9]+)/$',
        s5011_ideestab_api_views.s5011ideEstabDetail.as_view() ),

    url(r'^s5011-ideestab/listar/(?P<hash>.*)/$', 
        s5011_ideestab_listar_views.listar, 
        name='s5011_ideestab'),

    url(r'^s5011-ideestab/salvar/(?P<hash>.*)/$', 
        s5011_ideestab_salvar_views.salvar, 
        name='s5011_ideestab_salvar'),

    url(r'^s5011-infoestab/apagar/(?P<hash>.*)/$', 
        s5011_infoestab_apagar_views.apagar, 
        name='s5011_infoestab_apagar'),

    url(r'^s5011-infoestab/api/$',
        s5011_infoestab_api_views.s5011infoEstabList.as_view() ),

    url(r'^s5011-infoestab/api/(?P<pk>[0-9]+)/$',
        s5011_infoestab_api_views.s5011infoEstabDetail.as_view() ),

    url(r'^s5011-infoestab/listar/(?P<hash>.*)/$', 
        s5011_infoestab_listar_views.listar, 
        name='s5011_infoestab'),

    url(r'^s5011-infoestab/salvar/(?P<hash>.*)/$', 
        s5011_infoestab_salvar_views.salvar, 
        name='s5011_infoestab_salvar'),

    url(r'^s5011-infocomplobra/apagar/(?P<hash>.*)/$', 
        s5011_infocomplobra_apagar_views.apagar, 
        name='s5011_infocomplobra_apagar'),

    url(r'^s5011-infocomplobra/api/$',
        s5011_infocomplobra_api_views.s5011infoComplObraList.as_view() ),

    url(r'^s5011-infocomplobra/api/(?P<pk>[0-9]+)/$',
        s5011_infocomplobra_api_views.s5011infoComplObraDetail.as_view() ),

    url(r'^s5011-infocomplobra/listar/(?P<hash>.*)/$', 
        s5011_infocomplobra_listar_views.listar, 
        name='s5011_infocomplobra'),

    url(r'^s5011-infocomplobra/salvar/(?P<hash>.*)/$', 
        s5011_infocomplobra_salvar_views.salvar, 
        name='s5011_infocomplobra_salvar'),

    url(r'^s5011-idelotacao/apagar/(?P<hash>.*)/$', 
        s5011_idelotacao_apagar_views.apagar, 
        name='s5011_idelotacao_apagar'),

    url(r'^s5011-idelotacao/api/$',
        s5011_idelotacao_api_views.s5011ideLotacaoList.as_view() ),

    url(r'^s5011-idelotacao/api/(?P<pk>[0-9]+)/$',
        s5011_idelotacao_api_views.s5011ideLotacaoDetail.as_view() ),

    url(r'^s5011-idelotacao/listar/(?P<hash>.*)/$', 
        s5011_idelotacao_listar_views.listar, 
        name='s5011_idelotacao'),

    url(r'^s5011-idelotacao/salvar/(?P<hash>.*)/$', 
        s5011_idelotacao_salvar_views.salvar, 
        name='s5011_idelotacao_salvar'),

    url(r'^s5011-infotercsusp/apagar/(?P<hash>.*)/$', 
        s5011_infotercsusp_apagar_views.apagar, 
        name='s5011_infotercsusp_apagar'),

    url(r'^s5011-infotercsusp/api/$',
        s5011_infotercsusp_api_views.s5011infoTercSuspList.as_view() ),

    url(r'^s5011-infotercsusp/api/(?P<pk>[0-9]+)/$',
        s5011_infotercsusp_api_views.s5011infoTercSuspDetail.as_view() ),

    url(r'^s5011-infotercsusp/listar/(?P<hash>.*)/$', 
        s5011_infotercsusp_listar_views.listar, 
        name='s5011_infotercsusp'),

    url(r'^s5011-infotercsusp/salvar/(?P<hash>.*)/$', 
        s5011_infotercsusp_salvar_views.salvar, 
        name='s5011_infotercsusp_salvar'),

    url(r'^s5011-infoemprparcial/apagar/(?P<hash>.*)/$', 
        s5011_infoemprparcial_apagar_views.apagar, 
        name='s5011_infoemprparcial_apagar'),

    url(r'^s5011-infoemprparcial/api/$',
        s5011_infoemprparcial_api_views.s5011infoEmprParcialList.as_view() ),

    url(r'^s5011-infoemprparcial/api/(?P<pk>[0-9]+)/$',
        s5011_infoemprparcial_api_views.s5011infoEmprParcialDetail.as_view() ),

    url(r'^s5011-infoemprparcial/listar/(?P<hash>.*)/$', 
        s5011_infoemprparcial_listar_views.listar, 
        name='s5011_infoemprparcial'),

    url(r'^s5011-infoemprparcial/salvar/(?P<hash>.*)/$', 
        s5011_infoemprparcial_salvar_views.salvar, 
        name='s5011_infoemprparcial_salvar'),

    url(r'^s5011-dadosopport/apagar/(?P<hash>.*)/$', 
        s5011_dadosopport_apagar_views.apagar, 
        name='s5011_dadosopport_apagar'),

    url(r'^s5011-dadosopport/api/$',
        s5011_dadosopport_api_views.s5011dadosOpPortList.as_view() ),

    url(r'^s5011-dadosopport/api/(?P<pk>[0-9]+)/$',
        s5011_dadosopport_api_views.s5011dadosOpPortDetail.as_view() ),

    url(r'^s5011-dadosopport/listar/(?P<hash>.*)/$', 
        s5011_dadosopport_listar_views.listar, 
        name='s5011_dadosopport'),

    url(r'^s5011-dadosopport/salvar/(?P<hash>.*)/$', 
        s5011_dadosopport_salvar_views.salvar, 
        name='s5011_dadosopport_salvar'),

    url(r'^s5011-basesremun/apagar/(?P<hash>.*)/$', 
        s5011_basesremun_apagar_views.apagar, 
        name='s5011_basesremun_apagar'),

    url(r'^s5011-basesremun/api/$',
        s5011_basesremun_api_views.s5011basesRemunList.as_view() ),

    url(r'^s5011-basesremun/api/(?P<pk>[0-9]+)/$',
        s5011_basesremun_api_views.s5011basesRemunDetail.as_view() ),

    url(r'^s5011-basesremun/listar/(?P<hash>.*)/$', 
        s5011_basesremun_listar_views.listar, 
        name='s5011_basesremun'),

    url(r'^s5011-basesremun/salvar/(?P<hash>.*)/$', 
        s5011_basesremun_salvar_views.salvar, 
        name='s5011_basesremun_salvar'),

    url(r'^s5011-basesavnport/apagar/(?P<hash>.*)/$', 
        s5011_basesavnport_apagar_views.apagar, 
        name='s5011_basesavnport_apagar'),

    url(r'^s5011-basesavnport/api/$',
        s5011_basesavnport_api_views.s5011basesAvNPortList.as_view() ),

    url(r'^s5011-basesavnport/api/(?P<pk>[0-9]+)/$',
        s5011_basesavnport_api_views.s5011basesAvNPortDetail.as_view() ),

    url(r'^s5011-basesavnport/listar/(?P<hash>.*)/$', 
        s5011_basesavnport_listar_views.listar, 
        name='s5011_basesavnport'),

    url(r'^s5011-basesavnport/salvar/(?P<hash>.*)/$', 
        s5011_basesavnport_salvar_views.salvar, 
        name='s5011_basesavnport_salvar'),

    url(r'^s5011-infosubstpatropport/apagar/(?P<hash>.*)/$', 
        s5011_infosubstpatropport_apagar_views.apagar, 
        name='s5011_infosubstpatropport_apagar'),

    url(r'^s5011-infosubstpatropport/api/$',
        s5011_infosubstpatropport_api_views.s5011infoSubstPatrOpPortList.as_view() ),

    url(r'^s5011-infosubstpatropport/api/(?P<pk>[0-9]+)/$',
        s5011_infosubstpatropport_api_views.s5011infoSubstPatrOpPortDetail.as_view() ),

    url(r'^s5011-infosubstpatropport/listar/(?P<hash>.*)/$', 
        s5011_infosubstpatropport_listar_views.listar, 
        name='s5011_infosubstpatropport'),

    url(r'^s5011-infosubstpatropport/salvar/(?P<hash>.*)/$', 
        s5011_infosubstpatropport_salvar_views.salvar, 
        name='s5011_infosubstpatropport_salvar'),

    url(r'^s5011-basesaquis/apagar/(?P<hash>.*)/$', 
        s5011_basesaquis_apagar_views.apagar, 
        name='s5011_basesaquis_apagar'),

    url(r'^s5011-basesaquis/api/$',
        s5011_basesaquis_api_views.s5011basesAquisList.as_view() ),

    url(r'^s5011-basesaquis/api/(?P<pk>[0-9]+)/$',
        s5011_basesaquis_api_views.s5011basesAquisDetail.as_view() ),

    url(r'^s5011-basesaquis/listar/(?P<hash>.*)/$', 
        s5011_basesaquis_listar_views.listar, 
        name='s5011_basesaquis'),

    url(r'^s5011-basesaquis/salvar/(?P<hash>.*)/$', 
        s5011_basesaquis_salvar_views.salvar, 
        name='s5011_basesaquis_salvar'),

    url(r'^s5011-basescomerc/apagar/(?P<hash>.*)/$', 
        s5011_basescomerc_apagar_views.apagar, 
        name='s5011_basescomerc_apagar'),

    url(r'^s5011-basescomerc/api/$',
        s5011_basescomerc_api_views.s5011basesComercList.as_view() ),

    url(r'^s5011-basescomerc/api/(?P<pk>[0-9]+)/$',
        s5011_basescomerc_api_views.s5011basesComercDetail.as_view() ),

    url(r'^s5011-basescomerc/listar/(?P<hash>.*)/$', 
        s5011_basescomerc_listar_views.listar, 
        name='s5011_basescomerc'),

    url(r'^s5011-basescomerc/salvar/(?P<hash>.*)/$', 
        s5011_basescomerc_salvar_views.salvar, 
        name='s5011_basescomerc_salvar'),

    url(r'^s5011-infocrestab/apagar/(?P<hash>.*)/$', 
        s5011_infocrestab_apagar_views.apagar, 
        name='s5011_infocrestab_apagar'),

    url(r'^s5011-infocrestab/api/$',
        s5011_infocrestab_api_views.s5011infoCREstabList.as_view() ),

    url(r'^s5011-infocrestab/api/(?P<pk>[0-9]+)/$',
        s5011_infocrestab_api_views.s5011infoCREstabDetail.as_view() ),

    url(r'^s5011-infocrestab/listar/(?P<hash>.*)/$', 
        s5011_infocrestab_listar_views.listar, 
        name='s5011_infocrestab'),

    url(r'^s5011-infocrestab/salvar/(?P<hash>.*)/$', 
        s5011_infocrestab_salvar_views.salvar, 
        name='s5011_infocrestab_salvar'),

    url(r'^s5011-infocrcontrib/apagar/(?P<hash>.*)/$', 
        s5011_infocrcontrib_apagar_views.apagar, 
        name='s5011_infocrcontrib_apagar'),

    url(r'^s5011-infocrcontrib/api/$',
        s5011_infocrcontrib_api_views.s5011infoCRContribList.as_view() ),

    url(r'^s5011-infocrcontrib/api/(?P<pk>[0-9]+)/$',
        s5011_infocrcontrib_api_views.s5011infoCRContribDetail.as_view() ),

    url(r'^s5011-infocrcontrib/listar/(?P<hash>.*)/$', 
        s5011_infocrcontrib_listar_views.listar, 
        name='s5011_infocrcontrib'),

    url(r'^s5011-infocrcontrib/salvar/(?P<hash>.*)/$', 
        s5011_infocrcontrib_salvar_views.salvar, 
        name='s5011_infocrcontrib_salvar'),


]