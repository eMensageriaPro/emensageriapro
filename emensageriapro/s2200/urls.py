#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2200.views import s2200_cnh as s2200_cnh_views
from emensageriapro.s2200.views import s2200_ctps as s2200_ctps_views
from emensageriapro.s2200.views import s2200_oc as s2200_oc_views
from emensageriapro.s2200.views import s2200_rg as s2200_rg_views
from emensageriapro.s2200.views import s2200_ric as s2200_ric_views
from emensageriapro.s2200.views import s2200_rne as s2200_rne_views
from emensageriapro.s2200.views import s2200_afastamento as s2200_afastamento_views
from emensageriapro.s2200.views import s2200_alvarajudicial as s2200_alvarajudicial_views
from emensageriapro.s2200.views import s2200_aposentadoria as s2200_aposentadoria_views
from emensageriapro.s2200.views import s2200_aprend as s2200_aprend_views
from emensageriapro.s2200.views import s2200_brasil as s2200_brasil_views
from emensageriapro.s2200.views import s2200_cessao as s2200_cessao_views
from emensageriapro.s2200.views import s2200_contato as s2200_contato_views
from emensageriapro.s2200.views import s2200_dependente as s2200_dependente_views
from emensageriapro.s2200.views import s2200_desligamento as s2200_desligamento_views
from emensageriapro.s2200.views import s2200_exterior as s2200_exterior_views
from emensageriapro.s2200.views import s2200_filiacaosindical as s2200_filiacaosindical_views
from emensageriapro.s2200.views import s2200_horcontratual as s2200_horcontratual_views
from emensageriapro.s2200.views import s2200_horario as s2200_horario_views
from emensageriapro.s2200.views import s2200_ideestabvinc as s2200_ideestabvinc_views
from emensageriapro.s2200.views import s2200_idetrabsubstituido as s2200_idetrabsubstituido_views
from emensageriapro.s2200.views import s2200_infoceletista as s2200_infoceletista_views
from emensageriapro.s2200.views import s2200_infodecjud as s2200_infodecjud_views
from emensageriapro.s2200.views import s2200_infodeficiencia as s2200_infodeficiencia_views
from emensageriapro.s2200.views import s2200_infoestatutario as s2200_infoestatutario_views
from emensageriapro.s2200.views import s2200_localtrabdom as s2200_localtrabdom_views
from emensageriapro.s2200.views import s2200_localtrabgeral as s2200_localtrabgeral_views
from emensageriapro.s2200.views import s2200_mudancacpf as s2200_mudancacpf_views
from emensageriapro.s2200.views import s2200_observacoes as s2200_observacoes_views
from emensageriapro.s2200.views import s2200_sucessaovinc as s2200_sucessaovinc_views
from emensageriapro.s2200.views import s2200_trabestrangeiro as s2200_trabestrangeiro_views
from emensageriapro.s2200.views import s2200_trabtemporario as s2200_trabtemporario_views
from emensageriapro.s2200.views import s2200_transfdom as s2200_transfdom_views



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



url(r'^s2200-cnh/apagar/(?P<hash>.*)/$', 
        s2200_cnh_views.apagar, 
        name='s2200_cnh_apagar'),

url(r'^s2200-cnh/api/$',
            s2200_cnh_views.s2200CNHList.as_view() ),

        url(r'^s2200-cnh/api/(?P<pk>[0-9]+)/$',
            s2200_cnh_views.s2200CNHDetail.as_view() ),

url(r'^s2200-cnh/listar/(?P<hash>.*)/$', 
        s2200_cnh_views.listar, 
        name='s2200_cnh'),

url(r'^s2200-cnh/salvar/(?P<hash>.*)/$', 
        s2200_cnh_views.salvar, 
        name='s2200_cnh_salvar'),



url(r'^s2200-ctps/apagar/(?P<hash>.*)/$', 
        s2200_ctps_views.apagar, 
        name='s2200_ctps_apagar'),

url(r'^s2200-ctps/api/$',
            s2200_ctps_views.s2200CTPSList.as_view() ),

        url(r'^s2200-ctps/api/(?P<pk>[0-9]+)/$',
            s2200_ctps_views.s2200CTPSDetail.as_view() ),

url(r'^s2200-ctps/listar/(?P<hash>.*)/$', 
        s2200_ctps_views.listar, 
        name='s2200_ctps'),

