# coding: utf-8
from django import forms
from emensageriapro.s1270.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1270evtContratAvNP 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1270_remunavnp(forms.ModelForm):
    vrdesccp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrbcfgts = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrbccp13 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrbccp25 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrbccp20 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrbccp15 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrbccp00 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1270_remunavnp,self ).__init__(*args,**kwargs)
        
        self.fields['vrdesccp'].widget.attrs['required'] = True
        
        self.fields['vrbcfgts'].widget.attrs['required'] = True
        
        self.fields['vrbccp13'].widget.attrs['required'] = True
        
        self.fields['vrbccp25'].widget.attrs['required'] = True
        
        self.fields['vrbccp20'].widget.attrs['required'] = True
        
        self.fields['vrbccp15'].widget.attrs['required'] = True
        
        self.fields['vrbccp00'].widget.attrs['required'] = True
        
        self.fields['codlotacao'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        self.fields['s1270_evtcontratavnp'].queryset = s1270evtContratAvNP.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1270_evtcontratavnp'].widget.attrs['required'] = True

    class Meta:
        model = s1270remunAvNP
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

