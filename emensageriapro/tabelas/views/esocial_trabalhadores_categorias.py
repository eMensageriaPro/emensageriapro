#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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

import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.tabelas.forms import *
from emensageriapro.tabelas.models import *
from emensageriapro.controle_de_acesso.models import *
import base64
from emensageriapro.s1200.models import s1200remunOutrEmpr
from emensageriapro.s1200.models import s1200dmDev
from emensageriapro.s1202.models import s1202dmDev
from emensageriapro.s1202.models import s1202infoPerApurremunPerApur
from emensageriapro.s1202.models import s1202infoPerAntremunPerAnt
from emensageriapro.s1210.models import s1210detPgtoFer
from emensageriapro.s1210.models import s1210detPgtoAnt
from emensageriapro.esocial.models import s2200evtAdmissao
from emensageriapro.esocial.models import s2206evtAltContratual
from emensageriapro.esocial.models import s2210evtCAT
from emensageriapro.esocial.models import s2220evtMonit
from emensageriapro.esocial.models import s2221evtToxic
from emensageriapro.esocial.models import s2230evtAfastTemp
from emensageriapro.esocial.models import s2240evtExpRisco
from emensageriapro.esocial.models import s2245evtTreiCap
from emensageriapro.s2299.models import s2299infoTrabIntermremunOutrEmpr
from emensageriapro.esocial.models import s2300evtTSVInicio
from emensageriapro.esocial.models import s2306evtTSVAltContr
from emensageriapro.esocial.models import s2399evtTSVTermino
from emensageriapro.s2399.models import s2399remunOutrEmpr
from emensageriapro.s5001.models import s5001infoCategIncid
from emensageriapro.s5002.models import s5002infoIrrf
from emensageriapro.s5003.models import s5003infoTrabFGTS
from emensageriapro.s5003.models import s5003infoTrabDps
from emensageriapro.s5011.models import s5011basesRemun
from emensageriapro.s1200.forms import form_s1200_remunoutrempr
from emensageriapro.s1200.forms import form_s1200_dmdev
from emensageriapro.s1202.forms import form_s1202_dmdev
from emensageriapro.s1202.forms import form_s1202_infoperapur_remunperapur
from emensageriapro.s1202.forms import form_s1202_infoperant_remunperant
from emensageriapro.s1210.forms import form_s1210_detpgtofer
from emensageriapro.s1210.forms import form_s1210_detpgtoant
from emensageriapro.esocial.forms import form_s2200_evtadmissao
from emensageriapro.esocial.forms import form_s2206_evtaltcontratual
from emensageriapro.esocial.forms import form_s2210_evtcat
from emensageriapro.esocial.forms import form_s2220_evtmonit
from emensageriapro.esocial.forms import form_s2221_evttoxic
from emensageriapro.esocial.forms import form_s2230_evtafasttemp
from emensageriapro.esocial.forms import form_s2240_evtexprisco
from emensageriapro.esocial.forms import form_s2245_evttreicap
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_remunoutrempr
from emensageriapro.esocial.forms import form_s2300_evttsvinicio
from emensageriapro.esocial.forms import form_s2306_evttsvaltcontr
from emensageriapro.esocial.forms import form_s2399_evttsvtermino
from emensageriapro.s2399.forms import form_s2399_remunoutrempr
from emensageriapro.s5001.forms import form_s5001_infocategincid
from emensageriapro.s5002.forms import form_s5002_infoirrf
from emensageriapro.s5003.forms import form_s5003_infotrabfgts
from emensageriapro.s5003.forms import form_s5003_infotrabdps
from emensageriapro.s5011.forms import form_s5011_basesremun

#IMPORTACOES


