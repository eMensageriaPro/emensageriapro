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
from emensageriapro.r4040.models import r4040ideNat
from emensageriapro.r4040.forms import form_r4040_idenat


@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_EFDREINF
    TP_AMB = config.EFDREINF_TP_AMB

    if pk:

        r4040_evtbenefnid = get_object_or_404(r4040evtBenefNId, id=pk)

    if request.user.has_perm('efdreinf.can_see_r4040evtBenefNId'):

        if pk:

            r4040_evtbenefnid_form = form_r4040_evtbenefnid(request.POST or None, instance=r4040_evtbenefnid,
                                         initial={'ativo': True})
                     
        else:

            r4040_evtbenefnid_form = form_r4040_evtbenefnid(request.POST or None,
                                         initial={'versao': VERSAO_LAYOUT_EFDREINF,
                                                  'status': STATUS_EVENTO_CADASTRADO,
                                                  'tpamb': TP_AMB,
                                                  'procemi': 1,
                                                  'verproc': VERSAO_EMENSAGERIA,
                                                  'ativo': True})
                              
        if request.method == 'POST':

            if r4040_evtbenefnid_form.is_valid():

                obj = r4040_evtbenefnid_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')

                if not pk:

                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj, 'efdreinf')
             
                if 'r4040-evtbenefnid' not in request.session['return']:

                    return HttpResponseRedirect(request.session['return'])

                if pk != obj.id:

                    return redirect(
                        'r4040_evtbenefnid_salvar',
                        pk=obj.id)

            else:
                messages.error(request, u'Erro ao salvar!')

        r4040_evtbenefnid_form = disabled_form_fields(
             r4040_evtbenefnid_form,
             request.user.has_perm('efdreinf.change_r4040evtBenefNId'))

        if pk:

            if r4040_evtbenefnid.status != 0:

                r4040_evtbenefnid_form = disabled_form_fields(r4040_evtbenefnid_form, False)

        for field in r4040_evtbenefnid_form.fields.keys():

            r4040_evtbenefnid_form.fields[field].widget.attrs['ng-model'] = 'r4040_evtbenefnid_'+field

        if output:

            r4040_evtbenefnid_form = disabled_form_for_print(r4040_evtbenefnid_form)


        r4040_idenat_lista = None
        r4040_idenat_form = None

        if pk:

            r4040_evtbenefnid = get_object_or_404(r4040evtBenefNId, id=pk)

            r4040_idenat_form = form_r4040_idenat(
                initial={'r4040_evtbenefnid': r4040_evtbenefnid})
            r4040_idenat_form.fields['r4040_evtbenefnid'].widget.attrs['readonly'] = True
            r4040_idenat_lista = r4040ideNat.objects.\
                filter(r4040_evtbenefnid_id=r4040_evtbenefnid.id).all()

        else:

            r4040_evtbenefnid = None

        tabelas_secundarias = []

        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='r4040_evtbenefnid').all()

        if not request.POST:
            request.session['return'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_totalizador': False,
            'controle_alteracoes': controle_alteracoes,
            'r4040_evtbenefnid': r4040_evtbenefnid,
            'r4040_evtbenefnid_form': r4040_evtbenefnid_form,

            'r4040_idenat_form': r4040_idenat_form,
            'r4040_idenat_lista': r4040_idenat_lista,
            'data': datetime.datetime.now(),
            'modulos': ['efdreinf', ],
            'paginas': ['r4040_evtbenefnid', ],
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
        }

        if output == 'pdf':

            response = PDFTemplateResponse(
                request=request,
                template='r4040_evtbenefnid_salvar.html',
                filename="r4040_evtbenefnid.pdf",
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

            response = render_to_response('r4040_evtbenefnid_salvar.html', context)
            filename = "r4040_evtbenefnid.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 'r4040_evtbenefnid_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'tab': tab,
            'output': output,
            'modulos': ['efdreinf', ],
            'paginas': ['r4040_evtbenefnid', ],
            'data': datetime.datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)