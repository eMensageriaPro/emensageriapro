# coding: utf-8
from django import forms
from emensageriapro.s1080.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1080evtTabOperPort 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1080_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1080_exclusao,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['cnpjopportuario'].widget.attrs['required'] = True
        
        self.fields['s1080_evttaboperport'].widget.attrs['required'] = True

    class Meta:
        model = s1080exclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1080_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1080_alteracao_novavalidade,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['s1080_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1080alteracaonovaValidade
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1080_alteracao(forms.ModelForm):
    aliqratajust = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fap = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1080_alteracao,self ).__init__(*args,**kwargs)
        
        self.fields['aliqratajust'].widget.attrs['required'] = True
        
        self.fields['fap'].widget.attrs['required'] = True
        
        self.fields['aliqrat'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['cnpjopportuario'].widget.attrs['required'] = True
        
        self.fields['s1080_evttaboperport'].widget.attrs['required'] = True

    class Meta:
        model = s1080alteracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1080_inclusao(forms.ModelForm):
    aliqratajust = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fap = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1080_inclusao,self ).__init__(*args,**kwargs)
        
        self.fields['aliqratajust'].widget.attrs['required'] = True
        
        self.fields['fap'].widget.attrs['required'] = True
        
        self.fields['aliqrat'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['cnpjopportuario'].widget.attrs['required'] = True
        
        self.fields['s1080_evttaboperport'].widget.attrs['required'] = True

    class Meta:
        model = s1080inclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

