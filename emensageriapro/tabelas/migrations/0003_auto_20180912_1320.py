# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabelas', '0002_auto_20180910_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acidentessituacoesgeradoras',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='acidentessituacoesgeradoras',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='afastamentosmotivos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='afastamentosmotivos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='agentescausadoresacidentestrabalho',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='agentescausadoresacidentestrabalho',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='agentescausadoresdoencasprofissionais',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='agentescausadoresdoencasprofissionais',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='arquivosesocialtipos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='arquivosesocialtipos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='atividadespericulosasinsalubresespeciais',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='atividadespericulosasinsalubresespeciais',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='beneficiosprevidenciarioscessacaomotivos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='beneficiosprevidenciarioscessacaomotivos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='beneficiosprevidenciariostipos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='beneficiosprevidenciariostipos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='classificacaoservicosprestados',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='classificacaoservicosprestados',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='classificacaotributaria',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='classificacaotributaria',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='classificacoestributarias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='classificacoestributarias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='codificacoesacidentetrabalho',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='codificacoesacidentetrabalho',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='codigoaliquotasfpasterceiros',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='codigoaliquotasfpasterceiros',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='codigosatividadesprodutosservicoscprb',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='codigosatividadesprodutosservicoscprb',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='compatibilidadescategoriasclassificacoeslotacoes',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='compatibilidadescategoriasclassificacoeslotacoes',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='compatibilidadesfpasclassificacoestributarias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='compatibilidadesfpasclassificacoestributarias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='compatibilidadeslotacoesclassificacoes',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='compatibilidadeslotacoesclassificacoes',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='dependentestipos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='dependentestipos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='desligamentosmotivos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='desligamentosmotivos',
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
            model_name='fatoresrisco',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='fatoresrisco',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='financiamentosaposentadoriasespeciais',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='financiamentosaposentadoriasespeciais',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='informacoesbeneficiariosexterior',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='informacoesbeneficiariosexterior',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='inscricoestipos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='inscricoestipos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='logradourostipos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='logradourostipos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='lotacoestributariastipos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='lotacoestributariastipos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='naturezasjuridicas',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='naturezasjuridicas',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='naturezaslesoes',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='naturezaslesoes',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='naturezasrubricas',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='naturezasrubricas',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='pagamentoscodigos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='pagamentoscodigos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='paises',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='paises',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='partescorpoatingidas',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='partescorpoatingidas',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='procedimentosdiagnosticos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='procedimentosdiagnosticos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='programasplanosdocumentos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='programasplanosdocumentos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='regraspagamentoscodigos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='regraspagamentoscodigos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='rendimentosbeneficiariosexterior',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='rendimentosbeneficiariosexterior',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='rendimentosbeneficiariosexteriortributacao',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='rendimentosbeneficiariosexteriortributacao',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='trabalhadorescategorias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='trabalhadorescategorias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='treinamentoscapacitacoesexerciciossimulados',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='treinamentoscapacitacoesexerciciossimulados',
            name='modificado_por',
        ),
        migrations.DeleteModel(
            name='AcidentesSituacoesGeradoras',
        ),
        migrations.DeleteModel(
            name='AfastamentosMotivos',
        ),
        migrations.DeleteModel(
            name='AgentesCausadoresAcidentesTrabalho',
        ),
        migrations.DeleteModel(
            name='AgentesCausadoresDoencasProfissionais',
        ),
        migrations.DeleteModel(
            name='ArquivosEsocialTipos',
        ),
        migrations.DeleteModel(
            name='AtividadesPericulosasInsalubresEspeciais',
        ),
        migrations.DeleteModel(
            name='BeneficiosPrevidenciariosCessacaoMotivos',
        ),
        migrations.DeleteModel(
            name='BeneficiosPrevidenciariosTipos',
        ),
        migrations.DeleteModel(
            name='ClassificacaoServicosPrestados',
        ),
        migrations.DeleteModel(
            name='ClassificacaoTributaria',
        ),
        migrations.DeleteModel(
            name='ClassificacoesTributarias',
        ),
        migrations.DeleteModel(
            name='CodificacoesAcidenteTrabalho',
        ),
        migrations.DeleteModel(
            name='CodigoAliquotasFPASTerceiros',
        ),
        migrations.DeleteModel(
            name='CodigosAtividadesProdutosServicosCPRB',
        ),
        migrations.DeleteModel(
            name='CompatibilidadesCategoriasClassificacoesLotacoes',
        ),
        migrations.DeleteModel(
            name='CompatibilidadesFPASClassificacoesTributarias',
        ),
        migrations.DeleteModel(
            name='CompatibilidadesLotacoesClassificacoes',
        ),
        migrations.DeleteModel(
            name='DependentesTipos',
        ),
        migrations.DeleteModel(
            name='DesligamentosMotivos',
        ),
        migrations.DeleteModel(
            name='EFDReinfEventos',
        ),
        migrations.DeleteModel(
            name='FatoresRisco',
        ),
        migrations.DeleteModel(
            name='FinanciamentosAposentadoriasEspeciais',
        ),
        migrations.DeleteModel(
            name='InformacoesBeneficiariosExterior',
        ),
        migrations.DeleteModel(
            name='InscricoesTipos',
        ),
        migrations.DeleteModel(
            name='LogradourosTipos',
        ),
        migrations.DeleteModel(
            name='LotacoesTributariasTipos',
        ),
        migrations.DeleteModel(
            name='NaturezasJuridicas',
        ),
        migrations.DeleteModel(
            name='NaturezasLesoes',
        ),
        migrations.DeleteModel(
            name='NaturezasRubricas',
        ),
        migrations.DeleteModel(
            name='PagamentosCodigos',
        ),
        migrations.DeleteModel(
            name='Paises',
        ),
        migrations.DeleteModel(
            name='PartesCorpoAtingidas',
        ),
        migrations.DeleteModel(
            name='ProcedimentosDiagnosticos',
        ),
        migrations.DeleteModel(
            name='ProgramasPlanosDocumentos',
        ),
        migrations.DeleteModel(
            name='RegrasPagamentosCodigos',
        ),
        migrations.DeleteModel(
            name='RendimentosBeneficiariosExterior',
        ),
        migrations.DeleteModel(
            name='RendimentosBeneficiariosExteriorTributacao',
        ),
        migrations.DeleteModel(
            name='TrabalhadoresCategorias',
        ),
        migrations.DeleteModel(
            name='TreinamentosCapacitacoesExerciciosSimulados',
        ),
    ]