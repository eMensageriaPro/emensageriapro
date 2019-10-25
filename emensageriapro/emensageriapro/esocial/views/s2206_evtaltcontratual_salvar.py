#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"


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


from constance import config
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from wkhtmltopdf.views import PDFTemplateResponse
from emensageriapro.padrao import *
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s2206.models import s2206infoCeletista
from emensageriapro.s2206.forms import form_s2206_infoceletista
from emensageriapro.s2206.models import s2206infoEstatutario
from emensageriapro.s2206.forms import form_s2206_infoestatutario
from emensageriapro.s2206.models import s2206localTrabGeral
from emensageriapro.s2206.forms import form_s2206_localtrabgeral
from emensageriapro.s2206.models import s2206localTrabDom
from emensageriapro.s2206.forms import form_s2206_localtrabdom
from emensageriapro.s2206.models import s2206horContratual
from emensageriapro.s2206.forms import form_s2206_horcontratual
from emensageriapro.s2206.models import s2206filiacaoSindical
from emensageriapro.s2206.forms import form_s2206_filiacaosindical
from emensageriapro.s2206.models import s2206alvaraJudicial
from emensageriapro.s2206.forms import form_s2206_alvarajudicial
from emensageriapro.s2206.models import s2206observacoes
from emensageriapro.s2206.forms import form_s2206_observacoes
from emensageriapro.s2206.models import s2206servPubl
from emensageriapro.s2206.forms import form_s2206_servpubl


