# coding: utf-8
from django import forms
from emensageriapro.s2405.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.tabelas.models import Municipios 
from emensageriapro.tabelas.models import eSocialPaises 
from emensageriapro.tabelas.models import eSocialLogradourosTipos 
from emensageriapro.esocial.models import s2405evtCdBenefAlt 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s2405_dependente(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2405_dependente,self ).__init__(*args,**kwargs)
        
        self.fields['depfinsprev'].widget.attrs['required'] = True
        
        self.fields['incfismen'].widget.attrs['required'] = True
        
        self.fields['depirrf'].widget.attrs['required'] = True
        
        self.fields['sexodep'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['nmdep'].widget.attrs['required'] = True
        
        self.fields['tpdep'].widget.attrs['required'] = True
        self.fields['s2405_evtcdbenefalt'].queryset = s2405evtCdBenefAlt.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2405_evtcdbenefalt'].widget.attrs['required'] = True

    class Meta:
        model = s2405dependente
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2405_exterior(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2405_exterior,self ).__init__(*args,**kwargs)
        
        self.fields['nmcid'].widget.attrs['required'] = True
        
        self.fields['nrlograd'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['paisresid'].widget.attrs['required'] = True
        
        self.fields['s2405_endereco'].widget.attrs['required'] = True

    class Meta:
        model = s2405exterior
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2405_brasil(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2405_brasil,self ).__init__(*args,**kwargs)
        
        self.fields['uf'].widget.attrs['required'] = True
        
        self.fields['codmunic'].widget.attrs['required'] = True
        
        self.fields['cep'].widget.attrs['required'] = True
        
        self.fields['nrlograd'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['tplograd'].widget.attrs['required'] = True
        
        self.fields['s2405_endereco'].widget.attrs['required'] = True

    class Meta:
        model = s2405brasil
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2405_endereco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2405_endereco,self ).__init__(*args,**kwargs)
        
        self.fields['s2405_evtcdbenefalt'].widget.attrs['required'] = True

    class Meta:
        model = s2405endereco
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

