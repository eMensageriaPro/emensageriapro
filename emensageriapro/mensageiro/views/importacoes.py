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

    for_print = 0

    try:

        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #importacao_arquivos_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])

    except:

        usuario_id = False
        return redirect('login')

    processar_arquivo = False
    usuario = get_object_or_404(Usuarios,id=usuario_id)

    if True:

        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_excluido': 0,
            'show_modificado_por': 0,
            'show_modificado_em': 0,
            'show_criado_por': 0,
            'show_criado_em': 0,
            'show_quant_erros': 0,
            'show_quant_processado': 0,
            'show_quant_aguardando': 0,
            'show_quant_total': 0,
            'show_importado_por': 1,
            'show_data_hora': 1,
            'show_status': 1,
            'show_arquivo': 1, }
        post = False

        if request.method == 'POST':

            post = True
            dict_fields = {
                'quant_erros': 'quant_erros',
                'quant_processado': 'quant_processado',
                'quant_aguardando': 'quant_aguardando',
                'quant_total': 'quant_total',
                'importado_por': 'importado_por',
                'data_hora__range': 'data_hora__range',
                'status': 'status',
                'arquivo__icontains': 'arquivo__icontains',}

            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)

            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)

            if request.method == 'POST':
                dict_fields = {
                    'quant_erros': 'quant_erros',
                    'quant_processado': 'quant_processado',
                    'quant_aguardando': 'quant_aguardando',
                    'quant_total': 'quant_total',
                    'importado_por': 'importado_por',
                    'data_hora__range': 'data_hora__range',
                    'status': 'status',
                    'arquivo__icontains': 'arquivo__icontains',}

                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)

        dict_qs = clear_dict_fields(dict_fields)
        importacao_arquivos_lista = ImportacaoArquivos.objects.filter(**dict_qs).exclude(id=0).all()

        if not post and len(importacao_arquivos_lista) > 100:
            filtrar = True
            importacao_arquivos_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        importado_por_lista = Usuarios.objects.all()

        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'importacao_arquivos'

        context = {
            'processar_arquivo': processar_arquivo,
            'importacao_arquivos_lista': importacao_arquivos_lista,
            'usuario': usuario,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,
            'importado_por_lista': importado_por_lista,
        }

        return render(request, 'importacoes_listar.html', context)

    else:

        context = {
            'usuario': usuario,
            'data': datetime.datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)