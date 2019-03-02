#coding: utf-8
# © 2018 Marcelo Medeiros de Vasconcellos
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos<www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__credits__ = ["Marcelo Medeiros de Vasconcellos"]
__version__ = "1.0.0"
__maintainer__ = "Marcelo Medeiros de Vasconcellos"
__email__ = "marcelomdevasconcellos@gmail.com"


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
from emensageriapro.s1260.models import *
from emensageriapro.s1260.forms import *
from emensageriapro.functions import render_to_pdf, txt_xml
from wkhtmltopdf.views import PDFTemplateResponse
from datetime import datetime
import base64
import os


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO


@login_required
def verificar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s1260_evtcomprod_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1260_evtcomprod')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s1260_evtcomprod = get_object_or_404(s1260evtComProd.objects.using( db_slug ), excluido = False, id = s1260_evtcomprod_id)
        s1260_evtcomprod_lista = s1260evtComProd.objects.using( db_slug ).filter(id=s1260_evtcomprod_id, excluido = False).all()


        s1260_tpcomerc_lista = s1260tpComerc.objects.using(db_slug).filter(s1260_evtcomprod_id__in = listar_ids(s1260_evtcomprod_lista) ).filter(excluido=False).all()
        s1260_ideadquir_lista = s1260ideAdquir.objects.using(db_slug).filter(s1260_tpcomerc_id__in = listar_ids(s1260_tpcomerc_lista) ).filter(excluido=False).all()
        s1260_nfs_lista = s1260nfs.objects.using(db_slug).filter(s1260_ideadquir_id__in = listar_ids(s1260_ideadquir_lista) ).filter(excluido=False).all()
        s1260_infoprocjud_lista = s1260infoProcJud.objects.using(db_slug).filter(s1260_tpcomerc_id__in = listar_ids(s1260_tpcomerc_lista) ).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's1260_evtcomprod'
        context = {
            's1260_evtcomprod_lista': s1260_evtcomprod_lista,
            's1260_evtcomprod_id': s1260_evtcomprod_id,
            's1260_evtcomprod': s1260_evtcomprod,
  
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,

            's1260_tpcomerc_lista': s1260_tpcomerc_lista,
            's1260_ideadquir_lista': s1260_ideadquir_lista,
            's1260_nfs_lista': s1260_nfs_lista,
            's1260_infoprocjud_lista': s1260_infoprocjud_lista,
        }
        if for_print == 2:

            response = PDFTemplateResponse(request=request,
                                           template='s1260_evtcomprod_verificar.html',
                                           filename="s1260_evtcomprod.pdf",
                                           context=context,
                                           show_content_in_browser=True,
                                           cmd_options={'margin-top': 5,
                                                        'margin-bottom': 5,
                                                        'margin-right': 5,
                                                        'margin-left': 5,
                                                        "zoom": 3,
                                                        "viewport-size": "1366 x 513",
                                                        'javascript-delay': 1000,
                                                        'footer-center': '[page]/[topage]',
                                                        "no-stop-slow-scripts": True},
                                           )
            return response

        elif for_print == 3:

            response =  render_to_response('s1260_evtcomprod_verificar.html', context)
            filename = "%s.xls" % s1260_evtcomprod.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif for_print == 4:

            response =  render_to_response('s1260_evtcomprod_verificar.html', context)
            filename = "%s.csv" % s1260_evtcomprod.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        else:

            return render(request, 's1260_evtcomprod_verificar.html', context)

    else:

        context = {
            'usuario': usuario,
  
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }

        return render(request, 'permissao_negada.html', context)



