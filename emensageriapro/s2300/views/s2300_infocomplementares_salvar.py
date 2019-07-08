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


import datetime
import json
import base64
from django.contrib import messages
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from django.forms.models import model_to_dict
from wkhtmltopdf.views import PDFTemplateResponse
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from emensageriapro.padrao import *
from emensageriapro.s2300.forms import *
from emensageriapro.s2300.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s2300.models import s2300cargoFuncao
from emensageriapro.s2300.forms import form_s2300_cargofuncao
from emensageriapro.s2300.models import s2300remuneracao
from emensageriapro.s2300.forms import form_s2300_remuneracao
from emensageriapro.s2300.models import s2300fgts
from emensageriapro.s2300.forms import form_s2300_fgts
from emensageriapro.s2300.models import s2300infoDirigenteSindical
from emensageriapro.s2300.forms import form_s2300_infodirigentesindical
from emensageriapro.s2300.models import s2300infoTrabCedido
from emensageriapro.s2300.forms import form_s2300_infotrabcedido
from emensageriapro.s2300.models import s2300infoEstagiario
from emensageriapro.s2300.forms import form_s2300_infoestagiario



@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO

    evento_dados = {}
    evento_dados['status'] = STATUS_EVENTO_CADASTRADO

    if pk:

        s2300_infocomplementares = get_object_or_404(s2300infoComplementares, id=pk)
        evento_dados = s2300_infocomplementares.evento()

    if request.user.has_perm('s2300.can_see_s2300infoComplementares'):

        if pk:

            s2300_infocomplementares_form = form_s2300_infocomplementares(
                request.POST or None,
                instance=s2300_infocomplementares)
                     
        else:

            s2300_infocomplementares_form = form_s2300_infocomplementares(request.POST or None)
                     
        if request.method == 'POST':

            if s2300_infocomplementares_form.is_valid():

                obj = s2300_infocomplementares_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                 
                if 's2300-infocomplementares' not in request.session['return']:

                    return HttpResponseRedirect(request.session['return'])

                if pk != obj.id:

                    return redirect(
                        's2300_infocomplementares_salvar',
                        pk=obj.id)

            else:

                messages.error(request, u'Erro ao salvar!')

        s2300_infocomplementares_form = disabled_form_fields(
            s2300_infocomplementares_form,
            request.user.has_perm('s2300.change_s2300infoComplementares'))

        if pk:

            if evento_dados['status'] != STATUS_EVENTO_CADASTRADO:

                s2300_infocomplementares_form = disabled_form_fields(s2300_infocomplementares_form, 0)

        if output:

            s2300_infocomplementares_form = disabled_form_for_print(s2300_infocomplementares_form)


        s2300_cargofuncao_lista = None
        s2300_cargofuncao_form = None
        s2300_remuneracao_lista = None
        s2300_remuneracao_form = None
        s2300_fgts_lista = None
        s2300_fgts_form = None
        s2300_infodirigentesindical_lista = None
        s2300_infodirigentesindical_form = None
        s2300_infotrabcedido_lista = None
        s2300_infotrabcedido_form = None
        s2300_infoestagiario_lista = None
        s2300_infoestagiario_form = None

        if pk:

            s2300_infocomplementares = get_object_or_404(s2300infoComplementares, id=pk)

            s2300_cargofuncao_form = form_s2300_cargofuncao(
                initial={ 's2300_infocomplementares': s2300_infocomplementares })
            s2300_cargofuncao_form.fields['s2300_infocomplementares'].widget.attrs['readonly'] = True
            s2300_cargofuncao_lista = s2300cargoFuncao.objects.\
                filter(s2300_infocomplementares_id=s2300_infocomplementares.id).all()

            s2300_remuneracao_form = form_s2300_remuneracao(
                initial={ 's2300_infocomplementares': s2300_infocomplementares })
            s2300_remuneracao_form.fields['s2300_infocomplementares'].widget.attrs['readonly'] = True
            s2300_remuneracao_lista = s2300remuneracao.objects.\
                filter(s2300_infocomplementares_id=s2300_infocomplementares.id).all()

            s2300_fgts_form = form_s2300_fgts(
                initial={ 's2300_infocomplementares': s2300_infocomplementares })
            s2300_fgts_form.fields['s2300_infocomplementares'].widget.attrs['readonly'] = True
            s2300_fgts_lista = s2300fgts.objects.\
                filter(s2300_infocomplementares_id=s2300_infocomplementares.id).all()

            s2300_infodirigentesindical_form = form_s2300_infodirigentesindical(
                initial={ 's2300_infocomplementares': s2300_infocomplementares })
            s2300_infodirigentesindical_form.fields['s2300_infocomplementares'].widget.attrs['readonly'] = True
            s2300_infodirigentesindical_lista = s2300infoDirigenteSindical.objects.\
                filter(s2300_infocomplementares_id=s2300_infocomplementares.id).all()

            s2300_infotrabcedido_form = form_s2300_infotrabcedido(
                initial={ 's2300_infocomplementares': s2300_infocomplementares })
            s2300_infotrabcedido_form.fields['s2300_infocomplementares'].widget.attrs['readonly'] = True
            s2300_infotrabcedido_lista = s2300infoTrabCedido.objects.\
                filter(s2300_infocomplementares_id=s2300_infocomplementares.id).all()

            s2300_infoestagiario_form = form_s2300_infoestagiario(
                initial={ 's2300_infocomplementares': s2300_infocomplementares })
            s2300_infoestagiario_form.fields['s2300_infocomplementares'].widget.attrs['readonly'] = True
            s2300_infoestagiario_lista = s2300infoEstagiario.objects.\
                filter(s2300_infocomplementares_id=s2300_infocomplementares.id).all()


        else:

            s2300_infocomplementares = None

        tabelas_secundarias = []

        #if tab or 's2300_infocomplementares' in request.session['return_page']:
        #
        #    request.session['return_pk'] = pk
        #    request.session['return_tab'] = tab
        #    request.session['return_page'] = 's2300_infocomplementares_salvar'

        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s2300_infocomplementares').all()

        if not request.POST:
            request.session['return'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_dados': evento_dados,
            'controle_alteracoes': controle_alteracoes,
            's2300_infocomplementares': s2300_infocomplementares,
            's2300_infocomplementares_form': s2300_infocomplementares_form,
            'modulos': ['s2300', ],
            'paginas': ['s2300_infocomplementares', ],
            's2300_cargofuncao_form': s2300_cargofuncao_form,
            's2300_cargofuncao_lista': s2300_cargofuncao_lista,
            's2300_remuneracao_form': s2300_remuneracao_form,
            's2300_remuneracao_lista': s2300_remuneracao_lista,
            's2300_fgts_form': s2300_fgts_form,
            's2300_fgts_lista': s2300_fgts_lista,
            's2300_infodirigentesindical_form': s2300_infodirigentesindical_form,
            's2300_infodirigentesindical_lista': s2300_infodirigentesindical_lista,
            's2300_infotrabcedido_form': s2300_infotrabcedido_form,
            's2300_infotrabcedido_lista': s2300_infotrabcedido_lista,
            's2300_infoestagiario_form': s2300_infoestagiario_form,
            's2300_infoestagiario_lista': s2300_infoestagiario_lista,
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #s2300_infocomplementares_salvar_custom_variaveis_context#
        }

        if output == 'pdf':

            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='s2300_infocomplementares_salvar.html',
                filename="s2300_infocomplementares.pdf",
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

            from django.shortcuts import render_to_response

            response = render_to_response('s2300_infocomplementares_salvar.html', context)
            filename = "s2300_infocomplementares.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 's2300_infocomplementares_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['s2300', ],
            'paginas': ['s2300_infocomplementares', ],
            'data': datetime.datetime.now(),
        }

        return render(request,
                      'permissao_negada.html',
                      context)