# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esocial', '0011_auto_20180822_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='s1000evtinfoempregador',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1005evttabestab',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1010evttabrubrica',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1020evttablotacao',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1030evttabcargo',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1035evttabcarreira',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1040evttabfuncao',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1050evttabhortur',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1060evttabambiente',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1070evttabprocesso',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1080evttaboperport',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1200evtremun',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1202evtrmnrpps',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1207evtbenprrp',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1210evtpgtos',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1250evtaqprod',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1260evtcomprod',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1270evtcontratavnp',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1280evtinfocomplper',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1295evttotconting',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1298evtreabreevper',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1299evtfechaevper',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1300evtcontrsindpatr',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2190evtadmprelim',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2200evtadmissao',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2205evtaltcadastral',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2206evtaltcontratual',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2210evtcat',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2220evtmonit',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2230evtafasttemp',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2240evtexprisco',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2241evtinsapo',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2250evtavprevio',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2260evtconvinterm',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2298evtreintegr',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2299evtdeslig',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2300evttsvinicio',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2306evttsvaltcontr',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2399evttsvtermino',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s2400evtcdbenprrp',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s3000evtexclusao',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s5001evtbasestrab',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s5002evtirrfbenef',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s5011evtcs',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s5012evtirrf',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
    ]
