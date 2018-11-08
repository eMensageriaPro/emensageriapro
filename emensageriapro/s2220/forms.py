# coding: utf-8
from django import forms
from emensageriapro.s2220.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s2220evtMonit 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s2220_exame(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2220_exame,self ).__init__(*args,**kwargs)
        
        self.fields['dtinimonit'].widget.attrs['required'] = True
        
        self.fields['ordexame'].widget.attrs['required'] = True
        
        self.fields['interprexm'].widget.attrs['required'] = True
        
        self.fields['procrealizado'].widget.attrs['required'] = True
        
        self.fields['dtexm'].widget.attrs['required'] = True
        self.fields['s2220_evtmonit'].queryset = s2220evtMonit.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2220_evtmonit'].widget.attrs['required'] = True

    class Meta:
        model = s2220exame
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

