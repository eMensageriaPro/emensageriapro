#coding: utf-8

import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
import base64




def importar_lote(request, hash):
    import os
    from emensageriapro.settings import BASE_DIR
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #mapa_processamento_esocial_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='importacao_arquivos')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.funcoes_importacao import read_files

    arquivos = ImportacaoArquivosEventos.objects.using( db_slug ).filter(excluido = False, status=0).exclude(id=0).all()
    for arquivo in arquivos:
        filename = arquivo.arquivo

        arq_compl = filename
        from emensageriapro.funcoes_importacao import validar_arquivo
        dados_eventos = {}
        dados_evento, request, quant_erros, error_list = validar_arquivo(arquivo, request, lang='pt')
        #print arq_compl
        dados_eventos['validacoes'] = '<br>'.join(error_list)
        dados_eventos['criado_em'] = datetime.datetime.now()
        dados_eventos['criado_por_id'] = 1
        dados_eventos['excluido'] = False
        #print dados_eventos
        ImportacaoArquivosEventos.objects.using(db_slug).filter(id=arquivo.id).update(
            **dados_eventos).filter(id=arquivo.id)







    context = {
        'usuario': usuario,

        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,

        'permissao': permissao,
        'data': datetime.datetime.now(),
        'pagina': pagina,
        'dict_permissoes': dict_permissoes,
    }
    return render(request, 'permissao_negada.html', context)