#coding: utf-8

from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.shortcuts import render,redirect
from emensageriapro.padrao import *
from emensageriapro.controle_de_acesso.forms import *
from emensageriapro.controle_de_acesso.models import *
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.core.urlresolvers import reverse
from datetime import datetime


def json_to_dict(texto):
    import json
    dicionario = json.loads(texto)
    return dicionario

def dict_to_json(dicionario):
    import json
    json_string = json.dumps(dicionario)
    return json_string




def salvar_modulos_paginas_permitidas(db_slug):
    perfis = ConfigPerfis.objects.using( db_slug ).filter(excluido = False).all()
    for perfil in perfis:
        dados = {}
        dicionario = {}
        permissoes = ConfigPermissoes.objects.using( db_slug ).filter(excluido = False, config_perfis=perfil.id).all()
        for a in permissoes:
            chave = a.config_paginas.endereco
            dicionario[chave+'_listar'] = a.permite_listar
            dicionario[chave+'_cadastrar'] = a.permite_cadastrar
            dicionario[chave+'_editar'] = a.permite_editar
            dicionario[chave+'_visualizar'] = a.permite_visualizar
            dicionario[chave+'_apagar'] = a.permite_apagar
        dados['permissoes'] = dict_to_json(dicionario)
        paginas_permitidas_id = []
        modulos_permitidos_id = []
        for p in permissoes:
            if p.permite_listar:
                modulos_permitidos_id.append( '['+str(p.config_paginas.config_modulos.slug)+']')
                if p.config_paginas.config_modulos.modulo_pai_id:
                    modulos_permitidos_id.append('['+str(p.config_paginas.config_modulos.modulo_pai.slug)+']')
                    if p.config_paginas.config_modulos.modulo_pai.modulo_pai_id:
                        modulos_permitidos_id.append('['+str(p.config_paginas.config_modulos.modulo_pai.modulo_pai.slug)+']')
                paginas_permitidas_id.append('['+str(p.config_paginas.endereco+']'))
        dados['modulos_permitidos'] = ','.join(list(set(modulos_permitidos_id)))
        dados['paginas_permitidas'] = ','.join(list(set(paginas_permitidas_id)))
        obj = ConfigPerfis.objects.using( db_slug ).filter(id=perfil.id).update(**dados)


def ler_arquivo(arquivo):
    file = open(arquivo, 'r')
    texto = file.read()
    file.close()
    return texto


def gera_senha(tamanho):
    from random import choice
    caracters = '0123456789abcdefghijlmnopqrstuwvxz!?@#$'
    senha = ''
    for char in xrange(tamanho):
        senha += choice(caracters)
    return senha


def enviar_email_senha_recuperar(nome, email_usuario, senha):
    from django.utils.html import strip_tags
    from django.core.mail import send_mail
    mensagem_html = u"""
            <p>Prezado %s,<br>
            Acesse o sistema pelo link
            <a href="messageria.kmee.com.br">eMensageria</a><br>
            Nova senha é <strong>%s</strong><br>
            E-mail gerado automaticamente pelo sistema eMensageria</p>
        """ % (nome, senha)

    send_mail(
        u'Recuperação de senha | eMensageria',
        strip_tags(mensagem_html),
        'no-reply@kmee.com.br',
        [ email_usuario, ],
        fail_silently=False,
        html_message=mensagem_html,
    )



def recuperar_senha(request):
    db_slug = 'default'
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            dados_usuario = Usuarios.objects.using(db_slug).get(email=email, excluido=False)
        except:
            dados_usuario = None
        if dados_usuario:
            nova_senha = gera_senha(10)
            hashed_password = make_password(nova_senha)
            Usuarios.objects.using(db_slug).filter(email=email).update(senha=hashed_password)
            enviar_email_senha_recuperar(dados_usuario.nome, email, nova_senha)
            messages.success(request, 'Senha criada/alterada com sucesso, a nova senha foi enviada para seu e-mail!')
            return redirect('login')
        else:
            messages.error(request, 'Este email não está cadastrado em nossa base de dados!')
    context = {


    }
    return render(request, 'login_recuperar_senha.html', context)

def get_permissoes(permissoes):
    dict = {}
    for a in permissoes:
        chave = a.config_paginas.endereco
        dict[chave+'_listar'] = a.permite_listar
        dict[chave+'_cadastrar'] = a.permite_cadastrar
        dict[chave+'_editar'] = a.permite_editar
        dict[chave+'_visualizar'] = a.permite_visualizar
        dict[chave+'_apagar'] = a.permite_apagar
    return dict





def make_password(txt_pass):
    import hashlib
    hash0 = hashlib.md5(txt_pass).hexdigest()
    hash1 = hashlib.sha224(txt_pass).hexdigest()
    txt_pass_hash = hash0+ hash1
    return txt_pass_hash