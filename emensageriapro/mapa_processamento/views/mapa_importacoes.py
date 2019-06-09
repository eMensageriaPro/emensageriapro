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
def listar(request, tab='master'):

    if True:

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

        lista_aguardando = ImportacaoArquivosEventos.objects.filter(**dict_qs).filter(status=0).exclude(id=0).all()
        lista_erros = ImportacaoArquivosEventos.objects.filter(**dict_qs).filter(status=2).exclude(id=0).all()
        lista_processados = ImportacaoArquivos.objects.filter(status=0).all()

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'tab': tab,
            'lista_aguardando': lista_aguardando,
            'lista_erros': lista_erros,
            'lista_processados': lista_processados,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'show_fields': show_fields,
            'filtrar': filtrar,
        }

        return render(request, 'mapa_importacoes.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'data': datetime.datetime.now(),
            'dict_permissoes': dict_permissoes,
        }

        return render(request, 'permissao_negada.html', context)