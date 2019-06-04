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
def listar(request, output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
        STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
        STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
        STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
        STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
        STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
        STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO

    for_print = 0

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
                'importacao_arquivos': 'importacao_arquivos', }

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
                'importacao_arquivos': 'importacao_arquivos', }
                
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
                    
        dict_qs = clear_dict_fields(dict_fields)

        importacao_arquivos_eventos_lista = ImportacaoArquivosEventos.objects.\
            filter(**dict_qs).filter(status=0).exclude(id=0).all()

        importacao_arquivos_eventos_erros_lista = ImportacaoArquivosEventos.objects.\
            filter(**dict_qs).filter(status=2).exclude(id=0).all()

        esocial_enviados = TransmissorEventosEsocial.objects.\
            filter(status=STATUS_EVENTO_ENVIADO).exclude(id=0).all()

        esocial_validados_aguardando_envio = TransmissorEventosEsocial.objects.\
            filter(status=STATUS_EVENTO_AGUARD_ENVIO,
                   validacao_precedencia=1).exclude(id=0).all()

        esocial_validados_aguardando_precedencia = TransmissorEventosEsocial.objects.\
            filter(status=STATUS_EVENTO_AGUARD_PRECEDENCIA,
                   validacao_precedencia=0).exclude(id=0).all()

        esocial_erros_validacao = TransmissorEventosEsocial.objects.\
            filter(status=STATUS_EVENTO_VALIDADO_ERRO).exclude(id=0).all()

        esocial_assinados = TransmissorEventosEsocial.objects.\
            filter(status=STATUS_EVENTO_ASSINADO).exclude(id=0).all()

        esocial_cadastrados = TransmissorEventosEsocial.objects.\
            filter(status__in=[STATUS_EVENTO_CADASTRADO,
                               STATUS_EVENTO_DUPLICADO,
                               STATUS_EVENTO_IMPORTADO,
                               STATUS_EVENTO_GERADO]).exclude(id=0).all()

        esocial_erros_envio = TransmissorEventosEsocial.objects.\
            filter(status=STATUS_EVENTO_ENVIADO_ERRO).exclude(id=0).all()

        efdreinf_enviados = TransmissorEventosEfdreinf.objects.\
            filter(status=STATUS_EVENTO_ENVIADO).exclude(id=0).all()

        efdreinf_validados_aguardando_envio = TransmissorEventosEfdreinf.objects.\
            filter(status=STATUS_EVENTO_AGUARD_ENVIO,
                   validacao_precedencia=1).exclude(id=0).all()

        efdreinf_validados_aguardando_precedencia = TransmissorEventosEfdreinf.objects.\
            filter(status=STATUS_EVENTO_AGUARD_PRECEDENCIA,
                   validacao_precedencia=0).exclude(id=0).all()

        efdreinf_erros_validacao = TransmissorEventosEfdreinf.objects.\
            filter(status=STATUS_EVENTO_VALIDADO_ERRO).exclude(id=0).all()

        efdreinf_assinados = TransmissorEventosEfdreinf.objects.\
            filter(status=STATUS_EVENTO_ASSINADO).exclude(id=0).all()

        efdreinf_cadastrados = TransmissorEventosEfdreinf.objects.\
            filter(status__in=[STATUS_EVENTO_CADASTRADO,
                               STATUS_EVENTO_DUPLICADO,
                               STATUS_EVENTO_IMPORTADO,
                               STATUS_EVENTO_GERADO]).exclude(id=0).all()

        efdreinf_erros_envio = TransmissorEventosEfdreinf.objects.\
            filter(status=STATUS_EVENTO_ENVIADO_ERRO).exclude(id=0).all()


        importacao_arquivos_lista = ImportacaoArquivos.objects.filter(status=0).all()

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'importacao_arquivos_eventos_lista': importacao_arquivos_eventos_lista,
            'importacao_arquivos_eventos_erros_lista': importacao_arquivos_eventos_erros_lista,

            'esocial_enviados': esocial_enviados,
            'esocial_validados_aguardando_envio': esocial_validados_aguardando_envio,
            'esocial_validados_aguardando_precedencia': esocial_validados_aguardando_precedencia,
            'esocial_erros_validacao': esocial_erros_validacao,
            'esocial_assinados': esocial_assinados,
            'esocial_cadastrados': esocial_cadastrados,
            'esocial_erros_envio': esocial_erros_envio,

            'efdreinf_enviados': efdreinf_enviados,
            'efdreinf_validados_aguardando_envio': efdreinf_validados_aguardando_envio,
            'efdreinf_validados_aguardando_precedencia': efdreinf_validados_aguardando_precedencia,
            'efdreinf_erros_validacao': efdreinf_erros_validacao,
            'efdreinf_assinados': efdreinf_assinados,
            'efdreinf_cadastrados': efdreinf_cadastrados,
            'efdreinf_erros_envio': efdreinf_erros_envio,

            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'show_fields': show_fields,
            'for_print': for_print,
            'filtrar': filtrar,
            'importacao_arquivos_lista': importacao_arquivos_lista,
        }

        return render(request, 'mapa_processamento.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'data': datetime.datetime.now(),
            'pagina': pagina,
        }

        return render(request, 'permissao_negada.html', context)