url(r'^s2200-ctps/salvar/(?P<hash>.*)/$', 
        s2200_ctps_views.salvar, 
        name='s2200_ctps_salvar'),



url(r'^s2200-oc/apagar/(?P<hash>.*)/$', 
        s2200_oc_views.apagar, 
        name='s2200_oc_apagar'),

url(r'^s2200-oc/api/$',
            s2200_oc_views.s2200OCList.as_view() ),

        url(r'^s2200-oc/api/(?P<pk>[0-9]+)/$',
            s2200_oc_views.s2200OCDetail.as_view() ),

url(r'^s2200-oc/listar/(?P<hash>.*)/$', 
        s2200_oc_views.listar, 
        name='s2200_oc'),

url(r'^s2200-oc/salvar/(?P<hash>.*)/$', 
        s2200_oc_views.salvar, 
        name='s2200_oc_salvar'),



url(r'^s2200-rg/apagar/(?P<hash>.*)/$', 
        s2200_rg_views.apagar, 
        name='s2200_rg_apagar'),

url(r'^s2200-rg/api/$',
            s2200_rg_views.s2200RGList.as_view() ),

        url(r'^s2200-rg/api/(?P<pk>[0-9]+)/$',
            s2200_rg_views.s2200RGDetail.as_view() ),

url(r'^s2200-rg/listar/(?P<hash>.*)/$', 
        s2200_rg_views.listar, 
        name='s2200_rg'),

url(r'^s2200-rg/salvar/(?P<hash>.*)/$', 
        s2200_rg_views.salvar, 
        name='s2200_rg_salvar'),



url(r'^s2200-ric/apagar/(?P<hash>.*)/$', 
        s2200_ric_views.apagar, 
        name='s2200_ric_apagar'),

url(r'^s2200-ric/api/$',
            s2200_ric_views.s2200RICList.as_view() ),

        url(r'^s2200-ric/api/(?P<pk>[0-9]+)/$',
            s2200_ric_views.s2200RICDetail.as_view() ),

url(r'^s2200-ric/listar/(?P<hash>.*)/$', 
        s2200_ric_views.listar, 
        name='s2200_ric'),

url(r'^s2200-ric/salvar/(?P<hash>.*)/$', 
        s2200_ric_views.salvar, 
        name='s2200_ric_salvar'),



url(r'^s2200-rne/apagar/(?P<hash>.*)/$', 
        s2200_rne_views.apagar, 
        name='s2200_rne_apagar'),

url(r'^s2200-rne/api/$',
            s2200_rne_views.s2200RNEList.as_view() ),

        url(r'^s2200-rne/api/(?P<pk>[0-9]+)/$',
            s2200_rne_views.s2200RNEDetail.as_view() ),

url(r'^s2200-rne/listar/(?P<hash>.*)/$', 
        s2200_rne_views.listar, 
        name='s2200_rne'),

url(r'^s2200-rne/salvar/(?P<hash>.*)/$', 
        s2200_rne_views.salvar, 
        name='s2200_rne_salvar'),



url(r'^s2200-afastamento/apagar/(?P<hash>.*)/$', 
        s2200_afastamento_views.apagar, 
        name='s2200_afastamento_apagar'),

url(r'^s2200-afastamento/api/$',
            s2200_afastamento_views.s2200afastamentoList.as_view() ),

        url(r'^s2200-afastamento/api/(?P<pk>[0-9]+)/$',
            s2200_afastamento_views.s2200afastamentoDetail.as_view() ),

url(r'^s2200-afastamento/listar/(?P<hash>.*)/$', 
        s2200_afastamento_views.listar, 
        name='s2200_afastamento'),

url(r'^s2200-afastamento/salvar/(?P<hash>.*)/$', 
        s2200_afastamento_views.salvar, 
        name='s2200_afastamento_salvar'),



url(r'^s2200-alvarajudicial/apagar/(?P<hash>.*)/$', 
        s2200_alvarajudicial_views.apagar, 
        name='s2200_alvarajudicial_apagar'),

url(r'^s2200-alvarajudicial/api/$',
            s2200_alvarajudicial_views.s2200alvaraJudicialList.as_view() ),

        url(r'^s2200-alvarajudicial/api/(?P<pk>[0-9]+)/$',
            s2200_alvarajudicial_views.s2200alvaraJudicialDetail.as_view() ),

