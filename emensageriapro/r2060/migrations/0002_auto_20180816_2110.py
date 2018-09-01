# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r2060', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r2060tipoajuste',
            name='codajuste',
            field=models.IntegerField(choices=[(1, '1 - Ajuste da CPRB: Ado\xe7\xe3o do Regime de Caixa'), (10, '10 - O valor do aporte de recursos realizado nos termos do art 6 \xa73 inciso III da Lei 11.079/2004'), (11, '11 - Demais ajustes oriundos da Legisla\xe7\xe3o Tribut\xe1ria, estorno ou outras situa\xe7\xf5es'), (2, '2 - Ajuste da CPRB: Diferimento de Valores a recolher no per\xedodo'), (3, '3 - Adi\xe7\xe3o de valores Diferidos em Per\xedodo(s) Anteriores(es)'), (4, '4 - Exporta\xe7\xf5es diretas'), (5, '5 - Transporte internacional de cargas'), (6, '6 - Vendas canceladas e os descontos incondicionais concedidos'), (7, '7 - IPI, se inclu\xeddo na receita bruta'), (8, '8 - ICMS, quando cobrado pelo vendedor dos bens ou prestador dos servi\xe7os na condi\xe7\xe3o de substituto tribut\xe1rio'), (9, '9 - Receita bruta reconhecida pela constru\xe7\xe3o, recupera\xe7\xe3o, reforma, amplia\xe7\xe3o ou melhoramento da infraestrutura, cuja contrapartida seja ativo intang\xedvel representativo de direito de explora\xe7\xe3o, no caso de contratos de concess\xe3o de servi\xe7os p\xfablicos')]),
        ),
    ]
