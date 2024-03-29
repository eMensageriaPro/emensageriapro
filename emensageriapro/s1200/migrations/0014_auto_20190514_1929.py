# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-14 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s1200', '0013_auto_20190513_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1200dmdev',
            name='codcateg',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='s1200dmdev',
            name='idedmdev',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='s1200dmdev',
            name='s1200_evtremun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200dmdev_s1200_evtremun', to='esocial.s1200evtRemun'),
        ),
        migrations.AlterField(
            model_name='s1200infocomplem',
            name='dtnascto',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='s1200infocomplem',
            name='nmtrab',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='s1200infocomplem',
            name='s1200_evtremun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infocomplem_s1200_evtremun', to='esocial.s1200evtRemun'),
        ),
        migrations.AlterField(
            model_name='s1200infointerm',
            name='qtddiasinterm',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s1200infointerm',
            name='s1200_evtremun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infointerm_s1200_evtremun', to='esocial.s1200evtRemun'),
        ),
        migrations.AlterField(
            model_name='s1200infomv',
            name='indmv',
            field=models.IntegerField(choices=[(1, '1 - O declarante aplica a al\xedquota de desconto do segurado sobre a remunera\xe7\xe3o por ele informada (o percentual da al\xedquota ser\xe1 obtido considerando a remunera\xe7\xe3o total do trabalhador)'), (2, '2 - O declarante aplica a al\xedquota de desconto do segurado sobre a diferen\xe7a entre o limite m\xe1ximo do sal\xe1rio de contribui\xe7\xe3o e a remunera\xe7\xe3o de outra(s) empresa(s) para as quais o trabalhador informou que houve o desconto'), (3, '3 - O declarante n\xe3o realiza desconto do segurado, uma vez que houve desconto sobre o limite m\xe1ximo de sal\xe1rio de contribui\xe7\xe3o em outra(s) empresa(s).')]),
        ),
        migrations.AlterField(
            model_name='s1200infomv',
            name='s1200_evtremun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infomv_s1200_evtremun', to='esocial.s1200evtRemun'),
        ),
        migrations.AlterField(
            model_name='s1200infoperant',
            name='s1200_dmdev',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperant_s1200_dmdev', to='s1200.s1200dmDev'),
        ),
        migrations.AlterField(
            model_name='s1200infoperantideadc',
            name='dsc',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='s1200infoperantideadc',
            name='remunsuc',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s1200infoperantideadc',
            name='s1200_infoperant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperantideadc_s1200_infoperant', to='s1200.s1200infoPerAnt'),
        ),
        migrations.AlterField(
            model_name='s1200infoperantideadc',
            name='tpacconv',
            field=models.CharField(choices=[(b'A', 'A - Acordo Coletivo de Trabalho'), (b'B', 'B - Legisla\xe7\xe3o federal, estadual, municipal ou distrital'), (b'C', 'C - Conven\xe7\xe3o Coletiva de Trabalho'), (b'D', 'D - Senten\xe7a Normativa - Diss\xeddio'), (b'E', 'E - Convers\xe3o de Licen\xe7a Sa\xfade em Acidente de Trabalho'), (b'F', 'F - Outras verbas de natureza salarial ou n\xe3o salarial devidas ap\xf3s o desligamento.')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s1200infoperantideestablot',
            name='codlotacao',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='s1200infoperantideestablot',
            name='nrinsc',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='s1200infoperantideestablot',
            name='s1200_infoperant_ideperiodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperantideestablot_s1200_infoperant_ideperiodo', to='s1200.s1200infoPerAntidePeriodo'),
        ),
        migrations.AlterField(
            model_name='s1200infoperantideestablot',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (5, '5 - CGC')]),
        ),
        migrations.AlterField(
            model_name='s1200infoperantideperiodo',
            name='perref',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='s1200infoperantideperiodo',
            name='s1200_infoperant_ideadc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperantideperiodo_s1200_infoperant_ideadc', to='s1200.s1200infoPerAntideADC'),
        ),
        migrations.AlterField(
            model_name='s1200infoperantinfoagnocivo',
            name='grauexp',
            field=models.IntegerField(choices=[(1, '1 - Na\u0303o ensejador de aposentadoria especial'), (2, '2 - Ensejador de Aposentadoria Especial - FAE15_12% (15 anos de contribuic\u0327a\u0303o e ali\u0301quota de 12%)'), (3, '3 - Ensejador de Aposentadoria Especial - FAE20_09% (20 anos de contribuic\u0327a\u0303o e ali\u0301quota de 9%)'), (4, '4 - Ensejador de Aposentadoria Especial - FAE25_06% (25 anos de contribuic\u0327a\u0303o e ali\u0301quota de 6%).')]),
        ),
        migrations.AlterField(
            model_name='s1200infoperantinfoagnocivo',
            name='s1200_infoperant_remunperant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperantinfoagnocivo_s1200_infoperant_remunperant', to='s1200.s1200infoPerAntremunPerAnt'),
        ),
        migrations.AlterField(
            model_name='s1200infoperantinfocomplcont',
            name='codcbo',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='s1200infoperantinfocomplcont',
            name='s1200_dmdev',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperantinfocomplcont_s1200_dmdev', to='s1200.s1200dmDev'),
        ),
        migrations.AlterField(
            model_name='s1200infoperantinfotrabinterm',
            name='codconv',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='s1200infoperantinfotrabinterm',
            name='s1200_infoperant_remunperant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperantinfotrabinterm_s1200_infoperant_remunperant', to='s1200.s1200infoPerAntremunPerAnt'),
        ),
        migrations.AlterField(
            model_name='s1200infoperantitensremun',
            name='codrubr',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='s1200infoperantitensremun',
            name='idetabrubr',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='s1200infoperantitensremun',
            name='s1200_infoperant_remunperant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperantitensremun_s1200_infoperant_remunperant', to='s1200.s1200infoPerAntremunPerAnt'),
        ),
        migrations.AlterField(
            model_name='s1200infoperantitensremun',
            name='vrrubr',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1200infoperantremunperant',
            name='s1200_infoperant_ideestablot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperantremunperant_s1200_infoperant_ideestablot', to='s1200.s1200infoPerAntideEstabLot'),
        ),
        migrations.AlterField(
            model_name='s1200infoperapur',
            name='s1200_dmdev',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperapur_s1200_dmdev', to='s1200.s1200dmDev'),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurdetoper',
            name='cnpjoper',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurdetoper',
            name='regans',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurdetoper',
            name='s1200_infoperapur_infosaudecolet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperapurdetoper_s1200_infoperapur_infosaudecolet', to='s1200.s1200infoPerApurinfoSaudeColet'),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurdetoper',
            name='vrpgtit',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurdetplano',
            name='dtnascto',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurdetplano',
            name='nmdep',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurdetplano',
            name='s1200_infoperapur_detoper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperapurdetplano_s1200_infoperapur_detoper', to='s1200.s1200infoPerApurdetOper'),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurdetplano',
            name='tpdep',
            field=models.CharField(choices=[(b'01', '01 - C\xf4njuge'), (b'02', '02 - Companheiro(a) com o(a) qual tenha filho ou viva h\xe1 mais de 5 (cinco) anos ou possua Declara\xe7\xe3o de Uni\xe3o Est\xe1vel'), (b'03', '03 - Filho(a) ou enteado(a)'), (b'04', '04 - Filho(a) ou enteado(a), universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xba grau'), (b'06', '06 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial'), (b'07', '07 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xb0 grau, do(a) qual detenha a guarda judicial'), (b'09', '09 - Pais, av\xf3s e bisav\xf3s'), (b'10', '10 - Menor pobre do qual detenha a guarda judicial'), (b'11', '11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador'), (b'12', '12 - Ex-c\xf4njuge'), (b'99', '99 - Agregado/Outros')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurdetplano',
            name='vlrpgdep',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurideestablot',
            name='codlotacao',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurideestablot',
            name='nrinsc',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurideestablot',
            name='s1200_infoperapur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperapurideestablot_s1200_infoperapur', to='s1200.s1200infoPerApur'),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurideestablot',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (5, '5 - CGC')]),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurinfoagnocivo',
            name='grauexp',
            field=models.IntegerField(choices=[(1, '1 - Na\u0303o ensejador de aposentadoria especial'), (2, '2 - Ensejador de Aposentadoria Especial - FAE15_12% (15 anos de contribuic\u0327a\u0303o e ali\u0301quota de 12%)'), (3, '3 - Ensejador de Aposentadoria Especial - FAE20_09% (20 anos de contribuic\u0327a\u0303o e ali\u0301quota de 9%)'), (4, '4 - Ensejador de Aposentadoria Especial - FAE25_06% (25 anos de contribuic\u0327a\u0303o e ali\u0301quota de 6%).')]),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurinfoagnocivo',
            name='s1200_infoperapur_remunperapur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperapurinfoagnocivo_s1200_infoperapur_remunperapur', to='s1200.s1200infoPerApurremunPerApur'),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurinfosaudecolet',
            name='s1200_infoperapur_remunperapur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperapurinfosaudecolet_s1200_infoperapur_remunperapur', to='s1200.s1200infoPerApurremunPerApur'),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurinfotrabinterm',
            name='codconv',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurinfotrabinterm',
            name='s1200_infoperapur_remunperapur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperapurinfotrabinterm_s1200_infoperapur_remunperapur', to='s1200.s1200infoPerApurremunPerApur'),
        ),
        migrations.AlterField(
            model_name='s1200infoperapuritensremun',
            name='codrubr',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='s1200infoperapuritensremun',
            name='idetabrubr',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='s1200infoperapuritensremun',
            name='s1200_infoperapur_remunperapur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperapuritensremun_s1200_infoperapur_remunperapur', to='s1200.s1200infoPerApurremunPerApur'),
        ),
        migrations.AlterField(
            model_name='s1200infoperapuritensremun',
            name='vrrubr',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurremunperapur',
            name='s1200_infoperapur_ideestablot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200infoperapurremunperapur_s1200_infoperapur_ideestablot', to='s1200.s1200infoPerApurideEstabLot'),
        ),
        migrations.AlterField(
            model_name='s1200procjudtrab',
            name='nrprocjud',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='s1200procjudtrab',
            name='s1200_evtremun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200procjudtrab_s1200_evtremun', to='esocial.s1200evtRemun'),
        ),
        migrations.AlterField(
            model_name='s1200procjudtrab',
            name='tptrib',
            field=models.IntegerField(choices=[(1, '1 - IRRF'), (2, '2 - Contribui\xe7\xf5es sociais do trabalhador'), (3, '3 - FGTS'), (4, '4 - Contribui\xe7\xe3o sindical.')]),
        ),
        migrations.AlterField(
            model_name='s1200remunoutrempr',
            name='codcateg',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='s1200remunoutrempr',
            name='nrinsc',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='s1200remunoutrempr',
            name='s1200_infomv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200remunoutrempr_s1200_infomv', to='s1200.s1200infoMV'),
        ),
        migrations.AlterField(
            model_name='s1200remunoutrempr',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (5, '5 - CGC')]),
        ),
        migrations.AlterField(
            model_name='s1200remunoutrempr',
            name='vlrremunoe',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1200sucessaovinc',
            name='cnpjempregant',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='s1200sucessaovinc',
            name='dtadm',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='s1200sucessaovinc',
            name='s1200_infocomplem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1200sucessaovinc_s1200_infocomplem', to='s1200.s1200infoComplem'),
        ),
        migrations.AlterField(
            model_name='s1200sucessaovinc',
            name='tpinscant',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (5, '5 - CGC')]),
        ),
    ]
