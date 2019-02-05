# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 21:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('r3010', '0007_auto_20190204_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='r3010boletim',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r3010boletim_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r3010boletim',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r3010boletim_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r3010infoproc',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r3010infoproc_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r3010infoproc',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r3010infoproc_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r3010outrasreceitas',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r3010outrasreceitas_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r3010outrasreceitas',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r3010outrasreceitas_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r3010receitaingressos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r3010receitaingressos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r3010receitaingressos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r3010receitaingressos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
    ]
