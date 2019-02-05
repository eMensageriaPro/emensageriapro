# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabelas', '0015_auto_20190204_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cbo',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='cbo',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='cid',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='cid',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='cnae',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='cnae',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfclassificacaoservicosprestados',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfclassificacaoservicosprestados',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfclassificacaotributaria',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfclassificacaotributaria',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfcodigosatividadesprodutosservicoscprb',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfcodigosatividadesprodutosservicoscprb',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfeventos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfeventos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfinformacoesbeneficiariosexterior',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfinformacoesbeneficiariosexterior',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfpagamentoscodigos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfpagamentoscodigos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfpaises',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfpaises',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfregraspagamentoscodigos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfregraspagamentoscodigos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfrendimentosbeneficiariosexterior',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfrendimentosbeneficiariosexterior',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfrendimentosbeneficiariosexteriortributacao',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='efdreinfrendimentosbeneficiariosexteriortributacao',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialacidentessituacoesgeradoras',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialacidentessituacoesgeradoras',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialafastamentosmotivos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialafastamentosmotivos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialagentescausadoresacidentestrabalho',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialagentescausadoresacidentestrabalho',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialagentescausadoresdoencasprofissionais',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialagentescausadoresdoencasprofissionais',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialarquivosesocialtipos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialarquivosesocialtipos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialatividadespericulosasinsalubresespeciais',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialatividadespericulosasinsalubresespeciais',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialbeneficiosprevidenciarioscessacaomotivos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialbeneficiosprevidenciarioscessacaomotivos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialbeneficiosprevidenciariostipos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialbeneficiosprevidenciariostipos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialclassificacoestributarias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialclassificacoestributarias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialcodificacoesacidentetrabalho',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialcodificacoesacidentetrabalho',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialcodigoaliquotasfpasterceiros',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialcodigoaliquotasfpasterceiros',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialcompatibilidadescategoriasclassificacoeslotacoes',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialcompatibilidadescategoriasclassificacoeslotacoes',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialcompatibilidadesfpasclassificacoestributarias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialcompatibilidadesfpasclassificacoestributarias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialcompatibilidadeslotacoesclassificacoes',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialcompatibilidadeslotacoesclassificacoes',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialdependentestipos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialdependentestipos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialdesligamentosmotivos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialdesligamentosmotivos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialfatoresrisco',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialfatoresrisco',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialfinanciamentosaposentadoriasespeciais',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialfinanciamentosaposentadoriasespeciais',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialinscricoestipos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialinscricoestipos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esociallogradourostipos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esociallogradourostipos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esociallotacoestributariastipos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esociallotacoestributariastipos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialnaturezasjuridicas',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialnaturezasjuridicas',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialnaturezaslesoes',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialnaturezaslesoes',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialnaturezasrubricas',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialnaturezasrubricas',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialpaises',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialpaises',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialpartescorpoatingidas',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialpartescorpoatingidas',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialprocedimentosdiagnosticos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialprocedimentosdiagnosticos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialprogramasplanosdocumentos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialprogramasplanosdocumentos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialtrabalhadorescategorias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialtrabalhadorescategorias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='esocialtreinamentoscapacitacoesexerciciossimulados',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='esocialtreinamentoscapacitacoesexerciciossimulados',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='municipios',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='municipios',
            name='modificado_por',
        ),
        migrations.AlterField(
            model_name='cbo',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cbo',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cid',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cid',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cnae',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cnae',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfclassificacaoservicosprestados',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfclassificacaoservicosprestados',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfclassificacaotributaria',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfclassificacaotributaria',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfcodigosatividadesprodutosservicoscprb',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfcodigosatividadesprodutosservicoscprb',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfeventos',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfeventos',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfinformacoesbeneficiariosexterior',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfinformacoesbeneficiariosexterior',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfpagamentoscodigos',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfpagamentoscodigos',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfpaises',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfpaises',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfregraspagamentoscodigos',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfregraspagamentoscodigos',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfrendimentosbeneficiariosexterior',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfrendimentosbeneficiariosexterior',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfrendimentosbeneficiariosexteriortributacao',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='efdreinfrendimentosbeneficiariosexteriortributacao',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialacidentessituacoesgeradoras',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialacidentessituacoesgeradoras',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialafastamentosmotivos',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialafastamentosmotivos',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialagentescausadoresacidentestrabalho',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialagentescausadoresacidentestrabalho',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialagentescausadoresdoencasprofissionais',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialagentescausadoresdoencasprofissionais',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialarquivosesocialtipos',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialarquivosesocialtipos',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialatividadespericulosasinsalubresespeciais',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialatividadespericulosasinsalubresespeciais',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialbeneficiosprevidenciarioscessacaomotivos',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialbeneficiosprevidenciarioscessacaomotivos',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialbeneficiosprevidenciariostipos',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialbeneficiosprevidenciariostipos',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialclassificacoestributarias',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialclassificacoestributarias',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialcodificacoesacidentetrabalho',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialcodificacoesacidentetrabalho',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialcodigoaliquotasfpasterceiros',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialcodigoaliquotasfpasterceiros',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialcompatibilidadescategoriasclassificacoeslotacoes',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialcompatibilidadescategoriasclassificacoeslotacoes',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialcompatibilidadesfpasclassificacoestributarias',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialcompatibilidadesfpasclassificacoestributarias',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialcompatibilidadeslotacoesclassificacoes',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialcompatibilidadeslotacoesclassificacoes',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialdependentestipos',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialdependentestipos',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialdesligamentosmotivos',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialdesligamentosmotivos',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialfatoresrisco',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialfatoresrisco',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialfinanciamentosaposentadoriasespeciais',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialfinanciamentosaposentadoriasespeciais',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialinscricoestipos',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialinscricoestipos',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esociallogradourostipos',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esociallogradourostipos',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esociallotacoestributariastipos',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esociallotacoestributariastipos',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialnaturezasjuridicas',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialnaturezasjuridicas',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialnaturezaslesoes',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialnaturezaslesoes',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialnaturezasrubricas',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialnaturezasrubricas',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialpaises',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialpaises',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialpartescorpoatingidas',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialpartescorpoatingidas',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialprocedimentosdiagnosticos',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialprocedimentosdiagnosticos',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialprogramasplanosdocumentos',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialprogramasplanosdocumentos',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialtrabalhadorescategorias',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialtrabalhadorescategorias',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialtreinamentoscapacitacoesexerciciossimulados',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esocialtreinamentoscapacitacoesexerciciossimulados',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='municipios',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='municipios',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