@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        esocial_trabalhadores_categorias_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='esocial_trabalhadores_categorias')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    esocial_trabalhadores_categorias = get_object_or_404(eSocialTrabalhadoresCategorias.objects.using( db_slug ), excluido = False, id = esocial_trabalhadores_categorias_id)
    if request.method == 'POST':
        eSocialTrabalhadoresCategorias.objects.using( db_slug ).filter(id = esocial_trabalhadores_categorias_id).update(excluido = True)
        #esocial_trabalhadores_categorias_apagar_custom
        #esocial_trabalhadores_categorias_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'esocial_trabalhadores_categorias_salvar':
            return redirect('esocial_trabalhadores_categorias', hash=request.session['retorno_hash'])
        else:
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
    context = {
        'usuario': usuario,
<<<<<<< HEAD
   
        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,
   
=======
        
        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,
        
>>>>>>> 3217f7abcc9a9c37261d88e43626ba3e9fb91ee3
        'permissao': permissao,
        'data': datetime.datetime.now(),
        'pagina': pagina,
        'dict_permissoes': dict_permissoes,
        'hash': hash,
    }
    return render(request, 'esocial_trabalhadores_categorias_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class eSocialTrabalhadoresCategoriasList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = eSocialTrabalhadoresCategorias.objects.using(db_slug).all()
    serializer_class = eSocialTrabalhadoresCategoriasSerializer
    permission_classes = (IsAdminUser,)


class eSocialTrabalhadoresCategoriasDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = eSocialTrabalhadoresCategorias.objects.using(db_slug).all()
    serializer_class = eSocialTrabalhadoresCategoriasSerializer
    permission_classes = (IsAdminUser,)


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
def json_search(request, search):
    from django.http import JsonResponse
    import operator
    from django.db.models import Count, Q
    import urllib
    db_slug = 'default'
    search = urllib.unquote(search)
    lista = search.split(" ")
    dicionario = {}
    if search.strip():
        try:
            query = reduce(operator.and_, ((Q(titulo__icontains=item) | Q(codigo__icontains=item)) for item in lista))
            lista = eSocialTrabalhadoresCategorias.objects.using(db_slug).filter(excluido = False).filter(query).all()
        except:
            query = reduce(operator.and_, ((Q(descricao__icontains=item) | Q(codigo__icontains=item)) for item in lista))
            lista = eSocialTrabalhadoresCategorias.objects.using(db_slug).filter(excluido = False).filter(query).all()
    else:
        lista = eSocialTrabalhadoresCategorias.objects.using(db_slug).filter(excluido=False).all()
    lista_esocial_trabalhadores_categorias = []
    for a in lista:
        dic = {}
        dic['key'] = a.codigo
        dic['value'] = '%s' % (a)
        lista_esocial_trabalhadores_categorias.append(dic)
    dicionario['esocial_trabalhadores_categorias'] = lista_esocial_trabalhadores_categorias
    return JsonResponse(dicionario)


@login_required
def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #esocial_trabalhadores_categorias_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='esocial_trabalhadores_categorias')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_codigo': 1,
            'show_descricao': 1,
            'show_grupo': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'codigo__icontains': 'codigo__icontains',
                'descricao__icontains': 'descricao__icontains',
                'grupo': 'grupo',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'codigo__icontains': 'codigo__icontains',
                'descricao__icontains': 'descricao__icontains',
                'grupo': 'grupo',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        esocial_trabalhadores_categorias_lista = eSocialTrabalhadoresCategorias.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(esocial_trabalhadores_categorias_lista) > 100:
            filtrar = True
            esocial_trabalhadores_categorias_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
<<<<<<< HEAD

=======
    
>>>>>>> 3217f7abcc9a9c37261d88e43626ba3e9fb91ee3
        #esocial_trabalhadores_categorias_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'esocial_trabalhadores_categorias'
        context = {
            'esocial_trabalhadores_categorias_lista': esocial_trabalhadores_categorias_lista,
<<<<<<< HEAD
       
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
       
=======
            
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
>>>>>>> 3217f7abcc9a9c37261d88e43626ba3e9fb91ee3
            'permissao': permissao,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,
<<<<<<< HEAD
   
=======
        
>>>>>>> 3217f7abcc9a9c37261d88e43626ba3e9fb91ee3
        }
        if for_print in (0,1):
            return render(request, 'esocial_trabalhadores_categorias_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='esocial_trabalhadores_categorias_listar.html',
                filename="esocial_trabalhadores_categorias.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('esocial_trabalhadores_categorias_listar.html', context)
            filename = "esocial_trabalhadores_categorias.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/esocial_trabalhadores_categorias_csv.html', context)
            filename = "esocial_trabalhadores_categorias.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
    else:
        context = {
            'usuario': usuario,
<<<<<<< HEAD
       
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
       
=======
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
>>>>>>> 3217f7abcc9a9c37261d88e43626ba3e9fb91ee3
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)

@login_required
def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        esocial_trabalhadores_categorias_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='esocial_trabalhadores_categorias')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if esocial_trabalhadores_categorias_id:
        esocial_trabalhadores_categorias = get_object_or_404(eSocialTrabalhadoresCategorias.objects.using( db_slug ), excluido = False, id = esocial_trabalhadores_categorias_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if esocial_trabalhadores_categorias_id:
            esocial_trabalhadores_categorias_form = form_esocial_trabalhadores_categorias(request.POST or None, instance = esocial_trabalhadores_categorias, slug = db_slug)
        else:
            esocial_trabalhadores_categorias_form = form_esocial_trabalhadores_categorias(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if esocial_trabalhadores_categorias_form.is_valid():
                dados = esocial_trabalhadores_categorias_form.cleaned_data
                if esocial_trabalhadores_categorias_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #esocial_trabalhadores_categorias_campos_multiple_passo1
                    eSocialTrabalhadoresCategorias.objects.using(db_slug).filter(id=esocial_trabalhadores_categorias_id).update(**dados)
                    obj = eSocialTrabalhadoresCategorias.objects.using(db_slug).get(id=esocial_trabalhadores_categorias_id)
                    #esocial_trabalhadores_categorias_editar_custom
                    #esocial_trabalhadores_categorias_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #esocial_trabalhadores_categorias_cadastrar_campos_multiple_passo1
                    obj = eSocialTrabalhadoresCategorias(**dados)
                    obj.save(using = db_slug)
                    #esocial_trabalhadores_categorias_cadastrar_custom
                    #esocial_trabalhadores_categorias_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('esocial_trabalhadores_categorias_apagar', 'esocial_trabalhadores_categorias_salvar', 'esocial_trabalhadores_categorias'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if esocial_trabalhadores_categorias_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('esocial_trabalhadores_categorias_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        esocial_trabalhadores_categorias_form = disabled_form_fields(esocial_trabalhadores_categorias_form, permissao.permite_editar)
        #esocial_trabalhadores_categorias_campos_multiple_passo3

        for field in esocial_trabalhadores_categorias_form.fields.keys():
            esocial_trabalhadores_categorias_form.fields[field].widget.attrs['ng-model'] = 'esocial_trabalhadores_categorias_'+field
        if int(dict_hash['print']):
            esocial_trabalhadores_categorias_form = disabled_form_for_print(esocial_trabalhadores_categorias_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if esocial_trabalhadores_categorias_id:
            esocial_trabalhadores_categorias = get_object_or_404(eSocialTrabalhadoresCategorias.objects.using( db_slug ), excluido = False, id = esocial_trabalhadores_categorias_id)
            pass
        else:
            esocial_trabalhadores_categorias = None
        #esocial_trabalhadores_categorias_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'esocial_trabalhadores_categorias' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'esocial_trabalhadores_categorias_salvar'
        context = {
            'esocial_trabalhadores_categorias': esocial_trabalhadores_categorias,
            'esocial_trabalhadores_categorias_form': esocial_trabalhadores_categorias_form,
            'mensagem': mensagem,
            'esocial_trabalhadores_categorias_id': int(esocial_trabalhadores_categorias_id),
            'usuario': usuario,
<<<<<<< HEAD
       
=======
            
>>>>>>> 3217f7abcc9a9c37261d88e43626ba3e9fb91ee3
            'hash': hash,
            #[VARIAVEIS_SECUNDARIAS]
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
<<<<<<< HEAD
       
=======
            
>>>>>>> 3217f7abcc9a9c37261d88e43626ba3e9fb91ee3
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #esocial_trabalhadores_categorias_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'esocial_trabalhadores_categorias_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='esocial_trabalhadores_categorias_salvar.html',
                filename="esocial_trabalhadores_categorias.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('esocial_trabalhadores_categorias_salvar.html', context)
            filename = "esocial_trabalhadores_categorias.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

    else:
        context = {
            'usuario': usuario,
<<<<<<< HEAD
       
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
       
=======
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
>>>>>>> 3217f7abcc9a9c37261d88e43626ba3e9fb91ee3
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)

