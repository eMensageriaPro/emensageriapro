# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0003_auto_20180912_1359'),
        ('esocial', '0002_auto_20180912_1556'),
        ('s2200', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='s2200cessao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dtinicessao', models.DateField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2200cessao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2200cessao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2200_evtadmissao', models.OneToOneField(related_name='s2200cessao_s2200_evtadmissao', to='esocial.s2200evtAdmissao')),
            ],
            options={
                'ordering': ['s2200_evtadmissao', 'dtinicessao'],
                'db_table': 's2200_cessao',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='s2200dependente',
            options={'ordering': ['s2200_evtadmissao', 'tpdep', 'nmdep', 'dtnascto', 'cpfdep', 'sexodep', 'depirrf', 'depsf', 'inctrab', 'depfinsprev'], 'managed': True},
        ),
        migrations.AlterModelOptions(
            name='s2200infoestatutario',
            options={'ordering': ['s2200_evtadmissao', 'indprovim', 'tpprov', 'dtnomeacao', 'dtposse', 'dtexercicio', 'dtingsvpub', 'tpplanrp', 'indtetorgps', 'indabonoperm', 'dtiniabono', 'indparcremun', 'dtiniparc'], 'managed': True},
        ),
        migrations.AddField(
            model_name='s2200dependente',
            name='depfinsprev',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
        ),
        migrations.AddField(
            model_name='s2200dependente',
            name='sexodep',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'F', 'F - Feminino'), (b'M', 'M - Masculino')]),
        ),
        migrations.AddField(
            model_name='s2200infoestatutario',
            name='dtingsvpub',
            field=models.DateField(default='2018-09-10'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s2200infoestatutario',
            name='dtiniabono',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2200infoestatutario',
            name='dtiniparc',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2200infoestatutario',
            name='indabonoperm',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
        ),
        migrations.AddField(
            model_name='s2200infoestatutario',
            name='indparcremun',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
        ),
        migrations.AddField(
            model_name='s2200infoestatutario',
            name='indtetorgps',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
        ),
        migrations.AlterField(
            model_name='s2200brasil',
            name='tplograd',
            field=models.TextField(max_length=4),
        ),
        migrations.AlterField(
            model_name='s2200exterior',
            name='paisresid',
            field=models.TextField(max_length=3),
        ),
        migrations.AlterField(
            model_name='s2200localtrabdom',
            name='tplograd',
            field=models.TextField(max_length=4),
        ),
    ]
