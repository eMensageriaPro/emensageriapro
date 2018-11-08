# coding: utf-8
from django import forms
from emensageriapro.s3000.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s3000evtExclusao 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s3000_idefolhapagto(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s3000_idefolhapagto,self ).__init__(*args,**kwargs)
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['s3000_evtexclusao'].widget.attrs['required'] = True

    class Meta:
        model = s3000ideFolhaPagto
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s3000_idetrabalhador(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s3000_idetrabalhador,self ).__init__(*args,**kwargs)
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['s3000_evtexclusao'].widget.attrs['required'] = True

    class Meta:
        model = s3000ideTrabalhador
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

