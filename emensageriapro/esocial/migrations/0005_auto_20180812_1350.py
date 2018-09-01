# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esocial', '0004_auto_20180812_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1000evtinfoempregador',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1005evttabestab',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1010evttabrubrica',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1020evttablotacao',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1030evttabcargo',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1035evttabcarreira',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1040evttabfuncao',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1050evttabhortur',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1060evttabambiente',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1070evttabprocesso',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1080evttaboperport',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1200evtremun',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1202evtrmnrpps',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1207evtbenprrp',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1210evtpgtos',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1250evtaqprod',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1260evtcomprod',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1270evtcontratavnp',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1280evtinfocomplper',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1295evttotconting',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1298evtreabreevper',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1299evtfechaevper',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1300evtcontrsindpatr',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s2190evtadmprelim',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s2200evtadmissao',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s2205evtaltcadastral',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s2206evtaltcontratual',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s2210evtcat',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s2220evtmonit',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s2230evtafasttemp',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s2240evtexprisco',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s2241evtinsapo',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s2250evtavprevio',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s2260evtconvinterm',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s2298evtreintegr',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s2299evtdeslig',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s2300evttsvinicio',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s2306evttsvaltcontr',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s2399evttsvtermino',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s2400evtcdbenprrp',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s3000evtexclusao',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s5001evtbasestrab',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s5002evtirrfbenef',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s5011evtcs',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s5012evtirrf',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
    ]
