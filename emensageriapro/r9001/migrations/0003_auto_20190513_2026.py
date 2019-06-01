# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-13 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('r9001', '0002_auto_20190428_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r9001infocrtom',
            name='crtom',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='r9001infocrtom',
            name='r9001_rtom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9001infocrtom_r9001_rtom', to='r9001.r9001RTom'),
        ),
        migrations.AlterField(
            model_name='r9001infocrtom',
            name='vlrcrtom',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r9001infocrtom',
            name='vlrcrtomsusp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r9001infototal',
            name='nrinsc',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='r9001infototal',
            name='r9001_evttotal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9001infototal_r9001_evttotal', to='efdreinf.r9001evtTotal'),
        ),
        migrations.AlterField(
            model_name='r9001infototal',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (5, '5 - CGC')], default=0),
        ),
        migrations.AlterField(
            model_name='r9001rcoml',
            name='crcoml',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='r9001rcoml',
            name='r9001_infototal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9001rcoml_r9001_infototal', to='r9001.r9001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r9001rcoml',
            name='vlrcrcoml',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='r9001rcoml',
            name='vlrcrcomlsusp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r9001rcprb',
            name='crcprb',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='r9001rcprb',
            name='r9001_infototal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9001rcprb_r9001_infototal', to='r9001.r9001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r9001rcprb',
            name='vlrcrcprb',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='r9001rcprb',
            name='vlrcrcprbsusp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r9001regocorrs',
            name='codresp',
            field=models.CharField(default=b'A', max_length=6),
        ),
        migrations.AlterField(
            model_name='r9001regocorrs',
            name='dscresp',
            field=models.CharField(default=b'A', max_length=999),
        ),
        migrations.AlterField(
            model_name='r9001regocorrs',
            name='localerroaviso',
            field=models.CharField(default=b'A', max_length=200),
        ),
        migrations.AlterField(
            model_name='r9001regocorrs',
            name='r9001_evttotal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9001regocorrs_r9001_evttotal', to='efdreinf.r9001evtTotal'),
        ),
        migrations.AlterField(
            model_name='r9001regocorrs',
            name='tpocorr',
            field=models.IntegerField(choices=[(1, '1 - Erro'), (2, '2 - Aviso.')], default=0),
        ),
        migrations.AlterField(
            model_name='r9001rprest',
            name='nrinsctomador',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='r9001rprest',
            name='r9001_infototal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9001rprest_r9001_infototal', to='r9001.r9001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r9001rprest',
            name='tpinsctomador',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='r9001rprest',
            name='vlrtotalbaseret',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='r9001rprest',
            name='vlrtotalnretadic',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r9001rprest',
            name='vlrtotalnretprinc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r9001rprest',
            name='vlrtotalretadic',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r9001rprest',
            name='vlrtotalretprinc',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='r9001rrecespetdesp',
            name='crrecespetdesp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='r9001rrecespetdesp',
            name='r9001_infototal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9001rrecespetdesp_r9001_infototal', to='r9001.r9001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r9001rrecespetdesp',
            name='vlrcrrecespetdesp',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='r9001rrecespetdesp',
            name='vlrcrrecespetdespsusp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r9001rrecespetdesp',
            name='vlrreceitatotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='r9001rrecrepad',
            name='cnpjassocdesp',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='r9001rrecrepad',
            name='crrecrepad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='r9001rrecrepad',
            name='r9001_infototal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9001rrecrepad_r9001_infototal', to='r9001.r9001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r9001rrecrepad',
            name='vlrcrrecrepad',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='r9001rrecrepad',
            name='vlrcrrecrepadsusp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r9001rrecrepad',
            name='vlrtotalrep',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='r9001rtom',
            name='cnpjprestador',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='r9001rtom',
            name='r9001_infototal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9001rtom_r9001_infototal', to='r9001.r9001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r9001rtom',
            name='vlrtotalbaseret',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]