url(r'^s2200-alvarajudicial/listar/(?P<hash>.*)/$', 
        s2200_alvarajudicial_views.listar, 
        name='s2200_alvarajudicial'),

url(r'^s2200-alvarajudicial/salvar/(?P<hash>.*)/$', 
        s2200_alvarajudicial_views.salvar, 
        name='s2200_alvarajudicial_salvar'),



url(r'^s2200-aposentadoria/apagar/(?P<hash>.*)/$', 
        s2200_aposentadoria_views.apagar, 
        name='s2200_aposentadoria_apagar'),

url(r'^s2200-aposentadoria/api/$',
            s2200_aposentadoria_views.s2200aposentadoriaList.as_view() ),

        url(r'^s2200-aposentadoria/api/(?P<pk>[0-9]+)/$',
            s2200_aposentadoria_views.s2200aposentadoriaDetail.as_view() ),

url(r'^s2200-aposentadoria/listar/(?P<hash>.*)/$', 
        s2200_aposentadoria_views.listar, 
        name='s2200_aposentadoria'),

url(r'^s2200-aposentadoria/salvar/(?P<hash>.*)/$', 
        s2200_aposentadoria_views.salvar, 
        name='s2200_aposentadoria_salvar'),



url(r'^s2200-aprend/apagar/(?P<hash>.*)/$', 
        s2200_aprend_views.apagar, 
        name='s2200_aprend_apagar'),

url(r'^s2200-aprend/api/$',
            s2200_aprend_views.s2200aprendList.as_view() ),

        url(r'^s2200-aprend/api/(?P<pk>[0-9]+)/$',
            s2200_aprend_views.s2200aprendDetail.as_view() ),

url(r'^s2200-aprend/listar/(?P<hash>.*)/$', 
        s2200_aprend_views.listar, 
        name='s2200_aprend'),

url(r'^s2200-aprend/salvar/(?P<hash>.*)/$', 
        s2200_aprend_views.salvar, 
        name='s2200_aprend_salvar'),



url(r'^s2200-brasil/apagar/(?P<hash>.*)/$', 
        s2200_brasil_views.apagar, 
        name='s2200_brasil_apagar'),

url(r'^s2200-brasil/api/$',
            s2200_brasil_views.s2200brasilList.as_view() ),

        url(r'^s2200-brasil/api/(?P<pk>[0-9]+)/$',
            s2200_brasil_views.s2200brasilDetail.as_view() ),

url(r'^s2200-brasil/listar/(?P<hash>.*)/$', 
        s2200_brasil_views.listar, 
        name='s2200_brasil'),

url(r'^s2200-brasil/salvar/(?P<hash>.*)/$', 
        s2200_brasil_views.salvar, 
        name='s2200_brasil_salvar'),



url(r'^s2200-cessao/apagar/(?P<hash>.*)/$', 
        s2200_cessao_views.apagar, 
        name='s2200_cessao_apagar'),

url(r'^s2200-cessao/api/$',
            s2200_cessao_views.s2200cessaoList.as_view() ),

        url(r'^s2200-cessao/api/(?P<pk>[0-9]+)/$',
            s2200_cessao_views.s2200cessaoDetail.as_view() ),

url(r'^s2200-cessao/listar/(?P<hash>.*)/$', 
        s2200_cessao_views.listar, 
        name='s2200_cessao'),

url(r'^s2200-cessao/salvar/(?P<hash>.*)/$', 
        s2200_cessao_views.salvar, 
        name='s2200_cessao_salvar'),



url(r'^s2200-contato/apagar/(?P<hash>.*)/$', 
        s2200_contato_views.apagar, 
        name='s2200_contato_apagar'),

url(r'^s2200-contato/api/$',
            s2200_contato_views.s2200contatoList.as_view() ),

        url(r'^s2200-contato/api/(?P<pk>[0-9]+)/$',
            s2200_contato_views.s2200contatoDetail.as_view() ),

url(r'^s2200-contato/listar/(?P<hash>.*)/$', 
        s2200_contato_views.listar, 
        name='s2200_contato'),

