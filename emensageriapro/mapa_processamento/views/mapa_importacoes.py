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


IMPORTACAO_STATUS = [

    (0, u'Aguardando'),
    (1, u'Processando'),
    (2, u'Processado com sucesso'),
    (3, u'Erro - Processamento'),
    (4, u'Erro - Outros'),
    (5, u'Erro - Arquivo Inválido'),
    (6, u'Erro - Identidade já existente'),
    (7, u'Erro - Versão de leiaute incompatível'),
    (8, u'Erro - Validação de Leiaute'),

]

STATUS_IMPORT_AGUARDANDO = 0
STATUS_IMPORT_PROCESSANDO = 1
STATUS_IMPORT_PROCESSADO = 2
STATUS_IMPORT_ERRO_PROCESSAMENTO = 3
STATUS_IMPORT_ERRO_OUTROS = 4
STATUS_IMPORT_ERRO_ARQUIVO_INVALIDO = 5
STATUS_IMPORT_ERRO_IDENTIDADE_EXISTENTE = 6
STATUS_IMPORT_ERRO_VERSAO_LEIAUTE = 7
STATUS_IMPORT_ERRO_VALIDACAO_LEIAUTE = 8



@login_required
def listar(request, tab='master'):

    status_erros = [
        STATUS_IMPORT_ERRO_PROCESSAMENTO,
        STATUS_IMPORT_ERRO_OUTROS,
        STATUS_IMPORT_ERRO_ARQUIVO_INVALIDO,
        STATUS_IMPORT_ERRO_IDENTIDADE_EXISTENTE,
        STATUS_IMPORT_ERRO_VERSAO_LEIAUTE,
        STATUS_IMPORT_ERRO_VALIDACAO_LEIAUTE,
    ]

    if True:


        lista_aguardando = ImportacaoArquivosEventos.objects.filter(status=STATUS_IMPORT_AGUARDANDO).exclude(id=0).all()
        lista_erros = ImportacaoArquivosEventos.objects.filter(status__in=status_erros).exclude(id=0).all()
        lista_processando = ImportacaoArquivosEventos.objects.filter(status=STATUS_IMPORT_PROCESSANDO).all()
        lista_processados = ImportacaoArquivosEventos.objects.filter(status=STATUS_IMPORT_PROCESSADO).all()

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'tab': tab,
            'lista_aguardando': lista_aguardando,
            'lista_erros': lista_erros,
            'lista_processando': lista_processando,
            'lista_processados': lista_processados,
            'quant_aguardando': len(lista_aguardando),
            'quant_erros': len(lista_erros),
            'quant_processando': len(lista_processando),
            'quant_processados': len(lista_processados),
            'data': datetime.datetime.now(),
        }

        return render(request, 'mapa_importacoes.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'data': datetime.datetime.now(),
            'dict_permissoes': dict_permissoes,
        }

        return render(request, 'permissao_negada.html', context)