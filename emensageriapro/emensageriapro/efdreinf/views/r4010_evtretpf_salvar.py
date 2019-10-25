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
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.r4010.models import r4010idePgto
from emensageriapro.r4010.forms import form_r4010_idepgto
from emensageriapro.r4010.models import r4010ideOpSaude
from emensageriapro.r4010.forms import form_r4010_ideopsaude


@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_EFDREINF
    TP_AMB = config.EFDREINF_TP_AMB

    if pk:

        r4010_evtretpf = get_object_or_404(r4010evtRetPF, id=pk)

    if request.user.has_perm('efdreinf.can_see_r4010evtRetPF'):

        if pk:

            r4010_evtretpf_form = form_r4010_evtretpf(request.POST or None, instance=r4010_evtretpf,
                                         initial={'ativo': True})
                     
        else:

            r4010_evtretpf_form = form_r4010_evtretpf(request.POST or None,
                                         initial={'versao': VERSAO_LAYOUT_EFDREINF,
                                                  'status': STATUS_EVENTO_CADASTRADO,
                                                  'tpamb': TP_AMB,
                                                  'procemi': 1,
                                                  'verproc': VERSAO_EMENSAGERIA,
                                                  'ativo': True})
                              
        if request.method == 'POST':

            if r4010_evtretpf_form.is_valid():

                obj = r4010_evtretpf_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')

                if not pk:

                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj, 'efdreinf')
             
                if 'return_page' in request.session and request.session['return_page'] and 'r4010-evtretpf' not in request.session['return_page']:

                    return HttpResponseRedirect(request.session['return_page'])

                if pk != obj.id:

                    return redirect(
                        'r4010_evtretpf_salvar',
                        pk=obj.id)

            else:
                messages.error(request, u'Erro ao salvar!')

        r4010_evtretpf_form = disabled_form_fields(
             r4010_evtretpf_form,
             request.user.has_perm('efdreinf.change_r4010evtRetPF'))

        if pk:

            if r4010_evtretpf.status != 0:

                r4010_evtretpf_form = disabled_form_fields(r4010_evtretpf_form, False)

        for field in r4010_evtretpf_form.fields.keys():

            r4010_evtretpf_form.fields[field].widget.attrs['ng-model'] = 'r4010_evtretpf_'+field

        if output:

            r4010_evtretpf_form = disabled_form_for_print(r4010_evtretpf_form)


        r4010_idepgto_lista = None
        r4010_idepgto_form = None
        r4010_ideopsaude_lista = None
        r4010_ideopsaude_form = None

        if pk:

            r4010_evtretpf = get_object_or_404(r4010evtRetPF, id=pk)

            r4010_idepgto_form = form_r4010_idepgto(
                initial={'r4010_evtretpf': r4010_evtretpf})
            r4010_idepgto_form.fields['r4010_evtretpf'].widget.attrs['readonly'] = True
            r4010_idepgto_lista = r4010idePgto.objects.\
                filter(r4010_evtretpf_id=r4010_evtretpf.id).all()
            r4010_ideopsaude_form = form_r4010_ideopsaude(
                initial={'r4010_evtretpf': r4010_evtretpf})
            r4010_ideopsaude_form.fields['r4010_evtretpf'].widget.attrs['readonly'] = True
            r4010_ideopsaude_lista = r4010ideOpSaude.objects.\
                filter(r4010_evtretpf_id=r4010_evtretpf.id).all()

        else:

            r4010_evtretpf = None

        tabelas_secundarias = []

        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='r4010_evtretpf').all()

        if not request.POST:
            request.session['return_page'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_totalizador': False,
            'controle_alteracoes': controle_alteracoes,
            'r4010_evtretpf': r4010_evtretpf,
            'r4010_evtretpf_form': r4010_evtretpf_form,

            'r4010_idepgto_form': r4010_idepgto_form,
            'r4010_idepgto_lista': r4010_idepgto_lista,
            'r4010_ideopsaude_form': r4010_ideopsaude_form,
            'r4010_ideopsaude_lista': r4010_ideopsaude_lista,
            'data': datetime.datetime.now(),
            'modulos': ['efdreinf', ],
            'paginas': ['r4010_evtretpf', ],
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
        }

        if output == 'pdf':

            response = PDFTemplateResponse(
                request=request,
                template='r4010_evtretpf_salvar.html',
                filename="r4010_evtretpf.pdf",
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

            response = render_to_response('r4010_evtretpf_salvar.html', context)
            filename = "r4010_evtretpf.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 'r4010_evtretpf_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'tab': tab,
            'output': output,
            'modulos': ['efdreinf', ],
            'paginas': ['r4010_evtretpf', ],
            'data': datetime.datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)