# coding: utf-8
from django import forms
from emensageriapro.s1060.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1060evtTabAmbiente 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1060_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1060_exclusao,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codamb'].widget.attrs['required'] = True
        
        self.fields['s1060_evttabambiente'].widget.attrs['required'] = True

    class Meta:
        model = s1060exclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1060_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1060_alteracao_novavalidade,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['s1060_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1060alteracaonovaValidade
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1060_alteracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1060_alteracao,self ).__init__(*args,**kwargs)
        
        self.fields['localamb'].widget.attrs['required'] = True
        
        self.fields['dscamb'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codamb'].widget.attrs['required'] = True
        
        self.fields['s1060_evttabambiente'].widget.attrs['required'] = True

    class Meta:
        model = s1060alteracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1060_inclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1060_inclusao,self ).__init__(*args,**kwargs)
        
        self.fields['localamb'].widget.attrs['required'] = True
        
        self.fields['dscamb'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codamb'].widget.attrs['required'] = True
        
        self.fields['s1060_evttabambiente'].widget.attrs['required'] = True

    class Meta:
        model = s1060inclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

