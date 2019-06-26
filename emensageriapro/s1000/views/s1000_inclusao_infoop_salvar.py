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
from emensageriapro.s1000.forms import *
from emensageriapro.s1000.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s1000.models import s1000inclusaoinfoEFR
from emensageriapro.s1000.forms import form_s1000_inclusao_infoefr
from emensageriapro.s1000.models import s1000inclusaoinfoEnte
from emensageriapro.s1000.forms import form_s1000_inclusao_infoente



@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO

    evento_dados = {}
    evento_dados['status'] = STATUS_EVENTO_CADASTRADO

    if pk:

        s1000_inclusao_infoop = get_object_or_404(s1000inclusaoinfoOP, id=pk)
        evento_dados = s1000_inclusao_infoop.evento()

    if request.user.has_perm('s1000.can_see_s1000inclusaoinfoOP'):

        if pk:

            s1000_inclusao_infoop_form = form_s1000_inclusao_infoop(
                request.POST or None,
                instance=s1000_inclusao_infoop)
                     
        else:

            s1000_inclusao_infoop_form = form_s1000_inclusao_infoop(request.POST or None)
                     
        if request.method == 'POST':

            if s1000_inclusao_infoop_form.is_valid():

                obj = s1000_inclusao_infoop_form.save(request=request)
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
                #        's1000_inclusao_infoop',
                #        obj.id,
                #        request.user.id, 1)
                #
                #else:
                #
                #    gravar_auditoria(
                #        json.dumps(
                #            model_to_dict(s1000_inclusao_infoop),
                #            indent=4,
                #            sort_keys=True,
                #            default=str),
                #        json.dumps(
                #            model_to_dict(obj),
                #            indent=4,
                #            sort_keys=True,
                #            default=str),
                #        's1000_inclusao_infoop',
                #        pk,
                #        request.user.id, 2)
                 
                if request.session['return_page'] not in (
                    's1000_inclusao_infoop_apagar',
                    's1000_inclusao_infoop_salvar',
                    's1000_inclusao_infoop'):

                    return redirect(
                        request.session['return_page'],
                        pk=request.session['return_pk'])

                if pk != obj.id:

                    return redirect(
                        's1000_inclusao_infoop_salvar',
                        pk=obj.id)

            else:

                messages.error(request, u'Erro ao salvar!')

        s1000_inclusao_infoop_form = disabled_form_fields(
            s1000_inclusao_infoop_form,
            request.user.has_perm('s1000.change_s1000inclusaoinfoOP'))

        if pk:

            if evento_dados['status'] != STATUS_EVENTO_CADASTRADO:

                s1000_inclusao_infoop_form = disabled_form_fields(s1000_inclusao_infoop_form, 0)

        if output:

            s1000_inclusao_infoop_form = disabled_form_for_print(s1000_inclusao_infoop_form)


        s1000_inclusao_infoefr_lista = None
        s1000_inclusao_infoefr_form = None
        s1000_inclusao_infoente_lista = None
        s1000_inclusao_infoente_form = None

        if pk:

            s1000_inclusao_infoop = get_object_or_404(s1000inclusaoinfoOP, id=pk)

            s1000_inclusao_infoefr_form = form_s1000_inclusao_infoefr(
                initial={ 's1000_inclusao_infoop': s1000_inclusao_infoop })
            s1000_inclusao_infoefr_form.fields['s1000_inclusao_infoop'].widget.attrs['readonly'] = True
            s1000_inclusao_infoefr_lista = s1000inclusaoinfoEFR.objects.\
                filter(s1000_inclusao_infoop_id=s1000_inclusao_infoop.id).all()

            s1000_inclusao_infoente_form = form_s1000_inclusao_infoente(
                initial={ 's1000_inclusao_infoop': s1000_inclusao_infoop })
            s1000_inclusao_infoente_form.fields['s1000_inclusao_infoop'].widget.attrs['readonly'] = True
            s1000_inclusao_infoente_lista = s1000inclusaoinfoEnte.objects.\
                filter(s1000_inclusao_infoop_id=s1000_inclusao_infoop.id).all()


        else:

            s1000_inclusao_infoop = None

        tabelas_secundarias = []

        if tab or 's1000_inclusao_infoop' in request.session['return_page']:

            request.session['return_pk'] = pk
            request.session['return_tab'] = tab
            request.session['return_page'] = 's1000_inclusao_infoop_salvar'

        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s1000_inclusao_infoop').all()

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_dados': evento_dados,
            'controle_alteracoes': controle_alteracoes,
            's1000_inclusao_infoop': s1000_inclusao_infoop,
            's1000_inclusao_infoop_form': s1000_inclusao_infoop_form,
            'modulos': ['s1000', ],
            'paginas': ['s1000_inclusao_infoop', ],
            's1000_inclusao_infoefr_form': s1000_inclusao_infoefr_form,
            's1000_inclusao_infoefr_lista': s1000_inclusao_infoefr_lista,
            's1000_inclusao_infoente_form': s1000_inclusao_infoente_form,
            's1000_inclusao_infoente_lista': s1000_inclusao_infoente_lista,
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #s1000_inclusao_infoop_salvar_custom_variaveis_context#
        }

        if output == 'pdf':

            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='s1000_inclusao_infoop_salvar.html',
                filename="s1000_inclusao_infoop.pdf",
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

            response = render_to_response('s1000_inclusao_infoop_salvar.html', context)
            filename = "s1000_inclusao_infoop.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 's1000_inclusao_infoop_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['s1000', ],
            'paginas': ['s1000_inclusao_infoop', ],
            'data': datetime.datetime.now(),
        }

        return render(request,
                      'permissao_negada.html',
                      context)