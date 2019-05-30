# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-30 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1000', '0015_auto_20190525_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1000alteracao',
            name='classtrib',
            field=models.CharField(choices=[(b'01', '01 - Empresa enquadrada no regime de tributa\xe7\xe3o Simples Nacional com tributa\xe7\xe3o previdenci\xe1ria substitu\xedda'), (b'02', '02 - Empresa enquadrada no regime de tributa\xe7\xe3o Simples Nacional com tributa\xe7\xe3o previdenci\xe1ria n\xe3o substitu\xedda'), (b'03', '03 - Empresa enquadrada no regime de tributa\xe7\xe3o Simples Nacional com tributa\xe7\xe3o previdenci\xe1ria substitu\xedda e n\xe3o substitu\xedda'), (b'04', '04 - MEI - Micro Empreendedor Individual'), (b'06', '06 - Agroind\xfastria'), (b'07', '07 - Produtor Rural Pessoa Jur\xeddica'), (b'08', '08 - Cons\xf3rcio Simplificado de Produtores Rurais'), (b'09', '09 - \xd3rg\xe3o Gestor de M\xe3o de Obra'), (b'10', '10 - Entidade Sindical a que se refere a Lei 12.023/2009'), (b'11', '11 - Associa\xe7\xe3o Desportiva que mant\xe9m Clube de Futebol Profissional'), (b'13', '13 - Banco, caixa econ\xf4mica, sociedade de cr\xe9dito, financiamento e investimento e demais empresas relacionadas no par\xe1grafo 1\xba do art. 22 da Lei 8.212./91'), (b'14', '14 - Sindicatos em geral, exceto aquele classificado no c\xf3digo [10]'), (b'21', '21 - Pessoa F\xedsica, exceto Segurado Especial'), (b'22', '22 - Segurado Especial, inclusive quando for empregador dom\xe9stico'), (b'60', '60 - Miss\xe3o Diplom\xe1tica ou Reparti\xe7\xe3o Consular de carreira estrangeira'), (b'70', '70 - Empresa de que trata o Decreto 5.436/2005'), (b'80', '80 - Entidade Beneficente de Assist\xeancia Social isenta de contribui\xe7\xf5es sociais'), (b'85', '85 - Administra\xe7\xe3o Direta da Uni\xe3o, Estados, Distrito Federal e Munic\xedp\xedos, Autarquias e Funda\xe7\xf5es P\xfablicas'), (b'99', '99 - Pessoas Jur\xeddicas em Geral')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusao',
            name='classtrib',
            field=models.CharField(choices=[(b'01', '01 - Empresa enquadrada no regime de tributa\xe7\xe3o Simples Nacional com tributa\xe7\xe3o previdenci\xe1ria substitu\xedda'), (b'02', '02 - Empresa enquadrada no regime de tributa\xe7\xe3o Simples Nacional com tributa\xe7\xe3o previdenci\xe1ria n\xe3o substitu\xedda'), (b'03', '03 - Empresa enquadrada no regime de tributa\xe7\xe3o Simples Nacional com tributa\xe7\xe3o previdenci\xe1ria substitu\xedda e n\xe3o substitu\xedda'), (b'04', '04 - MEI - Micro Empreendedor Individual'), (b'06', '06 - Agroind\xfastria'), (b'07', '07 - Produtor Rural Pessoa Jur\xeddica'), (b'08', '08 - Cons\xf3rcio Simplificado de Produtores Rurais'), (b'09', '09 - \xd3rg\xe3o Gestor de M\xe3o de Obra'), (b'10', '10 - Entidade Sindical a que se refere a Lei 12.023/2009'), (b'11', '11 - Associa\xe7\xe3o Desportiva que mant\xe9m Clube de Futebol Profissional'), (b'13', '13 - Banco, caixa econ\xf4mica, sociedade de cr\xe9dito, financiamento e investimento e demais empresas relacionadas no par\xe1grafo 1\xba do art. 22 da Lei 8.212./91'), (b'14', '14 - Sindicatos em geral, exceto aquele classificado no c\xf3digo [10]'), (b'21', '21 - Pessoa F\xedsica, exceto Segurado Especial'), (b'22', '22 - Segurado Especial, inclusive quando for empregador dom\xe9stico'), (b'60', '60 - Miss\xe3o Diplom\xe1tica ou Reparti\xe7\xe3o Consular de carreira estrangeira'), (b'70', '70 - Empresa de que trata o Decreto 5.436/2005'), (b'80', '80 - Entidade Beneficente de Assist\xeancia Social isenta de contribui\xe7\xf5es sociais'), (b'85', '85 - Administra\xe7\xe3o Direta da Uni\xe3o, Estados, Distrito Federal e Munic\xedp\xedos, Autarquias e Funda\xe7\xf5es P\xfablicas'), (b'99', '99 - Pessoas Jur\xeddicas em Geral')], max_length=2, null=True),
        ),
    ]
