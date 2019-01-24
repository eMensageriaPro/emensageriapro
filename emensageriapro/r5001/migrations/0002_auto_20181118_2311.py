# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-18 23:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('r5001', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r5001infocrtom',
            options={'managed': True, 'ordering': ['r5001_rtom', 'crtom']},
        ),
        migrations.AlterModelOptions(
            name='r5001infototal',
            options={'managed': True, 'ordering': ['r5001_evttotal', 'tpinsc', 'nrinsc']},
        ),
        migrations.AlterModelOptions(
            name='r5001rcoml',
            options={'managed': True, 'ordering': ['r5001_infototal', 'crcoml', 'vlrcrcoml']},
        ),
        migrations.AlterModelOptions(
            name='r5001rcprb',
            options={'managed': True, 'ordering': ['r5001_infototal', 'crcprb', 'vlrcrcprb']},
        ),
        migrations.AlterModelOptions(
            name='r5001rprest',
            options={'managed': True, 'ordering': ['r5001_infototal', 'tpinsctomador', 'nrinsctomador', 'vlrtotalbaseret', 'vlrtotalretprinc']},
        ),
        migrations.AlterModelOptions(
            name='r5001rrecespetdesp',
            options={'managed': True, 'ordering': ['r5001_infototal', 'crrecespetdesp', 'vlrreceitatotal', 'vlrcrrecespetdesp']},
        ),
        migrations.AlterModelOptions(
            name='r5001rrecrepad',
            options={'managed': True, 'ordering': ['r5001_infototal', 'cnpjassocdesp', 'vlrtotalrep', 'crrecrepad', 'vlrcrrecrepad']},
        ),
        migrations.AddField(
            model_name='r5001infototal',
            name='nrinsc',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AddField(
            model_name='r5001infototal',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (4, '4 - CNO')], default=0),
        ),
        migrations.AddField(
            model_name='r5001rtom',
            name='cno',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='r5001infocrtom',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='r5001infocrtom',
            name='crtom',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='r5001infocrtom',
            name='r5001_rtom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r5001infocrtom_r5001_rtom', to='r5001.r5001RTom'),
        ),
        migrations.AlterField(
            model_name='r5001infototal',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='r5001infototal',
            name='r5001_evttotal',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r5001infototal_r5001_evttotal', to='efdreinf.r5001evtTotal'),
        ),
        migrations.AlterField(
            model_name='r5001rcoml',
            name='crcoml',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='r5001rcoml',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='r5001rcoml',
            name='r5001_infototal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r5001rcoml_r5001_infototal', to='r5001.r5001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r5001rcoml',
            name='vlrcrcoml',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rcprb',
            name='crcprb',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='r5001rcprb',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='r5001rcprb',
            name='r5001_infototal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r5001rcprb_r5001_infototal', to='r5001.r5001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r5001rcprb',
            name='vlrcrcprb',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001regocorrs',
            name='codresp',
            field=models.CharField(default=b'A', max_length=6),
        ),
        migrations.AlterField(
            model_name='r5001regocorrs',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='r5001regocorrs',
            name='dscresp',
            field=models.CharField(default=b'A', max_length=999),
        ),
        migrations.AlterField(
            model_name='r5001regocorrs',
            name='localerroaviso',
            field=models.CharField(default=b'A', max_length=200),
        ),
        migrations.AlterField(
            model_name='r5001regocorrs',
            name='r5001_evttotal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r5001regocorrs_r5001_evttotal', to='efdreinf.r5001evtTotal'),
        ),
        migrations.AlterField(
            model_name='r5001regocorrs',
            name='tpocorr',
            field=models.IntegerField(choices=[(1, '1 - Aviso'), (2, '2 - Erro')], default=0),
        ),
        migrations.AlterField(
            model_name='r5001rprest',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='r5001rprest',
            name='nrinsctomador',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rprest',
            name='r5001_infototal',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r5001rprest_r5001_infototal', to='r5001.r5001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r5001rprest',
            name='tpinsctomador',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (4, '4 - CNO')], default=0),
        ),
        migrations.AlterField(
            model_name='r5001rprest',
            name='vlrtotalbaseret',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rprest',
            name='vlrtotalretprinc',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rrecespetdesp',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='r5001rrecespetdesp',
            name='crrecespetdesp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='r5001rrecespetdesp',
            name='r5001_infototal',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r5001rrecespetdesp_r5001_infototal', to='r5001.r5001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r5001rrecespetdesp',
            name='vlrcrrecespetdesp',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rrecespetdesp',
            name='vlrreceitatotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rrecrepad',
            name='cnpjassocdesp',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rrecrepad',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='r5001rrecrepad',
            name='crrecrepad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='r5001rrecrepad',
            name='r5001_infototal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r5001rrecrepad_r5001_infototal', to='r5001.r5001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r5001rrecrepad',
            name='vlrcrrecrepad',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rrecrepad',
            name='vlrtotalrep',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rtom',
            name='cnpjprestador',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rtom',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='r5001rtom',
            name='r5001_infototal',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r5001rtom_r5001_infototal', to='r5001.r5001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r5001rtom',
            name='vlrtotalbaseret',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
    ]
