# coding: utf-8
from django import forms
from emensageriapro.s1050.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1050evtTabHorTur 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1050_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1050_alteracao_novavalidade,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['s1050_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1050alteracaonovaValidade
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1050_alteracao_horariointervalo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1050_alteracao_horariointervalo,self ).__init__(*args,**kwargs)
        
        self.fields['durinterv'].widget.attrs['required'] = True
        
        self.fields['tpinterv'].widget.attrs['required'] = True
        self.fields['s1050_alteracao'].queryset = s1050alteracao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1050_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1050alteracaohorarioIntervalo
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1050_alteracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1050_alteracao,self ).__init__(*args,**kwargs)
        
        self.fields['perhorflexivel'].widget.attrs['required'] = True
        
        self.fields['durjornada'].widget.attrs['required'] = True
        
        self.fields['hrsaida'].widget.attrs['required'] = True
        
        self.fields['hrentr'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codhorcontrat'].widget.attrs['required'] = True
        
        self.fields['s1050_evttabhortur'].widget.attrs['required'] = True

    class Meta:
        model = s1050alteracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1050_inclusao_horariointervalo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1050_inclusao_horariointervalo,self ).__init__(*args,**kwargs)
        
        self.fields['durinterv'].widget.attrs['required'] = True
        
        self.fields['tpinterv'].widget.attrs['required'] = True
        self.fields['s1050_inclusao'].queryset = s1050inclusao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1050_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1050inclusaohorarioIntervalo
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1050_inclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1050_inclusao,self ).__init__(*args,**kwargs)
        
        self.fields['perhorflexivel'].widget.attrs['required'] = True
        
        self.fields['durjornada'].widget.attrs['required'] = True
        
        self.fields['hrsaida'].widget.attrs['required'] = True
        
        self.fields['hrentr'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codhorcontrat'].widget.attrs['required'] = True
        
        self.fields['s1050_evttabhortur'].widget.attrs['required'] = True

    class Meta:
        model = s1050inclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1050_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1050_exclusao,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codhorcontrat'].widget.attrs['required'] = True
        
        self.fields['s1050_evttabhortur'].widget.attrs['required'] = True

    class Meta:
        model = s1050exclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