url(r'^s2200-contato/salvar/(?P<hash>.*)/$', 
        s2200_contato_views.salvar, 
        name='s2200_contato_salvar'),



url(r'^s2200-dependente/apagar/(?P<hash>.*)/$', 
        s2200_dependente_views.apagar, 
        name='s2200_dependente_apagar'),

url(r'^s2200-dependente/api/$',
            s2200_dependente_views.s2200dependenteList.as_view() ),

        url(r'^s2200-dependente/api/(?P<pk>[0-9]+)/$',
            s2200_dependente_views.s2200dependenteDetail.as_view() ),

url(r'^s2200-dependente/listar/(?P<hash>.*)/$', 
        s2200_dependente_views.listar, 
        name='s2200_dependente'),

url(r'^s2200-dependente/salvar/(?P<hash>.*)/$', 
        s2200_dependente_views.salvar, 
        name='s2200_dependente_salvar'),



url(r'^s2200-desligamento/apagar/(?P<hash>.*)/$', 
        s2200_desligamento_views.apagar, 
        name='s2200_desligamento_apagar'),

url(r'^s2200-desligamento/api/$',
            s2200_desligamento_views.s2200desligamentoList.as_view() ),

        url(r'^s2200-desligamento/api/(?P<pk>[0-9]+)/$',
            s2200_desligamento_views.s2200desligamentoDetail.as_view() ),

url(r'^s2200-desligamento/listar/(?P<hash>.*)/$', 
        s2200_desligamento_views.listar, 
        name='s2200_desligamento'),

url(r'^s2200-desligamento/salvar/(?P<hash>.*)/$', 
        s2200_desligamento_views.salvar, 
        name='s2200_desligamento_salvar'),



url(r'^s2200-exterior/apagar/(?P<hash>.*)/$', 
        s2200_exterior_views.apagar, 
        name='s2200_exterior_apagar'),

url(r'^s2200-exterior/api/$',
            s2200_exterior_views.s2200exteriorList.as_view() ),

        url(r'^s2200-exterior/api/(?P<pk>[0-9]+)/$',
            s2200_exterior_views.s2200exteriorDetail.as_view() ),

url(r'^s2200-exterior/listar/(?P<hash>.*)/$', 
        s2200_exterior_views.listar, 
        name='s2200_exterior'),

url(r'^s2200-exterior/salvar/(?P<hash>.*)/$', 
        s2200_exterior_views.salvar, 
        name='s2200_exterior_salvar'),



url(r'^s2200-filiacaosindical/apagar/(?P<hash>.*)/$', 
        s2200_filiacaosindical_views.apagar, 
        name='s2200_filiacaosindical_apagar'),

url(r'^s2200-filiacaosindical/api/$',
            s2200_filiacaosindical_views.s2200filiacaoSindicalList.as_view() ),

        url(r'^s2200-filiacaosindical/api/(?P<pk>[0-9]+)/$',
            s2200_filiacaosindical_views.s2200filiacaoSindicalDetail.as_view() ),

url(r'^s2200-filiacaosindical/listar/(?P<hash>.*)/$', 
        s2200_filiacaosindical_views.listar, 
        name='s2200_filiacaosindical'),

url(r'^s2200-filiacaosindical/salvar/(?P<hash>.*)/$', 
        s2200_filiacaosindical_views.salvar, 
        name='s2200_filiacaosindical_salvar'),



url(r'^s2200-horcontratual/apagar/(?P<hash>.*)/$', 
        s2200_horcontratual_views.apagar, 
        name='s2200_horcontratual_apagar'),

url(r'^s2200-horcontratual/api/$',
            s2200_horcontratual_views.s2200horContratualList.as_view() ),

        url(r'^s2200-horcontratual/api/(?P<pk>[0-9]+)/$',
            s2200_horcontratual_views.s2200horContratualDetail.as_view() ),

url(r'^s2200-horcontratual/listar/(?P<hash>.*)/$', 
        s2200_horcontratual_views.listar, 
        name='s2200_horcontratual'),

url(r'^s2200-horcontratual/salvar/(?P<hash>.*)/$', 
        s2200_horcontratual_views.salvar, 
        name='s2200_horcontratual_salvar'),



url(r'^s2200-horario/apagar/(?P<hash>.*)/$', 
        s2200_horario_views.apagar, 
        name='s2200_horario_apagar'),

