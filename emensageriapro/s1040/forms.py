# coding: utf-8
from django import forms
from emensageriapro.s1040.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1040evtTabFuncao 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1040_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1040_exclusao,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codfuncao'].widget.attrs['required'] = True
        
        self.fields['s1040_evttabfuncao'].widget.attrs['required'] = True

    class Meta:
        model = s1040exclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1040_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1040_alteracao_novavalidade,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['s1040_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1040alteracaonovaValidade
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1040_alteracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1040_alteracao,self ).__init__(*args,**kwargs)
        
        self.fields['codcbo'].widget.attrs['required'] = True
        
        self.fields['dscfuncao'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codfuncao'].widget.attrs['required'] = True
        
        self.fields['s1040_evttabfuncao'].widget.attrs['required'] = True

    class Meta:
        model = s1040alteracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1040_inclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1040_inclusao,self ).__init__(*args,**kwargs)
        
        self.fields['codcbo'].widget.attrs['required'] = True
        
        self.fields['dscfuncao'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codfuncao'].widget.attrs['required'] = True
        
        self.fields['s1040_evttabfuncao'].widget.attrs['required'] = True

    class Meta:
        model = s1040inclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

