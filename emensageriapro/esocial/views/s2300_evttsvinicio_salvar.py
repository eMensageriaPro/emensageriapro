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
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s2300.models import s2300documentos
from emensageriapro.s2300.forms import form_s2300_documentos
from emensageriapro.s2300.models import s2300brasil
from emensageriapro.s2300.forms import form_s2300_brasil
from emensageriapro.s2300.models import s2300exterior
from emensageriapro.s2300.forms import form_s2300_exterior
from emensageriapro.s2300.models import s2300trabEstrangeiro
from emensageriapro.s2300.forms import form_s2300_trabestrangeiro
from emensageriapro.s2300.models import s2300infoDeficiencia
from emensageriapro.s2300.forms import form_s2300_infodeficiencia
from emensageriapro.s2300.models import s2300dependente
from emensageriapro.s2300.forms import form_s2300_dependente
from emensageriapro.s2300.models import s2300contato
from emensageriapro.s2300.forms import form_s2300_contato
from emensageriapro.s2300.models import s2300infoComplementares
from emensageriapro.s2300.forms import form_s2300_infocomplementares
from emensageriapro.s2300.models import s2300mudancaCPF
from emensageriapro.s2300.forms import form_s2300_mudancacpf
from emensageriapro.s2300.models import s2300afastamento
from emensageriapro.s2300.forms import form_s2300_afastamento
from emensageriapro.s2300.models import s2300termino
from emensageriapro.s2300.forms import form_s2300_termino