def gerar_xml_s1260(s1260_evtcomprod_id, db_slug, versao=None):

    from django.template.loader import get_template
    from emensageriapro.functions import get_xmlns

    if s1260_evtcomprod_id:

        s1260_evtcomprod = get_object_or_404(
            s1260evtComProd.objects.using( db_slug ),
            excluido = False,
            id = s1260_evtcomprod_id)

        if not versao or versao == '|':

            versao = s1260_evtcomprod.versao

        evento = 's1260evtComProd'[5:]
        arquivo = 'xsd/esocial/%s/%s.xsd' % (versao, evento)
        xmlns = get_xmlns(arquivo)

        s1260_evtcomprod_lista = s1260evtComProd.objects.using( db_slug ).filter(id=s1260_evtcomprod_id, excluido = False).all()


        s1260_tpcomerc_lista = s1260tpComerc.objects.using(db_slug).filter(s1260_evtcomprod_id__in = listar_ids(s1260_evtcomprod_lista) ).filter(excluido=False).all()
        s1260_ideadquir_lista = s1260ideAdquir.objects.using(db_slug).filter(s1260_tpcomerc_id__in = listar_ids(s1260_tpcomerc_lista) ).filter(excluido=False).all()
        s1260_nfs_lista = s1260nfs.objects.using(db_slug).filter(s1260_ideadquir_id__in = listar_ids(s1260_ideadquir_lista) ).filter(excluido=False).all()
        s1260_infoprocjud_lista = s1260infoProcJud.objects.using(db_slug).filter(s1260_tpcomerc_id__in = listar_ids(s1260_tpcomerc_lista) ).filter(excluido=False).all()

        context = {
            'xmlns': xmlns,
            'versao': versao,
            'base': s1260_evtcomprod,
            's1260_evtcomprod_lista': s1260_evtcomprod_lista,
            's1260_evtcomprod_id': int(s1260_evtcomprod_id),
            's1260_evtcomprod': s1260_evtcomprod,

            's1260_tpcomerc_lista': s1260_tpcomerc_lista,
            's1260_ideadquir_lista': s1260_ideadquir_lista,
            's1260_nfs_lista': s1260_nfs_lista,
            's1260_infoprocjud_lista': s1260_infoprocjud_lista,
        }

        t = get_template('s1260_evtcomprod.xml')
        xml = t.render(context)
        return xml



@login_required
def recibo(request, hash, tipo):
    for_print = 0
    db_slug = 'default'

    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s1260_evtcomprod_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])

    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1260_evtcomprod')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:

        s1260_evtcomprod = get_object_or_404(
            s1260evtComProd.objects.using( db_slug ),
            excluido = False, id = s1260_evtcomprod_id)

        from emensageriapro.mensageiro.models import RetornosEventos, RetornosEventosHorarios, \
            RetornosEventosIntervalos, RetornosEventosOcorrencias

        retorno = get_object_or_404( RetornosEventos.objects.using(db_slug),
            id=s1260_evtcomprod.retornos_eventos_id, excluido=False)

        retorno_horarios = RetornosEventosHorarios.objects.using(db_slug).\
            filter(retornos_eventos_id=retorno.id,excluido=False).all()

        retorno_intervalos = RetornosEventosIntervalos.objects.using(db_slug).\
            filter(retornos_eventos_horarios_id__in=listar_ids(retorno_horarios),excluido=False).all()

        retorno_ocorrencias = RetornosEventosOcorrencias.objects.using(db_slug).\
            filter(retornos_eventos_id=retorno.id,excluido=False).all()

        context = {
            's1260_evtcomprod_id': s1260_evtcomprod_id,
            's1260_evtcomprod': s1260_evtcomprod,
            'retorno': retorno,
            'retorno_horarios': retorno_horarios,
            'retorno_intervalos': retorno_intervalos,
            'retorno_ocorrencias': retorno_ocorrencias,
  
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,
        }

        if tipo == 'XLS':
            response =  render_to_response('s1260_evtcomprod_recibo_pdf.html', context)
            filename = "%s.xls" % s1260_evtcomprod.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif tipo == 'CSV':
            response =  render_to_response('s1260_evtcomprod_recibo_csv.html', context)
            filename = "%s.csv" % s1260_evtcomprod.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        else:
            return render_to_pdf('s1260_evtcomprod_recibo_pdf.html', context)

    else:

        context = {
            'usuario': usuario,
  
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)



