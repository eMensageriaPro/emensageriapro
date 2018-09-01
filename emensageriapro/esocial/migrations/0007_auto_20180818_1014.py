# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esocial', '0006_auto_20180816_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='s1000evtinfoempregador',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1005evttabestab',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1010evttabrubrica',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1020evttablotacao',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1030evttabcargo',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1035evttabcarreira',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1040evttabfuncao',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1050evttabhortur',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1060evttabambiente',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1070evttabprocesso',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1080evttaboperport',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1200evtremun',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1202evtrmnrpps',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1207evtbenprrp',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1210evtpgtos',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1250evtaqprod',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1260evtcomprod',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1270evtcontratavnp',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1280evtinfocomplper',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1295evttotconting',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1298evtreabreevper',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1299evtfechaevper',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s1300evtcontrsindpatr',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s2190evtadmprelim',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s2200evtadmissao',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s2205evtaltcadastral',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s2206evtaltcontratual',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s2210evtcat',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s2220evtmonit',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s2230evtafasttemp',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s2240evtexprisco',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s2241evtinsapo',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s2250evtavprevio',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s2260evtconvinterm',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s2298evtreintegr',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s2299evtdeslig',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s2300evttsvinicio',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s2306evttsvaltcontr',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s2399evttsvtermino',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s2400evtcdbenprrp',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s3000evtexclusao',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s5001evtbasestrab',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s5002evtirrfbenef',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s5011evtcs',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='s5012evtirrf',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='s1000evtinfoempregador',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1005evttabestab',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1010evttabrubrica',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1020evttablotacao',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1030evttabcargo',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1035evttabcarreira',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1040evttabfuncao',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1050evttabhortur',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1060evttabambiente',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1070evttabprocesso',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1080evttaboperport',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1200evtremun',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1202evtrmnrpps',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1207evtbenprrp',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1210evtpgtos',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1250evtaqprod',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1260evtcomprod',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1270evtcontratavnp',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1280evtinfocomplper',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1295evttotconting',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1298evtreabreevper',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1299evtfechaevper',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s1300evtcontrsindpatr',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s2190evtadmprelim',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s2200evtadmissao',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s2205evtaltcadastral',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s2206evtaltcontratual',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s2210evtcat',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s2220evtmonit',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s2230evtafasttemp',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s2240evtexprisco',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s2241evtinsapo',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s2250evtavprevio',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s2260evtconvinterm',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s2298evtreintegr',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s2299evtdeslig',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s2300evttsvinicio',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s2306evttsvaltcontr',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s2399evttsvtermino',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s2400evtcdbenprrp',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s3000evtexclusao',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s5001evtbasestrab',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s5002evtirrfbenef',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s5011evtcs',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='s5012evtirrf',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
    ]
