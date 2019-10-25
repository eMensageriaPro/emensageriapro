# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1000', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1000alteracaoinfoefr',
            options={'ordering': ['s1000_alteracao_infoop', 'ideefr', 'cnpjefr', 'indrpps', 'prevcomp'], 'managed': True},
        ),
        migrations.AlterModelOptions(
            name='s1000alteracaoinfoop',
            options={'ordering': ['s1000_alteracao', 'nrsiafi', 'indugrpps', 'esferaop', 'poderop', 'vrtetorem', 'ideefr', 'cnpjefr'], 'managed': True},
        ),
        migrations.AlterModelOptions(
            name='s1000inclusaoinfoefr',
            options={'ordering': ['s1000_inclusao_infoop', 'ideefr', 'cnpjefr', 'indrpps', 'prevcomp'], 'managed': True},
        ),
        migrations.AlterModelOptions(
            name='s1000inclusaoinfoop',
            options={'ordering': ['s1000_inclusao', 'nrsiafi', 'indugrpps', 'esferaop', 'poderop', 'vrtetorem', 'ideefr', 'cnpjefr'], 'managed': True},
        ),
        migrations.AddField(
            model_name='s1000alteracaoinfoefr',
            name='indrpps',
            field=models.CharField(default=1, max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'N', 'N - N\xe3o'), (b'S', 'S - Sim'), (b'S', 'S - Sim')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s1000alteracaoinfoefr',
            name='prevcomp',
            field=models.CharField(default=1, max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s1000alteracaoinfoop',
            name='cnpjefr',
            field=models.CharField(max_length=14, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1000alteracaoinfoop',
            name='esferaop',
            field=models.IntegerField(blank=True, null=True, choices=[(1, '1 - Federal'), (2, '2 - Estadual ou distrital'), (3, '3 - Municipal')]),
        ),
        migrations.AddField(
            model_name='s1000alteracaoinfoop',
            name='ideefr',
            field=models.CharField(default=1, max_length=1, choices=[(b'N', 'N - N\xe3o \xe9 EFR'), (b'N', 'N - N\xe3o \xe9 EFR'), (b'S', 'S - \xc9 EFR'), (b'S', 'S - \xc9 EFR')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s1000alteracaoinfoop',
            name='indugrpps',
            field=models.CharField(default=1, max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s1000alteracaoinfoop',
            name='poderop',
            field=models.IntegerField(default=1, choices=[(1, '1 - Executivo'), (2, '2 - Judici\xe1rio'), (3, '3 - Legislativo'), (4, '4 - Minist\xe9rio P\xfablico'), (5, '5 - Tribunal de Contas'), (6, '6 - Defensoria P\xfablica')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s1000alteracaoinfoop',
            name='vrtetorem',
            field=models.DecimalField(default=1, max_length=14, max_digits=15, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s1000inclusaoinfoefr',
            name='indrpps',
            field=models.CharField(default=1, max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'N', 'N - N\xe3o'), (b'S', 'S - Sim'), (b'S', 'S - Sim')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s1000inclusaoinfoefr',
            name='prevcomp',
            field=models.CharField(default=1, max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s1000inclusaoinfoop',
            name='cnpjefr',
            field=models.CharField(max_length=14, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1000inclusaoinfoop',
            name='esferaop',
            field=models.IntegerField(blank=True, null=True, choices=[(1, '1 - Federal'), (2, '2 - Estadual ou distrital'), (3, '3 - Municipal')]),
        ),
        migrations.AddField(
            model_name='s1000inclusaoinfoop',
            name='ideefr',
            field=models.CharField(default=1, max_length=1, choices=[(b'N', 'N - N\xe3o \xe9 EFR'), (b'N', 'N - N\xe3o \xe9 EFR'), (b'S', 'S - \xc9 EFR'), (b'S', 'S - \xc9 EFR')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s1000inclusaoinfoop',
            name='indugrpps',
            field=models.CharField(default=1, max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s1000inclusaoinfoop',
            name='poderop',
            field=models.IntegerField(default=1, choices=[(1, '1 - Executivo'), (2, '2 - Judici\xe1rio'), (3, '3 - Legislativo'), (4, '4 - Minist\xe9rio P\xfablico'), (5, '5 - Tribunal de Contas'), (6, '6 - Defensoria P\xfablica')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s1000inclusaoinfoop',
            name='vrtetorem',
            field=models.DecimalField(default=1, max_length=14, max_digits=15, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='s1000alteracao',
            name='natjurid',
            field=models.TextField(max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoefr',
            name='ideefr',
            field=models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o \xe9 EFR'), (b'N', 'N - N\xe3o \xe9 EFR'), (b'S', 'S - \xc9 EFR'), (b'S', 'S - \xc9 EFR')]),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoente',
            name='indrpps',
            field=models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'N', 'N - N\xe3o'), (b'S', 'S - Sim'), (b'S', 'S - Sim')]),
        ),
        migrations.AlterField(
            model_name='s1000inclusao',
            name='natjurid',
            field=models.TextField(max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoefr',
            name='ideefr',
            field=models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o \xe9 EFR'), (b'N', 'N - N\xe3o \xe9 EFR'), (b'S', 'S - \xc9 EFR'), (b'S', 'S - \xc9 EFR')]),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoente',
            name='indrpps',
            field=models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'N', 'N - N\xe3o'), (b'S', 'S - Sim'), (b'S', 'S - Sim')]),
        ),
    ]
