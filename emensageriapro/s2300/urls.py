#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2300.views import s2300_documentos as s2300_documentos_views
from emensageriapro.s2300.views import s2300_ctps as s2300_ctps_views
from emensageriapro.s2300.views import s2300_ric as s2300_ric_views
from emensageriapro.s2300.views import s2300_rg as s2300_rg_views
from emensageriapro.s2300.views import s2300_rne as s2300_rne_views
from emensageriapro.s2300.views import s2300_oc as s2300_oc_views
from emensageriapro.s2300.views import s2300_cnh as s2300_cnh_views
from emensageriapro.s2300.views import s2300_brasil as s2300_brasil_views
from emensageriapro.s2300.views import s2300_exterior as s2300_exterior_views
from emensageriapro.s2300.views import s2300_trabestrangeiro as s2300_trabestrangeiro_views
from emensageriapro.s2300.views import s2300_infodeficiencia as s2300_infodeficiencia_views
from emensageriapro.s2300.views import s2300_dependente as s2300_dependente_views
from emensageriapro.s2300.views import s2300_contato as s2300_contato_views
from emensageriapro.s2300.views import s2300_infocomplementares as s2300_infocomplementares_views
from emensageriapro.s2300.views import s2300_cargofuncao as s2300_cargofuncao_views
from emensageriapro.s2300.views import s2300_remuneracao as s2300_remuneracao_views
from emensageriapro.s2300.views import s2300_fgts as s2300_fgts_views
from emensageriapro.s2300.views import s2300_infodirigentesindical as s2300_infodirigentesindical_views
from emensageriapro.s2300.views import s2300_infotrabcedido as s2300_infotrabcedido_views
from emensageriapro.s2300.views import s2300_infoestagiario as s2300_infoestagiario_views
from emensageriapro.s2300.views import s2300_ageintegracao as s2300_ageintegracao_views
from emensageriapro.s2300.views import s2300_supervisorestagio as s2300_supervisorestagio_views
from emensageriapro.s2300.views import s2300_afastamento as s2300_afastamento_views
from emensageriapro.s2300.views import s2300_termino as s2300_termino_views



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



url(r'^s2300-documentos/apagar/(?P<hash>.*)/$', 
        s2300_documentos_views.apagar, 
        name='s2300_documentos_apagar'),

url(r'^s2300-documentos/listar/(?P<hash>.*)/$', 
        s2300_documentos_views.listar, 
        name='s2300_documentos'),

url(r'^s2300-documentos/salvar/(?P<hash>.*)/$', 
        s2300_documentos_views.salvar, 
        name='s2300_documentos_salvar'),



url(r'^s2300-ctps/apagar/(?P<hash>.*)/$', 
        s2300_ctps_views.apagar, 
        name='s2300_ctps_apagar'),

url(r'^s2300-ctps/listar/(?P<hash>.*)/$', 
        s2300_ctps_views.listar, 
        name='s2300_ctps'),

url(r'^s2300-ctps/salvar/(?P<hash>.*)/$', 
        s2300_ctps_views.salvar, 
        name='s2300_ctps_salvar'),



url(r'^s2300-ric/apagar/(?P<hash>.*)/$', 
        s2300_ric_views.apagar, 
        name='s2300_ric_apagar'),

url(r'^s2300-ric/listar/(?P<hash>.*)/$', 
        s2300_ric_views.listar, 
        name='s2300_ric'),

url(r'^s2300-ric/salvar/(?P<hash>.*)/$', 
        s2300_ric_views.salvar, 
        name='s2300_ric_salvar'),



url(r'^s2300-rg/apagar/(?P<hash>.*)/$', 
        s2300_rg_views.apagar, 
        name='s2300_rg_apagar'),

url(r'^s2300-rg/listar/(?P<hash>.*)/$', 
        s2300_rg_views.listar, 
        name='s2300_rg'),

url(r'^s2300-rg/salvar/(?P<hash>.*)/$', 
        s2300_rg_views.salvar, 
        name='s2300_rg_salvar'),



url(r'^s2300-rne/apagar/(?P<hash>.*)/$', 
        s2300_rne_views.apagar, 
        name='s2300_rne_apagar'),

url(r'^s2300-rne/listar/(?P<hash>.*)/$', 
        s2300_rne_views.listar, 
        name='s2300_rne'),

url(r'^s2300-rne/salvar/(?P<hash>.*)/$', 
        s2300_rne_views.salvar, 
        name='s2300_rne_salvar'),



url(r'^s2300-oc/apagar/(?P<hash>.*)/$', 
        s2300_oc_views.apagar, 
        name='s2300_oc_apagar'),

url(r'^s2300-oc/listar/(?P<hash>.*)/$', 
        s2300_oc_views.listar, 
        name='s2300_oc'),

