# coding: utf-8
from django import forms
from emensageriapro.s1280.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1280evtInfoComplPer 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1280_infoativconcom(forms.ModelForm):
    fator13 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fatormes = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1280_infoativconcom,self ).__init__(*args,**kwargs)
        
        self.fields['fator13'].widget.attrs['required'] = True
        
        self.fields['fatormes'].widget.attrs['required'] = True
        
        self.fields['s1280_evtinfocomplper'].widget.attrs['required'] = True

    class Meta:
        model = s1280infoAtivConcom
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1280_infosubstpatropport(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1280_infosubstpatropport,self ).__init__(*args,**kwargs)
        
        self.fields['cnpjopportuario'].widget.attrs['required'] = True
        self.fields['s1280_evtinfocomplper'].queryset = s1280evtInfoComplPer.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1280_evtinfocomplper'].widget.attrs['required'] = True

    class Meta:
        model = s1280infoSubstPatrOpPort
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1280_infosubstpatr(forms.ModelForm):
    percredcontrib = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1280_infosubstpatr,self ).__init__(*args,**kwargs)
        
        self.fields['percredcontrib'].widget.attrs['required'] = True
        
        self.fields['indsubstpatr'].widget.attrs['required'] = True
        
        self.fields['s1280_evtinfocomplper'].widget.attrs['required'] = True

    class Meta:
        model = s1280infoSubstPatr
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

