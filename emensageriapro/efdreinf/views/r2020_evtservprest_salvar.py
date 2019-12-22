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
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.r2020.models import r2020nfs
from emensageriapro.r2020.forms import form_r2020_nfs
from emensageriapro.r2020.models import r2020infoProcRetPr
from emensageriapro.r2020.forms import form_r2020_infoprocretpr
from emensageriapro.r2020.models import r2020infoProcRetAd
from emensageriapro.r2020.forms import form_r2020_infoprocretad


@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_EFDREINF
    TP_AMB = config.EFDREINF_TP_AMB

    if pk:

        r2020_evtservprest = get_object_or_404(r2020evtServPrest, id=pk)

    if request.user.has_perm('efdreinf.can_see_r2020evtServPrest'):

        if pk:

            r2020_evtservprest_form = form_r2020_evtservprest(request.POST or None, instance=r2020_evtservprest,
                                         initial={'ativo': True})
                     
        else:

            r2020_evtservprest_form = form_r2020_evtservprest(request.POST or None,
                                         initial={'versao': VERSAO_LAYOUT_EFDREINF,
                                                  'status': STATUS_EVENTO_CADASTRADO,
                                                  'tpamb': TP_AMB,
                                                  'procemi': 1,
                                                  'verproc': VERSAO_EMENSAGERIA,
                                                  'ativo': True})
                              
        if request.method == 'POST':

            if r2020_evtservprest_form.is_valid():

                obj = r2020_evtservprest_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')

                if not pk:

                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj, 'efdreinf')
             
                if 'return_page' in request.session and request.session['return_page'] and 'r2020-evtservprest' not in request.session['return_page']:

                    return HttpResponseRedirect(request.session['return_page'])

                if pk != obj.id:

                    return redirect(
                        'r2020_evtservprest_salvar',
                        pk=obj.id)

            else:
                messages.error(request, u'Erro ao salvar!')

        r2020_evtservprest_form = disabled_form_fields(
             r2020_evtservprest_form,
             request.user.has_perm('efdreinf.change_r2020evtServPrest'))

        if pk:

            if r2020_evtservprest.status != 0:

                r2020_evtservprest_form = disabled_form_fields(r2020_evtservprest_form, False)

        for field in r2020_evtservprest_form.fields.keys():

            r2020_evtservprest_form.fields[field].widget.attrs['ng-model'] = 'r2020_evtservprest_'+field

        if output:

            r2020_evtservprest_form = disabled_form_for_print(r2020_evtservprest_form)


        r2020_nfs_lista = None
        r2020_nfs_form = None
        r2020_infoprocretpr_lista = None
        r2020_infoprocretpr_form = None
        r2020_infoprocretad_lista = None
        r2020_infoprocretad_form = None

        if pk:

            r2020_evtservprest = get_object_or_404(r2020evtServPrest, id=pk)

            r2020_nfs_form = form_r2020_nfs(
                initial={'r2020_evtservprest': r2020_evtservprest})
            r2020_nfs_form.fields['r2020_evtservprest'].widget.attrs['readonly'] = True
            r2020_nfs_lista = r2020nfs.objects.\
                filter(r2020_evtservprest_id=r2020_evtservprest.id).all()
            r2020_infoprocretpr_form = form_r2020_infoprocretpr(
                initial={'r2020_evtservprest': r2020_evtservprest})
            r2020_infoprocretpr_form.fields['r2020_evtservprest'].widget.attrs['readonly'] = True
            r2020_infoprocretpr_lista = r2020infoProcRetPr.objects.\
                filter(r2020_evtservprest_id=r2020_evtservprest.id).all()
            r2020_infoprocretad_form = form_r2020_infoprocretad(
                initial={'r2020_evtservprest': r2020_evtservprest})
            r2020_infoprocretad_form.fields['r2020_evtservprest'].widget.attrs['readonly'] = True
            r2020_infoprocretad_lista = r2020infoProcRetAd.objects.\
                filter(r2020_evtservprest_id=r2020_evtservprest.id).all()

        else:

            r2020_evtservprest = None

        tabelas_secundarias = []

        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='r2020_evtservprest').all()

        if not request.POST:
            request.session['return_page'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_totalizador': False,
            'controle_alteracoes': controle_alteracoes,
            'r2020_evtservprest': r2020_evtservprest,
            'r2020_evtservprest_form': r2020_evtservprest_form,

            'r2020_nfs_form': r2020_nfs_form,
            'r2020_nfs_lista': r2020_nfs_lista,
            'r2020_infoprocretpr_form': r2020_infoprocretpr_form,
            'r2020_infoprocretpr_lista': r2020_infoprocretpr_lista,
            'r2020_infoprocretad_form': r2020_infoprocretad_form,
            'r2020_infoprocretad_lista': r2020_infoprocretad_lista,
            'data': datetime.datetime.now(),
            'modulos': ['efdreinf', ],
            'paginas': ['r2020_evtservprest', ],
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
        }

        if output == 'pdf':

            response = PDFTemplateResponse(
                request=request,
                template='r2020_evtservprest_salvar.html',
                filename="r2020_evtservprest.pdf",
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

            response = render_to_response('r2020_evtservprest_salvar.html', context)
            filename = "r2020_evtservprest.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 'r2020_evtservprest_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'tab': tab,
            'output': output,
            'modulos': ['efdreinf', ],
            'paginas': ['r2020_evtservprest', ],
            'data': datetime.datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)