# coding: utf-8
from django import forms
from emensageriapro.tabelas.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 


__author__ = 'marcelovasconcellos'



#custom_forms#



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


class form_esocial_trabalhadores_categorias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_trabalhadores_categorias,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        
        self.fields['grupo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialTrabalhadoresCategorias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_financiamentos_aposentadorias_especiais(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_financiamentos_aposentadorias_especiais,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialFinanciamentosAposentadoriasEspeciais
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_naturezas_rubricas(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_naturezas_rubricas,self ).__init__(*args,**kwargs)
        
        self.fields['data_inicio'].widget.attrs['required'] = True
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['titulo'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialNaturezasRubricas
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_codigo_aliquotas_fpas_terceiros(forms.ModelForm):
    aliquota = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_codigo_aliquotas_fpas_terceiros,self ).__init__(*args,**kwargs)
        
        self.fields['ind_total'].widget.attrs['required'] = True
        
        self.fields['aliquota'].widget.attrs['required'] = True
        
        self.fields['codigo_terceiro'].widget.attrs['required'] = True
        
        self.fields['terceiros'].widget.attrs['required'] = True
        
        self.fields['base_calculo'].widget.attrs['required'] = True
        
        self.fields['tipo_empresa'].widget.attrs['required'] = True
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialCodigoAliquotasFPASTerceiros
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_inscricoes_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_inscricoes_tipos,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialInscricoesTipos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_paises(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_paises,self ).__init__(*args,**kwargs)
        
        self.fields['nome'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialPaises
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_dependentes_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_dependentes_tipos,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialDependentesTipos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_classificacoes_tributarias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_classificacoes_tributarias,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialClassificacoesTributarias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_arquivos_esocial_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_arquivos_esocial_tipos,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialArquivosEsocialTipos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_lotacoes_tributarias_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_lotacoes_tributarias_tipos,self ).__init__(*args,**kwargs)
        
        self.fields['preenchimento_campo_nr_insc'].widget.attrs['required'] = True
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialLotacoesTributariasTipos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_compatibilidades_categorias_classificacoes_lotacoes(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_compatibilidades_categorias_classificacoes_lotacoes,self ).__init__(*args,**kwargs)
        
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
        model = eSocialCompatibilidadesCategoriasClassificacoesLotacoes
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_compatibilidades_lotacoes_classificacoes(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_compatibilidades_lotacoes_classificacoes,self ).__init__(*args,**kwargs)
        
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
        model = eSocialCompatibilidadesLotacoesClassificacoes
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_partes_corpo_atingidas(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_partes_corpo_atingidas,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialPartesCorpoAtingidas
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_agentes_causadores_acidentes_trabalho(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_agentes_causadores_acidentes_trabalho,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialAgentesCausadoresAcidentesTrabalho
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_agentes_causadores_doencas_profissionais(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_agentes_causadores_doencas_profissionais,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialAgentesCausadoresDoencasProfissionais
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_acidentes_situacoes_geradoras(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_acidentes_situacoes_geradoras,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialAcidentesSituacoesGeradoras
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_naturezas_lesoes(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_naturezas_lesoes,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialNaturezasLesoes
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_afastamentos_motivos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_afastamentos_motivos,self ).__init__(*args,**kwargs)
        
        self.fields['data_inicio'].widget.attrs['required'] = True
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialAfastamentosMotivos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_desligamentos_motivos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_desligamentos_motivos,self ).__init__(*args,**kwargs)
        
        self.fields['data_inicio'].widget.attrs['required'] = True
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialDesligamentosMotivos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_logradouros_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_logradouros_tipos,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialLogradourosTipos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_naturezas_juridicas(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_naturezas_juridicas,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        
        self.fields['grupo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialNaturezasJuridicas
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_compatibilidades_fpas_classificacoes_tributarias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_compatibilidades_fpas_classificacoes_tributarias,self ).__init__(*args,**kwargs)
        
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
        model = eSocialCompatibilidadesFPASClassificacoesTributarias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_fatores_risco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_fatores_risco,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        
        self.fields['grupo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialFatoresRisco
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_codificacoes_acidente_trabalho(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_codificacoes_acidente_trabalho,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialCodificacoesAcidenteTrabalho
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_beneficios_previdenciarios_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_beneficios_previdenciarios_tipos,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        
        self.fields['grupo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialBeneficiosPrevidenciariosTipos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_beneficios_previdenciarios_cessacao_motivos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_beneficios_previdenciarios_cessacao_motivos,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialBeneficiosPrevidenciariosCessacaoMotivos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_procedimentos_diagnosticos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_procedimentos_diagnosticos,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialProcedimentosDiagnosticos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_atividades_periculosas_insalubres_especiais(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_atividades_periculosas_insalubres_especiais,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        
        self.fields['grupo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialAtividadesPericulosasInsalubresEspeciais
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_treinamentos_capacitacoes_exercicios_simulados(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_treinamentos_capacitacoes_exercicios_simulados,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialTreinamentosCapacitacoesExerciciosSimulados
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_esocial_programas_planos_documentos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_esocial_programas_planos_documentos,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = eSocialProgramasPlanosDocumentos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_efdreinf_pagamentos_codigos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_efdreinf_pagamentos_codigos,self ).__init__(*args,**kwargs)
        
        self.fields['beneficiario_pf'].widget.attrs['required'] = True
        
        self.fields['beneficiario_pj'].widget.attrs['required'] = True
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        
        self.fields['grupo'].widget.attrs['required'] = True

    class Meta:
        model = EFDReinfPagamentosCodigos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_efdreinf_regras_pagamentos_codigos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_efdreinf_regras_pagamentos_codigos,self ).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True
        
        self.fields['classificacao'].widget.attrs['required'] = True

    class Meta:
        model = EFDReinfRegrasPagamentosCodigos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_efdreinf_rendimentos_beneficiarios_exterior(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_efdreinf_rendimentos_beneficiarios_exterior,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = EFDReinfRendimentosBeneficiariosExterior
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_efdreinf_rendimentos_beneficiarios_exterior_tributacao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_efdreinf_rendimentos_beneficiarios_exterior_tributacao,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = EFDReinfRendimentosBeneficiariosExteriorTributacao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_efdreinf_informacoes_beneficiarios_exterior(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_efdreinf_informacoes_beneficiarios_exterior,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = EFDReinfInformacoesBeneficiariosExterior
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_efdreinf_classificacao_servicos_prestados(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_efdreinf_classificacao_servicos_prestados,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = EFDReinfClassificacaoServicosPrestados
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_efdreinf_paises(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_efdreinf_paises,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = EFDReinfPaises
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_efdreinf_classificacao_tributaria(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_efdreinf_classificacao_tributaria,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True

    class Meta:
        model = EFDReinfClassificacaoTributaria
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_efdreinf_codigos_atividades_produtos_servicos_cprb(forms.ModelForm):
    aliquota = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_efdreinf_codigos_atividades_produtos_servicos_cprb,self ).__init__(*args,**kwargs)
        
        self.fields['descricao'].widget.attrs['required'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        
        self.fields['grupo'].widget.attrs['required'] = True

    class Meta:
        model = EFDReinfCodigosAtividadesProdutosServicosCPRB
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


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

