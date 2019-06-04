#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s2206.views import s2206_infoceletista_apagar as s2206_infoceletista_apagar_views
from emensageriapro.s2206.views import s2206_infoceletista_listar as s2206_infoceletista_listar_views
from emensageriapro.s2206.views import s2206_infoceletista_salvar as s2206_infoceletista_salvar_views
from emensageriapro.s2206.views import s2206_infoceletista_api as s2206_infoceletista_api_views
from emensageriapro.s2206.views import s2206_trabtemp_apagar as s2206_trabtemp_apagar_views
from emensageriapro.s2206.views import s2206_trabtemp_listar as s2206_trabtemp_listar_views
from emensageriapro.s2206.views import s2206_trabtemp_salvar as s2206_trabtemp_salvar_views
from emensageriapro.s2206.views import s2206_trabtemp_api as s2206_trabtemp_api_views
from emensageriapro.s2206.views import s2206_aprend_apagar as s2206_aprend_apagar_views
from emensageriapro.s2206.views import s2206_aprend_listar as s2206_aprend_listar_views
from emensageriapro.s2206.views import s2206_aprend_salvar as s2206_aprend_salvar_views
from emensageriapro.s2206.views import s2206_aprend_api as s2206_aprend_api_views
from emensageriapro.s2206.views import s2206_infoestatutario_apagar as s2206_infoestatutario_apagar_views
from emensageriapro.s2206.views import s2206_infoestatutario_listar as s2206_infoestatutario_listar_views
from emensageriapro.s2206.views import s2206_infoestatutario_salvar as s2206_infoestatutario_salvar_views
from emensageriapro.s2206.views import s2206_infoestatutario_api as s2206_infoestatutario_api_views
from emensageriapro.s2206.views import s2206_localtrabgeral_apagar as s2206_localtrabgeral_apagar_views
from emensageriapro.s2206.views import s2206_localtrabgeral_listar as s2206_localtrabgeral_listar_views
from emensageriapro.s2206.views import s2206_localtrabgeral_salvar as s2206_localtrabgeral_salvar_views
from emensageriapro.s2206.views import s2206_localtrabgeral_api as s2206_localtrabgeral_api_views
from emensageriapro.s2206.views import s2206_localtrabdom_apagar as s2206_localtrabdom_apagar_views
from emensageriapro.s2206.views import s2206_localtrabdom_listar as s2206_localtrabdom_listar_views
from emensageriapro.s2206.views import s2206_localtrabdom_salvar as s2206_localtrabdom_salvar_views
from emensageriapro.s2206.views import s2206_localtrabdom_api as s2206_localtrabdom_api_views
from emensageriapro.s2206.views import s2206_horcontratual_apagar as s2206_horcontratual_apagar_views
from emensageriapro.s2206.views import s2206_horcontratual_listar as s2206_horcontratual_listar_views
from emensageriapro.s2206.views import s2206_horcontratual_salvar as s2206_horcontratual_salvar_views
from emensageriapro.s2206.views import s2206_horcontratual_api as s2206_horcontratual_api_views
from emensageriapro.s2206.views import s2206_horario_apagar as s2206_horario_apagar_views
from emensageriapro.s2206.views import s2206_horario_listar as s2206_horario_listar_views
from emensageriapro.s2206.views import s2206_horario_salvar as s2206_horario_salvar_views
from emensageriapro.s2206.views import s2206_horario_api as s2206_horario_api_views
from emensageriapro.s2206.views import s2206_filiacaosindical_apagar as s2206_filiacaosindical_apagar_views
from emensageriapro.s2206.views import s2206_filiacaosindical_listar as s2206_filiacaosindical_listar_views
from emensageriapro.s2206.views import s2206_filiacaosindical_salvar as s2206_filiacaosindical_salvar_views
from emensageriapro.s2206.views import s2206_filiacaosindical_api as s2206_filiacaosindical_api_views
from emensageriapro.s2206.views import s2206_alvarajudicial_apagar as s2206_alvarajudicial_apagar_views
from emensageriapro.s2206.views import s2206_alvarajudicial_listar as s2206_alvarajudicial_listar_views
from emensageriapro.s2206.views import s2206_alvarajudicial_salvar as s2206_alvarajudicial_salvar_views
from emensageriapro.s2206.views import s2206_alvarajudicial_api as s2206_alvarajudicial_api_views
from emensageriapro.s2206.views import s2206_observacoes_apagar as s2206_observacoes_apagar_views
from emensageriapro.s2206.views import s2206_observacoes_listar as s2206_observacoes_listar_views
from emensageriapro.s2206.views import s2206_observacoes_salvar as s2206_observacoes_salvar_views
from emensageriapro.s2206.views import s2206_observacoes_api as s2206_observacoes_api_views
from emensageriapro.s2206.views import s2206_servpubl_apagar as s2206_servpubl_apagar_views
from emensageriapro.s2206.views import s2206_servpubl_listar as s2206_servpubl_listar_views
from emensageriapro.s2206.views import s2206_servpubl_salvar as s2206_servpubl_salvar_views
from emensageriapro.s2206.views import s2206_servpubl_api as s2206_servpubl_api_views



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


    url(r'^s2206-infoceletista/apagar/(?P<pk>[0-9]+)/$', 
        s2206_infoceletista_apagar_views.apagar, 
        name='s2206_infoceletista_apagar'),

    url(r'^s2206-infoceletista/api/$',
        s2206_infoceletista_api_views.s2206infoCeletistaList.as_view() ),

    url(r'^s2206-infoceletista/api/(?P<pk>[0-9]+)/$',
        s2206_infoceletista_api_views.s2206infoCeletistaDetail.as_view() ),

    url(r'^s2206-infoceletista/$', 
        s2206_infoceletista_listar_views.listar, 
        name='s2206_infoceletista'),

    url(r'^s2206-infoceletista/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2206_infoceletista_salvar_views.salvar, 
        name='s2206_infoceletista_salvar'),
        
    url(r'^s2206-infoceletista/cadastrar/$', 
        s2206_infoceletista_salvar_views.salvar, 
        name='s2206_infoceletista_cadastrar'),

    url(r'^s2206-infoceletista/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2206_infoceletista_salvar_views.salvar, 
        name='s2206_infoceletista_salvar_output'),
        
    url(r'^s2206-infoceletista/(?P<output>[\w-]+)/$', 
        s2206_infoceletista_listar_views.listar, 
        name='s2206_infoceletista_output'),

    url(r'^s2206-trabtemp/apagar/(?P<pk>[0-9]+)/$', 
        s2206_trabtemp_apagar_views.apagar, 
        name='s2206_trabtemp_apagar'),

    url(r'^s2206-trabtemp/api/$',
        s2206_trabtemp_api_views.s2206trabTempList.as_view() ),

    url(r'^s2206-trabtemp/api/(?P<pk>[0-9]+)/$',
        s2206_trabtemp_api_views.s2206trabTempDetail.as_view() ),

    url(r'^s2206-trabtemp/$', 
        s2206_trabtemp_listar_views.listar, 
        name='s2206_trabtemp'),

    url(r'^s2206-trabtemp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2206_trabtemp_salvar_views.salvar, 
        name='s2206_trabtemp_salvar'),
        
    url(r'^s2206-trabtemp/cadastrar/$', 
        s2206_trabtemp_salvar_views.salvar, 
        name='s2206_trabtemp_cadastrar'),

    url(r'^s2206-trabtemp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2206_trabtemp_salvar_views.salvar, 
        name='s2206_trabtemp_salvar_output'),
        
    url(r'^s2206-trabtemp/(?P<output>[\w-]+)/$', 
        s2206_trabtemp_listar_views.listar, 
        name='s2206_trabtemp_output'),

    url(r'^s2206-aprend/apagar/(?P<pk>[0-9]+)/$', 
        s2206_aprend_apagar_views.apagar, 
        name='s2206_aprend_apagar'),

    url(r'^s2206-aprend/api/$',
        s2206_aprend_api_views.s2206aprendList.as_view() ),

    url(r'^s2206-aprend/api/(?P<pk>[0-9]+)/$',
        s2206_aprend_api_views.s2206aprendDetail.as_view() ),

    url(r'^s2206-aprend/$', 
        s2206_aprend_listar_views.listar, 
        name='s2206_aprend'),

    url(r'^s2206-aprend/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2206_aprend_salvar_views.salvar, 
        name='s2206_aprend_salvar'),
        
    url(r'^s2206-aprend/cadastrar/$', 
        s2206_aprend_salvar_views.salvar, 
        name='s2206_aprend_cadastrar'),

    url(r'^s2206-aprend/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2206_aprend_salvar_views.salvar, 
        name='s2206_aprend_salvar_output'),
        
    url(r'^s2206-aprend/(?P<output>[\w-]+)/$', 
        s2206_aprend_listar_views.listar, 
        name='s2206_aprend_output'),

    url(r'^s2206-infoestatutario/apagar/(?P<pk>[0-9]+)/$', 
        s2206_infoestatutario_apagar_views.apagar, 
        name='s2206_infoestatutario_apagar'),

    url(r'^s2206-infoestatutario/api/$',
        s2206_infoestatutario_api_views.s2206infoEstatutarioList.as_view() ),

    url(r'^s2206-infoestatutario/api/(?P<pk>[0-9]+)/$',
        s2206_infoestatutario_api_views.s2206infoEstatutarioDetail.as_view() ),

    url(r'^s2206-infoestatutario/$', 
        s2206_infoestatutario_listar_views.listar, 
        name='s2206_infoestatutario'),

    url(r'^s2206-infoestatutario/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2206_infoestatutario_salvar_views.salvar, 
        name='s2206_infoestatutario_salvar'),
        
    url(r'^s2206-infoestatutario/cadastrar/$', 
        s2206_infoestatutario_salvar_views.salvar, 
        name='s2206_infoestatutario_cadastrar'),

    url(r'^s2206-infoestatutario/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2206_infoestatutario_salvar_views.salvar, 
        name='s2206_infoestatutario_salvar_output'),
        
    url(r'^s2206-infoestatutario/(?P<output>[\w-]+)/$', 
        s2206_infoestatutario_listar_views.listar, 
        name='s2206_infoestatutario_output'),

    url(r'^s2206-localtrabgeral/apagar/(?P<pk>[0-9]+)/$', 
        s2206_localtrabgeral_apagar_views.apagar, 
        name='s2206_localtrabgeral_apagar'),

    url(r'^s2206-localtrabgeral/api/$',
        s2206_localtrabgeral_api_views.s2206localTrabGeralList.as_view() ),

    url(r'^s2206-localtrabgeral/api/(?P<pk>[0-9]+)/$',
        s2206_localtrabgeral_api_views.s2206localTrabGeralDetail.as_view() ),

    url(r'^s2206-localtrabgeral/$', 
        s2206_localtrabgeral_listar_views.listar, 
        name='s2206_localtrabgeral'),

    url(r'^s2206-localtrabgeral/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2206_localtrabgeral_salvar_views.salvar, 
        name='s2206_localtrabgeral_salvar'),
        
    url(r'^s2206-localtrabgeral/cadastrar/$', 
        s2206_localtrabgeral_salvar_views.salvar, 
        name='s2206_localtrabgeral_cadastrar'),

    url(r'^s2206-localtrabgeral/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2206_localtrabgeral_salvar_views.salvar, 
        name='s2206_localtrabgeral_salvar_output'),
        
    url(r'^s2206-localtrabgeral/(?P<output>[\w-]+)/$', 
        s2206_localtrabgeral_listar_views.listar, 
        name='s2206_localtrabgeral_output'),

    url(r'^s2206-localtrabdom/apagar/(?P<pk>[0-9]+)/$', 
        s2206_localtrabdom_apagar_views.apagar, 
        name='s2206_localtrabdom_apagar'),

    url(r'^s2206-localtrabdom/api/$',
        s2206_localtrabdom_api_views.s2206localTrabDomList.as_view() ),

    url(r'^s2206-localtrabdom/api/(?P<pk>[0-9]+)/$',
        s2206_localtrabdom_api_views.s2206localTrabDomDetail.as_view() ),

    url(r'^s2206-localtrabdom/$', 
        s2206_localtrabdom_listar_views.listar, 
        name='s2206_localtrabdom'),

    url(r'^s2206-localtrabdom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2206_localtrabdom_salvar_views.salvar, 
        name='s2206_localtrabdom_salvar'),
        
    url(r'^s2206-localtrabdom/cadastrar/$', 
        s2206_localtrabdom_salvar_views.salvar, 
        name='s2206_localtrabdom_cadastrar'),

    url(r'^s2206-localtrabdom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2206_localtrabdom_salvar_views.salvar, 
        name='s2206_localtrabdom_salvar_output'),
        
    url(r'^s2206-localtrabdom/(?P<output>[\w-]+)/$', 
        s2206_localtrabdom_listar_views.listar, 
        name='s2206_localtrabdom_output'),

    url(r'^s2206-horcontratual/apagar/(?P<pk>[0-9]+)/$', 
        s2206_horcontratual_apagar_views.apagar, 
        name='s2206_horcontratual_apagar'),

    url(r'^s2206-horcontratual/api/$',
        s2206_horcontratual_api_views.s2206horContratualList.as_view() ),

    url(r'^s2206-horcontratual/api/(?P<pk>[0-9]+)/$',
        s2206_horcontratual_api_views.s2206horContratualDetail.as_view() ),

    url(r'^s2206-horcontratual/$', 
        s2206_horcontratual_listar_views.listar, 
        name='s2206_horcontratual'),

    url(r'^s2206-horcontratual/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2206_horcontratual_salvar_views.salvar, 
        name='s2206_horcontratual_salvar'),
        
    url(r'^s2206-horcontratual/cadastrar/$', 
        s2206_horcontratual_salvar_views.salvar, 
        name='s2206_horcontratual_cadastrar'),

    url(r'^s2206-horcontratual/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2206_horcontratual_salvar_views.salvar, 
        name='s2206_horcontratual_salvar_output'),
        
    url(r'^s2206-horcontratual/(?P<output>[\w-]+)/$', 
        s2206_horcontratual_listar_views.listar, 
        name='s2206_horcontratual_output'),

    url(r'^s2206-horario/apagar/(?P<pk>[0-9]+)/$', 
        s2206_horario_apagar_views.apagar, 
        name='s2206_horario_apagar'),

    url(r'^s2206-horario/api/$',
        s2206_horario_api_views.s2206horarioList.as_view() ),

    url(r'^s2206-horario/api/(?P<pk>[0-9]+)/$',
        s2206_horario_api_views.s2206horarioDetail.as_view() ),

    url(r'^s2206-horario/$', 
        s2206_horario_listar_views.listar, 
        name='s2206_horario'),

    url(r'^s2206-horario/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2206_horario_salvar_views.salvar, 
        name='s2206_horario_salvar'),
        
    url(r'^s2206-horario/cadastrar/$', 
        s2206_horario_salvar_views.salvar, 
        name='s2206_horario_cadastrar'),

    url(r'^s2206-horario/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2206_horario_salvar_views.salvar, 
        name='s2206_horario_salvar_output'),
        
    url(r'^s2206-horario/(?P<output>[\w-]+)/$', 
        s2206_horario_listar_views.listar, 
        name='s2206_horario_output'),

    url(r'^s2206-filiacaosindical/apagar/(?P<pk>[0-9]+)/$', 
        s2206_filiacaosindical_apagar_views.apagar, 
        name='s2206_filiacaosindical_apagar'),

    url(r'^s2206-filiacaosindical/api/$',
        s2206_filiacaosindical_api_views.s2206filiacaoSindicalList.as_view() ),

    url(r'^s2206-filiacaosindical/api/(?P<pk>[0-9]+)/$',
        s2206_filiacaosindical_api_views.s2206filiacaoSindicalDetail.as_view() ),

    url(r'^s2206-filiacaosindical/$', 
        s2206_filiacaosindical_listar_views.listar, 
        name='s2206_filiacaosindical'),

    url(r'^s2206-filiacaosindical/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2206_filiacaosindical_salvar_views.salvar, 
        name='s2206_filiacaosindical_salvar'),
        
    url(r'^s2206-filiacaosindical/cadastrar/$', 
        s2206_filiacaosindical_salvar_views.salvar, 
        name='s2206_filiacaosindical_cadastrar'),

    url(r'^s2206-filiacaosindical/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2206_filiacaosindical_salvar_views.salvar, 
        name='s2206_filiacaosindical_salvar_output'),
        
    url(r'^s2206-filiacaosindical/(?P<output>[\w-]+)/$', 
        s2206_filiacaosindical_listar_views.listar, 
        name='s2206_filiacaosindical_output'),

    url(r'^s2206-alvarajudicial/apagar/(?P<pk>[0-9]+)/$', 
        s2206_alvarajudicial_apagar_views.apagar, 
        name='s2206_alvarajudicial_apagar'),

    url(r'^s2206-alvarajudicial/api/$',
        s2206_alvarajudicial_api_views.s2206alvaraJudicialList.as_view() ),

    url(r'^s2206-alvarajudicial/api/(?P<pk>[0-9]+)/$',
        s2206_alvarajudicial_api_views.s2206alvaraJudicialDetail.as_view() ),

    url(r'^s2206-alvarajudicial/$', 
        s2206_alvarajudicial_listar_views.listar, 
        name='s2206_alvarajudicial'),

    url(r'^s2206-alvarajudicial/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2206_alvarajudicial_salvar_views.salvar, 
        name='s2206_alvarajudicial_salvar'),
        
    url(r'^s2206-alvarajudicial/cadastrar/$', 
        s2206_alvarajudicial_salvar_views.salvar, 
        name='s2206_alvarajudicial_cadastrar'),

    url(r'^s2206-alvarajudicial/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2206_alvarajudicial_salvar_views.salvar, 
        name='s2206_alvarajudicial_salvar_output'),
        
    url(r'^s2206-alvarajudicial/(?P<output>[\w-]+)/$', 
        s2206_alvarajudicial_listar_views.listar, 
        name='s2206_alvarajudicial_output'),

    url(r'^s2206-observacoes/apagar/(?P<pk>[0-9]+)/$', 
        s2206_observacoes_apagar_views.apagar, 
        name='s2206_observacoes_apagar'),

    url(r'^s2206-observacoes/api/$',
        s2206_observacoes_api_views.s2206observacoesList.as_view() ),

    url(r'^s2206-observacoes/api/(?P<pk>[0-9]+)/$',
        s2206_observacoes_api_views.s2206observacoesDetail.as_view() ),

    url(r'^s2206-observacoes/$', 
        s2206_observacoes_listar_views.listar, 
        name='s2206_observacoes'),

    url(r'^s2206-observacoes/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2206_observacoes_salvar_views.salvar, 
        name='s2206_observacoes_salvar'),
        
    url(r'^s2206-observacoes/cadastrar/$', 
        s2206_observacoes_salvar_views.salvar, 
        name='s2206_observacoes_cadastrar'),

    url(r'^s2206-observacoes/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2206_observacoes_salvar_views.salvar, 
        name='s2206_observacoes_salvar_output'),
        
    url(r'^s2206-observacoes/(?P<output>[\w-]+)/$', 
        s2206_observacoes_listar_views.listar, 
        name='s2206_observacoes_output'),

    url(r'^s2206-servpubl/apagar/(?P<pk>[0-9]+)/$', 
        s2206_servpubl_apagar_views.apagar, 
        name='s2206_servpubl_apagar'),

    url(r'^s2206-servpubl/api/$',
        s2206_servpubl_api_views.s2206servPublList.as_view() ),

    url(r'^s2206-servpubl/api/(?P<pk>[0-9]+)/$',
        s2206_servpubl_api_views.s2206servPublDetail.as_view() ),

    url(r'^s2206-servpubl/$', 
        s2206_servpubl_listar_views.listar, 
        name='s2206_servpubl'),

    url(r'^s2206-servpubl/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2206_servpubl_salvar_views.salvar, 
        name='s2206_servpubl_salvar'),
        
    url(r'^s2206-servpubl/cadastrar/$', 
        s2206_servpubl_salvar_views.salvar, 
        name='s2206_servpubl_cadastrar'),

    url(r'^s2206-servpubl/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2206_servpubl_salvar_views.salvar, 
        name='s2206_servpubl_salvar_output'),
        
    url(r'^s2206-servpubl/(?P<output>[\w-]+)/$', 
        s2206_servpubl_listar_views.listar, 
        name='s2206_servpubl_output'),


]