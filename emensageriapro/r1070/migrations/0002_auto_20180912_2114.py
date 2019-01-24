# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r1070', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r1070alteracaoinfosusp',
            name='indsusp',
            field=models.CharField(max_length=2, choices=[(b'01', '01 - Liminar em Mandado de Seguran\xe7a'), (b'02', '02 - Dep\xf3sito Judicial do Montante Integral'), (b'03', '03 - Dep\xf3sito Administrativo do Montante Integral'), (b'04', '04 - Antecipa\xe7\xe3o de Tutela'), (b'05', '05 - Liminar em Medida Cautelar'), (b'08', '08 - Senten\xe7a em Mandado de Seguran\xe7a Favor\xe1vel ao Contribuinte'), (b'09', '09 - Senten\xe7a em A\xe7\xe3o Ordin\xe1ria Favor\xe1vel ao Contribuinte e Confirmada pelo TRF'), (b'10', '10 - Ac\xf3rd\xe3o do TRF Favor\xe1vel ao Contribuinte'), (b'11', '11 - Ac\xf3rd\xe3o do STJ em Recurso Especial Favor\xe1vel ao Contribuinte'), (b'12', '12 - Ac\xf3rd\xe3o do STF em Recurso Extraordin\xe1rio Favor\xe1vel ao Contribuinte'), (b'13', '13 - Senten\xe7a 1\xaa inst\xe2ncia n\xe3o transitada em julgado com efeito suspensivo'), (b'90', '90 - Decis\xe3o Definitiva a favor do contribuinte'), (b'92', '92 - Sem suspens\xe3o da exigibilidade')]),
        ),
        migrations.AlterField(
            model_name='r1070inclusaoinfosusp',
            name='indsusp',
            field=models.CharField(max_length=2, choices=[(b'01', '01 - Liminar em Mandado de Seguran\xe7a'), (b'02', '02 - Dep\xf3sito Judicial do Montante Integral'), (b'03', '03 - Dep\xf3sito Administrativo do Montante Integral'), (b'04', '04 - Antecipa\xe7\xe3o de Tutela'), (b'05', '05 - Liminar em Medida Cautelar'), (b'08', '08 - Senten\xe7a em Mandado de Seguran\xe7a Favor\xe1vel ao Contribuinte'), (b'09', '09 - Senten\xe7a em A\xe7\xe3o Ordin\xe1ria Favor\xe1vel ao Contribuinte e Confirmada pelo TRF'), (b'10', '10 - Ac\xf3rd\xe3o do TRF Favor\xe1vel ao Contribuinte'), (b'11', '11 - Ac\xf3rd\xe3o do STJ em Recurso Especial Favor\xe1vel ao Contribuinte'), (b'12', '12 - Ac\xf3rd\xe3o do STF em Recurso Extraordin\xe1rio Favor\xe1vel ao Contribuinte'), (b'13', '13 - Senten\xe7a 1\xaa inst\xe2ncia n\xe3o transitada em julgado com efeito suspensivo'), (b'90', '90 - Decis\xe3o Definitiva a favor do contribuinte'), (b'92', '92 - Sem suspens\xe3o da exigibilidade')]),
        ),
    ]
