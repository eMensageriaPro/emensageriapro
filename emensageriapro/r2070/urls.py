#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.r2070.views import r2070_compjud as r2070_compjud_views
from emensageriapro.r2070.views import r2070_depjudicial as r2070_depjudicial_views
from emensageriapro.r2070.views import r2070_detcompet as r2070_detcompet_views
from emensageriapro.r2070.views import r2070_detdeducao as r2070_detdeducao_views
from emensageriapro.r2070.views import r2070_ideestab as r2070_ideestab_views
from emensageriapro.r2070.views import r2070_infomolestia as r2070_infomolestia_views
from emensageriapro.r2070.views import r2070_infoprocjud as r2070_infoprocjud_views
from emensageriapro.r2070.views import r2070_infoprocjud_despprocjud as r2070_infoprocjud_despprocjud_views
from emensageriapro.r2070.views import r2070_infoprocjud_ideadvogado as r2070_infoprocjud_ideadvogado_views
from emensageriapro.r2070.views import r2070_infoprocjud_origemrecursos as r2070_infoprocjud_origemrecursos_views
from emensageriapro.r2070.views import r2070_inforra as r2070_inforra_views
from emensageriapro.r2070.views import r2070_inforra_despprocjud as r2070_inforra_despprocjud_views
from emensageriapro.r2070.views import r2070_inforra_ideadvogado as r2070_inforra_ideadvogado_views
from emensageriapro.r2070.views import r2070_inforesidext as r2070_inforesidext_views
from emensageriapro.r2070.views import r2070_pgtopf as r2070_pgtopf_views
from emensageriapro.r2070.views import r2070_pgtopj as r2070_pgtopj_views
from emensageriapro.r2070.views import r2070_pgtopj_despprocjud as r2070_pgtopj_despprocjud_views
from emensageriapro.r2070.views import r2070_pgtopj_ideadvogado as r2070_pgtopj_ideadvogado_views
from emensageriapro.r2070.views import r2070_pgtopj_infoprocjud as r2070_pgtopj_infoprocjud_views
from emensageriapro.r2070.views import r2070_pgtopj_origemrecursos as r2070_pgtopj_origemrecursos_views
from emensageriapro.r2070.views import r2070_pgtoresidext as r2070_pgtoresidext_views
from emensageriapro.r2070.views import r2070_rendisento as r2070_rendisento_views



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



url(r'^r2070-compjud/apagar/(?P<hash>.*)/$', 
        r2070_compjud_views.apagar, 
        name='r2070_compjud_apagar'),

url(r'^r2070-compjud/api/$',
            r2070_compjud_views.r2070compJudList.as_view() ),

        url(r'^r2070-compjud/api/(?P<pk>[0-9]+)/$',
            r2070_compjud_views.r2070compJudDetail.as_view() ),

url(r'^r2070-compjud/listar/(?P<hash>.*)/$', 
        r2070_compjud_views.listar, 
        name='r2070_compjud'),

url(r'^r2070-compjud/salvar/(?P<hash>.*)/$', 
        r2070_compjud_views.salvar, 
        name='r2070_compjud_salvar'),



url(r'^r2070-depjudicial/apagar/(?P<hash>.*)/$', 
        r2070_depjudicial_views.apagar, 
        name='r2070_depjudicial_apagar'),

url(r'^r2070-depjudicial/api/$',
            r2070_depjudicial_views.r2070depJudicialList.as_view() ),

        url(r'^r2070-depjudicial/api/(?P<pk>[0-9]+)/$',
            r2070_depjudicial_views.r2070depJudicialDetail.as_view() ),

url(r'^r2070-depjudicial/listar/(?P<hash>.*)/$', 
        r2070_depjudicial_views.listar, 
        name='r2070_depjudicial'),

url(r'^r2070-depjudicial/salvar/(?P<hash>.*)/$', 
        r2070_depjudicial_views.salvar, 
        name='r2070_depjudicial_salvar'),



url(r'^r2070-detcompet/apagar/(?P<hash>.*)/$', 
        r2070_detcompet_views.apagar, 
        name='r2070_detcompet_apagar'),

url(r'^r2070-detcompet/api/$',
            r2070_detcompet_views.r2070detCompetList.as_view() ),

        url(r'^r2070-detcompet/api/(?P<pk>[0-9]+)/$',
            r2070_detcompet_views.r2070detCompetDetail.as_view() ),

url(r'^r2070-detcompet/listar/(?P<hash>.*)/$', 
        r2070_detcompet_views.listar, 
        name='r2070_detcompet'),

