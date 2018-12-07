# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0001_initial'),
        ('efdreinf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='r5011infoCRTom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crtom', models.IntegerField()),
                ('vlrcrtom', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vlrcrtomsusp', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r5011infocrtom_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r5011infocrtom_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['r5011_rtom', 'crtom', 'vlrcrtom', 'vlrcrtomsusp'],
                'db_table': 'r5011_infocrtom',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r5011infoTotalContrib',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nrrecarqbase', models.CharField(max_length=52, null=True, blank=True)),
                ('indexistinfo', models.IntegerField(choices=[(1, '1 - H\xe1 informa\xe7\xf5es de bases e/ou de tributos'), (2, '2 - H\xe1 movimento, por\xe9m n\xe3o h\xe1 informa\xe7\xf5es de bases ou de tributos'), (3, '3 - N\xe3o h\xe1 movimento na compet\xeancia')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r5011infototalcontrib_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r5011infototalcontrib_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r5011_evttotalcontrib', models.ForeignKey(related_name='r5011infototalcontrib_r5011_evttotalcontrib', to='efdreinf.r5011evtTotalContrib')),
            ],
            options={
                'ordering': ['r5011_evttotalcontrib', 'nrrecarqbase', 'indexistinfo'],
                'db_table': 'r5011_infototalcontrib',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r5011RComl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crcoml', models.IntegerField()),
                ('vlrcrcoml', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrcrcomlsusp', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r5011rcoml_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r5011rcoml_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r5011_infototalcontrib', models.ForeignKey(related_name='r5011rcoml_r5011_infototalcontrib', to='r5011.r5011infoTotalContrib')),
            ],
            options={
                'ordering': ['r5011_infototalcontrib', 'crcoml', 'vlrcrcoml', 'vlrcrcomlsusp'],
                'db_table': 'r5011_rcoml',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r5011RCPRB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crcprb', models.IntegerField()),
                ('vlrcrcprb', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrcrcprbsusp', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r5011rcprb_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r5011rcprb_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r5011_infototalcontrib', models.ForeignKey(related_name='r5011rcprb_r5011_infototalcontrib', to='r5011.r5011infoTotalContrib')),
            ],
            options={
                'ordering': ['r5011_infototalcontrib', 'crcprb', 'vlrcrcprb', 'vlrcrcprbsusp'],
                'db_table': 'r5011_rcprb',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r5011regOcorrs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpocorr', models.IntegerField(choices=[(1, '1 - Aviso'), (2, '2 - Erro')])),
                ('localerroaviso', models.CharField(max_length=100)),
                ('codresp', models.CharField(max_length=6)),
                ('dscresp', models.CharField(max_length=999)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r5011regocorrs_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r5011regocorrs_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r5011_evttotalcontrib', models.ForeignKey(related_name='r5011regocorrs_r5011_evttotalcontrib', to='efdreinf.r5011evtTotalContrib')),
            ],
            options={
                'ordering': ['r5011_evttotalcontrib', 'tpocorr', 'localerroaviso', 'codresp', 'dscresp'],
                'db_table': 'r5011_regocorrs',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r5011RPrest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinsctomador', models.IntegerField(choices=[(1, '1 - CNPJ'), (4, '4 - CNO')])),
                ('nrinsctomador', models.CharField(max_length=14)),
                ('vlrtotalbaseret', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrtotalretprinc', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrtotalretadic', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vlrtotalnretprinc', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vlrtotalnretadic', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r5011rprest_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r5011rprest_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r5011_infototalcontrib', models.ForeignKey(related_name='r5011rprest_r5011_infototalcontrib', to='r5011.r5011infoTotalContrib')),
            ],
            options={
                'ordering': ['r5011_infototalcontrib', 'tpinsctomador', 'nrinsctomador', 'vlrtotalbaseret', 'vlrtotalretprinc', 'vlrtotalretadic', 'vlrtotalnretprinc', 'vlrtotalnretadic'],
                'db_table': 'r5011_rprest',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r5011RRecRepAD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjassocdesp', models.CharField(max_length=14)),
                ('vlrtotalrep', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('crrecrepad', models.IntegerField()),
                ('vlrcrrecrepad', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrcrrecrepadsusp', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r5011rrecrepad_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r5011rrecrepad_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r5011_infototalcontrib', models.ForeignKey(related_name='r5011rrecrepad_r5011_infototalcontrib', to='r5011.r5011infoTotalContrib')),
            ],
            options={
                'ordering': ['r5011_infototalcontrib', 'cnpjassocdesp', 'vlrtotalrep', 'crrecrepad', 'vlrcrrecrepad', 'vlrcrrecrepadsusp'],
                'db_table': 'r5011_rrecrepad',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r5011RTom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjprestador', models.CharField(max_length=14)),
                ('vlrtotalbaseret', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r5011rtom_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r5011rtom_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r5011_infototalcontrib', models.ForeignKey(related_name='r5011rtom_r5011_infototalcontrib', to='r5011.r5011infoTotalContrib')),
            ],
            options={
                'ordering': ['r5011_infototalcontrib', 'cnpjprestador', 'vlrtotalbaseret'],
                'db_table': 'r5011_rtom',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='r5011infocrtom',
            name='r5011_rtom',
            field=models.ForeignKey(related_name='r5011infocrtom_r5011_rtom', to='r5011.r5011RTom'),
        ),
    ]
