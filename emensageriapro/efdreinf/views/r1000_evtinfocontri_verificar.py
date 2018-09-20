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
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
import base64
from emensageriapro.r1000.models import *
from emensageriapro.r1000.forms import *
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
def verificar(request, hash, slug=0):
    for_print = 0
    if slug:
        conta = get_json(slug)
        if not conta:  
            raise Http404 
        else:
            db_slug = 'emensageriapro'+str(conta.id)
    else:
        db_slug = 'default'
        conta = None
    try: 
        usuario_id = request.user.id   
        dict_hash = get_hash_url( hash )
        r1000_evtinfocontri_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r1000_evtinfocontri')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri.objects.using( db_slug ), excluido = False, id = r1000_evtinfocontri_id)
        r1000_evtinfocontri_lista = r1000evtInfoContri.objects.using( db_slug ).filter(id=r1000_evtinfocontri_id, excluido = False).all()
        
    
        r1000_inclusao_lista = r1000inclusao.objects.using(db_slug).filter(r1000_evtinfocontri_id__in = listar_ids(r1000_evtinfocontri_lista) ).filter(excluido=False).all()    
        r1000_inclusao_softhouse_lista = r1000inclusaosoftHouse.objects.using(db_slug).filter(r1000_inclusao_id__in = listar_ids(r1000_inclusao_lista) ).filter(excluido=False).all()    
        r1000_inclusao_infoefr_lista = r1000inclusaoinfoEFR.objects.using(db_slug).filter(r1000_inclusao_id__in = listar_ids(r1000_inclusao_lista) ).filter(excluido=False).all()    
        r1000_alteracao_lista = r1000alteracao.objects.using(db_slug).filter(r1000_evtinfocontri_id__in = listar_ids(r1000_evtinfocontri_lista) ).filter(excluido=False).all()    
        r1000_alteracao_softhouse_lista = r1000alteracaosoftHouse.objects.using(db_slug).filter(r1000_alteracao_id__in = listar_ids(r1000_alteracao_lista) ).filter(excluido=False).all()    
        r1000_alteracao_infoefr_lista = r1000alteracaoinfoEFR.objects.using(db_slug).filter(r1000_alteracao_id__in = listar_ids(r1000_alteracao_lista) ).filter(excluido=False).all()    
        r1000_alteracao_novavalidade_lista = r1000alteracaonovaValidade.objects.using(db_slug).filter(r1000_alteracao_id__in = listar_ids(r1000_alteracao_lista) ).filter(excluido=False).all()    
        r1000_exclusao_lista = r1000exclusao.objects.using(db_slug).filter(r1000_evtinfocontri_id__in = listar_ids(r1000_evtinfocontri_lista) ).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r1000_evtinfocontri'
        context = {
            'r1000_evtinfocontri_lista': r1000_evtinfocontri_lista,
            'r1000_evtinfocontri_id': r1000_evtinfocontri_id, 
            'r1000_evtinfocontri': r1000_evtinfocontri, 
            'conta': conta, 
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            'slug': slug,
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,
    
            'r1000_inclusao_lista': r1000_inclusao_lista,    
            'r1000_inclusao_softhouse_lista': r1000_inclusao_softhouse_lista,    
            'r1000_inclusao_infoefr_lista': r1000_inclusao_infoefr_lista,    
            'r1000_alteracao_lista': r1000_alteracao_lista,    
            'r1000_alteracao_softhouse_lista': r1000_alteracao_softhouse_lista,    
            'r1000_alteracao_infoefr_lista': r1000_alteracao_infoefr_lista,    
            'r1000_alteracao_novavalidade_lista': r1000_alteracao_novavalidade_lista,    
            'r1000_exclusao_lista': r1000_exclusao_lista,
        }
        if for_print == 2:
            #return render_to_pdf('%s/r1000_evtinfocontri_verificar.html' % r1000_evtinfocontri.versao, context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(request=request,
                                           template='%s/r1000_evtinfocontri_verificar.html' % r1000_evtinfocontri.versao,
                                           filename="r1000_evtinfocontri.pdf",
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
            response =  render_to_response('%s/r1000_evtinfocontri_verificar.html' % r1000_evtinfocontri.versao, context)
            filename = "%s.xls" % r1000_evtinfocontri.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response =  render_to_response('%s/r1000_evtinfocontri_verificar.html' % r1000_evtinfocontri.versao, context)
            filename = "%s.csv" % r1000_evtinfocontri.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        else:
            return render(request, '%s/r1000_evtinfocontri_verificar.html' % r1000_evtinfocontri.versao, context)
    else:
        context = {
            'usuario': usuario, 
            'conta': conta, 
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            'slug': slug,
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)




