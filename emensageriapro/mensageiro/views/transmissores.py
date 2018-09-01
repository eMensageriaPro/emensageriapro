#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"



import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        transmissores_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissores')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    transmissores = get_object_or_404(TransmissorLote.objects.using( db_slug ), excluido = False, id = transmissores_id)
    if request.method == 'POST':
        TransmissorLote.objects.using( db_slug ).filter(id = transmissores_id).update(excluido = True)
        #transmissores_apagar_custom
        #transmissores_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'transmissores_salvar':
            return redirect('transmissores', hash=request.session['retorno_hash'])
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
    return render(request, 'transmissores_apagar.html', context)

def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        transmissores_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissores')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if transmissores_id:
        transmissores = get_object_or_404(TransmissorLote.objects.using( db_slug ), excluido = False, id = transmissores_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if transmissores_id:
            transmissores_form = form_transmissores(request.POST or None, instance = transmissores, slug = db_slug)
        else:
            transmissores_form = form_transmissores(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if transmissores_form.is_valid():
                dados = transmissores_form.cleaned_data
                if transmissores_id:
                    if request.FILES:
                        from emensageriapro.settings import BASE_DIR
                        from django.core.files.storage import FileSystemStorage
                        if bool(request.FILES.get('logotipo', False)) == True:
                            myfile = request.FILES['logotipo']
                            fs = FileSystemStorage(location=BASE_DIR+'/media/')
                            filename = fs.save(myfile.name, myfile)
                            dados['logotipo'] = filename
                            messages.success(request, 'Arquivo %s salvo com sucesso!' % filename)

                        files = ['esocial_certificado','efdreinf_certificado']
                        for f in files:
                            if bool(request.FILES.get(f, False)) == True:
                                myfile = request.FILES[f]
                                fs = FileSystemStorage(location=BASE_DIR+'/certificados/')
                                filename = fs.save(myfile.name, myfile)
                                dados[f] = filename
                                messages.success(request, 'Arquivo %s salvo com sucesso!' % filename)
                dados = transmissores_form.cleaned_data
                if transmissores_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #transmissores_campos_multiple_passo1
                    TransmissorLote.objects.using(db_slug).filter(id=transmissores_id).update(**dados)
                    obj = TransmissorLote.objects.using(db_slug).get(id=transmissores_id)
                    #transmissores_editar_custom
                    #transmissores_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #transmissores_cadastrar_campos_multiple_passo1
                    obj = TransmissorLote(**dados)
                    obj.save(using = db_slug)
                    #transmissores_cadastrar_custom
                    #transmissores_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('transmissores_apagar', 'transmissores_salvar', 'transmissores'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if transmissores_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('transmissores_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        transmissores_form = disabled_form_fields(transmissores_form, permissao.permite_editar)
        #transmissores_campos_multiple_passo3

        for field in transmissores_form.fields.keys():
            transmissores_form.fields[field].widget.attrs['ng-model'] = 'transmissores_'+field
        if int(dict_hash['print']):
            transmissores_form = disabled_form_for_print(transmissores_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if transmissores_id:
            transmissores = get_object_or_404(TransmissorLote.objects.using( db_slug ), excluido = False, id = transmissores_id)
            pass
        else:
            transmissores = None
        #transmissores_salvar_custom_variaveis#
        if transmissores.esocial_tempo_prox_envio > transmissores.esocial_intervalo:
            TransmissorLote.objects.using(db_slug).\
                filter(id=transmissores_id).update(esocial_tempo_prox_envio=transmissores.esocial_intervalo)
        if transmissores.efdreinf_tempo_prox_envio > transmissores.efdreinf_intervalo:
            TransmissorLote.objects.using(db_slug).\
                filter(id=transmissores_id).update(efdreinf_tempo_prox_envio=transmissores.efdreinf_intervalo)

        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'transmissores' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'transmissores_salvar'
        context = {
            'transmissores': transmissores,
            'transmissores_form': transmissores_form,
            'mensagem': mensagem,
            'transmissores_id': int(transmissores_id),
            'usuario': usuario,

            'hash': hash,
            #[VARIAVEIS_SECUNDARIAS]
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #transmissores_salvar_custom_variaveis_context#
        }
        return render(request, 'transmissores_salvar.html', context)
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

def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #transmissores_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissores')
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
            'show_efdreinf_pasta': 0,
            'show_efdreinf_senha': 0,
            'show_efdreinf_certificado': 0,
            'show_efdreinf_tempo_prox_envio': 0,
            'show_efdreinf_intervalo': 0,
            'show_efdreinf_timeout': 0,
            'show_efdreinf_lote_max': 0,
            'show_efdreinf_lote_min': 0,
            'show_efdreinf': 0,
            'show_esocial_pasta': 0,
            'show_esocial_senha': 0,
            'show_esocial_certificado': 0,
            'show_esocial_tempo_prox_envio': 0,
            'show_esocial_intervalo': 0,
            'show_esocial_timeout': 0,
            'show_esocial_lote_max': 0,
            'show_esocial_lote_min': 0,
            'show_eSocial': 0,
            'show_endereco_completo': 0,
            'show_logotipo': 0,
            'show_envio_automatico': 0,
            'show_validar_eventos': 0,
            'show_data_abertura': 0,
            'show_tipo_inscricao': 1,
            'show_cpf_cnpj': 1,
            'show_nome_empresa': 1, }
        post = False
        #ANTES-POST-LISTAGEM
        if request.method == 'POST':
            post = True
            dict_fields = {
                'efdreinf_tempo_prox_envio': 'efdreinf_tempo_prox_envio',
                'efdreinf_intervalo': 'efdreinf_intervalo',
                'efdreinf_timeout': 'efdreinf_timeout',
                'efdreinf_lote_max': 'efdreinf_lote_max',
                'efdreinf_lote_min': 'efdreinf_lote_min',
                'efdreinf': 'efdreinf',
                'esocial_tempo_prox_envio': 'esocial_tempo_prox_envio',
                'esocial_intervalo': 'esocial_intervalo',
                'esocial_timeout': 'esocial_timeout',
                'esocial_lote_max': 'esocial_lote_max',
                'esocial_lote_min': 'esocial_lote_min',
                'eSocial': 'eSocial',
                'endereco_completo__icontains': 'endereco_completo__icontains',
                'logotipo': 'logotipo',
                'envio_automatico': 'envio_automatico',
                'validar_eventos': 'validar_eventos',
                'data_abertura__range': 'data_abertura__range',
                'tipo_inscricao': 'tipo_inscricao',
                'cpf_cnpj__icontains': 'cpf_cnpj__icontains',
                'nome_empresa__icontains': 'nome_empresa__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'efdreinf_tempo_prox_envio': 'efdreinf_tempo_prox_envio',
                'efdreinf_intervalo': 'efdreinf_intervalo',
                'efdreinf_timeout': 'efdreinf_timeout',
                'efdreinf_lote_max': 'efdreinf_lote_max',
                'efdreinf_lote_min': 'efdreinf_lote_min',
                'efdreinf': 'efdreinf',
                'esocial_tempo_prox_envio': 'esocial_tempo_prox_envio',
                'esocial_intervalo': 'esocial_intervalo',
                'esocial_timeout': 'esocial_timeout',
                'esocial_lote_max': 'esocial_lote_max',
                'esocial_lote_min': 'esocial_lote_min',
                'eSocial': 'eSocial',
                'endereco_completo__icontains': 'endereco_completo__icontains',
                'logotipo': 'logotipo',
                'envio_automatico': 'envio_automatico',
                'validar_eventos': 'validar_eventos',
                'data_abertura__range': 'data_abertura__range',
                'tipo_inscricao': 'tipo_inscricao',
                'cpf_cnpj__icontains': 'cpf_cnpj__icontains',
                'nome_empresa__icontains': 'nome_empresa__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        transmissores_lista = TransmissorLote.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(transmissores_lista) > 100:
            filtrar = True
            transmissores_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #transmissores_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'transmissores'
        context = {
            'transmissores_lista': transmissores_lista,

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

        }
        return render(request, 'transmissores_listar.html', context)
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

