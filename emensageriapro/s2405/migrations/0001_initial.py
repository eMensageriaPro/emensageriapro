# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0003_auto_20180912_1359'),
        ('esocial', '0003_auto_20180912_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='s2405brasil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tplograd', models.TextField(max_length=4)),
                ('dsclograd', models.CharField(max_length=80)),
                ('nrlograd', models.CharField(max_length=10)),
                ('complemento', models.CharField(max_length=30, null=True, blank=True)),
                ('bairro', models.CharField(max_length=60, null=True, blank=True)),
                ('cep', models.CharField(max_length=8)),
                ('codmunic', models.TextField(max_length=7)),
                ('uf', models.CharField(max_length=2, choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2405brasil_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2405brasil_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2405_endereco', 'tplograd', 'dsclograd', 'nrlograd', 'complemento', 'bairro', 'cep', 'codmunic', 'uf'],
                'db_table': 's2405_brasil',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2405dependente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpdep', models.CharField(max_length=2)),
                ('nmdep', models.CharField(max_length=70)),
                ('dtnascto', models.DateField()),
                ('cpfdep', models.CharField(max_length=11, null=True, blank=True)),
                ('sexodep', models.CharField(max_length=1, choices=[(b'F', 'F - Feminino'), (b'M', 'M - Masculino')])),
                ('depirrf', models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')])),
                ('incfismen', models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'N', 'N - N\xe3o'), (b'S', 'S - Sim'), (b'S', 'S - Sim')])),
                ('depfinsprev', models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2405dependente_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2405dependente_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2405_evtcdbenefalt', models.ForeignKey(related_name='s2405dependente_s2405_evtcdbenefalt', to='esocial.s2405evtCdBenefAlt')),
            ],
            options={
                'ordering': ['s2405_evtcdbenefalt', 'tpdep', 'nmdep', 'dtnascto', 'cpfdep', 'sexodep', 'depirrf', 'incfismen', 'depfinsprev'],
                'db_table': 's2405_dependente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2405endereco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2405endereco_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2405endereco_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2405_evtcdbenefalt', models.OneToOneField(related_name='s2405endereco_s2405_evtcdbenefalt', to='esocial.s2405evtCdBenefAlt')),
            ],
            options={
                'ordering': ['s2405_evtcdbenefalt'],
                'db_table': 's2405_endereco',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2405exterior',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paisresid', models.TextField(max_length=3)),
                ('dsclograd', models.CharField(max_length=80)),
                ('nrlograd', models.CharField(max_length=10)),
                ('complemento', models.CharField(max_length=30, null=True, blank=True)),
                ('bairro', models.CharField(max_length=60, null=True, blank=True)),
                ('nmcid', models.CharField(max_length=50)),
                ('codpostal', models.CharField(max_length=12, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2405exterior_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2405exterior_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2405_endereco', models.OneToOneField(related_name='s2405exterior_s2405_endereco', to='s2405.s2405endereco')),
            ],
            options={
                'ordering': ['s2405_endereco', 'paisresid', 'dsclograd', 'nrlograd', 'complemento', 'bairro', 'nmcid', 'codpostal'],
                'db_table': 's2405_exterior',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='s2405brasil',
            name='s2405_endereco',
            field=models.OneToOneField(related_name='s2405brasil_s2405_endereco', to='s2405.s2405endereco'),
        ),
    ]
