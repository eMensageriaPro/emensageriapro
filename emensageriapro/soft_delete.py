# coding: utf-8
from django.db import models
from django.utils import timezone
from django.db.models.query import QuerySet
from django.apps import apps
from django.contrib.auth.models import User
from datetime import datetime
from get_username import get_username
import json
from emensageriapro.padrao import gravar_auditoria
get_model = apps.get_model


class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(ativo=True)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class SoftDeletionQuerySet(QuerySet):

    def delete(self, **kwargs):
        req = get_username()
        self.desativado_por_id = req.user.id
        self.desativado_em = timezone.now()
        self.ativo = None
        gravar_auditoria('{}', json.dumps(self.__dict__, sort_keys=True, default=str),
                         self._meta.db_table, self.pk, req.user.id, 3)
        return super(SoftDeletionQuerySet, self).update()

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(ativo=True)

    def dead(self):
        return self.exclude(ativo=None)


class SoftDeletionModel(models.Model):

    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
                                   related_name='%(class)s_criado_por',
                                   blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
                                       related_name='%(class)s_modificado_por',
                                       blank=True, null=True)
    desativado_em = models.DateTimeField(blank=True, null=True)
    desativado_por = models.ForeignKey(User,
                                       related_name='%(class)s_desativado_por',
                                       blank=True, null=True)
    ativo = models.NullBooleanField(blank=True, default=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        req = get_username()
        self.desativado_por_id = req.user.id
        self.desativado_em = timezone.now()
        self.ativo = None
        gravar_auditoria('{}', json.dumps(self.__dict__, sort_keys=True, default=str),
                         self._meta.db_table, self.pk, req.user.id, 3)
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()

    def save(self, **kwargs):
        req = get_username()
        if not self.criado_em:
            self.criado_em = timezone.now()
            self.criado_por_id = req.user.id
            TIPO = 1
        else:
            self.modificado_em = timezone.now()
            self.modificado_por_id = req.user.id
            TIPO = 2
        super(SoftDeletionModel, self).save(**kwargs)

        gravar_auditoria('{}', json.dumps(self.__dict__, sort_keys=True, default=str),
                         self._meta.db_table, self.pk, req.user.id, TIPO)

