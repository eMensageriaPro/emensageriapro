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
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


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




def s5001_evtbasestrab(request, hash):
    from emensageriapro.esocial.models import s5001evtBasesTrab
    from emensageriapro.s5001.models import *
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url(hash)
        s5001_evtbasestrab_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using(db_slug), excluido=False, id=usuario_id)
    pagina = ConfigPaginas.objects.using(db_slug).get(excluido=False, endereco='s5001_evtbasestrab')
    permissao = ConfigPermissoes.objects.using(db_slug).get(excluido=False, config_paginas=pagina,
                                                            config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s5001_evtbasestrab = get_object_or_404(s5001evtBasesTrab.objects.using(db_slug), excluido=False,
                                               id=s5001_evtbasestrab_id)
        s5001_evtbasestrab_lista = s5001evtBasesTrab.objects.using(db_slug).filter(id=s5001_evtbasestrab_id,
                                                                                   excluido=False).all()

        s5001_procjudtrab_lista = s5001procJudTrab.objects.using(db_slug).filter(
            s5001_evtbasestrab_id__in=listar_ids(s5001_evtbasestrab_lista)).filter(excluido=False).all()
        s5001_infocpcalc_lista = s5001infoCpCalc.objects.using(db_slug).filter(
            s5001_evtbasestrab_id__in=listar_ids(s5001_evtbasestrab_lista)).filter(excluido=False).all()
        s5001_infocp_lista = s5001infoCp.objects.using(db_slug).filter(
            s5001_evtbasestrab_id__in=listar_ids(s5001_evtbasestrab_lista)).filter(excluido=False).all()
        s5001_ideestablot_lista = s5001ideEstabLot.objects.using(db_slug).filter(
            s5001_infocp_id__in=listar_ids(s5001_infocp_lista)).filter(excluido=False).all()
        s5001_infocategincid_lista = s5001infoCategIncid.objects.using(db_slug).filter(
            s5001_ideestablot_id__in=listar_ids(s5001_ideestablot_lista)).filter(excluido=False).all()
        s5001_infobasecs_lista = s5001infoBaseCS.objects.using(db_slug).filter(
            s5001_infocategincid_id__in=listar_ids(s5001_infocategincid_lista)).filter(excluido=False).all()
        s5001_calcterc_lista = s5001calcTerc.objects.using(db_slug).filter(
            s5001_infocategincid_id__in=listar_ids(s5001_infocategincid_lista)).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's5001_evtbasestrab'
        context = {
            's5001_evtbasestrab_lista': s5001_evtbasestrab_lista,
            's5001_evtbasestrab_id': s5001_evtbasestrab_id,
            's5001_evtbasestrab': s5001_evtbasestrab,

            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,

            's5001_procjudtrab_lista': s5001_procjudtrab_lista,
            's5001_infocpcalc_lista': s5001_infocpcalc_lista,
            's5001_infocp_lista': s5001_infocp_lista,
            's5001_ideestablot_lista': s5001_ideestablot_lista,
            's5001_infocategincid_lista': s5001_infocategincid_lista,
            's5001_infobasecs_lista': s5001_infobasecs_lista,
            's5001_calcterc_lista': s5001_calcterc_lista,
        }
        #if for_print == 2:
        if for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            #import pdfkit
            #from django.template import loader
            #html = loader.render_to_string('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            response = PDFTemplateResponse(request=request,
                                           template='totalizadores/s5001_evtbasestrab.html',
                                           filename="s1000_evtinfoempregador.pdf",
                                           context=context,
                                           show_content_in_browser=True,
                                           cmd_options={'margin-top': 10,
                                                        'margin-bottom': 10,
                                                        'margin-right': 10,
                                                        'margin-left': 10,
                                                        "zoom": 1,
                                                        "viewport-size": "1366 x 513",
                                                        'javascript-delay': 1000,
                                                        'footer-center': '[page]/[topage]',
                                                        "no-stop-slow-scripts": True},
                                           )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('totalizadores/s5001_evtbasestrab.html', context)
            filename = "%s.xls" % s5001_evtbasestrab.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('totalizadores/s5001_evtbasestrab.html', context)
            filename = "%s.csv" % s5001_evtbasestrab.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        else:
            return render(request, 'totalizadores/s5001_evtbasestrab.html', context)
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


