#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"


from datetime import datetime
from constance import config
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from emensageriapro.controle_de_acesso.models import Usuarios
from emensageriapro.mapa_processamento.views.mapa_importacoes import STATUS_IMPORT_AGUARDANDO, \
    STATUS_IMPORT_PROCESSADO, \
    STATUS_IMPORT_ERRO_PROCESSAMENTO, STATUS_IMPORT_ERRO_ARQUIVO_INVALIDO, \
    STATUS_IMPORT_ERRO_IDENTIDADE_EXISTENTE, STATUS_IMPORT_ERRO_VERSAO_LEIAUTE
from emensageriapro.mensageiro.functions.funcoes import gravar_nome_arquivo
from emensageriapro.mensageiro.models import *
from emensageriapro.padrao import *


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



def get_ident(arquivo):
    ident = str(arquivo.id)
    while len(ident) < 10:
        ident = '0' + ident
    return ident




def move_event(arquivo, path_destino):

    import os
    from emensageriapro.settings import BASE_DIR

    ident = get_ident(arquivo)
    path_destino = '/%s/' % path_destino
    origem = BASE_DIR + arquivo.arquivo
    novo_arquivo = arquivo.arquivo.replace('/aguardando/', path_destino + ident + '__')
    destino = BASE_DIR + novo_arquivo

    os.system('mv %s %s' % (origem, destino))
    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(arquivo=novo_arquivo)
    gravar_nome_arquivo(novo_arquivo, 1)
    return novo_arquivo



def import_files_in_folder(request):

    import os
    from datetime import datetime
    from emensageriapro.settings import BASE_DIR

    create_import_dirs()

    lista = os.listdir(BASE_DIR + '/arquivos/Importacao/aguardando/')

    for arq in lista:

        path_arq = '/arquivos/Importacao/aguardando/' + arq

        arquivo = ImportacaoArquivosEventos.objects.\
            filter(arquivo=path_arq).all()

        if not arquivo:

            arq_import = ImportacaoArquivos.objects.\
                filter(arquivo=path_arq.replace('aguardando', 'enviado')).all()

            if arq_import:
                obj = arq_import[0]
            else:
                dados_importacao = {}
                dados_importacao['arquivo'] = path_arq
                dados_importacao['status'] = 0
                dados_importacao['data_hora'] = datetime.now()
                dados_importacao['quant_processado'] = 0
                dados_importacao['quant_erros'] = 0
                dados_importacao['quant_aguardando'] = 0
                dados_importacao['importado_por_id'] = request.user.id

                obj = ImportacaoArquivos(**dados_importacao)
                obj.save()

            dados_eventos = {}
            dados_eventos['importacao_arquivos_id'] = obj.id
            dados_eventos['evento'] = '-'
            dados_eventos['versao'] = '-'
            dados_eventos['identidade_evento'] = '-'
            dados_eventos['identidade'] = 0
            dados_eventos['arquivo'] = path_arq
            dados_eventos['status'] = 0
            dados_eventos['data_hora'] = datetime.now()
            dados_eventos['validacoes'] = ''

            obj_ev = ImportacaoArquivosEventos(**dados_eventos)
            obj_ev.save()


def scripts_processar_arquivos(request, tab):

    create_import_dirs()

    import os.path
    from emensageriapro.settings import BASE_DIR, VERSOES_EFDREINF, VERSOES_ESOCIAL
    from emensageriapro.functions import get_identidade_evento, get_versao_evento
    from emensageriapro.mensageiro.functions.funcoes_importacao import importar_arquivo

    arquivos_lista = ImportacaoArquivos.objects.all()
    ImportacaoArquivosEventos.objects.\
        exclude(importacao_arquivos__in=arquivos_lista).delete()

    arquivos = ImportacaoArquivosEventos.objects.\
        filter(status=STATUS_IMPORT_AGUARDANDO).exclude(id=0).all()

    for arquivo in arquivos:

        filename = arquivo.arquivo
        dados_eventos = {}

        if os.path.isfile(BASE_DIR + filename) and '.xml' in filename.lower():

            dados_eventos['identidade_evento'] = get_identidade_evento(ler_arquivo(filename))
            dados_eventos['versao'] = get_versao_evento(ler_arquivo(filename))

            existe_identidade_esocial = TransmissorEventosEsocial.objects.\
                filter(identidade=dados_eventos['identidade_evento']).all()

            existe_identidade_efdreinf = TransmissorEventosEfdreinf.objects.\
                filter(identidade=dados_eventos['identidade_evento']).all()

            if existe_identidade_esocial or existe_identidade_efdreinf:

                dados_eventos['status'] = STATUS_IMPORT_ERRO_IDENTIDADE_EXISTENTE
                error_list = ['Não é possível importar o evento pois o ID já existe em nossa base!']
                move_event(arquivo, 'erros')

            elif dados_eventos['versao'] in VERSOES_ESOCIAL or dados_eventos['versao'] in VERSOES_EFDREINF:

                quant_erros, error_list = validar_arquivo(request, filename, lang='pt')

                if not quant_erros or (quant_erros == 1 and 'Signature' in str(error_list)):

                    dados_importacao = importar_arquivo(arquivo, request, 1)

                    dados_eventos['evento'] = dados_importacao['evento']
                    dados_eventos['status'] = STATUS_IMPORT_PROCESSADO
                    # xml_ger, xml_imp = verificacao_importacao_funcao(arquivo)
                    # if xml_ger in xml_imp:
                    #     print 'OK'
                    # else:
                    #     print 'ERROR'

                else:

                    dados_eventos['status'] = STATUS_IMPORT_ERRO_PROCESSAMENTO
                    move_event(arquivo, 'erros')

            else:

                dados_eventos['status'] = STATUS_IMPORT_ERRO_VERSAO_LEIAUTE
                error_list = ['Versão do evento incompatível!']
                move_event(arquivo, 'erros')

        else:

            dados_eventos['status'] = STATUS_IMPORT_ERRO_ARQUIVO_INVALIDO
            error_list = ['Arquivo não encontrado!']

        dados_eventos['validacoes'] = '<br>'.join(error_list)

        ImportacaoArquivosEventos.objects.\
            filter(id=arquivo.id).update(**dados_eventos)

    if tab == 'mapa':

        messages.success(request, 'Processamento realizado com sucesso...')
        return redirect('mapa_importacoes', tab='master')

    return HttpResponse('')



