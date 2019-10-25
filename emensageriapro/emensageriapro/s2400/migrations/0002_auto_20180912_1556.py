# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0003_auto_20180912_1359'),
        ('esocial', '0002_auto_20180912_1556'),
        ('s2400', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='s2400dependente',
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
                ('criado_por', models.ForeignKey(related_name='s2400dependente_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2400dependente_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2400_evtcdbenefin', models.ForeignKey(related_name='s2400dependente_s2400_evtcdbenefin', to='esocial.s2400evtCdBenefIn')),
            ],
            options={
                'ordering': ['s2400_evtcdbenefin', 'tpdep', 'nmdep', 'dtnascto', 'cpfdep', 'sexodep', 'depirrf', 'incfismen', 'depfinsprev'],
                'db_table': 's2400_dependente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2400endereco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2400endereco_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2400endereco_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2400_evtcdbenefin', models.OneToOneField(related_name='s2400endereco_s2400_evtcdbenefin', to='esocial.s2400evtCdBenefIn')),
            ],
            options={
                'ordering': ['s2400_evtcdbenefin'],
                'db_table': 's2400_endereco',
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='s2400altbeneficio',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2400altbeneficio',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2400altbeneficio',
            name='s2400_evtcdbenprrp',
        ),
        migrations.RemoveField(
            model_name='s2400altbeneficioinfopenmorte',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2400altbeneficioinfopenmorte',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2400altbeneficioinfopenmorte',
            name='s2400_altbeneficio',
        ),
        migrations.RemoveField(
            model_name='s2400fimbeneficio',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2400fimbeneficio',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2400fimbeneficio',
            name='s2400_evtcdbenprrp',
        ),
        migrations.RemoveField(
            model_name='s2400inibeneficio',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2400inibeneficio',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2400inibeneficio',
            name='s2400_evtcdbenprrp',
        ),
        migrations.RemoveField(
            model_name='s2400inibeneficioinfopenmorte',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2400inibeneficioinfopenmorte',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2400inibeneficioinfopenmorte',
            name='s2400_inibeneficio',
        ),
        migrations.AlterModelOptions(
            name='s2400brasil',
            options={'ordering': ['s2400_endereco', 'tplograd', 'dsclograd', 'nrlograd', 'complemento', 'bairro', 'cep', 'codmunic', 'uf'], 'managed': True},
        ),
        migrations.AlterModelOptions(
            name='s2400exterior',
            options={'ordering': ['s2400_endereco', 'paisresid', 'dsclograd', 'nrlograd', 'complemento', 'bairro', 'nmcid', 'codpostal'], 'managed': True},
        ),
        migrations.RemoveField(
            model_name='s2400brasil',
            name='s2400_evtcdbenprrp',
        ),
        migrations.RemoveField(
            model_name='s2400exterior',
            name='s2400_evtcdbenprrp',
        ),
        migrations.AlterField(
            model_name='s2400brasil',
            name='bairro',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='s2400brasil',
            name='dsclograd',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='s2400brasil',
            name='tplograd',
            field=models.TextField(max_length=4),
        ),
        migrations.AlterField(
            model_name='s2400exterior',
            name='bairro',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='s2400exterior',
            name='dsclograd',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='s2400exterior',
            name='paisresid',
            field=models.TextField(max_length=3),
        ),
        migrations.DeleteModel(
            name='s2400altBeneficio',
        ),
        migrations.DeleteModel(
            name='s2400altBeneficioinfoPenMorte',
        ),
        migrations.DeleteModel(
            name='s2400fimBeneficio',
        ),
        migrations.DeleteModel(
            name='s2400iniBeneficio',
        ),
        migrations.DeleteModel(
            name='s2400iniBeneficioinfoPenMorte',
        ),
        migrations.AddField(
            model_name='s2400brasil',
            name='s2400_endereco',
            field=models.OneToOneField(related_name='s2400brasil_s2400_endereco', default=1, to='s2400.s2400endereco'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s2400exterior',
            name='s2400_endereco',
            field=models.OneToOneField(related_name='s2400exterior_s2400_endereco', default=1, to='s2400.s2400endereco'),
            preserve_default=False,
        ),
    ]
