# coding: utf-8
from django import forms
from emensageriapro.s1207.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1207evtBenPrRP 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1207_itens(forms.ModelForm):
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1207_itens,self ).__init__(*args,**kwargs)
        
        self.fields['vrrubr'].widget.attrs['required'] = True
        
        self.fields['idetabrubr'].widget.attrs['required'] = True
        
        self.fields['codrubr'].widget.attrs['required'] = True
        self.fields['s1207_dmdev'].queryset = s1207dmDev.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1207_dmdev'].widget.attrs['required'] = True

    class Meta:
        model = s1207itens
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1207_dmdev(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1207_dmdev,self ).__init__(*args,**kwargs)
        
        self.fields['idedmdev'].widget.attrs['required'] = True
        
        self.fields['nrbenefic'].widget.attrs['required'] = True
        
        self.fields['tpbenef'].widget.attrs['required'] = True
        self.fields['s1207_evtbenprrp'].queryset = s1207evtBenPrRP.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1207_evtbenprrp'].widget.attrs['required'] = True

    class Meta:
        model = s1207dmDev
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

