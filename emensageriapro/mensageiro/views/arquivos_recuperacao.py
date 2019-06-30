#coding: utf-8

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404

from emensageriapro.padrao import *
from emensageriapro.mensageiro.models import *
from emensageriapro.mapa_processamento.views.mapa_importacoes import STATUS_IMPORT_PROCESSADO


@login_required
def arquivos_recuperacao(request, pk):

    import os
    from datetime import datetime
    from emensageriapro.mensageiro.functions.funcoes_importacao import importar_arquivo
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.settings import BASE_DIR

    arquivos = get_object_or_404(Arquivos, id=pk)

    if arquivos.permite_recuperacao:

        arquivo_importacao = ImportacaoArquivosEventos.objects.filter(arquivo=arquivos.arquivo).all()

        if not arquivo_importacao:

            a = arquivos.arquivo.split('/')
            nome_arquivo = a[len(a) - 1]
            path_arq = '/arquivos/Importacao/aguardando/' + nome_arquivo

            os.system('cp %s %s' % (BASE_DIR + arquivos.arquivo, BASE_DIR + path_arq))

            arq_import = ImportacaoArquivos.objects. \
                filter(arquivo=arquivos.arquivo).all()

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

            arquivo_importacao = ImportacaoArquivosEventos.objects.filter(arquivo=path_arq).all()

        dados_importacao = importar_arquivo(arquivo_importacao[0], request, 0)
        dados_importacao['status'] = STATUS_IMPORT_PROCESSADO

        if dados_importacao:
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

    else:
        messages.error(request, 'Este arquivo não permite ser recuperado!')

    return redirect('arquivos')




@login_required
def arquivos_reprocessar(request, pk):

    import os
    from emensageriapro.settings import BASE_DIR

    arquivos = get_object_or_404(Arquivos, id=pk)

    texto = ''

    if not os.path.isfile(BASE_DIR + '/' + arquivos.arquivo):

        # texto = ler_arquivo(arquivos.arquivo)
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

    import os
    from emensageriapro.settings import BASE_DIR

    arquivos = get_object_or_404(Arquivos,  id=pk)

    if not os.path.isfile(BASE_DIR + '/' + arquivos.arquivo):

        messages.error(request, u'Arquivo não encontrado "%s"!' % arquivos.arquivo)
        return redirect('mapa_importacoes', tab='master')

    xml = ler_arquivo(arquivos.arquivo)

    return HttpResponse(xml, content_type='text/xml')