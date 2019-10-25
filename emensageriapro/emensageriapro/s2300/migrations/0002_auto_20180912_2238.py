# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2300', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s2300dependente',
            options={'ordering': ['s2300_evttsvinicio', 'tpdep', 'nmdep', 'dtnascto', 'cpfdep', 'sexodep', 'depirrf', 'depsf', 'inctrab', 'depfinsprev'], 'managed': True},
        ),
        migrations.AlterModelOptions(
            name='s2300infotrabcedido',
            options={'ordering': ['s2300_infocomplementares', 'categorig', 'cnpjcednt', 'matricced', 'dtadmced', 'tpregtrab', 'tpregprev', 'infonus', 'indremuncargo'], 'managed': True},
        ),
        migrations.AddField(
            model_name='s2300dependente',
            name='depfinsprev',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
        ),
        migrations.AddField(
            model_name='s2300dependente',
            name='sexodep',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'F', 'F - Feminino'), (b'M', 'M - Masculino')]),
        ),
        migrations.AddField(
            model_name='s2300infotrabcedido',
            name='indremuncargo',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
        ),
        migrations.AlterField(
            model_name='s2300brasil',
            name='tplograd',
            field=models.TextField(max_length=4),
        ),
        migrations.AlterField(
            model_name='s2300exterior',
            name='paisresid',
            field=models.TextField(max_length=3),
        ),
    ]
