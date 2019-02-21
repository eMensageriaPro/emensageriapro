# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2200', '0008_auto_20190204_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s2200afastamento',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200afastamento',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200alvarajudicial',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200alvarajudicial',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200aposentadoria',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200aposentadoria',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200aprend',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200aprend',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200brasil',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200brasil',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200cessao',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200cessao',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200cnh',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200cnh',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200contato',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200contato',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200ctps',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200ctps',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200dependente',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200dependente',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200desligamento',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200desligamento',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200exterior',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200exterior',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200filiacaosindical',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200filiacaosindical',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200horario',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200horario',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200horcontratual',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200horcontratual',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200ideestabvinc',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200ideestabvinc',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200idetrabsubstituido',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200idetrabsubstituido',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200infoceletista',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200infoceletista',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200infodecjud',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200infodecjud',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200infodeficiencia',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200infodeficiencia',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200infoestatutario',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200infoestatutario',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200localtrabdom',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200localtrabdom',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200localtrabgeral',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200localtrabgeral',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200mudancacpf',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200mudancacpf',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200observacoes',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200observacoes',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200oc',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200oc',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200rg',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200rg',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200ric',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200ric',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200rne',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200rne',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200sucessaovinc',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200sucessaovinc',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200trabestrangeiro',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200trabestrangeiro',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200trabtemporario',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200trabtemporario',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200transfdom',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200transfdom',
            name='modificado_por',
        ),
        migrations.AlterField(
            model_name='s2200afastamento',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200afastamento',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200alvarajudicial',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200alvarajudicial',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200aposentadoria',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200aposentadoria',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200aprend',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200aprend',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200brasil',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200brasil',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200cessao',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200cessao',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200cnh',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200cnh',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200contato',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200contato',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200ctps',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200ctps',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200dependente',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200dependente',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200desligamento',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200desligamento',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200exterior',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200exterior',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200filiacaosindical',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200filiacaosindical',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200horario',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200horario',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200horcontratual',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200horcontratual',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200ideestabvinc',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200ideestabvinc',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200idetrabsubstituido',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200idetrabsubstituido',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200infoceletista',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200infoceletista',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200infodecjud',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200infodecjud',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200infodeficiencia',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200infodeficiencia',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200infoestatutario',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200infoestatutario',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200localtrabdom',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200localtrabdom',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200localtrabgeral',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200localtrabgeral',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200mudancacpf',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200mudancacpf',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200observacoes',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200observacoes',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200oc',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200oc',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200rg',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200rg',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200ric',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200ric',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200rne',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200rne',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200sucessaovinc',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200sucessaovinc',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200trabestrangeiro',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200trabestrangeiro',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200trabtemporario',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200trabtemporario',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200transfdom',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2200transfdom',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]