url(r'^r2070-detcompet/salvar/(?P<hash>.*)/$', 
        r2070_detcompet_views.salvar, 
        name='r2070_detcompet_salvar'),



url(r'^r2070-detdeducao/apagar/(?P<hash>.*)/$', 
        r2070_detdeducao_views.apagar, 
        name='r2070_detdeducao_apagar'),

url(r'^r2070-detdeducao/api/$',
            r2070_detdeducao_views.r2070detDeducaoList.as_view() ),

        url(r'^r2070-detdeducao/api/(?P<pk>[0-9]+)/$',
            r2070_detdeducao_views.r2070detDeducaoDetail.as_view() ),

url(r'^r2070-detdeducao/listar/(?P<hash>.*)/$', 
        r2070_detdeducao_views.listar, 
        name='r2070_detdeducao'),

url(r'^r2070-detdeducao/salvar/(?P<hash>.*)/$', 
        r2070_detdeducao_views.salvar, 
        name='r2070_detdeducao_salvar'),



url(r'^r2070-ideestab/apagar/(?P<hash>.*)/$', 
        r2070_ideestab_views.apagar, 
        name='r2070_ideestab_apagar'),

url(r'^r2070-ideestab/api/$',
            r2070_ideestab_views.r2070ideEstabList.as_view() ),

        url(r'^r2070-ideestab/api/(?P<pk>[0-9]+)/$',
            r2070_ideestab_views.r2070ideEstabDetail.as_view() ),

url(r'^r2070-ideestab/listar/(?P<hash>.*)/$', 
        r2070_ideestab_views.listar, 
        name='r2070_ideestab'),

url(r'^r2070-ideestab/salvar/(?P<hash>.*)/$', 
        r2070_ideestab_views.salvar, 
        name='r2070_ideestab_salvar'),



url(r'^r2070-infomolestia/apagar/(?P<hash>.*)/$', 
        r2070_infomolestia_views.apagar, 
        name='r2070_infomolestia_apagar'),

url(r'^r2070-infomolestia/api/$',
            r2070_infomolestia_views.r2070infoMolestiaList.as_view() ),

        url(r'^r2070-infomolestia/api/(?P<pk>[0-9]+)/$',
            r2070_infomolestia_views.r2070infoMolestiaDetail.as_view() ),

url(r'^r2070-infomolestia/listar/(?P<hash>.*)/$', 
        r2070_infomolestia_views.listar, 
        name='r2070_infomolestia'),

url(r'^r2070-infomolestia/salvar/(?P<hash>.*)/$', 
        r2070_infomolestia_views.salvar, 
        name='r2070_infomolestia_salvar'),



url(r'^r2070-infoprocjud/apagar/(?P<hash>.*)/$', 
        r2070_infoprocjud_views.apagar, 
        name='r2070_infoprocjud_apagar'),

url(r'^r2070-infoprocjud/api/$',
            r2070_infoprocjud_views.r2070infoProcJudList.as_view() ),

        url(r'^r2070-infoprocjud/api/(?P<pk>[0-9]+)/$',
            r2070_infoprocjud_views.r2070infoProcJudDetail.as_view() ),

url(r'^r2070-infoprocjud/listar/(?P<hash>.*)/$', 
        r2070_infoprocjud_views.listar, 
        name='r2070_infoprocjud'),

url(r'^r2070-infoprocjud/salvar/(?P<hash>.*)/$', 
        r2070_infoprocjud_views.salvar, 
        name='r2070_infoprocjud_salvar'),



url(r'^r2070-infoprocjud-despprocjud/apagar/(?P<hash>.*)/$', 
        r2070_infoprocjud_despprocjud_views.apagar, 
        name='r2070_infoprocjud_despprocjud_apagar'),

url(r'^r2070-infoprocjud-despprocjud/api/$',
            r2070_infoprocjud_despprocjud_views.r2070infoProcJuddespProcJudList.as_view() ),

        url(r'^r2070-infoprocjud-despprocjud/api/(?P<pk>[0-9]+)/$',
            r2070_infoprocjud_despprocjud_views.r2070infoProcJuddespProcJudDetail.as_view() ),

url(r'^r2070-infoprocjud-despprocjud/listar/(?P<hash>.*)/$', 
        r2070_infoprocjud_despprocjud_views.listar, 
        name='r2070_infoprocjud_despprocjud'),

url(r'^r2070-infoprocjud-despprocjud/salvar/(?P<hash>.*)/$', 
        r2070_infoprocjud_despprocjud_views.salvar, 
        name='r2070_infoprocjud_despprocjud_salvar'),



