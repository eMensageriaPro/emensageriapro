# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 21:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tabelas', '0016_auto_20190204_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='cbo',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cbo_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cbo',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cbo_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cid',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cid_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cid',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cid_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cnae',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cnae_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cnae',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cnae_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfclassificacaoservicosprestados',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfclassificacaoservicosprestados_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfclassificacaoservicosprestados',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfclassificacaoservicosprestados_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfclassificacaotributaria',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfclassificacaotributaria_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfclassificacaotributaria',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfclassificacaotributaria_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfcodigosatividadesprodutosservicoscprb',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfcodigosatividadesprodutosservicoscprb_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfcodigosatividadesprodutosservicoscprb',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfcodigosatividadesprodutosservicoscprb_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfeventos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfeventos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfeventos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfeventos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfinformacoesbeneficiariosexterior',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfinformacoesbeneficiariosexterior_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfinformacoesbeneficiariosexterior',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfinformacoesbeneficiariosexterior_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfpagamentoscodigos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfpagamentoscodigos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfpagamentoscodigos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfpagamentoscodigos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfpaises',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfpaises_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfpaises',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfpaises_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfregraspagamentoscodigos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfregraspagamentoscodigos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfregraspagamentoscodigos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfregraspagamentoscodigos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfrendimentosbeneficiariosexterior',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfrendimentosbeneficiariosexterior_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfrendimentosbeneficiariosexterior',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfrendimentosbeneficiariosexterior_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfrendimentosbeneficiariosexteriortributacao',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfrendimentosbeneficiariosexteriortributacao_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='efdreinfrendimentosbeneficiariosexteriortributacao',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='efdreinfrendimentosbeneficiariosexteriortributacao_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialacidentessituacoesgeradoras',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialacidentessituacoesgeradoras_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialacidentessituacoesgeradoras',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialacidentessituacoesgeradoras_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialafastamentosmotivos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialafastamentosmotivos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialafastamentosmotivos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialafastamentosmotivos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialagentescausadoresacidentestrabalho',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialagentescausadoresacidentestrabalho_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialagentescausadoresacidentestrabalho',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialagentescausadoresacidentestrabalho_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialagentescausadoresdoencasprofissionais',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialagentescausadoresdoencasprofissionais_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialagentescausadoresdoencasprofissionais',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialagentescausadoresdoencasprofissionais_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialarquivosesocialtipos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialarquivosesocialtipos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialarquivosesocialtipos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialarquivosesocialtipos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialatividadespericulosasinsalubresespeciais',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialatividadespericulosasinsalubresespeciais_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialatividadespericulosasinsalubresespeciais',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialatividadespericulosasinsalubresespeciais_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialbeneficiosprevidenciarioscessacaomotivos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialbeneficiosprevidenciarioscessacaomotivos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialbeneficiosprevidenciarioscessacaomotivos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialbeneficiosprevidenciarioscessacaomotivos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialbeneficiosprevidenciariostipos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialbeneficiosprevidenciariostipos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialbeneficiosprevidenciariostipos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialbeneficiosprevidenciariostipos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialclassificacoestributarias',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialclassificacoestributarias_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialclassificacoestributarias',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialclassificacoestributarias_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialcodificacoesacidentetrabalho',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialcodificacoesacidentetrabalho_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialcodificacoesacidentetrabalho',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialcodificacoesacidentetrabalho_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialcodigoaliquotasfpasterceiros',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialcodigoaliquotasfpasterceiros_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialcodigoaliquotasfpasterceiros',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialcodigoaliquotasfpasterceiros_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialcompatibilidadescategoriasclassificacoeslotacoes',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialcompatibilidadescategoriasclassificacoeslotacoes_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialcompatibilidadescategoriasclassificacoeslotacoes',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialcompatibilidadescategoriasclassificacoeslotacoes_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialcompatibilidadesfpasclassificacoestributarias',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialcompatibilidadesfpasclassificacoestributarias_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialcompatibilidadesfpasclassificacoestributarias',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialcompatibilidadesfpasclassificacoestributarias_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialcompatibilidadeslotacoesclassificacoes',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialcompatibilidadeslotacoesclassificacoes_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialcompatibilidadeslotacoesclassificacoes',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialcompatibilidadeslotacoesclassificacoes_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialdependentestipos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialdependentestipos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialdependentestipos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialdependentestipos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialdesligamentosmotivos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialdesligamentosmotivos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialdesligamentosmotivos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialdesligamentosmotivos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialfatoresrisco',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialfatoresrisco_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialfatoresrisco',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialfatoresrisco_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialfinanciamentosaposentadoriasespeciais',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialfinanciamentosaposentadoriasespeciais_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialfinanciamentosaposentadoriasespeciais',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialfinanciamentosaposentadoriasespeciais_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialinscricoestipos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialinscricoestipos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialinscricoestipos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialinscricoestipos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esociallogradourostipos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esociallogradourostipos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esociallogradourostipos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esociallogradourostipos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esociallotacoestributariastipos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esociallotacoestributariastipos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esociallotacoestributariastipos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esociallotacoestributariastipos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialnaturezasjuridicas',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialnaturezasjuridicas_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialnaturezasjuridicas',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialnaturezasjuridicas_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialnaturezaslesoes',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialnaturezaslesoes_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialnaturezaslesoes',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialnaturezaslesoes_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialnaturezasrubricas',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialnaturezasrubricas_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialnaturezasrubricas',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialnaturezasrubricas_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialpaises',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialpaises_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialpaises',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialpaises_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialpartescorpoatingidas',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialpartescorpoatingidas_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialpartescorpoatingidas',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialpartescorpoatingidas_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialprocedimentosdiagnosticos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialprocedimentosdiagnosticos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialprocedimentosdiagnosticos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialprocedimentosdiagnosticos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialprogramasplanosdocumentos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialprogramasplanosdocumentos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialprogramasplanosdocumentos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialprogramasplanosdocumentos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialtrabalhadorescategorias',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialtrabalhadorescategorias_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialtrabalhadorescategorias',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialtrabalhadorescategorias_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialtreinamentoscapacitacoesexerciciossimulados',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialtreinamentoscapacitacoesexerciciossimulados_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esocialtreinamentoscapacitacoesexerciciossimulados',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esocialtreinamentoscapacitacoesexerciciossimulados_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='municipios',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='municipios_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='municipios',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='municipios_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
    ]
