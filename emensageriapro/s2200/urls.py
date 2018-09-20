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



url(r'^s2200-documentos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_documentos.apagar', 
        name='s2200_documentos_apagar'),

url(r'^s2200-documentos/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_documentos.listar', 
        name='s2200_documentos'),

url(r'^s2200-documentos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_documentos.salvar', 
        name='s2200_documentos_salvar'),



url(r'^s2200-ctps/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_ctps.apagar', 
        name='s2200_ctps_apagar'),

url(r'^s2200-ctps/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_ctps.listar', 
        name='s2200_ctps'),

url(r'^s2200-ctps/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_ctps.salvar', 
        name='s2200_ctps_salvar'),



url(r'^s2200-ric/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_ric.apagar', 
        name='s2200_ric_apagar'),

url(r'^s2200-ric/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_ric.listar', 
        name='s2200_ric'),

url(r'^s2200-ric/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_ric.salvar', 
        name='s2200_ric_salvar'),



url(r'^s2200-rg/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_rg.apagar', 
        name='s2200_rg_apagar'),

url(r'^s2200-rg/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_rg.listar', 
        name='s2200_rg'),

url(r'^s2200-rg/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_rg.salvar', 
        name='s2200_rg_salvar'),



url(r'^s2200-rne/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_rne.apagar', 
        name='s2200_rne_apagar'),

url(r'^s2200-rne/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_rne.listar', 
        name='s2200_rne'),

url(r'^s2200-rne/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_rne.salvar', 
        name='s2200_rne_salvar'),



url(r'^s2200-oc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_oc.apagar', 
        name='s2200_oc_apagar'),

url(r'^s2200-oc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_oc.listar', 
        name='s2200_oc'),

url(r'^s2200-oc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_oc.salvar', 
        name='s2200_oc_salvar'),



url(r'^s2200-cnh/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_cnh.apagar', 
        name='s2200_cnh_apagar'),

url(r'^s2200-cnh/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_cnh.listar', 
        name='s2200_cnh'),

url(r'^s2200-cnh/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_cnh.salvar', 
        name='s2200_cnh_salvar'),



url(r'^s2200-brasil/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_brasil.apagar', 
        name='s2200_brasil_apagar'),

url(r'^s2200-brasil/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_brasil.listar', 
        name='s2200_brasil'),

url(r'^s2200-brasil/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_brasil.salvar', 
        name='s2200_brasil_salvar'),



url(r'^s2200-exterior/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_exterior.apagar', 
        name='s2200_exterior_apagar'),

url(r'^s2200-exterior/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_exterior.listar', 
        name='s2200_exterior'),

url(r'^s2200-exterior/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_exterior.salvar', 
        name='s2200_exterior_salvar'),



url(r'^s2200-trabestrangeiro/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_trabestrangeiro.apagar', 
        name='s2200_trabestrangeiro_apagar'),

url(r'^s2200-trabestrangeiro/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_trabestrangeiro.listar', 
        name='s2200_trabestrangeiro'),

url(r'^s2200-trabestrangeiro/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_trabestrangeiro.salvar', 
        name='s2200_trabestrangeiro_salvar'),

)


urlpatterns += patterns('',


url(r'^s2200-infodeficiencia/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_infodeficiencia.apagar', 
        name='s2200_infodeficiencia_apagar'),

url(r'^s2200-infodeficiencia/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_infodeficiencia.listar', 
        name='s2200_infodeficiencia'),

url(r'^s2200-infodeficiencia/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_infodeficiencia.salvar', 
        name='s2200_infodeficiencia_salvar'),



url(r'^s2200-dependente/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_dependente.apagar', 
        name='s2200_dependente_apagar'),

url(r'^s2200-dependente/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_dependente.listar', 
        name='s2200_dependente'),

url(r'^s2200-dependente/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_dependente.salvar', 
        name='s2200_dependente_salvar'),



url(r'^s2200-aposentadoria/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_aposentadoria.apagar', 
        name='s2200_aposentadoria_apagar'),

url(r'^s2200-aposentadoria/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_aposentadoria.listar', 
        name='s2200_aposentadoria'),

url(r'^s2200-aposentadoria/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_aposentadoria.salvar', 
        name='s2200_aposentadoria_salvar'),



url(r'^s2200-contato/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_contato.apagar', 
        name='s2200_contato_apagar'),

url(r'^s2200-contato/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_contato.listar', 
        name='s2200_contato'),

url(r'^s2200-contato/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_contato.salvar', 
        name='s2200_contato_salvar'),



url(r'^s2200-infoceletista/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_infoceletista.apagar', 
        name='s2200_infoceletista_apagar'),

url(r'^s2200-infoceletista/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_infoceletista.listar', 
        name='s2200_infoceletista'),

url(r'^s2200-infoceletista/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_infoceletista.salvar', 
        name='s2200_infoceletista_salvar'),



url(r'^s2200-trabtemporario/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_trabtemporario.apagar', 
        name='s2200_trabtemporario_apagar'),

url(r'^s2200-trabtemporario/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_trabtemporario.listar', 
        name='s2200_trabtemporario'),

url(r'^s2200-trabtemporario/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_trabtemporario.salvar', 
        name='s2200_trabtemporario_salvar'),



url(r'^s2200-ideestabvinc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_ideestabvinc.apagar', 
        name='s2200_ideestabvinc_apagar'),

url(r'^s2200-ideestabvinc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_ideestabvinc.listar', 
        name='s2200_ideestabvinc'),

url(r'^s2200-ideestabvinc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_ideestabvinc.salvar', 
        name='s2200_ideestabvinc_salvar'),



url(r'^s2200-idetrabsubstituido/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_idetrabsubstituido.apagar', 
        name='s2200_idetrabsubstituido_apagar'),

url(r'^s2200-idetrabsubstituido/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_idetrabsubstituido.listar', 
        name='s2200_idetrabsubstituido'),

url(r'^s2200-idetrabsubstituido/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_idetrabsubstituido.salvar', 
        name='s2200_idetrabsubstituido_salvar'),



url(r'^s2200-aprend/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_aprend.apagar', 
        name='s2200_aprend_apagar'),

url(r'^s2200-aprend/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_aprend.listar', 
        name='s2200_aprend'),

url(r'^s2200-aprend/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_aprend.salvar', 
        name='s2200_aprend_salvar'),



url(r'^s2200-infoestatutario/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_infoestatutario.apagar', 
        name='s2200_infoestatutario_apagar'),

url(r'^s2200-infoestatutario/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_infoestatutario.listar', 
        name='s2200_infoestatutario'),

url(r'^s2200-infoestatutario/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_infoestatutario.salvar', 
        name='s2200_infoestatutario_salvar'),

)