@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    TP_AMB = config.ESOCIAL_TP_AMB

    if pk:

        s2300_evttsvinicio = get_object_or_404(s2300evtTSVInicio, id=pk)

    if request.user.has_perm('esocial.can_see_s2300evtTSVInicio'):

        if pk:

            s2300_evttsvinicio_form = form_s2300_evttsvinicio(request.POST or None, instance=s2300_evttsvinicio,
                                         initial={'ativo': True})
                     
        else:

            s2300_evttsvinicio_form = form_s2300_evttsvinicio(request.POST or None,
                                         initial={'versao': VERSAO_LAYOUT_ESOCIAL,
                                                  'status': STATUS_EVENTO_CADASTRADO,
                                                  'tpamb': TP_AMB,
                                                  'procemi': 1,
                                                  'verproc': VERSAO_EMENSAGERIA,
                                                  'ativo': True})
                              
        if request.method == 'POST':

            if s2300_evttsvinicio_form.is_valid():

                obj = s2300_evttsvinicio_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')

                if not pk:

                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj, 'esocial')
             
                if 's2300-evttsvinicio' not in request.session['return']:

                    return HttpResponseRedirect(request.session['return'])

                if pk != obj.id:

                    return redirect(
                        's2300_evttsvinicio_salvar',
                        pk=obj.id)

            else:
                messages.error(request, u'Erro ao salvar!')

        s2300_evttsvinicio_form = disabled_form_fields(
             s2300_evttsvinicio_form,
             request.user.has_perm('esocial.change_s2300evtTSVInicio'))

        if pk:

            if s2300_evttsvinicio.status != 0:

                s2300_evttsvinicio_form = disabled_form_fields(s2300_evttsvinicio_form, False)

        for field in s2300_evttsvinicio_form.fields.keys():

            s2300_evttsvinicio_form.fields[field].widget.attrs['ng-model'] = 's2300_evttsvinicio_'+field

        if output:

            s2300_evttsvinicio_form = disabled_form_for_print(s2300_evttsvinicio_form)


        s2300_documentos_lista = None
        s2300_documentos_form = None
        s2300_brasil_lista = None
        s2300_brasil_form = None
        s2300_exterior_lista = None
        s2300_exterior_form = None
        s2300_trabestrangeiro_lista = None
        s2300_trabestrangeiro_form = None
        s2300_infodeficiencia_lista = None
        s2300_infodeficiencia_form = None
        s2300_dependente_lista = None
        s2300_dependente_form = None
        s2300_contato_lista = None
        s2300_contato_form = None
        s2300_infocomplementares_lista = None
        s2300_infocomplementares_form = None
        s2300_mudancacpf_lista = None
        s2300_mudancacpf_form = None
        s2300_afastamento_lista = None
        s2300_afastamento_form = None
        s2300_termino_lista = None
        s2300_termino_form = None

        if pk:

            s2300_evttsvinicio = get_object_or_404(s2300evtTSVInicio, id=pk)

            s2300_documentos_form = form_s2300_documentos(
                initial={'s2300_evttsvinicio': s2300_evttsvinicio})
            s2300_documentos_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_documentos_lista = s2300documentos.objects.\
                filter(s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_brasil_form = form_s2300_brasil(
                initial={'s2300_evttsvinicio': s2300_evttsvinicio})
            s2300_brasil_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_brasil_lista = s2300brasil.objects.\
                filter(s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_exterior_form = form_s2300_exterior(
                initial={'s2300_evttsvinicio': s2300_evttsvinicio})
            s2300_exterior_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_exterior_lista = s2300exterior.objects.\
                filter(s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_trabestrangeiro_form = form_s2300_trabestrangeiro(
                initial={'s2300_evttsvinicio': s2300_evttsvinicio})
            s2300_trabestrangeiro_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_trabestrangeiro_lista = s2300trabEstrangeiro.objects.\
                filter(s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_infodeficiencia_form = form_s2300_infodeficiencia(
                initial={'s2300_evttsvinicio': s2300_evttsvinicio})
            s2300_infodeficiencia_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_infodeficiencia_lista = s2300infoDeficiencia.objects.\
                filter(s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_dependente_form = form_s2300_dependente(
                initial={'s2300_evttsvinicio': s2300_evttsvinicio})
            s2300_dependente_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_dependente_lista = s2300dependente.objects.\
                filter(s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_contato_form = form_s2300_contato(
                initial={'s2300_evttsvinicio': s2300_evttsvinicio})
            s2300_contato_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_contato_lista = s2300contato.objects.\
                filter(s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_infocomplementares_form = form_s2300_infocomplementares(
                initial={'s2300_evttsvinicio': s2300_evttsvinicio})
            s2300_infocomplementares_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_infocomplementares_lista = s2300infoComplementares.objects.\
                filter(s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_mudancacpf_form = form_s2300_mudancacpf(
                initial={'s2300_evttsvinicio': s2300_evttsvinicio})
            s2300_mudancacpf_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_mudancacpf_lista = s2300mudancaCPF.objects.\
                filter(s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_afastamento_form = form_s2300_afastamento(
                initial={'s2300_evttsvinicio': s2300_evttsvinicio})
            s2300_afastamento_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_afastamento_lista = s2300afastamento.objects.\
                filter(s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_termino_form = form_s2300_termino(
                initial={'s2300_evttsvinicio': s2300_evttsvinicio})
            s2300_termino_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_termino_lista = s2300termino.objects.\
                filter(s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()

        else:

            s2300_evttsvinicio = None

        tabelas_secundarias = []

        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s2300_evttsvinicio').all()

        if not request.POST:
            request.session['return'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_totalizador': False,
            'controle_alteracoes': controle_alteracoes,
            's2300_evttsvinicio': s2300_evttsvinicio,
            's2300_evttsvinicio_form': s2300_evttsvinicio_form,

            's2300_documentos_form': s2300_documentos_form,
            's2300_documentos_lista': s2300_documentos_lista,
            's2300_brasil_form': s2300_brasil_form,
            's2300_brasil_lista': s2300_brasil_lista,
            's2300_exterior_form': s2300_exterior_form,
            's2300_exterior_lista': s2300_exterior_lista,
            's2300_trabestrangeiro_form': s2300_trabestrangeiro_form,
            's2300_trabestrangeiro_lista': s2300_trabestrangeiro_lista,
            's2300_infodeficiencia_form': s2300_infodeficiencia_form,
            's2300_infodeficiencia_lista': s2300_infodeficiencia_lista,
            's2300_dependente_form': s2300_dependente_form,
            's2300_dependente_lista': s2300_dependente_lista,
            's2300_contato_form': s2300_contato_form,
            's2300_contato_lista': s2300_contato_lista,
            's2300_infocomplementares_form': s2300_infocomplementares_form,
            's2300_infocomplementares_lista': s2300_infocomplementares_lista,
            's2300_mudancacpf_form': s2300_mudancacpf_form,
            's2300_mudancacpf_lista': s2300_mudancacpf_lista,
            's2300_afastamento_form': s2300_afastamento_form,
            's2300_afastamento_lista': s2300_afastamento_lista,
            's2300_termino_form': s2300_termino_form,
            's2300_termino_lista': s2300_termino_lista,
            'data': datetime.datetime.now(),
            'modulos': ['esocial', ],
            'paginas': ['s2300_evttsvinicio', ],
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
        }

        if output == 'pdf':

            response = PDFTemplateResponse(
                request=request,
                template='s2300_evttsvinicio_salvar.html',
                filename="s2300_evttsvinicio.pdf",
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

            response = render_to_response('s2300_evttsvinicio_salvar.html', context)
            filename = "s2300_evttsvinicio.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 's2300_evttsvinicio_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'tab': tab,
            'output': output,
            'modulos': ['esocial', ],
            'paginas': ['s2300_evttsvinicio', ],
            'data': datetime.datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)