def gerar_xml_r1000(r1000_evtinfocontri_id, db_slug):
    from django.template.loader import get_template
    if r1000_evtinfocontri_id:
        r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri.objects.using( db_slug ), excluido = False, id = r1000_evtinfocontri_id)
        r1000_evtinfocontri_lista = r1000evtInfoContri.objects.using( db_slug ).filter(id=r1000_evtinfocontri_id, excluido = False).all()
    
        r1000_inclusao_lista = r1000inclusao.objects.using(db_slug).filter(r1000_evtinfocontri_id__in = listar_ids(r1000_evtinfocontri_lista) ).filter(excluido=False).all()    
        r1000_inclusao_softhouse_lista = r1000inclusaosoftHouse.objects.using(db_slug).filter(r1000_inclusao_id__in = listar_ids(r1000_inclusao_lista) ).filter(excluido=False).all()    
        r1000_inclusao_infoefr_lista = r1000inclusaoinfoEFR.objects.using(db_slug).filter(r1000_inclusao_id__in = listar_ids(r1000_inclusao_lista) ).filter(excluido=False).all()    
        r1000_alteracao_lista = r1000alteracao.objects.using(db_slug).filter(r1000_evtinfocontri_id__in = listar_ids(r1000_evtinfocontri_lista) ).filter(excluido=False).all()    
        r1000_alteracao_softhouse_lista = r1000alteracaosoftHouse.objects.using(db_slug).filter(r1000_alteracao_id__in = listar_ids(r1000_alteracao_lista) ).filter(excluido=False).all()    
        r1000_alteracao_infoefr_lista = r1000alteracaoinfoEFR.objects.using(db_slug).filter(r1000_alteracao_id__in = listar_ids(r1000_alteracao_lista) ).filter(excluido=False).all()    
        r1000_alteracao_novavalidade_lista = r1000alteracaonovaValidade.objects.using(db_slug).filter(r1000_alteracao_id__in = listar_ids(r1000_alteracao_lista) ).filter(excluido=False).all()    
        r1000_exclusao_lista = r1000exclusao.objects.using(db_slug).filter(r1000_evtinfocontri_id__in = listar_ids(r1000_evtinfocontri_lista) ).filter(excluido=False).all()
        context = {
            'base': r1000_evtinfocontri,
            'r1000_evtinfocontri_lista': r1000_evtinfocontri_lista,
            'r1000_evtinfocontri_id': int(r1000_evtinfocontri_id), 
            'r1000_evtinfocontri': r1000_evtinfocontri,
    
            'r1000_inclusao_lista': r1000_inclusao_lista,    
            'r1000_inclusao_softhouse_lista': r1000_inclusao_softhouse_lista,    
            'r1000_inclusao_infoefr_lista': r1000_inclusao_infoefr_lista,    
            'r1000_alteracao_lista': r1000_alteracao_lista,    
            'r1000_alteracao_softhouse_lista': r1000_alteracao_softhouse_lista,    
            'r1000_alteracao_infoefr_lista': r1000_alteracao_infoefr_lista,    
            'r1000_alteracao_novavalidade_lista': r1000_alteracao_novavalidade_lista,    
            'r1000_exclusao_lista': r1000_exclusao_lista,
        }
        #return render(request, 'xml/%s/r1000_evtinfocontri.html' % r1000_evtinfocontri.versao, context, content_type='text/xml')
        t = get_template('%s/r1000_evtinfocontri_xml.html' % r1000_evtinfocontri.versao)
        xml = t.render(context)
        return xml
        




