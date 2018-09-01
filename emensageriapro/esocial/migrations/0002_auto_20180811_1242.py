# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esocial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1000evtinfoempregador',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1005evttabestab',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1010evttabrubrica',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1020evttablotacao',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1030evttabcargo',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1035evttabcarreira',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1040evttabfuncao',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1050evttabhortur',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1060evttabambiente',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1070evttabprocesso',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1080evttaboperport',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1200evtremun',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1202evtrmnrpps',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1207evtbenprrp',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1210evtpgtos',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1250evtaqprod',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1260evtcomprod',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1270evtcontratavnp',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1280evtinfocomplper',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1295evttotconting',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1298evtreabreevper',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1299evtfechaevper',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s1300evtcontrsindpatr',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s2190evtadmprelim',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s2200evtadmissao',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s2205evtaltcadastral',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s2206evtaltcontratual',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s2210evtcat',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s2220evtmonit',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s2230evtafasttemp',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s2240evtexprisco',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s2241evtinsapo',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s2250evtavprevio',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s2260evtconvinterm',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s2298evtreintegr',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s2299evtdeslig',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s2300evttsvinicio',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s2306evttsvaltcontr',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s2399evttsvtermino',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s2400evtcdbenprrp',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s3000evtexclusao',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s5001evtbasestrab',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s5002evtirrfbenef',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s5011evtcs',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='s5012evtirrf',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
    ]
