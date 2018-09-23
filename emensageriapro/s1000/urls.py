#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1000.views import s1000_inclusao as s1000_inclusao_views
from emensageriapro.s1000.views import s1000_inclusao_dadosisencao as s1000_inclusao_dadosisencao_views
from emensageriapro.s1000.views import s1000_inclusao_infoop as s1000_inclusao_infoop_views
from emensageriapro.s1000.views import s1000_inclusao_infoefr as s1000_inclusao_infoefr_views
from emensageriapro.s1000.views import s1000_inclusao_infoente as s1000_inclusao_infoente_views
from emensageriapro.s1000.views import s1000_inclusao_infoorginternacional as s1000_inclusao_infoorginternacional_views
from emensageriapro.s1000.views import s1000_inclusao_softwarehouse as s1000_inclusao_softwarehouse_views
from emensageriapro.s1000.views import s1000_inclusao_situacaopj as s1000_inclusao_situacaopj_views
from emensageriapro.s1000.views import s1000_inclusao_situacaopf as s1000_inclusao_situacaopf_views
from emensageriapro.s1000.views import s1000_alteracao as s1000_alteracao_views
from emensageriapro.s1000.views import s1000_alteracao_dadosisencao as s1000_alteracao_dadosisencao_views
from emensageriapro.s1000.views import s1000_alteracao_infoop as s1000_alteracao_infoop_views
from emensageriapro.s1000.views import s1000_alteracao_infoefr as s1000_alteracao_infoefr_views
from emensageriapro.s1000.views import s1000_alteracao_infoente as s1000_alteracao_infoente_views
from emensageriapro.s1000.views import s1000_alteracao_infoorginternacional as s1000_alteracao_infoorginternacional_views
from emensageriapro.s1000.views import s1000_alteracao_softwarehouse as s1000_alteracao_softwarehouse_views
from emensageriapro.s1000.views import s1000_alteracao_situacaopj as s1000_alteracao_situacaopj_views
from emensageriapro.s1000.views import s1000_alteracao_situacaopf as s1000_alteracao_situacaopf_views
from emensageriapro.s1000.views import s1000_alteracao_novavalidade as s1000_alteracao_novavalidade_views
from emensageriapro.s1000.views import s1000_exclusao as s1000_exclusao_views



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



url(r'^s1000-inclusao/apagar/(?P<hash>.*)/$', 
        s1000_inclusao_views.apagar, 
        name='s1000_inclusao_apagar'),

url(r'^s1000-inclusao/listar/(?P<hash>.*)/$', 
        s1000_inclusao_views.listar, 
        name='s1000_inclusao'),

url(r'^s1000-inclusao/salvar/(?P<hash>.*)/$', 
        s1000_inclusao_views.salvar, 
        name='s1000_inclusao_salvar'),



url(r'^s1000-inclusao-dadosisencao/apagar/(?P<hash>.*)/$', 
        s1000_inclusao_dadosisencao_views.apagar, 
        name='s1000_inclusao_dadosisencao_apagar'),

url(r'^s1000-inclusao-dadosisencao/listar/(?P<hash>.*)/$', 
        s1000_inclusao_dadosisencao_views.listar, 
        name='s1000_inclusao_dadosisencao'),

url(r'^s1000-inclusao-dadosisencao/salvar/(?P<hash>.*)/$', 
        s1000_inclusao_dadosisencao_views.salvar, 
        name='s1000_inclusao_dadosisencao_salvar'),



url(r'^s1000-inclusao-infoop/apagar/(?P<hash>.*)/$', 
        s1000_inclusao_infoop_views.apagar, 
        name='s1000_inclusao_infoop_apagar'),

url(r'^s1000-inclusao-infoop/listar/(?P<hash>.*)/$', 
        s1000_inclusao_infoop_views.listar, 
        name='s1000_inclusao_infoop'),

url(r'^s1000-inclusao-infoop/salvar/(?P<hash>.*)/$', 
        s1000_inclusao_infoop_views.salvar, 
        name='s1000_inclusao_infoop_salvar'),



url(r'^s1000-inclusao-infoefr/apagar/(?P<hash>.*)/$', 
        s1000_inclusao_infoefr_views.apagar, 
        name='s1000_inclusao_infoefr_apagar'),

url(r'^s1000-inclusao-infoefr/listar/(?P<hash>.*)/$', 
        s1000_inclusao_infoefr_views.listar, 
        name='s1000_inclusao_infoefr'),

url(r'^s1000-inclusao-infoefr/salvar/(?P<hash>.*)/$', 
        s1000_inclusao_infoefr_views.salvar, 
        name='s1000_inclusao_infoefr_salvar'),



url(r'^s1000-inclusao-infoente/apagar/(?P<hash>.*)/$', 
        s1000_inclusao_infoente_views.apagar, 
        name='s1000_inclusao_infoente_apagar'),

