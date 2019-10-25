# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1202', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1202dmdev',
            options={'ordering': ['s1202_evtrmnrpps', 'idedmdev', 'codcateg'], 'managed': True},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperantideadc',
            options={'ordering': ['s1202_infoperant', 'dtlei', 'nrlei', 'dtef', 'dtacconv', 'tpacconv', 'compacconv', 'dtefacconv', 'dsc'], 'managed': True},
        ),
        migrations.AddField(
            model_name='s1202dmdev',
            name='codcateg',
            field=models.TextField(default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s1202infoperantideadc',
            name='compacconv',
            field=models.CharField(max_length=7, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1202infoperantideadc',
            name='dsc',
            field=models.CharField(default='aaa', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s1202infoperantideadc',
            name='dtacconv',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1202infoperantideadc',
            name='dtefacconv',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1202infoperantideadc',
            name='tpacconv',
            field=models.CharField(default=1, max_length=1, choices=[(b'B', 'B - Legisla\xe7\xe3o federal, estadual, municipal ou distrital'), (b'F', 'F - Outras verbas de natureza salarial ou n\xe3o salarial devidas ap\xf3s o desligamento'), (b'G', 'G - Decis\xe3o administrativa'), (b'H', 'H - Decis\xe3o judicial')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='s1202infoperantremunperant',
            name='codcateg',
            field=models.TextField(max_length=3),
        ),
        migrations.AlterField(
            model_name='s1202infoperapurremunperapur',
            name='codcateg',
            field=models.TextField(max_length=3),
        ),
        migrations.AlterField(
            model_name='s1202procjudtrab',
            name='tptrib',
            field=models.IntegerField(choices=[(2, '2 - Contribui\xe7\xf5es sociais do trabalhador'), (2, '2 - IRRF'), (3, '3 - FGTS'), (4, '4 - Contribui\xe7\xe3o sindical')]),
        ),
    ]