def s5002_evtirrfbenef(request, hash):
    from emensageriapro.esocial.models import s5002evtIrrfBenef
    from emensageriapro.s5002.models import *
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url(hash)
        s5002_evtirrfbenef_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using(db_slug), excluido=False, id=usuario_id)
    pagina = ConfigPaginas.objects.using(db_slug).get(excluido=False, endereco='s5002_evtirrfbenef')
    permissao = ConfigPermissoes.objects.using(db_slug).get(excluido=False, config_paginas=pagina,
                                                            config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s5002_evtirrfbenef = get_object_or_404(s5002evtIrrfBenef.objects.using(db_slug), excluido=False,
                                               id=s5002_evtirrfbenef_id)
        s5002_evtirrfbenef_lista = s5002evtIrrfBenef.objects.using(db_slug).filter(id=s5002_evtirrfbenef_id,
                                                                                   excluido=False).all()

        s5002_infodep_lista = s5002infoDep.objects.using(db_slug).filter(
            s5002_evtirrfbenef_id__in=listar_ids(s5002_evtirrfbenef_lista)).filter(excluido=False).all()
        s5002_infoirrf_lista = s5002infoIrrf.objects.using(db_slug).filter(
            s5002_evtirrfbenef_id__in=listar_ids(s5002_evtirrfbenef_lista)).filter(excluido=False).all()
        s5002_basesirrf_lista = s5002basesIrrf.objects.using(db_slug).filter(
            s5002_infoirrf_id__in=listar_ids(s5002_infoirrf_lista)).filter(excluido=False).all()
        s5002_irrf_lista = s5002irrf.objects.using(db_slug).filter(
            s5002_infoirrf_id__in=listar_ids(s5002_infoirrf_lista)).filter(excluido=False).all()
        s5002_idepgtoext_lista = s5002idePgtoExt.objects.using(db_slug).filter(
            s5002_infoirrf_id__in=listar_ids(s5002_infoirrf_lista)).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's5002_evtirrfbenef'
        context = {
            's5002_evtirrfbenef_lista': s5002_evtirrfbenef_lista,
            's5002_evtirrfbenef_id': s5002_evtirrfbenef_id,
            's5002_evtirrfbenef': s5002_evtirrfbenef,

            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,

            's5002_infodep_lista': s5002_infodep_lista,
            's5002_infoirrf_lista': s5002_infoirrf_lista,
            's5002_basesirrf_lista': s5002_basesirrf_lista,
            's5002_irrf_lista': s5002_irrf_lista,
            's5002_idepgtoext_lista': s5002_idepgtoext_lista,
        }
        if for_print == 2:
            return render_to_pdf('totalizadores/s5002_evtirrfbenef.html', context)
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('totalizadores/s5002_evtirrfbenef.html', context)
            filename = "%s.xls" % s5002_evtirrfbenef.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('totalizadores/s5002_evtirrfbenef.html', context)
            filename = "%s.csv" % s5002_evtirrfbenef.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        else:
            return render(request, 'totalizadores/s5002_evtirrfbenef.html', context)
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


def s5011_evtcs(request, hash):
    from emensageriapro.esocial.models import s5011evtCS
    from emensageriapro.s5011.models import *
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url(hash)
        s5011_evtcs_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using(db_slug), excluido=False, id=usuario_id)
    pagina = ConfigPaginas.objects.using(db_slug).get(excluido=False, endereco='s5011_evtcs')
    permissao = ConfigPermissoes.objects.using(db_slug).get(excluido=False, config_paginas=pagina,
                                                            config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s5011_evtcs = get_object_or_404(s5011evtCS.objects.using(db_slug), excluido=False, id=s5011_evtcs_id)
        s5011_evtcs_lista = s5011evtCS.objects.using(db_slug).filter(id=s5011_evtcs_id, excluido=False).all()

        s5011_infocpseg_lista = s5011infoCPSeg.objects.using(db_slug).filter(
            s5011_evtcs_id__in=listar_ids(s5011_evtcs_lista)).filter(excluido=False).all()
        s5011_infopj_lista = s5011infoPJ.objects.using(db_slug).filter(
            s5011_evtcs_id__in=listar_ids(s5011_evtcs_lista)).filter(excluido=False).all()
        s5011_infoatconc_lista = s5011infoAtConc.objects.using(db_slug).filter(
            s5011_infopj_id__in=listar_ids(s5011_infopj_lista)).filter(excluido=False).all()
        s5011_ideestab_lista = s5011ideEstab.objects.using(db_slug).filter(
            s5011_evtcs_id__in=listar_ids(s5011_evtcs_lista)).filter(excluido=False).all()
        s5011_infoestab_lista = s5011infoEstab.objects.using(db_slug).filter(
            s5011_ideestab_id__in=listar_ids(s5011_ideestab_lista)).filter(excluido=False).all()
        s5011_infocomplobra_lista = s5011infoComplObra.objects.using(db_slug).filter(
            s5011_infoestab_id__in=listar_ids(s5011_infoestab_lista)).filter(excluido=False).all()
        s5011_idelotacao_lista = s5011ideLotacao.objects.using(db_slug).filter(
            s5011_ideestab_id__in=listar_ids(s5011_ideestab_lista)).filter(excluido=False).all()
        s5011_infotercsusp_lista = s5011infoTercSusp.objects.using(db_slug).filter(
            s5011_idelotacao_id__in=listar_ids(s5011_idelotacao_lista)).filter(excluido=False).all()
        s5011_infoemprparcial_lista = s5011infoEmprParcial.objects.using(db_slug).filter(
            s5011_idelotacao_id__in=listar_ids(s5011_idelotacao_lista)).filter(excluido=False).all()
        s5011_dadosopport_lista = s5011dadosOpPort.objects.using(db_slug).filter(
            s5011_idelotacao_id__in=listar_ids(s5011_idelotacao_lista)).filter(excluido=False).all()
        s5011_basesremun_lista = s5011basesRemun.objects.using(db_slug).filter(
            s5011_idelotacao_id__in=listar_ids(s5011_idelotacao_lista)).filter(excluido=False).all()
        s5011_basesavnport_lista = s5011basesAvNPort.objects.using(db_slug).filter(
            s5011_idelotacao_id__in=listar_ids(s5011_idelotacao_lista)).filter(excluido=False).all()
        s5011_infosubstpatropport_lista = s5011infoSubstPatrOpPort.objects.using(db_slug).filter(
            s5011_idelotacao_id__in=listar_ids(s5011_idelotacao_lista)).filter(excluido=False).all()
        s5011_basesaquis_lista = s5011basesAquis.objects.using(db_slug).filter(
            s5011_ideestab_id__in=listar_ids(s5011_ideestab_lista)).filter(excluido=False).all()
        s5011_basescomerc_lista = s5011basesComerc.objects.using(db_slug).filter(
            s5011_ideestab_id__in=listar_ids(s5011_ideestab_lista)).filter(excluido=False).all()
        s5011_infocrestab_lista = s5011infoCREstab.objects.using(db_slug).filter(
            s5011_ideestab_id__in=listar_ids(s5011_ideestab_lista)).filter(excluido=False).all()
        s5011_infocrcontrib_lista = s5011infoCRContrib.objects.using(db_slug).filter(
            s5011_evtcs_id__in=listar_ids(s5011_evtcs_lista)).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's5011_evtcs'
        context = {
            's5011_evtcs_lista': s5011_evtcs_lista,
            's5011_evtcs_id': s5011_evtcs_id,
            's5011_evtcs': s5011_evtcs,

            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,

            's5011_infocpseg_lista': s5011_infocpseg_lista,
            's5011_infopj_lista': s5011_infopj_lista,
            's5011_infoatconc_lista': s5011_infoatconc_lista,
            's5011_ideestab_lista': s5011_ideestab_lista,
            's5011_infoestab_lista': s5011_infoestab_lista,
            's5011_infocomplobra_lista': s5011_infocomplobra_lista,
            's5011_idelotacao_lista': s5011_idelotacao_lista,
            's5011_infotercsusp_lista': s5011_infotercsusp_lista,
            's5011_infoemprparcial_lista': s5011_infoemprparcial_lista,
            's5011_dadosopport_lista': s5011_dadosopport_lista,
            's5011_basesremun_lista': s5011_basesremun_lista,
            's5011_basesavnport_lista': s5011_basesavnport_lista,
            's5011_infosubstpatropport_lista': s5011_infosubstpatropport_lista,
            's5011_basesaquis_lista': s5011_basesaquis_lista,
            's5011_basescomerc_lista': s5011_basescomerc_lista,
            's5011_infocrestab_lista': s5011_infocrestab_lista,
            's5011_infocrcontrib_lista': s5011_infocrcontrib_lista,
        }
        if for_print == 2:
            return render_to_pdf('totalizadores/s5011_evtcs.html', context)
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('totalizadores/s5011_evtcs.html', context)
            filename = "%s.xls" % s5011_evtcs.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('totalizadores/s5011_evtcs.html', context)
            filename = "%s.csv" % s5011_evtcs.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        else:
            return render(request, 'totalizadores/s5011_evtcs.html' % s5011_evtcs.versao, context)
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


def s5012_evtirrf(request, hash):
    from emensageriapro.esocial.models import s5012evtIrrf
    from emensageriapro.s5012.models import *
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url(hash)
        s5012_evtirrf_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using(db_slug), excluido=False, id=usuario_id)
    pagina = ConfigPaginas.objects.using(db_slug).get(excluido=False, endereco='s5012_evtirrf')
    permissao = ConfigPermissoes.objects.using(db_slug).get(excluido=False, config_paginas=pagina,
                                                            config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s5012_evtirrf = get_object_or_404(s5012evtIrrf.objects.using(db_slug), excluido=False, id=s5012_evtirrf_id)
        s5012_evtirrf_lista = s5012evtIrrf.objects.using(db_slug).filter(id=s5012_evtirrf_id, excluido=False).all()

        s5012_infocrcontrib_lista = s5012infoCRContrib.objects.using(db_slug).filter(
            s5012_evtirrf_id__in=listar_ids(s5012_evtirrf_lista)).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's5012_evtirrf'
        context = {
            's5012_evtirrf_lista': s5012_evtirrf_lista,
            's5012_evtirrf_id': s5012_evtirrf_id,
            's5012_evtirrf': s5012_evtirrf,

            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,

            's5012_infocrcontrib_lista': s5012_infocrcontrib_lista,
        }
        if for_print == 2:
            return render_to_pdf('totalizadores/s5012_evtirrf.html', context)
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('totalizadores/s5012_evtirrf.html', context)
            filename = "%s.xls" % s5012_evtirrf.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('totalizadores/s5012_evtirrf.html', context)
            filename = "%s.csv" % s5012_evtirrf.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        else:
            return render(request, 'totalizadores/s5012_evtirrf.html' % s5012_evtirrf.versao, context)
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


def r5001_evttotal(request, hash):
    from emensageriapro.efdreinf.models import r5001evtTotal
    from emensageriapro.r5001.models import *
    for_print = 0
    if slug:
        conta = get_json(slug)
        if not conta:
            raise Http404
        else:
            db_slug = 'emensageriapro' + str(conta.id)
    else:
        db_slug = 'default'
        conta = None
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url(hash)
        r5001_evttotal_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using(db_slug), excluido=False, id=usuario_id)
    pagina = ConfigPaginas.objects.using(db_slug).get(excluido=False, endereco='r5001_evttotal')
    permissao = ConfigPermissoes.objects.using(db_slug).get(excluido=False, config_paginas=pagina,
                                                            config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        r5001_evttotal = get_object_or_404(r5001evtTotal.objects.using(db_slug), excluido=False, id=r5001_evttotal_id)
        r5001_evttotal_lista = r5001evtTotal.objects.using(db_slug).filter(id=r5001_evttotal_id, excluido=False).all()

        r5001_regocorrs_lista = r5001regOcorrs.objects.using(db_slug).filter(
            r5001_evttotal_id__in=listar_ids(r5001_evttotal_lista)).filter(excluido=False).all()
        r5001_infototal_lista = r5001infoTotal.objects.using(db_slug).filter(
            r5001_evttotal_id__in=listar_ids(r5001_evttotal_lista)).filter(excluido=False).all()
        r5001_rtom_lista = r5001RTom.objects.using(db_slug).filter(
            r5001_infototal_id__in=listar_ids(r5001_infototal_lista)).filter(excluido=False).all()
        r5001_infocrtom_lista = r5001infoCRTom.objects.using(db_slug).filter(
            r5001_rtom_id__in=listar_ids(r5001_rtom_lista)).filter(excluido=False).all()
        r5001_rprest_lista = r5001RPrest.objects.using(db_slug).filter(
            r5001_infototal_id__in=listar_ids(r5001_infototal_lista)).filter(excluido=False).all()
        r5001_rrecrepad_lista = r5001RRecRepAD.objects.using(db_slug).filter(
            r5001_infototal_id__in=listar_ids(r5001_infototal_lista)).filter(excluido=False).all()
        r5001_rcoml_lista = r5001RComl.objects.using(db_slug).filter(
            r5001_infototal_id__in=listar_ids(r5001_infototal_lista)).filter(excluido=False).all()
        r5001_rcprb_lista = r5001RCPRB.objects.using(db_slug).filter(
            r5001_infototal_id__in=listar_ids(r5001_infototal_lista)).filter(excluido=False).all()
        r5001_rrecespetdesp_lista = r5001RRecEspetDesp.objects.using(db_slug).filter(
            r5001_infototal_id__in=listar_ids(r5001_infototal_lista)).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r5001_evttotal'
        context = {
            'r5001_evttotal_lista': r5001_evttotal_lista,
            'r5001_evttotal_id': r5001_evttotal_id,
            'r5001_evttotal': r5001_evttotal,

            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,

            'r5001_regocorrs_lista': r5001_regocorrs_lista,
            'r5001_infototal_lista': r5001_infototal_lista,
            'r5001_rtom_lista': r5001_rtom_lista,
            'r5001_infocrtom_lista': r5001_infocrtom_lista,
            'r5001_rprest_lista': r5001_rprest_lista,
            'r5001_rrecrepad_lista': r5001_rrecrepad_lista,
            'r5001_rcoml_lista': r5001_rcoml_lista,
            'r5001_rcprb_lista': r5001_rcprb_lista,
            'r5001_rrecespetdesp_lista': r5001_rrecespetdesp_lista,
        }
        if for_print == 2:
            return render_to_pdf('totalizadores/r5001_evttotal.html', context)
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('totalizadores/r5001_evttotal.html', context)
            filename = "%s.xls" % r5001_evttotal.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('totalizadores/r5001_evttotal.html', context)
            filename = "%s.csv" % r5001_evttotal.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        else:
            return render(request, 'totalizadores/r5001_evttotal.html' % r5001_evttotal.versao, context)
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


def r5011_evttotalcontrib(request, hash):
    from emensageriapro.efdreinf.models import r5011evtTotalContrib
    from emensageriapro.r5011.models import *
    for_print = 0
    if slug:
        conta = get_json(slug)
        if not conta:
            raise Http404
        else:
            db_slug = 'emensageriapro' + str(conta.id)
    else:
        db_slug = 'default'
        conta = None
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url(hash)
        r5011_evttotalcontrib_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using(db_slug), excluido=False, id=usuario_id)
    pagina = ConfigPaginas.objects.using(db_slug).get(excluido=False, endereco='r5011_evttotalcontrib')
    permissao = ConfigPermissoes.objects.using(db_slug).get(excluido=False, config_paginas=pagina,
                                                            config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        r5011_evttotalcontrib = get_object_or_404(r5011evtTotalContrib.objects.using(db_slug), excluido=False,
                                                  id=r5011_evttotalcontrib_id)
        r5011_evttotalcontrib_lista = r5011evtTotalContrib.objects.using(db_slug).filter(id=r5011_evttotalcontrib_id,
                                                                                         excluido=False).all()

        r5011_regocorrs_lista = r5011regOcorrs.objects.using(db_slug).filter(
            r5011_evttotalcontrib_id__in=listar_ids(r5011_evttotalcontrib_lista)).filter(excluido=False).all()
        r5011_infototalcontrib_lista = r5011infoTotalContrib.objects.using(db_slug).filter(
            r5011_evttotalcontrib_id__in=listar_ids(r5011_evttotalcontrib_lista)).filter(excluido=False).all()
        r5011_rtom_lista = r5011RTom.objects.using(db_slug).filter(
            r5011_infototalcontrib_id__in=listar_ids(r5011_infototalcontrib_lista)).filter(excluido=False).all()
        r5011_infocrtom_lista = r5011infoCRTom.objects.using(db_slug).filter(
            r5011_rtom_id__in=listar_ids(r5011_rtom_lista)).filter(excluido=False).all()
        r5011_rprest_lista = r5011RPrest.objects.using(db_slug).filter(
            r5011_infototalcontrib_id__in=listar_ids(r5011_infototalcontrib_lista)).filter(excluido=False).all()
        r5011_rrecrepad_lista = r5011RRecRepAD.objects.using(db_slug).filter(
            r5011_infototalcontrib_id__in=listar_ids(r5011_infototalcontrib_lista)).filter(excluido=False).all()
        r5011_rcoml_lista = r5011RComl.objects.using(db_slug).filter(
            r5011_infototalcontrib_id__in=listar_ids(r5011_infototalcontrib_lista)).filter(excluido=False).all()
        r5011_rcprb_lista = r5011RCPRB.objects.using(db_slug).filter(
            r5011_infototalcontrib_id__in=listar_ids(r5011_infototalcontrib_lista)).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r5011_evttotalcontrib'
        context = {
            'r5011_evttotalcontrib_lista': r5011_evttotalcontrib_lista,
            'r5011_evttotalcontrib_id': r5011_evttotalcontrib_id,
            'r5011_evttotalcontrib': r5011_evttotalcontrib,

            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,

            'r5011_regocorrs_lista': r5011_regocorrs_lista,
            'r5011_infototalcontrib_lista': r5011_infototalcontrib_lista,
            'r5011_rtom_lista': r5011_rtom_lista,
            'r5011_infocrtom_lista': r5011_infocrtom_lista,
            'r5011_rprest_lista': r5011_rprest_lista,
            'r5011_rrecrepad_lista': r5011_rrecrepad_lista,
            'r5011_rcoml_lista': r5011_rcoml_lista,
            'r5011_rcprb_lista': r5011_rcprb_lista,
        }
        if for_print == 2:
            return render_to_pdf('totalizadores/r5011_evttotalcontrib.html', context)
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('totalizadores/r5011_evttotalcontrib.html', context)
            filename = "%s.xls" % r5011_evttotalcontrib.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('totalizadores/r5011_evttotalcontrib.html', context)
            filename = "%s.csv" % r5011_evttotalcontrib.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        else:
            return render(request, 'totalizadores/r5011_evttotalcontrib.html' % r5011_evttotalcontrib.versao, context)
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

