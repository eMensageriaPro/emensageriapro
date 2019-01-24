#coding: utf-8
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
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


#
#
# def salvar_modulos_paginas_permitidas(db_slug):
#     perfis = ConfigPerfis.objects.using( db_slug ).filter(excluido = False).all()
#     for perfil in perfis:
#         dados = {}
#         dicionario = {}
#         permissoes = ConfigPermissoes.objects.using( db_slug ).filter(excluido = False, config_perfis=perfil.id).all()
#         for a in permissoes:
#             chave = a.config_paginas.endereco
#             dicionario[chave+'_listar'] = a.permite_listar
#             dicionario[chave+'_cadastrar'] = a.permite_cadastrar
#             dicionario[chave+'_editar'] = a.permite_editar
#             dicionario[chave+'_visualizar'] = a.permite_visualizar
#             dicionario[chave+'_apagar'] = a.permite_apagar
#         dados['permissoes'] = dict_to_json(dicionario)
#         paginas_permitidas_id = []
#         modulos_permitidos_id = []
#         for p in permissoes:
#             if p.permite_listar:
#                 modulos_permitidos_id.append( '['+str(p.config_paginas.config_modulos.slug)+']')
#                 if p.config_paginas.config_modulos.modulo_pai_id:
#                     modulos_permitidos_id.append('['+str(p.config_paginas.config_modulos.modulo_pai.slug)+']')
#                     if p.config_paginas.config_modulos.modulo_pai.modulo_pai_id:
#                         modulos_permitidos_id.append('['+str(p.config_paginas.config_modulos.modulo_pai.modulo_pai.slug)+']')
#                 paginas_permitidas_id.append('['+str(p.config_paginas.endereco+']'))
#         dados['modulos_permitidos'] = ','.join(list(set(modulos_permitidos_id)))
#         dados['paginas_permitidas'] = ','.join(list(set(paginas_permitidas_id)))
#         obj = ConfigPerfis.objects.using( db_slug ).filter(id=perfil.id).update(**dados)
#
#
# def ler_arquivo(arquivo):
#     file = open(arquivo, 'r')
#     texto = file.read()
#     file.close()
#     return texto
#
# def criar_paginas(slug):
#     conta = get_object_or_404(Contas.objects.using( 'default' ), excluido = False, slug = slug)
#     db_slug = 'emensageriapro'+str(conta.id)
#     conta = get_object_or_404(Contas.objects.using( db_slug ), excluido = False, slug = slug)
#     from datetime import datetime
#     try:
#         texto = ler_arquivo('emensageriapro/urls.py')
#     except:
#         texto = ler_arquivo('/home/emensageriapro/apps_wsgi/emensageriapro/emensageriapro/urls.py')
#     lista = texto.split("name='")
#     lista_urls = []
#     del lista[0]
#     for a in lista:
#         b = a.split("'")
#         lista_urls.append( b[0] )
#     lista_pagina = ConfigPaginas.objects.using(db_slug).all()
#     pags_existentes = []
#     for b in lista_pagina:
#         pags_existentes.append( b.endereco )
#     for a in lista_urls:
#         if a not in pags_existentes:
#             dados = {}
#             dados['titulo'] = a
#             dados['endereco'] = a
#             dados['ordem'] = 0
#             dados['exibe_menu'] = 0
#             dados['criado_em'] = datetime.now()
#             dados['excluido'] = False
#             dados['config_modulos_id'] = 1
#             dados['criado_por_id'] = 1
#             dados['icone_id'] = 5
#             ConfigPaginas(**dados).save(using=slug)
#     lista_pagina = ConfigPaginas.objects.using(db_slug).exclude(endereco__in=lista_urls).all()
#     for a in lista_pagina:
#         ConfigPermissoes.objects.using(db_slug).filter(config_paginas_id=a.id).delete()
#         ConfigPaginas.objects.using(db_slug).filter(id=a.id).delete()

