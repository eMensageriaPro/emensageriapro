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
from emensageriapro.r1000.forms import *
from emensageriapro.r1000.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.r1000.models import r1000inclusaosoftHouse
from emensageriapro.r1000.forms import form_r1000_inclusao_softhouse
from emensageriapro.r1000.models import r1000inclusaoinfoEFR
from emensageriapro.r1000.forms import form_r1000_inclusao_infoefr



@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO

    evento_dados = {}
    evento_dados['status'] = STATUS_EVENTO_CADASTRADO

    if pk:

        r1000_inclusao = get_object_or_404(r1000inclusao, id=pk)
        evento_dados = r1000_inclusao.evento()

    if request.user.has_perm('r1000.can_see_r1000inclusao'):

        if pk:

            r1000_inclusao_form = form_r1000_inclusao(
                request.POST or None,
                instance=r1000_inclusao)
                     
        else:

            r1000_inclusao_form = form_r1000_inclusao(request.POST or None)
                     
        if request.method == 'POST':

            if r1000_inclusao_form.is_valid():

                obj = r1000_inclusao_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                 
                if 'return_page' in request.session and request.session['return_page'] and 'r1000-inclusao' not in request.session['return_page']:

                    return HttpResponseRedirect(request.session['return_page'])

                if pk != obj.id:

                    return redirect(
                        'r1000_inclusao_salvar',
                        pk=obj.id)

            else:

                messages.error(request, u'Erro ao salvar!')

        r1000_inclusao_form = disabled_form_fields(
            r1000_inclusao_form,
            request.user.has_perm('r1000.change_r1000inclusao'))

        if pk:

            if evento_dados['status'] != STATUS_EVENTO_CADASTRADO:

                r1000_inclusao_form = disabled_form_fields(r1000_inclusao_form, 0)

        if output:

            r1000_inclusao_form = disabled_form_for_print(r1000_inclusao_form)


        r1000_inclusao_softhouse_lista = None
        r1000_inclusao_softhouse_form = None
        r1000_inclusao_infoefr_lista = None
        r1000_inclusao_infoefr_form = None

        if pk:

            r1000_inclusao = get_object_or_404(r1000inclusao, id=pk)

            r1000_inclusao_softhouse_form = form_r1000_inclusao_softhouse(
                initial={ 'r1000_inclusao': r1000_inclusao })
            r1000_inclusao_softhouse_form.fields['r1000_inclusao'].widget.attrs['readonly'] = True
            r1000_inclusao_softhouse_lista = r1000inclusaosoftHouse.objects.\
                filter(r1000_inclusao_id=r1000_inclusao.id).all()

            r1000_inclusao_infoefr_form = form_r1000_inclusao_infoefr(
                initial={ 'r1000_inclusao': r1000_inclusao })
            r1000_inclusao_infoefr_form.fields['r1000_inclusao'].widget.attrs['readonly'] = True
            r1000_inclusao_infoefr_lista = r1000inclusaoinfoEFR.objects.\
                filter(r1000_inclusao_id=r1000_inclusao.id).all()


        else:

            r1000_inclusao = None

        tabelas_secundarias = []

        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='r1000_inclusao').all()

        if not request.POST:
            request.session['return_page'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_dados': evento_dados,
            'controle_alteracoes': controle_alteracoes,
            'r1000_inclusao': r1000_inclusao,
            'r1000_inclusao_form': r1000_inclusao_form,
            'modulos': ['r1000', ],
            'paginas': ['r1000_inclusao', ],
            'r1000_inclusao_softhouse_form': r1000_inclusao_softhouse_form,
            'r1000_inclusao_softhouse_lista': r1000_inclusao_softhouse_lista,
            'r1000_inclusao_infoefr_form': r1000_inclusao_infoefr_form,
            'r1000_inclusao_infoefr_lista': r1000_inclusao_infoefr_lista,
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #r1000_inclusao_salvar_custom_variaveis_context#
        }

        if output == 'pdf':

            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='r1000_inclusao_salvar.html',
                filename="r1000_inclusao.pdf",
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

            response = render_to_response('r1000_inclusao_salvar.html', context)
            filename = "r1000_inclusao.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 'r1000_inclusao_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['r1000', ],
            'paginas': ['r1000_inclusao', ],
            'data': datetime.datetime.now(),
        }

        return render(request,
                      'permissao_negada.html',
                      context)