# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 21:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('s2210', '0009_auto_20190204_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='s2210agentecausador',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2210agentecausador_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2210agentecausador',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2210agentecausador_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2210atestado',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2210atestado_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2210atestado',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2210atestado_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2210catorigem',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2210catorigem_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2210catorigem',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2210catorigem_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2210idelocalacid',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2210idelocalacid_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2210idelocalacid',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2210idelocalacid_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2210parteatingida',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2210parteatingida_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2210parteatingida',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2210parteatingida_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
    ]