#
# def criar_permissoes(slug):
#     conta = get_object_or_404(Contas.objects.using( 'default' ), excluido = False, slug = slug)
#     db_slug = 'emensageriapro'+str(conta.id)
#     conta = get_object_or_404(Contas.objects.using( db_slug ), excluido = False, slug = slug)
#     from datetime import datetime
#     lista_paginas = ConfigPaginas.objects.using(db_slug).all()
#     lista_perfis = ConfigPerfis.objects.using(db_slug).all()
#     for per in lista_perfis:
#         for pag in lista_paginas:
#             lista = ConfigPermissoes.objects.using(db_slug).filter(config_paginas=pag.id, config_perfis=per.id).all()
#             if not lista:
#                 dados = {}
#                 dados['config_paginas_id'] = pag.id
#                 dados['config_perfis_id'] = per.id
#                 dados['criado_em'] = datetime.now()
#                 dados['excluido'] = False
#                 dados['criado_por_id'] = 1
#                 dados['permite_cadastrar'] = 0
#                 dados['permite_listar'] = 0
#                 dados['permite_visualizar'] = 0
#                 dados['permite_editar'] = 0
#                 dados['permite_apagar'] = 0
#                 dados['permite_tabelas_secundarias'] = 0
#                 ConfigPermissoes(**dados).save(using=db_slug)
#
#



def gera_senha(tamanho):
    from random import choice
    caracters = '0123456789abcdefghijlmnopqrstuwvxz!?@#$'
    senha = ''
    for char in xrange(tamanho):
        senha += choice(caracters)
    return senha


#
# def enviar_email_senha_recuperar(nome, email_usuario, senha, conta):
#     from django.utils.html import strip_tags
#     from django.core.mail import send_mail
#     mensagem_html = u"""
# <p>Prezado %s,<br>
# Acesse o sistema www.emensageriapro.adm.br pelo link
# <a href="http://www.emensageriapro.adm.br/">www.emensageriapro.adm.br/%s/</a><br>
# Nova senha é <strong>%s</strong><br>
# E-mail gerado automaticamente pelo sistema www.emensageriapro.com</p>
#     """ % (nome, conta.slug, conta.slug, senha)
#     send_mail(
#         u'Recuperação de senha | %s - www.emensageriapro.adm.br' % conta.titulo,
#         strip_tags(mensagem_html),
#         'recuperacao-de-senha@emensageriapro.adm.br',
#         [ email_usuario, ],
#         fail_silently=False,
#         html_message=mensagem_html,
#     )





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


@login_required
def alterar_senha(request):
    db_slug = 'default'
    try: usuario_id = request.user.id
    except: usuario_id = False
    if not usuario_id: return HttpResponseRedirect('/')
    usuario = get_object_or_404(Usuarios.objects.using(db_slug), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using(db_slug).get(excluido = False, endereco='usuarios')
    permissao = ConfigPermissoes.objects.using(db_slug).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    permissoes = ConfigPermissoes.objects.using(db_slug).filter(excluido = False, config_perfis=usuario.config_perfis).all()
    dict_permissoes = get_permissoes(permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if request.method == 'POST':
        if request.POST.get('senha') == request.POST.get('senha_repetir'):
            if request.POST.get('senha'):
                from django.contrib.auth.hashers import make_password
                hashed_password = make_password(request.POST.get('senha'))
                User.objects.using(db_slug).filter(id=usuario_id).update(password=hashed_password)
                messages.success(request, 'Senha alterada com sucesso!')
        else:
            messages.error(request, 'As duas senhas inseridas estão diferentes, insira duas senhas iguais para alterar a senha corretamente!')
    context = {

        'usuario': usuario,
        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,

        'permissao': permissao,
        'dict_permissoes': dict_permissoes,
    }
    return render(request, 'login_alterar_senha.html', context)


# def make_password(txt_pass):
#     import hashlib
#     hash0 = hashlib.md5(txt_pass).hexdigest()
#     hash1 = hashlib.sha224(txt_pass).hexdigest()
#     txt_pass_hash = hash0+ hash1
#     return txt_pass_hash