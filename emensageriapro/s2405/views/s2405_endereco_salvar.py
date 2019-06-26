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
from emensageriapro.s2405.forms import *
from emensageriapro.s2405.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s2405.models import s2405brasil
from emensageriapro.s2405.forms import form_s2405_brasil
from emensageriapro.s2405.models import s2405exterior
from emensageriapro.s2405.forms import form_s2405_exterior



@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO

    evento_dados = {}
    evento_dados['status'] = STATUS_EVENTO_CADASTRADO

    if pk:

        s2405_endereco = get_object_or_404(s2405endereco, id=pk)
        evento_dados = s2405_endereco.evento()

    if request.user.has_perm('s2405.can_see_s2405endereco'):

        if pk:

            s2405_endereco_form = form_s2405_endereco(
                request.POST or None,
                instance=s2405_endereco)
                     
        else:

            s2405_endereco_form = form_s2405_endereco(request.POST or None)
                     
        if request.method == 'POST':

            if s2405_endereco_form.is_valid():

                obj = s2405_endereco_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')

                #if not pk:
                #
                #    gravar_auditoria(
                #        '{}',
                #        json.dumps(
                #            model_to_dict(obj),
                #            indent=4,
                #            sort_keys=True,
                #            default=str),
                #        's2405_endereco',
                #        obj.id,
                #        request.user.id, 1)
                #
                #else:
                #
                #    gravar_auditoria(
                #        json.dumps(
                #            model_to_dict(s2405_endereco),
                #            indent=4,
                #            sort_keys=True,
                #            default=str),
                #        json.dumps(
                #            model_to_dict(obj),
                #            indent=4,
                #            sort_keys=True,
                #            default=str),
                #        's2405_endereco',
                #        pk,
                #        request.user.id, 2)
                 
                if request.session['return_page'] not in (
                    's2405_endereco_apagar',
                    's2405_endereco_salvar',
                    's2405_endereco'):

                    return redirect(
                        request.session['return_page'],
                        pk=request.session['return_pk'])

                if pk != obj.id:

                    return redirect(
                        's2405_endereco_salvar',
                        pk=obj.id)

            else:

                messages.error(request, u'Erro ao salvar!')

        s2405_endereco_form = disabled_form_fields(
            s2405_endereco_form,
            request.user.has_perm('s2405.change_s2405endereco'))

        if pk:

            if evento_dados['status'] != STATUS_EVENTO_CADASTRADO:

                s2405_endereco_form = disabled_form_fields(s2405_endereco_form, 0)

        if output:

            s2405_endereco_form = disabled_form_for_print(s2405_endereco_form)


        s2405_brasil_lista = None
        s2405_brasil_form = None
        s2405_exterior_lista = None
        s2405_exterior_form = None

        if pk:

            s2405_endereco = get_object_or_404(s2405endereco, id=pk)

            s2405_brasil_form = form_s2405_brasil(
                initial={ 's2405_endereco': s2405_endereco })
            s2405_brasil_form.fields['s2405_endereco'].widget.attrs['readonly'] = True
            s2405_brasil_lista = s2405brasil.objects.\
                filter(s2405_endereco_id=s2405_endereco.id).all()

            s2405_exterior_form = form_s2405_exterior(
                initial={ 's2405_endereco': s2405_endereco })
            s2405_exterior_form.fields['s2405_endereco'].widget.attrs['readonly'] = True
            s2405_exterior_lista = s2405exterior.objects.\
                filter(s2405_endereco_id=s2405_endereco.id).all()


        else:

            s2405_endereco = None

        tabelas_secundarias = []

        if tab or 's2405_endereco' in request.session['return_page']:

            request.session['return_pk'] = pk
            request.session['return_tab'] = tab
            request.session['return_page'] = 's2405_endereco_salvar'

        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s2405_endereco').all()

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_dados': evento_dados,
            'controle_alteracoes': controle_alteracoes,
            's2405_endereco': s2405_endereco,
            's2405_endereco_form': s2405_endereco_form,
            'modulos': ['s2405', ],
            'paginas': ['s2405_endereco', ],
            's2405_brasil_form': s2405_brasil_form,
            's2405_brasil_lista': s2405_brasil_lista,
            's2405_exterior_form': s2405_exterior_form,
            's2405_exterior_lista': s2405_exterior_lista,
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #s2405_endereco_salvar_custom_variaveis_context#
        }

        if output == 'pdf':

            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='s2405_endereco_salvar.html',
                filename="s2405_endereco.pdf",
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

            response = render_to_response('s2405_endereco_salvar.html', context)
            filename = "s2405_endereco.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 's2405_endereco_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['s2405', ],
            'paginas': ['s2405_endereco', ],
            'data': datetime.datetime.now(),
        }

        return render(request,
                      'permissao_negada.html',
                      context)