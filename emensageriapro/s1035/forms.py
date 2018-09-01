# coding: utf-8
from django import forms
from emensageriapro.s1035.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1035evtTabCarreira 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1035_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1035_exclusao,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codcarreira'].widget.attrs['required'] = True
        
        self.fields['s1035_evttabcarreira'].widget.attrs['required'] = True

    class Meta:
        model = s1035exclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1035_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1035_alteracao_novavalidade,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['s1035_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1035alteracaonovaValidade
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1035_alteracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1035_alteracao,self ).__init__(*args,**kwargs)
        
        self.fields['sitcarr'].widget.attrs['required'] = True
        
        self.fields['dtleicarr'].widget.attrs['required'] = True
        
        self.fields['dsccarreira'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codcarreira'].widget.attrs['required'] = True
        
        self.fields['s1035_evttabcarreira'].widget.attrs['required'] = True

    class Meta:
        model = s1035alteracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1035_inclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1035_inclusao,self ).__init__(*args,**kwargs)
        
        self.fields['sitcarr'].widget.attrs['required'] = True
        
        self.fields['dtleicarr'].widget.attrs['required'] = True
        
        self.fields['dsccarreira'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codcarreira'].widget.attrs['required'] = True
        
        self.fields['s1035_evttabcarreira'].widget.attrs['required'] = True

    class Meta:
        model = s1035inclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