@login_required
def recibo(request, hash, tipo, slug=0):
    from emensageriapro.efdreinf.models import r5001evtTotal, r5011evtTotalContrib
    from emensageriapro.r5001.models import r5001regOcorrs, r5001infoTotal, r5001RTom, \
        r5001infoCRTom, r5001RPrest, r5001RRecRepAD, r5001RComl, r5001RCPRB,r5001RRecEspetDesp
    from emensageriapro.r5011.models import r5011regOcorrs, r5011infoTotalContrib, r5011RTom, \
        r5011infoCRTom, r5011RPrest, r5011RRecRepAD, r5011RComl, r5011RCPRB
    
    for_print = 0
    if slug:
        conta = get_json(slug)
        if not conta:  
            raise Http404 
        else:
            db_slug = 'emensageriapro'+str(conta.id)
    else:
        db_slug = 'default'
        conta = None
    try: 
        usuario_id = request.user.id   
        dict_hash = get_hash_url( hash )
        r1000_evtinfocontri_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r1000_evtinfocontri')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        
        r1000_evtinfocontri = get_object_or_404(
            r1000evtInfoContri.objects.using( db_slug ),
            excluido = False, id = r1000_evtinfocontri_id)
    

        if r1000_evtinfocontri.retornos_evttotal_id:

            r5001evtTotal_dados = get_object_or_404( r5001evtTotal.objects.using(db_slug),
                id=r1000_evtinfocontri.retornos_evttotal_id, excluido=False)

            r5001infoTotal_dados = r5001infoTotal.objects.using(db_slug).\
                filter(r5001_evttotal_id=r5001evtTotal_dados.id,excluido=False).all()

            r5001RCPRB_dados = r5001RCPRB.objects.using(db_slug).\
                filter(r5001_infototal_id__in=listar_ids(r5001infoTotal_dados),excluido=False).all()

            r5001RComl_dados = r5001RComl.objects.using(db_slug).\
                filter(r5001_infototal_id__in=listar_ids(r5001infoTotal_dados),excluido=False).all()

            r5001RPrest_dados = r5001RPrest.objects.using(db_slug).\
                filter(r5001_infototal_id__in=listar_ids(r5001infoTotal_dados),excluido=False).all()

            r5001RRecEspetDesp_dados = r5001RRecEspetDesp.objects.using(db_slug).\
                filter(r5001_infototal_id__in=listar_ids(r5001infoTotal_dados),excluido=False).all()

            r5001RRecRepAD_dados = r5001RRecRepAD.objects.using(db_slug).\
                filter(r5001_infototal_id__in=listar_ids(r5001infoTotal_dados),excluido=False).all()

            r5001RTom_dados = r5001RTom.objects.using(db_slug).\
                filter(r5001_infototal_id__in=listar_ids(r5001infoTotal_dados),excluido=False).all()

            r5001infoCRTom_dados = r5001infoCRTom.objects.using(db_slug).\
                filter(r5001_rtom_id__in=listar_ids(r5001RTom_dados),excluido=False).all()

            r5001regOcorrs_dados = r5001regOcorrs.objects.using(db_slug).\
                filter(r5001_evttotal_id=r5001evtTotal_dados.id,excluido=False).all()

        else:

            r5001evtTotal_dados = None

            r5001infoTotal_dados = None

            r5001RCPRB_dados = None

            r5001RComl_dados = None

            r5001RPrest_dados = None

            r5001RRecEspetDesp_dados = None

            r5001RRecRepAD_dados = None

            r5001RTom_dados = None

            r5001infoCRTom_dados = None

            r5001regOcorrs_dados = None

        if r1000_evtinfocontri.retornos_evttotalcontrib_id:

            r5011evtTotalContrib_dados = get_object_or_404( r5011evtTotalContrib.objects.using(db_slug),
                id=r1000_evtinfocontri.retornos_evttotalcontrib_id, excluido=False)

            r5011infoTotalContrib_dados = r5011infoTotalContrib.objects.using(db_slug).\
                filter(r5011_evttotalcontrib_id=r5011evtTotalContrib_dados.id,excluido=False).all()

            r5011RCPRB_dados = r5011RCPRB.objects.using(db_slug).\
                filter(r5011_infototalcontrib_id__in=listar_ids(r5011infoTotalContrib_dados),excluido=False).all()

            r5011RComl_dados = r5011RComl.objects.using(db_slug).\
                filter(r5011_infototalcontrib_id__in=listar_ids(r5011infoTotalContrib_dados),excluido=False).all()

            r5011RPrest_dados = r5011RPrest.objects.using(db_slug).\
                filter(r5011_infototalcontrib_id__in=listar_ids(r5011infoTotalContrib_dados),excluido=False).all()

            r5011RRecEspetDesp_dados = None

            r5011RRecRepAD_dados = r5011RRecRepAD.objects.using(db_slug).\
                filter(r5011_infototalcontrib_id__in=listar_ids(r5011infoTotalContrib_dados),excluido=False).all()

            r5011RTom_dados = r5011RTom.objects.using(db_slug).\
                filter(r5011_infototalcontrib_id__in=listar_ids(r5011infoTotalContrib_dados),excluido=False).all()

            r5011infoCRTom_dados = r5011infoCRTom.objects.using(db_slug).\
                filter(r5011_rtom_id__in=listar_ids(r5011RTom_dados),excluido=False).all()

            r5011regOcorrs_dados = r5011regOcorrs.objects.using(db_slug).\
                filter(r5011_evttotalcontrib_id=r5011evtTotalContrib_dados.id,excluido=False).all()

        else:

            r5011evtTotalContrib_dados = None

            r5011infoTotalContrib_dados = None

            r5011RCPRB_dados = None

            r5011RComl_dados = None

            r5011RPrest_dados = None

            r5011RRecEspetDesp_dados = None

            r5011RRecRepAD_dados = None

            r5011RTom_dados = None

            r5011infoCRTom_dados = None

            r5011regOcorrs_dados = None



        
        context = {
            'r1000_evtinfocontri_id': r1000_evtinfocontri_id, 
            'r1000_evtinfocontri': r1000_evtinfocontri, 

            'r5001evtTotal_dados': r5001evtTotal_dados,
            'r5001infoTotal_dados': r5001infoTotal_dados,
            'r5001RCPRB_dados': r5001RCPRB_dados,
            'r5001RComl_dados': r5001RComl_dados,
            'r5001RPrest_dados': r5001RPrest_dados,
            'r5001RRecEspetDesp_dados': r5001RRecEspetDesp_dados,
            'r5001RRecRepAD_dados': r5001RRecRepAD_dados,
            'r5001RTom_dados': r5001RTom_dados,
            'r5001infoCRTom_dados': r5001infoCRTom_dados,
            'r5001regOcorrs_dados': r5001regOcorrs_dados,

            'r5011evtTotalContrib_dados': r5011evtTotalContrib_dados,
            'r5011infoTotalContrib_dados': r5011infoTotalContrib_dados,
            'r5011RCPRB_dados': r5011RCPRB_dados,
            'r5011RComl_dados': r5011RComl_dados,
            'r5011RPrest_dados': r5011RPrest_dados,
            'r5011RRecEspetDesp_dados': r5011RRecEspetDesp_dados,
            'r5011RRecRepAD_dados': r5011RRecRepAD_dados,
            'r5011RTom_dados': r5011RTom_dados,
            'r5011infoCRTom_dados': r5011infoCRTom_dados,
            'r5011regOcorrs_dados': r5011regOcorrs_dados,

            'conta': conta, 
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            'slug': slug,
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,
        }
     

        if tipo == 'XLS':
            from django.shortcuts import render_to_response
            response =  render_to_response('r1000_evtinfocontri_recibo_pdf.html', context)
            filename = "%s.xls" % r1000_evtinfocontri.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif tipo == 'CSV':
            from django.shortcuts import render_to_response
            response =  render_to_response('r1000_evtinfocontri_recibo_csv.html', context)
            filename = "%s.csv" % r1000_evtinfocontri.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        else:
            return render_to_pdf('r1000_evtinfocontri_recibo_pdf.html', context)
    else:
        context = {
            'usuario': usuario, 
            'conta': conta, 
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            'slug': slug,
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)