urlpatterns += patterns('',


url(r'^s2200-infodecjud/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_infodecjud.apagar', 
        name='s2200_infodecjud_apagar'),

url(r'^s2200-infodecjud/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_infodecjud.listar', 
        name='s2200_infodecjud'),

url(r'^s2200-infodecjud/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_infodecjud.salvar', 
        name='s2200_infodecjud_salvar'),



url(r'^s2200-localtrabgeral/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_localtrabgeral.apagar', 
        name='s2200_localtrabgeral_apagar'),

url(r'^s2200-localtrabgeral/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_localtrabgeral.listar', 
        name='s2200_localtrabgeral'),

url(r'^s2200-localtrabgeral/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_localtrabgeral.salvar', 
        name='s2200_localtrabgeral_salvar'),



url(r'^s2200-localtrabdom/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_localtrabdom.apagar', 
        name='s2200_localtrabdom_apagar'),

url(r'^s2200-localtrabdom/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_localtrabdom.listar', 
        name='s2200_localtrabdom'),

url(r'^s2200-localtrabdom/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_localtrabdom.salvar', 
        name='s2200_localtrabdom_salvar'),



url(r'^s2200-horcontratual/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_horcontratual.apagar', 
        name='s2200_horcontratual_apagar'),

url(r'^s2200-horcontratual/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_horcontratual.listar', 
        name='s2200_horcontratual'),

url(r'^s2200-horcontratual/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_horcontratual.salvar', 
        name='s2200_horcontratual_salvar'),



url(r'^s2200-horario/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_horario.apagar', 
        name='s2200_horario_apagar'),

url(r'^s2200-horario/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_horario.listar', 
        name='s2200_horario'),

url(r'^s2200-horario/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_horario.salvar', 
        name='s2200_horario_salvar'),



url(r'^s2200-filiacaosindical/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_filiacaosindical.apagar', 
        name='s2200_filiacaosindical_apagar'),

url(r'^s2200-filiacaosindical/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_filiacaosindical.listar', 
        name='s2200_filiacaosindical'),

url(r'^s2200-filiacaosindical/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_filiacaosindical.salvar', 
        name='s2200_filiacaosindical_salvar'),



url(r'^s2200-alvarajudicial/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_alvarajudicial.apagar', 
        name='s2200_alvarajudicial_apagar'),

url(r'^s2200-alvarajudicial/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_alvarajudicial.listar', 
        name='s2200_alvarajudicial'),

url(r'^s2200-alvarajudicial/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_alvarajudicial.salvar', 
        name='s2200_alvarajudicial_salvar'),



url(r'^s2200-observacoes/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_observacoes.apagar', 
        name='s2200_observacoes_apagar'),

url(r'^s2200-observacoes/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_observacoes.listar', 
        name='s2200_observacoes'),

url(r'^s2200-observacoes/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_observacoes.salvar', 
        name='s2200_observacoes_salvar'),



url(r'^s2200-sucessaovinc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_sucessaovinc.apagar', 
        name='s2200_sucessaovinc_apagar'),

url(r'^s2200-sucessaovinc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_sucessaovinc.listar', 
        name='s2200_sucessaovinc'),

url(r'^s2200-sucessaovinc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_sucessaovinc.salvar', 
        name='s2200_sucessaovinc_salvar'),



url(r'^s2200-transfdom/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_transfdom.apagar', 
        name='s2200_transfdom_apagar'),

url(r'^s2200-transfdom/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_transfdom.listar', 
        name='s2200_transfdom'),

url(r'^s2200-transfdom/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_transfdom.salvar', 
        name='s2200_transfdom_salvar'),

)


urlpatterns += patterns('',


url(r'^s2200-afastamento/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_afastamento.apagar', 
        name='s2200_afastamento_apagar'),

url(r'^s2200-afastamento/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_afastamento.listar', 
        name='s2200_afastamento'),

url(r'^s2200-afastamento/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_afastamento.salvar', 
        name='s2200_afastamento_salvar'),



url(r'^s2200-desligamento/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_desligamento.apagar', 
        name='s2200_desligamento_apagar'),

url(r'^s2200-desligamento/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_desligamento.listar', 
        name='s2200_desligamento'),

url(r'^s2200-desligamento/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_desligamento.salvar', 
        name='s2200_desligamento_salvar'),



url(r'^s2200-cessao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_cessao.apagar', 
        name='s2200_cessao_apagar'),

url(r'^s2200-cessao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_cessao.listar', 
        name='s2200_cessao'),

url(r'^s2200-cessao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2200.views.s2200_cessao.salvar', 
        name='s2200_cessao_salvar'),





)