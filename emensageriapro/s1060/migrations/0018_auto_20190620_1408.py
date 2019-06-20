# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 14:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('s1060', '0017_auto_20190602_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='s1060alteracao',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s1060alteracao',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s1060alteracao',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s1060alteracao_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s1060alteracaonovavalidade',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s1060alteracaonovavalidade',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s1060alteracaonovavalidade',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s1060alteracaonovavalidade_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s1060exclusao',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s1060exclusao',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s1060exclusao',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s1060exclusao_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s1060inclusao',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s1060inclusao',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s1060inclusao',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s1060inclusao_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
    ]