def gerar_xml_assinado(r1000_evtinfocontri_id, db_slug):
    import os
    from datetime import datetime 
    from django.http import HttpResponse
    from emensageriapro.funcoes_efdreinf import salvar_arquivo_efdreinf
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.funcoes_efdreinf import assinar_efdreinf
    r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri.objects.using(db_slug), excluido=False, id=r1000_evtinfocontri_id)
    if r1000_evtinfocontri.arquivo_original:
        xml = ler_arquivo(r1000_evtinfocontri.arquivo)
    else:
        xml = gerar_xml_r1000(r1000_evtinfocontri_id, db_slug)
    if 'Signature' in xml:
        xml_assinado = xml
    else:
        xml_assinado = assinar_efdreinf(xml)
    if r1000_evtinfocontri.status in (0,1,2,11):
        r1000evtInfoContri.objects.using(db_slug).filter(id=r1000_evtinfocontri_id,excluido=False).update(status=10)
    arquivo = 'arquivos/Eventos/r1000_evtinfocontri/%s.xml' % (r1000_evtinfocontri.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/r1000_evtinfocontri/' % BASE_DIR)
    if not os.path.exists(BASE_DIR+arquivo):
        salvar_arquivo_efdreinf(arquivo, xml_assinado, 1)
    xml_assinado = ler_arquivo(arquivo)
    return xml_assinado



@login_required
def gerar_xml(request, hash, slug=0):
    import os
    from datetime import datetime 
    from django.http import HttpResponse
    from emensageriapro.funcoes_efdreinf import salvar_arquivo_efdreinf
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.funcoes_efdreinf import assinar_efdreinf
    hora_atual = str(datetime.now()).replace(' ', '_').replace('.', '_').replace(':', '_') 
    for_print = 0
    if slug:
        conta = get_json(slug)
        if not conta:  
            raise Http404 
        else:
            db_slug = 'emensageriapro'+str(conta.id)
    else:
        db_slug = 'default'
        conta = None
    dict_hash = get_hash_url( hash )
    r1000_evtinfocontri_id = int(dict_hash['id'])
    if r1000_evtinfocontri_id:
        r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri.objects.using(db_slug), excluido=False, id=r1000_evtinfocontri_id)
        xml_assinado = gerar_xml_assinado(r1000_evtinfocontri_id, db_slug)
        return HttpResponse(xml_assinado, content_type='text/xml')
    else:
        context = {
            'conta': conta, 
            'slug': slug,
            'data': datetime.datetime.now(),
        }
        return render(request, 'permissao_negada.html', context)


