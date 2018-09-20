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

from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



SIM_NAO = (
    (0, u'Não'),
    (1, u'Sim'),
)

AUDITORIA_TIPO = (
    (1, u'Inclusão'),
    (2, u'Alteração'),
    (3, u'Exclusão'),
)

TIPOS_CONFIG_PAGINAS = (
    (0, u'Manual'),
    (1, u'Automático'),
)

class Auditoria(models.Model):
    tabela = models.CharField(max_length=200)
    identidade = models.IntegerField()
    situacao_anterior = models.TextField()
    situacao_posterior = models.TextField()
    tipo = models.IntegerField(choices=AUDITORIA_TIPO)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.tabela) + ' - ' + unicode(self.identidade) + ' - ' + unicode(self.tipo)
    #auditoria_custom#
    #auditoria_custom#
    class Meta:
        db_table = r'auditoria'
        managed = True
        ordering = ['identidade']


class ConfigModulos(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    modulo_pai = models.ForeignKey('ConfigModulos',
        related_name='%(class)s_modulo_pai', blank=True, null=True)
    ordem = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.titulo)
    #config_modulos_custom#
    #config_modulos_custom#
    class Meta:
        db_table = r'config_modulos'
        managed = True
        ordering = ['titulo']


class ConfigPaginas(models.Model):
    config_modulos = models.ForeignKey('ConfigModulos',
        related_name='%(class)s_config_modulos')
    titulo = models.CharField(max_length=2000)
    endereco = models.CharField(max_length=500)
    exibe_menu = models.IntegerField(choices=SIM_NAO)
    tipo = models.IntegerField(choices=TIPOS_CONFIG_PAGINAS)
    ordem = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.titulo)
    #config_paginas_custom#
    #config_paginas_custom#
    class Meta:
        db_table = r'config_paginas'
        managed = True
        ordering = ['titulo']


class ConfigPerfis(models.Model):
    titulo = models.CharField(max_length=25)
    permissoes = models.TextField(blank=True, null=True)
    modulos_permitidos = models.TextField(blank=True, null=True)
    paginas_permitidas = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.titulo)
    #config_perfis_custom#
    #config_perfis_custom#
    class Meta:
        db_table = r'config_perfis'
        managed = True
        ordering = ['titulo']


class ConfigPermissoes(models.Model):
    config_perfis = models.ForeignKey('ConfigPerfis',
        related_name='%(class)s_config_perfis')
    config_paginas = models.ForeignKey('ConfigPaginas',
        related_name='%(class)s_config_paginas')
    permite_listar = models.IntegerField(choices=SIM_NAO)
    permite_cadastrar = models.IntegerField(choices=SIM_NAO)
    permite_editar = models.IntegerField(choices=SIM_NAO)
    permite_visualizar = models.IntegerField(choices=SIM_NAO)
    permite_apagar = models.IntegerField(choices=SIM_NAO)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.config_perfis) + ' - ' + unicode(self.config_paginas)
    #config_permissoes_custom#
    #config_permissoes_custom#
    class Meta:
        db_table = r'config_permissoes'
        managed = True
        ordering = ['config_perfis', 'config_paginas']

from django.contrib.auth.models import User
class Usuarios(User):
    # username = models.CharField(max_length=20)
    # password = models.CharField(max_length=300, blank=True, default='asdkl1231')
    # first_name = models.CharField(max_length=60)
    # last_name = models.CharField(max_length=60)
    # email = models.EmailField(max_length=60)
    # is_superuser = models.BooleanField()
    # is_staff = models.BooleanField()
    # is_active = models.BooleanField()
    # last_login = models.DateTimeField()
    # date_joined = models.DateField()
    config_perfis = models.ForeignKey('ConfigPerfis',
        related_name='%(class)s_config_perfis')
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.first_name) + ' - ' + unicode(self.last_name) + ' - ' + unicode(self.email) + ' - ' + unicode(self.is_superuser) + ' - ' + unicode(self.is_staff) + ' - ' + unicode(self.is_active) + ' - ' + unicode(self.last_login) + ' - ' + unicode(self.date_joined)
    #usuarios_custom#
    #usuarios_custom#
    class Meta:
        db_table = r'usuarios'
        managed = True
        ordering = ['first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'is_active', 'last_login', 'date_joined']


#VIEWS_MODELS
