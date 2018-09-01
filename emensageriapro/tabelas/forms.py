# coding: utf-8
from django import forms
from emensageriapro.tabelas.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_efdreinf_eventos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_efdreinf_eventos,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = EFDReinfEventos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_codigos_atividades_produtos_servicos_cprb(forms.ModelForm):
    aliquota = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_codigos_atividades_produtos_servicos_cprb,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        
        self.fields['grupo'].widget.attrs['required'] = True

    class Meta:
        model = CodigosAtividadesProdutosServicosCPRB
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_classificacao_tributaria(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_classificacao_tributaria,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = ClassificacaoTributaria
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_classificacao_servicos_prestados(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_classificacao_servicos_prestados,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = ClassificacaoServicosPrestados
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_informacoes_beneficiarios_exterior(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_informacoes_beneficiarios_exterior,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = InformacoesBeneficiariosExterior
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_rendimentos_beneficiarios_exterior_tributacao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_rendimentos_beneficiarios_exterior_tributacao,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = RendimentosBeneficiariosExteriorTributacao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_rendimentos_beneficiarios_exterior(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_rendimentos_beneficiarios_exterior,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = RendimentosBeneficiariosExterior
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_regras_pagamentos_codigos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_regras_pagamentos_codigos,self ).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True
        
        self.fields['classificacao'].widget.attrs['required'] = True

    class Meta:
        model = RegrasPagamentosCodigos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_pagamentos_codigos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_pagamentos_codigos,self ).__init__(*args,**kwargs)
        
        self.fields['beneficiario_pf'].widget.attrs['required'] = True
        
        self.fields['beneficiario_pj'].widget.attrs['required'] = True
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        
        self.fields['grupo'].widget.attrs['required'] = True

    class Meta:
        model = PagamentosCodigos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_programas_planos_documentos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_programas_planos_documentos,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = ProgramasPlanosDocumentos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_treinamentos_capacitacoes_exercicios_simulados(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_treinamentos_capacitacoes_exercicios_simulados,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = TreinamentosCapacitacoesExerciciosSimulados
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_atividades_periculosas_insalubres_especiais(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_atividades_periculosas_insalubres_especiais,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        
        self.fields['grupo'].widget.attrs['required'] = True

    class Meta:
        model = AtividadesPericulosasInsalubresEspeciais
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_procedimentos_diagnosticos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_procedimentos_diagnosticos,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = ProcedimentosDiagnosticos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_beneficios_previdenciarios_cessacao_motivos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_beneficios_previdenciarios_cessacao_motivos,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = BeneficiosPrevidenciariosCessacaoMotivos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_beneficios_previdenciarios_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_beneficios_previdenciarios_tipos,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = BeneficiosPrevidenciariosTipos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_codificacoes_acidente_trabalho(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_codificacoes_acidente_trabalho,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = CodificacoesAcidenteTrabalho
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_fatores_risco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_fatores_risco,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        
        self.fields['grupo'].widget.attrs['required'] = True

    class Meta:
        model = FatoresRisco
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_compatibilidades_fpas_classificacoes_tributarias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_compatibilidades_fpas_classificacoes_tributarias,self ).__init__(*args,**kwargs)
        
        self.fields['classificacao_tributaria_99'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_85'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_80'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_70'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_60'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_22'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_21'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_14'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_13'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_11'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_10'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_09'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_08'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_07'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_06'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_04'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_03'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_02'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria_01'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = CompatibilidadesFPASClassificacoesTributarias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_naturezas_juridicas(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_naturezas_juridicas,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        
        self.fields['grupo'].widget.attrs['required'] = True

    class Meta:
        model = NaturezasJuridicas
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_logradouros_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_logradouros_tipos,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = LogradourosTipos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_desligamentos_motivos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_desligamentos_motivos,self ).__init__(*args,**kwargs)
        
        self.fields['data_termino'].widget.attrs['required'] = True
        
        self.fields['data_inicio'].widget.attrs['required'] = True
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = DesligamentosMotivos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_afastamentos_motivos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_afastamentos_motivos,self ).__init__(*args,**kwargs)
        
        self.fields['data_termino'].widget.attrs['required'] = True
        
        self.fields['data_inicio'].widget.attrs['required'] = True
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = AfastamentosMotivos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_naturezas_lesoes(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_naturezas_lesoes,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = NaturezasLesoes
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_acidentes_situacoes_geradoras(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_acidentes_situacoes_geradoras,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = AcidentesSituacoesGeradoras
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_agentes_causadores_doencas_profissionais(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_agentes_causadores_doencas_profissionais,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = AgentesCausadoresDoencasProfissionais
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_agentes_causadores_acidentes_trabalho(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_agentes_causadores_acidentes_trabalho,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = AgentesCausadoresAcidentesTrabalho
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_partes_corpo_atingidas(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_partes_corpo_atingidas,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = PartesCorpoAtingidas
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_compatibilidades_lotacoes_classificacoes(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_compatibilidades_lotacoes_classificacoes,self ).__init__(*args,**kwargs)
        
        self.fields['tipo_classificacao_tributaria_99'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_85'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_80'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_70'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_60'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_22'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_21'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_14'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_13'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_11'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_10'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_09'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_08'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_07'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_06'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_04'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_03'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_02'].widget.attrs['required'] = True
        
        self.fields['tipo_classificacao_tributaria_01'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = CompatibilidadesLotacoesClassificacoes
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_compatibilidades_categorias_classificacoes_lotacoes(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_compatibilidades_categorias_classificacoes_lotacoes,self ).__init__(*args,**kwargs)
        
        self.fields['tipo_lotacao_tributaria_91'].widget.attrs['required'] = True
        
        self.fields['tipo_lotacao_tributaria_90'].widget.attrs['required'] = True
        
        self.fields['tipo_lotacao_tributaria_24'].widget.attrs['required'] = True
        
        self.fields['tipo_lotacao_tributaria_21'].widget.attrs['required'] = True
        
        self.fields['tipo_lotacao_tributaria_10'].widget.attrs['required'] = True
        
        self.fields['tipo_lotacao_tributaria_09'].widget.attrs['required'] = True
        
        self.fields['tipo_lotacao_tributaria_08'].widget.attrs['required'] = True
        
        self.fields['tipo_lotacao_tributaria_07'].widget.attrs['required'] = True
        
        self.fields['tipo_lotacao_tributaria_06'].widget.attrs['required'] = True
        
        self.fields['tipo_lotacao_tributaria_05'].widget.attrs['required'] = True
        
        self.fields['tipo_lotacao_tributaria_04'].widget.attrs['required'] = True
        
        self.fields['tipo_lotacao_tributaria_03'].widget.attrs['required'] = True
        
        self.fields['tipo_lotacao_tributaria_02'].widget.attrs['required'] = True
        
        self.fields['tipo_lotacao_tributaria_01'].widget.attrs['required'] = True
        
        self.fields['classificacao_tributaria'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = CompatibilidadesCategoriasClassificacoesLotacoes
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_lotacoes_tributarias_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_lotacoes_tributarias_tipos,self ).__init__(*args,**kwargs)
        
        self.fields['preenchimento_campo_nr_insc'].widget.attrs['required'] = True
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = LotacoesTributariasTipos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_arquivos_esocial_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_arquivos_esocial_tipos,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = ArquivosEsocialTipos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_classificacoes_tributarias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_classificacoes_tributarias,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = ClassificacoesTributarias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_dependentes_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_dependentes_tipos,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = DependentesTipos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_paises(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_paises,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        
        self.fields['nome'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = Paises
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_inscricoes_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_inscricoes_tipos,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = InscricoesTipos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_codigo_aliquotas_fpas_terceiros(forms.ModelForm):
    aliquota = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_codigo_aliquotas_fpas_terceiros,self ).__init__(*args,**kwargs)
        
        self.fields['ind_total'].widget.attrs['required'] = True
        
        self.fields['aliquota'].widget.attrs['required'] = True
        
        self.fields['codigo_terceiro'].widget.attrs['required'] = True
        
        self.fields['terceiros'].widget.attrs['required'] = True
        
        self.fields['base_calculo'].widget.attrs['required'] = True
        
        self.fields['tipo_empresa'].widget.attrs['required'] = True
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = CodigoAliquotasFPASTerceiros
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_naturezas_rubricas(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_naturezas_rubricas,self ).__init__(*args,**kwargs)
        
        self.fields['data_inicio'].widget.attrs['required'] = True
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['titulo'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = NaturezasRubricas
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_financiamentos_aposentadorias_especiais(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_financiamentos_aposentadorias_especiais,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = FinanciamentosAposentadoriasEspeciais
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_trabalhadores_categorias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_trabalhadores_categorias,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        
        self.fields['grupo'].widget.attrs['required'] = True

    class Meta:
        model = TrabalhadoresCategorias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_cnae(forms.ModelForm):
    aliquota = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_cnae,self ).__init__(*args,**kwargs)
        
        self.fields['aliquota'].widget.attrs['required'] = True
        
        self.fields['data_inicio'].widget.attrs['required'] = True
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = CNAE
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_cid(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_cid,self ).__init__(*args,**kwargs)
        
        self.fields['descricao_resumida'].widget.attrs['required'] = True
        
        self.fields['data_inicio'].widget.attrs['required'] = True
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = CID
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_cbo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_cbo,self ).__init__(*args,**kwargs)
        
        self.fields['data_inicio'].widget.attrs['required'] = True
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = CBO
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_municipios(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_municipios,self ).__init__(*args,**kwargs)
        
        self.fields['titulo'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = Municipios
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