url(r'^s1000-inclusao-infoente/listar/(?P<hash>.*)/$', 
        s1000_inclusao_infoente_views.listar, 
        name='s1000_inclusao_infoente'),

url(r'^s1000-inclusao-infoente/salvar/(?P<hash>.*)/$', 
        s1000_inclusao_infoente_views.salvar, 
        name='s1000_inclusao_infoente_salvar'),



url(r'^s1000-inclusao-infoorginternacional/apagar/(?P<hash>.*)/$', 
        s1000_inclusao_infoorginternacional_views.apagar, 
        name='s1000_inclusao_infoorginternacional_apagar'),

url(r'^s1000-inclusao-infoorginternacional/listar/(?P<hash>.*)/$', 
        s1000_inclusao_infoorginternacional_views.listar, 
        name='s1000_inclusao_infoorginternacional'),

url(r'^s1000-inclusao-infoorginternacional/salvar/(?P<hash>.*)/$', 
        s1000_inclusao_infoorginternacional_views.salvar, 
        name='s1000_inclusao_infoorginternacional_salvar'),



url(r'^s1000-inclusao-softwarehouse/apagar/(?P<hash>.*)/$', 
        s1000_inclusao_softwarehouse_views.apagar, 
        name='s1000_inclusao_softwarehouse_apagar'),

url(r'^s1000-inclusao-softwarehouse/listar/(?P<hash>.*)/$', 
        s1000_inclusao_softwarehouse_views.listar, 
        name='s1000_inclusao_softwarehouse'),

url(r'^s1000-inclusao-softwarehouse/salvar/(?P<hash>.*)/$', 
        s1000_inclusao_softwarehouse_views.salvar, 
        name='s1000_inclusao_softwarehouse_salvar'),



url(r'^s1000-inclusao-situacaopj/apagar/(?P<hash>.*)/$', 
        s1000_inclusao_situacaopj_views.apagar, 
        name='s1000_inclusao_situacaopj_apagar'),

url(r'^s1000-inclusao-situacaopj/listar/(?P<hash>.*)/$', 
        s1000_inclusao_situacaopj_views.listar, 
        name='s1000_inclusao_situacaopj'),

url(r'^s1000-inclusao-situacaopj/salvar/(?P<hash>.*)/$', 
        s1000_inclusao_situacaopj_views.salvar, 
        name='s1000_inclusao_situacaopj_salvar'),



url(r'^s1000-inclusao-situacaopf/apagar/(?P<hash>.*)/$', 
        s1000_inclusao_situacaopf_views.apagar, 
        name='s1000_inclusao_situacaopf_apagar'),

url(r'^s1000-inclusao-situacaopf/listar/(?P<hash>.*)/$', 
        s1000_inclusao_situacaopf_views.listar, 
        name='s1000_inclusao_situacaopf'),

url(r'^s1000-inclusao-situacaopf/salvar/(?P<hash>.*)/$', 
        s1000_inclusao_situacaopf_views.salvar, 
        name='s1000_inclusao_situacaopf_salvar'),



url(r'^s1000-alteracao/apagar/(?P<hash>.*)/$', 
        s1000_alteracao_views.apagar, 
        name='s1000_alteracao_apagar'),

url(r'^s1000-alteracao/listar/(?P<hash>.*)/$', 
        s1000_alteracao_views.listar, 
        name='s1000_alteracao'),

url(r'^s1000-alteracao/salvar/(?P<hash>.*)/$', 
        s1000_alteracao_views.salvar, 
        name='s1000_alteracao_salvar'),



url(r'^s1000-alteracao-dadosisencao/apagar/(?P<hash>.*)/$', 
        s1000_alteracao_dadosisencao_views.apagar, 
        name='s1000_alteracao_dadosisencao_apagar'),

url(r'^s1000-alteracao-dadosisencao/listar/(?P<hash>.*)/$', 
        s1000_alteracao_dadosisencao_views.listar, 
        name='s1000_alteracao_dadosisencao'),

url(r'^s1000-alteracao-dadosisencao/salvar/(?P<hash>.*)/$', 
        s1000_alteracao_dadosisencao_views.salvar, 
        name='s1000_alteracao_dadosisencao_salvar'),



url(r'^s1000-alteracao-infoop/apagar/(?P<hash>.*)/$', 
        s1000_alteracao_infoop_views.apagar, 
        name='s1000_alteracao_infoop_apagar'),

url(r'^s1000-alteracao-infoop/listar/(?P<hash>.*)/$', 
        s1000_alteracao_infoop_views.listar, 
        name='s1000_alteracao_infoop'),

url(r'^s1000-alteracao-infoop/salvar/(?P<hash>.*)/$', 
        s1000_alteracao_infoop_views.salvar, 
        name='s1000_alteracao_infoop_salvar'),



