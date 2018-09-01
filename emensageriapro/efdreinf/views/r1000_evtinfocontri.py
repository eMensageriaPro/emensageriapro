#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"



import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import *
import base64
from emensageriapro.r1000.models import r1000inclusao
from emensageriapro.r1000.models import r1000alteracao
from emensageriapro.r1000.models import r1000exclusao
from emensageriapro.r1000.forms import form_r1000_inclusao
from emensageriapro.r1000.forms import form_r1000_alteracao
from emensageriapro.r1000.forms import form_r1000_exclusao

#IMPORTACOES


#view_identidade_evento#
def identidade_evento(r1000_evtinfocontri_id, db_slug):
    from emensageriapro.mensageiro.models import TransmissorEventosEfdreinf
    dados_evento = r1000evtInfoContri.objects.using( db_slug ).get(id=r1000_evtinfocontri_id)
    identidade = 'ID'
    identidade += str(dados_evento.tpinsc)
    nr_insc = dados_evento.nrinsc
    while len(nr_insc) != 14:
        nr_insc = nr_insc+'0'
    identidade += nr_insc
    identidade += str(dados_evento.criado_em.year)
    mes = str(dados_evento.criado_em.month)
    if len(mes) == 1: mes = '0'+mes
    identidade += mes
    dia = str(dados_evento.criado_em.day)
    if len(dia) == 1: dia = '0'+dia
    identidade += dia
    hora = str(dados_evento.criado_em.hour)
    if len(hora) == 1: hora = '0'+hora
    identidade += hora
    minuto = str(dados_evento.criado_em.minute)
    if len(minuto) == 1: minuto = '0'+minuto
    identidade += minuto
    segundo = str(dados_evento.criado_em.second)
    if len(segundo) == 1: segundo = '0'+segundo
    identidade += segundo
    existe = True
    n = 0
    while existe:
        n+=1
        sequencial = str(n)
        while len(sequencial) != 5:
            sequencial = '0'+sequencial
        identidade_temp = identidade + sequencial
        lista_eventos = TransmissorEventosEfdreinf.objects.using(db_slug).filter(criado_em=dados_evento.criado_em,
                                                                         excluido=False, identidade = identidade_temp).all()
        if not lista_eventos:
            r1000evtInfoContri.objects.using(db_slug).filter(id=r1000_evtinfocontri_id).update(identidade=identidade_temp)
            existe = False
    return identidade_temp
#view_identidade_evento#



def gerar_identidade(request, chave, evento_id):
    from emensageriapro.settings import PASS_SCRIPT
    if chave == PASS_SCRIPT:
        db_slug = 'default'
        ident = identidade_evento(evento_id, db_slug)
        mensagem = ident
    else:
        mensagem = 'Chave incorreta!'
    return HttpResponse(mensagem)


