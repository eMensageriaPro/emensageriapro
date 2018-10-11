# coding: utf-8
from django import forms
from emensageriapro.s1065.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1065evtTabEquipamento 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1065_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1065_exclusao,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codep'].widget.attrs['required'] = True
        
        self.fields['s1065_evttabequipamento'].widget.attrs['required'] = True

    class Meta:
        model = s1065exclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1065_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1065_alteracao_novavalidade,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['s1065_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1065alteracaonovaValidade
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1065_alteracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1065_alteracao,self ).__init__(*args,**kwargs)
        
        self.fields['dscep'].widget.attrs['required'] = True
        
        self.fields['tpep'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codep'].widget.attrs['required'] = True
        
        self.fields['s1065_evttabequipamento'].widget.attrs['required'] = True

    class Meta:
        model = s1065alteracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1065_inclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1065_inclusao,self ).__init__(*args,**kwargs)
        
        self.fields['dscep'].widget.attrs['required'] = True
        
        self.fields['tpep'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codep'].widget.attrs['required'] = True
        
        self.fields['s1065_evttabequipamento'].widget.attrs['required'] = True

    class Meta:
        model = s1065inclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

