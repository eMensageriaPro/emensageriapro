#coding: utf-8

import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import Usuarios
import base64
from emensageriapro.padrao import executar_sql



@login_required
def arquivos_recuperacao(request, pk):
    
    arquivos = get_object_or_404(Arquivos, id=pk)

    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes_importacao import importar_arquivo

    if arquivos.permite_recuperacao:

        dados = importar_arquivo(arquivos.arquivo, request, 0)

        if dados:

            messages.warning(request, 'Arquivo recuperado com sucesso! Por gentileza confira todo o conteúdo do mesmo, pois este processo não passou por validação')

        else:

            messages.error(request, 'Arquivo não pode ser recuperado pois já existe um arquivo com a mesma identidade cadastrado!')

    else:

        messages.error(request,
                       'Este arquivo não permite ser recuperado!')

    # atualizar_versao()

    return redirect('arquivos')




@login_required
def arquivos_reprocessar(request, pk):

    import os
    from emensageriapro.settings import BASE_DIR

    arquivos = get_object_or_404(Arquivos, id=pk)

    texto = ''

    if not os.path.isfile(BASE_DIR + '/' + arquivos.arquivo):

        texto = ler_arquivo(arquivos.arquivo)
        return redirect('mapa_importacoes', tab='master')

    a = arquivos.arquivo.split('/')
    b = a[len(a)-1].split('.')
    transmissor_id = int(b[0])

    if 'eSocial' in texto:

        if 'WsEnviarLoteEventos' in arquivos.arquivo:

            from emensageriapro.mensageiro.functions.funcoes_esocial_comunicacao import read_envioLoteEventos
            read_envioLoteEventos(arquivos.arquivo, transmissor_id)

        elif 'WsConsultarLoteEventos' in arquivos.arquivo:

            from emensageriapro.mensageiro.functions.funcoes_esocial_comunicacao import read_consultaLoteEventos
            read_consultaLoteEventos(arquivos.arquivo, transmissor_id)

        messages.success(request, 'Arquivo processado com sucesso!')

    elif 'Reinf' in texto:

        if 'RecepcaoLoteReinf' in arquivos.arquivo:
            from emensageriapro.mensageiro.functions.funcoes_efdreinf_comunicacao import read_envioLoteEventos
            read_envioLoteEventos(arquivos.arquivo, transmissor_id)

        elif 'ConsultasReinf' in arquivos.arquivo:
            from emensageriapro.mensageiro.functions.funcoes_efdreinf_comunicacao import read_consultaLoteEventos
            read_consultaLoteEventos(arquivos.arquivo, transmissor_id)

        messages.success(request, 'Arquivo processado com sucesso!')

    else:

        messages.error(request,
                       'Não foi possível reprocessar o arquivo!')

    return redirect('mapa_importacoes', tab='master')



@login_required
def arquivos_visualizacao(request, pk):

    from emensageriapro.settings import BASE_DIR
    import os

    arquivos = get_object_or_404(Arquivos,  id=pk)

    if not os.path.isfile(BASE_DIR + '/' + arquivos.arquivo):
        messages.error(request, 'Arquivo não encontrado!')
        return redirect('mapa_importacoes', tab='master')

    xml = ler_arquivo(arquivos.arquivo)
    return HttpResponse(xml, content_type='text/xml')