#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

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

urlpatterns = patterns('',
    # Examples:



url(r'^s2300-documentos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_documentos.apagar', 
        name='s2300_documentos_apagar'),

url(r'^s2300-documentos/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_documentos.listar', 
        name='s2300_documentos'),

url(r'^s2300-documentos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_documentos.salvar', 
        name='s2300_documentos_salvar'),



url(r'^s2300-ctps/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_ctps.apagar', 
        name='s2300_ctps_apagar'),

url(r'^s2300-ctps/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_ctps.listar', 
        name='s2300_ctps'),

url(r'^s2300-ctps/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_ctps.salvar', 
        name='s2300_ctps_salvar'),



url(r'^s2300-ric/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_ric.apagar', 
        name='s2300_ric_apagar'),

url(r'^s2300-ric/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_ric.listar', 
        name='s2300_ric'),

url(r'^s2300-ric/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_ric.salvar', 
        name='s2300_ric_salvar'),



url(r'^s2300-rg/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_rg.apagar', 
        name='s2300_rg_apagar'),

url(r'^s2300-rg/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_rg.listar', 
        name='s2300_rg'),

url(r'^s2300-rg/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_rg.salvar', 
        name='s2300_rg_salvar'),



url(r'^s2300-rne/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_rne.apagar', 
        name='s2300_rne_apagar'),

url(r'^s2300-rne/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_rne.listar', 
        name='s2300_rne'),

url(r'^s2300-rne/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_rne.salvar', 
        name='s2300_rne_salvar'),



url(r'^s2300-oc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_oc.apagar', 
        name='s2300_oc_apagar'),

url(r'^s2300-oc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_oc.listar', 
        name='s2300_oc'),

url(r'^s2300-oc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_oc.salvar', 
        name='s2300_oc_salvar'),



url(r'^s2300-cnh/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_cnh.apagar', 
        name='s2300_cnh_apagar'),

url(r'^s2300-cnh/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_cnh.listar', 
        name='s2300_cnh'),

url(r'^s2300-cnh/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_cnh.salvar', 
        name='s2300_cnh_salvar'),



url(r'^s2300-brasil/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_brasil.apagar', 
        name='s2300_brasil_apagar'),

url(r'^s2300-brasil/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_brasil.listar', 
        name='s2300_brasil'),

url(r'^s2300-brasil/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_brasil.salvar', 
        name='s2300_brasil_salvar'),



url(r'^s2300-exterior/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_exterior.apagar', 
        name='s2300_exterior_apagar'),

url(r'^s2300-exterior/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_exterior.listar', 
        name='s2300_exterior'),

url(r'^s2300-exterior/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_exterior.salvar', 
        name='s2300_exterior_salvar'),



url(r'^s2300-trabestrangeiro/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_trabestrangeiro.apagar', 
        name='s2300_trabestrangeiro_apagar'),

url(r'^s2300-trabestrangeiro/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_trabestrangeiro.listar', 
        name='s2300_trabestrangeiro'),

url(r'^s2300-trabestrangeiro/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_trabestrangeiro.salvar', 
        name='s2300_trabestrangeiro_salvar'),

)


