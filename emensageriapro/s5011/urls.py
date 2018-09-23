#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s5011.views import s5011_infocpseg as s5011_infocpseg_views
from emensageriapro.s5011.views import s5011_infopj as s5011_infopj_views
from emensageriapro.s5011.views import s5011_infoatconc as s5011_infoatconc_views
from emensageriapro.s5011.views import s5011_ideestab as s5011_ideestab_views
from emensageriapro.s5011.views import s5011_infoestab as s5011_infoestab_views
from emensageriapro.s5011.views import s5011_infocomplobra as s5011_infocomplobra_views
from emensageriapro.s5011.views import s5011_idelotacao as s5011_idelotacao_views
from emensageriapro.s5011.views import s5011_infotercsusp as s5011_infotercsusp_views
from emensageriapro.s5011.views import s5011_infoemprparcial as s5011_infoemprparcial_views
from emensageriapro.s5011.views import s5011_dadosopport as s5011_dadosopport_views
from emensageriapro.s5011.views import s5011_basesremun as s5011_basesremun_views
from emensageriapro.s5011.views import s5011_basesavnport as s5011_basesavnport_views
from emensageriapro.s5011.views import s5011_infosubstpatropport as s5011_infosubstpatropport_views
from emensageriapro.s5011.views import s5011_basesaquis as s5011_basesaquis_views
from emensageriapro.s5011.views import s5011_basescomerc as s5011_basescomerc_views
from emensageriapro.s5011.views import s5011_infocrestab as s5011_infocrestab_views
from emensageriapro.s5011.views import s5011_infocrcontrib as s5011_infocrcontrib_views



"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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
        s5011_infocpseg_views.apagar, 
        name='s5011_infocpseg_apagar'),

url(r'^s5011-infocpseg/listar/(?P<hash>.*)/$', 
        s5011_infocpseg_views.listar, 
        name='s5011_infocpseg'),

url(r'^s5011-infocpseg/salvar/(?P<hash>.*)/$', 
        s5011_infocpseg_views.salvar, 
        name='s5011_infocpseg_salvar'),



url(r'^s5011-infopj/apagar/(?P<hash>.*)/$', 
        s5011_infopj_views.apagar, 
        name='s5011_infopj_apagar'),

url(r'^s5011-infopj/listar/(?P<hash>.*)/$', 
        s5011_infopj_views.listar, 
        name='s5011_infopj'),

url(r'^s5011-infopj/salvar/(?P<hash>.*)/$', 
        s5011_infopj_views.salvar, 
        name='s5011_infopj_salvar'),



url(r'^s5011-infoatconc/apagar/(?P<hash>.*)/$', 
        s5011_infoatconc_views.apagar, 
        name='s5011_infoatconc_apagar'),

url(r'^s5011-infoatconc/listar/(?P<hash>.*)/$', 
        s5011_infoatconc_views.listar, 
        name='s5011_infoatconc'),

url(r'^s5011-infoatconc/salvar/(?P<hash>.*)/$', 
        s5011_infoatconc_views.salvar, 
        name='s5011_infoatconc_salvar'),



url(r'^s5011-ideestab/apagar/(?P<hash>.*)/$', 
        s5011_ideestab_views.apagar, 
        name='s5011_ideestab_apagar'),

url(r'^s5011-ideestab/listar/(?P<hash>.*)/$', 
        s5011_ideestab_views.listar, 
        name='s5011_ideestab'),

url(r'^s5011-ideestab/salvar/(?P<hash>.*)/$', 
        s5011_ideestab_views.salvar, 
        name='s5011_ideestab_salvar'),



url(r'^s5011-infoestab/apagar/(?P<hash>.*)/$', 
        s5011_infoestab_views.apagar, 
        name='s5011_infoestab_apagar'),

url(r'^s5011-infoestab/listar/(?P<hash>.*)/$', 
        s5011_infoestab_views.listar, 
        name='s5011_infoestab'),

url(r'^s5011-infoestab/salvar/(?P<hash>.*)/$', 
        s5011_infoestab_views.salvar, 
        name='s5011_infoestab_salvar'),



url(r'^s5011-infocomplobra/apagar/(?P<hash>.*)/$', 
        s5011_infocomplobra_views.apagar, 
        name='s5011_infocomplobra_apagar'),

url(r'^s5011-infocomplobra/listar/(?P<hash>.*)/$', 
        s5011_infocomplobra_views.listar, 
        name='s5011_infocomplobra'),

url(r'^s5011-infocomplobra/salvar/(?P<hash>.*)/$', 
        s5011_infocomplobra_views.salvar, 
        name='s5011_infocomplobra_salvar'),



url(r'^s5011-idelotacao/apagar/(?P<hash>.*)/$', 
        s5011_idelotacao_views.apagar, 
        name='s5011_idelotacao_apagar'),

url(r'^s5011-idelotacao/listar/(?P<hash>.*)/$', 
        s5011_idelotacao_views.listar, 
        name='s5011_idelotacao'),

url(r'^s5011-idelotacao/salvar/(?P<hash>.*)/$', 
        s5011_idelotacao_views.salvar, 
        name='s5011_idelotacao_salvar'),



url(r'^s5011-infotercsusp/apagar/(?P<hash>.*)/$', 
        s5011_infotercsusp_views.apagar, 
        name='s5011_infotercsusp_apagar'),

