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
from emensageriapro.r2010.forms import *
from emensageriapro.r2010.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.r2010.models import r2010infoTpServ
from emensageriapro.r2010.forms import form_r2010_infotpserv



@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO

    evento_dados = {}
    evento_dados['status'] = STATUS_EVENTO_CADASTRADO

    if pk:

        r2010_nfs = get_object_or_404(r2010nfs, id=pk)
        evento_dados = r2010_nfs.evento()

    if request.user.has_perm('r2010.can_see_r2010nfs'):

        if pk:

            r2010_nfs_form = form_r2010_nfs(
                request.POST or None,
                instance=r2010_nfs)
                     
        else:

            r2010_nfs_form = form_r2010_nfs(request.POST or None)
                     
        if request.method == 'POST':

            if r2010_nfs_form.is_valid():

                obj = r2010_nfs_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                 
                if 'return_page' in request.session and request.session['return_page'] and 'r2010-nfs' not in request.session['return_page']:

                    return HttpResponseRedirect(request.session['return_page'])

                if pk != obj.id:

                    return redirect(
                        'r2010_nfs_salvar',
                        pk=obj.id)

            else:

                messages.error(request, u'Erro ao salvar!')

        r2010_nfs_form = disabled_form_fields(
            r2010_nfs_form,
            request.user.has_perm('r2010.change_r2010nfs'))

        if pk:

            if evento_dados['status'] != STATUS_EVENTO_CADASTRADO:

                r2010_nfs_form = disabled_form_fields(r2010_nfs_form, 0)

        if output:

            r2010_nfs_form = disabled_form_for_print(r2010_nfs_form)


        r2010_infotpserv_lista = None
        r2010_infotpserv_form = None

        if pk:

            r2010_nfs = get_object_or_404(r2010nfs, id=pk)

            r2010_infotpserv_form = form_r2010_infotpserv(
                initial={ 'r2010_nfs': r2010_nfs })
            r2010_infotpserv_form.fields['r2010_nfs'].widget.attrs['readonly'] = True
            r2010_infotpserv_lista = r2010infoTpServ.objects.\
                filter(r2010_nfs_id=r2010_nfs.id).all()


        else:

            r2010_nfs = None

        tabelas_secundarias = []

        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='r2010_nfs').all()

        if not request.POST:
            request.session['return_page'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_dados': evento_dados,
            'controle_alteracoes': controle_alteracoes,
            'r2010_nfs': r2010_nfs,
            'r2010_nfs_form': r2010_nfs_form,
            'modulos': ['r2010', ],
            'paginas': ['r2010_nfs', ],
            'r2010_infotpserv_form': r2010_infotpserv_form,
            'r2010_infotpserv_lista': r2010_infotpserv_lista,
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #r2010_nfs_salvar_custom_variaveis_context#
        }

        if output == 'pdf':

            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='r2010_nfs_salvar.html',
                filename="r2010_nfs.pdf",
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

            response = render_to_response('r2010_nfs_salvar.html', context)
            filename = "r2010_nfs.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 'r2010_nfs_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['r2010', ],
            'paginas': ['r2010_nfs', ],
            'data': datetime.datetime.now(),
        }

        return render(request,
                      'permissao_negada.html',
                      context)