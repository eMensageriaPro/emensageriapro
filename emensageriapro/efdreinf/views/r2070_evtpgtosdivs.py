#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"



import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import *
import base64
from emensageriapro.r2070.models import r2070infoResidExt
from emensageriapro.r2070.models import r2070infoMolestia
from emensageriapro.r2070.models import r2070ideEstab
from emensageriapro.r2070.forms import form_r2070_inforesidext
from emensageriapro.r2070.forms import form_r2070_infomolestia
from emensageriapro.r2070.forms import form_r2070_ideestab

#IMPORTACOES


#view_identidade_evento#
def identidade_evento(r2070_evtpgtosdivs_id, db_slug):
    from emensageriapro.mensageiro.models import TransmissorEventosEfdreinf
    dados_evento = r2070evtPgtosDivs.objects.using( db_slug ).get(id=r2070_evtpgtosdivs_id)
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
        lista_eventos = TransmissorEventosEfdreinf.objects.using(db_slug).filter(criado_em=dados_evento.criado_em,
                                                                         excluido=False, identidade = identidade_temp).all()
        if not lista_eventos:
            r2070evtPgtosDivs.objects.using(db_slug).filter(id=r2070_evtpgtosdivs_id).update(identidade=identidade_temp)
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
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_EFDREINF, TP_AMB
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r2070_evtpgtosdivs_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2070_evtpgtosdivs')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if r2070_evtpgtosdivs_id:
        r2070_evtpgtosdivs = get_object_or_404(r2070evtPgtosDivs.objects.using( db_slug ), excluido = False, id = r2070_evtpgtosdivs_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if r2070_evtpgtosdivs_id:
        if r2070_evtpgtosdivs.status != 0:
            dict_permissoes['r2070_evtpgtosdivs_apagar'] = 0
            dict_permissoes['r2070_evtpgtosdivs_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if r2070_evtpgtosdivs_id:
            r2070_evtpgtosdivs_form = form_r2070_evtpgtosdivs(request.POST or None, instance = r2070_evtpgtosdivs, slug = db_slug)
        else:
            r2070_evtpgtosdivs_form = form_r2070_evtpgtosdivs(request.POST or None, slug = db_slug, initial={'versao': VERSAO_LAYOUT_EFDREINF, 'processamento_codigo_resposta': 0, 'tpamb': TP_AMB, 'procemi': 1, 'verproc': VERSAO_EMENSAGERIA})
        if request.method == 'POST':
            if r2070_evtpgtosdivs_form.is_valid():
                dados = r2070_evtpgtosdivs_form.cleaned_data
                import json
                from django.forms.models import model_to_dict
                if r2070_evtpgtosdivs_id:
                    if r2070_evtpgtosdivs.status == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #r2070_evtpgtosdivs_campos_multiple_passo1
                        r2070evtPgtosDivs.objects.using(db_slug).filter(id=r2070_evtpgtosdivs_id).update(**dados)
                        obj = r2070evtPgtosDivs.objects.using(db_slug).get(id=r2070_evtpgtosdivs_id)
                        #r2070_evtpgtosdivs_editar_custom
                        #r2070_evtpgtosdivs_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(r2070_evtpgtosdivs), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         'r2070_evtpgtosdivs', r2070_evtpgtosdivs_id, usuario_id, 2)
                    else:
                        messages.error(request, 'Não é possível salvar o evento, pois o mesmo não está com o status "Cadastrado"!')

                else:
                    dados['arquivo_original'] = 0

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #r2070_evtpgtosdivs_cadastrar_campos_multiple_passo1
                    obj = r2070evtPgtosDivs(**dados)
                    obj.save(using = db_slug)
                    #r2070_evtpgtosdivs_cadastrar_custom
                    #r2070_evtpgtosdivs_cadastrar_campos_multiple_passo2
                    identidade_evento(obj.id, db_slug)
                    messages.success(request, 'Cadastrado com sucesso!')
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     'r2070_evtpgtosdivs', obj.id, usuario_id, 1)
                if request.session['retorno_pagina'] not in ('r2070_evtpgtosdivs_apagar', 'r2070_evtpgtosdivs_salvar', 'r2070_evtpgtosdivs'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if r2070_evtpgtosdivs_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('r2070_evtpgtosdivs_salvar', hash=url_hash)

            else:
                messages.error(request, 'Erro ao salvar!')
        r2070_evtpgtosdivs_form = disabled_form_fields(r2070_evtpgtosdivs_form, permissao.permite_editar)
    
        if r2070_evtpgtosdivs_id:
            if r2070_evtpgtosdivs.status != 0:
                r2070_evtpgtosdivs_form = disabled_form_fields(r2070_evtpgtosdivs_form, False)
        #r2070_evtpgtosdivs_campos_multiple_passo3

        for field in r2070_evtpgtosdivs_form.fields.keys():
            r2070_evtpgtosdivs_form.fields[field].widget.attrs['ng-model'] = 'r2070_evtpgtosdivs_'+field
        if int(dict_hash['print']):
            r2070_evtpgtosdivs_form = disabled_form_for_print(r2070_evtpgtosdivs_form)
   
        r2070_inforesidext_form = None
        r2070_inforesidext_lista = None
        r2070_infomolestia_form = None
        r2070_infomolestia_lista = None
        r2070_ideestab_form = None
        r2070_ideestab_lista = None
        if r2070_evtpgtosdivs_id:
            r2070_evtpgtosdivs = get_object_or_404(r2070evtPgtosDivs.objects.using( db_slug ), excluido = False, id = r2070_evtpgtosdivs_id)
       
            r2070_inforesidext_form = form_r2070_inforesidext(initial={ 'r2070_evtpgtosdivs': r2070_evtpgtosdivs }, slug=db_slug)
            r2070_inforesidext_form.fields['r2070_evtpgtosdivs'].widget.attrs['readonly'] = True
            r2070_inforesidext_lista = r2070infoResidExt.objects.using( db_slug ).filter(excluido = False, r2070_evtpgtosdivs_id=r2070_evtpgtosdivs.id).all()
            r2070_infomolestia_form = form_r2070_infomolestia(initial={ 'r2070_evtpgtosdivs': r2070_evtpgtosdivs }, slug=db_slug)
            r2070_infomolestia_form.fields['r2070_evtpgtosdivs'].widget.attrs['readonly'] = True
            r2070_infomolestia_lista = r2070infoMolestia.objects.using( db_slug ).filter(excluido = False, r2070_evtpgtosdivs_id=r2070_evtpgtosdivs.id).all()
            r2070_ideestab_form = form_r2070_ideestab(initial={ 'r2070_evtpgtosdivs': r2070_evtpgtosdivs }, slug=db_slug)
            r2070_ideestab_form.fields['r2070_evtpgtosdivs'].widget.attrs['readonly'] = True
            r2070_ideestab_lista = r2070ideEstab.objects.using( db_slug ).filter(excluido = False, r2070_evtpgtosdivs_id=r2070_evtpgtosdivs.id).all()
        else:
            r2070_evtpgtosdivs = None
        #r2070_evtpgtosdivs_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if 'r2070_evtpgtosdivs'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False
        if not evento_totalizador:
            r2070_evtpgtosdivs_form.fields['tpamb'].widget.attrs['disabled'] = True
            r2070_evtpgtosdivs_form.fields['tpamb'].widget.attrs['readonly'] = True
            r2070_evtpgtosdivs_form.fields['tpamb'].value = TP_AMB
            r2070_evtpgtosdivs_form.fields['procemi'].widget.attrs['disabled'] = True
            r2070_evtpgtosdivs_form.fields['procemi'].widget.attrs['readonly'] = True
            r2070_evtpgtosdivs_form.fields['procemi'].value = 1
            r2070_evtpgtosdivs_form.fields['verproc'].widget.attrs['readonly'] = True
            r2070_evtpgtosdivs_form.fields['verproc'].value = VERSAO_EMENSAGERIA
    
        if dict_hash['tab'] or 'r2070_evtpgtosdivs' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r2070_evtpgtosdivs_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=r2070_evtpgtosdivs_id, tabela='r2070_evtpgtosdivs').all()
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            'r2070_evtpgtosdivs': r2070_evtpgtosdivs,
            'r2070_evtpgtosdivs_form': r2070_evtpgtosdivs_form,
            'mensagem': mensagem,
            'r2070_evtpgtosdivs_id': int(r2070_evtpgtosdivs_id),
            'usuario': usuario,
            
            'hash': hash,
       
            'r2070_inforesidext_form': r2070_inforesidext_form,
            'r2070_inforesidext_lista': r2070_inforesidext_lista,
            'r2070_infomolestia_form': r2070_infomolestia_form,
            'r2070_infomolestia_lista': r2070_infomolestia_lista,
            'r2070_ideestab_form': r2070_ideestab_form,
            'r2070_ideestab_lista': r2070_ideestab_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r2070_evtpgtosdivs_salvar_custom_variaveis_context#
        }
    
        if for_print in (0,1 ):
            return render(request, 'r2070_evtpgtosdivs_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r2070_evtpgtosdivs_salvar.html',
                filename="r2070_evtpgtosdivs.pdf",
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
            response = render_to_response('r2070_evtpgtosdivs_salvar.html', context)
            filename = "r2070_evtpgtosdivs.xls"
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

@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r2070_evtpgtosdivs_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2070_evtpgtosdivs')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    r2070_evtpgtosdivs = get_object_or_404(r2070evtPgtosDivs.objects.using( db_slug ), excluido = False, id = r2070_evtpgtosdivs_id)

    if r2070_evtpgtosdivs_id:
        if r2070_evtpgtosdivs.status != 0:
            dict_permissoes['r2070_evtpgtosdivs_apagar'] = 0
            dict_permissoes['r2070_evtpgtosdivs_editar'] = 0

    if request.method == 'POST':
        if r2070_evtpgtosdivs.status == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(r2070_evtpgtosdivs), indent=4, sort_keys=True, default=str)
            r2070evtPgtosDivs.objects.using( db_slug ).filter(id = r2070_evtpgtosdivs_id).delete()
            #r2070_evtpgtosdivs_apagar_custom
            #r2070_evtpgtosdivs_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             'r2070_evtpgtosdivs', r2070_evtpgtosdivs_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')
        
        if request.session['retorno_pagina']== 'r2070_evtpgtosdivs_salvar':
            return redirect('r2070_evtpgtosdivs', hash=request.session['retorno_hash'])
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
    return render(request, 'r2070_evtpgtosdivs_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class r2070evtPgtosDivsList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = r2070evtPgtosDivs.objects.using(db_slug).all()
    serializer_class = r2070evtPgtosDivsSerializer
    permission_classes = (IsAdminUser,)


class r2070evtPgtosDivsDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = r2070evtPgtosDivs.objects.using(db_slug).all()
    serializer_class = r2070evtPgtosDivsSerializer
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
        #r2070_evtpgtosdivs_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2070_evtpgtosdivs')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_excluido': 0,
            'show_modificado_por': 0,
            'show_modificado_em': 0,
            'show_criado_por': 0,
            'show_criado_em': 0,
            'show_infopgto': 0,
            'show_nmrazaobenef': 1,
            'show_nrinscbenef': 0,
            'show_tpinscbenef': 0,
            'show_codpgto': 1,
            'show_idebenef': 0,
            'show_nrinsc': 0,
            'show_tpinsc': 0,
            'show_idecontri': 0,
            'show_verproc': 0,
            'show_procemi': 0,
            'show_tpamb': 0,
            'show_perapur': 1,
            'show_nrrecibo': 0,
            'show_indretif': 1,
            'show_ideevento': 0,
            'show_identidade': 1,
            'show_evtpgtosdivs': 0,
            'show_dhprocess': 0,
            'show_descretorno': 0,
            'show_cdretorno': 1,
            'show_status': 1,
            'show_versao': 0,
            'show_transmissor_lote_efdreinf': 0,
            'show_arquivo': 0,
            'show_arquivo_original': 0,
            'show_validacoes': 0,
            'show_validacao_precedencia': 0,
            'show_ocorrencias': 0,
            'show_retornos_evttotalcontrib': 0,
            'show_retornos_evttotal': 0, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'infopgto': 'infopgto',
                'nmrazaobenef__icontains': 'nmrazaobenef__icontains',
                'nrinscbenef__icontains': 'nrinscbenef__icontains',
                'tpinscbenef': 'tpinscbenef',
                'codpgto': 'codpgto',
                'idebenef': 'idebenef',
                'nrinsc__icontains': 'nrinsc__icontains',
                'tpinsc': 'tpinsc',
                'idecontri': 'idecontri',
                'verproc__icontains': 'verproc__icontains',
                'procemi': 'procemi',
                'tpamb': 'tpamb',
                'perapur__icontains': 'perapur__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'indretif': 'indretif',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'evtpgtosdivs': 'evtpgtosdivs',
                'status': 'status',
                'versao__icontains': 'versao__icontains',
                'transmissor_lote_efdreinf': 'transmissor_lote_efdreinf',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'infopgto': 'infopgto',
                'nmrazaobenef__icontains': 'nmrazaobenef__icontains',
                'nrinscbenef__icontains': 'nrinscbenef__icontains',
                'tpinscbenef': 'tpinscbenef',
                'codpgto': 'codpgto',
                'idebenef': 'idebenef',
                'nrinsc__icontains': 'nrinsc__icontains',
                'tpinsc': 'tpinsc',
                'idecontri': 'idecontri',
                'verproc__icontains': 'verproc__icontains',
                'procemi': 'procemi',
                'tpamb': 'tpamb',
                'perapur__icontains': 'perapur__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'indretif': 'indretif',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'evtpgtosdivs': 'evtpgtosdivs',
                'status': 'status',
                'versao__icontains': 'versao__icontains',
                'transmissor_lote_efdreinf': 'transmissor_lote_efdreinf',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        r2070_evtpgtosdivs_lista = r2070evtPgtosDivs.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(r2070_evtpgtosdivs_lista) > 100:
            filtrar = True
            r2070_evtpgtosdivs_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
   
        transmissor_lote_efdreinf_lista = TransmissorLoteEfdreinf.objects.using( db_slug ).filter(excluido = False).all()
        #r2070_evtpgtosdivs_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r2070_evtpgtosdivs'
        context = {
            'r2070_evtpgtosdivs_lista': r2070_evtpgtosdivs_lista,
            
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
       
            'transmissor_lote_efdreinf_lista': transmissor_lote_efdreinf_lista,
        }
        #return render(request, 'r2070_evtpgtosdivs_listar.html', context)
        if for_print in (0,1):
            return render(request, 'r2070_evtpgtosdivs_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r2070_evtpgtosdivs_listar.html',
                filename="r2070_evtpgtosdivs.pdf",
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
            response = render_to_response('r2070_evtpgtosdivs_listar.html', context)
            filename = "r2070_evtpgtosdivs.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/r2070_evtpgtosdivs_csv.html', context)
            filename = "r2070_evtpgtosdivs.csv"
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

