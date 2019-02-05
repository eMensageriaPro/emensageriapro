# coding: utf-8
from django.db import models
from django.utils import timezone
from django.db.models.query import QuerySet
from django.apps import apps
from datetime import datetime

get_model = apps.get_model


class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(excluido=False)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class SoftDeletionQuerySet(QuerySet):

    def delete(self, **kwargs):
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
            self.modificado_por_id = request.user.id
            self.modificado_em = timezone.now()
            self.excluido = None
        return super(SoftDeletionQuerySet, self).save()

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(excluido=False)

    def dead(self):
        return self.exclude(excluido=True)


class SoftDeletionModel(models.Model):
    excluido = models.NullBooleanField(blank=True, default=False)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
            self.modificado_por_id = request.user.id

        self.modificado_em = timezone.now()
        self.excluido = None
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()

    def save(self, **kwargs):
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
            if not self.criado_em:
                self.criado_em = timezone.now()
                self.criado_por_id = request.user.id
            self.modificado_por_id = request.user.id
            self.modificado_em = timezone.now()
        super(SoftDeletionModel, self).save(**kwargs)