@login_required
def importacao_visualizacao(request, pk):

    import os
    from emensageriapro.settings import BASE_DIR

    arquivos = get_object_or_404(ImportacaoArquivosEventos,  id=pk)

    if not os.path.isfile(BASE_DIR + '/' + arquivos.arquivo):

        messages.error(request, u'Arquivo não encontrado "%s"!' % arquivos.arquivo)
        return redirect('mapa_importacoes', tab='master')

    xml = ler_arquivo(arquivos.arquivo)

    return HttpResponse(xml, content_type='text/xml')




@login_required
def importacao_reprocessar(request, pk):

    import os
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes_importacao import importar_arquivo

    arquivos = get_object_or_404(ImportacaoArquivosEventos, id=pk)

    dados_importacao = importar_arquivo(arquivos, request, 0)

    if dados_importacao:

        ImportacaoArquivosEventos.objects.filter(id=arquivos.id).\
            update(status=STATUS_IMPORT_PROCESSADO)

        messages.warning(request, '''
                    Arquivo recuperado com sucesso! 
                    Por gentileza confira todo o conteúdo 
                    do mesmo, pois este processo não 
                    passou por validação''')

    else:

        messages.error(request, '''
                    Arquivo não pode ser recuperado 
                    pois já existe um arquivo com a 
                    mesma identidade cadastrado!''')

    return redirect('mapa_importacoes', tab='master')




@login_required
def scripts_salvar_arquivos(request, tab='master'):

    create_import_dirs()

    import os
    from datetime import datetime
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
        dados_importacao['data_hora'] = datetime.now()
        dados_importacao['quant_processado'] = 0
        dados_importacao['quant_erros'] = 0
        dados_importacao['quant_aguardando'] = 0
        dados_importacao['importado_por_id'] = request.user.id

        obj = ImportacaoArquivos(**dados_importacao)
        obj.save()

        arquivos = ImportacaoArquivos.objects.\
            filter(status=0).all()

        for arquivo in arquivos:

            filename = BASE_DIR + arquivo.arquivo

            if '.xml' in filename.lower():

                destino = filename.replace('/enviado/', '/aguardando/')

                dados_eventos = {}
                dados_eventos['importacao_arquivos_id'] = arquivo.id
                dados_eventos['evento'] = '-'
                dados_eventos['versao'] = '-'
                dados_eventos['identidade_evento'] = '-'
                dados_eventos['identidade'] = 0
                dados_eventos['arquivo'] = arquivo.arquivo.replace('/enviado/', '/aguardando/')
                dados_eventos['status'] = 0
                dados_eventos['data_hora'] = datetime.now()
                dados_eventos['validacoes'] = ''

                obj = ImportacaoArquivosEventos(**dados_eventos)
                obj.save()

                comando = 'cp %s %s' % (filename, destino)
                os.system(comando)

            elif '.zip' in filename:

                import zipfile

                zip_ref = zipfile.ZipFile(filename, 'r')
                # os.system('unzip -o -a %s -d %s' % (filename, BASE_DIR + '/arquivos/Importacao/aguardando/'))
                # zip_ref = zipfile.ZipFile(filename)
                lista = zip_ref.namelist()

                n = 0

                for arquivo_evento in lista:

                    if '.xml' in arquivo_evento.lower():

                        path_arq = '/arquivos/Importacao/aguardando/' + arquivo_evento

                        arquivo_existe = ImportacaoArquivosEventos.objects. \
                            filter(arquivo=path_arq).all()

                        if not arquivo_existe and '.xml' in arquivo_evento.lower():

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
                                dados_eventos['data_hora'] = datetime.now()
                                dados_eventos['validacoes'] = ''

                                obj = ImportacaoArquivosEventos(**dados_eventos)
                                obj.save()

                zip_ref.extractall(BASE_DIR + '/arquivos/Importacao/aguardando/')
                zip_ref.close()

            ImportacaoArquivos.objects.filter(id=arquivo.id).update(status=2)

        if config.IMPORT_AUTOMATIC_FUNCTIONS_ENABLED:

            messages.success(request,
                u'''Arquivo %s extraido com sucesso! 
                    Aguarde um momento que o arquivo 
                    será processado em breve ou 
                    clique em "Processar Arquivos" 
                    para processar os arquivos''' % arquivo)
            return redirect('mapa_importacoes', tab='master')

        else:

            messages.success(request,
                u'''Arquivo %s extraido com sucesso!
                    Habilite a função de processamento automático 
                    ou clique em "Processar Arquivos" 
                    para processar os arquivos''' % arquivo)
            return redirect('mapa_importacoes', tab='master')

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
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


@login_required
def imprimir(request, pk):

    from datetime import datetime

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
            'data': datetime.now(),
            'show_fields': show_fields,
            'hash': hash,
            'filtrar': filtrar,
            'importado_por_lista': importado_por_lista,
        }

        return render_to_pdf('importacoes_imprimir.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'data': datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)