url(r'^s2300-oc/salvar/(?P<hash>.*)/$', 
        s2300_oc_views.salvar, 
        name='s2300_oc_salvar'),



url(r'^s2300-cnh/apagar/(?P<hash>.*)/$', 
        s2300_cnh_views.apagar, 
        name='s2300_cnh_apagar'),

url(r'^s2300-cnh/listar/(?P<hash>.*)/$', 
        s2300_cnh_views.listar, 
        name='s2300_cnh'),

url(r'^s2300-cnh/salvar/(?P<hash>.*)/$', 
        s2300_cnh_views.salvar, 
        name='s2300_cnh_salvar'),



url(r'^s2300-brasil/apagar/(?P<hash>.*)/$', 
        s2300_brasil_views.apagar, 
        name='s2300_brasil_apagar'),

url(r'^s2300-brasil/listar/(?P<hash>.*)/$', 
        s2300_brasil_views.listar, 
        name='s2300_brasil'),

url(r'^s2300-brasil/salvar/(?P<hash>.*)/$', 
        s2300_brasil_views.salvar, 
        name='s2300_brasil_salvar'),



url(r'^s2300-exterior/apagar/(?P<hash>.*)/$', 
        s2300_exterior_views.apagar, 
        name='s2300_exterior_apagar'),

url(r'^s2300-exterior/listar/(?P<hash>.*)/$', 
        s2300_exterior_views.listar, 
        name='s2300_exterior'),

url(r'^s2300-exterior/salvar/(?P<hash>.*)/$', 
        s2300_exterior_views.salvar, 
        name='s2300_exterior_salvar'),



url(r'^s2300-trabestrangeiro/apagar/(?P<hash>.*)/$', 
        s2300_trabestrangeiro_views.apagar, 
        name='s2300_trabestrangeiro_apagar'),

url(r'^s2300-trabestrangeiro/listar/(?P<hash>.*)/$', 
        s2300_trabestrangeiro_views.listar, 
        name='s2300_trabestrangeiro'),

url(r'^s2300-trabestrangeiro/salvar/(?P<hash>.*)/$', 
        s2300_trabestrangeiro_views.salvar, 
        name='s2300_trabestrangeiro_salvar'),



url(r'^s2300-infodeficiencia/apagar/(?P<hash>.*)/$', 
        s2300_infodeficiencia_views.apagar, 
        name='s2300_infodeficiencia_apagar'),

url(r'^s2300-infodeficiencia/listar/(?P<hash>.*)/$', 
        s2300_infodeficiencia_views.listar, 
        name='s2300_infodeficiencia'),

url(r'^s2300-infodeficiencia/salvar/(?P<hash>.*)/$', 
        s2300_infodeficiencia_views.salvar, 
        name='s2300_infodeficiencia_salvar'),



url(r'^s2300-dependente/apagar/(?P<hash>.*)/$', 
        s2300_dependente_views.apagar, 
        name='s2300_dependente_apagar'),

url(r'^s2300-dependente/listar/(?P<hash>.*)/$', 
        s2300_dependente_views.listar, 
        name='s2300_dependente'),

url(r'^s2300-dependente/salvar/(?P<hash>.*)/$', 
        s2300_dependente_views.salvar, 
        name='s2300_dependente_salvar'),



url(r'^s2300-contato/apagar/(?P<hash>.*)/$', 
        s2300_contato_views.apagar, 
        name='s2300_contato_apagar'),

url(r'^s2300-contato/listar/(?P<hash>.*)/$', 
        s2300_contato_views.listar, 
        name='s2300_contato'),

url(r'^s2300-contato/salvar/(?P<hash>.*)/$', 
        s2300_contato_views.salvar, 
        name='s2300_contato_salvar'),



url(r'^s2300-infocomplementares/apagar/(?P<hash>.*)/$', 
        s2300_infocomplementares_views.apagar, 
        name='s2300_infocomplementares_apagar'),

url(r'^s2300-infocomplementares/listar/(?P<hash>.*)/$', 
        s2300_infocomplementares_views.listar, 
        name='s2300_infocomplementares'),

url(r'^s2300-infocomplementares/salvar/(?P<hash>.*)/$', 
        s2300_infocomplementares_views.salvar, 
        name='s2300_infocomplementares_salvar'),



url(r'^s2300-cargofuncao/apagar/(?P<hash>.*)/$', 
        s2300_cargofuncao_views.apagar, 
        name='s2300_cargofuncao_apagar'),

url(r'^s2300-cargofuncao/listar/(?P<hash>.*)/$', 
        s2300_cargofuncao_views.listar, 
        name='s2300_cargofuncao'),

url(r'^s2300-cargofuncao/salvar/(?P<hash>.*)/$', 
        s2300_cargofuncao_views.salvar, 
        name='s2300_cargofuncao_salvar'),



