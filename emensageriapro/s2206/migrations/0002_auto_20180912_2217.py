# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2206', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s2206infoestatutario',
            options={'ordering': ['s2206_evtaltcontratual', 'tpplanrp', 'indtetorgps', 'indabonoperm', 'indparcremun'], 'managed': True},
        ),
        migrations.AddField(
            model_name='s2206infoestatutario',
            name='indabonoperm',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
        ),
        migrations.AddField(
            model_name='s2206infoestatutario',
            name='indparcremun',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
        ),
        migrations.AddField(
            model_name='s2206infoestatutario',
            name='indtetorgps',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
        ),
        migrations.AlterField(
            model_name='s2206localtrabdom',
            name='tplograd',
            field=models.TextField(max_length=4),
        ),
    ]
