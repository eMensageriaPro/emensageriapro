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
from emensageriapro.s2299.forms import *
from emensageriapro.s2299.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s2299.models import s2299infoPerApurdetVerbas
from emensageriapro.s2299.forms import form_s2299_infoperapur_detverbas
from emensageriapro.s2299.models import s2299infoPerApurinfoSaudeColet
from emensageriapro.s2299.forms import form_s2299_infoperapur_infosaudecolet
from emensageriapro.s2299.models import s2299infoPerApurinfoAgNocivo
from emensageriapro.s2299.forms import form_s2299_infoperapur_infoagnocivo
from emensageriapro.s2299.models import s2299infoPerApurinfoSimples
from emensageriapro.s2299.forms import form_s2299_infoperapur_infosimples



@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO

    evento_dados = {}
    evento_dados['status'] = STATUS_EVENTO_CADASTRADO

    if pk:

        s2299_infoperapur_ideestablot = get_object_or_404(s2299infoPerApurideEstabLot, id=pk)
        evento_dados = s2299_infoperapur_ideestablot.evento()

    if request.user.has_perm('s2299.can_see_s2299infoPerApurideEstabLot'):

        if pk:

            s2299_infoperapur_ideestablot_form = form_s2299_infoperapur_ideestablot(
                request.POST or None,
                instance=s2299_infoperapur_ideestablot)
                     
        else:

            s2299_infoperapur_ideestablot_form = form_s2299_infoperapur_ideestablot(request.POST or None)
                     
        if request.method == 'POST':

            if s2299_infoperapur_ideestablot_form.is_valid():

                obj = s2299_infoperapur_ideestablot_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                 
                if 'return_page' in request.session and request.session['return_page'] and 's2299-infoperapur-ideestablot' not in request.session['return_page']:

                    return HttpResponseRedirect(request.session['return_page'])

                if pk != obj.id:

                    return redirect(
                        's2299_infoperapur_ideestablot_salvar',
                        pk=obj.id)

            else:

                messages.error(request, u'Erro ao salvar!')

        s2299_infoperapur_ideestablot_form = disabled_form_fields(
            s2299_infoperapur_ideestablot_form,
            request.user.has_perm('s2299.change_s2299infoPerApurideEstabLot'))

        if pk:

            if evento_dados['status'] != STATUS_EVENTO_CADASTRADO:

                s2299_infoperapur_ideestablot_form = disabled_form_fields(s2299_infoperapur_ideestablot_form, 0)

        if output:

            s2299_infoperapur_ideestablot_form = disabled_form_for_print(s2299_infoperapur_ideestablot_form)


        s2299_infoperapur_detverbas_lista = None
        s2299_infoperapur_detverbas_form = None
        s2299_infoperapur_infosaudecolet_lista = None
        s2299_infoperapur_infosaudecolet_form = None
        s2299_infoperapur_infoagnocivo_lista = None
        s2299_infoperapur_infoagnocivo_form = None
        s2299_infoperapur_infosimples_lista = None
        s2299_infoperapur_infosimples_form = None

        if pk:

            s2299_infoperapur_ideestablot = get_object_or_404(s2299infoPerApurideEstabLot, id=pk)

            s2299_infoperapur_detverbas_form = form_s2299_infoperapur_detverbas(
                initial={ 's2299_infoperapur_ideestablot': s2299_infoperapur_ideestablot })
            s2299_infoperapur_detverbas_form.fields['s2299_infoperapur_ideestablot'].widget.attrs['readonly'] = True
            s2299_infoperapur_detverbas_lista = s2299infoPerApurdetVerbas.objects.\
                filter(s2299_infoperapur_ideestablot_id=s2299_infoperapur_ideestablot.id).all()

            s2299_infoperapur_infosaudecolet_form = form_s2299_infoperapur_infosaudecolet(
                initial={ 's2299_infoperapur_ideestablot': s2299_infoperapur_ideestablot })
            s2299_infoperapur_infosaudecolet_form.fields['s2299_infoperapur_ideestablot'].widget.attrs['readonly'] = True
            s2299_infoperapur_infosaudecolet_lista = s2299infoPerApurinfoSaudeColet.objects.\
                filter(s2299_infoperapur_ideestablot_id=s2299_infoperapur_ideestablot.id).all()

            s2299_infoperapur_infoagnocivo_form = form_s2299_infoperapur_infoagnocivo(
                initial={ 's2299_infoperapur_ideestablot': s2299_infoperapur_ideestablot })
            s2299_infoperapur_infoagnocivo_form.fields['s2299_infoperapur_ideestablot'].widget.attrs['readonly'] = True
            s2299_infoperapur_infoagnocivo_lista = s2299infoPerApurinfoAgNocivo.objects.\
                filter(s2299_infoperapur_ideestablot_id=s2299_infoperapur_ideestablot.id).all()

            s2299_infoperapur_infosimples_form = form_s2299_infoperapur_infosimples(
                initial={ 's2299_infoperapur_ideestablot': s2299_infoperapur_ideestablot })
            s2299_infoperapur_infosimples_form.fields['s2299_infoperapur_ideestablot'].widget.attrs['readonly'] = True
            s2299_infoperapur_infosimples_lista = s2299infoPerApurinfoSimples.objects.\
                filter(s2299_infoperapur_ideestablot_id=s2299_infoperapur_ideestablot.id).all()


        else:

            s2299_infoperapur_ideestablot = None

        tabelas_secundarias = []

        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s2299_infoperapur_ideestablot').all()

        if not request.POST:
            request.session['return_page'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_dados': evento_dados,
            'controle_alteracoes': controle_alteracoes,
            's2299_infoperapur_ideestablot': s2299_infoperapur_ideestablot,
            's2299_infoperapur_ideestablot_form': s2299_infoperapur_ideestablot_form,
            'modulos': ['s2299', ],
            'paginas': ['s2299_infoperapur_ideestablot', ],
            's2299_infoperapur_detverbas_form': s2299_infoperapur_detverbas_form,
            's2299_infoperapur_detverbas_lista': s2299_infoperapur_detverbas_lista,
            's2299_infoperapur_infosaudecolet_form': s2299_infoperapur_infosaudecolet_form,
            's2299_infoperapur_infosaudecolet_lista': s2299_infoperapur_infosaudecolet_lista,
            's2299_infoperapur_infoagnocivo_form': s2299_infoperapur_infoagnocivo_form,
            's2299_infoperapur_infoagnocivo_lista': s2299_infoperapur_infoagnocivo_lista,
            's2299_infoperapur_infosimples_form': s2299_infoperapur_infosimples_form,
            's2299_infoperapur_infosimples_lista': s2299_infoperapur_infosimples_lista,
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #s2299_infoperapur_ideestablot_salvar_custom_variaveis_context#
        }

        if output == 'pdf':

            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='s2299_infoperapur_ideestablot_salvar.html',
                filename="s2299_infoperapur_ideestablot.pdf",
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

            response = render_to_response('s2299_infoperapur_ideestablot_salvar.html', context)
            filename = "s2299_infoperapur_ideestablot.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 's2299_infoperapur_ideestablot_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['s2299', ],
            'paginas': ['s2299_infoperapur_ideestablot', ],
            'data': datetime.datetime.now(),
        }

        return render(request,
                      'permissao_negada.html',
                      context)