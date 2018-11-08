# coding: utf-8
from django import forms
from emensageriapro.s1030.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1030evtTabCargo 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1030_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1030_exclusao,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codcargo'].widget.attrs['required'] = True
        
        self.fields['s1030_evttabcargo'].widget.attrs['required'] = True

    class Meta:
        model = s1030exclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1030_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1030_alteracao_novavalidade,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['s1030_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1030alteracaonovaValidade
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1030_alteracao_cargopublico(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1030_alteracao_cargopublico,self ).__init__(*args,**kwargs)
        
        self.fields['sitcargo'].widget.attrs['required'] = True
        
        self.fields['dtlei'].widget.attrs['required'] = True
        
        self.fields['nrlei'].widget.attrs['required'] = True
        
        self.fields['dedicexcl'].widget.attrs['required'] = True
        
        self.fields['contagemesp'].widget.attrs['required'] = True
        
        self.fields['acumcargo'].widget.attrs['required'] = True
        
        self.fields['s1030_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1030alteracaocargoPublico
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1030_alteracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1030_alteracao,self ).__init__(*args,**kwargs)
        
        self.fields['codcbo'].widget.attrs['required'] = True
        
        self.fields['nmcargo'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codcargo'].widget.attrs['required'] = True
        
        self.fields['s1030_evttabcargo'].widget.attrs['required'] = True

    class Meta:
        model = s1030alteracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1030_inclusao_cargopublico(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1030_inclusao_cargopublico,self ).__init__(*args,**kwargs)
        
        self.fields['sitcargo'].widget.attrs['required'] = True
        
        self.fields['dtlei'].widget.attrs['required'] = True
        
        self.fields['nrlei'].widget.attrs['required'] = True
        
        self.fields['dedicexcl'].widget.attrs['required'] = True
        
        self.fields['contagemesp'].widget.attrs['required'] = True
        
        self.fields['acumcargo'].widget.attrs['required'] = True
        
        self.fields['s1030_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1030inclusaocargoPublico
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1030_inclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1030_inclusao,self ).__init__(*args,**kwargs)
        
        self.fields['codcbo'].widget.attrs['required'] = True
        
        self.fields['nmcargo'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codcargo'].widget.attrs['required'] = True
        
        self.fields['s1030_evttabcargo'].widget.attrs['required'] = True

    class Meta:
        model = s1030inclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