def salvar(request, hash):
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_MODELO, TP_AMB
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        r1000_evtinfocontri_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r1000_evtinfocontri')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if r1000_evtinfocontri_id:
        r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri.objects.using( db_slug ), excluido = False, id = r1000_evtinfocontri_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if r1000_evtinfocontri_id:
        if r1000_evtinfocontri.status != 0:
            dict_permissoes['r1000_evtinfocontri_apagar'] = 0
            dict_permissoes['r1000_evtinfocontri_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if r1000_evtinfocontri_id:
            r1000_evtinfocontri_form = form_r1000_evtinfocontri(request.POST or None, instance = r1000_evtinfocontri, slug = db_slug)
        else:
            r1000_evtinfocontri_form = form_r1000_evtinfocontri(request.POST or None, slug = db_slug, initial={'versao': VERSAO_MODELO, 'processamento_codigo_resposta': 0, 'tpamb': TP_AMB, 'procemi': 1, 'verproc': VERSAO_EMENSAGERIA})
        if request.method == 'POST':
            if r1000_evtinfocontri_form.is_valid():
                dados = r1000_evtinfocontri_form.cleaned_data
                import json
                from django.forms.models import model_to_dict
                if r1000_evtinfocontri_id:
                    if r1000_evtinfocontri.status == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #r1000_evtinfocontri_campos_multiple_passo1
                        r1000evtInfoContri.objects.using(db_slug).filter(id=r1000_evtinfocontri_id).update(**dados)
                        obj = r1000evtInfoContri.objects.using(db_slug).get(id=r1000_evtinfocontri_id)
                        #r1000_evtinfocontri_editar_custom
                        #r1000_evtinfocontri_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(r1000_evtinfocontri), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         'r1000_evtinfocontri', r1000_evtinfocontri_id, usuario_id, 2)
                    else:
                        messages.error(request, 'Não é possível salvar o evento, pois o mesmo não está com o status "Cadastrado"!')

                else:
                    dados['arquivo_original'] = 0

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #r1000_evtinfocontri_cadastrar_campos_multiple_passo1
                    obj = r1000evtInfoContri(**dados)
                    obj.save(using = db_slug)
                    #r1000_evtinfocontri_cadastrar_custom
                    #r1000_evtinfocontri_cadastrar_campos_multiple_passo2
                    identidade_evento(obj.id, db_slug)
                    messages.success(request, 'Cadastrado com sucesso!')
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     'r1000_evtinfocontri', obj.id, usuario_id, 1)
                if request.session['retorno_pagina'] not in ('r1000_evtinfocontri_apagar', 'r1000_evtinfocontri_salvar', 'r1000_evtinfocontri'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if r1000_evtinfocontri_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('r1000_evtinfocontri_salvar', hash=url_hash)

            else:
                messages.error(request, 'Erro ao salvar!')
        r1000_evtinfocontri_form = disabled_form_fields(r1000_evtinfocontri_form, permissao.permite_editar)

        if r1000_evtinfocontri_id:
            if r1000_evtinfocontri.status != 0:
                r1000_evtinfocontri_form = disabled_form_fields(r1000_evtinfocontri_form, False)
        #r1000_evtinfocontri_campos_multiple_passo3

        for field in r1000_evtinfocontri_form.fields.keys():
            r1000_evtinfocontri_form.fields[field].widget.attrs['ng-model'] = 'r1000_evtinfocontri_'+field
        if int(dict_hash['print']):
            r1000_evtinfocontri_form = disabled_form_for_print(r1000_evtinfocontri_form)

        r1000_inclusao_form = None
        r1000_inclusao_lista = None
        r1000_alteracao_form = None
        r1000_alteracao_lista = None
        r1000_exclusao_form = None
        r1000_exclusao_lista = None
        if r1000_evtinfocontri_id:
            r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri.objects.using( db_slug ), excluido = False, id = r1000_evtinfocontri_id)

            r1000_inclusao_form = form_r1000_inclusao(initial={ 'r1000_evtinfocontri': r1000_evtinfocontri }, slug=db_slug)
            r1000_inclusao_form.fields['r1000_evtinfocontri'].widget.attrs['readonly'] = True
            r1000_inclusao_lista = r1000inclusao.objects.using( db_slug ).filter(excluido = False, r1000_evtinfocontri_id=r1000_evtinfocontri.id).all()
            r1000_alteracao_form = form_r1000_alteracao(initial={ 'r1000_evtinfocontri': r1000_evtinfocontri }, slug=db_slug)
            r1000_alteracao_form.fields['r1000_evtinfocontri'].widget.attrs['readonly'] = True
            r1000_alteracao_lista = r1000alteracao.objects.using( db_slug ).filter(excluido = False, r1000_evtinfocontri_id=r1000_evtinfocontri.id).all()
            r1000_exclusao_form = form_r1000_exclusao(initial={ 'r1000_evtinfocontri': r1000_evtinfocontri }, slug=db_slug)
            r1000_exclusao_form.fields['r1000_evtinfocontri'].widget.attrs['readonly'] = True
            r1000_exclusao_lista = r1000exclusao.objects.using( db_slug ).filter(excluido = False, r1000_evtinfocontri_id=r1000_evtinfocontri.id).all()
        else:
            r1000_evtinfocontri = None
        #r1000_evtinfocontri_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if 'r1000_evtinfocontri'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False
        if not evento_totalizador:
            r1000_evtinfocontri_form.fields['tpamb'].widget.attrs['disabled'] = True
            r1000_evtinfocontri_form.fields['tpamb'].widget.attrs['readonly'] = True
            r1000_evtinfocontri_form.fields['tpamb'].value = TP_AMB
            r1000_evtinfocontri_form.fields['procemi'].widget.attrs['disabled'] = True
            r1000_evtinfocontri_form.fields['procemi'].widget.attrs['readonly'] = True
            r1000_evtinfocontri_form.fields['procemi'].value = 1
            r1000_evtinfocontri_form.fields['verproc'].widget.attrs['readonly'] = True
            r1000_evtinfocontri_form.fields['verproc'].value = VERSAO_EMENSAGERIA

        if dict_hash['tab'] or 'r1000_evtinfocontri' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r1000_evtinfocontri_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=r1000_evtinfocontri_id, tabela='r1000_evtinfocontri').all()
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            'r1000_evtinfocontri': r1000_evtinfocontri,
            'r1000_evtinfocontri_form': r1000_evtinfocontri_form,
            'mensagem': mensagem,
            'r1000_evtinfocontri_id': int(r1000_evtinfocontri_id),
            'usuario': usuario,

            'hash': hash,

            'r1000_inclusao_form': r1000_inclusao_form,
            'r1000_inclusao_lista': r1000_inclusao_lista,
            'r1000_alteracao_form': r1000_alteracao_form,
            'r1000_alteracao_lista': r1000_alteracao_lista,
            'r1000_exclusao_form': r1000_exclusao_form,
            'r1000_exclusao_lista': r1000_exclusao_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r1000_evtinfocontri_salvar_custom_variaveis_context#
        }
        return render(request, 'r1000_evtinfocontri_salvar.html', context)
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

