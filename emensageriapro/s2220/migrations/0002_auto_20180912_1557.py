# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0003_auto_20180912_1359'),
        ('esocial', '0003_auto_20180912_1556'),
        ('s2220', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='s2220exMedOcup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpexameocup', models.IntegerField(choices=[(0, '0 - Exame m\xe9dico ocupacional'), (1, '1 - Exame toxicol\xf3gico do motorista profissional')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2220exmedocup_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2220exmedocup_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2220_evtmonit', models.OneToOneField(related_name='s2220exmedocup_s2220_evtmonit', to='esocial.s2220evtMonit')),
            ],
            options={
                'ordering': ['s2220_evtmonit', 'tpexameocup'],
                'db_table': 's2220_exmedocup',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2220toxicologico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dtexame', models.DateField()),
                ('cnpjlab', models.CharField(max_length=14)),
                ('codseqexame', models.CharField(max_length=11)),
                ('nmmed', models.CharField(max_length=70)),
                ('nrcrm', models.CharField(max_length=8)),
                ('ufcrm', models.CharField(max_length=2, choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2220toxicologico_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2220toxicologico_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2220_evtmonit', models.OneToOneField(related_name='s2220toxicologico_s2220_evtmonit', to='esocial.s2220evtMonit')),
            ],
            options={
                'ordering': ['s2220_evtmonit', 'dtexame', 'cnpjlab', 'codseqexame', 'nmmed', 'nrcrm', 'ufcrm'],
                'db_table': 's2220_toxicologico',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='s2220exame',
            options={'ordering': ['s2220_evtmonit', 'dtexm', 'procrealizado', 'obsproc', 'interprexm', 'ordexame', 'dtinimonit', 'dtfimmonit', 'indresult', 'nisresp', 'nrconsclasse', 'ufconsclasse', 'cpfresp', 'nmresp', 'nrcrm', 'ufcrm'], 'managed': True},
        ),
        migrations.AddField(
            model_name='s2220exame',
            name='cpfresp',
            field=models.CharField(default=999, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s2220exame',
            name='nmresp',
            field=models.CharField(default='aaa', max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s2220exame',
            name='nrcrm',
            field=models.CharField(default=999, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s2220exame',
            name='ufcrm',
            field=models.CharField(default='CE', max_length=2, choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')]),
            preserve_default=False,
        ),
    ]
