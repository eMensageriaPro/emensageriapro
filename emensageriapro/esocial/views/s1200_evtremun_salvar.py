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
from constance import config
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
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s1200.models import s1200infoMV
from emensageriapro.s1200.forms import form_s1200_infomv
from emensageriapro.s1200.models import s1200infoComplem
from emensageriapro.s1200.forms import form_s1200_infocomplem
from emensageriapro.s1200.models import s1200procJudTrab
from emensageriapro.s1200.forms import form_s1200_procjudtrab
from emensageriapro.s1200.models import s1200infoInterm
from emensageriapro.s1200.forms import form_s1200_infointerm
from emensageriapro.s1200.models import s1200dmDev
from emensageriapro.s1200.forms import form_s1200_dmdev


@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    TP_AMB = config.ESOCIAL_TP_AMB

    if pk:

        s1200_evtremun = get_object_or_404(s1200evtRemun, id=pk)

        #if s1200_evtremun.status != STATUS_EVENTO_CADASTRADO:
        #
        #    dict_permissoes = {}
        #    dict_permissoes['s1200_evtremun_apagar'] = 0
        #    dict_permissoes['s1200_evtremun_editar'] = 0

    if request.user.has_perm('esocial.can_see_s1200evtRemun'):

        if pk:

            s1200_evtremun_form = form_s1200_evtremun(request.POST or None, instance = s1200_evtremun,
                                         initial={'ativo': True})
                     
        else:

            s1200_evtremun_form = form_s1200_evtremun(request.POST or None,
                                         initial={'versao': VERSAO_LAYOUT_ESOCIAL,
                                                  'status': STATUS_EVENTO_CADASTRADO,
                                                  'tpamb': TP_AMB,
                                                  'procemi': 1,
                                                  'verproc': VERSAO_EMENSAGERIA,
                                                  'ativo': True})
                              
        if request.method == 'POST':

            if s1200_evtremun_form.is_valid():

                obj = s1200_evtremun_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')

                if not pk:

                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
             
                if 's1200-evtremun' not in request.session['return']:

                    return HttpResponseRedirect(request.session['return'])

                if pk != obj.id:

                    return redirect(
                        's1200_evtremun_salvar',
                        pk=obj.id)

            else:
                messages.error(request, u'Erro ao salvar!')

        s1200_evtremun_form = disabled_form_fields(
             s1200_evtremun_form,
             request.user.has_perm('esocial.change_s1200evtRemun'))

        if pk:

            if s1200_evtremun.status != 0:

                s1200_evtremun_form = disabled_form_fields(s1200_evtremun_form, False)

        #s1200_evtremun_campos_multiple_passo3

        for field in s1200_evtremun_form.fields.keys():

            s1200_evtremun_form.fields[field].widget.attrs['ng-model'] = 's1200_evtremun_'+field

        if output:

            s1200_evtremun_form = disabled_form_for_print(s1200_evtremun_form)


        s1200_infomv_lista = None
        s1200_infomv_form = None
        s1200_infocomplem_lista = None
        s1200_infocomplem_form = None
        s1200_procjudtrab_lista = None
        s1200_procjudtrab_form = None
        s1200_infointerm_lista = None
        s1200_infointerm_form = None
        s1200_dmdev_lista = None
        s1200_dmdev_form = None

        if pk:

            s1200_evtremun = get_object_or_404(s1200evtRemun, id=pk)

            s1200_infomv_form = form_s1200_infomv(
                initial={ 's1200_evtremun': s1200_evtremun })
            s1200_infomv_form.fields['s1200_evtremun'].widget.attrs['readonly'] = True
            s1200_infomv_lista = s1200infoMV.objects.\
                filter(s1200_evtremun_id=s1200_evtremun.id).all()
            s1200_infocomplem_form = form_s1200_infocomplem(
                initial={ 's1200_evtremun': s1200_evtremun })
            s1200_infocomplem_form.fields['s1200_evtremun'].widget.attrs['readonly'] = True
            s1200_infocomplem_lista = s1200infoComplem.objects.\
                filter(s1200_evtremun_id=s1200_evtremun.id).all()
            s1200_procjudtrab_form = form_s1200_procjudtrab(
                initial={ 's1200_evtremun': s1200_evtremun })
            s1200_procjudtrab_form.fields['s1200_evtremun'].widget.attrs['readonly'] = True
            s1200_procjudtrab_lista = s1200procJudTrab.objects.\
                filter(s1200_evtremun_id=s1200_evtremun.id).all()
            s1200_infointerm_form = form_s1200_infointerm(
                initial={ 's1200_evtremun': s1200_evtremun })
            s1200_infointerm_form.fields['s1200_evtremun'].widget.attrs['readonly'] = True
            s1200_infointerm_lista = s1200infoInterm.objects.\
                filter(s1200_evtremun_id=s1200_evtremun.id).all()
            s1200_dmdev_form = form_s1200_dmdev(
                initial={ 's1200_evtremun': s1200_evtremun })
            s1200_dmdev_form.fields['s1200_evtremun'].widget.attrs['readonly'] = True
            s1200_dmdev_lista = s1200dmDev.objects.\
                filter(s1200_evtremun_id=s1200_evtremun.id).all()

        else:

            s1200_evtremun = None

        #s1200_evtremun_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]

        if 's1200_evtremun'[1] == '5':
            evento_totalizador = True

        else:
            evento_totalizador = False

        #if tab or 's1200_evtremun' in request.session['return_page']:
        #
        #    request.session['return_pk'] = pk
        #    request.session['return_tab'] = tab
        #    request.session['return_page'] = 's1200_evtremun_salvar'

        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s1200_evtremun').all()

        if not request.POST:
            request.session['return'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            's1200_evtremun': s1200_evtremun,
            's1200_evtremun_form': s1200_evtremun_form,

            's1200_infomv_form': s1200_infomv_form,
            's1200_infomv_lista': s1200_infomv_lista,
            's1200_infocomplem_form': s1200_infocomplem_form,
            's1200_infocomplem_lista': s1200_infocomplem_lista,
            's1200_procjudtrab_form': s1200_procjudtrab_form,
            's1200_procjudtrab_lista': s1200_procjudtrab_lista,
            's1200_infointerm_form': s1200_infointerm_form,
            's1200_infointerm_lista': s1200_infointerm_lista,
            's1200_dmdev_form': s1200_dmdev_form,
            's1200_dmdev_lista': s1200_dmdev_lista,
            'data': datetime.datetime.now(),
            'modulos': ['esocial', ],
            'paginas': ['s1200_evtremun', ],
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #s1200_evtremun_salvar_custom_variaveis_context#
        }


        if output == 'pdf':

            response = PDFTemplateResponse(
                request=request,
                template='s1200_evtremun_salvar.html',
                filename="s1200_evtremun.pdf",
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

            response = render_to_response('s1200_evtremun_salvar.html', context)
            filename = "s1200_evtremun.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 's1200_evtremun_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'tab': tab,
            'output': output,
            'modulos': ['esocial', ],
            'paginas': ['s1200_evtremun', ],
            'data': datetime.datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)