urlpatterns += patterns('',


url(r'^s2300-infodeficiencia/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_infodeficiencia.apagar', 
        name='s2300_infodeficiencia_apagar'),

url(r'^s2300-infodeficiencia/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_infodeficiencia.listar', 
        name='s2300_infodeficiencia'),

url(r'^s2300-infodeficiencia/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_infodeficiencia.salvar', 
        name='s2300_infodeficiencia_salvar'),



url(r'^s2300-dependente/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_dependente.apagar', 
        name='s2300_dependente_apagar'),

url(r'^s2300-dependente/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_dependente.listar', 
        name='s2300_dependente'),

url(r'^s2300-dependente/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_dependente.salvar', 
        name='s2300_dependente_salvar'),



url(r'^s2300-contato/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_contato.apagar', 
        name='s2300_contato_apagar'),

url(r'^s2300-contato/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_contato.listar', 
        name='s2300_contato'),

url(r'^s2300-contato/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_contato.salvar', 
        name='s2300_contato_salvar'),



url(r'^s2300-infocomplementares/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_infocomplementares.apagar', 
        name='s2300_infocomplementares_apagar'),

url(r'^s2300-infocomplementares/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_infocomplementares.listar', 
        name='s2300_infocomplementares'),

url(r'^s2300-infocomplementares/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_infocomplementares.salvar', 
        name='s2300_infocomplementares_salvar'),



url(r'^s2300-cargofuncao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_cargofuncao.apagar', 
        name='s2300_cargofuncao_apagar'),

url(r'^s2300-cargofuncao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_cargofuncao.listar', 
        name='s2300_cargofuncao'),

url(r'^s2300-cargofuncao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_cargofuncao.salvar', 
        name='s2300_cargofuncao_salvar'),



url(r'^s2300-remuneracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_remuneracao.apagar', 
        name='s2300_remuneracao_apagar'),

url(r'^s2300-remuneracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_remuneracao.listar', 
        name='s2300_remuneracao'),

url(r'^s2300-remuneracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_remuneracao.salvar', 
        name='s2300_remuneracao_salvar'),



url(r'^s2300-fgts/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_fgts.apagar', 
        name='s2300_fgts_apagar'),

url(r'^s2300-fgts/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_fgts.listar', 
        name='s2300_fgts'),

url(r'^s2300-fgts/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_fgts.salvar', 
        name='s2300_fgts_salvar'),



url(r'^s2300-infodirigentesindical/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_infodirigentesindical.apagar', 
        name='s2300_infodirigentesindical_apagar'),

url(r'^s2300-infodirigentesindical/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_infodirigentesindical.listar', 
        name='s2300_infodirigentesindical'),

url(r'^s2300-infodirigentesindical/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_infodirigentesindical.salvar', 
        name='s2300_infodirigentesindical_salvar'),



url(r'^s2300-infotrabcedido/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_infotrabcedido.apagar', 
        name='s2300_infotrabcedido_apagar'),

url(r'^s2300-infotrabcedido/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_infotrabcedido.listar', 
        name='s2300_infotrabcedido'),

url(r'^s2300-infotrabcedido/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_infotrabcedido.salvar', 
        name='s2300_infotrabcedido_salvar'),



url(r'^s2300-infoestagiario/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_infoestagiario.apagar', 
        name='s2300_infoestagiario_apagar'),

url(r'^s2300-infoestagiario/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_infoestagiario.listar', 
        name='s2300_infoestagiario'),

url(r'^s2300-infoestagiario/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_infoestagiario.salvar', 
        name='s2300_infoestagiario_salvar'),

)


urlpatterns += patterns('',


url(r'^s2300-ageintegracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_ageintegracao.apagar', 
        name='s2300_ageintegracao_apagar'),

url(r'^s2300-ageintegracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_ageintegracao.listar', 
        name='s2300_ageintegracao'),

url(r'^s2300-ageintegracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_ageintegracao.salvar', 
        name='s2300_ageintegracao_salvar'),



url(r'^s2300-supervisorestagio/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_supervisorestagio.apagar', 
        name='s2300_supervisorestagio_apagar'),

url(r'^s2300-supervisorestagio/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_supervisorestagio.listar', 
        name='s2300_supervisorestagio'),

url(r'^s2300-supervisorestagio/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_supervisorestagio.salvar', 
        name='s2300_supervisorestagio_salvar'),



url(r'^s2300-afastamento/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_afastamento.apagar', 
        name='s2300_afastamento_apagar'),

url(r'^s2300-afastamento/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_afastamento.listar', 
        name='s2300_afastamento'),

url(r'^s2300-afastamento/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_afastamento.salvar', 
        name='s2300_afastamento_salvar'),



url(r'^s2300-termino/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_termino.apagar', 
        name='s2300_termino_apagar'),

url(r'^s2300-termino/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_termino.listar', 
        name='s2300_termino'),

url(r'^s2300-termino/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2300.views.s2300_termino.salvar', 
        name='s2300_termino_salvar'),





)