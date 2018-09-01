# coding: utf-8
from django import forms
from emensageriapro.s2210.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s2210evtCAT 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s2210_catorigem(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2210_catorigem,self ).__init__(*args,**kwargs)
        
        self.fields['dtcatorig'].widget.attrs['required'] = True
        
        self.fields['s2210_evtcat'].widget.attrs['required'] = True

    class Meta:
        model = s2210catOrigem
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2210_atestado(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2210_atestado,self ).__init__(*args,**kwargs)
        
        self.fields['nroc'].widget.attrs['required'] = True
        
        self.fields['ideoc'].widget.attrs['required'] = True
        
        self.fields['nmemit'].widget.attrs['required'] = True
        
        self.fields['codcid'].widget.attrs['required'] = True
        
        self.fields['indafast'].widget.attrs['required'] = True
        
        self.fields['durtrat'].widget.attrs['required'] = True
        
        self.fields['indinternacao'].widget.attrs['required'] = True
        
        self.fields['hratendimento'].widget.attrs['required'] = True
        
        self.fields['dtatendimento'].widget.attrs['required'] = True
        
        self.fields['s2210_evtcat'].widget.attrs['required'] = True

    class Meta:
        model = s2210atestado
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2210_agentecausador(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2210_agentecausador,self ).__init__(*args,**kwargs)
        
        self.fields['codagntcausador'].widget.attrs['required'] = True
        self.fields['s2210_evtcat'].queryset = s2210evtCAT.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2210_evtcat'].widget.attrs['required'] = True

    class Meta:
        model = s2210agenteCausador
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2210_parteatingida(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2210_parteatingida,self ).__init__(*args,**kwargs)
        
        self.fields['lateralidade'].widget.attrs['required'] = True
        
        self.fields['codparteating'].widget.attrs['required'] = True
        self.fields['s2210_evtcat'].queryset = s2210evtCAT.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2210_evtcat'].widget.attrs['required'] = True

    class Meta:
        model = s2210parteAtingida
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