url(r'^r2070-infoprocjud-ideadvogado/apagar/(?P<hash>.*)/$', 
        r2070_infoprocjud_ideadvogado_views.apagar, 
        name='r2070_infoprocjud_ideadvogado_apagar'),

url(r'^r2070-infoprocjud-ideadvogado/api/$',
            r2070_infoprocjud_ideadvogado_views.r2070infoProcJudideAdvogadoList.as_view() ),

        url(r'^r2070-infoprocjud-ideadvogado/api/(?P<pk>[0-9]+)/$',
            r2070_infoprocjud_ideadvogado_views.r2070infoProcJudideAdvogadoDetail.as_view() ),

url(r'^r2070-infoprocjud-ideadvogado/listar/(?P<hash>.*)/$', 
        r2070_infoprocjud_ideadvogado_views.listar, 
        name='r2070_infoprocjud_ideadvogado'),

url(r'^r2070-infoprocjud-ideadvogado/salvar/(?P<hash>.*)/$', 
        r2070_infoprocjud_ideadvogado_views.salvar, 
        name='r2070_infoprocjud_ideadvogado_salvar'),



url(r'^r2070-infoprocjud-origemrecursos/apagar/(?P<hash>.*)/$', 
        r2070_infoprocjud_origemrecursos_views.apagar, 
        name='r2070_infoprocjud_origemrecursos_apagar'),

url(r'^r2070-infoprocjud-origemrecursos/api/$',
            r2070_infoprocjud_origemrecursos_views.r2070infoProcJudorigemRecursosList.as_view() ),

        url(r'^r2070-infoprocjud-origemrecursos/api/(?P<pk>[0-9]+)/$',
            r2070_infoprocjud_origemrecursos_views.r2070infoProcJudorigemRecursosDetail.as_view() ),

url(r'^r2070-infoprocjud-origemrecursos/listar/(?P<hash>.*)/$', 
        r2070_infoprocjud_origemrecursos_views.listar, 
        name='r2070_infoprocjud_origemrecursos'),

url(r'^r2070-infoprocjud-origemrecursos/salvar/(?P<hash>.*)/$', 
        r2070_infoprocjud_origemrecursos_views.salvar, 
        name='r2070_infoprocjud_origemrecursos_salvar'),



url(r'^r2070-inforra/apagar/(?P<hash>.*)/$', 
        r2070_inforra_views.apagar, 
        name='r2070_inforra_apagar'),

url(r'^r2070-inforra/api/$',
            r2070_inforra_views.r2070infoRRAList.as_view() ),

        url(r'^r2070-inforra/api/(?P<pk>[0-9]+)/$',
            r2070_inforra_views.r2070infoRRADetail.as_view() ),

url(r'^r2070-inforra/listar/(?P<hash>.*)/$', 
        r2070_inforra_views.listar, 
        name='r2070_inforra'),

url(r'^r2070-inforra/salvar/(?P<hash>.*)/$', 
        r2070_inforra_views.salvar, 
        name='r2070_inforra_salvar'),



url(r'^r2070-inforra-despprocjud/apagar/(?P<hash>.*)/$', 
        r2070_inforra_despprocjud_views.apagar, 
        name='r2070_inforra_despprocjud_apagar'),

url(r'^r2070-inforra-despprocjud/api/$',
            r2070_inforra_despprocjud_views.r2070infoRRAdespProcJudList.as_view() ),

        url(r'^r2070-inforra-despprocjud/api/(?P<pk>[0-9]+)/$',
            r2070_inforra_despprocjud_views.r2070infoRRAdespProcJudDetail.as_view() ),

url(r'^r2070-inforra-despprocjud/listar/(?P<hash>.*)/$', 
        r2070_inforra_despprocjud_views.listar, 
        name='r2070_inforra_despprocjud'),

url(r'^r2070-inforra-despprocjud/salvar/(?P<hash>.*)/$', 
        r2070_inforra_despprocjud_views.salvar, 
        name='r2070_inforra_despprocjud_salvar'),



url(r'^r2070-inforra-ideadvogado/apagar/(?P<hash>.*)/$', 
        r2070_inforra_ideadvogado_views.apagar, 
        name='r2070_inforra_ideadvogado_apagar'),

url(r'^r2070-inforra-ideadvogado/api/$',
            r2070_inforra_ideadvogado_views.r2070infoRRAideAdvogadoList.as_view() ),

        url(r'^r2070-inforra-ideadvogado/api/(?P<pk>[0-9]+)/$',
            r2070_inforra_ideadvogado_views.r2070infoRRAideAdvogadoDetail.as_view() ),

