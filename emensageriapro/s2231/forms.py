# coding: utf-8
from django import forms
from emensageriapro.s2231.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s2231evtCessao 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s2231_fimcessao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2231_fimcessao,self ).__init__(*args,**kwargs)
        
        self.fields['dttermcessao'].widget.attrs['required'] = True
        
        self.fields['s2231_evtcessao'].widget.attrs['required'] = True

    class Meta:
        model = s2231fimCessao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2231_inicessao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2231_inicessao,self ).__init__(*args,**kwargs)
        
        self.fields['indcessao'].widget.attrs['required'] = True
        
        self.fields['infonus'].widget.attrs['required'] = True
        
        self.fields['cnpjcess'].widget.attrs['required'] = True
        
        self.fields['dtinicessao'].widget.attrs['required'] = True
        
        self.fields['s2231_evtcessao'].widget.attrs['required'] = True

    class Meta:
        model = s2231iniCessao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

