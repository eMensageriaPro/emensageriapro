#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2206.views import s2206_infoceletista as s2206_infoceletista_views
from emensageriapro.s2206.views import s2206_trabtemp as s2206_trabtemp_views
from emensageriapro.s2206.views import s2206_aprend as s2206_aprend_views
from emensageriapro.s2206.views import s2206_infoestatutario as s2206_infoestatutario_views
from emensageriapro.s2206.views import s2206_localtrabgeral as s2206_localtrabgeral_views
from emensageriapro.s2206.views import s2206_localtrabdom as s2206_localtrabdom_views
from emensageriapro.s2206.views import s2206_horcontratual as s2206_horcontratual_views
from emensageriapro.s2206.views import s2206_horario as s2206_horario_views
from emensageriapro.s2206.views import s2206_filiacaosindical as s2206_filiacaosindical_views
from emensageriapro.s2206.views import s2206_alvarajudicial as s2206_alvarajudicial_views
from emensageriapro.s2206.views import s2206_observacoes as s2206_observacoes_views
from emensageriapro.s2206.views import s2206_servpubl as s2206_servpubl_views



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



url(r'^s2206-infoceletista/apagar/(?P<hash>.*)/$', 
        s2206_infoceletista_views.apagar, 
        name='s2206_infoceletista_apagar'),

url(r'^s2206-infoceletista/listar/(?P<hash>.*)/$', 
        s2206_infoceletista_views.listar, 
        name='s2206_infoceletista'),

url(r'^s2206-infoceletista/salvar/(?P<hash>.*)/$', 
        s2206_infoceletista_views.salvar, 
        name='s2206_infoceletista_salvar'),



url(r'^s2206-trabtemp/apagar/(?P<hash>.*)/$', 
        s2206_trabtemp_views.apagar, 
        name='s2206_trabtemp_apagar'),

url(r'^s2206-trabtemp/listar/(?P<hash>.*)/$', 
        s2206_trabtemp_views.listar, 
        name='s2206_trabtemp'),

url(r'^s2206-trabtemp/salvar/(?P<hash>.*)/$', 
        s2206_trabtemp_views.salvar, 
        name='s2206_trabtemp_salvar'),



url(r'^s2206-aprend/apagar/(?P<hash>.*)/$', 
        s2206_aprend_views.apagar, 
        name='s2206_aprend_apagar'),

url(r'^s2206-aprend/listar/(?P<hash>.*)/$', 
        s2206_aprend_views.listar, 
        name='s2206_aprend'),

url(r'^s2206-aprend/salvar/(?P<hash>.*)/$', 
        s2206_aprend_views.salvar, 
        name='s2206_aprend_salvar'),



url(r'^s2206-infoestatutario/apagar/(?P<hash>.*)/$', 
        s2206_infoestatutario_views.apagar, 
        name='s2206_infoestatutario_apagar'),

url(r'^s2206-infoestatutario/listar/(?P<hash>.*)/$', 
        s2206_infoestatutario_views.listar, 
        name='s2206_infoestatutario'),

url(r'^s2206-infoestatutario/salvar/(?P<hash>.*)/$', 
        s2206_infoestatutario_views.salvar, 
        name='s2206_infoestatutario_salvar'),



url(r'^s2206-localtrabgeral/apagar/(?P<hash>.*)/$', 
        s2206_localtrabgeral_views.apagar, 
        name='s2206_localtrabgeral_apagar'),

url(r'^s2206-localtrabgeral/listar/(?P<hash>.*)/$', 
        s2206_localtrabgeral_views.listar, 
        name='s2206_localtrabgeral'),

url(r'^s2206-localtrabgeral/salvar/(?P<hash>.*)/$', 
        s2206_localtrabgeral_views.salvar, 
        name='s2206_localtrabgeral_salvar'),



url(r'^s2206-localtrabdom/apagar/(?P<hash>.*)/$', 
        s2206_localtrabdom_views.apagar, 
        name='s2206_localtrabdom_apagar'),

url(r'^s2206-localtrabdom/listar/(?P<hash>.*)/$', 
        s2206_localtrabdom_views.listar, 
        name='s2206_localtrabdom'),

url(r'^s2206-localtrabdom/salvar/(?P<hash>.*)/$', 
        s2206_localtrabdom_views.salvar, 
        name='s2206_localtrabdom_salvar'),



url(r'^s2206-horcontratual/apagar/(?P<hash>.*)/$', 
        s2206_horcontratual_views.apagar, 
        name='s2206_horcontratual_apagar'),

url(r'^s2206-horcontratual/listar/(?P<hash>.*)/$', 
        s2206_horcontratual_views.listar, 
        name='s2206_horcontratual'),

url(r'^s2206-horcontratual/salvar/(?P<hash>.*)/$', 
        s2206_horcontratual_views.salvar, 
        name='s2206_horcontratual_salvar'),



url(r'^s2206-horario/apagar/(?P<hash>.*)/$', 
        s2206_horario_views.apagar, 
        name='s2206_horario_apagar'),

url(r'^s2206-horario/listar/(?P<hash>.*)/$', 
        s2206_horario_views.listar, 
        name='s2206_horario'),

url(r'^s2206-horario/salvar/(?P<hash>.*)/$', 
        s2206_horario_views.salvar, 
        name='s2206_horario_salvar'),



url(r'^s2206-filiacaosindical/apagar/(?P<hash>.*)/$', 
        s2206_filiacaosindical_views.apagar, 
        name='s2206_filiacaosindical_apagar'),

url(r'^s2206-filiacaosindical/listar/(?P<hash>.*)/$', 
        s2206_filiacaosindical_views.listar, 
        name='s2206_filiacaosindical'),

url(r'^s2206-filiacaosindical/salvar/(?P<hash>.*)/$', 
        s2206_filiacaosindical_views.salvar, 
        name='s2206_filiacaosindical_salvar'),



url(r'^s2206-alvarajudicial/apagar/(?P<hash>.*)/$', 
        s2206_alvarajudicial_views.apagar, 
        name='s2206_alvarajudicial_apagar'),

url(r'^s2206-alvarajudicial/listar/(?P<hash>.*)/$', 
        s2206_alvarajudicial_views.listar, 
        name='s2206_alvarajudicial'),

url(r'^s2206-alvarajudicial/salvar/(?P<hash>.*)/$', 
        s2206_alvarajudicial_views.salvar, 
        name='s2206_alvarajudicial_salvar'),



url(r'^s2206-observacoes/apagar/(?P<hash>.*)/$', 
        s2206_observacoes_views.apagar, 
        name='s2206_observacoes_apagar'),

url(r'^s2206-observacoes/listar/(?P<hash>.*)/$', 
        s2206_observacoes_views.listar, 
        name='s2206_observacoes'),

url(r'^s2206-observacoes/salvar/(?P<hash>.*)/$', 
        s2206_observacoes_views.salvar, 
        name='s2206_observacoes_salvar'),



url(r'^s2206-servpubl/apagar/(?P<hash>.*)/$', 
        s2206_servpubl_views.apagar, 
        name='s2206_servpubl_apagar'),

url(r'^s2206-servpubl/listar/(?P<hash>.*)/$', 
        s2206_servpubl_views.listar, 
        name='s2206_servpubl'),

url(r'^s2206-servpubl/salvar/(?P<hash>.*)/$', 
        s2206_servpubl_views.salvar, 
        name='s2206_servpubl_salvar'),





]