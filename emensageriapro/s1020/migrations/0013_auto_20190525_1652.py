# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-25 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1020', '0012_auto_20190514_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1020alteracao',
            name='codlotacao',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='s1020alteracao',
            name='codtercs',
            field=models.CharField(choices=[(b'507', '507 - 507'), (b'515', '515 - 515'), (b'523', '523 - 523'), (b'531', '531 - 531'), (b'540', '540 - 540'), (b'558', '558 - 558'), (b'566', '566 - 566'), (b'574', '574 - 574'), (b'582', '582 - 582'), (b'590', '590 - 590'), (b'604', '604 - 604'), (b'612', '612 - 612'), (b'620', '620 - 620'), (b'639', '639 - 639'), (b'647', '647 - 647'), (b'655', '655 - 655'), (b'680', '680 - 680'), (b'736', '736 - 736'), (b'744', '744 - 744'), (b'779', '779 - 779'), (b'787', '787 - 787'), (b'795', '795 - 795'), (b'825', '825 - 825'), (b'833', '833 - 833'), (b'868', '868 - 868'), (b'876', '876 - 876')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='s1020alteracao',
            name='fpas',
            field=models.IntegerField(choices=[(507, '507 - 507'), (515, '515 - 515'), (523, '523 - 523'), (531, '531 - 531'), (540, '540 - 540'), (558, '558 - 558'), (566, '566 - 566'), (574, '574 - 574'), (582, '582 - 582'), (590, '590 - 590'), (604, '604 - 604'), (612, '612 - 612'), (620, '620 - 620'), (639, '639 - 639'), (647, '647 - 647'), (655, '655 - 655'), (680, '680 - 680'), (736, '736 - 736'), (744, '744 - 744'), (779, '779 - 779'), (787, '787 - 787'), (795, '795 - 795'), (825, '825 - 825'), (833, '833 - 833'), (868, '868 - 868'), (876, '876 - 876')], null=True),
        ),
        migrations.AlterField(
            model_name='s1020alteracao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='s1020alteracao',
            name='tplotacao',
            field=models.CharField(choices=[(b'01', '01 - Classifica\xe7\xe3o da atividade econ\xf4mica exercida pela Pessoa Jur\xeddica para fins de atribui\xe7\xe3o de c\xf3digo FPAS, inclusive obras de constru\xe7\xe3o civil pr\xf3pria, exceto: a) empreitada parcial ou sub-empreitada de obra de constru\xe7\xe3o civil (utilizar op\xe7\xe3o 02), b) presta\xe7\xe3o de servi\xe7os em instala\xe7\xf5es de terceiros (utilizar op\xe7\xf5es 03 a 09), c) Embarca\xe7\xe3o inscrita no Registro Especial Brasileiro - REB (utilizar op\xe7\xe3o 10).'), (b'02', '02 - Obra de Constru\xe7\xe3o Civil - Empreitada Parcial ou Sub- empreitada'), (b'03', '03 - Pessoa F\xedsica Tomadora de Servi\xe7os prestados mediante cess\xe3o de m\xe3o de obra, exceto contratante de cooperativa'), (b'04', '04 - Pessoa Jur\xeddica Tomadora de Servi\xe7os prestados mediante cess\xe3o de m\xe3o de obra, exceto contratante de cooperativa, nos termos da lei 8.212/1991'), (b'05', '05 - Pessoa Jur\xeddica Tomadora de Servi\xe7os prestados por cooperados por interm\xe9dio de cooperativa de trabalho, exceto aqueles prestados a entidade beneficente/isenta'), (b'06', '06 - Entidade beneficente/isenta Tomadora de Servi\xe7os prestados por cooperados por interm\xe9dio de cooperativa de trabalho'), (b'07', '07 - Pessoa F\xedsica tomadora de Servi\xe7os prestados por Cooperados por interm\xe9dio de Cooperativa de Trabalho'), (b'08', '08 - Operador Portu\xe1rio tomador de servi\xe7os de trabalhadores avulsos'), (b'09', '09 - Contratante de trabalhadores avulsos n\xe3o portu\xe1rios por interm\xe9dio de Sindicato'), (b'10', '10 - Embarca\xe7\xe3o inscrita no Registro Especial Brasileiro - REB'), (b'21', '21 - Classifica\xe7\xe3o da atividade econ\xf4mica ou obra pr\xf3pria de constru\xe7\xe3o civil da Pessoa F\xedsica'), (b'24', '24 - Empregador Dom\xe9stico'), (b'90', '90 - Atividades desenvolvidas no exterior por trabalhador vinculado ao Regime Geral de Previd\xeancia Social (expatriados)'), (b'91', '91 - Atividades desenvolvidas por trabalhador estrangeiro vinculado a Regime de Previd\xeancia Social Estrangeiro')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='s1020alteracaoinfoemprparcial',
            name='nrinsccontrat',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='s1020alteracaoinfoemprparcial',
            name='nrinscprop',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='s1020alteracaoinfoemprparcial',
            name='tpinsccontrat',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF.')], null=True),
        ),
        migrations.AlterField(
            model_name='s1020alteracaoinfoemprparcial',
            name='tpinscprop',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='s1020alteracaonovavalidade',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='s1020alteracaoprocjudterceiro',
            name='codsusp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='s1020alteracaoprocjudterceiro',
            name='codterc',
            field=models.CharField(choices=[(b'507', '507 - 507'), (b'515', '515 - 515'), (b'523', '523 - 523'), (b'531', '531 - 531'), (b'540', '540 - 540'), (b'558', '558 - 558'), (b'566', '566 - 566'), (b'574', '574 - 574'), (b'582', '582 - 582'), (b'590', '590 - 590'), (b'604', '604 - 604'), (b'612', '612 - 612'), (b'620', '620 - 620'), (b'639', '639 - 639'), (b'647', '647 - 647'), (b'655', '655 - 655'), (b'680', '680 - 680'), (b'736', '736 - 736'), (b'744', '744 - 744'), (b'779', '779 - 779'), (b'787', '787 - 787'), (b'795', '795 - 795'), (b'825', '825 - 825'), (b'833', '833 - 833'), (b'868', '868 - 868'), (b'876', '876 - 876')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='s1020alteracaoprocjudterceiro',
            name='nrprocjud',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='s1020exclusao',
            name='codlotacao',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='s1020exclusao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='s1020inclusao',
            name='codlotacao',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='s1020inclusao',
            name='codtercs',
            field=models.CharField(choices=[(b'507', '507 - 507'), (b'515', '515 - 515'), (b'523', '523 - 523'), (b'531', '531 - 531'), (b'540', '540 - 540'), (b'558', '558 - 558'), (b'566', '566 - 566'), (b'574', '574 - 574'), (b'582', '582 - 582'), (b'590', '590 - 590'), (b'604', '604 - 604'), (b'612', '612 - 612'), (b'620', '620 - 620'), (b'639', '639 - 639'), (b'647', '647 - 647'), (b'655', '655 - 655'), (b'680', '680 - 680'), (b'736', '736 - 736'), (b'744', '744 - 744'), (b'779', '779 - 779'), (b'787', '787 - 787'), (b'795', '795 - 795'), (b'825', '825 - 825'), (b'833', '833 - 833'), (b'868', '868 - 868'), (b'876', '876 - 876')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='s1020inclusao',
            name='fpas',
            field=models.IntegerField(choices=[(507, '507 - 507'), (515, '515 - 515'), (523, '523 - 523'), (531, '531 - 531'), (540, '540 - 540'), (558, '558 - 558'), (566, '566 - 566'), (574, '574 - 574'), (582, '582 - 582'), (590, '590 - 590'), (604, '604 - 604'), (612, '612 - 612'), (620, '620 - 620'), (639, '639 - 639'), (647, '647 - 647'), (655, '655 - 655'), (680, '680 - 680'), (736, '736 - 736'), (744, '744 - 744'), (779, '779 - 779'), (787, '787 - 787'), (795, '795 - 795'), (825, '825 - 825'), (833, '833 - 833'), (868, '868 - 868'), (876, '876 - 876')], null=True),
        ),
        migrations.AlterField(
            model_name='s1020inclusao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='s1020inclusao',
            name='tplotacao',
            field=models.CharField(choices=[(b'01', '01 - Classifica\xe7\xe3o da atividade econ\xf4mica exercida pela Pessoa Jur\xeddica para fins de atribui\xe7\xe3o de c\xf3digo FPAS, inclusive obras de constru\xe7\xe3o civil pr\xf3pria, exceto: a) empreitada parcial ou sub-empreitada de obra de constru\xe7\xe3o civil (utilizar op\xe7\xe3o 02), b) presta\xe7\xe3o de servi\xe7os em instala\xe7\xf5es de terceiros (utilizar op\xe7\xf5es 03 a 09), c) Embarca\xe7\xe3o inscrita no Registro Especial Brasileiro - REB (utilizar op\xe7\xe3o 10).'), (b'02', '02 - Obra de Constru\xe7\xe3o Civil - Empreitada Parcial ou Sub- empreitada'), (b'03', '03 - Pessoa F\xedsica Tomadora de Servi\xe7os prestados mediante cess\xe3o de m\xe3o de obra, exceto contratante de cooperativa'), (b'04', '04 - Pessoa Jur\xeddica Tomadora de Servi\xe7os prestados mediante cess\xe3o de m\xe3o de obra, exceto contratante de cooperativa, nos termos da lei 8.212/1991'), (b'05', '05 - Pessoa Jur\xeddica Tomadora de Servi\xe7os prestados por cooperados por interm\xe9dio de cooperativa de trabalho, exceto aqueles prestados a entidade beneficente/isenta'), (b'06', '06 - Entidade beneficente/isenta Tomadora de Servi\xe7os prestados por cooperados por interm\xe9dio de cooperativa de trabalho'), (b'07', '07 - Pessoa F\xedsica tomadora de Servi\xe7os prestados por Cooperados por interm\xe9dio de Cooperativa de Trabalho'), (b'08', '08 - Operador Portu\xe1rio tomador de servi\xe7os de trabalhadores avulsos'), (b'09', '09 - Contratante de trabalhadores avulsos n\xe3o portu\xe1rios por interm\xe9dio de Sindicato'), (b'10', '10 - Embarca\xe7\xe3o inscrita no Registro Especial Brasileiro - REB'), (b'21', '21 - Classifica\xe7\xe3o da atividade econ\xf4mica ou obra pr\xf3pria de constru\xe7\xe3o civil da Pessoa F\xedsica'), (b'24', '24 - Empregador Dom\xe9stico'), (b'90', '90 - Atividades desenvolvidas no exterior por trabalhador vinculado ao Regime Geral de Previd\xeancia Social (expatriados)'), (b'91', '91 - Atividades desenvolvidas por trabalhador estrangeiro vinculado a Regime de Previd\xeancia Social Estrangeiro')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='s1020inclusaoinfoemprparcial',
            name='nrinsccontrat',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='s1020inclusaoinfoemprparcial',
            name='nrinscprop',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='s1020inclusaoinfoemprparcial',
            name='tpinsccontrat',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF.')], null=True),
        ),
        migrations.AlterField(
            model_name='s1020inclusaoinfoemprparcial',
            name='tpinscprop',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='s1020inclusaoprocjudterceiro',
            name='codsusp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='s1020inclusaoprocjudterceiro',
            name='codterc',
            field=models.CharField(choices=[(b'507', '507 - 507'), (b'515', '515 - 515'), (b'523', '523 - 523'), (b'531', '531 - 531'), (b'540', '540 - 540'), (b'558', '558 - 558'), (b'566', '566 - 566'), (b'574', '574 - 574'), (b'582', '582 - 582'), (b'590', '590 - 590'), (b'604', '604 - 604'), (b'612', '612 - 612'), (b'620', '620 - 620'), (b'639', '639 - 639'), (b'647', '647 - 647'), (b'655', '655 - 655'), (b'680', '680 - 680'), (b'736', '736 - 736'), (b'744', '744 - 744'), (b'779', '779 - 779'), (b'787', '787 - 787'), (b'795', '795 - 795'), (b'825', '825 - 825'), (b'833', '833 - 833'), (b'868', '868 - 868'), (b'876', '876 - 876')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='s1020inclusaoprocjudterceiro',
            name='nrprocjud',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
