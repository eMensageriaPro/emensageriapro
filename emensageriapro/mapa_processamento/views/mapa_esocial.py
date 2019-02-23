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
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES





@login_required
def listar(request, hash):
    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
        STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
        STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
        STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
        STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
        STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
        STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO
    for_print = 0
    db_slug = 'default'
    from emensageriapro.controle_de_acesso.views.login import criar_permissoes, salvar_modulos_paginas_permitidas
    criar_permissoes(db_slug)
    salvar_modulos_paginas_permitidas(db_slug)
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #importacao_arquivos_eventos_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='importacao_arquivos_eventos')
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
            'show_validacoes': 0,
            'show_data_hora': 1,
            'show_status': 1,
            'show_identidade': 0,
            'show_identidade_evento': 1,
            'show_versao': 0,
            'show_evento': 1,
            'show_arquivo': 1,
            'show_importacao_arquivos': 0, }
        post = False
        #ANTES-POST-LISTAGEM
        if request.method == 'POST':
            post = True
            dict_fields = {
                'validacoes__icontains': 'validacoes__icontains',
                'data_hora__range': 'data_hora__range',
                'status': 'status',
                'identidade': 'identidade',
                'identidade_evento__icontains': 'identidade_evento__icontains',
                'versao__icontains': 'versao__icontains',
                'evento__icontains': 'evento__icontains',
                'arquivo__icontains': 'arquivo__icontains',
                'importacao_arquivos': 'importacao_arquivos',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'validacoes__icontains': 'validacoes__icontains',
                'data_hora__range': 'data_hora__range',
                'status': 'status',
                'identidade': 'identidade',
                'identidade_evento__icontains': 'identidade_evento__icontains',
                'versao__icontains': 'versao__icontains',
                'evento__icontains': 'evento__icontains',
                'arquivo__icontains': 'arquivo__icontains',
                'importacao_arquivos': 'importacao_arquivos',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)

        esocial_enviados = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False,
                   status=STATUS_EVENTO_ENVIADO).exclude(id=0).all()

        esocial_validados_aguardando_envio = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False,
                   status=STATUS_EVENTO_AGUARD_ENVIO,
                   validacao_precedencia=1).exclude(id=0).all()

        esocial_validados_aguardando_precedencia = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False,
                   status=STATUS_EVENTO_AGUARD_PRECEDENCIA,
                   validacao_precedencia=0).exclude(id=0).all()

        esocial_validados = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False,
                   status=STATUS_EVENTO_VALIDADO,
                   validacao_precedencia=0).exclude(id=0).all()

        esocial_erros_validacao = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False,
                   status=STATUS_EVENTO_VALIDADO_ERRO).exclude(id=0).all()

        esocial_assinados = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False,
                   status=STATUS_EVENTO_ASSINADO).exclude(id=0).all()

        esocial_cadastrados = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False,
                   status__in=[STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_IMPORTADO, STATUS_EVENTO_GERADO]).exclude(id=0).all()

        esocial_erros_envio = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False,
                   status=STATUS_EVENTO_ENVIADO_ERRO).exclude(id=0).all()

        esocial_processados = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False,
                   status=STATUS_EVENTO_PROCESSADO,
                   validacao_precedencia=0).exclude(id=0).all()


        #importacao_arquivos_eventos_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'mapa_processamento'

        context = {

            'tab': dict_hash['tab'],
            'esocial_enviados': esocial_enviados,
            'esocial_validados_aguardando_envio': esocial_validados_aguardando_envio,
            'esocial_validados_aguardando_precedencia': esocial_validados_aguardando_precedencia,
            'esocial_validados': esocial_validados,
            'esocial_erros_validacao': esocial_erros_validacao,
            'esocial_assinados': esocial_assinados,
            'esocial_cadastrados': esocial_cadastrados,
            'esocial_erros_envio': esocial_erros_envio,
            'esocial_processados': esocial_processados,

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
        return render(request, 'mapa_esocial.html', context)
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