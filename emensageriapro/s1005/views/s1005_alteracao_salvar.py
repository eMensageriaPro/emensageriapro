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
from emensageriapro.s1005.forms import *
from emensageriapro.s1005.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s1005.models import s1005alteracaoprocAdmJudRat
from emensageriapro.s1005.forms import form_s1005_alteracao_procadmjudrat
from emensageriapro.s1005.models import s1005alteracaoprocAdmJudFap
from emensageriapro.s1005.forms import form_s1005_alteracao_procadmjudfap
from emensageriapro.s1005.models import s1005alteracaoinfoCaepf
from emensageriapro.s1005.forms import form_s1005_alteracao_infocaepf
from emensageriapro.s1005.models import s1005alteracaoinfoObra
from emensageriapro.s1005.forms import form_s1005_alteracao_infoobra
from emensageriapro.s1005.models import s1005alteracaoinfoEntEduc
from emensageriapro.s1005.forms import form_s1005_alteracao_infoenteduc
from emensageriapro.s1005.models import s1005alteracaoinfoPCD
from emensageriapro.s1005.forms import form_s1005_alteracao_infopcd
from emensageriapro.s1005.models import s1005alteracaonovaValidade
from emensageriapro.s1005.forms import form_s1005_alteracao_novavalidade



@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO

    evento_dados = {}
    evento_dados['status'] = STATUS_EVENTO_CADASTRADO

    if pk:

        s1005_alteracao = get_object_or_404(s1005alteracao, id=pk)
        evento_dados = s1005_alteracao.evento()

    if request.user.has_perm('s1005.can_see_s1005alteracao'):

        if pk:

            s1005_alteracao_form = form_s1005_alteracao(
                request.POST or None,
                instance=s1005_alteracao)
                     
        else:

            s1005_alteracao_form = form_s1005_alteracao(request.POST or None)
                     
        if request.method == 'POST':

            if s1005_alteracao_form.is_valid():

                obj = s1005_alteracao_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                 
                if 'return_page' in request.session and request.session['return_page'] and 's1005-alteracao' not in request.session['return_page']:

                    return HttpResponseRedirect(request.session['return_page'])

                if pk != obj.id:

                    return redirect(
                        's1005_alteracao_salvar',
                        pk=obj.id)

            else:

                messages.error(request, u'Erro ao salvar!')

        s1005_alteracao_form = disabled_form_fields(
            s1005_alteracao_form,
            request.user.has_perm('s1005.change_s1005alteracao'))

        if pk:

            if evento_dados['status'] != STATUS_EVENTO_CADASTRADO:

                s1005_alteracao_form = disabled_form_fields(s1005_alteracao_form, 0)

        if output:

            s1005_alteracao_form = disabled_form_for_print(s1005_alteracao_form)


        s1005_alteracao_procadmjudrat_lista = None
        s1005_alteracao_procadmjudrat_form = None
        s1005_alteracao_procadmjudfap_lista = None
        s1005_alteracao_procadmjudfap_form = None
        s1005_alteracao_infocaepf_lista = None
        s1005_alteracao_infocaepf_form = None
        s1005_alteracao_infoobra_lista = None
        s1005_alteracao_infoobra_form = None
        s1005_alteracao_infoenteduc_lista = None
        s1005_alteracao_infoenteduc_form = None
        s1005_alteracao_infopcd_lista = None
        s1005_alteracao_infopcd_form = None
        s1005_alteracao_novavalidade_lista = None
        s1005_alteracao_novavalidade_form = None

        if pk:

            s1005_alteracao = get_object_or_404(s1005alteracao, id=pk)

            s1005_alteracao_procadmjudrat_form = form_s1005_alteracao_procadmjudrat(
                initial={ 's1005_alteracao': s1005_alteracao })
            s1005_alteracao_procadmjudrat_form.fields['s1005_alteracao'].widget.attrs['readonly'] = True
            s1005_alteracao_procadmjudrat_lista = s1005alteracaoprocAdmJudRat.objects.\
                filter(s1005_alteracao_id=s1005_alteracao.id).all()

            s1005_alteracao_procadmjudfap_form = form_s1005_alteracao_procadmjudfap(
                initial={ 's1005_alteracao': s1005_alteracao })
            s1005_alteracao_procadmjudfap_form.fields['s1005_alteracao'].widget.attrs['readonly'] = True
            s1005_alteracao_procadmjudfap_lista = s1005alteracaoprocAdmJudFap.objects.\
                filter(s1005_alteracao_id=s1005_alteracao.id).all()

            s1005_alteracao_infocaepf_form = form_s1005_alteracao_infocaepf(
                initial={ 's1005_alteracao': s1005_alteracao })
            s1005_alteracao_infocaepf_form.fields['s1005_alteracao'].widget.attrs['readonly'] = True
            s1005_alteracao_infocaepf_lista = s1005alteracaoinfoCaepf.objects.\
                filter(s1005_alteracao_id=s1005_alteracao.id).all()

            s1005_alteracao_infoobra_form = form_s1005_alteracao_infoobra(
                initial={ 's1005_alteracao': s1005_alteracao })
            s1005_alteracao_infoobra_form.fields['s1005_alteracao'].widget.attrs['readonly'] = True
            s1005_alteracao_infoobra_lista = s1005alteracaoinfoObra.objects.\
                filter(s1005_alteracao_id=s1005_alteracao.id).all()

            s1005_alteracao_infoenteduc_form = form_s1005_alteracao_infoenteduc(
                initial={ 's1005_alteracao': s1005_alteracao })
            s1005_alteracao_infoenteduc_form.fields['s1005_alteracao'].widget.attrs['readonly'] = True
            s1005_alteracao_infoenteduc_lista = s1005alteracaoinfoEntEduc.objects.\
                filter(s1005_alteracao_id=s1005_alteracao.id).all()

            s1005_alteracao_infopcd_form = form_s1005_alteracao_infopcd(
                initial={ 's1005_alteracao': s1005_alteracao })
            s1005_alteracao_infopcd_form.fields['s1005_alteracao'].widget.attrs['readonly'] = True
            s1005_alteracao_infopcd_lista = s1005alteracaoinfoPCD.objects.\
                filter(s1005_alteracao_id=s1005_alteracao.id).all()

            s1005_alteracao_novavalidade_form = form_s1005_alteracao_novavalidade(
                initial={ 's1005_alteracao': s1005_alteracao })
            s1005_alteracao_novavalidade_form.fields['s1005_alteracao'].widget.attrs['readonly'] = True
            s1005_alteracao_novavalidade_lista = s1005alteracaonovaValidade.objects.\
                filter(s1005_alteracao_id=s1005_alteracao.id).all()


        else:

            s1005_alteracao = None

        tabelas_secundarias = []

        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s1005_alteracao').all()

        if not request.POST:
            request.session['return_page'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_dados': evento_dados,
            'controle_alteracoes': controle_alteracoes,
            's1005_alteracao': s1005_alteracao,
            's1005_alteracao_form': s1005_alteracao_form,
            'modulos': ['s1005', ],
            'paginas': ['s1005_alteracao', ],
            's1005_alteracao_procadmjudrat_form': s1005_alteracao_procadmjudrat_form,
            's1005_alteracao_procadmjudrat_lista': s1005_alteracao_procadmjudrat_lista,
            's1005_alteracao_procadmjudfap_form': s1005_alteracao_procadmjudfap_form,
            's1005_alteracao_procadmjudfap_lista': s1005_alteracao_procadmjudfap_lista,
            's1005_alteracao_infocaepf_form': s1005_alteracao_infocaepf_form,
            's1005_alteracao_infocaepf_lista': s1005_alteracao_infocaepf_lista,
            's1005_alteracao_infoobra_form': s1005_alteracao_infoobra_form,
            's1005_alteracao_infoobra_lista': s1005_alteracao_infoobra_lista,
            's1005_alteracao_infoenteduc_form': s1005_alteracao_infoenteduc_form,
            's1005_alteracao_infoenteduc_lista': s1005_alteracao_infoenteduc_lista,
            's1005_alteracao_infopcd_form': s1005_alteracao_infopcd_form,
            's1005_alteracao_infopcd_lista': s1005_alteracao_infopcd_lista,
            's1005_alteracao_novavalidade_form': s1005_alteracao_novavalidade_form,
            's1005_alteracao_novavalidade_lista': s1005_alteracao_novavalidade_lista,
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #s1005_alteracao_salvar_custom_variaveis_context#
        }

        if output == 'pdf':

            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='s1005_alteracao_salvar.html',
                filename="s1005_alteracao.pdf",
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

            response = render_to_response('s1005_alteracao_salvar.html', context)
            filename = "s1005_alteracao.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 's1005_alteracao_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['s1005', ],
            'paginas': ['s1005_alteracao', ],
            'data': datetime.datetime.now(),
        }

        return render(request,
                      'permissao_negada.html',
                      context)