url(r'^s2200-horario/api/$',
            s2200_horario_views.s2200horarioList.as_view() ),

        url(r'^s2200-horario/api/(?P<pk>[0-9]+)/$',
            s2200_horario_views.s2200horarioDetail.as_view() ),

url(r'^s2200-horario/listar/(?P<hash>.*)/$', 
        s2200_horario_views.listar, 
        name='s2200_horario'),

url(r'^s2200-horario/salvar/(?P<hash>.*)/$', 
        s2200_horario_views.salvar, 
        name='s2200_horario_salvar'),



url(r'^s2200-ideestabvinc/apagar/(?P<hash>.*)/$', 
        s2200_ideestabvinc_views.apagar, 
        name='s2200_ideestabvinc_apagar'),

url(r'^s2200-ideestabvinc/api/$',
            s2200_ideestabvinc_views.s2200ideEstabVincList.as_view() ),

        url(r'^s2200-ideestabvinc/api/(?P<pk>[0-9]+)/$',
            s2200_ideestabvinc_views.s2200ideEstabVincDetail.as_view() ),

url(r'^s2200-ideestabvinc/listar/(?P<hash>.*)/$', 
        s2200_ideestabvinc_views.listar, 
        name='s2200_ideestabvinc'),

url(r'^s2200-ideestabvinc/salvar/(?P<hash>.*)/$', 
        s2200_ideestabvinc_views.salvar, 
        name='s2200_ideestabvinc_salvar'),



url(r'^s2200-idetrabsubstituido/apagar/(?P<hash>.*)/$', 
        s2200_idetrabsubstituido_views.apagar, 
        name='s2200_idetrabsubstituido_apagar'),

url(r'^s2200-idetrabsubstituido/api/$',
            s2200_idetrabsubstituido_views.s2200ideTrabSubstituidoList.as_view() ),

        url(r'^s2200-idetrabsubstituido/api/(?P<pk>[0-9]+)/$',
            s2200_idetrabsubstituido_views.s2200ideTrabSubstituidoDetail.as_view() ),

url(r'^s2200-idetrabsubstituido/listar/(?P<hash>.*)/$', 
        s2200_idetrabsubstituido_views.listar, 
        name='s2200_idetrabsubstituido'),

url(r'^s2200-idetrabsubstituido/salvar/(?P<hash>.*)/$', 
        s2200_idetrabsubstituido_views.salvar, 
        name='s2200_idetrabsubstituido_salvar'),



url(r'^s2200-infoceletista/apagar/(?P<hash>.*)/$', 
        s2200_infoceletista_views.apagar, 
        name='s2200_infoceletista_apagar'),

url(r'^s2200-infoceletista/api/$',
            s2200_infoceletista_views.s2200infoCeletistaList.as_view() ),

        url(r'^s2200-infoceletista/api/(?P<pk>[0-9]+)/$',
            s2200_infoceletista_views.s2200infoCeletistaDetail.as_view() ),

url(r'^s2200-infoceletista/listar/(?P<hash>.*)/$', 
        s2200_infoceletista_views.listar, 
        name='s2200_infoceletista'),

url(r'^s2200-infoceletista/salvar/(?P<hash>.*)/$', 
        s2200_infoceletista_views.salvar, 
        name='s2200_infoceletista_salvar'),



url(r'^s2200-infodecjud/apagar/(?P<hash>.*)/$', 
        s2200_infodecjud_views.apagar, 
        name='s2200_infodecjud_apagar'),

url(r'^s2200-infodecjud/api/$',
            s2200_infodecjud_views.s2200infoDecJudList.as_view() ),

        url(r'^s2200-infodecjud/api/(?P<pk>[0-9]+)/$',
            s2200_infodecjud_views.s2200infoDecJudDetail.as_view() ),

url(r'^s2200-infodecjud/listar/(?P<hash>.*)/$', 
        s2200_infodecjud_views.listar, 
        name='s2200_infodecjud'),

url(r'^s2200-infodecjud/salvar/(?P<hash>.*)/$', 
        s2200_infodecjud_views.salvar, 
        name='s2200_infodecjud_salvar'),



url(r'^s2200-infodeficiencia/apagar/(?P<hash>.*)/$', 
        s2200_infodeficiencia_views.apagar, 
        name='s2200_infodeficiencia_apagar'),