url(r'^s1000-alteracao-infoefr/apagar/(?P<hash>.*)/$', 
        s1000_alteracao_infoefr_views.apagar, 
        name='s1000_alteracao_infoefr_apagar'),

url(r'^s1000-alteracao-infoefr/listar/(?P<hash>.*)/$', 
        s1000_alteracao_infoefr_views.listar, 
        name='s1000_alteracao_infoefr'),

url(r'^s1000-alteracao-infoefr/salvar/(?P<hash>.*)/$', 
        s1000_alteracao_infoefr_views.salvar, 
        name='s1000_alteracao_infoefr_salvar'),



url(r'^s1000-alteracao-infoente/apagar/(?P<hash>.*)/$', 
        s1000_alteracao_infoente_views.apagar, 
        name='s1000_alteracao_infoente_apagar'),

url(r'^s1000-alteracao-infoente/listar/(?P<hash>.*)/$', 
        s1000_alteracao_infoente_views.listar, 
        name='s1000_alteracao_infoente'),

url(r'^s1000-alteracao-infoente/salvar/(?P<hash>.*)/$', 
        s1000_alteracao_infoente_views.salvar, 
        name='s1000_alteracao_infoente_salvar'),



url(r'^s1000-alteracao-infoorginternacional/apagar/(?P<hash>.*)/$', 
        s1000_alteracao_infoorginternacional_views.apagar, 
        name='s1000_alteracao_infoorginternacional_apagar'),

url(r'^s1000-alteracao-infoorginternacional/listar/(?P<hash>.*)/$', 
        s1000_alteracao_infoorginternacional_views.listar, 
        name='s1000_alteracao_infoorginternacional'),

url(r'^s1000-alteracao-infoorginternacional/salvar/(?P<hash>.*)/$', 
        s1000_alteracao_infoorginternacional_views.salvar, 
        name='s1000_alteracao_infoorginternacional_salvar'),



url(r'^s1000-alteracao-softwarehouse/apagar/(?P<hash>.*)/$', 
        s1000_alteracao_softwarehouse_views.apagar, 
        name='s1000_alteracao_softwarehouse_apagar'),

url(r'^s1000-alteracao-softwarehouse/listar/(?P<hash>.*)/$', 
        s1000_alteracao_softwarehouse_views.listar, 
        name='s1000_alteracao_softwarehouse'),

url(r'^s1000-alteracao-softwarehouse/salvar/(?P<hash>.*)/$', 
        s1000_alteracao_softwarehouse_views.salvar, 
        name='s1000_alteracao_softwarehouse_salvar'),



url(r'^s1000-alteracao-situacaopj/apagar/(?P<hash>.*)/$', 
        s1000_alteracao_situacaopj_views.apagar, 
        name='s1000_alteracao_situacaopj_apagar'),

url(r'^s1000-alteracao-situacaopj/listar/(?P<hash>.*)/$', 
        s1000_alteracao_situacaopj_views.listar, 
        name='s1000_alteracao_situacaopj'),

url(r'^s1000-alteracao-situacaopj/salvar/(?P<hash>.*)/$', 
        s1000_alteracao_situacaopj_views.salvar, 
        name='s1000_alteracao_situacaopj_salvar'),



url(r'^s1000-alteracao-situacaopf/apagar/(?P<hash>.*)/$', 
        s1000_alteracao_situacaopf_views.apagar, 
        name='s1000_alteracao_situacaopf_apagar'),

url(r'^s1000-alteracao-situacaopf/listar/(?P<hash>.*)/$', 
        s1000_alteracao_situacaopf_views.listar, 
        name='s1000_alteracao_situacaopf'),

url(r'^s1000-alteracao-situacaopf/salvar/(?P<hash>.*)/$', 
        s1000_alteracao_situacaopf_views.salvar, 
        name='s1000_alteracao_situacaopf_salvar'),



url(r'^s1000-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        s1000_alteracao_novavalidade_views.apagar, 
        name='s1000_alteracao_novavalidade_apagar'),

url(r'^s1000-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        s1000_alteracao_novavalidade_views.listar, 
        name='s1000_alteracao_novavalidade'),

url(r'^s1000-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        s1000_alteracao_novavalidade_views.salvar, 
        name='s1000_alteracao_novavalidade_salvar'),



url(r'^s1000-exclusao/apagar/(?P<hash>.*)/$', 
        s1000_exclusao_views.apagar, 
        name='s1000_exclusao_apagar'),

url(r'^s1000-exclusao/listar/(?P<hash>.*)/$', 
        s1000_exclusao_views.listar, 
        name='s1000_exclusao'),

url(r'^s1000-exclusao/salvar/(?P<hash>.*)/$', 
        s1000_exclusao_views.salvar, 
        name='s1000_exclusao_salvar'),





]