def gerar_xml_assinado(s1260_evtcomprod_id, db_slug):
    from emensageriapro.mensageiro.functions.funcoes_esocial import salvar_arquivo_esocial
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes_esocial import assinar_esocial

    s1260_evtcomprod = get_object_or_404(
        s1260evtComProd.objects.using(db_slug),
        excluido=False,
        id=s1260_evtcomprod_id)

    if s1260_evtcomprod.arquivo_original:

        xml = ler_arquivo(s1260_evtcomprod.arquivo)

    else:

        xml = gerar_xml_s1260(s1260_evtcomprod_id, db_slug)

    if 'Signature' in xml:

        xml_assinado = xml

    else:

        xml_assinado = assinar_esocial(xml)

    if s1260_evtcomprod.status in (STATUS_EVENTO_CADASTRADO,
                           STATUS_EVENTO_IMPORTADO,
                           STATUS_EVENTO_DUPLICADO,
                           STATUS_EVENTO_GERADO):

        s1260evtComProd.objects.using(db_slug).\
            filter(id=s1260_evtcomprod_id,excluido=False).update(status=STATUS_EVENTO_ASSINADO)

    arquivo = 'arquivos/Eventos/s1260_evtcomprod/%s.xml' % (s1260_evtcomprod.identidade)

    os.system('mkdir -p %s/arquivos/Eventos/s1260_evtcomprod/' % BASE_DIR)

    if not os.path.exists(BASE_DIR+arquivo):

        salvar_arquivo_esocial(arquivo, xml_assinado, 1)

    xml_assinado = ler_arquivo(arquivo)

    return xml_assinado



@login_required
def gerar_xml(request, hash):


    db_slug = 'default'
    dict_hash = get_hash_url( hash )
    s1260_evtcomprod_id = int(dict_hash['id'])

    if s1260_evtcomprod_id:

        xml_assinado = gerar_xml_assinado(s1260_evtcomprod_id, db_slug)
        return HttpResponse(xml_assinado, content_type='text/xml')

    context = {'data': datetime.now(),}
    return render(request, 'permissao_negada.html', context)



