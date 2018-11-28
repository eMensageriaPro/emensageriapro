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
from emensageriapro.s2200.models import s2200CTPS
from emensageriapro.s2200.models import s2200RIC
from emensageriapro.s2200.models import s2200RG
from emensageriapro.s2200.models import s2200RNE
from emensageriapro.s2200.models import s2200OC
from emensageriapro.s2200.models import s2200CNH
from emensageriapro.s2200.models import s2200brasil
from emensageriapro.s2200.models import s2200exterior
from emensageriapro.s2200.models import s2200trabEstrangeiro
from emensageriapro.s2200.models import s2200infoDeficiencia
from emensageriapro.s2200.models import s2200dependente
from emensageriapro.s2200.models import s2200aposentadoria
from emensageriapro.s2200.models import s2200contato
from emensageriapro.s2200.models import s2200infoCeletista
from emensageriapro.s2200.models import s2200infoEstatutario
from emensageriapro.s2200.models import s2200localTrabGeral
from emensageriapro.s2200.models import s2200localTrabDom
from emensageriapro.s2200.models import s2200horContratual
from emensageriapro.s2200.models import s2200filiacaoSindical
from emensageriapro.s2200.models import s2200alvaraJudicial
from emensageriapro.s2200.models import s2200observacoes
from emensageriapro.s2200.models import s2200sucessaoVinc
from emensageriapro.s2200.models import s2200transfDom
from emensageriapro.s2200.models import s2200mudancaCPF
from emensageriapro.s2200.models import s2200afastamento
from emensageriapro.s2200.models import s2200desligamento
from emensageriapro.s2200.models import s2200cessao
from emensageriapro.s2200.forms import form_s2200_ctps
from emensageriapro.s2200.forms import form_s2200_ric
from emensageriapro.s2200.forms import form_s2200_rg
from emensageriapro.s2200.forms import form_s2200_rne
from emensageriapro.s2200.forms import form_s2200_oc
from emensageriapro.s2200.forms import form_s2200_cnh
from emensageriapro.s2200.forms import form_s2200_brasil
from emensageriapro.s2200.forms import form_s2200_exterior
from emensageriapro.s2200.forms import form_s2200_trabestrangeiro
from emensageriapro.s2200.forms import form_s2200_infodeficiencia
from emensageriapro.s2200.forms import form_s2200_dependente
from emensageriapro.s2200.forms import form_s2200_aposentadoria
from emensageriapro.s2200.forms import form_s2200_contato
from emensageriapro.s2200.forms import form_s2200_infoceletista
from emensageriapro.s2200.forms import form_s2200_infoestatutario
from emensageriapro.s2200.forms import form_s2200_localtrabgeral
from emensageriapro.s2200.forms import form_s2200_localtrabdom
from emensageriapro.s2200.forms import form_s2200_horcontratual
from emensageriapro.s2200.forms import form_s2200_filiacaosindical
from emensageriapro.s2200.forms import form_s2200_alvarajudicial
from emensageriapro.s2200.forms import form_s2200_observacoes
from emensageriapro.s2200.forms import form_s2200_sucessaovinc
from emensageriapro.s2200.forms import form_s2200_transfdom
from emensageriapro.s2200.forms import form_s2200_mudancacpf
from emensageriapro.s2200.forms import form_s2200_afastamento
from emensageriapro.s2200.forms import form_s2200_desligamento
from emensageriapro.s2200.forms import form_s2200_cessao

#IMPORTACOES