def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
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
    r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri.objects.using( db_slug ), excluido = False, id = r1000_evtinfocontri_id)

    if r1000_evtinfocontri_id:
        if r1000_evtinfocontri.status != 0:
            dict_permissoes['r1000_evtinfocontri_apagar'] = 0
            dict_permissoes['r1000_evtinfocontri_editar'] = 0

    if request.method == 'POST':
        if r1000_evtinfocontri.status == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(r1000_evtinfocontri), indent=4, sort_keys=True, default=str)
            r1000evtInfoContri.objects.using( db_slug ).filter(id = r1000_evtinfocontri_id).delete()
            #r1000_evtinfocontri_apagar_custom
            #r1000_evtinfocontri_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             'r1000_evtinfocontri', r1000_evtinfocontri_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 'r1000_evtinfocontri_salvar':
            return redirect('r1000_evtinfocontri', hash=request.session['retorno_hash'])
        else:
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
    context = {
        'usuario': usuario,

        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,

        'permissao': permissao,
        'data': datetime.datetime.now(),
        'pagina': pagina,
        'dict_permissoes': dict_permissoes,
        'hash': hash,
    }
    return render(request, 'r1000_evtinfocontri_apagar.html', context)

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

def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #r1000_evtinfocontri_id = int(dict_hash['id'])
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
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_excluido': 0,
            'show_modificado_por': 0,
            'show_modificado_em': 0,
            'show_criado_por': 0,
            'show_criado_em': 0,
            'show_infocontri': 0,
            'show_nrinsc': 0,
            'show_tpinsc': 0,
            'show_idecontri': 0,
            'show_verproc': 0,
            'show_procemi': 0,
            'show_tpamb': 0,
            'show_ideevento': 0,
            'show_identidade': 1,
            'show_evtinfocontri': 0,
            'show_dhprocess': 0,
            'show_descretorno': 0,
            'show_cdretorno': 1,
            'show_operacao': 1,
            'show_status': 1,
            'show_versao': 0,
            'show_transmissor_lote_efdreinf': 0,
            'show_arquivo': 0,
            'show_arquivo_original': 0,
            'show_validacoes': 0,
            'show_validacao_precedencia': 0,
            'show_ocorrencias': 0,
            'show_retornos_evttotalcontrib': 0,
            'show_retornos_evttotal': 0, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'infocontri': 'infocontri',
                'nrinsc__icontains': 'nrinsc__icontains',
                'tpinsc': 'tpinsc',
                'idecontri': 'idecontri',
                'verproc__icontains': 'verproc__icontains',
                'procemi': 'procemi',
                'tpamb': 'tpamb',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'evtinfocontri': 'evtinfocontri',
                'operacao': 'operacao',
                'status': 'status',
                'versao__icontains': 'versao__icontains',
                'transmissor_lote_efdreinf': 'transmissor_lote_efdreinf',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'infocontri': 'infocontri',
                'nrinsc__icontains': 'nrinsc__icontains',
                'tpinsc': 'tpinsc',
                'idecontri': 'idecontri',
                'verproc__icontains': 'verproc__icontains',
                'procemi': 'procemi',
                'tpamb': 'tpamb',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'evtinfocontri': 'evtinfocontri',
                'operacao': 'operacao',
                'status': 'status',
                'versao__icontains': 'versao__icontains',
                'transmissor_lote_efdreinf': 'transmissor_lote_efdreinf',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        r1000_evtinfocontri_lista = r1000evtInfoContri.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(r1000_evtinfocontri_lista) > 100:
            filtrar = True
            r1000_evtinfocontri_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lote_efdreinf_lista = TransmissorLoteEfdreinf.objects.using( db_slug ).filter(excluido = False).all()
        #r1000_evtinfocontri_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r1000_evtinfocontri'
        context = {
            'r1000_evtinfocontri_lista': r1000_evtinfocontri_lista,

            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,

            'transmissor_lote_efdreinf_lista': transmissor_lote_efdreinf_lista,
        }
        #return render(request, 'r1000_evtinfocontri_listar.html', context)
        if for_print in (0,1):
            return render(request, 'r1000_evtinfocontri_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r1000_evtinfocontri_listar.html',
                filename="r1000_evtinfocontri.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             'viewport-size': "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('r1000_evtinfocontri_listar.html', context)
            filename = "r1000_evtinfocontri.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/r1000_evtinfocontri_csv.html', context)
            filename = "r1000_evtinfocontri.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
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

