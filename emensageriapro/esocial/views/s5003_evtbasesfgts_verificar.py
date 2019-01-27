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


import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
import base64
from emensageriapro.s5003.models import *
from emensageriapro.s5003.forms import *
import os


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

def txt_xml(texto):
    texto = str(texto)
    texto = texto.replace(">",'&gt;')
    texto = texto.replace("<",'&lt;')
    texto = texto.replace("&",'&amp;')
    texto = texto.replace('"','&quot;')
    texto = texto.replace("'",'&apos;')
    return texto



@login_required
def verificar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s5003_evtbasesfgts_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s5003_evtbasesfgts')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s5003_evtbasesfgts = get_object_or_404(s5003evtBasesFGTS.objects.using( db_slug ), excluido = False, id = s5003_evtbasesfgts_id)
        s5003_evtbasesfgts_lista = s5003evtBasesFGTS.objects.using( db_slug ).filter(id=s5003_evtbasesfgts_id, excluido = False).all()


        s5003_infofgts_lista = s5003infoFGTS.objects.using(db_slug).filter(s5003_evtbasesfgts_id__in = listar_ids(s5003_evtbasesfgts_lista) ).filter(excluido=False).all()
        s5003_ideestablot_lista = s5003ideEstabLot.objects.using(db_slug).filter(s5003_infofgts_id__in = listar_ids(s5003_infofgts_lista) ).filter(excluido=False).all()
        s5003_infotrabfgts_lista = s5003infoTrabFGTS.objects.using(db_slug).filter(s5003_ideestablot_id__in = listar_ids(s5003_ideestablot_lista) ).filter(excluido=False).all()
        s5003_baseperapur_lista = s5003basePerApur.objects.using(db_slug).filter(s5003_infotrabfgts_id__in = listar_ids(s5003_infotrabfgts_lista) ).filter(excluido=False).all()
        s5003_infobaseperante_lista = s5003infoBasePerAntE.objects.using(db_slug).filter(s5003_infotrabfgts_id__in = listar_ids(s5003_infotrabfgts_lista) ).filter(excluido=False).all()
        s5003_baseperante_lista = s5003basePerAntE.objects.using(db_slug).filter(s5003_infobaseperante_id__in = listar_ids(s5003_infobaseperante_lista) ).filter(excluido=False).all()
        s5003_infotrabdps_lista = s5003infoTrabDps.objects.using(db_slug).filter(s5003_infofgts_id__in = listar_ids(s5003_infofgts_lista) ).filter(excluido=False).all()
        s5003_dpsperapur_lista = s5003dpsPerApur.objects.using(db_slug).filter(s5003_infotrabdps_id__in = listar_ids(s5003_infotrabdps_lista) ).filter(excluido=False).all()
        s5003_infodpsperante_lista = s5003infoDpsPerAntE.objects.using(db_slug).filter(s5003_infotrabdps_id__in = listar_ids(s5003_infotrabdps_lista) ).filter(excluido=False).all()
        s5003_dpsperante_lista = s5003dpsPerAntE.objects.using(db_slug).filter(s5003_infodpsperante_id__in = listar_ids(s5003_infodpsperante_lista) ).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's5003_evtbasesfgts'
        context = {
            's5003_evtbasesfgts_lista': s5003_evtbasesfgts_lista,
            's5003_evtbasesfgts_id': s5003_evtbasesfgts_id,
            's5003_evtbasesfgts': s5003_evtbasesfgts,

            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,

            's5003_infofgts_lista': s5003_infofgts_lista,
            's5003_ideestablot_lista': s5003_ideestablot_lista,
            's5003_infotrabfgts_lista': s5003_infotrabfgts_lista,
            's5003_baseperapur_lista': s5003_baseperapur_lista,
            's5003_infobaseperante_lista': s5003_infobaseperante_lista,
            's5003_baseperante_lista': s5003_baseperante_lista,
            's5003_infotrabdps_lista': s5003_infotrabdps_lista,
            's5003_dpsperapur_lista': s5003_dpsperapur_lista,
            's5003_infodpsperante_lista': s5003_infodpsperante_lista,
            's5003_dpsperante_lista': s5003_dpsperante_lista,
        }
        if for_print == 2:

            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(request=request,
                                           template='s5003_evtbasesfgts_verificar.html',
                                           filename="s5003_evtbasesfgts.pdf",
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
            from django.shortcuts import render_to_response
            response =  render_to_response('s5003_evtbasesfgts_verificar.html', context)
            filename = "%s.xls" % s5003_evtbasesfgts.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response =  render_to_response('s5003_evtbasesfgts_verificar.html', context)
            filename = "%s.csv" % s5003_evtbasesfgts.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        else:
            return render(request, 's5003_evtbasesfgts_verificar.html', context)
    else:
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



def gerar_xml_s5003(s5003_evtbasesfgts_id, db_slug, versao=None):

    from django.template.loader import get_template

    if s5003_evtbasesfgts_id:

        s5003_evtbasesfgts = get_object_or_404(
            s5003evtBasesFGTS.objects.using( db_slug ),
            excluido = False,
            id = s5003_evtbasesfgts_id)

        if not versao:

            versao = s5003_evtbasesfgts.versao

        s5003_evtbasesfgts_lista = s5003evtBasesFGTS.objects.using( db_slug ).filter(id=s5003_evtbasesfgts_id, excluido = False).all()


        s5003_infofgts_lista = s5003infoFGTS.objects.using(db_slug).filter(s5003_evtbasesfgts_id__in = listar_ids(s5003_evtbasesfgts_lista) ).filter(excluido=False).all()
        s5003_ideestablot_lista = s5003ideEstabLot.objects.using(db_slug).filter(s5003_infofgts_id__in = listar_ids(s5003_infofgts_lista) ).filter(excluido=False).all()
        s5003_infotrabfgts_lista = s5003infoTrabFGTS.objects.using(db_slug).filter(s5003_ideestablot_id__in = listar_ids(s5003_ideestablot_lista) ).filter(excluido=False).all()
        s5003_baseperapur_lista = s5003basePerApur.objects.using(db_slug).filter(s5003_infotrabfgts_id__in = listar_ids(s5003_infotrabfgts_lista) ).filter(excluido=False).all()
        s5003_infobaseperante_lista = s5003infoBasePerAntE.objects.using(db_slug).filter(s5003_infotrabfgts_id__in = listar_ids(s5003_infotrabfgts_lista) ).filter(excluido=False).all()
        s5003_baseperante_lista = s5003basePerAntE.objects.using(db_slug).filter(s5003_infobaseperante_id__in = listar_ids(s5003_infobaseperante_lista) ).filter(excluido=False).all()
        s5003_infotrabdps_lista = s5003infoTrabDps.objects.using(db_slug).filter(s5003_infofgts_id__in = listar_ids(s5003_infofgts_lista) ).filter(excluido=False).all()
        s5003_dpsperapur_lista = s5003dpsPerApur.objects.using(db_slug).filter(s5003_infotrabdps_id__in = listar_ids(s5003_infotrabdps_lista) ).filter(excluido=False).all()
        s5003_infodpsperante_lista = s5003infoDpsPerAntE.objects.using(db_slug).filter(s5003_infotrabdps_id__in = listar_ids(s5003_infotrabdps_lista) ).filter(excluido=False).all()
        s5003_dpsperante_lista = s5003dpsPerAntE.objects.using(db_slug).filter(s5003_infodpsperante_id__in = listar_ids(s5003_infodpsperante_lista) ).filter(excluido=False).all()

        context = {
            'versao': versao,
            'base': s5003_evtbasesfgts,
            's5003_evtbasesfgts_lista': s5003_evtbasesfgts_lista,
            's5003_evtbasesfgts_id': int(s5003_evtbasesfgts_id),
            's5003_evtbasesfgts': s5003_evtbasesfgts,


            's5003_infofgts_lista': s5003_infofgts_lista,
            's5003_ideestablot_lista': s5003_ideestablot_lista,
            's5003_infotrabfgts_lista': s5003_infotrabfgts_lista,
            's5003_baseperapur_lista': s5003_baseperapur_lista,
            's5003_infobaseperante_lista': s5003_infobaseperante_lista,
            's5003_baseperante_lista': s5003_baseperante_lista,
            's5003_infotrabdps_lista': s5003_infotrabdps_lista,
            's5003_dpsperapur_lista': s5003_dpsperapur_lista,
            's5003_infodpsperante_lista': s5003_infodpsperante_lista,
            's5003_dpsperante_lista': s5003_dpsperante_lista,

        }

        t = get_template('s5003_evtbasesfgts.xml')
        xml = t.render(context)
        return xml



@login_required
def recibo(request, hash, tipo):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s5003_evtbasesfgts_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s5003_evtbasesfgts')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:

        s5003_evtbasesfgts = get_object_or_404(
            s5003evtBasesFGTS.objects.using( db_slug ),
            excluido = False, id = s5003_evtbasesfgts_id)

        from emensageriapro.mensageiro.models import RetornosEventos, RetornosEventosHorarios, \
            RetornosEventosIntervalos, RetornosEventosOcorrencias

        retorno = get_object_or_404( RetornosEventos.objects.using(db_slug),
            id=s5003_evtbasesfgts.retornos_eventos_id, excluido=False)

        retorno_horarios = RetornosEventosHorarios.objects.using(db_slug).\
            filter(retornos_eventos_id=retorno.id,excluido=False).all()

        retorno_intervalos = RetornosEventosIntervalos.objects.using(db_slug).\
            filter(retornos_eventos_horarios_id__in=listar_ids(retorno_horarios),excluido=False).all()

        retorno_ocorrencias = RetornosEventosOcorrencias.objects.using(db_slug).\
            filter(retornos_eventos_id=retorno.id,excluido=False).all()

        context = {
            's5003_evtbasesfgts_id': s5003_evtbasesfgts_id,
            's5003_evtbasesfgts': s5003_evtbasesfgts,

            'retorno': retorno,
            'retorno_horarios': retorno_horarios,
            'retorno_intervalos': retorno_intervalos,
            'retorno_ocorrencias': retorno_ocorrencias,


            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,
        }

        if tipo == 'XLS':
            from django.shortcuts import render_to_response
            response =  render_to_response('s5003_evtbasesfgts_recibo_pdf.html', context)
            filename = "%s.xls" % s5003_evtbasesfgts.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif tipo == 'CSV':
            from django.shortcuts import render_to_response
            response =  render_to_response('s5003_evtbasesfgts_recibo_csv.html', context)
            filename = "%s.csv" % s5003_evtbasesfgts.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        else:
            return render_to_pdf('s5003_evtbasesfgts_recibo_pdf.html', context)
    else:
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



def gerar_xml_assinado(s5003_evtbasesfgts_id, db_slug):
    import os
    from emensageriapro.mensageiro.functions.funcoes_esocial import salvar_arquivo_esocial
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes_esocial import assinar_esocial

    s5003_evtbasesfgts = get_object_or_404(
        s5003evtBasesFGTS.objects.using(db_slug),
        excluido=False,
        id=s5003_evtbasesfgts_id)

    if s5003_evtbasesfgts.arquivo_original:

        xml = ler_arquivo(s5003_evtbasesfgts.arquivo)

    else:

        xml = gerar_xml_s5003(s5003_evtbasesfgts_id, db_slug)

    if 'Signature' in xml:

        xml_assinado = xml

    else:

        xml_assinado = assinar_esocial(xml)

    if s5003_evtbasesfgts.status in (0,1,2,11):

        s5003evtBasesFGTS.objects.using(db_slug).\
            filter(id=s5003_evtbasesfgts_id,excluido=False).update(status=10)

    arquivo = 'arquivos/Eventos/s5003_evtbasesfgts/%s.xml' % (s5003_evtbasesfgts.identidade)

    os.system('mkdir -p %s/arquivos/Eventos/s5003_evtbasesfgts/' % BASE_DIR)

    if not os.path.exists(BASE_DIR+arquivo):

        salvar_arquivo_esocial(arquivo, xml_assinado, 1)

    xml_assinado = ler_arquivo(arquivo)

    return xml_assinado



@login_required
def gerar_xml(request, hash):

    from datetime import datetime
    from django.http import HttpResponse
    db_slug = 'default'
    dict_hash = get_hash_url( hash )
    s5003_evtbasesfgts_id = int(dict_hash['id'])

    if s5003_evtbasesfgts_id:

        xml_assinado = gerar_xml_assinado(s5003_evtbasesfgts_id, db_slug)
        return HttpResponse(xml_assinado, content_type='text/xml')

    context = {'data': datetime.datetime.now(),}
    return render(request, 'permissao_negada.html', context)



@login_required
def duplicar(request, hash):

    from emensageriapro.esocial.views.s5003_evtbasesfgts_importar import read_s5003_evtbasesfgts_string
    from emensageriapro.esocial.views.s5003_evtbasesfgts import identidade_evento

    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s5003_evtbasesfgts_id = int(dict_hash['id'])

    if s5003_evtbasesfgts_id:

        s5003_evtbasesfgts = get_object_or_404(
            s5003evtBasesFGTS.objects.using(db_slug),
            excluido=False,
            id=s5003_evtbasesfgts_id)

        texto = gerar_xml_s5003(s5003_evtbasesfgts_id, db_slug, versao="|")
        dados = read_s5003_evtbasesfgts_string({}, texto.encode('utf-8'), 0)
        nova_identidade = identidade_evento(dados['id'], db_slug)

        s5003evtBasesFGTS.objects.using(db_slug).filter(id=dados['id']).\
            update(status=0, arquivo_original=0, arquivo='')

        gravar_auditoria(u'{}', u'{"funcao": "Evento de identidade %s criado a partir da duplicação do evento %s"}' % (nova_identidade, s5003_evtbasesfgts.identidade),
            's5003_evtbasesfgts', dados['id'], request.user.id, 1)

        messages.success(request, 'Evento duplicado com sucesso! Foi criado uma nova identidade para este evento!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['id'] )
        return redirect('s5003_evtbasesfgts_salvar', hash=url_hash)

    messages.error(request, 'Erro ao duplicar evento!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])




@login_required
def criar_alteracao(request, hash):

    from emensageriapro.esocial.views.s5003_evtbasesfgts_importar import read_s5003_evtbasesfgts_string
    from emensageriapro.esocial.views.s5003_evtbasesfgts import identidade_evento

    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s5003_evtbasesfgts_id = int(dict_hash['id'])

    if s5003_evtbasesfgts_id:

        s5003_evtbasesfgts = get_object_or_404(
            s5003evtBasesFGTS.objects.using(db_slug),
            excluido=False,
            id=s5003_evtbasesfgts_id)

        texto = gerar_xml_s5003(s5003_evtbasesfgts_id, db_slug, versao="|")
        texto = texto.replace('<inclusao>','<alteracao>').replace('</inclusao>','</alteracao>')
        dados = read_s5003_evtbasesfgts_string({}, texto.encode('utf-8'), 0)
        nova_identidade = identidade_evento(dados['id'], db_slug)

        s5003evtBasesFGTS.objects.using(db_slug).filter(id=dados['id']).\
            update(status=0, arquivo_original=0, arquivo='')

        gravar_auditoria(u'{}',
            u'{"funcao": "Evento de de alteração de identidade %s criado a partir da duplicação do evento %s"}' % (nova_identidade, s5003_evtbasesfgts.identidade),
            's5003_evtbasesfgts', dados['id'], request.user.id, 1)

        messages.success(request, 'Evento de alteração criado com sucesso!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['id'] )
        return redirect('s5003_evtbasesfgts_salvar', hash=url_hash)

    messages.error(request, 'Erro ao criar evento de alteração!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])




@login_required
def criar_exclusao(request, hash):

    from emensageriapro.esocial.views.s5003_evtbasesfgts_importar import read_s5003_evtbasesfgts_string
    from emensageriapro.esocial.views.s5003_evtbasesfgts import identidade_evento

    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s5003_evtbasesfgts_id = int(dict_hash['id'])

    if s5003_evtbasesfgts_id:

        s5003_evtbasesfgts = get_object_or_404(
            s5003evtBasesFGTS.objects.using(db_slug),
            excluido=False,
            id=s5003_evtbasesfgts_id)

        texto = gerar_xml_s5003(s5003_evtbasesfgts_id, db_slug, versao="|")
        texto = texto.replace('<inclusao>','<exclusao>').replace('</inclusao>','</exclusao>')
        texto = texto.replace('<alteracao>','<exclusao>').replace('</alteracao>','</exclusao>')
        dados = read_s5003_evtbasesfgts_string({}, texto.encode('utf-8'), 0)
        nova_identidade = identidade_evento(dados['id'], db_slug)

        s5003evtBasesFGTS.objects.using(db_slug).filter(id=dados['id']).\
            update(status=0, arquivo_original=0, arquivo='')

        gravar_auditoria(u'{}',
            u'{"funcao": "Evento de exclusão de identidade %s criado a partir da duplicação do evento %s"}' % (nova_identidade, s5003_evtbasesfgts.identidade),
            's5003_evtbasesfgts', dados['id'], request.user.id, 1)

        messages.success(request, 'Evento de exclusão criado com sucesso!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['id'] )
        return redirect('s5003_evtbasesfgts_salvar', hash=url_hash)

    messages.error(request, 'Erro ao criar evento de exclusão!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])




@login_required
def alterar_identidade(request, hash):

    from emensageriapro.esocial.views.s5003_evtbasesfgts import identidade_evento
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s5003_evtbasesfgts_id = int(dict_hash['id'])

    if s5003_evtbasesfgts_id:

        s5003_evtbasesfgts = get_object_or_404(
            s5003evtBasesFGTS.objects.using(db_slug),
            excluido=False,
            id=s5003_evtbasesfgts_id)

        if s5003_evtbasesfgts.status == 0:

            nova_identidade = identidade_evento(s5003_evtbasesfgts_id, db_slug)
            messages.success(request, 'Identidade do evento alterada com sucesso! Nova identidade: %s' % nova_identidade)
            url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % s5003_evtbasesfgts_id )

            gravar_auditoria(u'{}',
                u'{"funcao": "Identidade do evento foi alterada"}',
                's5003_evtbasesfgts', s5003_evtbasesfgts_id, request.user.id, 1)

            return redirect('s5003_evtbasesfgts_salvar', hash=url_hash)

        else:

            messages.error(request, 'Não foi possível alterar a identidade do evento! Somente é possível alterar o status de eventos que estão abertos para edição (status: Cadastrado)!')
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])

    messages.error(request, 'Erro ao alterar identidade do evento!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])



@login_required
def abrir_evento_para_edicao(request, hash):
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes_esocial import gravar_nome_arquivo
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s5003_evtbasesfgts_id = int(dict_hash['id'])

    if s5003_evtbasesfgts_id:
        s5003_evtbasesfgts = get_object_or_404(s5003evtBasesFGTS.objects.using(db_slug), excluido=False, id=s5003_evtbasesfgts_id)

        if s5003_evtbasesfgts.status in (0, 1, 2, 3, 4, 10, 11) or s5003_evtbasesfgts.processamento_codigo_resposta in (401,402):
            s5003evtBasesFGTS.objects.using(db_slug).filter(id=s5003_evtbasesfgts_id).update(status=0, arquivo_original=0)
            arquivo = 'arquivos/Eventos/s5003_evtbasesfgts/%s.xml' % (s5003_evtbasesfgts.identidade)

            if os.path.exists(BASE_DIR + '/' + arquivo):
                from datetime import datetime
                data_hora_atual = str(datetime.now()).replace(':','_').replace(' ','_').replace('.','_')
                dad = (BASE_DIR, s5003_evtbasesfgts.identidade, BASE_DIR, s5003_evtbasesfgts.identidade, data_hora_atual)
                os.system('mv %s/arquivos/Eventos/s5003_evtbasesfgts/%s.xml %s/arquivos/Eventos/s5003_evtbasesfgts/%s_backup_%s.xml' % dad)
                gravar_nome_arquivo('/arquivos/Eventos/s5003_evtbasesfgts/%s_backup_%s.xml' % (s5003_evtbasesfgts.identidade, data_hora_atual),
                    1)
            messages.success(request, 'Evento aberto para edição!')
            usuario_id = request.user.id
            gravar_auditoria(u'{}', u'{"funcao": "Evento aberto para edição"}',
            's5003_evtbasesfgts', s5003_evtbasesfgts_id, usuario_id, 1)
            url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % s5003_evtbasesfgts_id )
            return redirect('s5003_evtbasesfgts_salvar', hash=url_hash)
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



def validar_evento_funcao(s5003_evtbasesfgts_id, db_slug):
    from emensageriapro.padrao import executar_sql
    from emensageriapro.mensageiro.functions.funcoes_importacao import get_versao_evento
    from emensageriapro.mensageiro.functions.funcoes_validacoes_precedencia import validar_precedencia
    from emensageriapro.mensageiro.functions.funcoes_validacoes import get_schema_name, validar_schema
    from emensageriapro.settings import BASE_DIR
    lista_validacoes = []
    s5003_evtbasesfgts = get_object_or_404(s5003evtBasesFGTS.objects.using(db_slug), excluido=False, id=s5003_evtbasesfgts_id)
    if s5003_evtbasesfgts.transmissor_lote_esocial:
        if s5003_evtbasesfgts.transmissor_lote_esocial.transmissor:
            if s5003_evtbasesfgts.transmissor_lote_esocial.transmissor.verificar_predecessao:
                quant = validar_precedencia('esocial', 's5003_evtbasesfgts', s5003_evtbasesfgts_id)
                if quant <= 0:
                    lista_validacoes.append(u'Precedência não foi enviada!')
                    precedencia = 0
                else:
                    precedencia = 1
            else:
                precedencia = 1
        else:
            lista_validacoes.append(u'Precedência não pode ser verificada. Vincule um transmissor para que este evento possa ser validado!')
            precedencia = 0
    else:
        lista_validacoes.append(u'Precedência não pode ser verificada. Cadastre um transmissor para este evento para que possa ser validado!')
        precedencia = 0

    s5003evtBasesFGTS.objects.using( db_slug ).\
        filter(id=s5003_evtbasesfgts_id, excluido = False).\
        update(validacao_precedencia=precedencia)

    #executar_sql("UPDATE public.s5003_evtbasesfgts SET validacao_precedencia=%s WHERE id=%s;" % (precedencia, s5003_evtbasesfgts_id), False)
    #
    # Validações internas
    #
    arquivo = 'arquivos/Eventos/s5003_evtbasesfgts/%s.xml' % (s5003_evtbasesfgts.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/s5003_evtbasesfgts/' % BASE_DIR)
    lista = []
    tipo = 'esocial'
    if not os.path.exists(BASE_DIR + '/' + arquivo):
        gerar_xml_assinado(s5003_evtbasesfgts_id, db_slug)
    if os.path.exists(BASE_DIR + '/' + arquivo):
        texto_xml = ler_arquivo(arquivo).replace("s:", "")
        versao = get_versao_evento(texto_xml)
        from emensageriapro.esocial.views.s5003_evtbasesfgts_validar import validacoes_s5003_evtbasesfgts
        lista = validacoes_s5003_evtbasesfgts(arquivo)
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

        s5003evtBasesFGTS.objects.using( db_slug ).\
            filter(id=s5003_evtbasesfgts_id, excluido = False).\
            update(validacoes=validacoes, status=3)

        #executar_sql("UPDATE public.s5003_evtbasesfgts SET validacoes='%s', status=3 WHERE id=%s;" % ('<br>'.join(lista_validacoes).replace("'","''"), s5003_evtbasesfgts_id), False)

    else:

        s5003evtBasesFGTS.objects.using( db_slug ).\
            filter(id=s5003_evtbasesfgts_id, excluido = False).\
            update(validacoes='', status=4)

        #executar_sql("UPDATE public.s5003_evtbasesfgts SET validacoes='', status=4 WHERE id=%s;" % (s5003_evtbasesfgts_id), False)

    return lista_validacoes



@login_required
def validar_evento(request, hash):

    from emensageriapro.settings import VERSOES_ESOCIAL
    from emensageriapro.mensageiro.functions.funcoes_validacoes import VERSAO_ATUAL
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s5003_evtbasesfgts_id = int(dict_hash['id'])

    if s5003_evtbasesfgts_id:

        s5003_evtbasesfgts = get_object_or_404(
            s5003evtBasesFGTS.objects.using(db_slug),
            excluido=False,
            id=s5003_evtbasesfgts_id)

        if s5003_evtbasesfgts.versao in VERSOES_ESOCIAL:

            validar_evento_funcao(s5003_evtbasesfgts_id, db_slug)
            messages.success(request, u'Validações processadas com sucesso!')

        else:

            messages.error(request, u'Não foi possível validar o evento pois a versão do evento não é compatível com a versão do sistema!')
    else:

        messages.error(request, u'Não foi possível validar o evento pois o mesmo não foi identificado!')

    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
