# coding: utf-8
from django import forms
from emensageriapro.s2230.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s2230evtAfastTemp 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s2230_iniafastamento(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2230_iniafastamento,self ).__init__(*args,**kwargs)
        
        self.fields['codmotafast'].widget.attrs['required'] = True
        
        self.fields['dtiniafast'].widget.attrs['required'] = True
        
        self.fields['s2230_evtafasttemp'].widget.attrs['required'] = True

    class Meta:
        model = s2230iniAfastamento
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2230_infoatestado(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2230_infoatestado,self ).__init__(*args,**kwargs)
        
        self.fields['qtddiasafast'].widget.attrs['required'] = True
        self.fields['s2230_iniafastamento'].queryset = s2230iniAfastamento.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2230_iniafastamento'].widget.attrs['required'] = True

    class Meta:
        model = s2230infoAtestado
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2230_emitente(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2230_emitente,self ).__init__(*args,**kwargs)
        
        self.fields['nroc'].widget.attrs['required'] = True
        
        self.fields['ideoc'].widget.attrs['required'] = True
        
        self.fields['nmemit'].widget.attrs['required'] = True
        
        self.fields['s2230_infoatestado'].widget.attrs['required'] = True

    class Meta:
        model = s2230emitente
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2230_infocessao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2230_infocessao,self ).__init__(*args,**kwargs)
        
        self.fields['infonus'].widget.attrs['required'] = True
        
        self.fields['cnpjcess'].widget.attrs['required'] = True
        
        self.fields['s2230_iniafastamento'].widget.attrs['required'] = True

    class Meta:
        model = s2230infoCessao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2230_infomandsind(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2230_infomandsind,self ).__init__(*args,**kwargs)
        
        self.fields['infonusremun'].widget.attrs['required'] = True
        
        self.fields['cnpjsind'].widget.attrs['required'] = True
        
        self.fields['s2230_iniafastamento'].widget.attrs['required'] = True

    class Meta:
        model = s2230infoMandSind
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2230_inforetif(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2230_inforetif,self ).__init__(*args,**kwargs)
        
        self.fields['origretif'].widget.attrs['required'] = True
        
        self.fields['s2230_evtafasttemp'].widget.attrs['required'] = True

    class Meta:
        model = s2230infoRetif
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2230_fimafastamento(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2230_fimafastamento,self ).__init__(*args,**kwargs)
        
        self.fields['dttermafast'].widget.attrs['required'] = True
        
        self.fields['s2230_evtafasttemp'].widget.attrs['required'] = True

    class Meta:
        model = s2230fimAfastamento
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