@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2200_evtadmissao_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2200_evtadmissao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    s2200_evtadmissao = get_object_or_404(s2200evtAdmissao.objects.using( db_slug ), excluido = False, id = s2200_evtadmissao_id)

    if s2200_evtadmissao_id:
        if s2200_evtadmissao.status != 0:
            dict_permissoes['s2200_evtadmissao_apagar'] = 0
            dict_permissoes['s2200_evtadmissao_editar'] = 0

    if request.method == 'POST':
        if s2200_evtadmissao.status == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s2200_evtadmissao), indent=4, sort_keys=True, default=str)
            s2200evtAdmissao.objects.using( db_slug ).filter(id = s2200_evtadmissao_id).delete()
            #s2200_evtadmissao_apagar_custom
            #s2200_evtadmissao_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's2200_evtadmissao', s2200_evtadmissao_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')
        
        if request.session['retorno_pagina']== 's2200_evtadmissao_salvar':
            return redirect('s2200_evtadmissao', hash=request.session['retorno_hash'])
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
    return render(request, 's2200_evtadmissao_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class s2200evtAdmissaoList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = s2200evtAdmissao.objects.using(db_slug).all()
    serializer_class = s2200evtAdmissaoSerializer
    permission_classes = (IsAdminUser,)


class s2200evtAdmissaoDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = s2200evtAdmissao.objects.using(db_slug).all()
    serializer_class = s2200evtAdmissaoSerializer
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
        #s2200_evtadmissao_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2200_evtadmissao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_arquivo': 0,
            'show_arquivo_original': 0,
            'show_cadini': 1,
            'show_clauassec': 0,
            'show_codcargo': 0,
            'show_codcarreira': 0,
            'show_codcateg': 1,
            'show_codfuncao': 0,
            'show_codmunic': 0,
            'show_cpftrab': 1,
            'show_dscsalvar': 0,
            'show_dtingrcargo': 0,
            'show_dtingrcarr': 0,
            'show_dtnascto': 1,
            'show_dtterm': 0,
            'show_duracao': 0,
            'show_endereco': 0,
            'show_estciv': 0,
            'show_evtadmissao': 0,
            'show_grauinstr': 1,
            'show_ideempregador': 0,
            'show_ideevento': 0,
            'show_identidade': 1,
            'show_indpriempr': 0,
            'show_indretif': 1,
            'show_infocontrato': 0,
            'show_inforegimetrab': 0,
            'show_matricula': 1,
            'show_nascimento': 0,
            'show_nistrab': 1,
            'show_nmmae': 0,
            'show_nmpai': 0,
            'show_nmsoc': 0,
            'show_nmtrab': 1,
            'show_nrinsc': 1,
            'show_nrrecibo': 0,
            'show_nrrecinfprelim': 0,
            'show_objdet': 0,
            'show_ocorrencias': 0,
            'show_paisnac': 1,
            'show_paisnascto': 1,
            'show_procemi': 1,
            'show_processamento_codigo_resposta': 1,
            'show_processamento_data_hora': 0,
            'show_processamento_descricao_resposta': 0,
            'show_processamento_versao_app_processamento': 0,
            'show_racacor': 1,
            'show_recepcao_data_hora': 0,
            'show_recepcao_protocolo_envio_lote': 0,
            'show_recepcao_tp_amb': 0,
            'show_recepcao_versao_app': 0,
            'show_recibo_hash': 0,
            'show_recibo_numero': 0,
            'show_remuneracao': 0,
            'show_retornos_eventos': 0,
            'show_sexo': 1,
            'show_status': 1,
            'show_tpamb': 1,
            'show_tpcontr': 1,
            'show_tpinsc': 1,
            'show_tpregprev': 1,
            'show_tpregtrab': 1,
            'show_trabalhador': 0,
            'show_transmissor_lote_esocial': 0,
            'show_uf': 0,
            'show_undsalfixo': 1,
            'show_validacao_precedencia': 0,
            'show_validacoes': 0,
            'show_verproc': 1,
            'show_versao': 0,
            'show_vinculo': 0,
            'show_vrsalfx': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'cadini__icontains': 'cadini__icontains',
                'clauassec__icontains': 'clauassec__icontains',
                'codcargo__icontains': 'codcargo__icontains',
                'codcarreira__icontains': 'codcarreira__icontains',
                'codcateg__icontains': 'codcateg__icontains',
                'codfuncao__icontains': 'codfuncao__icontains',
                'codmunic__icontains': 'codmunic__icontains',
                'cpftrab__icontains': 'cpftrab__icontains',
                'dscsalvar__icontains': 'dscsalvar__icontains',
                'dtingrcargo__range': 'dtingrcargo__range',
                'dtingrcarr__range': 'dtingrcarr__range',
                'dtnascto__range': 'dtnascto__range',
                'dtterm__range': 'dtterm__range',
                'duracao': 'duracao',
                'endereco': 'endereco',
                'estciv': 'estciv',
                'evtadmissao': 'evtadmissao',
                'grauinstr__icontains': 'grauinstr__icontains',
                'ideempregador': 'ideempregador',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'indpriempr__icontains': 'indpriempr__icontains',
                'indretif': 'indretif',
                'infocontrato': 'infocontrato',
                'inforegimetrab': 'inforegimetrab',
                'matricula__icontains': 'matricula__icontains',
                'nascimento': 'nascimento',
                'nistrab__icontains': 'nistrab__icontains',
                'nmmae__icontains': 'nmmae__icontains',
                'nmpai__icontains': 'nmpai__icontains',
                'nmsoc__icontains': 'nmsoc__icontains',
                'nmtrab__icontains': 'nmtrab__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'nrrecinfprelim__icontains': 'nrrecinfprelim__icontains',
                'objdet__icontains': 'objdet__icontains',
                'paisnac__icontains': 'paisnac__icontains',
                'paisnascto__icontains': 'paisnascto__icontains',
                'procemi': 'procemi',
                'racacor': 'racacor',
                'remuneracao': 'remuneracao',
                'sexo__icontains': 'sexo__icontains',
                'status': 'status',
                'tpamb': 'tpamb',
                'tpcontr': 'tpcontr',
                'tpinsc': 'tpinsc',
                'tpregprev': 'tpregprev',
                'tpregtrab': 'tpregtrab',
                'trabalhador': 'trabalhador',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',
                'uf__icontains': 'uf__icontains',
                'undsalfixo': 'undsalfixo',
                'verproc__icontains': 'verproc__icontains',
                'versao__icontains': 'versao__icontains',
                'vinculo': 'vinculo',
                'vrsalfx': 'vrsalfx',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'cadini__icontains': 'cadini__icontains',
                'clauassec__icontains': 'clauassec__icontains',
                'codcargo__icontains': 'codcargo__icontains',
                'codcarreira__icontains': 'codcarreira__icontains',
                'codcateg__icontains': 'codcateg__icontains',
                'codfuncao__icontains': 'codfuncao__icontains',
                'codmunic__icontains': 'codmunic__icontains',
                'cpftrab__icontains': 'cpftrab__icontains',
                'dscsalvar__icontains': 'dscsalvar__icontains',
                'dtingrcargo__range': 'dtingrcargo__range',
                'dtingrcarr__range': 'dtingrcarr__range',
                'dtnascto__range': 'dtnascto__range',
                'dtterm__range': 'dtterm__range',
                'duracao': 'duracao',
                'endereco': 'endereco',
                'estciv': 'estciv',
                'evtadmissao': 'evtadmissao',
                'grauinstr__icontains': 'grauinstr__icontains',
                'ideempregador': 'ideempregador',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'indpriempr__icontains': 'indpriempr__icontains',
                'indretif': 'indretif',
                'infocontrato': 'infocontrato',
                'inforegimetrab': 'inforegimetrab',
                'matricula__icontains': 'matricula__icontains',
                'nascimento': 'nascimento',
                'nistrab__icontains': 'nistrab__icontains',
                'nmmae__icontains': 'nmmae__icontains',
                'nmpai__icontains': 'nmpai__icontains',
                'nmsoc__icontains': 'nmsoc__icontains',
                'nmtrab__icontains': 'nmtrab__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'nrrecinfprelim__icontains': 'nrrecinfprelim__icontains',
                'objdet__icontains': 'objdet__icontains',
                'paisnac__icontains': 'paisnac__icontains',
                'paisnascto__icontains': 'paisnascto__icontains',
                'procemi': 'procemi',
                'racacor': 'racacor',
                'remuneracao': 'remuneracao',
                'sexo__icontains': 'sexo__icontains',
                'status': 'status',
                'tpamb': 'tpamb',
                'tpcontr': 'tpcontr',
                'tpinsc': 'tpinsc',
                'tpregprev': 'tpregprev',
                'tpregtrab': 'tpregtrab',
                'trabalhador': 'trabalhador',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',
                'uf__icontains': 'uf__icontains',
                'undsalfixo': 'undsalfixo',
                'verproc__icontains': 'verproc__icontains',
                'versao__icontains': 'versao__icontains',
                'vinculo': 'vinculo',
                'vrsalfx': 'vrsalfx',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s2200_evtadmissao_lista = s2200evtAdmissao.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s2200_evtadmissao_lista) > 100:
            filtrar = True
            s2200_evtadmissao_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
   
        transmissor_lote_esocial_lista = TransmissorLoteEsocial.objects.using( db_slug ).filter(excluido = False).all()
        #s2200_evtadmissao_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2200_evtadmissao'
        context = {
            's2200_evtadmissao_lista': s2200_evtadmissao_lista,
            
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
        #return render(request, 's2200_evtadmissao_listar.html', context)
        if for_print in (0,1):
            return render(request, 's2200_evtadmissao_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2200_evtadmissao_listar.html',
                filename="s2200_evtadmissao.pdf",
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
            response = render_to_response('s2200_evtadmissao_listar.html', context)
            filename = "s2200_evtadmissao.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/s2200_evtadmissao_csv.html', context)
            filename = "s2200_evtadmissao.csv"
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
def identidade_evento(s2200_evtadmissao_id, db_slug):
    from emensageriapro.mensageiro.models import TransmissorEventosEsocial
    dados_evento = s2200evtAdmissao.objects.using( db_slug ).get(id=s2200_evtadmissao_id)
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
            s2200evtAdmissao.objects.using(db_slug).filter(id=s2200_evtadmissao_id).update(identidade=identidade_temp)
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
        s2200_evtadmissao_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2200_evtadmissao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s2200_evtadmissao_id:
        s2200_evtadmissao = get_object_or_404(s2200evtAdmissao.objects.using( db_slug ), excluido = False, id = s2200_evtadmissao_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if s2200_evtadmissao_id:
        if s2200_evtadmissao.status != 0:
            dict_permissoes['s2200_evtadmissao_apagar'] = 0
            dict_permissoes['s2200_evtadmissao_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s2200_evtadmissao_id:
            s2200_evtadmissao_form = form_s2200_evtadmissao(request.POST or None, instance = s2200_evtadmissao, slug = db_slug)
        else:
            s2200_evtadmissao_form = form_s2200_evtadmissao(request.POST or None, slug = db_slug, initial={'versao': VERSAO_LAYOUT_ESOCIAL, 'status': 0, 'processamento_codigo_resposta': 0, 'tpamb': TP_AMB, 'procemi': 1, 'verproc': VERSAO_EMENSAGERIA})
        if request.method == 'POST':
            if s2200_evtadmissao_form.is_valid():
                dados = s2200_evtadmissao_form.cleaned_data
                import json
                from django.forms.models import model_to_dict
                if s2200_evtadmissao_id:
                    if s2200_evtadmissao.status == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #s2200_evtadmissao_campos_multiple_passo1
                        s2200evtAdmissao.objects.using(db_slug).filter(id=s2200_evtadmissao_id).update(**dados)
                        obj = s2200evtAdmissao.objects.using(db_slug).get(id=s2200_evtadmissao_id)
                        #s2200_evtadmissao_editar_custom
                        #s2200_evtadmissao_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(s2200_evtadmissao), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         's2200_evtadmissao', s2200_evtadmissao_id, usuario_id, 2)
                    else:
                        obj = s2200evtAdmissao.objects.using(db_slug).get(id=s2200_evtadmissao_id)
                        messages.error(request, 'Não é possível salvar o evento, pois o mesmo não está com o status "Cadastrado"!')

                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #s2200_evtadmissao_cadastrar_campos_multiple_passo1
                    obj = s2200evtAdmissao(**dados)
                    obj.save(using = db_slug)
                    #s2200_evtadmissao_cadastrar_custom
                    #s2200_evtadmissao_cadastrar_campos_multiple_passo2
                    identidade_evento(obj.id, db_slug)
                    messages.success(request, 'Cadastrado com sucesso!')
                    s2200_evtadmissao_form = form_s2200_evtadmissao(request.POST or None, instance = obj, slug = db_slug)
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's2200_evtadmissao', obj.id, usuario_id, 1)
                if request.session['retorno_pagina'] not in ('s2200_evtadmissao_apagar', 's2200_evtadmissao_salvar', 's2200_evtadmissao'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s2200_evtadmissao_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2200_evtadmissao_salvar', hash=url_hash)

            else:
                messages.error(request, 'Erro ao salvar!')
        s2200_evtadmissao_form = disabled_form_fields(s2200_evtadmissao_form, permissao.permite_editar)
    
        if s2200_evtadmissao_id:
            if s2200_evtadmissao.status != 0:
                s2200_evtadmissao_form = disabled_form_fields(s2200_evtadmissao_form, False)
        #s2200_evtadmissao_campos_multiple_passo3

        for field in s2200_evtadmissao_form.fields.keys():
            s2200_evtadmissao_form.fields[field].widget.attrs['ng-model'] = 's2200_evtadmissao_'+field
        if int(dict_hash['print']):
            s2200_evtadmissao_form = disabled_form_for_print(s2200_evtadmissao_form)
   
        s2200_ctps_form = None
        s2200_ctps_lista = None
        s2200_ric_form = None
        s2200_ric_lista = None
        s2200_rg_form = None
        s2200_rg_lista = None
        s2200_rne_form = None
        s2200_rne_lista = None
        s2200_oc_form = None
        s2200_oc_lista = None
        s2200_cnh_form = None
        s2200_cnh_lista = None
        s2200_brasil_form = None
        s2200_brasil_lista = None
        s2200_exterior_form = None
        s2200_exterior_lista = None
        s2200_trabestrangeiro_form = None
        s2200_trabestrangeiro_lista = None
        s2200_infodeficiencia_form = None
        s2200_infodeficiencia_lista = None
        s2200_dependente_form = None
        s2200_dependente_lista = None
        s2200_aposentadoria_form = None
        s2200_aposentadoria_lista = None
        s2200_contato_form = None
        s2200_contato_lista = None
        s2200_infoceletista_form = None
        s2200_infoceletista_lista = None
        s2200_infoestatutario_form = None
        s2200_infoestatutario_lista = None
        s2200_localtrabgeral_form = None
        s2200_localtrabgeral_lista = None
        s2200_localtrabdom_form = None
        s2200_localtrabdom_lista = None
        s2200_horcontratual_form = None
        s2200_horcontratual_lista = None
        s2200_filiacaosindical_form = None
        s2200_filiacaosindical_lista = None
        s2200_alvarajudicial_form = None
        s2200_alvarajudicial_lista = None
        s2200_observacoes_form = None
        s2200_observacoes_lista = None
        s2200_sucessaovinc_form = None
        s2200_sucessaovinc_lista = None
        s2200_transfdom_form = None
        s2200_transfdom_lista = None
        s2200_mudancacpf_form = None
        s2200_mudancacpf_lista = None
        s2200_afastamento_form = None
        s2200_afastamento_lista = None
        s2200_desligamento_form = None
        s2200_desligamento_lista = None
        s2200_cessao_form = None
        s2200_cessao_lista = None
        if s2200_evtadmissao_id:
            s2200_evtadmissao = get_object_or_404(s2200evtAdmissao.objects.using( db_slug ), excluido = False, id = s2200_evtadmissao_id)
       
            s2200_ctps_form = form_s2200_ctps(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_ctps_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_ctps_lista = s2200CTPS.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_ric_form = form_s2200_ric(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_ric_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_ric_lista = s2200RIC.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_rg_form = form_s2200_rg(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_rg_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_rg_lista = s2200RG.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_rne_form = form_s2200_rne(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_rne_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_rne_lista = s2200RNE.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_oc_form = form_s2200_oc(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_oc_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_oc_lista = s2200OC.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_cnh_form = form_s2200_cnh(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_cnh_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_cnh_lista = s2200CNH.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_brasil_form = form_s2200_brasil(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_brasil_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_brasil_lista = s2200brasil.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_exterior_form = form_s2200_exterior(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_exterior_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_exterior_lista = s2200exterior.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_trabestrangeiro_form = form_s2200_trabestrangeiro(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_trabestrangeiro_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_trabestrangeiro_lista = s2200trabEstrangeiro.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_infodeficiencia_form = form_s2200_infodeficiencia(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_infodeficiencia_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_infodeficiencia_lista = s2200infoDeficiencia.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_dependente_form = form_s2200_dependente(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_dependente_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_dependente_lista = s2200dependente.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_aposentadoria_form = form_s2200_aposentadoria(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_aposentadoria_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_aposentadoria_lista = s2200aposentadoria.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_contato_form = form_s2200_contato(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_contato_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_contato_lista = s2200contato.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_infoceletista_form = form_s2200_infoceletista(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_infoceletista_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_infoceletista_lista = s2200infoCeletista.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_infoestatutario_form = form_s2200_infoestatutario(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_infoestatutario_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_infoestatutario_lista = s2200infoEstatutario.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_localtrabgeral_form = form_s2200_localtrabgeral(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_localtrabgeral_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_localtrabgeral_lista = s2200localTrabGeral.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_localtrabdom_form = form_s2200_localtrabdom(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_localtrabdom_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_localtrabdom_lista = s2200localTrabDom.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_horcontratual_form = form_s2200_horcontratual(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_horcontratual_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_horcontratual_lista = s2200horContratual.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_filiacaosindical_form = form_s2200_filiacaosindical(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_filiacaosindical_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_filiacaosindical_lista = s2200filiacaoSindical.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_alvarajudicial_form = form_s2200_alvarajudicial(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_alvarajudicial_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_alvarajudicial_lista = s2200alvaraJudicial.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_observacoes_form = form_s2200_observacoes(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_observacoes_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_observacoes_lista = s2200observacoes.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_sucessaovinc_form = form_s2200_sucessaovinc(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_sucessaovinc_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_sucessaovinc_lista = s2200sucessaoVinc.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_transfdom_form = form_s2200_transfdom(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_transfdom_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_transfdom_lista = s2200transfDom.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_mudancacpf_form = form_s2200_mudancacpf(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_mudancacpf_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_mudancacpf_lista = s2200mudancaCPF.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_afastamento_form = form_s2200_afastamento(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_afastamento_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_afastamento_lista = s2200afastamento.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_desligamento_form = form_s2200_desligamento(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_desligamento_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_desligamento_lista = s2200desligamento.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_cessao_form = form_s2200_cessao(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_cessao_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_cessao_lista = s2200cessao.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
        else:
            s2200_evtadmissao = None
        #s2200_evtadmissao_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if 's2200_evtadmissao'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False
        if not evento_totalizador:
            s2200_evtadmissao_form.fields['tpamb'].widget.attrs['disabled'] = True
            s2200_evtadmissao_form.fields['tpamb'].widget.attrs['readonly'] = True
            s2200_evtadmissao_form.fields['tpamb'].value = TP_AMB
            s2200_evtadmissao_form.fields['procemi'].widget.attrs['disabled'] = True
            s2200_evtadmissao_form.fields['procemi'].widget.attrs['readonly'] = True
            s2200_evtadmissao_form.fields['procemi'].value = 1
            s2200_evtadmissao_form.fields['verproc'].widget.attrs['readonly'] = True
            s2200_evtadmissao_form.fields['verproc'].value = VERSAO_EMENSAGERIA
    
        if dict_hash['tab'] or 's2200_evtadmissao' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2200_evtadmissao_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s2200_evtadmissao_id, tabela='s2200_evtadmissao').all()
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            's2200_evtadmissao': s2200_evtadmissao,
            's2200_evtadmissao_form': s2200_evtadmissao_form,
            'mensagem': mensagem,
            's2200_evtadmissao_id': int(s2200_evtadmissao_id),
            'usuario': usuario,
            
            'hash': hash,
       
            's2200_ctps_form': s2200_ctps_form,
            's2200_ctps_lista': s2200_ctps_lista,
            's2200_ric_form': s2200_ric_form,
            's2200_ric_lista': s2200_ric_lista,
            's2200_rg_form': s2200_rg_form,
            's2200_rg_lista': s2200_rg_lista,
            's2200_rne_form': s2200_rne_form,
            's2200_rne_lista': s2200_rne_lista,
            's2200_oc_form': s2200_oc_form,
            's2200_oc_lista': s2200_oc_lista,
            's2200_cnh_form': s2200_cnh_form,
            's2200_cnh_lista': s2200_cnh_lista,
            's2200_brasil_form': s2200_brasil_form,
            's2200_brasil_lista': s2200_brasil_lista,
            's2200_exterior_form': s2200_exterior_form,
            's2200_exterior_lista': s2200_exterior_lista,
            's2200_trabestrangeiro_form': s2200_trabestrangeiro_form,
            's2200_trabestrangeiro_lista': s2200_trabestrangeiro_lista,
            's2200_infodeficiencia_form': s2200_infodeficiencia_form,
            's2200_infodeficiencia_lista': s2200_infodeficiencia_lista,
            's2200_dependente_form': s2200_dependente_form,
            's2200_dependente_lista': s2200_dependente_lista,
            's2200_aposentadoria_form': s2200_aposentadoria_form,
            's2200_aposentadoria_lista': s2200_aposentadoria_lista,
            's2200_contato_form': s2200_contato_form,
            's2200_contato_lista': s2200_contato_lista,
            's2200_infoceletista_form': s2200_infoceletista_form,
            's2200_infoceletista_lista': s2200_infoceletista_lista,
            's2200_infoestatutario_form': s2200_infoestatutario_form,
            's2200_infoestatutario_lista': s2200_infoestatutario_lista,
            's2200_localtrabgeral_form': s2200_localtrabgeral_form,
            's2200_localtrabgeral_lista': s2200_localtrabgeral_lista,
            's2200_localtrabdom_form': s2200_localtrabdom_form,
            's2200_localtrabdom_lista': s2200_localtrabdom_lista,
            's2200_horcontratual_form': s2200_horcontratual_form,
            's2200_horcontratual_lista': s2200_horcontratual_lista,
            's2200_filiacaosindical_form': s2200_filiacaosindical_form,
            's2200_filiacaosindical_lista': s2200_filiacaosindical_lista,
            's2200_alvarajudicial_form': s2200_alvarajudicial_form,
            's2200_alvarajudicial_lista': s2200_alvarajudicial_lista,
            's2200_observacoes_form': s2200_observacoes_form,
            's2200_observacoes_lista': s2200_observacoes_lista,
            's2200_sucessaovinc_form': s2200_sucessaovinc_form,
            's2200_sucessaovinc_lista': s2200_sucessaovinc_lista,
            's2200_transfdom_form': s2200_transfdom_form,
            's2200_transfdom_lista': s2200_transfdom_lista,
            's2200_mudancacpf_form': s2200_mudancacpf_form,
            's2200_mudancacpf_lista': s2200_mudancacpf_lista,
            's2200_afastamento_form': s2200_afastamento_form,
            's2200_afastamento_lista': s2200_afastamento_lista,
            's2200_desligamento_form': s2200_desligamento_form,
            's2200_desligamento_lista': s2200_desligamento_lista,
            's2200_cessao_form': s2200_cessao_form,
            's2200_cessao_lista': s2200_cessao_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2200_evtadmissao_salvar_custom_variaveis_context#
        }
    
        if for_print in (0,1 ):
            return render(request, 's2200_evtadmissao_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2200_evtadmissao_salvar.html',
                filename="s2200_evtadmissao.pdf",
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
            response = render_to_response('s2200_evtadmissao_salvar.html', context)
            filename = "s2200_evtadmissao.xls"
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

