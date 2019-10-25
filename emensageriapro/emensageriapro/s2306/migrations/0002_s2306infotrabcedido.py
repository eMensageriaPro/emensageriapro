# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0003_auto_20180912_1359'),
        ('s2306', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='s2306infoTrabCedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indremuncargo', models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2306infotrabcedido_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2306infotrabcedido_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2306_infocomplementares', models.OneToOneField(related_name='s2306infotrabcedido_s2306_infocomplementares', to='s2306.s2306infoComplementares')),
            ],
            options={
                'ordering': ['s2306_infocomplementares', 'indremuncargo'],
                'db_table': 's2306_infotrabcedido',
                'managed': True,
            },
        ),
    ]
