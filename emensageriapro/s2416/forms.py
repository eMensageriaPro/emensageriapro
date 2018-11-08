# coding: utf-8
from django import forms
from emensageriapro.s2416.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s2416evtCdBenAlt 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s2416_suspensao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2416_suspensao,self ).__init__(*args,**kwargs)
        
        self.fields['mtvsuspensao'].widget.attrs['required'] = True
        
        self.fields['s2416_evtcdbenalt'].widget.attrs['required'] = True

    class Meta:
        model = s2416suspensao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2416_homologtc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2416_homologtc,self ).__init__(*args,**kwargs)
        
        self.fields['nratolegal'].widget.attrs['required'] = True
        
        self.fields['s2416_evtcdbenalt'].widget.attrs['required'] = True

    class Meta:
        model = s2416homologTC
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2416_infopenmorte(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2416_infopenmorte,self ).__init__(*args,**kwargs)
        
        self.fields['tppenmorte'].widget.attrs['required'] = True
        
        self.fields['s2416_evtcdbenalt'].widget.attrs['required'] = True

    class Meta:
        model = s2416infoPenMorte
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

