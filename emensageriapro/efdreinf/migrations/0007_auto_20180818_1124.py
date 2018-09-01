# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efdreinf', '0006_auto_20180816_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='r1000evtinfocontri',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='r1070evttabprocesso',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='r2010evtservtom',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='r2020evtservprest',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='r2030evtassocdesprec',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='r2040evtassocdesprep',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='r2050evtcomprod',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='r2060evtcprb',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='r2070evtpgtosdivs',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='r2098evtreabreevper',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='r2099evtfechaevper',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='r3010evtespdesportivo',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='r5001evttotal',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='r5011evttotalcontrib',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AddField(
            model_name='r9000evtexclusao',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='r1000evtinfocontri',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r1070evttabprocesso',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2010evtservtom',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2020evtservprest',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2030evtassocdesprec',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2040evtassocdesprep',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2050evtcomprod',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2060evtcprb',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2070evtpgtosdivs',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2098evtreabreevper',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2099evtfechaevper',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r3010evtespdesportivo',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r5001evttotal',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r5011evttotalcontrib',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r9000evtexclusao',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
    ]
