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
from emensageriapro.controle_de_acesso.models import Usuarios
import base64
from emensageriapro.padrao import executar_sql
from emensageriapro.mensageiro.functions.funcoes_esocial import gravar_nome_arquivo

from emensageriapro.mapa_processamento.views.mapa_importacoes import STATUS_IMPORT_AGUARDANDO, \
    STATUS_IMPORT_PROCESSANDO, STATUS_IMPORT_PROCESSADO, \
    STATUS_IMPORT_ERRO_PROCESSAMENTO,STATUS_IMPORT_ERRO_OUTROS, STATUS_IMPORT_ERRO_ARQUIVO_INVALIDO, \
    STATUS_IMPORT_ERRO_IDENTIDADE_EXISTENTE, STATUS_IMPORT_ERRO_VERSAO_LEIAUTE, STATUS_IMPORT_ERRO_VALIDACAO_LEIAUTE



def create_import_dirs():

    import os
    from emensageriapro.settings import BASE_DIR

    dir_list = [
        'erros',
        'processado',
        'aguardando',
        'enviado'
    ]

    for d in dir_list:
        diretory_name = BASE_DIR + '/arquivos/Importacao/%s/' % d
        if not os.path.isdir(diretory_name):
            os.system('mkdir -p %s' % diretory_name)



def validar_arquivo(request, arquivo, lang=None):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_schema
    from django.contrib import messages
    import untangle

    quant_erros = 0
    error_list = 0
    xml = ler_arquivo(arquivo).replace("s:", "")
    dados = {}

    try:

        doc = untangle.parse(xml)
        dados['status'] = 1

    except:

        messages.error(request, 'Erro na importação. Arquivo XML inválido!')
        dados['status'] = 3
        return 1, ['Erro na importação. Arquivo XML inválido!']

    if dados['status'] == 1:

        from emensageriapro.mensageiro.functions.funcoes_validacoes import get_schema_name
        schema_filename = get_schema_name(arquivo)
        quant_erros, error_list = validar_schema(request, schema_filename, arquivo, lang=lang)

    return quant_erros, error_list




def scripts_processar_arquivos(request, tab):

    create_import_dirs()

    import os.path
    from emensageriapro.settings import BASE_DIR, VERSOES_EFDREINF, VERSOES_ESOCIAL
    from emensageriapro.mensageiro.functions.funcoes_importacao import importar_arquivo, \
        get_identidade_evento, get_versao_evento

    arquivos_lista = ImportacaoArquivos.objects.all()
    ImportacaoArquivosEventos.objects.exclude(importacao_arquivos__in=arquivos_lista).delete()

    arquivos = ImportacaoArquivosEventos.objects.filter(status=STATUS_IMPORT_AGUARDANDO).exclude(id=0).all()

    for arquivo in arquivos:

        error_list = []

        ident = str(arquivo.id)

        while len(ident) < 10:
            ident = '0' + ident

        filename = arquivo.arquivo
        dados_eventos = {}

        if os.path.isfile(BASE_DIR+filename):

            dados_eventos['identidade_evento'] = get_identidade_evento(ler_arquivo(filename))
            dados_eventos['versao'] = get_versao_evento(ler_arquivo(filename))

            existe_identidade_esocial = TransmissorEventosEsocial.objects.filter(identidade=dados_eventos['identidade_evento']).all()
            existe_identidade_efdreinf = TransmissorEventosEfdreinf.objects.filter(identidade=dados_eventos['identidade_evento']).all()

            if existe_identidade_esocial or existe_identidade_efdreinf:

                dados_eventos['status'] = STATUS_IMPORT_ERRO_IDENTIDADE_EXISTENTE
                error_list = ['Não é possível importar o evento pois o ID já existe em nossa base!']
                origem = BASE_DIR + arquivo.arquivo
                destino = BASE_DIR + arquivo.arquivo.replace('/aguardando/', '/erro/' + ident + '__')
                os.system('mv %s %s' % (origem, destino))
                dados_eventos['arquivo'] = arquivo.arquivo.replace('/aguardando/', '/erro/'+ ident + '__')
                gravar_nome_arquivo(dados_eventos['arquivo'], 1)

            elif dados_eventos['versao'] in VERSOES_ESOCIAL or dados_eventos['versao'] in VERSOES_EFDREINF:

                quant_erros, error_list = validar_arquivo(request, filename, lang='pt')

                if not quant_erros or (quant_erros == 1 and 'Signature' in str(error_list)):

                    dados_importacao = importar_arquivo(filename, request, 1)
                    dados_eventos['evento'] = dados_importacao['tabela']
                    dados_eventos['status'] = STATUS_IMPORT_PROCESSADO
                    origem = BASE_DIR + arquivo.arquivo
                    destino = BASE_DIR + arquivo.arquivo.replace('/aguardando/', '/processado/' + ident + '__')
                    os.system('mv %s %s' % (origem, destino))
                    dados_eventos['arquivo'] = arquivo.arquivo.replace('/aguardando/', '/processado/' + ident + '__')

                    gravar_nome_arquivo(dados_eventos['arquivo'], 1)

                else:

                    dados_eventos['status'] = STATUS_IMPORT_ERRO_PROCESSAMENTO
                    origem = BASE_DIR + arquivo.arquivo
                    destino = BASE_DIR + arquivo.arquivo.replace('/aguardando/', '/erro/' + ident + '__')
                    os.system('mv %s %s' % (origem, destino))
                    dados_eventos['arquivo'] = arquivo.arquivo.replace('/aguardando/', '/erro/' + ident + '__')
                    gravar_nome_arquivo(dados_eventos['arquivo'], 1)

            else:

                dados_eventos['status'] = STATUS_IMPORT_ERRO_VERSAO_LEIAUTE
                error_list = ['Versão do evento incompatível!']
                origem = BASE_DIR + arquivo.arquivo
                destino = BASE_DIR + arquivo.arquivo.replace('/aguardando/', '/erro/' + ident + '__')
                os.system('mv %s %s' % (origem, destino))
                dados_eventos['arquivo'] = arquivo.arquivo.replace('/aguardando/', '/erro/'+ ident + '__')
                ia_id = arquivo.importacao_arquivos_id
                gravar_nome_arquivo(dados_eventos['arquivo'], 1)

        else:

            dados_eventos['status'] = STATUS_IMPORT_ERRO_ARQUIVO_INVALIDO
            error_list = ['Arquivo não encontrado!']

        dados_eventos['validacoes'] = '<br>'.join(error_list)
        dados_eventos['criado_em'] = datetime.datetime.now()
        dados_eventos['criado_por_id'] = request.user.id
        dados_eventos['ativo'] = True
        ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(**dados_eventos)

    if tab == 'mapa':
        messages.success(request, 'Processamento realizado com sucesso...')
        return redirect('mapa_importacoes', tab='master')

    return HttpResponse('')




