#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import *
import base64
from emensageriapro.s2405.models import s2405brasil
from emensageriapro.s2405.models import s2405exterior
from emensageriapro.s2405.models import s2405dependente
from emensageriapro.s2405.forms import form_s2405_brasil
from emensageriapro.s2405.forms import form_s2405_exterior
from emensageriapro.s2405.forms import form_s2405_dependente

#IMPORTACOES


@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2405_evtcdbenefalt_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2405_evtcdbenefalt')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    s2405_evtcdbenefalt = get_object_or_404(s2405evtCdBenefAlt.objects.using( db_slug ), excluido = False, id = s2405_evtcdbenefalt_id)

    if s2405_evtcdbenefalt_id:
        if s2405_evtcdbenefalt.status != 0:
            dict_permissoes['s2405_evtcdbenefalt_apagar'] = 0
            dict_permissoes['s2405_evtcdbenefalt_editar'] = 0

    if request.method == 'POST':
        if s2405_evtcdbenefalt.status == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s2405_evtcdbenefalt), indent=4, sort_keys=True, default=str)
            s2405evtCdBenefAlt.objects.using( db_slug ).filter(id = s2405_evtcdbenefalt_id).delete()
            #s2405_evtcdbenefalt_apagar_custom
            #s2405_evtcdbenefalt_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's2405_evtcdbenefalt', s2405_evtcdbenefalt_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 's2405_evtcdbenefalt_salvar':
            return redirect('s2405_evtcdbenefalt', hash=request.session['retorno_hash'])
        else:
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
    context = {
        'usuario': usuario,

        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,

        'permissao': permissao,
        'data': datetime.datetime.now(),
        'pagina': pagina,
        'dict_permissoes': dict_permissoes,
        'hash': hash,
    }
    return render(request, 's2405_evtcdbenefalt_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class s2405evtCdBenefAltList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = s2405evtCdBenefAlt.objects.using(db_slug).all()
    serializer_class = s2405evtCdBenefAltSerializer
    permission_classes = (IsAdminUser,)


class s2405evtCdBenefAltDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = s2405evtCdBenefAlt.objects.using(db_slug).all()
    serializer_class = s2405evtCdBenefAltSerializer
    permission_classes = (IsAdminUser,)


def render_to_pdf(template_src, context_dict={}):
    from io import BytesIO
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

@login_required
def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #s2405_evtcdbenefalt_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2405_evtcdbenefalt')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_alteracao': 0,
            'show_arquivo': 0,
            'show_arquivo_original': 0,
            'show_cpfbenef': 1,
            'show_dadosbenef': 0,
            'show_dadosnasc': 0,
            'show_dtalteracao': 1,
            'show_dtincfismen': 0,
            'show_estciv': 0,
            'show_evtcdbenefalt': 0,
            'show_idebenef': 0,
            'show_ideempregador': 0,
            'show_ideevento': 0,
            'show_identidade': 1,
            'show_incfismen': 1,
            'show_indretif': 1,
            'show_nisbenef': 0,
            'show_nmbenefic': 1,
            'show_nmmae': 0,
            'show_nmpai': 0,
            'show_nrinsc': 1,
            'show_nrrecibo': 0,
            'show_ocorrencias': 0,
            'show_paisnac': 1,
            'show_procemi': 1,
            'show_processamento_codigo_resposta': 1,
            'show_processamento_data_hora': 0,
            'show_processamento_descricao_resposta': 1,
            'show_processamento_versao_app_processamento': 0,
            'show_racacor': 1,
            'show_recepcao_data_hora': 0,
            'show_recepcao_protocolo_envio_lote': 0,
            'show_recepcao_tp_amb': 0,
            'show_recepcao_versao_app': 0,
            'show_recibo_hash': 0,
            'show_recibo_numero': 0,
            'show_retornos_eventos': 0,
            'show_sexo': 1,
            'show_status': 1,
            'show_tpamb': 1,
            'show_tpinsc': 1,
            'show_transmissor_lote_esocial': 0,
            'show_validacao_precedencia': 0,
            'show_validacoes': 0,
            'show_verproc': 1,
            'show_versao': 0, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'alteracao': 'alteracao',
                'cpfbenef__icontains': 'cpfbenef__icontains',
                'dadosbenef': 'dadosbenef',
                'dadosnasc': 'dadosnasc',
                'dtalteracao__range': 'dtalteracao__range',
                'dtincfismen__range': 'dtincfismen__range',
                'estciv': 'estciv',
                'evtcdbenefalt': 'evtcdbenefalt',
                'idebenef': 'idebenef',
                'ideempregador': 'ideempregador',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'incfismen__icontains': 'incfismen__icontains',
                'indretif': 'indretif',
                'nisbenef__icontains': 'nisbenef__icontains',
                'nmbenefic__icontains': 'nmbenefic__icontains',
                'nmmae__icontains': 'nmmae__icontains',
                'nmpai__icontains': 'nmpai__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'paisnac__icontains': 'paisnac__icontains',
                'procemi': 'procemi',
                'racacor': 'racacor',
                'sexo__icontains': 'sexo__icontains',
                'status': 'status',
                'tpamb': 'tpamb',
                'tpinsc': 'tpinsc',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',
                'verproc__icontains': 'verproc__icontains',
                'versao__icontains': 'versao__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'alteracao': 'alteracao',
                'cpfbenef__icontains': 'cpfbenef__icontains',
                'dadosbenef': 'dadosbenef',
                'dadosnasc': 'dadosnasc',
                'dtalteracao__range': 'dtalteracao__range',
                'dtincfismen__range': 'dtincfismen__range',
                'estciv': 'estciv',
                'evtcdbenefalt': 'evtcdbenefalt',
                'idebenef': 'idebenef',
                'ideempregador': 'ideempregador',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'incfismen__icontains': 'incfismen__icontains',
                'indretif': 'indretif',
                'nisbenef__icontains': 'nisbenef__icontains',
                'nmbenefic__icontains': 'nmbenefic__icontains',
                'nmmae__icontains': 'nmmae__icontains',
                'nmpai__icontains': 'nmpai__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'paisnac__icontains': 'paisnac__icontains',
                'procemi': 'procemi',
                'racacor': 'racacor',
                'sexo__icontains': 'sexo__icontains',
                'status': 'status',
                'tpamb': 'tpamb',
                'tpinsc': 'tpinsc',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',
                'verproc__icontains': 'verproc__icontains',
                'versao__icontains': 'versao__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s2405_evtcdbenefalt_lista = s2405evtCdBenefAlt.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s2405_evtcdbenefalt_lista) > 100:
            filtrar = True
            s2405_evtcdbenefalt_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lote_esocial_lista = TransmissorLoteEsocial.objects.using( db_slug ).filter(excluido = False).all()
        #s2405_evtcdbenefalt_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2405_evtcdbenefalt'
        context = {
            's2405_evtcdbenefalt_lista': s2405_evtcdbenefalt_lista,
  
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,

            'transmissor_lote_esocial_lista': transmissor_lote_esocial_lista,
        }
        #return render(request, 's2405_evtcdbenefalt_listar.html', context)
        if for_print in (0,1):
            return render(request, 's2405_evtcdbenefalt_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2405_evtcdbenefalt_listar.html',
                filename="s2405_evtcdbenefalt.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             'viewport-size': "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('s2405_evtcdbenefalt_listar.html', context)
            filename = "s2405_evtcdbenefalt.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/s2405_evtcdbenefalt_csv.html', context)
            filename = "s2405_evtcdbenefalt.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
    else:
        context = {
            'usuario': usuario,
  
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)

#view_identidade_evento#
def identidade_evento(s2405_evtcdbenefalt_id, db_slug):
    from emensageriapro.mensageiro.models import TransmissorEventosEsocial
    dados_evento = s2405evtCdBenefAlt.objects.using( db_slug ).get(id=s2405_evtcdbenefalt_id)
    identidade = 'ID'
    identidade += str(dados_evento.tpinsc)
    nr_insc = dados_evento.nrinsc
    while len(nr_insc) != 14:
        nr_insc = nr_insc+'0'
    identidade += nr_insc
    identidade += str(dados_evento.criado_em.year)
    mes = str(dados_evento.criado_em.month)
    if len(mes) == 1: mes = '0'+mes
    identidade += mes
    dia = str(dados_evento.criado_em.day)
    if len(dia) == 1: dia = '0'+dia
    identidade += dia
    hora = str(dados_evento.criado_em.hour)
    if len(hora) == 1: hora = '0'+hora
    identidade += hora
    minuto = str(dados_evento.criado_em.minute)
    if len(minuto) == 1: minuto = '0'+minuto
    identidade += minuto
    segundo = str(dados_evento.criado_em.second)
    if len(segundo) == 1: segundo = '0'+segundo
    identidade += segundo
    existe = True
    n = 0
    while existe:
        n+=1
        sequencial = str(n)
        while len(sequencial) != 5:
            sequencial = '0'+sequencial
        identidade_temp = identidade + sequencial
        lista_eventos = TransmissorEventosEsocial.objects.using(db_slug).filter(criado_em=dados_evento.criado_em,
                                                                         excluido=False, identidade = identidade_temp).all()
        if not lista_eventos:
            s2405evtCdBenefAlt.objects.using(db_slug).filter(id=s2405_evtcdbenefalt_id).update(identidade=identidade_temp)
            existe = False
    return identidade_temp
#view_identidade_evento#



def gerar_identidade(request, chave, evento_id):
    from emensageriapro.settings import PASS_SCRIPT
    if chave == PASS_SCRIPT:
        db_slug = 'default'
        ident = identidade_evento(evento_id, db_slug)
        mensagem = ident
    else:
        mensagem = 'Chave incorreta!'
    return HttpResponse(mensagem)


@login_required
def salvar(request, hash):
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL, TP_AMB
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2405_evtcdbenefalt_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2405_evtcdbenefalt')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s2405_evtcdbenefalt_id:
        s2405_evtcdbenefalt = get_object_or_404(s2405evtCdBenefAlt.objects.using( db_slug ), excluido = False, id = s2405_evtcdbenefalt_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if s2405_evtcdbenefalt_id:
        if s2405_evtcdbenefalt.status != 0:
            dict_permissoes['s2405_evtcdbenefalt_apagar'] = 0
            dict_permissoes['s2405_evtcdbenefalt_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s2405_evtcdbenefalt_id:
            s2405_evtcdbenefalt_form = form_s2405_evtcdbenefalt(request.POST or None, instance = s2405_evtcdbenefalt, slug = db_slug)
        else:
            s2405_evtcdbenefalt_form = form_s2405_evtcdbenefalt(request.POST or None, slug = db_slug, initial={'versao': VERSAO_LAYOUT_ESOCIAL, 'status': 0, 'processamento_codigo_resposta': 0, 'tpamb': TP_AMB, 'procemi': 1, 'verproc': VERSAO_EMENSAGERIA})
        if request.method == 'POST':
            if s2405_evtcdbenefalt_form.is_valid():
                dados = s2405_evtcdbenefalt_form.cleaned_data
                import json
                from django.forms.models import model_to_dict
                if s2405_evtcdbenefalt_id:
                    if s2405_evtcdbenefalt.status == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #s2405_evtcdbenefalt_campos_multiple_passo1
                        s2405evtCdBenefAlt.objects.using(db_slug).filter(id=s2405_evtcdbenefalt_id).update(**dados)
                        obj = s2405evtCdBenefAlt.objects.using(db_slug).get(id=s2405_evtcdbenefalt_id)
                        #s2405_evtcdbenefalt_editar_custom
                        #s2405_evtcdbenefalt_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(s2405_evtcdbenefalt), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         's2405_evtcdbenefalt', s2405_evtcdbenefalt_id, usuario_id, 2)
                    else:
                        obj = s2405evtCdBenefAlt.objects.using(db_slug).get(id=s2405_evtcdbenefalt_id)
                        messages.error(request, 'Não é possível salvar o evento, pois o mesmo não está com o status "Cadastrado"!')

                else:
                    dados['processamento_codigo_resposta'] = '- -'
                    dados['processamento_descricao_resposta'] = '- -'

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #s2405_evtcdbenefalt_cadastrar_campos_multiple_passo1
                    obj = s2405evtCdBenefAlt(**dados)
                    obj.save(using = db_slug)
                    #s2405_evtcdbenefalt_cadastrar_custom
                    #s2405_evtcdbenefalt_cadastrar_campos_multiple_passo2
                    identidade_evento(obj.id, db_slug)
                    messages.success(request, 'Cadastrado com sucesso!')
                    s2405_evtcdbenefalt_form = form_s2405_evtcdbenefalt(request.POST or None, instance = obj, slug = db_slug)
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's2405_evtcdbenefalt', obj.id, usuario_id, 1)
                if request.session['retorno_pagina'] not in ('s2405_evtcdbenefalt_apagar', 's2405_evtcdbenefalt_salvar', 's2405_evtcdbenefalt'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s2405_evtcdbenefalt_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2405_evtcdbenefalt_salvar', hash=url_hash)

            else:
                messages.error(request, 'Erro ao salvar!')
        s2405_evtcdbenefalt_form = disabled_form_fields(s2405_evtcdbenefalt_form, permissao.permite_editar)

        if s2405_evtcdbenefalt_id:
            if s2405_evtcdbenefalt.status != 0:
                s2405_evtcdbenefalt_form = disabled_form_fields(s2405_evtcdbenefalt_form, False)
        #s2405_evtcdbenefalt_campos_multiple_passo3

        for field in s2405_evtcdbenefalt_form.fields.keys():
            s2405_evtcdbenefalt_form.fields[field].widget.attrs['ng-model'] = 's2405_evtcdbenefalt_'+field
        if int(dict_hash['print']):
            s2405_evtcdbenefalt_form = disabled_form_for_print(s2405_evtcdbenefalt_form)

        s2405_brasil_form = None
        s2405_brasil_lista = None
        s2405_exterior_form = None
        s2405_exterior_lista = None
        s2405_dependente_form = None
        s2405_dependente_lista = None
        if s2405_evtcdbenefalt_id:
            s2405_evtcdbenefalt = get_object_or_404(s2405evtCdBenefAlt.objects.using( db_slug ), excluido = False, id = s2405_evtcdbenefalt_id)

            s2405_brasil_form = form_s2405_brasil(initial={ 's2405_evtcdbenefalt': s2405_evtcdbenefalt }, slug=db_slug)
            s2405_brasil_form.fields['s2405_evtcdbenefalt'].widget.attrs['readonly'] = True
            s2405_brasil_lista = s2405brasil.objects.using( db_slug ).filter(excluido = False, s2405_evtcdbenefalt_id=s2405_evtcdbenefalt.id).all()
            s2405_exterior_form = form_s2405_exterior(initial={ 's2405_evtcdbenefalt': s2405_evtcdbenefalt }, slug=db_slug)
            s2405_exterior_form.fields['s2405_evtcdbenefalt'].widget.attrs['readonly'] = True
            s2405_exterior_lista = s2405exterior.objects.using( db_slug ).filter(excluido = False, s2405_evtcdbenefalt_id=s2405_evtcdbenefalt.id).all()
            s2405_dependente_form = form_s2405_dependente(initial={ 's2405_evtcdbenefalt': s2405_evtcdbenefalt }, slug=db_slug)
            s2405_dependente_form.fields['s2405_evtcdbenefalt'].widget.attrs['readonly'] = True
            s2405_dependente_lista = s2405dependente.objects.using( db_slug ).filter(excluido = False, s2405_evtcdbenefalt_id=s2405_evtcdbenefalt.id).all()
        else:
            s2405_evtcdbenefalt = None
        #s2405_evtcdbenefalt_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if 's2405_evtcdbenefalt'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False
        if not evento_totalizador:
            s2405_evtcdbenefalt_form.fields['tpamb'].widget.attrs['disabled'] = True
            s2405_evtcdbenefalt_form.fields['tpamb'].widget.attrs['readonly'] = True
            s2405_evtcdbenefalt_form.fields['tpamb'].value = TP_AMB
            s2405_evtcdbenefalt_form.fields['procemi'].widget.attrs['disabled'] = True
            s2405_evtcdbenefalt_form.fields['procemi'].widget.attrs['readonly'] = True
            s2405_evtcdbenefalt_form.fields['procemi'].value = 1
            s2405_evtcdbenefalt_form.fields['verproc'].widget.attrs['readonly'] = True
            s2405_evtcdbenefalt_form.fields['verproc'].value = VERSAO_EMENSAGERIA

        if dict_hash['tab'] or 's2405_evtcdbenefalt' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2405_evtcdbenefalt_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s2405_evtcdbenefalt_id, tabela='s2405_evtcdbenefalt').all()
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            's2405_evtcdbenefalt': s2405_evtcdbenefalt,
            's2405_evtcdbenefalt_form': s2405_evtcdbenefalt_form,
            'mensagem': mensagem,
            's2405_evtcdbenefalt_id': int(s2405_evtcdbenefalt_id),
            'usuario': usuario,
  
            'hash': hash,

            's2405_brasil_form': s2405_brasil_form,
            's2405_brasil_lista': s2405_brasil_lista,
            's2405_exterior_form': s2405_exterior_form,
            's2405_exterior_lista': s2405_exterior_lista,
            's2405_dependente_form': s2405_dependente_form,
            's2405_dependente_lista': s2405_dependente_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2405_evtcdbenefalt_salvar_custom_variaveis_context#
        }

        if for_print in (0,1 ):
            return render(request, 's2405_evtcdbenefalt_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2405_evtcdbenefalt_salvar.html',
                filename="s2405_evtcdbenefalt.pdf",
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
                             "no-stop-slow-scripts": True},
            )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('s2405_evtcdbenefalt_salvar.html', context)
            filename = "s2405_evtcdbenefalt.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
    else:
        context = {
            'usuario': usuario,
  
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)