url(r'^s2300-remuneracao/apagar/(?P<hash>.*)/$', 
        s2300_remuneracao_views.apagar, 
        name='s2300_remuneracao_apagar'),

url(r'^s2300-remuneracao/listar/(?P<hash>.*)/$', 
        s2300_remuneracao_views.listar, 
        name='s2300_remuneracao'),

url(r'^s2300-remuneracao/salvar/(?P<hash>.*)/$', 
        s2300_remuneracao_views.salvar, 
        name='s2300_remuneracao_salvar'),



url(r'^s2300-fgts/apagar/(?P<hash>.*)/$', 
        s2300_fgts_views.apagar, 
        name='s2300_fgts_apagar'),

url(r'^s2300-fgts/listar/(?P<hash>.*)/$', 
        s2300_fgts_views.listar, 
        name='s2300_fgts'),

url(r'^s2300-fgts/salvar/(?P<hash>.*)/$', 
        s2300_fgts_views.salvar, 
        name='s2300_fgts_salvar'),



url(r'^s2300-infodirigentesindical/apagar/(?P<hash>.*)/$', 
        s2300_infodirigentesindical_views.apagar, 
        name='s2300_infodirigentesindical_apagar'),

url(r'^s2300-infodirigentesindical/listar/(?P<hash>.*)/$', 
        s2300_infodirigentesindical_views.listar, 
        name='s2300_infodirigentesindical'),

url(r'^s2300-infodirigentesindical/salvar/(?P<hash>.*)/$', 
        s2300_infodirigentesindical_views.salvar, 
        name='s2300_infodirigentesindical_salvar'),



url(r'^s2300-infotrabcedido/apagar/(?P<hash>.*)/$', 
        s2300_infotrabcedido_views.apagar, 
        name='s2300_infotrabcedido_apagar'),

url(r'^s2300-infotrabcedido/listar/(?P<hash>.*)/$', 
        s2300_infotrabcedido_views.listar, 
        name='s2300_infotrabcedido'),

url(r'^s2300-infotrabcedido/salvar/(?P<hash>.*)/$', 
        s2300_infotrabcedido_views.salvar, 
        name='s2300_infotrabcedido_salvar'),



url(r'^s2300-infoestagiario/apagar/(?P<hash>.*)/$', 
        s2300_infoestagiario_views.apagar, 
        name='s2300_infoestagiario_apagar'),

url(r'^s2300-infoestagiario/listar/(?P<hash>.*)/$', 
        s2300_infoestagiario_views.listar, 
        name='s2300_infoestagiario'),

url(r'^s2300-infoestagiario/salvar/(?P<hash>.*)/$', 
        s2300_infoestagiario_views.salvar, 
        name='s2300_infoestagiario_salvar'),



url(r'^s2300-ageintegracao/apagar/(?P<hash>.*)/$', 
        s2300_ageintegracao_views.apagar, 
        name='s2300_ageintegracao_apagar'),

url(r'^s2300-ageintegracao/listar/(?P<hash>.*)/$', 
        s2300_ageintegracao_views.listar, 
        name='s2300_ageintegracao'),

url(r'^s2300-ageintegracao/salvar/(?P<hash>.*)/$', 
        s2300_ageintegracao_views.salvar, 
        name='s2300_ageintegracao_salvar'),



url(r'^s2300-supervisorestagio/apagar/(?P<hash>.*)/$', 
        s2300_supervisorestagio_views.apagar, 
        name='s2300_supervisorestagio_apagar'),

url(r'^s2300-supervisorestagio/listar/(?P<hash>.*)/$', 
        s2300_supervisorestagio_views.listar, 
        name='s2300_supervisorestagio'),

url(r'^s2300-supervisorestagio/salvar/(?P<hash>.*)/$', 
        s2300_supervisorestagio_views.salvar, 
        name='s2300_supervisorestagio_salvar'),



url(r'^s2300-afastamento/apagar/(?P<hash>.*)/$', 
        s2300_afastamento_views.apagar, 
        name='s2300_afastamento_apagar'),

url(r'^s2300-afastamento/listar/(?P<hash>.*)/$', 
        s2300_afastamento_views.listar, 
        name='s2300_afastamento'),

url(r'^s2300-afastamento/salvar/(?P<hash>.*)/$', 
        s2300_afastamento_views.salvar, 
        name='s2300_afastamento_salvar'),



url(r'^s2300-termino/apagar/(?P<hash>.*)/$', 
        s2300_termino_views.apagar, 
        name='s2300_termino_apagar'),

url(r'^s2300-termino/listar/(?P<hash>.*)/$', 
        s2300_termino_views.listar, 
        name='s2300_termino'),

url(r'^s2300-termino/salvar/(?P<hash>.*)/$', 
        s2300_termino_views.salvar, 
        name='s2300_termino_salvar'),





]