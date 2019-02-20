# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.tabelas.models import * 


__author__ = 'marcelovasconcellos'

"""

    eMensageria - Sistema Open-Source de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""

#custom_forms#




class form_municipios(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_municipios, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['titulo'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_municipios, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = Municipios
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_cbo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_cbo, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True        
        self.fields['data_inicio'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_cbo, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = CBO
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_cid(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_cid, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True        
        self.fields['data_inicio'].widget.attrs['required'] = True        
        self.fields['descricao_resumida'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_cid, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = CID
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_cnae(forms.ModelForm):
    aliquota = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_cnae, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True        
        self.fields['data_inicio'].widget.attrs['required'] = True        
        self.fields['aliquota'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_cnae, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = CNAE
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_trabalhadores_categorias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_trabalhadores_categorias, self).__init__(*args,**kwargs)
        
        self.fields['grupo'].widget.attrs['required'] = True        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_trabalhadores_categorias, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialTrabalhadoresCategorias
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_financiamentos_aposentadorias_especiais(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_financiamentos_aposentadorias_especiais, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_financiamentos_aposentadorias_especiais, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialFinanciamentosAposentadoriasEspeciais
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_naturezas_rubricas(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_naturezas_rubricas, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['titulo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True        
        self.fields['data_inicio'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_naturezas_rubricas, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialNaturezasRubricas
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_codigo_aliquotas_fpas_terceiros(forms.ModelForm):
    aliquota = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_codigo_aliquotas_fpas_terceiros, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True        
        self.fields['tipo_empresa'].widget.attrs['required'] = True        
        self.fields['base_calculo'].widget.attrs['required'] = True        
        self.fields['terceiros'].widget.attrs['required'] = True        
        self.fields['codigo_terceiro'].widget.attrs['required'] = True        
        self.fields['aliquota'].widget.attrs['required'] = True        
        self.fields['ind_total'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_codigo_aliquotas_fpas_terceiros, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialCodigoAliquotasFPASTerceiros
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_inscricoes_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_inscricoes_tipos, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_inscricoes_tipos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialInscricoesTipos
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_paises(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_paises, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['nome'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_paises, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialPaises
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_dependentes_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_dependentes_tipos, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_dependentes_tipos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialDependentesTipos
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_classificacoes_tributarias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_classificacoes_tributarias, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_classificacoes_tributarias, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialClassificacoesTributarias
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_arquivos_esocial_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_arquivos_esocial_tipos, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_arquivos_esocial_tipos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialArquivosEsocialTipos
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_lotacoes_tributarias_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_lotacoes_tributarias_tipos, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True        
        self.fields['preenchimento_campo_nr_insc'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_lotacoes_tributarias_tipos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialLotacoesTributariasTipos
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_compatibilidades_categorias_classificacoes_lotacoes(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_compatibilidades_categorias_classificacoes_lotacoes, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria'].widget.attrs['required'] = True        
        self.fields['tipo_lotacao_tributaria_01'].widget.attrs['required'] = True        
        self.fields['tipo_lotacao_tributaria_02'].widget.attrs['required'] = True        
        self.fields['tipo_lotacao_tributaria_03'].widget.attrs['required'] = True        
        self.fields['tipo_lotacao_tributaria_04'].widget.attrs['required'] = True        
        self.fields['tipo_lotacao_tributaria_05'].widget.attrs['required'] = True        
        self.fields['tipo_lotacao_tributaria_06'].widget.attrs['required'] = True        
        self.fields['tipo_lotacao_tributaria_07'].widget.attrs['required'] = True        
        self.fields['tipo_lotacao_tributaria_08'].widget.attrs['required'] = True        
        self.fields['tipo_lotacao_tributaria_09'].widget.attrs['required'] = True        
        self.fields['tipo_lotacao_tributaria_10'].widget.attrs['required'] = True        
        self.fields['tipo_lotacao_tributaria_21'].widget.attrs['required'] = True        
        self.fields['tipo_lotacao_tributaria_24'].widget.attrs['required'] = True        
        self.fields['tipo_lotacao_tributaria_90'].widget.attrs['required'] = True        
        self.fields['tipo_lotacao_tributaria_91'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_compatibilidades_categorias_classificacoes_lotacoes, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialCompatibilidadesCategoriasClassificacoesLotacoes
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_compatibilidades_lotacoes_classificacoes(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_compatibilidades_lotacoes_classificacoes, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_01'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_02'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_03'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_04'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_06'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_07'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_08'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_09'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_10'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_11'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_13'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_14'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_21'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_22'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_60'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_70'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_80'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_85'].widget.attrs['required'] = True        
        self.fields['tipo_classificacao_tributaria_99'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_compatibilidades_lotacoes_classificacoes, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialCompatibilidadesLotacoesClassificacoes
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_partes_corpo_atingidas(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_partes_corpo_atingidas, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_partes_corpo_atingidas, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialPartesCorpoAtingidas
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_agentes_causadores_acidentes_trabalho(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_agentes_causadores_acidentes_trabalho, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_agentes_causadores_acidentes_trabalho, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialAgentesCausadoresAcidentesTrabalho
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_agentes_causadores_doencas_profissionais(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_agentes_causadores_doencas_profissionais, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_agentes_causadores_doencas_profissionais, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialAgentesCausadoresDoencasProfissionais
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_acidentes_situacoes_geradoras(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_acidentes_situacoes_geradoras, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_acidentes_situacoes_geradoras, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialAcidentesSituacoesGeradoras
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_naturezas_lesoes(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_naturezas_lesoes, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_naturezas_lesoes, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialNaturezasLesoes
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_afastamentos_motivos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_afastamentos_motivos, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True        
        self.fields['data_inicio'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_afastamentos_motivos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialAfastamentosMotivos
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_desligamentos_motivos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_desligamentos_motivos, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True        
        self.fields['data_inicio'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_desligamentos_motivos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialDesligamentosMotivos
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_logradouros_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_logradouros_tipos, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_logradouros_tipos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialLogradourosTipos
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_naturezas_juridicas(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_naturezas_juridicas, self).__init__(*args,**kwargs)
        
        self.fields['grupo'].widget.attrs['required'] = True        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_naturezas_juridicas, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialNaturezasJuridicas
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_compatibilidades_fpas_classificacoes_tributarias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_compatibilidades_fpas_classificacoes_tributarias, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_01'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_02'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_03'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_04'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_06'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_07'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_08'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_09'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_10'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_11'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_13'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_14'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_21'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_22'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_60'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_70'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_80'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_85'].widget.attrs['required'] = True        
        self.fields['classificacao_tributaria_99'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_compatibilidades_fpas_classificacoes_tributarias, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialCompatibilidadesFPASClassificacoesTributarias
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_fatores_risco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_fatores_risco, self).__init__(*args,**kwargs)
        
        self.fields['grupo'].widget.attrs['required'] = True        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_fatores_risco, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialFatoresRisco
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_codificacoes_acidente_trabalho(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_codificacoes_acidente_trabalho, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_codificacoes_acidente_trabalho, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialCodificacoesAcidenteTrabalho
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_beneficios_previdenciarios_tipos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_beneficios_previdenciarios_tipos, self).__init__(*args,**kwargs)
        
        self.fields['grupo'].widget.attrs['required'] = True        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_beneficios_previdenciarios_tipos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialBeneficiosPrevidenciariosTipos
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_beneficios_previdenciarios_cessacao_motivos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_beneficios_previdenciarios_cessacao_motivos, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_beneficios_previdenciarios_cessacao_motivos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialBeneficiosPrevidenciariosCessacaoMotivos
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_procedimentos_diagnosticos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_procedimentos_diagnosticos, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_procedimentos_diagnosticos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialProcedimentosDiagnosticos
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_atividades_periculosas_insalubres_especiais(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_atividades_periculosas_insalubres_especiais, self).__init__(*args,**kwargs)
        
        self.fields['grupo'].widget.attrs['required'] = True        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_atividades_periculosas_insalubres_especiais, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialAtividadesPericulosasInsalubresEspeciais
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_treinamentos_capacitacoes_exercicios_simulados(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_treinamentos_capacitacoes_exercicios_simulados, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_treinamentos_capacitacoes_exercicios_simulados, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialTreinamentosCapacitacoesExerciciosSimulados
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_esocial_programas_planos_documentos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_esocial_programas_planos_documentos, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_esocial_programas_planos_documentos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = eSocialProgramasPlanosDocumentos
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_efdreinf_pagamentos_codigos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_efdreinf_pagamentos_codigos, self).__init__(*args,**kwargs)
        
        self.fields['grupo'].widget.attrs['required'] = True        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['beneficiario_pj'].widget.attrs['required'] = True        
        self.fields['beneficiario_pf'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_efdreinf_pagamentos_codigos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = EFDReinfPagamentosCodigos
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_efdreinf_regras_pagamentos_codigos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_efdreinf_regras_pagamentos_codigos, self).__init__(*args,**kwargs)
        
        self.fields['classificacao'].widget.attrs['required'] = True        
        self.fields['codigo'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_efdreinf_regras_pagamentos_codigos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = EFDReinfRegrasPagamentosCodigos
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'descricao',
 
        ]



class form_efdreinf_rendimentos_beneficiarios_exterior(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_efdreinf_rendimentos_beneficiarios_exterior, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_efdreinf_rendimentos_beneficiarios_exterior, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = EFDReinfRendimentosBeneficiariosExterior
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_efdreinf_rendimentos_beneficiarios_exterior_tributacao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_efdreinf_rendimentos_beneficiarios_exterior_tributacao, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_efdreinf_rendimentos_beneficiarios_exterior_tributacao, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = EFDReinfRendimentosBeneficiariosExteriorTributacao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_efdreinf_informacoes_beneficiarios_exterior(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_efdreinf_informacoes_beneficiarios_exterior, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_efdreinf_informacoes_beneficiarios_exterior, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = EFDReinfInformacoesBeneficiariosExterior
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_efdreinf_classificacao_servicos_prestados(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_efdreinf_classificacao_servicos_prestados, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_efdreinf_classificacao_servicos_prestados, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = EFDReinfClassificacaoServicosPrestados
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_efdreinf_paises(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_efdreinf_paises, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_efdreinf_paises, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = EFDReinfPaises
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_efdreinf_classificacao_tributaria(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_efdreinf_classificacao_tributaria, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_efdreinf_classificacao_tributaria, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = EFDReinfClassificacaoTributaria
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_efdreinf_codigos_atividades_produtos_servicos_cprb(forms.ModelForm):
    aliquota = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_efdreinf_codigos_atividades_produtos_servicos_cprb, self).__init__(*args,**kwargs)
        
        self.fields['grupo'].widget.attrs['required'] = True        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_efdreinf_codigos_atividades_produtos_servicos_cprb, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = EFDReinfCodigosAtividadesProdutosServicosCPRB
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_efdreinf_eventos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_efdreinf_eventos, self).__init__(*args,**kwargs)
        
        self.fields['codigo'].widget.attrs['required'] = True        
        self.fields['descricao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_efdreinf_eventos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = EFDReinfEventos
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

