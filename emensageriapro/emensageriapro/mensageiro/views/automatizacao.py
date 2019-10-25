# #coding: utf-8
#
# __author__ = "Marcelo Medeiros de Vasconcellos"
# __copyright__ = "Copyright 2018"
# __email__ = "marcelomdevasconcellos@gmail.com"
#
#
#
# import datetime
# from django.contrib import messages
# from django.http import HttpResponseRedirect, Http404, HttpResponse
# from django.shortcuts import render, redirect, get_object_or_404
# from django.db.models import Count
# from emensageriapro.padrao import *
# from emensageriapro.mensageiro.forms import *
# from emensageriapro.mensageiro.models import *
# from emensageriapro.controle_de_acesso.models import Usuarios
# import base64
#
#
# def render_to_pdf(template_src, context_dict={}):
#
#     from io import BytesIO
#     from django.http import HttpResponse
#     from django.template.loader import get_template
#     from xhtml2pdf import pisa
#     template = get_template(template_src)
#     html  = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
#
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#
#     return None
#
#
# def scripts_validacao_automatica(request):
#
#     import os
#     from emensageriapro.settings import BASE_DIR
#     from emensageriapro.padrao import executar_sql
#     from emensageriapro.mensageiro.functions.funcoes_importacao import importar_arquivo
#     from emensageriapro.mensageiro.views.processar_arquivos import validar_arquivo
#
#     for_print = 0
#
#     executar_sql("""
#     UPDATE public.importacao_arquivos_eventos
#        SET ativo=Null
#      WHERE importacao_arquivos_id IN (SELECT id FROM importacao_arquivos WHERE ativo=Null) ;
#
#     """, False)
#
#     arquivos = ImportacaoArquivosEventos.objects.filter(status=0).exclude(id=0).all()
#
#     for arquivo in arquivos:
#
#         filename = arquivo.arquivo
#
#         arq_compl = filename
#         dados_eventos = {}
#         quant_erros, error_list = validar_arquivo(filename, request, lang='pt')
#
#         if not error_list:
#             dados_eventos = importar_arquivo(filename, request, 1)
#
#         if not dados_eventos:
#             dados_eventos = {}
#             dados_eventos['status'] = 5
#             dados_eventos['validacoes'] = 'Evento já existe em nossa base!'
#             dados_eventos['criado_em'] = datetime.datetime.now()
#             dados_eventos['criado_por_id'] = 1
#             dados_eventos['ativo'] = True
#
#             ImportacaoArquivosEventos.objects.\
#                 filter(id=arquivo.id).update(**dados_eventos)
#
#             ia_id = arquivo.importacao_arquivos_id
#
#             executar_sql("""
#                 UPDATE public.importacao_arquivos SET
#                 quant_aquardando = (
#                 SELECT count(*) FROM public.importacao_arquivos_eventos e
#                 WHERE e.importacao_arquivos_id=%s AND e.status=0),
#                 quant_error = (
#                 SELECT count(*) FROM public.importacao_arquivos_eventos e
#                 WHERE e.importacao_arquivos_id=%s AND e.status in (2,5)),
#                 quant_processado = (
#                 SELECT count(*) FROM public.importacao_arquivos_eventos e
#                 WHERE e.importacao_arquivos_id=%s AND e.status=1)
#                 WHERE id=%s
#             """ % (ia_id, ia_id, ia_id, ia_id), False)
#
#         else:
#
#             if error_list:
#
#                 dados_eventos['status'] = 2
#
#             else:
#
#                 dados_eventos['status'] = 4
#
#             dados_eventos['validacoes'] = '<br>'.join(error_list)
#             dados_eventos['criado_em'] = datetime.datetime.now()
#             dados_eventos['criado_por_id'] = 1
#             dados_eventos['ativo'] = True
#
#             ImportacaoArquivosEventos.objects.\
#                 filter(id=arquivo.id).update(**dados_eventos)
#
#             ia_id = arquivo.importacao_arquivos_id
#
#             executar_sql("""
#                 UPDATE public.importacao_arquivos SET
#                 quant_aquardando = (
#                 SELECT count(*) FROM public.importacao_arquivos_eventos e
#                 WHERE e.importacao_arquivos_id=%s AND e.status=0),
#                 quant_error = (
#                 SELECT count(*) FROM public.importacao_arquivos_eventos e
#                 WHERE e.importacao_arquivos_id=%s AND e.status in (2,5) ),
#                 quant_processado = (
#                 SELECT count(*) FROM public.importacao_arquivos_eventos e
#                 WHERE e.importacao_arquivos_id=%s AND e.status=1)
#                 WHERE id=%s
#             """ % (ia_id, ia_id, ia_id, ia_id), False)
#
#     arquivos = ImportacaoArquivosEventos.objects.exclude(id=0).all()
#
#     for arquivo in arquivos:
#
#         if arquivo.status in [2,5]:
#
#             for arquivo in arquivos:
#
#                 origem = BASE_DIR + '/' + arquivo.arquivo
#                 destino = BASE_DIR + '/' + arquivo.arquivo.replace('/aguardando/', '/erro/')
#                 os.system('mv %s %s' % (origem, destino))
#                 dados = {}
#                 dados['arquivo'] = arquivo.arquivo.replace('/aguardando/', '/erro/')
#                 ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(**dados)
#
#         elif arquivo.status == 1:
#
#             for arquivo in arquivos:
#
#                 origem = BASE_DIR + '/' + arquivo.arquivo
#                 destino = BASE_DIR + '/' + arquivo.arquivo.replace('/aguardando/', '/processado/')
#                 os.system('mv %s %s' % (origem, destino))
#                 dados = {}
#                 dados['arquivo'] = arquivo.arquivo.replace('/aguardando/', '/processado/')
#                 ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(**dados)
#
#     return HttpResponse('')
#
#
#
#
# def scripts_transmissao_automatica(request):
#
#     import os
#     from emensageriapro.settings import BASE_DIR
#     from emensageriapro.padrao import executar_sql
#     from emensageriapro.mensageiro.functions.funcoes_importacao import importar_arquivo
#     from emensageriapro.mensageiro.views.processar_arquivos import validar_arquivo
#     for_print = 0
#
#     executar_sql("""
#     UPDATE public.importacao_arquivos_eventos
#        SET ativo=Null
#      WHERE importacao_arquivos_id IN (SELECT id FROM importacao_arquivos WHERE ativo=Null) ;
#
#     """, False)
#
#     arquivos = ImportacaoArquivosEventos.objects.filter(status=0).exclude(id=0).all()
#
#     for arquivo in arquivos:
#
#         filename = arquivo.arquivo
#         arq_compl = filename
#         dados_eventos = {}
#         quant_erros, error_list = validar_arquivo(filename, request, lang='pt')
#
#         if not error_list:
#             dados_eventos = importar_arquivo(filename, request, 1)
#
#         if not dados_eventos:
#             dados_eventos = {}
#             dados_eventos['status'] = 5
#             dados_eventos['validacoes'] = 'Evento já existe em nossa base!'
#             dados_eventos['criado_em'] = datetime.datetime.now()
#             dados_eventos['criado_por_id'] = 1
#             dados_eventos['ativo'] = True
#             ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(**dados_eventos)
#             ia_id = arquivo.importacao_arquivos_id
#
#             executar_sql("""
#                 UPDATE public.importacao_arquivos SET
#                 quant_aquardando = (
#                 SELECT count(*) FROM public.importacao_arquivos_eventos e
#                 WHERE e.importacao_arquivos_id=%s AND e.status=0),
#                 quant_error = (
#                 SELECT count(*) FROM public.importacao_arquivos_eventos e
#                 WHERE e.importacao_arquivos_id=%s AND e.status in (2,5)),
#                 quant_processado = (
#                 SELECT count(*) FROM public.importacao_arquivos_eventos e
#                 WHERE e.importacao_arquivos_id=%s AND e.status=1)
#                 WHERE id=%s
#             """ % (ia_id, ia_id, ia_id, ia_id), False)
#
#         else:
#
#             if error_list:
#                 dados_eventos['status'] = 2
#
#             else:
#                 dados_eventos['status'] = 4
#
#             dados_eventos['validacoes'] = '<br>'.join(error_list)
#             dados_eventos['criado_em'] = datetime.datetime.now()
#             dados_eventos['criado_por_id'] = 1
#             dados_eventos['ativo'] = True
#
#             ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(**dados_eventos)
#
#             ia_id = arquivo.importacao_arquivos_id
#
#             executar_sql("""
#                 UPDATE public.importacao_arquivos SET
#                 quant_aquardando = (
#                 SELECT count(*) FROM public.importacao_arquivos_eventos e
#                 WHERE e.importacao_arquivos_id=%s AND e.status=0),
#                 quant_error = (
#                 SELECT count(*) FROM public.importacao_arquivos_eventos e
#                 WHERE e.importacao_arquivos_id=%s AND e.status in (2,5) ),
#                 quant_processado = (
#                 SELECT count(*) FROM public.importacao_arquivos_eventos e
#                 WHERE e.importacao_arquivos_id=%s AND e.status=1)
#                 WHERE id=%s
#             """ % (ia_id, ia_id, ia_id, ia_id), False)
#
#     arquivos = ImportacaoArquivosEventos.objects.exclude(id=0).all()
#
#     for arquivo in arquivos:
#
#         if arquivo.status in [2,5]:
#
#             for arquivo in arquivos:
#
#                 origem = BASE_DIR + '/' + arquivo.arquivo
#                 destino = BASE_DIR + '/' + arquivo.arquivo.replace('/aguardando/', '/erro/')
#                 os.system('mv %s %s' % (origem, destino))
#                 dados = {}
#                 dados['arquivo'] = arquivo.arquivo.replace('/aguardando/', '/erro/')
#                 ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(**dados)
#
#         elif arquivo.status == 1:
#
#             for arquivo in arquivos:
#
#                 origem = BASE_DIR + '/' + arquivo.arquivo
#                 destino = BASE_DIR + '/' + arquivo.arquivo.replace('/aguardando/', '/processado/')
#                 print 'mv %s %s' % (origem, destino)
#                 os.system('mv %s %s' % (origem, destino))
#                 dados = {}
#                 dados['arquivo'] = arquivo.arquivo.replace('/aguardando/', '/processado/')
#                 ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(**dados)
#
#     return HttpResponse('')