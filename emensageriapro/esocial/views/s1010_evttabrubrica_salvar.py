# eMensageriaAI #
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
from emensageriapro.s1010.models import s1010inclusao
from emensageriapro.s1010.forms import form_s1010_inclusao
from emensageriapro.s1010.models import s1010alteracao
from emensageriapro.s1010.forms import form_s1010_alteracao
from emensageriapro.s1010.models import s1010exclusao
from emensageriapro.s1010.forms import form_s1010_exclusao


@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    TP_AMB = config.ESOCIAL_TP_AMB

    if pk:

        s1010_evttabrubrica = get_object_or_404(s1010evtTabRubrica, id=pk)

    if request.user.has_perm('esocial.can_see_s1010evtTabRubrica'):

        if pk:

            s1010_evttabrubrica_form = form_s1010_evttabrubrica(request.POST or None, instance=s1010_evttabrubrica,
                                         initial={'ativo': True})
                     
        else:

            s1010_evttabrubrica_form = form_s1010_evttabrubrica(request.POST or None,
                                         initial={'versao': VERSAO_LAYOUT_ESOCIAL,
                                                  'status': STATUS_EVENTO_CADASTRADO,
                                                  'tpamb': TP_AMB,
                                                  'procemi': 1,
                                                  'verproc': VERSAO_EMENSAGERIA,
                                                  'ativo': True})
                              
        if request.method == 'POST':

            if s1010_evttabrubrica_form.is_valid():

                obj = s1010_evttabrubrica_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')

                if not pk:

                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj, 'esocial')
             
                if 'return_page' in request.session and request.session['return_page'] and 's1010-evttabrubrica' not in request.session['return_page']:

                    return HttpResponseRedirect(request.session['return_page'])

                if pk != obj.id:

                    return redirect(
                        's1010_evttabrubrica_salvar',
                        pk=obj.id)

            else:
                messages.error(request, u'Erro ao salvar!')

        s1010_evttabrubrica_form = disabled_form_fields(
             s1010_evttabrubrica_form,
             request.user.has_perm('esocial.change_s1010evtTabRubrica'))

        if pk:

            if s1010_evttabrubrica.status != 0:

                s1010_evttabrubrica_form = disabled_form_fields(s1010_evttabrubrica_form, False)

        for field in s1010_evttabrubrica_form.fields.keys():

            s1010_evttabrubrica_form.fields[field].widget.attrs['ng-model'] = 's1010_evttabrubrica_'+field

        if output:

            s1010_evttabrubrica_form = disabled_form_for_print(s1010_evttabrubrica_form)


        s1010_inclusao_lista = None
        s1010_inclusao_form = None
        s1010_alteracao_lista = None
        s1010_alteracao_form = None
        s1010_exclusao_lista = None
        s1010_exclusao_form = None

        if pk:

            s1010_evttabrubrica = get_object_or_404(s1010evtTabRubrica, id=pk)

            s1010_inclusao_form = form_s1010_inclusao(
                initial={'s1010_evttabrubrica': s1010_evttabrubrica})
            s1010_inclusao_form.fields['s1010_evttabrubrica'].widget.attrs['readonly'] = True
            s1010_inclusao_lista = s1010inclusao.objects.\
                filter(s1010_evttabrubrica_id=s1010_evttabrubrica.id).all()
            s1010_alteracao_form = form_s1010_alteracao(
                initial={'s1010_evttabrubrica': s1010_evttabrubrica})
            s1010_alteracao_form.fields['s1010_evttabrubrica'].widget.attrs['readonly'] = True
            s1010_alteracao_lista = s1010alteracao.objects.\
                filter(s1010_evttabrubrica_id=s1010_evttabrubrica.id).all()
            s1010_exclusao_form = form_s1010_exclusao(
                initial={'s1010_evttabrubrica': s1010_evttabrubrica})
            s1010_exclusao_form.fields['s1010_evttabrubrica'].widget.attrs['readonly'] = True
            s1010_exclusao_lista = s1010exclusao.objects.\
                filter(s1010_evttabrubrica_id=s1010_evttabrubrica.id).all()

        else:

            s1010_evttabrubrica = None

        tabelas_secundarias = []

        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s1010_evttabrubrica').all()

        if not request.POST:
            request.session['return_page'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_totalizador': False,
            'controle_alteracoes': controle_alteracoes,
            's1010_evttabrubrica': s1010_evttabrubrica,
            's1010_evttabrubrica_form': s1010_evttabrubrica_form,

            's1010_inclusao_form': s1010_inclusao_form,
            's1010_inclusao_lista': s1010_inclusao_lista,
            's1010_alteracao_form': s1010_alteracao_form,
            's1010_alteracao_lista': s1010_alteracao_lista,
            's1010_exclusao_form': s1010_exclusao_form,
            's1010_exclusao_lista': s1010_exclusao_lista,
            'data': datetime.datetime.now(),
            'modulos': ['esocial', ],
            'paginas': ['s1010_evttabrubrica', ],
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
        }

        if output == 'pdf':

            response = PDFTemplateResponse(
                request=request,
                template='s1010_evttabrubrica_salvar.html',
                filename="s1010_evttabrubrica.pdf",
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

            response = render_to_response('s1010_evttabrubrica_salvar.html', context)
            filename = "s1010_evttabrubrica.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 's1010_evttabrubrica_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'tab': tab,
            'output': output,
            'modulos': ['esocial', ],
            'paginas': ['s1010_evttabrubrica', ],
            'data': datetime.datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)