url(r'^r2070-inforra-ideadvogado/listar/(?P<hash>.*)/$', 
        r2070_inforra_ideadvogado_views.listar, 
        name='r2070_inforra_ideadvogado'),

url(r'^r2070-inforra-ideadvogado/salvar/(?P<hash>.*)/$', 
        r2070_inforra_ideadvogado_views.salvar, 
        name='r2070_inforra_ideadvogado_salvar'),



url(r'^r2070-inforesidext/apagar/(?P<hash>.*)/$', 
        r2070_inforesidext_views.apagar, 
        name='r2070_inforesidext_apagar'),

url(r'^r2070-inforesidext/api/$',
            r2070_inforesidext_views.r2070infoResidExtList.as_view() ),

        url(r'^r2070-inforesidext/api/(?P<pk>[0-9]+)/$',
            r2070_inforesidext_views.r2070infoResidExtDetail.as_view() ),

url(r'^r2070-inforesidext/listar/(?P<hash>.*)/$', 
        r2070_inforesidext_views.listar, 
        name='r2070_inforesidext'),

url(r'^r2070-inforesidext/salvar/(?P<hash>.*)/$', 
        r2070_inforesidext_views.salvar, 
        name='r2070_inforesidext_salvar'),



url(r'^r2070-pgtopf/apagar/(?P<hash>.*)/$', 
        r2070_pgtopf_views.apagar, 
        name='r2070_pgtopf_apagar'),

url(r'^r2070-pgtopf/api/$',
            r2070_pgtopf_views.r2070pgtoPFList.as_view() ),

        url(r'^r2070-pgtopf/api/(?P<pk>[0-9]+)/$',
            r2070_pgtopf_views.r2070pgtoPFDetail.as_view() ),

url(r'^r2070-pgtopf/listar/(?P<hash>.*)/$', 
        r2070_pgtopf_views.listar, 
        name='r2070_pgtopf'),

url(r'^r2070-pgtopf/salvar/(?P<hash>.*)/$', 
        r2070_pgtopf_views.salvar, 
        name='r2070_pgtopf_salvar'),



url(r'^r2070-pgtopj/apagar/(?P<hash>.*)/$', 
        r2070_pgtopj_views.apagar, 
        name='r2070_pgtopj_apagar'),

url(r'^r2070-pgtopj/api/$',
            r2070_pgtopj_views.r2070pgtoPJList.as_view() ),

        url(r'^r2070-pgtopj/api/(?P<pk>[0-9]+)/$',
            r2070_pgtopj_views.r2070pgtoPJDetail.as_view() ),

url(r'^r2070-pgtopj/listar/(?P<hash>.*)/$', 
        r2070_pgtopj_views.listar, 
        name='r2070_pgtopj'),

url(r'^r2070-pgtopj/salvar/(?P<hash>.*)/$', 
        r2070_pgtopj_views.salvar, 
        name='r2070_pgtopj_salvar'),



url(r'^r2070-pgtopj-despprocjud/apagar/(?P<hash>.*)/$', 
        r2070_pgtopj_despprocjud_views.apagar, 
        name='r2070_pgtopj_despprocjud_apagar'),

url(r'^r2070-pgtopj-despprocjud/api/$',
            r2070_pgtopj_despprocjud_views.r2070pgtoPJdespProcJudList.as_view() ),

        url(r'^r2070-pgtopj-despprocjud/api/(?P<pk>[0-9]+)/$',
            r2070_pgtopj_despprocjud_views.r2070pgtoPJdespProcJudDetail.as_view() ),

url(r'^r2070-pgtopj-despprocjud/listar/(?P<hash>.*)/$', 
        r2070_pgtopj_despprocjud_views.listar, 
        name='r2070_pgtopj_despprocjud'),

url(r'^r2070-pgtopj-despprocjud/salvar/(?P<hash>.*)/$', 
        r2070_pgtopj_despprocjud_views.salvar, 
        name='r2070_pgtopj_despprocjud_salvar'),



url(r'^r2070-pgtopj-ideadvogado/apagar/(?P<hash>.*)/$', 
        r2070_pgtopj_ideadvogado_views.apagar, 
        name='r2070_pgtopj_ideadvogado_apagar'),

url(r'^r2070-pgtopj-ideadvogado/api/$',
            r2070_pgtopj_ideadvogado_views.r2070pgtoPJideAdvogadoList.as_view() ),

        url(r'^r2070-pgtopj-ideadvogado/api/(?P<pk>[0-9]+)/$',
            r2070_pgtopj_ideadvogado_views.r2070pgtoPJideAdvogadoDetail.as_view() ),