url(r'^s5011-infotercsusp/listar/(?P<hash>.*)/$', 
        s5011_infotercsusp_views.listar, 
        name='s5011_infotercsusp'),

url(r'^s5011-infotercsusp/salvar/(?P<hash>.*)/$', 
        s5011_infotercsusp_views.salvar, 
        name='s5011_infotercsusp_salvar'),



url(r'^s5011-infoemprparcial/apagar/(?P<hash>.*)/$', 
        s5011_infoemprparcial_views.apagar, 
        name='s5011_infoemprparcial_apagar'),

url(r'^s5011-infoemprparcial/listar/(?P<hash>.*)/$', 
        s5011_infoemprparcial_views.listar, 
        name='s5011_infoemprparcial'),

url(r'^s5011-infoemprparcial/salvar/(?P<hash>.*)/$', 
        s5011_infoemprparcial_views.salvar, 
        name='s5011_infoemprparcial_salvar'),



url(r'^s5011-dadosopport/apagar/(?P<hash>.*)/$', 
        s5011_dadosopport_views.apagar, 
        name='s5011_dadosopport_apagar'),

url(r'^s5011-dadosopport/listar/(?P<hash>.*)/$', 
        s5011_dadosopport_views.listar, 
        name='s5011_dadosopport'),

url(r'^s5011-dadosopport/salvar/(?P<hash>.*)/$', 
        s5011_dadosopport_views.salvar, 
        name='s5011_dadosopport_salvar'),



url(r'^s5011-basesremun/apagar/(?P<hash>.*)/$', 
        s5011_basesremun_views.apagar, 
        name='s5011_basesremun_apagar'),

url(r'^s5011-basesremun/listar/(?P<hash>.*)/$', 
        s5011_basesremun_views.listar, 
        name='s5011_basesremun'),

url(r'^s5011-basesremun/salvar/(?P<hash>.*)/$', 
        s5011_basesremun_views.salvar, 
        name='s5011_basesremun_salvar'),



url(r'^s5011-basesavnport/apagar/(?P<hash>.*)/$', 
        s5011_basesavnport_views.apagar, 
        name='s5011_basesavnport_apagar'),

url(r'^s5011-basesavnport/listar/(?P<hash>.*)/$', 
        s5011_basesavnport_views.listar, 
        name='s5011_basesavnport'),

url(r'^s5011-basesavnport/salvar/(?P<hash>.*)/$', 
        s5011_basesavnport_views.salvar, 
        name='s5011_basesavnport_salvar'),



url(r'^s5011-infosubstpatropport/apagar/(?P<hash>.*)/$', 
        s5011_infosubstpatropport_views.apagar, 
        name='s5011_infosubstpatropport_apagar'),

url(r'^s5011-infosubstpatropport/listar/(?P<hash>.*)/$', 
        s5011_infosubstpatropport_views.listar, 
        name='s5011_infosubstpatropport'),

url(r'^s5011-infosubstpatropport/salvar/(?P<hash>.*)/$', 
        s5011_infosubstpatropport_views.salvar, 
        name='s5011_infosubstpatropport_salvar'),



url(r'^s5011-basesaquis/apagar/(?P<hash>.*)/$', 
        s5011_basesaquis_views.apagar, 
        name='s5011_basesaquis_apagar'),

url(r'^s5011-basesaquis/listar/(?P<hash>.*)/$', 
        s5011_basesaquis_views.listar, 
        name='s5011_basesaquis'),

url(r'^s5011-basesaquis/salvar/(?P<hash>.*)/$', 
        s5011_basesaquis_views.salvar, 
        name='s5011_basesaquis_salvar'),



url(r'^s5011-basescomerc/apagar/(?P<hash>.*)/$', 
        s5011_basescomerc_views.apagar, 
        name='s5011_basescomerc_apagar'),

url(r'^s5011-basescomerc/listar/(?P<hash>.*)/$', 
        s5011_basescomerc_views.listar, 
        name='s5011_basescomerc'),

url(r'^s5011-basescomerc/salvar/(?P<hash>.*)/$', 
        s5011_basescomerc_views.salvar, 
        name='s5011_basescomerc_salvar'),



url(r'^s5011-infocrestab/apagar/(?P<hash>.*)/$', 
        s5011_infocrestab_views.apagar, 
        name='s5011_infocrestab_apagar'),

url(r'^s5011-infocrestab/listar/(?P<hash>.*)/$', 
        s5011_infocrestab_views.listar, 
        name='s5011_infocrestab'),

url(r'^s5011-infocrestab/salvar/(?P<hash>.*)/$', 
        s5011_infocrestab_views.salvar, 
        name='s5011_infocrestab_salvar'),



url(r'^s5011-infocrcontrib/apagar/(?P<hash>.*)/$', 
        s5011_infocrcontrib_views.apagar, 
        name='s5011_infocrcontrib_apagar'),

url(r'^s5011-infocrcontrib/listar/(?P<hash>.*)/$', 
        s5011_infocrcontrib_views.listar, 
        name='s5011_infocrcontrib'),

url(r'^s5011-infocrcontrib/salvar/(?P<hash>.*)/$', 
        s5011_infocrcontrib_views.salvar, 
        name='s5011_infocrcontrib_salvar'),





]