@login_required
def duplicar(request, hash):

    from emensageriapro.esocial.views.s1260_evtcomprod_importar import read_s1260_evtcomprod_string
    from emensageriapro.functions import identidade_evento

    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s1260_evtcomprod_id = int(dict_hash['id'])

    if s1260_evtcomprod_id:

        s1260_evtcomprod = get_object_or_404(
            s1260evtComProd.objects.using(db_slug),
            excluido=False,
            id=s1260_evtcomprod_id)

        texto = gerar_xml_s1260(s1260_evtcomprod_id, db_slug, versao="|")
        dados = read_s1260_evtcomprod_string({}, texto.encode('utf-8'), 0)
        nova_identidade = identidade_evento(s1260_evtcomprod)

        s1260evtComProd.objects.using(db_slug).filter(id=dados['id']).\
            update(status=STATUS_EVENTO_CADASTRADO,
                   arquivo_original=0,
                   arquivo='')

        gravar_auditoria(u'{}', u'{"funcao": "Evento de identidade %s criado a partir da duplicação do evento %s"}' % (nova_identidade, s1260_evtcomprod.identidade),
            's1260_evtcomprod', dados['id'], request.user.id, 1)

        messages.success(request, u'Evento duplicado com sucesso! Foi criado uma nova identidade para este evento!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['id'] )
        return redirect('s1260_evtcomprod_salvar', hash=url_hash)

    messages.error(request, 'Erro ao duplicar evento!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])




@login_required
def criar_alteracao(request, hash):

    from emensageriapro.esocial.views.s1260_evtcomprod_importar import read_s1260_evtcomprod_string
    from emensageriapro.functions import identidade_evento

    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s1260_evtcomprod_id = int(dict_hash['id'])

    if s1260_evtcomprod_id:

        s1260_evtcomprod = get_object_or_404(
            s1260evtComProd.objects.using(db_slug),
            excluido=False,
            id=s1260_evtcomprod_id)

        texto = gerar_xml_s1260(s1260_evtcomprod_id, db_slug, versao="|")
        texto = texto.replace('<inclusao>','<alteracao>').replace('</inclusao>','</alteracao>')
        dados = read_s1260_evtcomprod_string({}, texto.encode('utf-8'), 0)
        nova_identidade = identidade_evento(s1260_evtcomprod)

        s1260evtComProd.objects.using(db_slug).filter(id=dados['id']).\
            update(status=STATUS_EVENTO_CADASTRADO,
                   arquivo_original=0,
                   arquivo='')

        gravar_auditoria(u'{}',
            u'{"funcao": "Evento de de alteração de identidade %s criado a partir da duplicação do evento %s"}' % (nova_identidade, s1260_evtcomprod.identidade),
            's1260_evtcomprod', dados['id'], request.user.id, 1)

        messages.success(request, u'Evento de alteração criado com sucesso!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['id'] )
        return redirect('s1260_evtcomprod_salvar', hash=url_hash)

    messages.error(request, 'Erro ao criar evento de alteração!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])




@login_required
def criar_exclusao(request, hash):

    from emensageriapro.esocial.views.s1260_evtcomprod_importar import read_s1260_evtcomprod_string
    from emensageriapro.functions import identidade_evento

    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s1260_evtcomprod_id = int(dict_hash['id'])

    if s1260_evtcomprod_id:

        s1260_evtcomprod = get_object_or_404(
            s1260evtComProd.objects.using(db_slug),
            excluido=False,
            id=s1260_evtcomprod_id)

        texto = gerar_xml_s1260(s1260_evtcomprod_id, db_slug, versao="|")
        texto = texto.replace('<inclusao>','<exclusao>').replace('</inclusao>','</exclusao>')
        texto = texto.replace('<alteracao>','<exclusao>').replace('</alteracao>','</exclusao>')
        dados = read_s1260_evtcomprod_string({}, texto.encode('utf-8'), 0)
        nova_identidade = identidade_evento(s1260_evtcomprod)

        s1260evtComProd.objects.using(db_slug).filter(id=dados['id']).\
            update(status=STATUS_EVENTO_CADASTRADO,
                   arquivo_original=0,
                   arquivo='')

        gravar_auditoria(u'{}',
            u'{"funcao": "Evento de exclusão de identidade %s criado a partir da duplicação do evento %s"}' % (nova_identidade, s1260_evtcomprod.identidade),
            's1260_evtcomprod', dados['id'], request.user.id, 1)

        messages.success(request, u'Evento de exclusão criado com sucesso!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['id'] )
        return redirect('s1260_evtcomprod_salvar', hash=url_hash)

    messages.error(request, 'Erro ao criar evento de exclusão!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])




@login_required
def alterar_identidade(request, hash):

    from emensageriapro.functions import identidade_evento
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s1260_evtcomprod_id = int(dict_hash['id'])

    if s1260_evtcomprod_id:

        s1260_evtcomprod = get_object_or_404(
            s1260evtComProd.objects.using(db_slug),
            excluido=False,
            id=s1260_evtcomprod_id)

        if s1260_evtcomprod.status == STATUS_EVENTO_CADASTRADO:

            nova_identidade = identidade_evento(s1260_evtcomprod)
            messages.success(request, u'Identidade do evento alterada com sucesso! Nova identidade: %s' % nova_identidade)
            url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % s1260_evtcomprod_id )

            gravar_auditoria(u'{}',
                u'{"funcao": "Identidade do evento foi alterada"}',
                's1260_evtcomprod', s1260_evtcomprod_id, request.user.id, 1)

            return redirect('s1260_evtcomprod_salvar', hash=url_hash)

        else:

            messages.error(request, u'Não foi possível alterar a identidade do evento! Somente é possível alterar o status de eventos que estão abertos para edição (status: Cadastrado)!')
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])

    messages.error(request, u'Erro ao alterar identidade do evento!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])



@login_required
def abrir_evento_para_edicao(request, hash):
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes_esocial import gravar_nome_arquivo
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s1260_evtcomprod_id = int(dict_hash['id'])

    if s1260_evtcomprod_id:
        s1260_evtcomprod = get_object_or_404(s1260evtComProd.objects.using(db_slug), excluido=False, id=s1260_evtcomprod_id)

        status_list = [
            STATUS_EVENTO_CADASTRADO,
            STATUS_EVENTO_IMPORTADO,
            STATUS_EVENTO_DUPLICADO,
            STATUS_EVENTO_GERADO,
            STATUS_EVENTO_GERADO_ERRO,
            STATUS_EVENTO_ASSINADO,
            STATUS_EVENTO_ASSINADO_ERRO,
            STATUS_EVENTO_VALIDADO,
            STATUS_EVENTO_VALIDADO_ERRO,
            STATUS_EVENTO_AGUARD_PRECEDENCIA,
            STATUS_EVENTO_AGUARD_ENVIO,
            STATUS_EVENTO_ENVIADO_ERRO
        ]

        if s1260_evtcomprod.status in status_list:
            s1260evtComProd.objects.using(db_slug).filter(id=s1260_evtcomprod_id).update(status=STATUS_EVENTO_CADASTRADO,
                                                                          arquivo_original=0)
            arquivo = 'arquivos/Eventos/s1260_evtcomprod/%s.xml' % (s1260_evtcomprod.identidade)

            if os.path.exists(BASE_DIR + '/' + arquivo):

                data_hora_atual = str(datetime.now()).replace(':','_').replace(' ','_').replace('.','_')
                dad = (BASE_DIR, s1260_evtcomprod.identidade, BASE_DIR, s1260_evtcomprod.identidade, data_hora_atual)
                os.system('mv %s/arquivos/Eventos/s1260_evtcomprod/%s.xml %s/arquivos/Eventos/s1260_evtcomprod/%s_backup_%s.xml' % dad)
                gravar_nome_arquivo('/arquivos/Eventos/s1260_evtcomprod/%s_backup_%s.xml' % (s1260_evtcomprod.identidade, data_hora_atual),
                    1)
            messages.success(request, 'Evento aberto para edição!')
            usuario_id = request.user.id
            gravar_auditoria(u'{}', u'{"funcao": "Evento aberto para edição"}',
                's1260_evtcomprod', s1260_evtcomprod_id, usuario_id, 1)
            url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % s1260_evtcomprod_id )
            return redirect('s1260_evtcomprod_salvar', hash=url_hash)
        else:
            messages.error(request, u'''
            Não foi possível abrir o evento para edição! Somente é possível
            abrir eventos com os seguintes status: "Cadastrado", "Importado", "Validado",
            "Duplicado", "Erro na validação", "XML Assinado" ou "XML Gerado"
             ou com o status "Enviado com sucesso" e os seguintes códigos de resposta do servidor:
             "401 - Lote Incorreto - Erro preenchimento" ou "402 - Lote Incorreto - schema Inválido"!''')
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])

    messages.error(request, 'Erro ao abrir evento para edição!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])



def validar_evento_funcao(s1260_evtcomprod_id, db_slug):
    from emensageriapro.padrao import executar_sql
    from emensageriapro.mensageiro.functions.funcoes_importacao import get_versao_evento
    from emensageriapro.mensageiro.functions.funcoes_validacoes_precedencia import validar_precedencia
    from emensageriapro.mensageiro.functions.funcoes_validacoes import get_schema_name, validar_schema
    from emensageriapro.settings import BASE_DIR, VERIFICAR_PREDECESSAO_ANTES_ENVIO
    lista_validacoes = []
    s1260_evtcomprod = get_object_or_404(s1260evtComProd.objects.using(db_slug), excluido=False, id=s1260_evtcomprod_id)

    #
    # Validações internas
    #

    arquivo = 'arquivos/Eventos/s1260_evtcomprod/%s.xml' % (s1260_evtcomprod.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/s1260_evtcomprod/' % BASE_DIR)
    lista = []
    tipo = 'esocial'
    if not os.path.exists(BASE_DIR + '/' + arquivo):
        gerar_xml_assinado(s1260_evtcomprod_id, db_slug)
    if os.path.exists(BASE_DIR + '/' + arquivo):
        texto_xml = ler_arquivo(arquivo).replace("s:", "")
        versao = get_versao_evento(texto_xml)
        from emensageriapro.esocial.views.s1260_evtcomprod_validar import validacoes_s1260_evtcomprod
        lista = validacoes_s1260_evtcomprod(arquivo)
    for a in lista:
        if a:
            lista_validacoes.append(a)
    #
    # validando schema
    #
    schema_filename = get_schema_name(arquivo)
    quant_erros, error_list = validar_schema(schema_filename, arquivo, lang='pt')
    for a in error_list:
        if a:
            lista_validacoes.append(a)
    #
    #
    #
    if lista_validacoes:

        validacoes = '<br>'.join(lista_validacoes).replace("'","''")

        s1260evtComProd.objects.using( db_slug ).\
            filter(id=s1260_evtcomprod_id, excluido = False).\
            update(validacoes=validacoes,
                   status=STATUS_EVENTO_VALIDADO_ERRO)

    else:

        if VERIFICAR_PREDECESSAO_ANTES_ENVIO:

            quant = validar_precedencia('esocial', 's1260_evtcomprod', s1260_evtcomprod_id)

            if quant <= 0:

                s1260evtComProd.objects.using( db_slug ).\
                    filter(id=s1260_evtcomprod_id, excluido = False).\
                    update(validacoes=None,
                           status=STATUS_EVENTO_AGUARD_PRECEDENCIA)

            else:

                s1260evtComProd.objects.using( db_slug ).\
                    filter(id=s1260_evtcomprod_id, excluido = False).\
                    update(validacoes=None,
                           status=STATUS_EVENTO_AGUARD_ENVIO)

        else:

            s1260evtComProd.objects.using(db_slug). \
                filter(id=s1260_evtcomprod_id, excluido=False).\
                update(validacoes=None,
                       status=STATUS_EVENTO_AGUARD_ENVIO)

    return lista_validacoes



@login_required
def validar_evento(request, hash):

    from emensageriapro.settings import VERSOES_ESOCIAL, VERIFICAR_PREDECESSAO_ANTES_ENVIO
    # from emensageriapro.mensageiro.functions.funcoes_validacoes import VERSAO_ATUAL

    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s1260_evtcomprod_id = int(dict_hash['id'])

    if s1260_evtcomprod_id:

        s1260_evtcomprod = get_object_or_404(
            s1260evtComProd.objects.using(db_slug),
            excluido=False,
            id=s1260_evtcomprod_id)

        if s1260_evtcomprod.versao in VERSOES_ESOCIAL:

            validar_evento_funcao(s1260_evtcomprod_id, db_slug)

            if s1260_evtcomprod.transmissor_lote_esocial and not VERIFICAR_PREDECESSAO_ANTES_ENVIO:
                s1260evtComProd.objects.using(db_slug).\
                    filter(excluido=False, id=s1260_evtcomprod_id).update(status=STATUS_EVENTO_AGUARD_ENVIO)

            elif s1260_evtcomprod.transmissor_lote_esocial and VERIFICAR_PREDECESSAO_ANTES_ENVIO:
                s1260evtComProd.objects.using(db_slug).\
                    filter(excluido=False, id=s1260_evtcomprod_id).update(status=STATUS_EVENTO_AGUARD_PRECEDENCIA)

            messages.success(request, u'Validações processadas com sucesso!')

        else:

            messages.error(request, u'Não foi possível validar o evento pois a versão do evento não é compatível com a versão do sistema!')
    else:

        messages.error(request, u'Não foi possível validar o evento pois o mesmo não foi identificado!')

    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