url(r'^s2200-infodeficiencia/api/$',
            s2200_infodeficiencia_views.s2200infoDeficienciaList.as_view() ),

        url(r'^s2200-infodeficiencia/api/(?P<pk>[0-9]+)/$',
            s2200_infodeficiencia_views.s2200infoDeficienciaDetail.as_view() ),

url(r'^s2200-infodeficiencia/listar/(?P<hash>.*)/$', 
        s2200_infodeficiencia_views.listar, 
        name='s2200_infodeficiencia'),

url(r'^s2200-infodeficiencia/salvar/(?P<hash>.*)/$', 
        s2200_infodeficiencia_views.salvar, 
        name='s2200_infodeficiencia_salvar'),



url(r'^s2200-infoestatutario/apagar/(?P<hash>.*)/$', 
        s2200_infoestatutario_views.apagar, 
        name='s2200_infoestatutario_apagar'),

url(r'^s2200-infoestatutario/api/$',
            s2200_infoestatutario_views.s2200infoEstatutarioList.as_view() ),

        url(r'^s2200-infoestatutario/api/(?P<pk>[0-9]+)/$',
            s2200_infoestatutario_views.s2200infoEstatutarioDetail.as_view() ),

url(r'^s2200-infoestatutario/listar/(?P<hash>.*)/$', 
        s2200_infoestatutario_views.listar, 
        name='s2200_infoestatutario'),

url(r'^s2200-infoestatutario/salvar/(?P<hash>.*)/$', 
        s2200_infoestatutario_views.salvar, 
        name='s2200_infoestatutario_salvar'),



url(r'^s2200-localtrabdom/apagar/(?P<hash>.*)/$', 
        s2200_localtrabdom_views.apagar, 
        name='s2200_localtrabdom_apagar'),

url(r'^s2200-localtrabdom/api/$',
            s2200_localtrabdom_views.s2200localTrabDomList.as_view() ),

        url(r'^s2200-localtrabdom/api/(?P<pk>[0-9]+)/$',
            s2200_localtrabdom_views.s2200localTrabDomDetail.as_view() ),

url(r'^s2200-localtrabdom/listar/(?P<hash>.*)/$', 
        s2200_localtrabdom_views.listar, 
        name='s2200_localtrabdom'),

url(r'^s2200-localtrabdom/salvar/(?P<hash>.*)/$', 
        s2200_localtrabdom_views.salvar, 
        name='s2200_localtrabdom_salvar'),



url(r'^s2200-localtrabgeral/apagar/(?P<hash>.*)/$', 
        s2200_localtrabgeral_views.apagar, 
        name='s2200_localtrabgeral_apagar'),

url(r'^s2200-localtrabgeral/api/$',
            s2200_localtrabgeral_views.s2200localTrabGeralList.as_view() ),

        url(r'^s2200-localtrabgeral/api/(?P<pk>[0-9]+)/$',
            s2200_localtrabgeral_views.s2200localTrabGeralDetail.as_view() ),

url(r'^s2200-localtrabgeral/listar/(?P<hash>.*)/$', 
        s2200_localtrabgeral_views.listar, 
        name='s2200_localtrabgeral'),

url(r'^s2200-localtrabgeral/salvar/(?P<hash>.*)/$', 
        s2200_localtrabgeral_views.salvar, 
        name='s2200_localtrabgeral_salvar'),



url(r'^s2200-mudancacpf/apagar/(?P<hash>.*)/$', 
        s2200_mudancacpf_views.apagar, 
        name='s2200_mudancacpf_apagar'),

url(r'^s2200-mudancacpf/api/$',
            s2200_mudancacpf_views.s2200mudancaCPFList.as_view() ),

        url(r'^s2200-mudancacpf/api/(?P<pk>[0-9]+)/$',
            s2200_mudancacpf_views.s2200mudancaCPFDetail.as_view() ),

url(r'^s2200-mudancacpf/listar/(?P<hash>.*)/$', 
        s2200_mudancacpf_views.listar, 
        name='s2200_mudancacpf'),

url(r'^s2200-mudancacpf/salvar/(?P<hash>.*)/$', 
        s2200_mudancacpf_views.salvar, 
        name='s2200_mudancacpf_salvar'),



