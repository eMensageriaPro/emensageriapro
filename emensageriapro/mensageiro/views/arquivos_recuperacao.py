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


#
# def atualizar_versao():
#
#     executar_sql("""
#     UPDATE s1000_evtinfoempregador SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1005_evttabestab SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1010_evttabrubrica SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1020_evttablotacao SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1030_evttabcargo SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1035_evttabcarreira SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1040_evttabfuncao SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1050_evttabhortur SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1060_evttabambiente SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1070_evttabprocesso SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1080_evttaboperport SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1200_evtremun SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1202_evtrmnrpps SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1207_evtbenprrp SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1210_evtpgtos SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1250_evtaqprod SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1260_evtcomprod SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1270_evtcontratavnp SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1280_evtinfocomplper SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1295_evttotconting SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1298_evtreabreevper SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1299_evtfechaevper SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s1300_evtcontrsindpatr SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s2190_evtadmprelim SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s2200_evtadmissao SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s2205_evtaltcadastral SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s2206_evtaltcontratual SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s2210_evtcat SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s2220_evtmonit SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s2230_evtafasttemp SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s2240_evtexprisco SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s2241_evtinsapo SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s2250_evtavprevio SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s2260_evtconvinterm SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s2298_evtreintegr SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s2299_evtdeslig SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s2300_evttsvinicio SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s2306_evttsvaltcontr SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s2399_evttsvtermino SET versao='v02_04_02' WHERE status in (0,1,2);
#     --UPDATE s2400_evtcdbenprrp SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s3000_evtexclusao SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s5001_evtbasestrab SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s5002_evtirrfbenef SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s5011_evtcs SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE s5012_evtirrf SET versao='v02_04_02' WHERE status in (0,1,2);
#     UPDATE r1000_evtinfocontri SET versao='v1_03_02' WHERE status in (0,1,2);
#     UPDATE r1070_evttabprocesso SET versao='v1_03_02' WHERE status in (0,1,2);
#     UPDATE r2010_evtservtom SET versao='v1_03_02' WHERE status in (0,1,2);
#     UPDATE r2020_evtservprest SET versao='v1_03_02' WHERE status in (0,1,2);
#     UPDATE r2030_evtassocdesprec SET versao='v1_03_02' WHERE status in (0,1,2);
#     UPDATE r2040_evtassocdesprep SET versao='v1_03_02' WHERE status in (0,1,2);
#     UPDATE r2050_evtcomprod SET versao='v1_03_02' WHERE status in (0,1,2);
#     UPDATE r2060_evtcprb SET versao='v1_03_02' WHERE status in (0,1,2);
#     UPDATE r2070_evtpgtosdivs SET versao='v1_03_02' WHERE status in (0,1,2);
#     UPDATE r2098_evtreabreevper SET versao='v1_03_02' WHERE status in (0,1,2);
#     UPDATE r2099_evtfechaevper SET versao='v1_03_02' WHERE status in (0,1,2);
#     UPDATE r3010_evtespdesportivo SET versao='v1_03_02' WHERE status in (0,1,2);
#     UPDATE r5001_evttotal SET versao='v1_03_02' WHERE status in (0,1,2);
#     UPDATE r5011_evttotalcontrib SET versao='v1_03_02' WHERE status in (0,1,2);
#     UPDATE r9000_evtexclusao SET versao='v1_03_02' WHERE status in (0,1,2);
#     """, False)



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

    return redirect('arquivos', hash=request.session['retorno_hash'])




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
    if not os.path.isfile(BASE_DIR + arquivos.arquivo):
        messages.error(request, 'Arquivo não encontrado!')
        return redirect('mapa_importacoes', tab='master')

    xml = ler_arquivo(arquivos.arquivo)
    return HttpResponse(xml, content_type='text/xml')