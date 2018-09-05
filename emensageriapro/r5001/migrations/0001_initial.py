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
            name='r5001infoCRTom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crtom', models.IntegerField()),
                ('vlrcrtom', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vlrcrtomsusp', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r5001infocrtom_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r5001infocrtom_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['r5001_rtom', 'crtom', 'vlrcrtom', 'vlrcrtomsusp'],
                'db_table': 'r5001_infocrtom',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r5001infoTotal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nrrecarqbase', models.CharField(max_length=52, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r5001infototal_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r5001infototal_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r5001_evttotal', models.OneToOneField(related_name='r5001infototal_r5001_evttotal', to='efdreinf.r5001evtTotal')),
            ],
            options={
                'ordering': ['r5001_evttotal', 'nrrecarqbase'],
                'db_table': 'r5001_infototal',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r5001RComl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crcoml', models.IntegerField()),
                ('vlrcrcoml', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrcrcomlsusp', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r5001rcoml_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r5001rcoml_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r5001_infototal', models.ForeignKey(related_name='r5001rcoml_r5001_infototal', to='r5001.r5001infoTotal')),
            ],
            options={
                'ordering': ['r5001_infototal', 'crcoml', 'vlrcrcoml', 'vlrcrcomlsusp'],
                'db_table': 'r5001_rcoml',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r5001RCPRB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crcprb', models.IntegerField()),
                ('vlrcrcprb', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrcrcprbsusp', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r5001rcprb_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r5001rcprb_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r5001_infototal', models.ForeignKey(related_name='r5001rcprb_r5001_infototal', to='r5001.r5001infoTotal')),
            ],
            options={
                'ordering': ['r5001_infototal', 'crcprb', 'vlrcrcprb', 'vlrcrcprbsusp'],
                'db_table': 'r5001_rcprb',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r5001regOcorrs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpocorr', models.IntegerField(choices=[(1, '1 - Aviso'), (2, '2 - Erro')])),
                ('localerroaviso', models.CharField(max_length=100)),
                ('codresp', models.CharField(max_length=6)),
                ('dscresp', models.CharField(max_length=999)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r5001regocorrs_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r5001regocorrs_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r5001_evttotal', models.ForeignKey(related_name='r5001regocorrs_r5001_evttotal', to='efdreinf.r5001evtTotal')),
            ],
            options={
                'ordering': ['r5001_evttotal', 'tpocorr', 'localerroaviso', 'codresp', 'dscresp'],
                'db_table': 'r5001_regocorrs',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r5001RPrest',
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
                ('criado_por', models.ForeignKey(related_name='r5001rprest_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r5001rprest_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r5001_infototal', models.OneToOneField(related_name='r5001rprest_r5001_infototal', to='r5001.r5001infoTotal')),
            ],
            options={
                'ordering': ['r5001_infototal', 'tpinsctomador', 'nrinsctomador', 'vlrtotalbaseret', 'vlrtotalretprinc', 'vlrtotalretadic', 'vlrtotalnretprinc', 'vlrtotalnretadic'],
                'db_table': 'r5001_rprest',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r5001RRecEspetDesp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crrecespetdesp', models.IntegerField()),
                ('vlrreceitatotal', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrcrrecespetdesp', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrcrrecespetdespsusp', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r5001rrecespetdesp_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r5001rrecespetdesp_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r5001_infototal', models.OneToOneField(related_name='r5001rrecespetdesp_r5001_infototal', to='r5001.r5001infoTotal')),
            ],
            options={
                'ordering': ['r5001_infototal', 'crrecespetdesp', 'vlrreceitatotal', 'vlrcrrecespetdesp', 'vlrcrrecespetdespsusp'],
                'db_table': 'r5001_rrecespetdesp',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r5001RRecRepAD',
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
                ('criado_por', models.ForeignKey(related_name='r5001rrecrepad_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r5001rrecrepad_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r5001_infototal', models.ForeignKey(related_name='r5001rrecrepad_r5001_infototal', to='r5001.r5001infoTotal')),
            ],
            options={
                'ordering': ['r5001_infototal', 'cnpjassocdesp', 'vlrtotalrep', 'crrecrepad', 'vlrcrrecrepad', 'vlrcrrecrepadsusp'],
                'db_table': 'r5001_rrecrepad',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r5001RTom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjprestador', models.CharField(max_length=14)),
                ('vlrtotalbaseret', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r5001rtom_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r5001rtom_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r5001_infototal', models.OneToOneField(related_name='r5001rtom_r5001_infototal', to='r5001.r5001infoTotal')),
            ],
            options={
                'ordering': ['r5001_infototal', 'cnpjprestador', 'vlrtotalbaseret'],
                'db_table': 'r5001_rtom',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='r5001infocrtom',
            name='r5001_rtom',
            field=models.ForeignKey(related_name='r5001infocrtom_r5001_rtom', to='r5001.r5001RTom'),
        ),
    ]
