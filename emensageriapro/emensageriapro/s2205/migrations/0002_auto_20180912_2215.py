# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2205', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s2205dependente',
            options={'ordering': ['s2205_evtaltcadastral', 'tpdep', 'nmdep', 'dtnascto', 'cpfdep', 'sexodep', 'depirrf', 'depsf', 'inctrab', 'depfinsprev'], 'managed': True},
        ),
        migrations.AddField(
            model_name='s2205dependente',
            name='depfinsprev',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
        ),
        migrations.AddField(
            model_name='s2205dependente',
            name='sexodep',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'F', 'F - Feminino'), (b'M', 'M - Masculino')]),
        ),
        migrations.AlterField(
            model_name='s2205brasil',
            name='tplograd',
            field=models.TextField(max_length=4),
        ),
        migrations.AlterField(
            model_name='s2205exterior',
            name='paisresid',
            field=models.TextField(max_length=3),
        ),
    ]
