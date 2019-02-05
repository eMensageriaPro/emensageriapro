# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 21:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('s2399', '0009_auto_20190204_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='s2399detoper',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399detoper_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399detoper',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399detoper_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399detplano',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399detplano_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399detplano',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399detplano_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399detverbas',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399detverbas_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399detverbas',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399detverbas_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399dmdev',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399dmdev_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399dmdev',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399dmdev_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399ideestablot',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399ideestablot_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399ideestablot',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399ideestablot_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399infoagnocivo',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399infoagnocivo_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399infoagnocivo',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399infoagnocivo_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399infomv',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399infomv_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399infomv',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399infomv_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399infosimples',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399infosimples_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399infosimples',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399infosimples_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399mudancacpf',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399mudancacpf_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399mudancacpf',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399mudancacpf_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399procjudtrab',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399procjudtrab_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399procjudtrab',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399procjudtrab_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399quarentena',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399quarentena_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399quarentena',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399quarentena_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399remunoutrempr',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399remunoutrempr_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2399remunoutrempr',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2399remunoutrempr_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
    ]
