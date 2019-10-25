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
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from django.forms.models import model_to_dict
from wkhtmltopdf.views import PDFTemplateResponse
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from emensageriapro.padrao import *
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
from emensageriapro.mensageiro.forms import form_importacao_arquivos_eventos


@login_required
def salvar(request, pk=None, tab='master', output=None):

    if pk:

        importacao_arquivos = get_object_or_404(ImportacaoArquivos, id=pk)

    if request.user.has_perm('mensageiro.can_see_ImportacaoArquivos'):

        if pk:

            importacao_arquivos_form = form_importacao_arquivos(request.POST or None, instance=importacao_arquivos)

        else:

            importacao_arquivos_form = form_importacao_arquivos(request.POST or None)

        if request.method == 'POST':

            if importacao_arquivos_form.is_valid():

                #importacao_arquivos_campos_multiple_passo1


                obj = importacao_arquivos_form.save(request=request)
                messages.success(request, 'Salvo com sucesso!')
                #importacao_arquivos_campos_multiple_passo2

                if 'return_page' in request.session and request.session['return_page'] and 'importacao-arquivos' not in request.session['return_page']:

                    return HttpResponseRedirect(request.session['return_page'])

                if pk != obj.id:

                    return redirect(
                        'importacao_arquivos_salvar',
                        pk=obj.id)

            else:

                messages.error(request, 'Erro ao salvar!')

        importacao_arquivos_form = disabled_form_fields(importacao_arquivos_form, request.user.has_perm('mensageiro.change_ImportacaoArquivos'))
        #importacao_arquivos_campos_multiple_passo3

        if output:

            importacao_arquivos_form = disabled_form_for_print(importacao_arquivos_form)


        importacao_arquivos_eventos_lista = None
        importacao_arquivos_eventos_form = None

        if pk:

            importacao_arquivos = get_object_or_404(ImportacaoArquivos, id=pk)

            importacao_arquivos_eventos_form = form_importacao_arquivos_eventos(
                initial={ 'importacao_arquivos': importacao_arquivos })
            importacao_arquivos_eventos_form.fields['importacao_arquivos'].widget.attrs['readonly'] = True
            importacao_arquivos_eventos_lista = ImportacaoArquivosEventos.objects.\
                filter(importacao_arquivos_id=importacao_arquivos.id).all()


        else:

            importacao_arquivos = None

        #importacao_arquivos_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]

        if not request.POST:
            request.session['return_page'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'importacao_arquivos': importacao_arquivos,
            'importacao_arquivos_form': importacao_arquivos_form,
            'importacao_arquivos_eventos_form': importacao_arquivos_eventos_form,
            'importacao_arquivos_eventos_lista': importacao_arquivos_eventos_lista,
            'modulos': ['mensageiro', ],
            'paginas': ['importacao_arquivos', ],
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            #importacao_arquivos_salvar_custom_variaveis_context#
        }

        if output == 'pdf':

            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='importacao_arquivos_salvar.html',
                filename="importacao_arquivos.pdf",
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
                             "no-stop-slow-scripts": True})
         
            return response

        elif output == 'xls':

            from django.shortcuts import render_to_response

            response = render_to_response('importacao_arquivos_salvar.html', context)
            filename = "importacao_arquivos.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 'importacao_arquivos_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['mensageiro', ],
            'paginas': ['importacao_arquivos', ],
            'data': datetime.datetime.now(),
        }

        return render(request,
            'permissao_negada.html',
            context)