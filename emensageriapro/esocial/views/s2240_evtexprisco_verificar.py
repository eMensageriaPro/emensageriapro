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
from emensageriapro.s2240.models import *
from emensageriapro.s2240.forms import *
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
        s2240_evtexprisco_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2240_evtexprisco')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s2240_evtexprisco = get_object_or_404(s2240evtExpRisco.objects.using( db_slug ), excluido = False, id = s2240_evtexprisco_id)
        s2240_evtexprisco_lista = s2240evtExpRisco.objects.using( db_slug ).filter(id=s2240_evtexprisco_id, excluido = False).all()


        s2240_iniexprisco_infoamb_lista = s2240iniExpRiscoinfoAmb.objects.using(db_slug).filter(s2240_evtexprisco_id__in = listar_ids(s2240_evtexprisco_lista) ).filter(excluido=False).all()
        s2240_iniexprisco_ativpericinsal_lista = s2240iniExpRiscoativPericInsal.objects.using(db_slug).filter(s2240_evtexprisco_id__in = listar_ids(s2240_evtexprisco_lista) ).filter(excluido=False).all()
        s2240_iniexprisco_fatrisco_lista = s2240iniExpRiscofatRisco.objects.using(db_slug).filter(s2240_evtexprisco_id__in = listar_ids(s2240_evtexprisco_lista) ).filter(excluido=False).all()
        s2240_iniexprisco_epc_lista = s2240iniExpRiscoepc.objects.using(db_slug).filter(s2240_iniexprisco_fatrisco_id__in = listar_ids(s2240_iniexprisco_fatrisco_lista) ).filter(excluido=False).all()
        s2240_iniexprisco_epi_lista = s2240iniExpRiscoepi.objects.using(db_slug).filter(s2240_iniexprisco_fatrisco_id__in = listar_ids(s2240_iniexprisco_fatrisco_lista) ).filter(excluido=False).all()
        s2240_iniexprisco_respreg_lista = s2240iniExpRiscorespReg.objects.using(db_slug).filter(s2240_evtexprisco_id__in = listar_ids(s2240_evtexprisco_lista) ).filter(excluido=False).all()
        s2240_iniexprisco_obs_lista = s2240iniExpRiscoobs.objects.using(db_slug).filter(s2240_evtexprisco_id__in = listar_ids(s2240_evtexprisco_lista) ).filter(excluido=False).all()
        s2240_altexprisco_lista = s2240altExpRisco.objects.using(db_slug).filter(s2240_evtexprisco_id__in = listar_ids(s2240_evtexprisco_lista) ).filter(excluido=False).all()
        s2240_altexprisco_infoamb_lista = s2240altExpRiscoinfoAmb.objects.using(db_slug).filter(s2240_altexprisco_id__in = listar_ids(s2240_altexprisco_lista) ).filter(excluido=False).all()
        s2240_altexprisco_fatrisco_lista = s2240altExpRiscofatRisco.objects.using(db_slug).filter(s2240_altexprisco_infoamb_id__in = listar_ids(s2240_altexprisco_infoamb_lista) ).filter(excluido=False).all()
        s2240_altexprisco_epc_lista = s2240altExpRiscoepc.objects.using(db_slug).filter(s2240_altexprisco_fatrisco_id__in = listar_ids(s2240_altexprisco_fatrisco_lista) ).filter(excluido=False).all()
        s2240_altexprisco_epi_lista = s2240altExpRiscoepi.objects.using(db_slug).filter(s2240_altexprisco_fatrisco_id__in = listar_ids(s2240_altexprisco_fatrisco_lista) ).filter(excluido=False).all()
        s2240_fimexprisco_lista = s2240fimExpRisco.objects.using(db_slug).filter(s2240_evtexprisco_id__in = listar_ids(s2240_evtexprisco_lista) ).filter(excluido=False).all()
        s2240_fimexprisco_infoamb_lista = s2240fimExpRiscoinfoAmb.objects.using(db_slug).filter(s2240_fimexprisco_id__in = listar_ids(s2240_fimexprisco_lista) ).filter(excluido=False).all()
        s2240_fimexprisco_respreg_lista = s2240fimExpRiscorespReg.objects.using(db_slug).filter(s2240_evtexprisco_id__in = listar_ids(s2240_evtexprisco_lista) ).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2240_evtexprisco'
        context = {
            's2240_evtexprisco_lista': s2240_evtexprisco_lista,
            's2240_evtexprisco_id': s2240_evtexprisco_id,
            's2240_evtexprisco': s2240_evtexprisco,
  
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,

            's2240_iniexprisco_infoamb_lista': s2240_iniexprisco_infoamb_lista,
            's2240_iniexprisco_ativpericinsal_lista': s2240_iniexprisco_ativpericinsal_lista,
            's2240_iniexprisco_fatrisco_lista': s2240_iniexprisco_fatrisco_lista,
            's2240_iniexprisco_epc_lista': s2240_iniexprisco_epc_lista,
            's2240_iniexprisco_epi_lista': s2240_iniexprisco_epi_lista,
            's2240_iniexprisco_respreg_lista': s2240_iniexprisco_respreg_lista,
            's2240_iniexprisco_obs_lista': s2240_iniexprisco_obs_lista,
            's2240_altexprisco_lista': s2240_altexprisco_lista,
            's2240_altexprisco_infoamb_lista': s2240_altexprisco_infoamb_lista,
            's2240_altexprisco_fatrisco_lista': s2240_altexprisco_fatrisco_lista,
            's2240_altexprisco_epc_lista': s2240_altexprisco_epc_lista,
            's2240_altexprisco_epi_lista': s2240_altexprisco_epi_lista,
            's2240_fimexprisco_lista': s2240_fimexprisco_lista,
            's2240_fimexprisco_infoamb_lista': s2240_fimexprisco_infoamb_lista,
            's2240_fimexprisco_respreg_lista': s2240_fimexprisco_respreg_lista,
        }
        if for_print == 2:

            response = PDFTemplateResponse(request=request,
                                           template='s2240_evtexprisco_verificar.html',
                                           filename="s2240_evtexprisco.pdf",
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

            response =  render_to_response('s2240_evtexprisco_verificar.html', context)
            filename = "%s.xls" % s2240_evtexprisco.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif for_print == 4:

            response =  render_to_response('s2240_evtexprisco_verificar.html', context)
            filename = "%s.csv" % s2240_evtexprisco.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        else:

            return render(request, 's2240_evtexprisco_verificar.html', context)

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



def gerar_xml_s2240(s2240_evtexprisco_id, db_slug, versao=None):

    from django.template.loader import get_template
    from emensageriapro.functions import get_xmlns

    if s2240_evtexprisco_id:

        s2240_evtexprisco = get_object_or_404(
            s2240evtExpRisco.objects.using( db_slug ),
            excluido = False,
            id = s2240_evtexprisco_id)

        if not versao or versao == '|':

            versao = s2240_evtexprisco.versao

        evento = 's2240evtExpRisco'[5:]
        arquivo = 'xsd/esocial/%s/%s.xsd' % (versao, evento)
        xmlns = get_xmlns(arquivo)

        s2240_evtexprisco_lista = s2240evtExpRisco.objects.using( db_slug ).filter(id=s2240_evtexprisco_id, excluido = False).all()


        s2240_iniexprisco_infoamb_lista = s2240iniExpRiscoinfoAmb.objects.using(db_slug).filter(s2240_evtexprisco_id__in = listar_ids(s2240_evtexprisco_lista) ).filter(excluido=False).all()
        s2240_iniexprisco_ativpericinsal_lista = s2240iniExpRiscoativPericInsal.objects.using(db_slug).filter(s2240_evtexprisco_id__in = listar_ids(s2240_evtexprisco_lista) ).filter(excluido=False).all()
        s2240_iniexprisco_fatrisco_lista = s2240iniExpRiscofatRisco.objects.using(db_slug).filter(s2240_evtexprisco_id__in = listar_ids(s2240_evtexprisco_lista) ).filter(excluido=False).all()
        s2240_iniexprisco_epc_lista = s2240iniExpRiscoepc.objects.using(db_slug).filter(s2240_iniexprisco_fatrisco_id__in = listar_ids(s2240_iniexprisco_fatrisco_lista) ).filter(excluido=False).all()
        s2240_iniexprisco_epi_lista = s2240iniExpRiscoepi.objects.using(db_slug).filter(s2240_iniexprisco_fatrisco_id__in = listar_ids(s2240_iniexprisco_fatrisco_lista) ).filter(excluido=False).all()
        s2240_iniexprisco_respreg_lista = s2240iniExpRiscorespReg.objects.using(db_slug).filter(s2240_evtexprisco_id__in = listar_ids(s2240_evtexprisco_lista) ).filter(excluido=False).all()
        s2240_iniexprisco_obs_lista = s2240iniExpRiscoobs.objects.using(db_slug).filter(s2240_evtexprisco_id__in = listar_ids(s2240_evtexprisco_lista) ).filter(excluido=False).all()
        s2240_altexprisco_lista = s2240altExpRisco.objects.using(db_slug).filter(s2240_evtexprisco_id__in = listar_ids(s2240_evtexprisco_lista) ).filter(excluido=False).all()
        s2240_altexprisco_infoamb_lista = s2240altExpRiscoinfoAmb.objects.using(db_slug).filter(s2240_altexprisco_id__in = listar_ids(s2240_altexprisco_lista) ).filter(excluido=False).all()
        s2240_altexprisco_fatrisco_lista = s2240altExpRiscofatRisco.objects.using(db_slug).filter(s2240_altexprisco_infoamb_id__in = listar_ids(s2240_altexprisco_infoamb_lista) ).filter(excluido=False).all()
        s2240_altexprisco_epc_lista = s2240altExpRiscoepc.objects.using(db_slug).filter(s2240_altexprisco_fatrisco_id__in = listar_ids(s2240_altexprisco_fatrisco_lista) ).filter(excluido=False).all()
        s2240_altexprisco_epi_lista = s2240altExpRiscoepi.objects.using(db_slug).filter(s2240_altexprisco_fatrisco_id__in = listar_ids(s2240_altexprisco_fatrisco_lista) ).filter(excluido=False).all()
        s2240_fimexprisco_lista = s2240fimExpRisco.objects.using(db_slug).filter(s2240_evtexprisco_id__in = listar_ids(s2240_evtexprisco_lista) ).filter(excluido=False).all()
        s2240_fimexprisco_infoamb_lista = s2240fimExpRiscoinfoAmb.objects.using(db_slug).filter(s2240_fimexprisco_id__in = listar_ids(s2240_fimexprisco_lista) ).filter(excluido=False).all()
        s2240_fimexprisco_respreg_lista = s2240fimExpRiscorespReg.objects.using(db_slug).filter(s2240_evtexprisco_id__in = listar_ids(s2240_evtexprisco_lista) ).filter(excluido=False).all()

        context = {
            'xmlns': xmlns,
            'versao': versao,
            'base': s2240_evtexprisco,
            's2240_evtexprisco_lista': s2240_evtexprisco_lista,
            's2240_evtexprisco_id': int(s2240_evtexprisco_id),
            's2240_evtexprisco': s2240_evtexprisco,

            's2240_iniexprisco_infoamb_lista': s2240_iniexprisco_infoamb_lista,
            's2240_iniexprisco_ativpericinsal_lista': s2240_iniexprisco_ativpericinsal_lista,
            's2240_iniexprisco_fatrisco_lista': s2240_iniexprisco_fatrisco_lista,
            's2240_iniexprisco_epc_lista': s2240_iniexprisco_epc_lista,
            's2240_iniexprisco_epi_lista': s2240_iniexprisco_epi_lista,
            's2240_iniexprisco_respreg_lista': s2240_iniexprisco_respreg_lista,
            's2240_iniexprisco_obs_lista': s2240_iniexprisco_obs_lista,
            's2240_altexprisco_lista': s2240_altexprisco_lista,
            's2240_altexprisco_infoamb_lista': s2240_altexprisco_infoamb_lista,
            's2240_altexprisco_fatrisco_lista': s2240_altexprisco_fatrisco_lista,
            's2240_altexprisco_epc_lista': s2240_altexprisco_epc_lista,
            's2240_altexprisco_epi_lista': s2240_altexprisco_epi_lista,
            's2240_fimexprisco_lista': s2240_fimexprisco_lista,
            's2240_fimexprisco_infoamb_lista': s2240_fimexprisco_infoamb_lista,
            's2240_fimexprisco_respreg_lista': s2240_fimexprisco_respreg_lista,
        }

        t = get_template('s2240_evtexprisco.xml')
        xml = t.render(context)
        return xml



@login_required
def recibo(request, hash, tipo):
    for_print = 0
    db_slug = 'default'

    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2240_evtexprisco_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])

    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2240_evtexprisco')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:

        s2240_evtexprisco = get_object_or_404(
            s2240evtExpRisco.objects.using( db_slug ),
            excluido = False, id = s2240_evtexprisco_id)

        from emensageriapro.mensageiro.models import RetornosEventos, RetornosEventosHorarios, \
            RetornosEventosIntervalos, RetornosEventosOcorrencias

        retorno = get_object_or_404( RetornosEventos.objects.using(db_slug),
            id=s2240_evtexprisco.retornos_eventos_id, excluido=False)

        retorno_horarios = RetornosEventosHorarios.objects.using(db_slug).\
            filter(retornos_eventos_id=retorno.id,excluido=False).all()

        retorno_intervalos = RetornosEventosIntervalos.objects.using(db_slug).\
            filter(retornos_eventos_horarios_id__in=listar_ids(retorno_horarios),excluido=False).all()

        retorno_ocorrencias = RetornosEventosOcorrencias.objects.using(db_slug).\
            filter(retornos_eventos_id=retorno.id,excluido=False).all()

        context = {
            's2240_evtexprisco_id': s2240_evtexprisco_id,
            's2240_evtexprisco': s2240_evtexprisco,
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
            response =  render_to_response('s2240_evtexprisco_recibo_pdf.html', context)
            filename = "%s.xls" % s2240_evtexprisco.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif tipo == 'CSV':
            response =  render_to_response('s2240_evtexprisco_recibo_csv.html', context)
            filename = "%s.csv" % s2240_evtexprisco.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        else:
            return render_to_pdf('s2240_evtexprisco_recibo_pdf.html', context)

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



def gerar_xml_assinado(s2240_evtexprisco_id, db_slug):
    from emensageriapro.mensageiro.functions.funcoes_esocial import salvar_arquivo_esocial
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes_esocial import assinar_esocial

    s2240_evtexprisco = get_object_or_404(
        s2240evtExpRisco.objects.using(db_slug),
        excluido=False,
        id=s2240_evtexprisco_id)

    if s2240_evtexprisco.arquivo_original:

        xml = ler_arquivo(s2240_evtexprisco.arquivo)

    else:

        xml = gerar_xml_s2240(s2240_evtexprisco_id, db_slug)

    if 'Signature' in xml:

        xml_assinado = xml

    else:

        xml_assinado = assinar_esocial(xml)

    if s2240_evtexprisco.status in (STATUS_EVENTO_CADASTRADO,
                           STATUS_EVENTO_IMPORTADO,
                           STATUS_EVENTO_DUPLICADO,
                           STATUS_EVENTO_GERADO):

        s2240evtExpRisco.objects.using(db_slug).\
            filter(id=s2240_evtexprisco_id,excluido=False).update(status=STATUS_EVENTO_ASSINADO)

    arquivo = 'arquivos/Eventos/s2240_evtexprisco/%s.xml' % (s2240_evtexprisco.identidade)

    os.system('mkdir -p %s/arquivos/Eventos/s2240_evtexprisco/' % BASE_DIR)

    if not os.path.exists(BASE_DIR+arquivo):

        salvar_arquivo_esocial(arquivo, xml_assinado, 1)

    xml_assinado = ler_arquivo(arquivo)

    return xml_assinado



@login_required
def gerar_xml(request, hash):


    db_slug = 'default'
    dict_hash = get_hash_url( hash )
    s2240_evtexprisco_id = int(dict_hash['id'])

    if s2240_evtexprisco_id:

        xml_assinado = gerar_xml_assinado(s2240_evtexprisco_id, db_slug)
        return HttpResponse(xml_assinado, content_type='text/xml')

    context = {'data': datetime.now(),}
    return render(request, 'permissao_negada.html', context)



@login_required
def duplicar(request, hash):

    from emensageriapro.esocial.views.s2240_evtexprisco_importar import read_s2240_evtexprisco_string
    from emensageriapro.functions import identidade_evento

    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s2240_evtexprisco_id = int(dict_hash['id'])

    if s2240_evtexprisco_id:

        s2240_evtexprisco = get_object_or_404(
            s2240evtExpRisco.objects.using(db_slug),
            excluido=False,
            id=s2240_evtexprisco_id)

        texto = gerar_xml_s2240(s2240_evtexprisco_id, db_slug, versao="|")
        dados = read_s2240_evtexprisco_string({}, texto.encode('utf-8'), 0)
        nova_identidade = identidade_evento(s2240_evtexprisco)

        s2240evtExpRisco.objects.using(db_slug).filter(id=dados['id']).\
            update(status=STATUS_EVENTO_CADASTRADO,
                   arquivo_original=0,
                   arquivo='')

        gravar_auditoria(u'{}', u'{"funcao": "Evento de identidade %s criado a partir da duplicação do evento %s"}' % (nova_identidade, s2240_evtexprisco.identidade),
            's2240_evtexprisco', dados['id'], request.user.id, 1)

        messages.success(request, u'Evento duplicado com sucesso! Foi criado uma nova identidade para este evento!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['id'] )
        return redirect('s2240_evtexprisco_salvar', hash=url_hash)

    messages.error(request, 'Erro ao duplicar evento!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])




@login_required
def criar_alteracao(request, hash):

    from emensageriapro.esocial.views.s2240_evtexprisco_importar import read_s2240_evtexprisco_string
    from emensageriapro.functions import identidade_evento

    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s2240_evtexprisco_id = int(dict_hash['id'])

    if s2240_evtexprisco_id:

        s2240_evtexprisco = get_object_or_404(
            s2240evtExpRisco.objects.using(db_slug),
            excluido=False,
            id=s2240_evtexprisco_id)

        texto = gerar_xml_s2240(s2240_evtexprisco_id, db_slug, versao="|")
        texto = texto.replace('<inclusao>','<alteracao>').replace('</inclusao>','</alteracao>')
        dados = read_s2240_evtexprisco_string({}, texto.encode('utf-8'), 0)
        nova_identidade = identidade_evento(s2240_evtexprisco)

        s2240evtExpRisco.objects.using(db_slug).filter(id=dados['id']).\
            update(status=STATUS_EVENTO_CADASTRADO,
                   arquivo_original=0,
                   arquivo='')

        gravar_auditoria(u'{}',
            u'{"funcao": "Evento de de alteração de identidade %s criado a partir da duplicação do evento %s"}' % (nova_identidade, s2240_evtexprisco.identidade),
            's2240_evtexprisco', dados['id'], request.user.id, 1)

        messages.success(request, u'Evento de alteração criado com sucesso!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['id'] )
        return redirect('s2240_evtexprisco_salvar', hash=url_hash)

    messages.error(request, 'Erro ao criar evento de alteração!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])




@login_required
def criar_exclusao(request, hash):

    from emensageriapro.esocial.views.s2240_evtexprisco_importar import read_s2240_evtexprisco_string
    from emensageriapro.functions import identidade_evento

    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s2240_evtexprisco_id = int(dict_hash['id'])

    if s2240_evtexprisco_id:

        s2240_evtexprisco = get_object_or_404(
            s2240evtExpRisco.objects.using(db_slug),
            excluido=False,
            id=s2240_evtexprisco_id)

        texto = gerar_xml_s2240(s2240_evtexprisco_id, db_slug, versao="|")
        texto = texto.replace('<inclusao>','<exclusao>').replace('</inclusao>','</exclusao>')
        texto = texto.replace('<alteracao>','<exclusao>').replace('</alteracao>','</exclusao>')
        dados = read_s2240_evtexprisco_string({}, texto.encode('utf-8'), 0)
        nova_identidade = identidade_evento(s2240_evtexprisco)

        s2240evtExpRisco.objects.using(db_slug).filter(id=dados['id']).\
            update(status=STATUS_EVENTO_CADASTRADO,
                   arquivo_original=0,
                   arquivo='')

        gravar_auditoria(u'{}',
            u'{"funcao": "Evento de exclusão de identidade %s criado a partir da duplicação do evento %s"}' % (nova_identidade, s2240_evtexprisco.identidade),
            's2240_evtexprisco', dados['id'], request.user.id, 1)

        messages.success(request, u'Evento de exclusão criado com sucesso!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['id'] )
        return redirect('s2240_evtexprisco_salvar', hash=url_hash)

    messages.error(request, 'Erro ao criar evento de exclusão!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])




@login_required
def alterar_identidade(request, hash):

    from emensageriapro.functions import identidade_evento
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s2240_evtexprisco_id = int(dict_hash['id'])

    if s2240_evtexprisco_id:

        s2240_evtexprisco = get_object_or_404(
            s2240evtExpRisco.objects.using(db_slug),
            excluido=False,
            id=s2240_evtexprisco_id)

        if s2240_evtexprisco.status == STATUS_EVENTO_CADASTRADO:

            nova_identidade = identidade_evento(s2240_evtexprisco)
            messages.success(request, u'Identidade do evento alterada com sucesso! Nova identidade: %s' % nova_identidade)
            url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % s2240_evtexprisco_id )

            gravar_auditoria(u'{}',
                u'{"funcao": "Identidade do evento foi alterada"}',
                's2240_evtexprisco', s2240_evtexprisco_id, request.user.id, 1)

            return redirect('s2240_evtexprisco_salvar', hash=url_hash)

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
    s2240_evtexprisco_id = int(dict_hash['id'])

    if s2240_evtexprisco_id:
        s2240_evtexprisco = get_object_or_404(s2240evtExpRisco.objects.using(db_slug), excluido=False, id=s2240_evtexprisco_id)

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

        if s2240_evtexprisco.status in status_list:
            s2240evtExpRisco.objects.using(db_slug).filter(id=s2240_evtexprisco_id).update(status=STATUS_EVENTO_CADASTRADO,
                                                                          arquivo_original=0)
            arquivo = 'arquivos/Eventos/s2240_evtexprisco/%s.xml' % (s2240_evtexprisco.identidade)

            if os.path.exists(BASE_DIR + '/' + arquivo):

                data_hora_atual = str(datetime.now()).replace(':','_').replace(' ','_').replace('.','_')
                dad = (BASE_DIR, s2240_evtexprisco.identidade, BASE_DIR, s2240_evtexprisco.identidade, data_hora_atual)
                os.system('mv %s/arquivos/Eventos/s2240_evtexprisco/%s.xml %s/arquivos/Eventos/s2240_evtexprisco/%s_backup_%s.xml' % dad)
                gravar_nome_arquivo('/arquivos/Eventos/s2240_evtexprisco/%s_backup_%s.xml' % (s2240_evtexprisco.identidade, data_hora_atual),
                    1)
            messages.success(request, 'Evento aberto para edição!')
            usuario_id = request.user.id
            gravar_auditoria(u'{}', u'{"funcao": "Evento aberto para edição"}',
                's2240_evtexprisco', s2240_evtexprisco_id, usuario_id, 1)
            url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % s2240_evtexprisco_id )
            return redirect('s2240_evtexprisco_salvar', hash=url_hash)
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



def validar_evento_funcao(s2240_evtexprisco_id, db_slug):
    from emensageriapro.padrao import executar_sql
    from emensageriapro.mensageiro.functions.funcoes_importacao import get_versao_evento
    from emensageriapro.mensageiro.functions.funcoes_validacoes_precedencia import validar_precedencia
    from emensageriapro.mensageiro.functions.funcoes_validacoes import get_schema_name, validar_schema
    from emensageriapro.settings import BASE_DIR, VERIFICAR_PREDECESSAO_ANTES_ENVIO
    lista_validacoes = []
    s2240_evtexprisco = get_object_or_404(s2240evtExpRisco.objects.using(db_slug), excluido=False, id=s2240_evtexprisco_id)

    #
    # Validações internas
    #

    arquivo = 'arquivos/Eventos/s2240_evtexprisco/%s.xml' % (s2240_evtexprisco.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/s2240_evtexprisco/' % BASE_DIR)
    lista = []
    tipo = 'esocial'
    if not os.path.exists(BASE_DIR + '/' + arquivo):
        gerar_xml_assinado(s2240_evtexprisco_id, db_slug)
    if os.path.exists(BASE_DIR + '/' + arquivo):
        texto_xml = ler_arquivo(arquivo).replace("s:", "")
        versao = get_versao_evento(texto_xml)
        from emensageriapro.esocial.views.s2240_evtexprisco_validar import validacoes_s2240_evtexprisco
        lista = validacoes_s2240_evtexprisco(arquivo)
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

        s2240evtExpRisco.objects.using( db_slug ).\
            filter(id=s2240_evtexprisco_id, excluido = False).\
            update(validacoes=validacoes,
                   status=STATUS_EVENTO_VALIDADO_ERRO)

    else:

        if VERIFICAR_PREDECESSAO_ANTES_ENVIO:

            quant = validar_precedencia('esocial', 's2240_evtexprisco', s2240_evtexprisco_id)

            if quant <= 0:

                s2240evtExpRisco.objects.using( db_slug ).\
                    filter(id=s2240_evtexprisco_id, excluido = False).\
                    update(validacoes=None,
                           status=STATUS_EVENTO_AGUARD_PRECEDENCIA)

            else:

                s2240evtExpRisco.objects.using( db_slug ).\
                    filter(id=s2240_evtexprisco_id, excluido = False).\
                    update(validacoes=None,
                           status=STATUS_EVENTO_AGUARD_ENVIO)

        else:

            s2240evtExpRisco.objects.using(db_slug). \
                filter(id=s2240_evtexprisco_id, excluido=False).\
                update(validacoes=None,
                       status=STATUS_EVENTO_AGUARD_ENVIO)

    return lista_validacoes



@login_required
def validar_evento(request, hash):

    from emensageriapro.settings import VERSOES_ESOCIAL, VERIFICAR_PREDECESSAO_ANTES_ENVIO
    # from emensageriapro.mensageiro.functions.funcoes_validacoes import VERSAO_ATUAL

    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s2240_evtexprisco_id = int(dict_hash['id'])

    if s2240_evtexprisco_id:

        s2240_evtexprisco = get_object_or_404(
            s2240evtExpRisco.objects.using(db_slug),
            excluido=False,
            id=s2240_evtexprisco_id)

        if s2240_evtexprisco.versao in VERSOES_ESOCIAL:

            validar_evento_funcao(s2240_evtexprisco_id, db_slug)

            if s2240_evtexprisco.transmissor_lote_esocial and not VERIFICAR_PREDECESSAO_ANTES_ENVIO:
                s2240evtExpRisco.objects.using(db_slug).\
                    filter(excluido=False, id=s2240_evtexprisco_id).update(status=STATUS_EVENTO_AGUARD_ENVIO)

            elif s2240_evtexprisco.transmissor_lote_esocial and VERIFICAR_PREDECESSAO_ANTES_ENVIO:
                s2240evtExpRisco.objects.using(db_slug).\
                    filter(excluido=False, id=s2240_evtexprisco_id).update(status=STATUS_EVENTO_AGUARD_PRECEDENCIA)

            messages.success(request, u'Validações processadas com sucesso!')

        else:

            messages.error(request, u'Não foi possível validar o evento pois a versão do evento não é compatível com a versão do sistema!')
    else:

        messages.error(request, u'Não foi possível validar o evento pois o mesmo não foi identificado!')

    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
