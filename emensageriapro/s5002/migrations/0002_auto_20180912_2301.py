# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s5002', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s5002idepgtoext',
            name='codpais',
            field=models.TextField(max_length=3),
        ),
        migrations.AlterField(
            model_name='s5002infoirrf',
            name='codcateg',
            field=models.TextField(max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='s5002irrf',
            name='tpcr',
            field=models.IntegerField(choices=[(3533, '3533 - Proventos de Aposentadoria, Reserva, Reforma ou Pens\xe3o Pagos por Previd\xeancia P\xfablica'), (47301, '047301 - Renda e Proventos de Qualquer Natureza'), (56107, '056107 - IRRF - Rendimento do Trabalho Assalariado no Pa\xeds/Ausente no Exterior a Servi\xe7o do Pa\xeds'), (56108, '056108 - IRRF - Empregado Dom\xe9stico'), (56109, '056109 - IRRF - Empregado Dom\xe9stico - 13\xba Sal Rescis\xe3o'), (56110, '056110 - IRRF - Empregado dom\xe9stico - 13\xba sal\xe1rio'), (56111, '056111 - IRRF - Empregado/Trabalhador Rural - Segurado Especial'), (56112, '056112 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13\xb0 sal\xe1rio'), (56113, '056113 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13\xb0 sal\xe1rio rescis\xf3rio'), (58806, '058806 - IRRF - Rendimento do trabalho sem v\xednculo empregat\xedcio'), (61001, '061001 - IRRF - Rendimentos relativos a presta\xe7\xe3o de servi\xe7os de transporte rodovi\xe1rio internacional de carga, pagos a transportador aut\xf4nomo PF residente no Paraguai'), (328006, '328006 - IRRF - Servi\xe7os Prestados por associados de cooperativas de trabalho'), (356201, '356201 - IRRF - Participa\xe7\xe3o dos trabalhadores em Lucros ou Resultados (PLR)')]),
        ),
    ]