url(r'^r2070-pgtopj-ideadvogado/listar/(?P<hash>.*)/$', 
        r2070_pgtopj_ideadvogado_views.listar, 
        name='r2070_pgtopj_ideadvogado'),

url(r'^r2070-pgtopj-ideadvogado/salvar/(?P<hash>.*)/$', 
        r2070_pgtopj_ideadvogado_views.salvar, 
        name='r2070_pgtopj_ideadvogado_salvar'),



url(r'^r2070-pgtopj-infoprocjud/apagar/(?P<hash>.*)/$', 
        r2070_pgtopj_infoprocjud_views.apagar, 
        name='r2070_pgtopj_infoprocjud_apagar'),

url(r'^r2070-pgtopj-infoprocjud/api/$',
            r2070_pgtopj_infoprocjud_views.r2070pgtoPJinfoProcJudList.as_view() ),

        url(r'^r2070-pgtopj-infoprocjud/api/(?P<pk>[0-9]+)/$',
            r2070_pgtopj_infoprocjud_views.r2070pgtoPJinfoProcJudDetail.as_view() ),

url(r'^r2070-pgtopj-infoprocjud/listar/(?P<hash>.*)/$', 
        r2070_pgtopj_infoprocjud_views.listar, 
        name='r2070_pgtopj_infoprocjud'),

url(r'^r2070-pgtopj-infoprocjud/salvar/(?P<hash>.*)/$', 
        r2070_pgtopj_infoprocjud_views.salvar, 
        name='r2070_pgtopj_infoprocjud_salvar'),



url(r'^r2070-pgtopj-origemrecursos/apagar/(?P<hash>.*)/$', 
        r2070_pgtopj_origemrecursos_views.apagar, 
        name='r2070_pgtopj_origemrecursos_apagar'),

url(r'^r2070-pgtopj-origemrecursos/api/$',
            r2070_pgtopj_origemrecursos_views.r2070pgtoPJorigemRecursosList.as_view() ),

        url(r'^r2070-pgtopj-origemrecursos/api/(?P<pk>[0-9]+)/$',
            r2070_pgtopj_origemrecursos_views.r2070pgtoPJorigemRecursosDetail.as_view() ),

url(r'^r2070-pgtopj-origemrecursos/listar/(?P<hash>.*)/$', 
        r2070_pgtopj_origemrecursos_views.listar, 
        name='r2070_pgtopj_origemrecursos'),

url(r'^r2070-pgtopj-origemrecursos/salvar/(?P<hash>.*)/$', 
        r2070_pgtopj_origemrecursos_views.salvar, 
        name='r2070_pgtopj_origemrecursos_salvar'),



url(r'^r2070-pgtoresidext/apagar/(?P<hash>.*)/$', 
        r2070_pgtoresidext_views.apagar, 
        name='r2070_pgtoresidext_apagar'),

url(r'^r2070-pgtoresidext/api/$',
            r2070_pgtoresidext_views.r2070pgtoResidExtList.as_view() ),

        url(r'^r2070-pgtoresidext/api/(?P<pk>[0-9]+)/$',
            r2070_pgtoresidext_views.r2070pgtoResidExtDetail.as_view() ),

url(r'^r2070-pgtoresidext/listar/(?P<hash>.*)/$', 
        r2070_pgtoresidext_views.listar, 
        name='r2070_pgtoresidext'),

url(r'^r2070-pgtoresidext/salvar/(?P<hash>.*)/$', 
        r2070_pgtoresidext_views.salvar, 
        name='r2070_pgtoresidext_salvar'),



url(r'^r2070-rendisento/apagar/(?P<hash>.*)/$', 
        r2070_rendisento_views.apagar, 
        name='r2070_rendisento_apagar'),

url(r'^r2070-rendisento/api/$',
            r2070_rendisento_views.r2070rendIsentoList.as_view() ),

        url(r'^r2070-rendisento/api/(?P<pk>[0-9]+)/$',
            r2070_rendisento_views.r2070rendIsentoDetail.as_view() ),

url(r'^r2070-rendisento/listar/(?P<hash>.*)/$', 
        r2070_rendisento_views.listar, 
        name='r2070_rendisento'),

url(r'^r2070-rendisento/salvar/(?P<hash>.*)/$', 
        r2070_rendisento_views.salvar, 
        name='r2070_rendisento_salvar'),





]