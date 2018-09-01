#coding: utf-8



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


class Usuarios(models.Model):
    usuario = models.CharField(max_length=20)
    senha = models.CharField(max_length=300, blank=True, default='asdkl1231')
    nome = models.CharField(max_length=60)
    email = models.EmailField()
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
        return unicode(self.nome)
    #usuarios_custom#
    #usuarios_custom#
    class Meta:
        db_table = r'usuarios'
        managed = True
        ordering = ['nome']


#VIEWS_MODELS
