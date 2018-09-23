#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.r2030.views import r2030_recursosrec as r2030_recursosrec_views
from emensageriapro.r2030.views import r2030_inforecurso as r2030_inforecurso_views
from emensageriapro.r2030.views import r2030_infoproc as r2030_infoproc_views



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



url(r'^r2030-recursosrec/apagar/(?P<hash>.*)/$', 
        r2030_recursosrec_views.apagar, 
        name='r2030_recursosrec_apagar'),

url(r'^r2030-recursosrec/listar/(?P<hash>.*)/$', 
        r2030_recursosrec_views.listar, 
        name='r2030_recursosrec'),

url(r'^r2030-recursosrec/salvar/(?P<hash>.*)/$', 
        r2030_recursosrec_views.salvar, 
        name='r2030_recursosrec_salvar'),



url(r'^r2030-inforecurso/apagar/(?P<hash>.*)/$', 
        r2030_inforecurso_views.apagar, 
        name='r2030_inforecurso_apagar'),

url(r'^r2030-inforecurso/listar/(?P<hash>.*)/$', 
        r2030_inforecurso_views.listar, 
        name='r2030_inforecurso'),

url(r'^r2030-inforecurso/salvar/(?P<hash>.*)/$', 
        r2030_inforecurso_views.salvar, 
        name='r2030_inforecurso_salvar'),



url(r'^r2030-infoproc/apagar/(?P<hash>.*)/$', 
        r2030_infoproc_views.apagar, 
        name='r2030_infoproc_apagar'),

url(r'^r2030-infoproc/listar/(?P<hash>.*)/$', 
        r2030_infoproc_views.listar, 
        name='r2030_infoproc'),

url(r'^r2030-infoproc/salvar/(?P<hash>.*)/$', 
        r2030_infoproc_views.salvar, 
        name='r2030_infoproc_salvar'),





]