@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    TP_AMB = config.ESOCIAL_TP_AMB

    if pk:

        s2206_evtaltcontratual = get_object_or_404(s2206evtAltContratual, id=pk)

    if request.user.has_perm('esocial.can_see_s2206evtAltContratual'):

        if pk:

            s2206_evtaltcontratual_form = form_s2206_evtaltcontratual(request.POST or None, instance=s2206_evtaltcontratual,
                                         initial={'ativo': True})
                     
        else:

            s2206_evtaltcontratual_form = form_s2206_evtaltcontratual(request.POST or None,
                                         initial={'versao': VERSAO_LAYOUT_ESOCIAL,
                                                  'status': STATUS_EVENTO_CADASTRADO,
                                                  'tpamb': TP_AMB,
                                                  'procemi': 1,
                                                  'verproc': VERSAO_EMENSAGERIA,
                                                  'ativo': True})
                              
        if request.method == 'POST':

            if s2206_evtaltcontratual_form.is_valid():

                obj = s2206_evtaltcontratual_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')

                if not pk:

                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj, 'esocial')
             
                if 'return_page' in request.session and request.session['return_page'] and 's2206-evtaltcontratual' not in request.session['return_page']:

                    return HttpResponseRedirect(request.session['return_page'])

                if pk != obj.id:

                    return redirect(
                        's2206_evtaltcontratual_salvar',
                        pk=obj.id)

            else:
                messages.error(request, u'Erro ao salvar!')

        s2206_evtaltcontratual_form = disabled_form_fields(
             s2206_evtaltcontratual_form,
             request.user.has_perm('esocial.change_s2206evtAltContratual'))

        if pk:

            if s2206_evtaltcontratual.status != 0:

                s2206_evtaltcontratual_form = disabled_form_fields(s2206_evtaltcontratual_form, False)

        for field in s2206_evtaltcontratual_form.fields.keys():

            s2206_evtaltcontratual_form.fields[field].widget.attrs['ng-model'] = 's2206_evtaltcontratual_'+field

        if output:

            s2206_evtaltcontratual_form = disabled_form_for_print(s2206_evtaltcontratual_form)


        s2206_infoceletista_lista = None
        s2206_infoceletista_form = None
        s2206_infoestatutario_lista = None
        s2206_infoestatutario_form = None
        s2206_localtrabgeral_lista = None
        s2206_localtrabgeral_form = None
        s2206_localtrabdom_lista = None
        s2206_localtrabdom_form = None
        s2206_horcontratual_lista = None
        s2206_horcontratual_form = None
        s2206_filiacaosindical_lista = None
        s2206_filiacaosindical_form = None
        s2206_alvarajudicial_lista = None
        s2206_alvarajudicial_form = None
        s2206_observacoes_lista = None
        s2206_observacoes_form = None
        s2206_servpubl_lista = None
        s2206_servpubl_form = None

        if pk:

            s2206_evtaltcontratual = get_object_or_404(s2206evtAltContratual, id=pk)

            s2206_infoceletista_form = form_s2206_infoceletista(
                initial={'s2206_evtaltcontratual': s2206_evtaltcontratual})
            s2206_infoceletista_form.fields['s2206_evtaltcontratual'].widget.attrs['readonly'] = True
            s2206_infoceletista_lista = s2206infoCeletista.objects.\
                filter(s2206_evtaltcontratual_id=s2206_evtaltcontratual.id).all()
            s2206_infoestatutario_form = form_s2206_infoestatutario(
                initial={'s2206_evtaltcontratual': s2206_evtaltcontratual})
            s2206_infoestatutario_form.fields['s2206_evtaltcontratual'].widget.attrs['readonly'] = True
            s2206_infoestatutario_lista = s2206infoEstatutario.objects.\
                filter(s2206_evtaltcontratual_id=s2206_evtaltcontratual.id).all()
            s2206_localtrabgeral_form = form_s2206_localtrabgeral(
                initial={'s2206_evtaltcontratual': s2206_evtaltcontratual})
            s2206_localtrabgeral_form.fields['s2206_evtaltcontratual'].widget.attrs['readonly'] = True
            s2206_localtrabgeral_lista = s2206localTrabGeral.objects.\
                filter(s2206_evtaltcontratual_id=s2206_evtaltcontratual.id).all()
            s2206_localtrabdom_form = form_s2206_localtrabdom(
                initial={'s2206_evtaltcontratual': s2206_evtaltcontratual})
            s2206_localtrabdom_form.fields['s2206_evtaltcontratual'].widget.attrs['readonly'] = True
            s2206_localtrabdom_lista = s2206localTrabDom.objects.\
                filter(s2206_evtaltcontratual_id=s2206_evtaltcontratual.id).all()
            s2206_horcontratual_form = form_s2206_horcontratual(
                initial={'s2206_evtaltcontratual': s2206_evtaltcontratual})
            s2206_horcontratual_form.fields['s2206_evtaltcontratual'].widget.attrs['readonly'] = True
            s2206_horcontratual_lista = s2206horContratual.objects.\
                filter(s2206_evtaltcontratual_id=s2206_evtaltcontratual.id).all()
            s2206_filiacaosindical_form = form_s2206_filiacaosindical(
                initial={'s2206_evtaltcontratual': s2206_evtaltcontratual})
            s2206_filiacaosindical_form.fields['s2206_evtaltcontratual'].widget.attrs['readonly'] = True
            s2206_filiacaosindical_lista = s2206filiacaoSindical.objects.\
                filter(s2206_evtaltcontratual_id=s2206_evtaltcontratual.id).all()
            s2206_alvarajudicial_form = form_s2206_alvarajudicial(
                initial={'s2206_evtaltcontratual': s2206_evtaltcontratual})
            s2206_alvarajudicial_form.fields['s2206_evtaltcontratual'].widget.attrs['readonly'] = True
            s2206_alvarajudicial_lista = s2206alvaraJudicial.objects.\
                filter(s2206_evtaltcontratual_id=s2206_evtaltcontratual.id).all()
            s2206_observacoes_form = form_s2206_observacoes(
                initial={'s2206_evtaltcontratual': s2206_evtaltcontratual})
            s2206_observacoes_form.fields['s2206_evtaltcontratual'].widget.attrs['readonly'] = True
            s2206_observacoes_lista = s2206observacoes.objects.\
                filter(s2206_evtaltcontratual_id=s2206_evtaltcontratual.id).all()
            s2206_servpubl_form = form_s2206_servpubl(
                initial={'s2206_evtaltcontratual': s2206_evtaltcontratual})
            s2206_servpubl_form.fields['s2206_evtaltcontratual'].widget.attrs['readonly'] = True
            s2206_servpubl_lista = s2206servPubl.objects.\
                filter(s2206_evtaltcontratual_id=s2206_evtaltcontratual.id).all()

        else:

            s2206_evtaltcontratual = None

        tabelas_secundarias = []

        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s2206_evtaltcontratual').all()

        if not request.POST:
            request.session['return_page'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_totalizador': False,
            'controle_alteracoes': controle_alteracoes,
            's2206_evtaltcontratual': s2206_evtaltcontratual,
            's2206_evtaltcontratual_form': s2206_evtaltcontratual_form,

            's2206_infoceletista_form': s2206_infoceletista_form,
            's2206_infoceletista_lista': s2206_infoceletista_lista,
            's2206_infoestatutario_form': s2206_infoestatutario_form,
            's2206_infoestatutario_lista': s2206_infoestatutario_lista,
            's2206_localtrabgeral_form': s2206_localtrabgeral_form,
            's2206_localtrabgeral_lista': s2206_localtrabgeral_lista,
            's2206_localtrabdom_form': s2206_localtrabdom_form,
            's2206_localtrabdom_lista': s2206_localtrabdom_lista,
            's2206_horcontratual_form': s2206_horcontratual_form,
            's2206_horcontratual_lista': s2206_horcontratual_lista,
            's2206_filiacaosindical_form': s2206_filiacaosindical_form,
            's2206_filiacaosindical_lista': s2206_filiacaosindical_lista,
            's2206_alvarajudicial_form': s2206_alvarajudicial_form,
            's2206_alvarajudicial_lista': s2206_alvarajudicial_lista,
            's2206_observacoes_form': s2206_observacoes_form,
            's2206_observacoes_lista': s2206_observacoes_lista,
            's2206_servpubl_form': s2206_servpubl_form,
            's2206_servpubl_lista': s2206_servpubl_lista,
            'data': datetime.datetime.now(),
            'modulos': ['esocial', ],
            'paginas': ['s2206_evtaltcontratual', ],
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
        }

        if output == 'pdf':

            response = PDFTemplateResponse(
                request=request,
                template='s2206_evtaltcontratual_salvar.html',
                filename="s2206_evtaltcontratual.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True}, )

            return response

        elif output == 'xls':

            response = render_to_response('s2206_evtaltcontratual_salvar.html', context)
            filename = "s2206_evtaltcontratual.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 's2206_evtaltcontratual_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'tab': tab,
            'output': output,
            'modulos': ['esocial', ],
            'paginas': ['s2206_evtaltcontratual', ],
            'data': datetime.datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)