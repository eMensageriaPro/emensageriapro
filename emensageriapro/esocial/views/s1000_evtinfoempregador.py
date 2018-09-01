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
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import *
import base64
from emensageriapro.s1000.models import s1000inclusao
from emensageriapro.s1000.models import s1000alteracao
from emensageriapro.s1000.models import s1000exclusao
from emensageriapro.s1000.forms import form_s1000_inclusao
from emensageriapro.s1000.forms import form_s1000_alteracao
from emensageriapro.s1000.forms import form_s1000_exclusao

#IMPORTACOES


#view_identidade_evento#
def identidade_evento(s1000_evtinfoempregador_id, db_slug):
    from emensageriapro.mensageiro.models import TransmissorEventosEsocial
    dados_evento = s1000evtInfoEmpregador.objects.using( db_slug ).get(id=s1000_evtinfoempregador_id)
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
        lista_eventos = TransmissorEventosEsocial.objects.using(db_slug).filter(criado_em=dados_evento.criado_em,
                                                                         excluido=False, identidade = identidade_temp).all()
        if not lista_eventos:
            s1000evtInfoEmpregador.objects.using(db_slug).filter(id=s1000_evtinfoempregador_id).update(identidade=identidade_temp)
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
        s1000_evtinfoempregador_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1000_evtinfoempregador')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s1000_evtinfoempregador_id:
        s1000_evtinfoempregador = get_object_or_404(s1000evtInfoEmpregador.objects.using( db_slug ), excluido = False, id = s1000_evtinfoempregador_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if s1000_evtinfoempregador_id:
        if s1000_evtinfoempregador.status != 0:
            dict_permissoes['s1000_evtinfoempregador_apagar'] = 0
            dict_permissoes['s1000_evtinfoempregador_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s1000_evtinfoempregador_id:
            s1000_evtinfoempregador_form = form_s1000_evtinfoempregador(request.POST or None, instance = s1000_evtinfoempregador, slug = db_slug)
        else:
            s1000_evtinfoempregador_form = form_s1000_evtinfoempregador(request.POST or None, slug = db_slug, initial={'versao': VERSAO_MODELO, 'processamento_codigo_resposta': 0, 'tpamb': TP_AMB, 'procemi': 1, 'verproc': VERSAO_EMENSAGERIA})
        if request.method == 'POST':
            if s1000_evtinfoempregador_form.is_valid():
                dados = s1000_evtinfoempregador_form.cleaned_data
                import json
                from django.forms.models import model_to_dict
                if s1000_evtinfoempregador_id:
                    if s1000_evtinfoempregador.status == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #s1000_evtinfoempregador_campos_multiple_passo1
                        s1000evtInfoEmpregador.objects.using(db_slug).filter(id=s1000_evtinfoempregador_id).update(**dados)
                        obj = s1000evtInfoEmpregador.objects.using(db_slug).get(id=s1000_evtinfoempregador_id)
                        #s1000_evtinfoempregador_editar_custom
                        #s1000_evtinfoempregador_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(s1000_evtinfoempregador), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         's1000_evtinfoempregador', s1000_evtinfoempregador_id, usuario_id, 2)
                    else:
                        messages.error(request, 'Não é possível salvar o evento, pois o mesmo não está com o status "Cadastrado"!')

                else:
                    dados['arquivo_original'] = 0

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #s1000_evtinfoempregador_cadastrar_campos_multiple_passo1
                    obj = s1000evtInfoEmpregador(**dados)
                    obj.save(using = db_slug)
                    #s1000_evtinfoempregador_cadastrar_custom
                    #s1000_evtinfoempregador_cadastrar_campos_multiple_passo2
                    identidade_evento(obj.id, db_slug)
                    messages.success(request, 'Cadastrado com sucesso!')
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's1000_evtinfoempregador', obj.id, usuario_id, 1)
                if request.session['retorno_pagina'] not in ('s1000_evtinfoempregador_apagar', 's1000_evtinfoempregador_salvar', 's1000_evtinfoempregador'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s1000_evtinfoempregador_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s1000_evtinfoempregador_salvar', hash=url_hash)

            else:
                messages.error(request, 'Erro ao salvar!')
        s1000_evtinfoempregador_form = disabled_form_fields(s1000_evtinfoempregador_form, permissao.permite_editar)

        if s1000_evtinfoempregador_id:
            if s1000_evtinfoempregador.status != 0:
                s1000_evtinfoempregador_form = disabled_form_fields(s1000_evtinfoempregador_form, False)
        #s1000_evtinfoempregador_campos_multiple_passo3

        for field in s1000_evtinfoempregador_form.fields.keys():
            s1000_evtinfoempregador_form.fields[field].widget.attrs['ng-model'] = 's1000_evtinfoempregador_'+field
        if int(dict_hash['print']):
            s1000_evtinfoempregador_form = disabled_form_for_print(s1000_evtinfoempregador_form)

        s1000_inclusao_form = None
        s1000_inclusao_lista = None
        s1000_alteracao_form = None
        s1000_alteracao_lista = None
        s1000_exclusao_form = None
        s1000_exclusao_lista = None
        if s1000_evtinfoempregador_id:
            s1000_evtinfoempregador = get_object_or_404(s1000evtInfoEmpregador.objects.using( db_slug ), excluido = False, id = s1000_evtinfoempregador_id)

            s1000_inclusao_form = form_s1000_inclusao(initial={ 's1000_evtinfoempregador': s1000_evtinfoempregador }, slug=db_slug)
            s1000_inclusao_form.fields['s1000_evtinfoempregador'].widget.attrs['readonly'] = True
            s1000_inclusao_lista = s1000inclusao.objects.using( db_slug ).filter(excluido = False, s1000_evtinfoempregador_id=s1000_evtinfoempregador.id).all()
            s1000_alteracao_form = form_s1000_alteracao(initial={ 's1000_evtinfoempregador': s1000_evtinfoempregador }, slug=db_slug)
            s1000_alteracao_form.fields['s1000_evtinfoempregador'].widget.attrs['readonly'] = True
            s1000_alteracao_lista = s1000alteracao.objects.using( db_slug ).filter(excluido = False, s1000_evtinfoempregador_id=s1000_evtinfoempregador.id).all()
            s1000_exclusao_form = form_s1000_exclusao(initial={ 's1000_evtinfoempregador': s1000_evtinfoempregador }, slug=db_slug)
            s1000_exclusao_form.fields['s1000_evtinfoempregador'].widget.attrs['readonly'] = True
            s1000_exclusao_lista = s1000exclusao.objects.using( db_slug ).filter(excluido = False, s1000_evtinfoempregador_id=s1000_evtinfoempregador.id).all()
        else:
            s1000_evtinfoempregador = None
        #s1000_evtinfoempregador_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if 's1000_evtinfoempregador'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False
        if not evento_totalizador:
            s1000_evtinfoempregador_form.fields['tpamb'].widget.attrs['disabled'] = True
            s1000_evtinfoempregador_form.fields['tpamb'].widget.attrs['readonly'] = True
            s1000_evtinfoempregador_form.fields['tpamb'].value = TP_AMB
            s1000_evtinfoempregador_form.fields['procemi'].widget.attrs['disabled'] = True
            s1000_evtinfoempregador_form.fields['procemi'].widget.attrs['readonly'] = True
            s1000_evtinfoempregador_form.fields['procemi'].value = 1
            s1000_evtinfoempregador_form.fields['verproc'].widget.attrs['readonly'] = True
            s1000_evtinfoempregador_form.fields['verproc'].value = VERSAO_EMENSAGERIA

        if dict_hash['tab'] or 's1000_evtinfoempregador' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's1000_evtinfoempregador_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s1000_evtinfoempregador_id, tabela='s1000_evtinfoempregador').all()
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            's1000_evtinfoempregador': s1000_evtinfoempregador,
            's1000_evtinfoempregador_form': s1000_evtinfoempregador_form,
            'mensagem': mensagem,
            's1000_evtinfoempregador_id': int(s1000_evtinfoempregador_id),
            'usuario': usuario,

            'hash': hash,

            's1000_inclusao_form': s1000_inclusao_form,
            's1000_inclusao_lista': s1000_inclusao_lista,
            's1000_alteracao_form': s1000_alteracao_form,
            's1000_alteracao_lista': s1000_alteracao_lista,
            's1000_exclusao_form': s1000_exclusao_form,
            's1000_exclusao_lista': s1000_exclusao_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s1000_evtinfoempregador_salvar_custom_variaveis_context#
        }
        return render(request, 's1000_evtinfoempregador_salvar.html', context)
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
        s1000_evtinfoempregador_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1000_evtinfoempregador')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    s1000_evtinfoempregador = get_object_or_404(s1000evtInfoEmpregador.objects.using( db_slug ), excluido = False, id = s1000_evtinfoempregador_id)

    if s1000_evtinfoempregador_id:
        if s1000_evtinfoempregador.status != 0:
            dict_permissoes['s1000_evtinfoempregador_apagar'] = 0
            dict_permissoes['s1000_evtinfoempregador_editar'] = 0

    if request.method == 'POST':
        if s1000_evtinfoempregador.status == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s1000_evtinfoempregador), indent=4, sort_keys=True, default=str)
            s1000evtInfoEmpregador.objects.using( db_slug ).filter(id = s1000_evtinfoempregador_id).delete()
            #s1000_evtinfoempregador_apagar_custom
            #s1000_evtinfoempregador_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's1000_evtinfoempregador', s1000_evtinfoempregador_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 's1000_evtinfoempregador_salvar':
            return redirect('s1000_evtinfoempregador', hash=request.session['retorno_hash'])
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
    return render(request, 's1000_evtinfoempregador_apagar.html', context)

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
        #s1000_evtinfoempregador_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1000_evtinfoempregador')
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
            'show_infoempregador': 0,
            'show_nrinsc': 1,
            'show_tpinsc': 1,
            'show_ideempregador': 0,
            'show_verproc': 0,
            'show_procemi': 0,
            'show_tpamb': 0,
            'show_ideevento': 0,
            'show_identidade': 1,
            'show_evtinfoempregador': 0,
            'show_operacao': 1,
            'show_recibo_hash': 0,
            'show_recibo_numero': 0,
            'show_processamento_data_hora': 0,
            'show_processamento_versao_app_processamento': 0,
            'show_processamento_descricao_resposta': 0,
            'show_processamento_codigo_resposta': 1,
            'show_recepcao_protocolo_envio_lote': 0,
            'show_recepcao_versao_app': 0,
            'show_recepcao_data_hora': 0,
            'show_recepcao_tp_amb': 0,
            'show_status': 1,
            'show_versao': 0,
            'show_transmissor_lote_esocial': 0,
            'show_arquivo': 0,
            'show_arquivo_original': 0,
            'show_validacoes': 0,
            'show_validacao_precedencia': 0,
            'show_ocorrencias': 0,
            'show_retornos_eventos': 0, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'infoempregador': 'infoempregador',
                'nrinsc__icontains': 'nrinsc__icontains',
                'tpinsc': 'tpinsc',
                'ideempregador': 'ideempregador',
                'verproc__icontains': 'verproc__icontains',
                'procemi': 'procemi',
                'tpamb': 'tpamb',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'evtinfoempregador': 'evtinfoempregador',
                'operacao': 'operacao',
                'status': 'status',
                'versao__icontains': 'versao__icontains',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'infoempregador': 'infoempregador',
                'nrinsc__icontains': 'nrinsc__icontains',
                'tpinsc': 'tpinsc',
                'ideempregador': 'ideempregador',
                'verproc__icontains': 'verproc__icontains',
                'procemi': 'procemi',
                'tpamb': 'tpamb',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'evtinfoempregador': 'evtinfoempregador',
                'operacao': 'operacao',
                'status': 'status',
                'versao__icontains': 'versao__icontains',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s1000_evtinfoempregador_lista = s1000evtInfoEmpregador.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s1000_evtinfoempregador_lista) > 100:
            filtrar = True
            s1000_evtinfoempregador_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lote_esocial_lista = TransmissorLoteEsocial.objects.using( db_slug ).filter(excluido = False).all()
        #s1000_evtinfoempregador_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's1000_evtinfoempregador'
        context = {
            's1000_evtinfoempregador_lista': s1000_evtinfoempregador_lista,

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

            'transmissor_lote_esocial_lista': transmissor_lote_esocial_lista,
        }
        #return render(request, 's1000_evtinfoempregador_listar.html', context)
        if for_print in (0,1):
            return render(request, 's1000_evtinfoempregador_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s1000_evtinfoempregador_listar.html',
                filename="s1000_evtinfoempregador.pdf",
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
            response = render_to_response('s1000_evtinfoempregador_listar.html', context)
            filename = "s1000_evtinfoempregador.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/s1000_evtinfoempregador_csv.html', context)
            filename = "s1000_evtinfoempregador.csv"
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