url(r'^s2200-observacoes/apagar/(?P<hash>.*)/$', 
        s2200_observacoes_views.apagar, 
        name='s2200_observacoes_apagar'),

url(r'^s2200-observacoes/api/$',
            s2200_observacoes_views.s2200observacoesList.as_view() ),

        url(r'^s2200-observacoes/api/(?P<pk>[0-9]+)/$',
            s2200_observacoes_views.s2200observacoesDetail.as_view() ),

url(r'^s2200-observacoes/listar/(?P<hash>.*)/$', 
        s2200_observacoes_views.listar, 
        name='s2200_observacoes'),

url(r'^s2200-observacoes/salvar/(?P<hash>.*)/$', 
        s2200_observacoes_views.salvar, 
        name='s2200_observacoes_salvar'),



url(r'^s2200-sucessaovinc/apagar/(?P<hash>.*)/$', 
        s2200_sucessaovinc_views.apagar, 
        name='s2200_sucessaovinc_apagar'),

url(r'^s2200-sucessaovinc/api/$',
            s2200_sucessaovinc_views.s2200sucessaoVincList.as_view() ),

        url(r'^s2200-sucessaovinc/api/(?P<pk>[0-9]+)/$',
            s2200_sucessaovinc_views.s2200sucessaoVincDetail.as_view() ),

url(r'^s2200-sucessaovinc/listar/(?P<hash>.*)/$', 
        s2200_sucessaovinc_views.listar, 
        name='s2200_sucessaovinc'),

url(r'^s2200-sucessaovinc/salvar/(?P<hash>.*)/$', 
        s2200_sucessaovinc_views.salvar, 
        name='s2200_sucessaovinc_salvar'),



url(r'^s2200-trabestrangeiro/apagar/(?P<hash>.*)/$', 
        s2200_trabestrangeiro_views.apagar, 
        name='s2200_trabestrangeiro_apagar'),

url(r'^s2200-trabestrangeiro/api/$',
            s2200_trabestrangeiro_views.s2200trabEstrangeiroList.as_view() ),

        url(r'^s2200-trabestrangeiro/api/(?P<pk>[0-9]+)/$',
            s2200_trabestrangeiro_views.s2200trabEstrangeiroDetail.as_view() ),

url(r'^s2200-trabestrangeiro/listar/(?P<hash>.*)/$', 
        s2200_trabestrangeiro_views.listar, 
        name='s2200_trabestrangeiro'),

url(r'^s2200-trabestrangeiro/salvar/(?P<hash>.*)/$', 
        s2200_trabestrangeiro_views.salvar, 
        name='s2200_trabestrangeiro_salvar'),



url(r'^s2200-trabtemporario/apagar/(?P<hash>.*)/$', 
        s2200_trabtemporario_views.apagar, 
        name='s2200_trabtemporario_apagar'),

url(r'^s2200-trabtemporario/api/$',
            s2200_trabtemporario_views.s2200trabTemporarioList.as_view() ),

        url(r'^s2200-trabtemporario/api/(?P<pk>[0-9]+)/$',
            s2200_trabtemporario_views.s2200trabTemporarioDetail.as_view() ),

url(r'^s2200-trabtemporario/listar/(?P<hash>.*)/$', 
        s2200_trabtemporario_views.listar, 
        name='s2200_trabtemporario'),

url(r'^s2200-trabtemporario/salvar/(?P<hash>.*)/$', 
        s2200_trabtemporario_views.salvar, 
        name='s2200_trabtemporario_salvar'),



url(r'^s2200-transfdom/apagar/(?P<hash>.*)/$', 
        s2200_transfdom_views.apagar, 
        name='s2200_transfdom_apagar'),

url(r'^s2200-transfdom/api/$',
            s2200_transfdom_views.s2200transfDomList.as_view() ),

        url(r'^s2200-transfdom/api/(?P<pk>[0-9]+)/$',
            s2200_transfdom_views.s2200transfDomDetail.as_view() ),

url(r'^s2200-transfdom/listar/(?P<hash>.*)/$', 
        s2200_transfdom_views.listar, 
        name='s2200_transfdom'),

url(r'^s2200-transfdom/salvar/(?P<hash>.*)/$', 
        s2200_transfdom_views.salvar, 
        name='s2200_transfdom_salvar'),





]