@login_required
def scripts_salvar_arquivos(request, tab='master'):

    import os
    from emensageriapro.settings import BASE_DIR
    from django.core.files.storage import FileSystemStorage

    # tipos: 1-pdf; 2-xls, 3-csv

    if request.method == 'POST' and request.FILES['arquivo']:

        myfile = request.FILES['arquivo']
        fs = FileSystemStorage(location=BASE_DIR + '/arquivos/Importacao/enviado/')
        nome_arquivo = myfile.name.replace(' ', '-')
        filename = fs.save(nome_arquivo, myfile)

        dados_importacao = {}
        dados_importacao['arquivo'] = '/arquivos/Importacao/enviado/' + filename
        dados_importacao['status'] = 0
        dados_importacao['data_hora'] = datetime.datetime.now()
        dados_importacao['quant_processado'] = 0
        dados_importacao['quant_erros'] = 0
        dados_importacao['quant_aguardando'] = 0
        dados_importacao['importado_por_id'] = request.user.id
        dados_importacao['criado_em'] = datetime.datetime.now()
        dados_importacao['criado_por_id'] = request.user.id
        dados_importacao['ativo'] = True

        obj = ImportacaoArquivos(**dados_importacao)
        obj.save()

        arquivos = ImportacaoArquivos.objects.filter(status=0).exclude(id=0).all()

        for arquivo in arquivos:

            filename = BASE_DIR + '/' + arquivo.arquivo

            if '.xml' in filename.lower():

                destino = filename.replace('/enviado/', '/aguardando/')
                os.system('mv %s %s' % (filename, destino))

            elif '.zip' in filename:

                os.system('unzip -o -a %s -d %s' % (filename, BASE_DIR + '/arquivos/Importacao/aguardando'))

            lista = os.listdir(BASE_DIR + '/arquivos/Importacao/aguardando')

            n = 0

            for arquivo_evento in lista:

                if '.xml' in arquivo_evento.lower():

                    n += 1
                    arq_compl = '/arquivos/Importacao/aguardando/' + arquivo_evento

                    dados_eventos = {}
                    dados_eventos['importacao_arquivos_id'] = arquivo.id
                    dados_eventos['evento'] = '-'
                    dados_eventos['versao'] = '-'
                    dados_eventos['identidade_evento'] = '-'
                    dados_eventos['identidade'] = 0
                    dados_eventos['arquivo'] = arq_compl
                    dados_eventos['status'] = 0
                    dados_eventos['data_hora'] = datetime.datetime.now()
                    dados_eventos['validacoes'] = ''
                    dados_eventos['criado_em'] = datetime.datetime.now()
                    dados_eventos['criado_por_id'] = request.user.id
                    dados_eventos['ativo'] = True

                    obj = ImportacaoArquivosEventos(**dados_eventos)
                    obj.save()

            messages.success(request, 'Arquivo %s extraido com sucesso! Processando arquivos...' % arquivo)

    else:

        messages.error(request, 'Não foram encontrados arquivos para processamento!')

    if tab == 'mapa':

        return redirect('mapa_importacoes', tab='master')

    else:

        return redirect('importacao_arquivos')




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
def imprimir(request, pk):

    # tipos: 1-pdf; 2-xls, 3-csv

    if True:

        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_ativo': 0,
            'show_modificado_por': 0,
            'show_modificado_em': 0,
            'show_criado_por': 0,
            'show_criado_em': 0,
            'show_quant_erros': 0,
            'show_quant_processado': 0,
            'show_quant_aguardando': 0,
            'show_importado_por': 1,
            'show_data_hora': 1,
            'show_status': 1,
            'show_arquivo': 1, }

        dict_qs = clear_dict_fields(dict_fields)

        importacao_arquivos_lista = ImportacaoArquivos.objects.filter(**dict_qs).\
            filter(id=pk).exclude(id=0).all()

        ia_lista = []

        for a in importacao_arquivos_lista:

            ia_lista.append(a.id)

        importacao_arquivos_eventos_lista = ImportacaoArquivosEventos.objects.\
            filter(**dict_qs).filter(importacao_arquivos_id__in=ia_lista).exclude(id=0).all()

        importado_por_lista = Usuarios.objects.all()

        context = {
            'importacao_arquivos_lista': importacao_arquivos_lista,
            'importacao_arquivos_eventos_lista': importacao_arquivos_eventos_lista,
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'user': request.user,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'show_fields': show_fields,
            'hash': hash,
            'filtrar': filtrar,
            'importado_por_lista': importado_por_lista,
        }

        return render_to_pdf('importacoes_imprimir.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'data': datetime.datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)