@login_required
def duplicar(request, hash):
    from emensageriapro.settings import BASE_DIR
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    r1000_evtinfocontri_id = int(dict_hash['id'])
    if r1000_evtinfocontri_id:
        r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri.objects.using(db_slug), excluido=False,
                                                    id=r1000_evtinfocontri_id)

        arquivo = 'arquivos/Eventos/r1000_evtinfocontri/%s.xml' % r1000_evtinfocontri.identidade
        if not os.path.exists(BASE_DIR + '/' + arquivo):
            xml = gerar_xml_assinado(r1000_evtinfocontri_id, db_slug)
        
        texto = ler_arquivo('arquivos/Eventos/r1000_evtinfocontri/%s.xml' % r1000_evtinfocontri.identidade)
        salvar_arquivo('arquivos/Eventos/r1000_evtinfocontri/%s_duplicado_temp.xml' % r1000_evtinfocontri.identidade, texto)
        from emensageriapro.funcoes_importacao import importar_arquivo
        dados = importar_arquivo('arquivos/Eventos/r1000_evtinfocontri/%s_duplicado_temp.xml' % r1000_evtinfocontri.identidade, request)
        from emensageriapro.efdreinf.views.r1000_evtinfocontri import identidade_evento
        dent = identidade_evento(dados['identidade'], db_slug)
        r1000evtInfoContri.objects.using(db_slug).filter(id=dados['identidade']).update(status=0, arquivo_original=0, arquivo='')
        messages.success(request, 'Evento duplicado com sucesso! Foi criado uma nova identidade para este evento!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['identidade'] )
        usuario_id = request.user.id
        gravar_auditoria(u'{}', u'{"funcao": "Evento de identidade %s criado a partir da duplicação do evento %s"}' % (dent, r1000_evtinfocontri.identidade), 
            'r1000_evtinfocontri', dados['identidade'], usuario_id, 1)
        return redirect('r1000_evtinfocontri_salvar', hash=url_hash)
    messages.error(request, 'Erro ao duplicar evento!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])



@login_required
def criar_alteracao(request, hash):
    from emensageriapro.settings import BASE_DIR
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    r1000_evtinfocontri_id = int(dict_hash['id'])
    if r1000_evtinfocontri_id:
        r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri.objects.using(db_slug), excluido=False,
                                                    id=r1000_evtinfocontri_id)
        arquivo = 'arquivos/Eventos/r1000_evtinfocontri/%s.xml' % r1000_evtinfocontri.identidade
        if not os.path.exists(BASE_DIR + '/' + arquivo):
            xml = gerar_xml_assinado(r1000_evtinfocontri_id, db_slug)
        texto = ler_arquivo('arquivos/Eventos/r1000_evtinfocontri/%s.xml' % r1000_evtinfocontri.identidade)
        texto = texto.replace('<inclusao>','<alteracao>').replace('</inclusao>','</alteracao>')
        salvar_arquivo('arquivos/Eventos/r1000_evtinfocontri/%s_alteracao_temp.xml' % r1000_evtinfocontri.identidade, texto)
        from emensageriapro.funcoes_importacao import importar_arquivo
        dados = importar_arquivo('arquivos/Eventos/r1000_evtinfocontri/%s_alteracao_temp.xml' % r1000_evtinfocontri.identidade, request)
        from emensageriapro.efdreinf.views.r1000_evtinfocontri import identidade_evento
        dent = identidade_evento(dados['identidade'], db_slug)
        r1000evtInfoContri.objects.using(db_slug).filter(id=dados['identidade']).update(status=0, arquivo_original=0, arquivo='')
        usuario_id = request.user.id
        gravar_auditoria(u'{}', u'{"funcao": "Evento de de alteração de identidade %s criado a partir da duplicação do evento %s"}' % (dent, r1000_evtinfocontri.identidade), 
            'r1000_evtinfocontri', dados['identidade'], usuario_id, 1)
        messages.success(request, 'Evento de alteração criado com sucesso!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['identidade'] )
        return redirect('r1000_evtinfocontri_salvar', hash=url_hash)
    messages.error(request, 'Erro ao criar evento de alteração!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])



@login_required
def criar_exclusao(request, hash):
    from emensageriapro.settings import BASE_DIR
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    r1000_evtinfocontri_id = int(dict_hash['id'])
    if r1000_evtinfocontri_id:
        r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri.objects.using(db_slug), excluido=False,
                                                    id=r1000_evtinfocontri_id)
        arquivo = 'arquivos/Eventos/r1000_evtinfocontri/%s.xml' % r1000_evtinfocontri.identidade
        if not os.path.exists(BASE_DIR + '/' + arquivo):
            xml = gerar_xml_assinado(r1000_evtinfocontri_id, db_slug)
        texto = ler_arquivo('arquivos/Eventos/r1000_evtinfocontri/%s.xml' % r1000_evtinfocontri.identidade)
        texto = texto.replace('<inclusao>','<exclusao>').replace('</inclusao>','</exclusao>')
        texto = texto.replace('<alteracao>','<exclusao>').replace('</alteracao>','</exclusao>')
        salvar_arquivo('arquivos/Eventos/r1000_evtinfocontri/%s_exclusao_temp.xml' % r1000_evtinfocontri.identidade, texto)
        from emensageriapro.funcoes_importacao import importar_arquivo
        dados = importar_arquivo('arquivos/Eventos/r1000_evtinfocontri/%s_exclusao_temp.xml' % r1000_evtinfocontri.identidade, request)
        from emensageriapro.efdreinf.views.r1000_evtinfocontri import identidade_evento
        dent = identidade_evento(dados['identidade'], db_slug)
        r1000evtInfoContri.objects.using(db_slug).filter(id=dados['identidade']).update(status=0, arquivo_original=0, arquivo='')
        usuario_id = request.user.id
        gravar_auditoria(u'{}', u'{"funcao": "Evento de exclusão de identidade %s criado a partir da duplicação do evento %s"}' % (dent, r1000_evtinfocontri.identidade), 
            'r1000_evtinfocontri', dados['identidade'], usuario_id, 1)
        messages.success(request, 'Evento de exclusão criado com sucesso!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['identidade'] )
        return redirect('r1000_evtinfocontri_salvar', hash=url_hash)
    messages.error(request, 'Erro ao criar evento de exclusão!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])




@login_required
def alterar_identidade(request, hash):
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    r1000_evtinfocontri_id = int(dict_hash['id'])
    if r1000_evtinfocontri_id:
        r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri.objects.using(db_slug), excluido=False,
                                                    id=r1000_evtinfocontri_id)
        if r1000_evtinfocontri.status == 0:
            from emensageriapro.efdreinf.views.r1000_evtinfocontri import identidade_evento
            dent = identidade_evento(r1000_evtinfocontri_id, db_slug)
            messages.success(request, 'Identidade do evento alterada com sucesso!')
            usuario_id = request.user.id 
            gravar_auditoria(u'{}', u'{"funcao": "Identidade do evento foi alterada"}', 
            'r1000_evtinfocontri', r1000_evtinfocontri_id, usuario_id, 1)
            url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % r1000_evtinfocontri_id )
            return redirect('r1000_evtinfocontri_salvar', hash=url_hash)
        else:
            messages.error(request, 'Não foi possível alterar a identidade do evento! Somente é possível alterar o status de eventos que estão abertos para edição (status: Cadastrado)!')
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])

    messages.error(request, 'Erro ao alterar identidade do evento!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])



@login_required
def abrir_evento_para_edicao(request, hash):
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.funcoes_efdreinf import gravar_nome_arquivo
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    r1000_evtinfocontri_id = int(dict_hash['id'])
    if r1000_evtinfocontri_id:
        r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri.objects.using(db_slug), excluido=False, id=r1000_evtinfocontri_id)
        if r1000_evtinfocontri.status in (0, 1, 2, 3, 4, 5, 10, 11):
            r1000evtInfoContri.objects.using(db_slug).filter(id=r1000_evtinfocontri_id).update(status=0, arquivo_original=0)
            arquivo = 'arquivos/Eventos/r1000_evtinfocontri/%s.xml' % (r1000_evtinfocontri.identidade)
            if os.path.exists(BASE_DIR + '/' + arquivo):
                from datetime import datetime
                data_hora_atual = str(datetime.now()).replace(':','_').replace(' ','_').replace('.','_')
                dad = (BASE_DIR, r1000_evtinfocontri.identidade, BASE_DIR, r1000_evtinfocontri.identidade, data_hora_atual)
                os.system('mv %s/arquivos/Eventos/r1000_evtinfocontri/%s.xml %s/arquivos/Eventos/r1000_evtinfocontri/%s_backup_%s.xml' % dad)
                gravar_nome_arquivo('/arquivos/Eventos/r1000_evtinfocontri/%s_backup_%s.xml' % (r1000_evtinfocontri.identidade, data_hora_atual), 
                    1)
            messages.success(request, 'Evento aberto para edição!')
            usuario_id = request.user.id 
            gravar_auditoria(u'{}', u'{"funcao": "Evento aberto para edição"}', 
            'r1000_evtinfocontri', r1000_evtinfocontri_id, usuario_id, 1)
            url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % r1000_evtinfocontri_id )
            return redirect('r1000_evtinfocontri_salvar', hash=url_hash)
        else:
            messages.error(request, '''
            Não foi possível abrir o evento para edição! Somente é possível 
            abrir eventos com os seguintes status: "Cadastrado", "Importado", "Validado", 
            "Duplicado", "Erro na validação", "XML Assinado" ou "XML Gerado"
             ou com o status "Enviado com sucesso" e os seguintes códigos de resposta do servidor:
             "401 - Lote Incorreto - Erro preenchimento" ou "402 - Lote Incorreto - schema Inválido"!''')
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])

    messages.error(request, 'Erro ao abrir evento para edição!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])



@login_required
def validar_evento_funcao(r1000_evtinfocontri_id, db_slug):
    from emensageriapro.padrao import executar_sql
    from emensageriapro.funcoes_importacao import get_versao_evento
    from emensageriapro.funcoes_validacoes_precedencia import validar_precedencia
    from emensageriapro.funcoes_validacoes import get_schema_name, validar_schema
    from emensageriapro.settings import BASE_DIR
    lista_validacoes = []
    r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri.objects.using(db_slug), excluido=False, id=r1000_evtinfocontri_id)
    quant = validar_precedencia('efdreinf', 'r1000_evtinfocontri', r1000_evtinfocontri_id)
    if quant <= 0:
        lista_validacoes.append('Precedência não foi enviada!')
        precedencia = 0
    else:
        precedencia = 1
    executar_sql("UPDATE public.r1000_evtinfocontri SET validacao_precedencia=%s WHERE id=%s;" % (precedencia, r1000_evtinfocontri_id), False)
    #
    # Validações internas
    #
    arquivo = 'arquivos/Eventos/r1000_evtinfocontri/%s.xml' % (r1000_evtinfocontri.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/r1000_evtinfocontri/' % BASE_DIR)
    lista = []
    tipo = 'efdreinf'
    if not os.path.exists(BASE_DIR + '/' + arquivo):
        gerar_xml_assinado(r1000_evtinfocontri_id, db_slug)
    if os.path.exists(BASE_DIR + '/' + arquivo):
        texto_xml = ler_arquivo(arquivo).replace("s:", "")
        versao = get_versao_evento(texto_xml)
        if tipo == 'esocial':
            if versao == 'v02_04_02':
                from emensageriapro.esocial.validacoes.v02_04_02.r1000_evtinfocontri import validacoes_r1000_evtinfocontri
                lista = validacoes_r1000_evtinfocontri(arquivo)
        elif tipo == 'efdreinf':
            if versao == 'v1_03_02':
                from emensageriapro.efdreinf.validacoes.v1_03_02.r1000_evtinfocontri import validacoes_r1000_evtinfocontri
                lista = validacoes_r1000_evtinfocontri(arquivo)
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
        executar_sql("UPDATE public.r1000_evtinfocontri SET validacoes='%s', status=3 WHERE id=%s;" % ('<br>'.join(lista_validacoes).replace("'","''"), r1000_evtinfocontri_id), False)
    else:
        executar_sql("UPDATE public.r1000_evtinfocontri SET validacoes='', status=4 WHERE id=%s;" % (r1000_evtinfocontri_id), False)
    return lista_validacoes



@login_required
def validar_evento(request, hash):
    from emensageriapro.funcoes_validacoes import VERSAO_ATUAL
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    r1000_evtinfocontri_id = int(dict_hash['id'])
    if r1000_evtinfocontri_id:
        lista_validacoes = []
        r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri.objects.using(db_slug), excluido=False, id=r1000_evtinfocontri_id)
        if r1000_evtinfocontri.versao in VERSAO_ATUAL:
            lista_validacoes = validar_evento_funcao(r1000_evtinfocontri_id, db_slug)
            messages.success(request, 'Validações processadas com sucesso!')
        else:
            messages.error(request, 'Não foi possível validar o evento pois a versão do evento não é compatível com a versão do sistema!')
    else:    
        messages.error(request, 'Não foi possível validar o evento pois o mesmo não foi identificado!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
