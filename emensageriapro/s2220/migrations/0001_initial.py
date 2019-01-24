# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esocial', '0001_initial'),
        ('controle_de_acesso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='s2220exame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dtexm', models.DateField()),
                ('procrealizado', models.IntegerField(null=True, blank=True)),
                ('obsproc', models.CharField(max_length=200, null=True, blank=True)),
                ('interprexm', models.IntegerField(choices=[(1, '1 - EE'), (2, '2 - SC'), (3, '3 - SC+')])),
                ('ordexame', models.IntegerField(choices=[(1, '1 - Referencial'), (2, '2 - Sequencial')])),
                ('dtinimonit', models.DateField()),
                ('dtfimmonit', models.DateField(null=True, blank=True)),
                ('indresult', models.IntegerField(blank=True, null=True, choices=[(1, '1 - Normal'), (2, '2 - Alterado'), (3, '3 - Est\xe1vel'), (4, '4 - Agravamento')])),
                ('nisresp', models.CharField(max_length=11)),
                ('nrconsclasse', models.CharField(max_length=8)),
                ('ufconsclasse', models.CharField(blank=True, max_length=2, null=True, choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2220exame_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2220exame_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2220_evtmonit', models.ForeignKey(related_name='s2220exame_s2220_evtmonit', to='esocial.s2220evtMonit')),
            ],
            options={
                'ordering': ['s2220_evtmonit', 'dtexm', 'procrealizado', 'obsproc', 'interprexm', 'ordexame', 'dtinimonit', 'dtfimmonit', 'indresult', 'nisresp', 'nrconsclasse', 'ufconsclasse'],
                'db_table': 's2220_exame',
                'managed': True,
            },
        ),
    ]
